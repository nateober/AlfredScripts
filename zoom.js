// Prefer to take configuration from Alfred Environment Variable
// Set here if you can't or don't want to go through the trouble of configuring
var OrgURL = "zoommtg://yourOrg.zoom.us/";
// ----------------------------------------------------------

ObjC.import('stdlib');

var baseURL = $.getenv('zoomURL') ? $.getenv('zoomURL') : OrgURL;

var app = Application.currentApplication();
app.includeStandardAdditions = true;

function parseMeetingID(text) {
    regex = /https:\/\/[a-z0-9.\/]*j\/([0-9].+)/;
    regex2 = /([0-9].+)/;

    match = regex.exec(text);
    if (match !== null) {
        return (match[1]);
    }
	else {
		match = regex2.exec(text);
    		if (match !== null) {
   		     return (match[1]);
    		}
		else {
        		return "";
		}
    }
}

function timeStep(startRangeMin, startRangeMax) {
    var outlook = Application("Microsoft Outlook");
    var calendar = outlook.calendars[1];

    var today = new Date();
    var plusMinutes = new Date();
    var minusMinutes = new Date();

    plusMinutes.setMinutes(today.getMinutes() + startRangeMax);
    minusMinutes.setMinutes(today.getMinutes() - startRangeMin);


    var events = calendar.calendarEvents.whose({
        _and: [{
                "startTime": {
                    _greaterThan: minusMinutes
                }
            },
            {
                "startTime": {
                    _lessThan: plusMinutes
                }
            }
        ]
    });

    return (events);

}

function meetingIDFromEvent(event) {
    var locationID = parseMeetingID(event.location());
    var bodyID = parseMeetingID(event.plainTextContent());

    var outputID = "";

    // prefer body for source of truth
    if (bodyID != "") {
        outputID = bodyID;
    } else if (locationID != "") {
        outputID = locationID;
    }

    return bodyID;
}

function openZoomMeeting(meetingID) {
    if (meetingID != "") {
        var uri = baseURL + "join?action=join&confno=" + meetingID;
        app.openLocation(uri);
    } else {
        app.displayDialog("No meeting found");
    }
}

function fromOutlook() {
    //Prefer earliest meeting, but be prepared to join one that you're incredibly late (or early) for
    var events = timeStep(5, 5);
    if (events.length == 0) {
        events = timeStep(10, 10);
        if (events.length == 0) {
            events = timeStep(15, 15);
            if (events.length == 0) {
                events = timeStep(30, 30);
            }
            if (events.length == 0) {
                events = timeStep(45, 45);
            }
        }
    }

    if (events.length > 0) {

        if (events.length == 1) {
            app.displayDialog("Opening meeting for: '" + events[0].subject() + "'");
            openZoomMeeting(meetingIDFromEvent(events[0]));
        }

        if (events.length > 1) {
            var event;
            var subjects = events().map(m => m.subject());

            var subject = app.chooseFromList(subjects, {
                withPrompt: "Multiple meetings found, select one:",
                defaultItems: subjects[0]
            });

            if (subject == "") {
                app.displayDialog("User cancelled");
                return;
            }

            for (i = 0; i < events().length; i++) {
                if (events[i].subject() == subject) {
                    event = events[i];
                }
            }
            app.displayDialog("Opening meeting for: '" + event.subject() + "'");
            openZoomMeeting(meetingIDFromEvent(event));
        }
    } else {
        app.displayDialog("No meeting found");
    }
}

function run(argv) {
    
    if (argv.length > 0) {
        var query = argv[0];
        openZoomMeeting(parseMeetingID(query));
    } else {
        fromOutlook();
    }

}
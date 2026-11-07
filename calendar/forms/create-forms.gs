/**
 * Builds both Google Forms for the Along the 299 calendar, each with its own private response sheet.
 *
 * How to run (once):
 *  1. Go to script.google.com, click New project, delete the sample code and paste all of this in.
 *  2. Click Run (the function is createAll). Approve the permissions when asked.
 *  3. Open View, then Logs. Copy the links it prints and send them to Claude.
 *
 * Nothing here publishes anything. Responses stay private until you mark a row Approved.
 */
function createAll() {
  var ss = SpreadsheetApp.create('Along the 299 submissions');
  var sub = buildSubmissionForm(ss);
  var fix = buildCorrectionForm();
  Logger.log('SUBMIT FORM (share this):  ' + sub.getPublishedUrl());
  Logger.log('SUBMIT FORM (edit):        ' + sub.getEditUrl());
  Logger.log('CORRECTION FORM (share):   ' + fix.form.getPublishedUrl());
  Logger.log('CORRECTION FORM (edit):    ' + fix.form.getEditUrl());
  Logger.log('CORRECTION "which event" field id: ' + fix.eventFieldId);
  Logger.log('SPREADSHEET:               ' + ss.getUrl());
}

function yesNo_(form, title, help, required) {
  var it = form.addMultipleChoiceItem().setTitle(title).setChoiceValues(['Yes', 'No']).setRequired(!!required);
  if (help) it.setHelpText(help);
  return it;
}

function buildSubmissionForm(ss) {
  var f = FormApp.create('Share an event: What\'s going on along the 299');
  f.setDescription('Event name, date, time and town are always shown. The other details are shown only where you answer Yes. ' +
    'Every event is reviewed before it appears. The events calendar covers Highway 299 and towns within about a 90 minute drive of Willow Creek. ' +
    'Have a flyer? Add a link to it below, or email it to us.');
  f.setCollectEmail(false).setAllowResponseEdits(false).setConfirmationMessage('Thank you. We review every event before it appears on the calendar.');
  // Order matters: it must match the sheet columns B to S used by the Public tab formula.
  f.addTextItem().setTitle('Event name').setRequired(true);                                          // B
  f.addDateItem().setTitle('Date (first day)').setRequired(true);                                    // C
  f.addDateItem().setTitle('Last day (only if it runs more than one day)');                          // D
  f.addTimeItem().setTitle('Start time');                                                            // E
  f.addTimeItem().setTitle('End time');                                                              // F
  f.addListItem().setTitle('Town').setChoiceValues(['Willow Creek', 'Hoopa', 'Burnt Ranch', 'Big Bar', 'Salyer', 'Orleans', 'Junction City', 'Weaverville', 'Hayfork', 'Blue Lake', 'Arcata', 'McKinleyville', 'Eureka', 'Ferndale', 'Fortuna', 'Trinidad', 'Other']).setRequired(true); // G
  f.addTextItem().setTitle('Place name (for example, Studio 299)');                                  // H
  f.addTextItem().setTitle('Street address');                                                        // I
  yesNo_(f, 'Show the street address publicly?', '', true);                                          // J
  f.addTextItem().setTitle('Website or Facebook page');                                              // K
  yesNo_(f, 'Show the website publicly?', '', true);                                                 // L
  f.addParagraphTextItem().setTitle('Short description');                                            // M
  yesNo_(f, 'Is it free?', '', false);                                                               // N
  f.addTextItem().setTitle('Link to your flyer (or email it to us)');                                // O
  yesNo_(f, 'Show the flyer publicly?', '', true);                                                   // P
  f.addTextItem().setTitle('Your name (private)').setHelpText('Only used if we have a question. Never shown.'); // Q
  f.addTextItem().setTitle('Phone (private)').setHelpText('Never shown.');                           // R
  f.addTextItem().setTitle('Email (private)').setHelpText('Never shown.');                           // S
  f.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
  SpreadsheetApp.flush();
  // The destination tab is named after the form. Rename it to the name the formulas expect.
  var tab = ss.getSheets().filter(function (s) { return /Form Responses/.test(s.getName()); })[0] ||
            ss.getSheets()[ss.getSheets().length - 1];
  tab.setName('Form Responses 1');
  tab.getRange('T1').setValue('Approved');
  var pub = ss.getSheetByName('Public') || ss.insertSheet('Public');
  pub.getRange('A1:K1').setValues([['title', 'date', 'end_date', 'start_time', 'end_time', 'town', 'place', 'address', 'website', 'description', 'free']]);
  pub.getRange('A2').setFormula(
    "=IFERROR(FILTER({'Form Responses 1'!B2:B," +
    "ARRAYFORMULA(IF('Form Responses 1'!C2:C=\"\",\"\",TEXT('Form Responses 1'!C2:C,\"yyyy-mm-dd\")))," +
    "ARRAYFORMULA(IF('Form Responses 1'!D2:D=\"\",\"\",TEXT('Form Responses 1'!D2:D,\"yyyy-mm-dd\")))," +
    "ARRAYFORMULA(IF('Form Responses 1'!E2:E=\"\",\"\",TEXT('Form Responses 1'!E2:E,\"HH:mm\")))," +
    "ARRAYFORMULA(IF('Form Responses 1'!F2:F=\"\",\"\",TEXT('Form Responses 1'!F2:F,\"HH:mm\")))," +
    "'Form Responses 1'!G2:G,'Form Responses 1'!H2:H," +
    "ARRAYFORMULA(IF('Form Responses 1'!J2:J=\"Yes\",'Form Responses 1'!I2:I,\"\"))," +
    "ARRAYFORMULA(IF('Form Responses 1'!L2:L=\"Yes\",'Form Responses 1'!K2:K,\"\"))," +
    "'Form Responses 1'!M2:M,'Form Responses 1'!N2:N}," +
    "'Form Responses 1'!T2:T=\"Yes\"),\"\")");
  return f;
}

function buildCorrectionForm() {
  var f = FormApp.create('Report a mistake: What\'s going on along the 299');
  f.setDescription('Spot something wrong on the calendar? Tell us what it should say. Nothing changes until we check it, ' +
    'and nothing you send here is shown publicly. A link to a flyer, page or post that shows the right details helps a lot.');
  f.setCollectEmail(false).setAllowResponseEdits(false).setConfirmationMessage('Thank you. We will check it and fix the calendar.');
  var which = f.addTextItem().setTitle('Which event?').setHelpText('The event name, and the date if you know it.').setRequired(true);
  f.addCheckboxItem().setTitle('What is wrong?').setChoiceValues(['Date', 'Time', 'Place or address', 'Town', 'Description', 'The event was canceled or moved', 'It should not be listed', 'Something else']).setRequired(true);
  f.addParagraphTextItem().setTitle('What should it say?').setRequired(true);
  f.addTextItem().setTitle('Link that shows the right details (flyer, website, post)');
  f.addTextItem().setTitle('Your name (private, optional)');
  f.addTextItem().setTitle('Email or phone (private, optional)').setHelpText('Only used if we have a question. Never shown.');
  var cs = SpreadsheetApp.create('Along the 299 corrections');
  f.setDestination(FormApp.DestinationType.SPREADSHEET, cs.getId());
  // Entry id of "Which event?" so the calendar can fill it in from each event card.
  var resp = f.createResponse().withItemResponse(which.createResponse('X'));
  var m = /entry\.(\d+)=X/.exec(resp.toPrefilledUrl());
  return { form: f, eventFieldId: m ? m[1] : 'not found, see the SETUP note' };
}

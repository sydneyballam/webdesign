/**
 * Adds three questions to the live "Share an event" form and updates the Public tab to match.
 *   - Hosted by (business or group)
 *   - Cost (for example, $7 or kids free)
 *   - Town not listed? Type it here
 *
 * How to run (once):
 *  1. Go to script.google.com, click New project, delete the sample code and paste all of this in.
 *  2. Click Run (function addFields). Approve the permissions when asked.
 *  3. Open View, then Logs and send Claude the three "ENTRY" lines it prints.
 *
 * It finds the form by its title, so you don't need any links. Running it twice is safe: questions that
 * already exist are not added again. The Public tab is rebuilt by looking up each column by its heading,
 * so it does not matter where Google put the new columns. Nothing is published that wasn't already.
 */
var FORM_TITLE = "Share an event: What's going on along the 299";

function addFields() {
  var files = DriveApp.getFilesByName(FORM_TITLE);
  if (!files.hasNext()) throw new Error('Could not find a form titled: ' + FORM_TITLE);
  var form = FormApp.openById(files.next().getId());

  var wanted = [
    {key: 'host', title: 'Hosted by (business or group)', help: 'Shown on the calendar as "From ..."'},
    {key: 'cost', title: 'Cost (for example, $7, or kids free)', help: 'Leave blank if free. People like to know before they go.'},
    {key: 'other', title: 'Town not listed? Type it here', help: 'Only if you chose Other above.'}
  ];
  var items = form.getItems();
  wanted.forEach(function (w) {
    var item = items.filter(function (i) { return i.getTitle() === w.title; })[0];
    if (!item) item = form.addTextItem().setTitle(w.title).setHelpText(w.help);
    // The id the web page needs is found by pre-filling one answer and reading it back.
    var url = form.createResponse().withItemResponse(item.asTextItem().createResponse('X')).toPrefilledUrl();
    var m = url.match(/entry\.(\d+)=X/);
    Logger.log('ENTRY ' + w.key + ' = ' + (m ? m[1] : 'not found'));
  });
  SpreadsheetApp.flush();
  rebuildPublic_(SpreadsheetApp.openById(form.getDestinationId()));
  Logger.log('Done. Public tab rebuilt.');
}

function letter_(n) { var s = ''; while (n > 0) { var r = (n - 1) % 26; s = String.fromCharCode(65 + r) + s; n = Math.floor((n - 1) / 26); } return s; }

function rebuildPublic_(ss) {
  var src = ss.getSheetByName('Form Responses 1');
  if (!src) throw new Error('No tab named "Form Responses 1".');
  var heads = src.getRange(1, 1, 1, src.getLastColumn()).getValues()[0];
  function col(re, not) {
    for (var i = 0; i < heads.length; i++) if (re.test(heads[i]) && !(not && not.test(heads[i]))) return letter_(i + 1);
    throw new Error('No column matching ' + re);
  }
  var C = {
    title: col(/^Event name/i), date: col(/^Date \(first/i), end: col(/^Last day/i),
    start: col(/^Start time/i), endt: col(/^End time/i),
    town: col(/town|where this event/i, /not listed/i), other: col(/not listed/i),
    place: col(/^Place name/i), addr: col(/^Street address/i), showAddr: col(/^Show the street/i),
    site: col(/^Website/i), showSite: col(/^Show the website/i), desc: col(/^Short description/i),
    free: col(/^Is it free/i), cost: col(/^Cost/i), host: col(/^Hosted by/i), ok: col(/^Approved$/i)
  };
  var pub = ss.getSheetByName('Public') || ss.insertSheet('Public');
  pub.clear();
  pub.getRange(1, 1, 1, 13).setValues([['title', 'date', 'end_date', 'start_time', 'end_time', 'town', 'place', 'address', 'website', 'description', 'free', 'cost', 'source']]);
  var R = "'Form Responses 1'!", rows = [];
  for (var r = 2; r <= 500; r++) {
    var c = function (k) { return R + C[k] + r; };
    var show = function (expr) { return '=IF(' + c('ok') + '=TRUE,' + expr + ',"")'; };
    rows.push([
      show(c('title')),
      show('IF(' + c('date') + '="","",TEXT(' + c('date') + ',"yyyy-mm-dd"))'),
      show('IF(' + c('end') + '="","",TEXT(' + c('end') + ',"yyyy-mm-dd"))'),
      show('IF(' + c('start') + '="","",TEXT(' + c('start') + ',"HH:mm"))'),
      show('IF(' + c('endt') + '="","",TEXT(' + c('endt') + ',"HH:mm"))'),
      show('IF(AND(' + c('town') + '="Other",' + c('other') + '<>""),PROPER(TRIM(' + c('other') + ')),' + c('town') + ')'),
      show(c('place')),
      show('IF(' + c('showAddr') + '="Yes",' + c('addr') + ',"")'),
      show('IF(' + c('showSite') + '="Yes",' + c('site') + ',"")'),
      show(c('desc')),
      show(c('free')),
      show(c('cost')),
      show(c('host'))
    ]);
  }
  pub.getRange(2, 1, rows.length, 13).setFormulas(rows);
  pub.setFrozenRows(1);
}

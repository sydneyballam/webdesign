/**
 * One time fix for the sheet you already have. Run fixSheet once:
 * it turns the Approved column into tick boxes and rebuilds the Public tab with simple per row formulas.
 */
function fixSheet() {
  var ss = SpreadsheetApp.openById('1SFnytzRpELHUcn8uPpTINTYp2IuGxX3_d1Zpi2p5nrE');
  var tab = ss.getSheetByName('Form Responses 1');
  tab.getRange('T1').setValue('Approved');
  tab.getRange('T2:T500').insertCheckboxes();
  tab.setFrozenRows(1);
  buildPublicTab_(ss);
}

function buildPublicTab_(ss) {
  // One simple formula per row (rows 2 to 500). A row shows up only when its Approved box is ticked.
  var pub = ss.getSheetByName('Public') || ss.insertSheet('Public');
  pub.clear();
  pub.getRange('A1:K1').setValues([['title', 'date', 'end_date', 'start_time', 'end_time', 'town', 'place', 'address', 'website', 'description', 'free']]);
  var R = "'Form Responses 1'!";
  var rows = [];
  for (var r = 2; r <= 500; r++) {
    var ok = R + 'T' + r + '=TRUE';
    var c = function (col) { return R + col + r; };
    var show = function (expr) { return '=IF(' + ok + ',' + expr + ',"")'; };
    rows.push([
      show(c('B')),
      show('IF(' + c('C') + '="","",TEXT(' + c('C') + ',"yyyy-mm-dd"))'),
      show('IF(' + c('D') + '="","",TEXT(' + c('D') + ',"yyyy-mm-dd"))'),
      show('IF(' + c('E') + '="","",TEXT(' + c('E') + ',"HH:mm"))'),
      show('IF(' + c('F') + '="","",TEXT(' + c('F') + ',"HH:mm"))'),
      show(c('G')),
      show(c('H')),
      show('IF(' + c('J') + '="Yes",' + c('I') + ',"")'),
      show('IF(' + c('L') + '="Yes",' + c('K') + ',"")'),
      show(c('M')),
      show(c('N'))
    ]);
  }
  pub.getRange(2, 1, rows.length, 11).setFormulas(rows);
  pub.setFrozenRows(1);
}

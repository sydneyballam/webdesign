/**
 * One time fix for the sheet you already have: turns the Approved column into tick boxes
 * and makes the Public tab publish only the rows that are ticked.
 * Paste this into the same Apps Script project (a new file or below the other code), then Run fixSheet.
 */
function fixSheet() {
  var ss = SpreadsheetApp.openById('1SFnytzRpELHUcn8uPpTINTYp2IuGxX3_d1Zpi2p5nrE');
  var tab = ss.getSheetByName('Form Responses 1');
  tab.getRange('T1').setValue('Approved');
  tab.getRange('T2:T1000').insertCheckboxes();
  tab.setFrozenRows(1);
  var pub = ss.getSheetByName('Public');
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
    "'Form Responses 1'!T2:T=TRUE),\"\")");
}

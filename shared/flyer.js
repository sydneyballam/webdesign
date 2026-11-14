/* Flyer maker shared by the Event Desk and the calendar. Flyer.draw(canvas, details, scale) paints a flyer. */
(function(root){
var X=null;
function pd(s){var p=s.split('-');return new Date(+p[0],p[1]-1,+p[2])}
function t12(t){if(!t)return'';var p=t.split(':'),h=+p[0],m=p[1],ap=h>=12?'PM':'AM';h=h%12||12;return h+(m==='00'?'':':'+m)+' '+ap}
function timeLine(s,e){var a=t12(s),b=t12(e);return a&&b?a+' to '+b:a}
function lum(h){var n=parseInt(h.slice(1),16),r=n>>16,g=n>>8&255,b=n&255;return(.299*r+.587*g+.114*b)/255}
function onCol(h){return lum(h)>.6?'#151A3C':'#FFFFFF'}
function wrap(t,mw,font){X.font=font;var w=t.split(/\s+/),l=[],cur='';w.forEach(function(s){var n=cur?cur+' '+s:s;if(X.measureText(n).width>mw&&cur){l.push(cur);cur=s}else cur=n});if(cur)l.push(cur);return l}
function fit(t,mw,maxPx,minPx,weight,maxLines){var px=maxPx,ls;for(;px>=minPx;px-=4){ls=wrap(t,mw,weight+' '+px+'px '+FFAM);if(ls.length<=maxLines)break}return{px:px,ls:ls,font:weight+' '+px+'px '+FFAM}}
function rr(a,b,w,h,r){X.beginPath();X.moveTo(a+r,b);X.arcTo(a+w,b,a+w,b+h,r);X.arcTo(a+w,b+h,a,b+h,r);X.arcTo(a,b+h,a,b,r);X.arcTo(a,b,a+w,b,r);X.closePath()}
function lines(f,xx,yy,col,lh){X.fillStyle=col;X.font=f.font;f.ls.forEach(function(s,i){X.fillText(s,xx,yy+i*(f.px*lh))});return yy+f.ls.length*f.px*lh}

var FONTS={modern:'system-ui,Helvetica,Arial,sans-serif',friendly:"'Trebuchet MS','Avenir Next','Segoe UI',system-ui,sans-serif",classic:"Georgia,'Times New Roman',Times,serif",tall:"Impact,'Haettenschweiler','Arial Narrow Bold','Arial Narrow',sans-serif",hand:"'Segoe Print','Bradley Hand','Chalkboard SE','Comic Sans MS','Marker Felt',cursive",type:"'Courier New',Courier,monospace"};
var FFAM=FONTS.modern;
function shade(h,f){var n=parseInt(h.slice(1),16),r=n>>16,g=n>>8&255,b=n&255;r=Math.round(r*f);g=Math.round(g*f);b=Math.round(b*f);return'rgb('+r+','+g+','+b+')'}
function draw(cv,o,scale){
  var x=cv.getContext('2d');scale=scale||1;cv.width=Math.round(1080*scale);cv.height=Math.round(1350*scale);x.setTransform(scale,0,0,scale,0,0);X=x;
  FFAM=FONTS[o.font]||FONTS.modern;
  var st=o.style||'bold',col=o.color||'#FF4F8B',on=onCol(col),W=1080,H=1350,M=80;
  x.clearRect(0,0,W,H);x.textBaseline='top';x.textAlign='left';
  var title=o.title||'Your event',biz=o.biz||'',tm=timeLine(o.start,o.end),place=o.place||'',price=o.price||'',desc=o.desc||'';
  var bg,fg,sub,inv=(st==='bold'||st==='gradient');
  if(st==='bold'){bg=col;fg=on;sub=on}
  else if(st==='gradient'){bg=shade(col,.45);fg=lum(col)>.75?'#151A3C':'#FFFFFF';sub=fg;on=fg}
  else if(st==='frame'){bg='#FFF8EC';fg='#151A3C';sub='#5A6088'}
  else if(st==='poster'){bg='#151A3C';fg='#FFFFFF';sub='#C9CFF5'}
  else{bg='#FFFFFF';fg='#151A3C';sub='#5A6088'}
  var tc=o.tcolor||'auto';if(tc!=='auto'){fg=tc;sub=tc}
  var bgl=st==='gradient'?lum(col)*.6:(bg.charAt(0)==='#'?lum(bg):.5);var cd=Math.abs(bgl-lum(fg));var low=cd<.35;
  if(st==='gradient'){var gr=x.createLinearGradient(0,0,0,H);gr.addColorStop(0,col);gr.addColorStop(1,bg);x.fillStyle=gr}else x.fillStyle=bg;
  x.fillRect(0,0,W,H);
  if(st==='gradient'){x.globalAlpha=.14;x.fillStyle='#fff';x.beginPath();x.arc(W*.85,H*.12,330,0,7);x.fill();x.beginPath();x.arc(W*.1,H*.9,260,0,7);x.fill();x.globalAlpha=1}
  if(st==='frame'){x.strokeStyle=col;x.lineWidth=14;x.strokeRect(34,34,W-68,H-68);x.strokeStyle='#151A3C';x.lineWidth=3;x.strokeRect(66,66,W-132,H-132)}
  if(st==='stripes'){x.fillStyle=col;x.beginPath();x.moveTo(0,0);x.lineTo(W,0);x.lineTo(W,120);x.lineTo(0,235);x.closePath();x.fill();x.beginPath();x.moveTo(0,H);x.lineTo(W,H);x.lineTo(W,H-235);x.lineTo(0,H-120);x.closePath();x.fill();x.globalAlpha=.35;x.fillStyle='#fff';x.beginPath();x.moveTo(0,250);x.lineTo(W,135);x.lineTo(W,160);x.lineTo(0,275);x.closePath();x.fill();x.globalAlpha=1}
  if(st==='poster'){x.fillStyle=col;x.fillRect(0,0,W,40);x.fillRect(0,H-40,W,40);x.fillStyle=col;x.beginPath();x.arc(W-60,420,260,0,7);x.globalAlpha=.18;x.fill();x.globalAlpha=1}
  if(st==='clean'){x.fillStyle=col;x.fillRect(0,0,34,H);x.fillRect(0,H-26,W,26)}
  var L=(st==='clean'||st==='frame')?M+30:M,mw=W-L-(st==='frame'?M+30:M),cx=L+mw/2;
  x.font='700 34px '+FFAM;x.fillStyle=st==='poster'?col:(st==='stripes'?onCol(col):sub);
  x.textAlign='center';x.fillText((biz||'').toUpperCase().slice(0,40),cx,st==='poster'?90:(st==='stripes'?58:(st==='frame'?100:70)));x.textAlign='left';
  // big date badge
  var y=st==='poster'?170:(st==='stripes'?285:(st==='frame'?170:150));
  if(o.date){var dd=pd(o.date);var mon=dd.toLocaleDateString('en-US',{month:'short'}).toUpperCase(),dn=dd.getDate();
    var bw=190,bh=210,wk=dd.toLocaleDateString('en-US',{weekday:'long'});
    if(o.date2&&o.date2>o.date){var d2=pd(o.date2);wk=dd.toLocaleDateString('en-US',{weekday:'short'})+' to '+d2.toLocaleDateString('en-US',{weekday:'short'})}
    x.font='800 46px '+FFAM;var iw=x.measureText(wk).width;x.font='600 38px '+FFAM;iw=Math.max(iw,x.measureText(tm).width);if(price){x.font='800 36px '+FFAM;iw=Math.max(iw,x.measureText(price).width+44)}
    var L=cx-(bw+36+iw)/2;rr(L,y,bw,bh,28);x.fillStyle=inv?on:col;x.fill();
    var bc=inv?col:on;x.fillStyle=bc;x.font='800 44px '+FFAM;x.textAlign='center';x.fillText(mon,L+bw/2,y+22);x.font='900 112px '+FFAM;x.fillText(String(dn),L+bw/2,y+70);x.textAlign='left';
    x.font='800 46px '+FFAM;x.fillStyle=sub;x.fillText(wk,L+bw+36,y+20);x.font='600 38px '+FFAM;x.fillText(tm,L+bw+36,y+82);
    if(price){x.font='800 36px '+FFAM;var pw=x.measureText(price).width+44;rr(L+bw+36,y+144,pw,56,28);x.fillStyle=inv?on:col;x.fill();x.fillStyle=inv?col:on;x.fillText(price,L+bw+58,y+152)}
    y+=bh+60}
  var site=(o.site||'').replace(/^https?:\/\/(www\.)?/i,'').replace(/\/$/,'');var fy=H-(st==='stripes'?(site?410:350):(st==='frame'?(site?340:280):(site?310:250))), avail=fy-40-y, FF=FFAM, best=null;
  for(var tp=150;tp>=60&&!best;tp-=6){
    var tf='900 '+tp+'px '+FF, tl=wrap(title,mw,tf); if(tl.length>4&&tp>60)continue;
    var th=tl.length*tp*1.04+34, rem=avail-th;
    if(!desc){if(rem>=0)best={tp:tp,tl:tl,tf:tf,dl:null};continue}
    for(var dp=44;dp>=28;dp-=2){var df2='500 '+dp+'px '+FF,dl=wrap(desc,mw,df2);if(dl.length*dp*1.35<=rem){best={tp:tp,tl:tl,tf:tf,dp:dp,df:df2,dl:dl};break}}
  }
  if(!best){ // too much text: smallest sizes, shorten the description with ...
    var tp2=60,tf2='900 60px '+FF,tl2=wrap(title,mw,tf2).slice(0,3),rem2=avail-tl2.length*60*1.04-34,dp2=28,df3='500 28px '+FF,dl3=wrap(desc,mw,df3),mx=Math.max(1,Math.floor(rem2/(28*1.35)));
    if(dl3.length>mx){dl3=dl3.slice(0,mx);var last=dl3[mx-1];x.font=df3;while(last.length>1&&x.measureText(last+'\u2026').width>mw)last=last.slice(0,-1);dl3[mx-1]=last.replace(/[\s,.;:]+$/,'')+'\u2026'}
    best={tp:tp2,tl:tl2,tf:tf2,dp:dp2,df:df3,dl:dl3};
  }
  x.textAlign='center';
  y=lines({px:best.tp,ls:best.tl,font:best.tf},cx,y,fg,1.04)+34;
  if(best.dl)lines({px:best.dp,ls:best.dl,font:best.df},cx,y,sub,1.35);
  // footer
  x.fillStyle=inv?on:col;x.fillRect(cx-50,fy,100,8);
  x.font='700 42px '+FFAM;x.fillStyle=fg;
  var pf=fit(place,mw,48,32,'800',2),py=lines(pf,cx,fy+32,fg,1.2);
  if(site){var sf=fit(site,mw,38,24,'700',1);x.fillStyle=inv?on:col;if(lum(col)>.8&&!inv&&st!=='poster')x.fillStyle=fg;lines(sf,cx,py+8,x.fillStyle,1.2)}
  x.font='600 30px '+FFAM;x.fillStyle=st==='stripes'?onCol(col):sub;x.fillText('Part of What\u2019s Going On Along the 299',cx,st==='stripes'?H-62:(st==='frame'?H-112:H-90));x.textAlign='left';
  return{lowContrast:low};
}

var STYLES=['bold','poster','clean','gradient','frame','stripes'],FONTKEYS=['modern','friendly','classic','tall','hand','type'],COLORS=['#FF4F8B','#FFC93C','#2FBF8F','#3B82F6','#7B6CFF','#FF8A3D','#E5383B','#14B8A6','#1E3A8A','#7A3E1D'];
function hash(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)}return h>>>0}
/* The same seed always gives the same look, so a card never changes between visits. */
function pick(seed){var h=hash(String(seed));return{style:STYLES[h%STYLES.length],font:FONTKEYS[(h>>>5)%FONTKEYS.length],color:COLORS[(h>>>11)%COLORS.length]}}
root.Flyer={draw:draw,pick:pick,fonts:FONTS};
})(window);

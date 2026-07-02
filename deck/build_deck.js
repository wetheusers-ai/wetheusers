const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const FA = require("react-icons/fa");
const PATH = require("path");
const ASSET = (n)=>PATH.join(__dirname,"assets",n);

// ---------- palette ----------
const NAVY="1B2A4A", NAVY_DEEP="13203B", NAVY_CARD="243457";
const GOLD="B08D3A", GOLD_BR="C9A24B", IVORY="F1ECDD", SLATE="9AA6BC";
const PARCH="F4F1EA", PARCH_CARD="FBF8F0", INK="1B2A4A", BODY="3B4663", MUTED="76716A";
const DISP="Cambria", SANS="Calibri";
const URL="wetheusers.ai", URLU="WETHEUSERS.AI";
const sh=(o={})=>Object.assign({type:"outer",color:"000000",blur:9,offset:4,angle:90,opacity:0.30},o);

async function icon(name,hex,size=320){
  const svg=ReactDOMServer.renderToStaticMarkup(React.createElement(FA[name],{color:"#"+hex,size:String(size)}));
  const png=await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64,"+png.toString("base64");
}

(async()=>{
  const I={};
  for(const [n,c] of [
    ["FaUserShield",GOLD_BR],["FaRecycle",GOLD_BR],["FaBalanceScale",GOLD_BR],
    ["FaUser",INK],["FaUsers",INK],["FaGlobeAmericas",INK],
    ["FaHandHoldingUsd",GOLD_BR],["FaUnlockAlt",GOLD_BR],["FaCodeBranch",GOLD_BR],
    ["FaScroll",INK],["FaBookOpen",INK],["FaFeatherAlt",INK],
  ]) I[n+"_"+c]=await icon(n,c);

  const pres=new pptxgen();
  pres.defineLayout({name:"W16x9",width:10,height:5.625}); pres.layout="W16x9";
  pres.author="We the Users"; pres.title="We the Users — A Declaration of Internet Independence";
  const W=10,H=5.625,M=0.62;

  function chrome(s,n,dark){
    s.addShape(pres.shapes.RECTANGLE,{x:M,y:0.40,w:0.12,h:0.12,rotate:45,fill:{color:GOLD},line:{type:"none"}});
    s.addText("WE THE USERS",{x:M+0.24,y:0.30,w:4,h:0.32,margin:0,fontFace:SANS,fontSize:11.5,bold:true,charSpacing:3,color:dark?IVORY:INK,valign:"middle"});
    s.addText(String(n),{x:W-1.1,y:H-0.52,w:0.5,h:0.3,margin:0,align:"right",fontFace:SANS,fontSize:10,color:dark?SLATE:MUTED});
  }
  const eyebrow=(s,t,x,y,w,dark)=>s.addText(t.toUpperCase(),{x,y,w,h:0.3,margin:0,fontFace:SANS,fontSize:12.5,bold:true,charSpacing:3.2,color:dark?GOLD_BR:GOLD});

  // 1 — COVER
  let s=pres.addSlide(); s.background={color:NAVY_DEEP};
  s.addShape(pres.shapes.RECTANGLE,{x:(W-0.16)/2,y:1.18,w:0.16,h:0.16,rotate:45,fill:{color:GOLD},line:{type:"none"}});
  s.addText("A DECLARATION OF INTERNET INDEPENDENCE",{x:0,y:1.62,w:W,h:0.34,align:"center",fontFace:SANS,fontSize:13.5,bold:true,charSpacing:4,color:GOLD_BR});
  s.addText("We the Users",{x:0,y:2.05,w:W,h:1.25,align:"center",fontFace:DISP,bold:true,fontSize:76,color:IVORY,shadow:sh({blur:12,offset:6,opacity:0.38})});
  s.addText("An internet owned by the people who use it.",{x:0,y:3.42,w:W,h:0.45,align:"center",fontFace:DISP,italic:true,fontSize:21,color:"D8D2C2"});
  s.addText("JULY 2, 2026",{x:0,y:4.55,w:W,h:0.34,align:"center",fontFace:SANS,fontSize:14,bold:true,charSpacing:5,color:IVORY});
  s.addNotes("Open here. The 250th anniversary of the vote for American independence, reclaimed for the internet. One breath, then move.");

  // 2 — YOU CAST A SHADOW
  s=pres.addSlide(); s.background={color:NAVY}; chrome(s,2,true);
  eyebrow(s,"The shadow you cast",M,1.35,8,true);
  s.addText("You cast a shadow\nyou cannot see.",{x:M,y:1.78,w:8.8,h:1.7,margin:0,fontFace:DISP,bold:true,fontSize:48,color:IVORY,lineSpacingMultiple:1.0,shadow:sh()});
  s.addText("Every click, message, route, and purchase is a trace of a real life. Yours. Gathered and kept, they become a detailed, searchable record of a single person: your digital shadow.",
    {x:M,y:3.72,w:8.4,h:1.2,margin:0,fontFace:SANS,fontSize:17,color:"CFD5E0",lineSpacingMultiple:1.16});
  s.addNotes("Make it personal. The shadow is not an abstraction, it is them. Land 'your digital shadow' as the name for it.");

  // 3 — SOMEONE ELSE OWNS IT
  s=pres.addSlide(); s.background={color:PARCH}; chrome(s,3,false);
  eyebrow(s,"The bargain we never agreed to",M,1.35,8,false);
  s.addText([
    {text:"We the Users have become",options:{color:INK,breakLine:true}},
    {text:"we the used.",options:{color:GOLD,italic:true}},
  ],{x:M,y:1.74,w:9,h:1.62,margin:0,fontFace:DISP,bold:true,fontSize:46,lineSpacingMultiple:1.0,shadow:sh({color:"B9B097",opacity:0.4,blur:7,offset:3})});
  s.addText("Your digital shadow is taken without leave, and the value built on it, above all the new artificial intelligence, flows to the few who hold it.",
    {x:M,y:3.55,w:5.55,h:1.4,margin:0,fontFace:SANS,fontSize:16.5,color:BODY,lineSpacingMultiple:1.18});
  const ow=(x,big,lab)=>{ s.addShape(pres.shapes.ROUNDED_RECTANGLE,{x,y:3.55,w:1.75,h:1.35,rectRadius:0.08,fill:{color:PARCH_CARD},line:{type:"none"},shadow:sh({color:"9A927C",blur:7,offset:2,opacity:0.22})});
    s.addText(big,{x,y:3.74,w:1.75,h:0.6,align:"center",margin:0,fontFace:DISP,bold:true,fontSize:34,color:GOLD});
    s.addText(lab,{x,y:4.36,w:1.75,h:0.45,align:"center",margin:0,fontFace:SANS,fontSize:12.5,bold:true,charSpacing:1,color:INK}); };
  ow(6.45,"No","SAY"); ow(8.30,"No","SHARE");
  s.addNotes("The indictment, in four words: We the Users have become we the used. Let the pun land, then the proof, your shadow taken and the value kept: no say, no share.");

  // 4 — THE PROBLEM, IN ONE PICTURE
  s=pres.addSlide(); s.background={color:NAVY}; chrome(s,4,true);
  eyebrow(s,"The problem",M,0.82,8,true);
  (function(img){ const hImg=3.96, wImg=hImg*1448/1256, x=(W-wImg)/2, y=1.24;
    s.addShape(pres.shapes.RECTANGLE,{x:x-0.06,y:y-0.06,w:wImg+0.12,h:hImg+0.12,fill:{color:IVORY},line:{type:"none"}});
    s.addImage({path:img,x,y,w:wImg,h:hImg,shadow:sh({blur:10,offset:5,opacity:0.42})});
    s.addShape(pres.shapes.RECTANGLE,{x:x-0.06,y:y-0.06,w:wImg+0.12,h:hImg+0.12,fill:{type:"none"},line:{color:GOLD,width:1}});
  })(ASSET("cartoon-used.png"));
  s.addNotes("The indictment as one picture: your data fills the pipe, the platform drinks, and only a trickle reaches the person who made it. Let it land.");

  // 4 — NO ONE CHOSE THIS
  s=pres.addSlide(); s.background={color:NAVY}; chrome(s,5,true);
  eyebrow(s,"It was a choice",M,1.45,8,true);
  s.addText("No one chose this.",{x:M,y:1.9,w:9,h:1.0,margin:0,fontFace:DISP,bold:true,fontSize:54,color:IVORY,shadow:sh()});
  s.addText([
    {text:"We click 'I agree.' But we don't — not because we agree, but because there is no other button.",options:{breakLine:true,color:"CFD5E0"}},
    {text:"",options:{breakLine:true,fontSize:8}},
    {text:"It was built. And it can be built differently.",options:{color:GOLD_BR,bold:true}},
  ],{x:M,y:3.25,w:8.6,h:1.6,margin:0,fontFace:SANS,fontSize:19,lineSpacingMultiple:1.18});
  s.addNotes("The hinge of the whole pitch. The consent is a fiction: we click agree, but we never chose this. It was authored, not natural. Slow down on the last line.");

  // 5 — WE HAVE DONE THIS BEFORE (physical 1776 -> digital 2026)
  s=pres.addSlide(); s.background={color:PARCH}; chrome(s,6,false);
  eyebrow(s,"A 250-year-old idea",M,1.35,8,false);
  s.addText("We have done this before.",{x:M,y:1.74,w:9,h:0.9,margin:0,fontFace:DISP,bold:true,fontSize:42,color:INK});
  s.addText("Settled by reflection and choice, not by accident and force.",{x:M,y:2.7,w:9,h:0.4,margin:0,fontFace:DISP,italic:true,fontSize:18,color:GOLD});
  const yr=4.05;
  s.addShape(pres.shapes.LINE,{x:M+0.15,y:yr,w:8.5,h:0,line:{color:GOLD,width:1.5}});
  const node=(x,year,lead,txt)=>{ s.addShape(pres.shapes.OVAL,{x:x-0.1,y:yr-0.1,w:0.2,h:0.2,fill:{color:GOLD},line:{type:"none"}});
    s.addText(year,{x:x-1.3,y:yr-0.82,w:2.6,h:0.5,align:"center",margin:0,fontFace:DISP,bold:true,fontSize:30,color:INK});
    s.addText([{text:lead,options:{bold:true,color:INK}},{text:txt,options:{color:BODY}}],
      {x:x-1.85,y:yr+0.16,w:3.7,h:0.78,align:"center",margin:0,fontFace:SANS,fontSize:13,lineSpacingMultiple:1.08}); };
  node(M+1.7,"1776","The physical world ","declared independence from a power that ruled it without its consent.");
  node(W-M-1.7,"2026","The digital world ","declares its own, exactly 250 years on.");
  s.addNotes("Borrow the legitimacy of 1776. The physical world threw off rule without consent; the digital world now does the same. Hamilton's framing: government by reflection and choice.");

  // 6 — THE VISION
  s=pres.addSlide(); s.background={color:NAVY}; chrome(s,7,true);
  eyebrow(s,"The vision",M,1.28,8,true);
  s.addText("An internet owned by the people who use it.",{x:M,y:1.66,w:8.9,h:0.95,margin:0,fontFace:DISP,bold:true,fontSize:33,color:IVORY,lineSpacingMultiple:0.98,shadow:sh({opacity:0.26})});
  const vcard=(x,ic,head,body)=>{ const w=2.74;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE,{x,y:2.95,w,h:2.05,rectRadius:0.08,fill:{color:NAVY_CARD},line:{type:"none"},shadow:sh({blur:8,offset:3,opacity:0.34})});
    s.addImage({data:ic,x:x+0.26,y:3.16,w:0.52,h:0.52});
    s.addText(head,{x:x+0.26,y:3.78,w:w-0.46,h:0.54,margin:0,valign:"top",fontFace:DISP,bold:true,fontSize:16,color:GOLD_BR,lineSpacingMultiple:0.95});
    s.addText(body,{x:x+0.26,y:4.36,w:w-0.46,h:0.6,margin:0,fontFace:SANS,fontSize:12,color:"CFD5E0",lineSpacingMultiple:1.05}); };
  vcard(M,      I["FaUserShield_"+GOLD_BR],"Your data is yours","Held by you, shared on your terms, and yours to carry away.");
  vcard(M+2.92, I["FaRecycle_"+GOLD_BR],   "Rewards flow back","The value the network creates returns to the people who make it.");
  vcard(M+5.84, I["FaBalanceScale_"+GOLD_BR],"No one above the rest","Returns are capped. No founder, engineer, or investor reigns.");
  s.addNotes("The promise, in three. Ownership, fair return, and the anti-oligarchy rule that keeps it honest.");

  // 8 — THE REMEDY, IN ONE PICTURE
  s=pres.addSlide(); s.background={color:NAVY}; chrome(s,8,true);
  eyebrow(s,"The remedy",M,0.82,8,true);
  (function(img){ const hImg=3.96, wImg=hImg*1448/1256, x=(W-wImg)/2, y=1.24;
    s.addShape(pres.shapes.RECTANGLE,{x:x-0.06,y:y-0.06,w:wImg+0.12,h:hImg+0.12,fill:{color:IVORY},line:{type:"none"}});
    s.addImage({path:img,x,y,w:wImg,h:hImg,shadow:sh({blur:10,offset:5,opacity:0.42})});
    s.addShape(pres.shapes.RECTANGLE,{x:x-0.06,y:y-0.06,w:wImg+0.12,h:hImg+0.12,fill:{type:"none"},line:{color:GOLD,width:1}});
  })(ASSET("cartoon-users.png"));
  s.addNotes("The same shadow, the same pipe, but the rewards now branch out to everyone and the hoarder's chair sits empty. This is what 'owned by the people who use it' looks like.");

  // 7 — THREE TIERS
  s=pres.addSlide(); s.background={color:PARCH}; chrome(s,9,false);
  eyebrow(s,"How it is built",M,1.28,8,false);
  s.addText("Power, divided three ways.",{x:M,y:1.62,w:9,h:0.85,margin:0,fontFace:DISP,bold:true,fontSize:36,color:INK});
  s.addText("Federalism, so that no part can rule the rest.",{x:M,y:2.4,w:9,h:0.34,margin:0,fontFace:DISP,italic:true,fontSize:16,color:GOLD});
  const tier=(y,ic,head,body)=>{ s.addShape(pres.shapes.ROUNDED_RECTANGLE,{x:M,y,w:8.2,h:0.86,rectRadius:0.07,fill:{color:PARCH_CARD},line:{type:"none"},shadow:sh({color:"9A927C",blur:6,offset:2,opacity:0.20})});
    s.addImage({data:ic,x:M+0.28,y:y+0.21,w:0.44,h:0.44});
    s.addText(head,{x:M+0.95,y,w:3.0,h:0.86,margin:0,valign:"middle",fontFace:DISP,bold:true,fontSize:18,color:INK});
    s.addText(body,{x:M+4.1,y,w:3.95,h:0.86,margin:0,valign:"middle",fontFace:SANS,fontSize:13.5,color:BODY,lineSpacingMultiple:1.08}); };
  tier(2.72,I["FaUser_"+INK],        "Individuals","Each person, holding their own shadow and identity.");
  tier(3.70,I["FaUsers_"+INK],       "Communities","Where people gather and set the rules of their own house.");
  tier(4.68,I["FaGlobeAmericas_"+INK],"The Commonwealth","A thin, shared floor, deliberately the least powerful tier.");
  s.addNotes("Keep this light for a public room. The point is not the org chart, it is that power is split on purpose, like a citizen, a state, and a federal government.");

  // 8 — GUARDRAILS
  s=pres.addSlide(); s.background={color:NAVY}; chrome(s,10,true);
  eyebrow(s,"What keeps it honest",M,1.28,8,true);
  s.addText("Three guardrails against\nthe old internet's return.",{x:M,y:1.62,w:9,h:1.0,margin:0,fontFace:DISP,bold:true,fontSize:31,color:IVORY,lineSpacingMultiple:0.98,shadow:sh({opacity:0.26})});
  const gcard=(x,ic,head,body)=>{ const w=2.74;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE,{x,y:3.0,w,h:2.05,rectRadius:0.08,fill:{color:NAVY_CARD},line:{type:"none"},shadow:sh({blur:8,offset:3,opacity:0.34})});
    s.addImage({data:ic,x:x+0.26,y:3.25,w:0.6,h:0.6});
    s.addText(head,{x:x+0.26,y:3.96,w:w-0.5,h:0.4,margin:0,fontFace:DISP,bold:true,fontSize:18,color:GOLD_BR});
    s.addText(body,{x:x+0.26,y:4.34,w:w-0.5,h:0.62,margin:0,fontFace:SANS,fontSize:12.5,color:"CFD5E0",lineSpacingMultiple:1.1}); };
  gcard(M,      I["FaHandHoldingUsd_"+GOLD_BR],"Capped returns","No one draws permanent rent on a public square.");
  gcard(M+2.92, I["FaUnlockAlt_"+GOLD_BR],     "Written in the open","The Covenant and the Code, with nothing run in secret.");
  gcard(M+5.84, I["FaCodeBranch_"+GOLD_BR],    "Forkable","If the center betrays the people, they take it and leave.");
  s.addNotes("The constitution is two things: the Covenant people agree to, and the Code that runs it. And the deepest check: the whole thing can be forked.");

  // 9 — THOUSAND-YEAR HORIZON
  s=pres.addSlide(); s.background={color:NAVY_DEEP}; chrome(s,11,true);
  eyebrow(s,"The horizon",M,1.3,8,true);
  s.addText([{text:"1,000",options:{fontFace:DISP,bold:true,fontSize:120,color:IVORY}},
             {text:"  years",options:{fontFace:DISP,italic:true,fontSize:52,color:GOLD_BR}}],
    {x:M,y:1.95,w:9,h:1.7,margin:0,align:"left",shadow:sh({blur:12,offset:6,opacity:0.36})});
  s.addText("Not built for the next quarter. Built for the next thousand years, because only an internet owned by the people who use it is built to last that long.",
    {x:M,y:4.1,w:8.7,h:0.95,margin:0,fontFace:SANS,fontSize:17,color:"CFD5E0",lineSpacingMultiple:1.16});
  s.addNotes("The time signature of the project. This is not a startup quarter, it is a founding meant to endure.");

  // 10 — THE CASE (essays divider)
  s=pres.addSlide(); s.background={color:PARCH}; chrome(s,12,false);
  eyebrow(s,"The case",M,1.2,8,false);
  s.addText("We didn't just declare it.\nWe made the case.",{x:M,y:1.55,w:9,h:1.05,margin:0,fontFace:DISP,bold:true,fontSize:38,color:INK,lineSpacingMultiple:0.98});
  const items=[
    ["01","We Never Agreed","why change is possible"],
    ["02","The Shape of Your Digital Shadow","what your data is made of"],
    ["03","Ambition Against Ambition","how power stays divided"],
    ["04","The Longer Race","the economics"],
    ["05","The Ledger and the Spoils","AI meets crypto"],
  ];
  items.forEach((it,i)=>{ const y=2.95+i*0.42;
    s.addText(it[0],{x:M,y,w:0.5,h:0.42,margin:0,valign:"middle",fontFace:DISP,bold:true,fontSize:19,color:GOLD});
    s.addText(it[1],{x:M+0.62,y,w:5.6,h:0.42,margin:0,valign:"middle",fontFace:DISP,bold:true,fontSize:16.5,color:INK});
    s.addText(it[2],{x:M+6.3,y,w:2.45,h:0.42,margin:0,valign:"middle",fontFace:SANS,italic:true,fontSize:12,color:MUTED}); });
  s.addNotes("Pivot to depth. The movement is not a slogan; the full argument lives in five short essays. Walk them quickly.");

  // ---- per-essay template ----
  function essaySlide(num,dark,tag,title,thesis,essence){
    const e=pres.addSlide(); e.background={color:dark?NAVY:PARCH}; chrome(e,num,dark);
    const numeral=String(num-12).padStart(2,"0");
    e.addText("ESSAY",{x:M,y:2.0,w:2.3,h:0.3,margin:0,fontFace:SANS,fontSize:13,bold:true,charSpacing:3,color:dark?GOLD_BR:GOLD});
    e.addText(numeral,{x:M-0.05,y:2.26,w:2.4,h:1.45,margin:0,fontFace:DISP,bold:true,fontSize:110,color:dark?GOLD_BR:GOLD,shadow:dark?sh({opacity:0.3}):undefined});
    const RX=3.2,RW=6.2;
    e.addText(tag.toUpperCase(),{x:RX,y:1.5,w:RW,h:0.3,margin:0,fontFace:SANS,fontSize:12.5,bold:true,charSpacing:3,color:dark?GOLD_BR:GOLD});
    e.addText(title,{x:RX,y:1.85,w:RW,h:1.05,margin:0,fontFace:DISP,bold:true,fontSize:32,color:dark?IVORY:INK,lineSpacingMultiple:0.98,
      shadow:dark?sh({opacity:0.28}):sh({color:"B9B097",opacity:0.4,blur:6,offset:2})});
    e.addText(thesis,{x:RX,y:3.0,w:RW,h:0.55,margin:0,fontFace:DISP,italic:true,fontSize:19,color:dark?GOLD_BR:GOLD,lineSpacingMultiple:1.0});
    e.addText(essence,{x:RX,y:3.66,w:RW,h:1.5,margin:0,fontFace:SANS,fontSize:14,color:dark?"CFD5E0":BODY,lineSpacingMultiple:1.16});
    return e;
  }
  essaySlide(13,true ,"Why change is possible","We Never Agreed",
    "What was built can be built differently.",
    "We click 'I agree' to an internet we never chose. It was designed this way by a few, for their benefit — and a design is a choice we can remake.");
  essaySlide(14,false,"What your data is made of","The Shape of Your Digital Shadow",
    "Your shadow has a shape, and the shape has rights.",
    "Your shadow comes in regions: what you make, what you do, what you are, and what is inferred about you. Over each, a free person should hold the rights to see, correct, hold, and profit.");
  essaySlide(15,true ,"How power stays divided","Ambition Against Ambition",
    "No part of the new internet should rule the rest.",
    "The old internet fused control, money, and authority in a few hands. The new one splits those powers, holds them in check, and keeps the whole thing forkable, so no part can ever dominate.");
  essaySlide(16,false,"The economics","The Longer Race",
    "Working together can out-build racing apart.",
    "A collaborative internet can create at least as much value as a cut-throat one, and share it far more evenly. Cooperation is not charity. Over a long enough race, it wins.");
  essaySlide(17,true ,"AI meets crypto","The Ledger and the Spoils",
    "The ledger was the easy part. The spoils are the prize.",
    "Crypto decentralized the ledger but left the rewards concentrated in a few hands. Joining AI's value creation to crypto's verifiable ownership can finally decentralize the spoils themselves.");

  // 16 — WHAT LAUNCHES JULY 2
  s=pres.addSlide(); s.background={color:PARCH}; chrome(s,18,false);
  eyebrow(s,"What we launch on July 2",M,1.28,8,false);
  s.addText("Words first. Then the building.",{x:M,y:1.62,w:9,h:0.85,margin:0,fontFace:DISP,bold:true,fontSize:36,color:INK});
  const jc=(x,ic,head,body)=>{ const w=2.74;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE,{x,y:2.78,w,h:1.7,rectRadius:0.08,fill:{color:PARCH_CARD},line:{type:"none"},shadow:sh({color:"9A927C",blur:6,offset:2,opacity:0.20})});
    s.addImage({data:ic,x:x+0.26,y:3.0,w:0.56,h:0.56});
    s.addText(head,{x:x+0.26,y:3.62,w:w-0.5,h:0.36,margin:0,fontFace:DISP,bold:true,fontSize:17,color:INK});
    s.addText(body,{x:x+0.26,y:3.98,w:w-0.5,h:0.46,margin:0,fontFace:SANS,fontSize:12.5,color:BODY,lineSpacingMultiple:1.08}); };
  jc(M,      I["FaScroll_"+INK],   "The Declaration","The principles, the grievances, and the intent.");
  jc(M+2.92, I["FaBookOpen_"+INK], "The case","Five short essays making the argument in full.");
  jc(M+5.84, I["FaFeatherAlt_"+INK],"Your name","A place to affirm it and join the founding cohort.");
  s.addText("The constitution comes after: the Covenant and the Code, written in public.",{x:M,y:4.7,w:9,h:0.4,margin:0,fontFace:DISP,italic:true,fontSize:16,color:GOLD});
  s.addNotes("Manage expectations honestly: July 2 is the declaration moment, not the finished republic. In 1776 they declared; the constitution came later.");

  // 17 — FOR EVERYONE
  s=pres.addSlide(); s.background={color:NAVY}; chrome(s,19,true);
  eyebrow(s,"Who it is for",M,1.5,8,true);
  s.addText("This one is for everyone.",{x:M,y:1.95,w:9,h:1.0,margin:0,fontFace:DISP,bold:true,fontSize:48,color:IVORY,shadow:sh()});
  s.addText([
    {text:"Belonging is a matter of affirmation and participation.",options:{breakLine:true,color:"CFD5E0"}},
    {text:"Not of birth, or border, or wealth.",options:{color:GOLD_BR,bold:true}},
  ],{x:M,y:3.35,w:8.7,h:1.1,margin:0,fontFace:SANS,fontSize:20,lineSpacingMultiple:1.2});
  s.addNotes("Open the doors. No geography, no gatekeeping by money or birth. You belong by showing up and affirming the idea.");

  // 18 — CTA
  s=pres.addSlide(); s.background={color:NAVY_DEEP}; chrome(s,20,true);
  s.addShape(pres.shapes.RECTANGLE,{x:(W-0.16)/2,y:1.35,w:0.16,h:0.16,rotate:45,fill:{color:GOLD},line:{type:"none"}});
  s.addText("JULY 2, 2026",{x:0,y:1.74,w:W,h:0.32,align:"center",fontFace:SANS,fontSize:13,bold:true,charSpacing:4,color:GOLD_BR});
  s.addText("Add your name.",{x:0,y:2.12,w:W,h:1.05,align:"center",fontFace:DISP,bold:true,fontSize:60,color:IVORY,shadow:sh({blur:12,offset:6,opacity:0.36})});
  s.addText("Affirm the Declaration. Join the founding cohort. Help build the internet that should have been.",
    {x:1.0,y:3.4,w:8.0,h:0.7,align:"center",margin:0,fontFace:SANS,fontSize:17,color:"CFD5E0",lineSpacingMultiple:1.15});
  s.addShape(pres.shapes.ROUNDED_RECTANGLE,{x:3.35,y:4.32,w:3.3,h:0.62,rectRadius:0.31,fill:{color:GOLD},line:{type:"none"},shadow:sh({blur:8,offset:3,opacity:0.3})});
  s.addText(URL,{x:3.35,y:4.32,w:3.3,h:0.62,align:"center",valign:"middle",margin:0,fontFace:SANS,fontSize:18,bold:true,color:NAVY_DEEP});
  s.addNotes("The ask. One action: add your name at "+URL+".");

  // 19 — CLOSING
  s=pres.addSlide(); s.background={color:NAVY};
  s.addText("We the Users",{x:0,y:2.0,w:W,h:1.1,align:"center",fontFace:DISP,bold:true,fontSize:58,color:IVORY,shadow:sh({blur:11,offset:5,opacity:0.34})});
  s.addText("Not we the used.",{x:0,y:3.16,w:W,h:0.55,align:"center",fontFace:DISP,italic:true,fontSize:26,color:GOLD_BR});
  s.addText("JULY 2, 2026   ·   "+URLU,{x:0,y:4.5,w:W,h:0.34,align:"center",fontFace:SANS,fontSize:12.5,bold:true,charSpacing:3,color:SLATE});
  s.addNotes("Close on the banner and its shadow: We the Users, not we the used. The whole movement in five words.");

  await pres.writeFile({fileName:PATH.join(__dirname,"We-the-Users-Launch-Deck.pptx")});
  console.log("written 21 slides");
})();

click("start");
var seasons=0;
for (var s=0;s<13;s++){
  // try voting and research, building on selected tiles is UI-driven; just begin
  click("vote","none"); click("tab","research"); click("tab","build"); click("begin");
  click("speed","4");
  frames(400, 50);
  click("hall"); click("give"); click("tab","council");
  var d=els["#dialog"].innerHTML; if (d.indexOf("Session over")>=0){ print("ENDED after loop "+s); print(d.replace(/<[^>]+>/g," ").replace(/\s+/g," ").slice(0,700)); break; }
  print("loop "+s+" dock: "+els["#dock"].innerHTML.replace(/<[^>]+>/g," ").replace(/\s+/g," ").slice(0,120));
}
print("RANKS: "+els["#ranks"].innerHTML.replace(/<[^>]+>/g," ").replace(/\s+/g," "));
print("LOG: "+els["#log"].innerHTML.replace(/<[^>]+>/g," ").replace(/\s+/g," ").slice(0,900));

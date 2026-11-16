var __out=[];
function runBatch(styles, n, others){
  for (var si=0; si<styles.length; si++) for (var s=1; s<=n; s++){
    globalThis.__seed = s*7919 + si*104729 + 13;
    var r = globalThis.__sim(styles[si], others);
    r.p0 = styles[si]; __out.push(r);
  }
}

var __raf=[], __listeners={}, __t=0;
function mkEl(){ var e={innerHTML:"",textContent:"",hidden:false,style:{},dataset:{},width:1000,height:640,
  addEventListener:function(n,f){ (__listeners[n]=__listeners[n]||[]).push(f); },
  setAttribute:function(){}, getBoundingClientRect:function(){return{left:0,top:0,width:1000,height:640};},
  getContext:function(){ return ctxStub; } }; return e; }
var grad={addColorStop:function(){}};
var ctxStub=new Proxy({}, {get:function(t,k){ if(k==="createLinearGradient"||k==="createRadialGradient") return function(){return grad;}; if(k in t) return t[k]; return function(){}; }, set:function(t,k,v){t[k]=v;return true;}});
var els={};
var document={ querySelector:function(s){ return els[s]||(els[s]=mkEl()); }, querySelectorAll:function(){ return []; },
  createElement:function(){ return mkEl(); }, addEventListener:function(n,f){ (__listeners[n]=__listeners[n]||[]).push(f); } };
var window={ addEventListener:function(){}, matchMedia:function(){return{matches:false};} };
var localStorage={ getItem:function(){return null;}, setItem:function(){} };
var performance={ now:function(){ return __t; } };
function requestAnimationFrame(f){ __raf.push(f); }
function setTimeout(f){ return 0; } function clearTimeout(){}
function click(act,k,extra){ var btn={dataset:Object.assign({act:act,k:k},extra||{}),disabled:false}; var ev={target:{closest:function(){return btn;}}}; __listeners.click.forEach(function(f){f(ev);}); }
function frames(n,ms){ for(var i=0;i<n;i++){ __t+=ms; var q=__raf; __raf=[]; q.forEach(function(f){f(__t);}); } }

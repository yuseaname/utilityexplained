
(function(){
  function init(id){
    var root=document.getElementById(id); if(!root) return;
    var L={l:root.querySelector('#st-last'),n:root.querySelector('#st-now'),kl:root.querySelector('#st-kwh-last'),kn:root.querySelector('#st-kwh-now')};
    var GO=root.querySelector('#st-go'),OUT=root.querySelector('#st-out'); if(!GO||!OUT) return;
    function fmt(n){return '$'+n.toFixed(2);}
    function run(){
      var l=parseFloat(L.l.value)||0,n=parseFloat(L.n.value)||0,kl=parseFloat(L.kl.value)||0,kn=parseFloat(L.kn.value)||0;
      if(l<=0||n<=0||kl<=0||kn<=0){OUT.innerHTML='<p class="calc-err">Fill in all four numbers (they are on your bills).</p>';return;}
      var rl=l/kl, rn=n/kn, dTotal=n-l;
      var usagePart=(kn-kl)*rl, ratePart=(rn-rl)*kn;
      var h='<p class="calc-verdict"><strong>Total change: '+fmt(dTotal)+'</strong></p>';
      if(dTotal>-1){
        h+='<p class="calc-detail">Usage effect: <strong>'+fmt(usagePart)+'</strong> ('+(kn-kl).toFixed(0)+' kWh difference at your old rate)</p>';
        h+='<p class="calc-detail">Rate effect: <strong>'+fmt(ratePart)+'</strong> ('+rl.toFixed(3)+' to '+rn.toFixed(3)+' $/kWh'+(Math.abs(rn-rl)/rl>0.15?' — a >15% rate jump; check for a rate change or tier blowthrough':'')+')</p>';
        if(Math.abs(ratePart)>Math.abs(usagePart)){
          h+='<p class="calc-detail"><strong>Your increase is mostly RATE, not usage.</strong> Read <a href="/blog/25-utility-bill-taxes-fees-franchise-charges-explained/">why charges per kWh change</a>, then check whether a <a href="/blog/08-time-of-use-electricity/">time-of-use plan</a> is now the better deal.</p>';
        } else {
          h+='<p class="calc-detail"><strong>Your increase is mostly USAGE.</strong> Start with the <a href="/blog/how-to-lower-electric-bill-complete-guide/">17-step lower-bill guide</a> — or find the culprit appliance with a <a href="https://www.amazon.com/s?k=p3+kill+a+watt+electricity+monitor&tag=utexplained-20" rel="sponsored nofollow noopener" target="_blank">plug-in watt meter (~$25)</a>.</p>';
        }
      } else {
        h+='<p class="calc-detail">Your bill went down '+fmt(-dTotal)+'. Compare the rate lines to see if a usage drop or a rate drop did it.</p>';
      }
      OUT.innerHTML=h;
    }
    GO.addEventListener('click',run);
    Object.values(L).forEach(function(el){el.addEventListener('keydown',function(e){if(e.key==='Enter')run();});});
  }
  document.addEventListener('DOMContentLoaded',function(){init('spike-triage');});
})();

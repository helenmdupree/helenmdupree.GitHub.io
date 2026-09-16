/* SOUBEL Knowledge dropdown interaction guard */
(function(){
  function init(){
    const dropdown=document.querySelector('.desktop-nav .knowledge-dropdown');
    if(!dropdown || dropdown.dataset.soubelDropdownFix==='true') return;
    dropdown.dataset.soubelDropdownFix='true';

    const button=dropdown.querySelector('.dropbtn');
    const panel=dropdown.querySelector('.dropdown-panel');
    if(!button || !panel) return;

    if(!document.querySelector('#soubel-knowledge-dropdown-fix-style')){
      const style=document.createElement('style');
      style.id='soubel-knowledge-dropdown-fix-style';
      style.textContent=`
@media(min-width:1051px){
  .desktop-nav .knowledge-dropdown .dropdown-panel{
    display:none!important;
    opacity:0!important;
    visibility:hidden!important;
    pointer-events:none!important;
  }
  .desktop-nav .knowledge-dropdown.soubel-open .dropdown-panel{
    display:grid!important;
    opacity:1!important;
    visibility:visible!important;
    pointer-events:auto!important;
  }
}`;
      document.head.appendChild(style);
    }

    let closeTimer=null;
    const open=()=>{
      if(closeTimer){clearTimeout(closeTimer);closeTimer=null;}
      dropdown.classList.add('soubel-open');
      button.setAttribute('aria-expanded','true');
    };
    const close=()=>{
      if(closeTimer){clearTimeout(closeTimer);closeTimer=null;}
      dropdown.classList.remove('soubel-open');
      button.setAttribute('aria-expanded','false');
      button.blur();
    };
    const scheduleClose=()=>{
      if(closeTimer) clearTimeout(closeTimer);
      closeTimer=setTimeout(close,120);
    };

    button.setAttribute('aria-expanded','false');
    dropdown.addEventListener('mouseenter',open);
    dropdown.addEventListener('mouseleave',scheduleClose);
    panel.addEventListener('mouseenter',open);

    button.addEventListener('click',e=>{
      e.preventDefault();
      dropdown.classList.contains('soubel-open') ? close() : open();
    });

    panel.querySelectorAll('a').forEach(link=>link.addEventListener('click',close));
    document.querySelectorAll('.desktop-nav > *').forEach(item=>{
      if(item!==dropdown) item.addEventListener('mouseenter',close);
    });
    document.addEventListener('pointerdown',e=>{
      if(!dropdown.contains(e.target)) close();
    });
    document.addEventListener('keydown',e=>{
      if(e.key==='Escape') close();
    });
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',()=>setTimeout(init,0));
  else setTimeout(init,0);
})();

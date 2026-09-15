/* SOUBEL analytics foundation */
(function(){
  const GA4_MEASUREMENT_ID = 'G-J9WDHGCCW3';
  const params = new URLSearchParams(location.search);
  const utm = {};
  ['utm_source','utm_medium','utm_campaign','utm_content','utm_term'].forEach(k=>{if(params.get(k)) utm[k]=params.get(k);});
  if(Object.keys(utm).length){
    try{sessionStorage.setItem('soubel_utm',JSON.stringify(utm));}catch(e){}
  }

  window.dataLayer = window.dataLayer || [];
  // Privacy guard: never send literal public-site search text to analytics.
  window.gtag = window.gtag || function(){
    const args=Array.from(arguments);
    if(args[0]==='event' && args[1]==='site_search' && args[2] && typeof args[2]==='object'){
      const safe=Object.assign({},args[2]);
      if(Object.prototype.hasOwnProperty.call(safe,'search_term')){
        const n=String(safe.search_term||'').length;
        safe.search_length_bucket=n<10?'2-9':n<25?'10-24':n<50?'25-49':'50+';
        delete safe.search_term;
      }
      args[2]=safe;
    }
    dataLayer.push(args);
  };

  if(GA4_MEASUREMENT_ID){
    const sc=document.createElement('script');
    sc.async=true;
    sc.src='https://www.googletagmanager.com/gtag/js?id='+encodeURIComponent(GA4_MEASUREMENT_ID);
    document.head.appendChild(sc);
    gtag('js',new Date());
    gtag('config',GA4_MEASUREMENT_ID,{send_page_view:true});
  }

  function sendEvent(name,params){
    if(!GA4_MEASUREMENT_ID) return;
    const stored=(()=>{try{return JSON.parse(sessionStorage.getItem('soubel_utm')||'{}');}catch(e){return {};}})();
    gtag('event',name,Object.assign({},stored,params||{}));
  }

  document.addEventListener('click',function(e){
    const a=e.target.closest('a');
    if(!a) return;
    const href=a.getAttribute('href')||'';
    const text=(a.textContent||'').trim().replace(/\s+/g,' ').slice(0,120);
    let eventName='navigation_click';
    if(/^https?:\/\//i.test(href) && !href.includes('soubel.com')) eventName='outbound_click';
    if(/linkedin\.com|instagram\.com/i.test(href)) eventName='social_click';
    if(href.startsWith('/knowledge-library')) eventName='knowledge_library_click';
    if(href.startsWith('/industry-intelligence')) eventName='industry_intelligence_click';
    if(href.startsWith('/analysis-perspectives') || href.startsWith('/insights/')) eventName='article_click';
    if(href.startsWith('/resources')) eventName='resource_click';
    if(href.startsWith('/downloads/')) eventName='resource_download';
    if(/^mailto:|\/contact\//i.test(href)) eventName='contact_intent';
    sendEvent(eventName,{link_url:href,link_text:text,page_path:location.pathname});
  });

  if(document.querySelector('.article-body,.archive-article-body')){
    let sent=false;
    const onScroll=()=>{
      if(sent) return;
      const doc=document.documentElement;
      const max=Math.max(1,doc.scrollHeight-innerHeight);
      if(scrollY/max>=0.75){
        sent=true;
        sendEvent('article_75_percent',{page_path:location.pathname,document_title:document.title});
        removeEventListener('scroll',onScroll);
      }
    };
    addEventListener('scroll',onScroll,{passive:true});
  }
})();

/* SOUBEL header v6 — split Retina assets + tablet-safe navigation */
(function(){
  const brand=document.querySelector('.brand-logo');
  const img=brand && brand.querySelector('img');
  if(img){
    img.style.opacity='0';
    img.style.width='100%';
    img.style.height='100%';
    img.style.maxWidth='none';
  }
  if(brand) brand.classList.add('soubel-header-v6');
  if(!document.querySelector('#soubel-header-v6-style')){
    const style=document.createElement('style');
    style.id='soubel-header-v6-style';
    style.textContent=`
.brand-logo.soubel-header-v6{position:relative!important;display:block!important;width:320px!important;height:62px!important;flex:0 0 auto!important;overflow:visible!important}
.brand-logo.soubel-header-v6::before,.brand-logo.soubel-header-v6::after{content:"";position:absolute;top:50%;transform:translateY(-50%);background-repeat:no-repeat;background-position:center;background-size:contain;pointer-events:none}
.brand-logo.soubel-header-v6::before{left:0;width:32%;aspect-ratio:240/124;background-image:url('/assets/soubel-header-emblem-v6.png')}
.brand-logo.soubel-header-v6::after{right:0;width:66%;aspect-ratio:420/67;background-image:url('/assets/soubel-header-text-v6.png')}
@media(max-width:1050px){.desktop-nav{display:none!important}.menu-toggle{display:block!important}.header-inner{min-height:82px!important}.mobile-menu{inset:82px 0 0 0!important}.brand-logo.soubel-header-v6{width:320px!important;height:62px!important}}
@media(max-width:620px){.header-inner{min-height:62px!important}.mobile-menu{inset:62px 0 0 0!important}.brand-logo.soubel-header-v6{width:min(250px,calc(100vw - 100px))!important;height:50px!important}}
`;
    document.head.appendChild(style);
  }
})();

/* SOUBEL global search loader */
(function(){
  if(document.querySelector('script[data-soubel-global-search]')) return;
  const script=document.createElement('script');
  script.src='/assets/global-search.js?v=1';
  script.defer=true;
  script.dataset.soubelGlobalSearch='true';
  document.head.appendChild(script);
})();

/* SOUBEL Knowledge dropdown — two-column desktop layout with Resource subcategories */
(function(){
  function refineKnowledgeMenu(){
    const panel=document.querySelector('.desktop-nav .knowledge-dropdown .dropdown-panel');
    if(!panel) return;

    const links=[...panel.querySelectorAll(':scope > a')];
    links.forEach(a=>{
      const href=a.getAttribute('href')||'';
      if(href.startsWith('/resources/') && href!=='/resources/'){
        a.classList.add('knowledge-resource-subitem');
      }
      if(href==='/resources/') a.classList.add('knowledge-resources-parent');
    });

    if(!document.querySelector('#knowledge-dropdown-reconcile-style')){
      const style=document.createElement('style');
      style.id='knowledge-dropdown-reconcile-style';
      style.textContent=`
.desktop-nav .knowledge-dropdown{position:relative}
.desktop-nav .knowledge-dropdown .dropdown-panel{
  left:50%!important;
  right:auto!important;
  transform:translateX(-68%)!important;
  width:min(720px,calc(100vw - 36px))!important;
  min-width:640px!important;
  max-width:720px!important;
  display:grid!important;
  grid-auto-flow:column!important;
  grid-template-rows:repeat(7,auto)!important;
  grid-template-columns:repeat(2,minmax(0,1fr))!important;
  column-gap:22px!important;
  padding:18px!important;
}
.desktop-nav .knowledge-dropdown .dropdown-panel>a{
  min-width:0!important;
  white-space:normal!important;
}
.desktop-nav .knowledge-dropdown .knowledge-resources-parent{
  margin-top:2px!important;
  font-weight:800!important;
}
.desktop-nav .knowledge-dropdown .knowledge-resource-subitem{
  position:relative!important;
  padding-left:34px!important;
  font-size:.9em!important;
  line-height:1.28!important;
  color:#9fc1c7!important;
}
.desktop-nav .knowledge-dropdown .knowledge-resource-subitem::before{
  content:"↳";
  position:absolute;
  left:16px;
  color:#4fb2b7;
}
@media(max-width:1180px){
  .desktop-nav .knowledge-dropdown .dropdown-panel{
    transform:translateX(-73%)!important;
    width:min(660px,calc(100vw - 28px))!important;
    min-width:600px!important;
  }
}
`;
      document.head.appendChild(style);
    }
  }

  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded',()=>setTimeout(refineKnowledgeMenu,0),{once:true});
  }else{
    setTimeout(refineKnowledgeMenu,0);
  }
})();
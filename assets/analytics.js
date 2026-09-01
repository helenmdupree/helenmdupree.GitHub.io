/* SOUBEL analytics foundation */
(function(){
  const GA4_MEASUREMENT_ID = '';
  const params = new URLSearchParams(location.search);
  const utm = {};
  ['utm_source','utm_medium','utm_campaign','utm_content','utm_term'].forEach(k=>{if(params.get(k)) utm[k]=params.get(k);});
  if(Object.keys(utm).length){
    try{sessionStorage.setItem('soubel_utm',JSON.stringify(utm));}catch(e){}
  }

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function(){dataLayer.push(arguments);};

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

/* SOUBEL header v5 — Retina asset + tablet-safe navigation */
(function(){
  const img=document.querySelector('.brand-logo img');
  if(img){
    img.src='/assets/soubel-header-v5.png';
    img.removeAttribute('srcset');
  }
  if(!document.querySelector('#soubel-header-v5-style')){
    const style=document.createElement('style');
    style.id='soubel-header-v5-style';
    style.textContent='.brand-logo{flex:0 0 auto!important}.brand-logo img{width:320px!important;height:auto!important;max-width:none!important;object-fit:contain!important}@media(max-width:1050px){.desktop-nav{display:none!important}.menu-toggle{display:block!important}.brand-logo img{width:320px!important;height:auto!important}.header-inner{min-height:82px!important}.mobile-menu{inset:82px 0 0 0!important}}@media(max-width:620px){.header-inner{min-height:62px!important}.mobile-menu{inset:62px 0 0 0!important}.brand-logo img{width:min(250px,calc(100vw - 100px))!important;height:auto!important}}';
    document.head.appendChild(style);
  }
})();
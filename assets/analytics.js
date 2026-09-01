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
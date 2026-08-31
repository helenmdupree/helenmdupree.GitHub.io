/* SOUBEL analytics foundation — V1.11
   Add the production GA4 Measurement ID below when the GA4 property is created.
   Search Console verification belongs in the site <head> or DNS, not in this file. */
(function(){
  const GA4_MEASUREMENT_ID = ''; // Example format: G-XXXXXXXXXX. Intentionally blank until assigned.
  const currentYear = String(new Date().getFullYear());
  document.querySelectorAll('[data-current-year]').forEach(el => el.textContent = currentYear);

  // Preserve campaign attribution for the session so future LinkedIn/Instagram UTM links remain measurable.
  const params = new URLSearchParams(location.search);
  const utm = {};
  ['utm_source','utm_medium','utm_campaign','utm_content','utm_term'].forEach(k => { if(params.get(k)) utm[k]=params.get(k); });
  if(Object.keys(utm).length){ try{ sessionStorage.setItem('soubel_utm', JSON.stringify(utm)); }catch(e){} }

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function(){ dataLayer.push(arguments); };
  if(GA4_MEASUREMENT_ID){
    const sc=document.createElement('script'); sc.async=true; sc.src='https://www.googletagmanager.com/gtag/js?id='+encodeURIComponent(GA4_MEASUREMENT_ID); document.head.appendChild(sc);
    gtag('js', new Date()); gtag('config', GA4_MEASUREMENT_ID, {send_page_view:true});
  }

  // Useful events: outbound source clicks, social clicks, knowledge/intelligence navigation and contact-intent links.
  document.addEventListener('click', function(e){
    const a=e.target.closest('a'); if(!a) return;
    const href=a.getAttribute('href')||'';
    let eventName='navigation_click';
    if(/^https?:\/\//i.test(href) && !href.includes('soubel.com')) eventName='outbound_click';
    if(/linkedin\.com|instagram\.com/i.test(href)) eventName='social_click';
    if(href.startsWith('/knowledge-library')) eventName='knowledge_library_click';
    if(href.startsWith('/industry-intelligence')) eventName='industry_intelligence_click';
    if(/^mailto:|\/contact\//i.test(href)) eventName='contact_intent';
    if(GA4_MEASUREMENT_ID) gtag('event', eventName, {link_url:href, link_text:(a.textContent||'').trim().slice(0,100)});
  });

  // Public visitor counter capability. Hidden by default. A production endpoint may return {"visitors":1234}.
  // The counter becomes eligible only when the returned count meets the HTML data-threshold (currently 1000).
  const counter=document.querySelector('[data-audience-counter]');
  const COUNTER_ENDPOINT=''; // Intentionally blank until a first-party counting endpoint is chosen.
  if(counter && COUNTER_ENDPOINT){
    fetch(COUNTER_ENDPOINT,{credentials:'same-origin'}).then(r=>r.json()).then(data=>{
      const count=Number(data.visitors||0), threshold=Number(counter.dataset.threshold||1000);
      if(Number.isFinite(count) && count>=threshold){
        counter.querySelector('[data-audience-count]').textContent=count.toLocaleString(); counter.hidden=false; counter.setAttribute('aria-hidden','false');
      }
    }).catch(()=>{});
  }
})();

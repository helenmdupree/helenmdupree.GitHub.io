/* SOUBEL analytics foundation + V1.74 live refinement loader */
(function(){
  const GA4_MEASUREMENT_ID = '';
  const currentYear = String(new Date().getFullYear());
  document.querySelectorAll('[data-current-year]').forEach(el => el.textContent = currentYear);

  /* V1.74: load the refinement layer after the established master stylesheet. */
  if(!document.querySelector('link[href="/assets/v174-live-refinement.css"]')){
    const css=document.createElement('link'); css.rel='stylesheet'; css.href='/assets/v174-live-refinement.css?v=174'; document.head.appendChild(css);
  }

  const path=location.pathname.replace(/\/+$/,'/') || '/';
  const linkify=(container,map)=>{
    if(!container) return;
    [...container.querySelectorAll('span')].forEach(sp=>{
      const t=sp.textContent.trim(), href=map[t];
      if(href){ const a=document.createElement('a'); a.href=href; a.textContent=t; sp.replaceWith(a); }
      else sp.classList.add('inactive-topic');
    });
  };

  /* Industry Intelligence: real navigation and cleaner future-feed language. */
  if(path==='/industry-intelligence/'){
    const h1=document.querySelector('.topic-hero h1'); if(h1 && h1.textContent.trim()==='What is happening now.') h1.textContent='What is happening now';
    linkify(document.querySelector('.filter-row'),{
      'Midstream':'/markets/midstream-pipelines/','Pipelines':'/markets/midstream-pipelines/','Integrity':'/expertise/pipeline-asset-integrity/','Corrosion':'/expertise/corrosion-cathodic-protection/','Regulatory':'/insights/pipeline-integrity-regulation/','M&A':'/expertise/commercial-growth-strategic-accounts/','AI & Technology':'/expertise/digital-transformation-ai/','Projects':'/expertise/commercial-growth-strategic-accounts/','PHMSA':'/insights/phmsa-prescriptive-to-predictive/','Energy Infrastructure':'/markets/utilities-industrial-infrastructure/'
    });
    const es=document.querySelector('.empty-state'); if(es){ const h=es.querySelector('h3'), p=es.querySelector('p:last-child'); if(h) h.textContent='Latest developments, added as they matter.'; if(p) p.textContent='Selected developments will appear here in reverse chronological order after source and editorial review, with links to original reporting or primary sources and concise SOUBEL context.'; }
  }

  /* About: page title should not compete with the actual SOUBEL wordmark. */
  if(path==='/about/'){
    const h1=document.querySelector('.page-hero h1'); if(h1 && h1.textContent.trim()==='SOUBEL') h1.textContent='About SOUBEL';
  }

  /* Corrosion knowledge branch: every exploration chip now has a destination. */
  if(path==='/knowledge-library/corrosion-cathodic-protection/'){
    linkify(document.querySelector('#next-depth .filter-row'),{
      '850 On / Polarized Potential / 100 mV':'#fundamentals','CIPS / CIS':'#field','DCVG':'#field','Interference':'#fundamentals','AC Interference & Mitigation':'#fundamentals','Remote Monitoring':'#field','Coatings + CP':'#materials','ECDA':'#integrity','Integrity Excavations & Direct Examination':'#integrity','Data Confidence':'/knowledge-library/asset-performance/condition-context/','Integrity Software & Data Management':'/expertise/digital-transformation-ai/','AI-Assisted Interpretation':'/expertise/digital-transformation-ai/'
    });
  }

  /* A-Z: existing substantive destinations are links; roadmap-only terms stop pretending to be buttons. */
  if(path==='/knowledge-library/'){
    const map={
      'AI & Machine Learning':'/expertise/digital-transformation-ai/','Asset Integrity':'/expertise/pipeline-asset-integrity/','Asset Performance':'/knowledge-library/asset-performance/','Business Cases':'/expertise/commercial-growth-strategic-accounts/','Cathodic Protection':'/knowledge-library/corrosion-cathodic-protection/','CIPS / CIS':'/knowledge-library/corrosion-cathodic-protection/#field','Coatings':'/knowledge-library/corrosion-cathodic-protection/#materials','Commercial Growth':'/expertise/commercial-growth-strategic-accounts/','Corrosion':'/knowledge-library/corrosion-cathodic-protection/','Data Confidence':'/knowledge-library/asset-performance/condition-context/','Digital Transformation':'/expertise/digital-transformation-ai/','Digital Twins':'/expertise/digital-transformation-ai/','ECDA':'/knowledge-library/corrosion-cathodic-protection/#integrity','Enterprise AI Readiness':'/insights/integrity-shift/enterprise-readiness-for-ai/','Field Execution':'/operational-trust/','Ground Truth':'/knowledge-library/asset-performance/condition-context/','ILI':'/expertise/pipeline-asset-integrity/','Integrity Management':'/expertise/pipeline-asset-integrity/','Inspection':'/expertise/pipeline-asset-integrity/','Internal Corrosion':'/expertise/pipeline-asset-integrity/','Machine Learning':'/expertise/digital-transformation-ai/','Mega Rule':'/insights/phmsa-prescriptive-to-predictive/','Midstream':'/markets/midstream-pipelines/','Operational Risk':'/expertise/operational-risk/','Operational Trust':'/operational-trust/','PHMSA':'/insights/phmsa-prescriptive-to-predictive/','Pipeline Integrity':'/expertise/pipeline-asset-integrity/','Regulation':'/insights/pipeline-integrity-regulation/','Revenue Strategy':'/insights/revenue-strategy-is-built/','Risk':'/expertise/operational-risk/','SCC':'/expertise/pipeline-asset-integrity/','SCCDA':'/expertise/pipeline-asset-integrity/','Strategic Accounts':'/expertise/commercial-growth-strategic-accounts/','Technology Adoption':'/expertise/digital-transformation-ai/','Traceability':'/operational-trust/','Validation':'/expertise/digital-transformation-ai/','Value Quantification':'/expertise/commercial-growth-strategic-accounts/'
    };
    document.querySelectorAll('.az-topics').forEach(box=>linkify(box,map));
    const az=document.querySelector('.az-index'); if(az){ const intro=az.previousElementSibling; if(intro && intro.classList.contains('section-intro')) intro.textContent='Active topics link to substantive SOUBEL material. Additional subjects remain visible as the library roadmap and will become active only when meaningful content is ready.'; }
  }

  const params = new URLSearchParams(location.search), utm = {};
  ['utm_source','utm_medium','utm_campaign','utm_content','utm_term'].forEach(k => { if(params.get(k)) utm[k]=params.get(k); });
  if(Object.keys(utm).length){ try{ sessionStorage.setItem('soubel_utm', JSON.stringify(utm)); }catch(e){} }
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function(){ dataLayer.push(arguments); };
  if(GA4_MEASUREMENT_ID){ const sc=document.createElement('script'); sc.async=true; sc.src='https://www.googletagmanager.com/gtag/js?id='+encodeURIComponent(GA4_MEASUREMENT_ID); document.head.appendChild(sc); gtag('js', new Date()); gtag('config', GA4_MEASUREMENT_ID, {send_page_view:true}); }
  document.addEventListener('click', function(e){ const a=e.target.closest('a'); if(!a) return; const href=a.getAttribute('href')||''; let eventName='navigation_click'; if(/^https?:\/\//i.test(href) && !href.includes('soubel.com')) eventName='outbound_click'; if(/linkedin\.com|instagram\.com/i.test(href)) eventName='social_click'; if(href.startsWith('/knowledge-library')) eventName='knowledge_library_click'; if(href.startsWith('/industry-intelligence')) eventName='industry_intelligence_click'; if(/^mailto:|\/contact\//i.test(href)) eventName='contact_intent'; if(GA4_MEASUREMENT_ID) gtag('event', eventName, {link_url:href, link_text:(a.textContent||'').trim().slice(0,100)}); });
  const counter=document.querySelector('[data-audience-counter]'), COUNTER_ENDPOINT='';
  if(counter && COUNTER_ENDPOINT){ fetch(COUNTER_ENDPOINT,{credentials:'same-origin'}).then(r=>r.json()).then(data=>{ const count=Number(data.visitors||0), threshold=Number(counter.dataset.threshold||1000); if(Number.isFinite(count) && count>=threshold){ counter.querySelector('[data-audience-count]').textContent=count.toLocaleString(); counter.hidden=false; counter.setAttribute('aria-hidden','false'); } }).catch(()=>{}); }
})();

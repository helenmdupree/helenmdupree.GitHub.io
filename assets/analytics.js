/* SOUBEL analytics foundation + V1.75 refinement loader */
(function(){
  const GA4_MEASUREMENT_ID = '';
  const currentYear = String(new Date().getFullYear());
  document.querySelectorAll('[data-current-year]').forEach(el => el.textContent = currentYear);

  if(!document.querySelector('link[href="/assets/v174-live-refinement.css"]')){
    const css=document.createElement('link'); css.rel='stylesheet'; css.href='/assets/v174-live-refinement.css?v=174'; document.head.appendChild(css);
  }

  const path=location.pathname.replace(/\/+$/,'/') || '/';
  const resourceLinks=[
    ['/resources/','Resources Overview'],
    ['/downloads/SOUBEL_Pipeline_Integrity_Metallurgy_PHMSA_Executive_Technical_Fluency_Guide.pdf','Pipeline Integrity, Metallurgy & PHMSA'],
    ['/downloads/SOUBEL_Reliability_Maintenance_Decision_Workbook.pdf','Reliability & Maintenance Workbook'],
    ['/downloads/SOUBEL_When_Asset_Condition_Changes_Practical_Guide.pdf','When Asset Condition Changes'],
    ['/downloads/SOUBEL_Lifecycle_Decision_Comparison.pdf','Lifecycle Decision Comparison']
  ];

  /* Resources: keep the right-edge dropdown inside the viewport and keep SOUBEL open when PDFs are viewed. */
  if(!document.querySelector('#resources-nav-audit-style')){
    const style=document.createElement('style');
    style.id='resources-nav-audit-style';
    style.textContent=`
      .desktop-nav .resources-dropdown .dropdown-panel{left:auto!important;right:0!important;max-width:min(390px,calc(100vw - 28px))!important}
      .desktop-nav .resources-dropdown .dropdown-panel a{white-space:normal!important}
    `;
    document.head.appendChild(style);
  }

  /* V1.75 live audit: Resources is a top-level dropdown with direct access to current publications. */
  document.querySelectorAll('.desktop-nav').forEach(nav=>{
    let resources=[...nav.children].find(el=>el.classList?.contains('dropdown') && el.querySelector('.dropbtn')?.textContent.trim()==='Resources');
    if(!resources){
      const direct=[...nav.children].find(el=>el.tagName==='A' && el.getAttribute('href')==='/resources/');
      resources=document.createElement('div'); resources.className='dropdown resources-dropdown';
      const button=document.createElement('button'); button.className='dropbtn'; button.textContent='Resources';
      const panel=document.createElement('div'); panel.className='dropdown-panel';
      resourceLinks.forEach(([href,text])=>{ const a=document.createElement('a'); a.href=href; a.textContent=text; panel.appendChild(a); });
      resources.append(button,panel);
      if(direct) direct.replaceWith(resources);
      else {
        const about=[...nav.children].find(el=>el.classList?.contains('dropdown') && el.querySelector('.dropbtn')?.textContent.trim()==='About');
        if(about) nav.insertBefore(resources,about); else nav.appendChild(resources);
      }
    }
    resources.classList.add('resources-dropdown');
    const about=[...nav.children].find(el=>el.classList && el.classList.contains('dropdown') && el.querySelector('.dropbtn')?.textContent.trim()==='About');
    const panel=about?.querySelector('.dropdown-panel');
    if(panel && !panel.querySelector('a[href="/about/career-in-motion/"]')){
      const a=document.createElement('a'); a.href='/about/career-in-motion/'; a.textContent='A Career in Motion';
      const experience=panel.querySelector('a[href="/about/experience/"]');
      if(experience) experience.insertAdjacentElement('afterend',a); else panel.appendChild(a);
    }
  });
  document.querySelectorAll('.mobile-menu').forEach(menu=>{
    [...menu.querySelectorAll('a[href="/resources/"]')].forEach(a=>{ if(!a.closest('.resources-group')) a.remove(); });
    let resources=[...menu.querySelectorAll('.group')].find(g=>g.querySelector('.group-title')?.textContent.trim()==='Resources');
    if(!resources){
      resources=document.createElement('div'); resources.className='group resources-group';
      const title=document.createElement('div'); title.className='group-title'; title.textContent='Resources'; resources.appendChild(title);
      const about=[...menu.querySelectorAll('.group')].find(g=>g.querySelector('.group-title')?.textContent.trim()==='About');
      if(about) menu.insertBefore(resources,about); else menu.appendChild(resources);
    }
    if(!resources.querySelector('a')) resourceLinks.forEach(([href,text])=>{ const a=document.createElement('a'); a.href=href; a.textContent=text; a.className='sub'; resources.appendChild(a); });
    const about=[...menu.querySelectorAll('.group')].find(g=>g.querySelector('.group-title')?.textContent.trim()==='About');
    if(about && !about.querySelector('a[href="/about/career-in-motion/"]')){
      const a=document.createElement('a'); a.href='/about/career-in-motion/'; a.textContent='A Career in Motion'; a.className='sub';
      const experience=about.querySelector('a[href="/about/experience/"]');
      if(experience) experience.insertAdjacentElement('afterend',a); else about.appendChild(a);
    }
  });

  /* All SOUBEL PDF publications open separately so the website remains available underneath. */
  document.querySelectorAll('a[href^="/downloads/"][href$=".pdf"]').forEach(a=>{
    a.target='_blank';
    a.rel='noopener';
  });

  const linkify=(container,map)=>{
    if(!container) return;
    [...container.querySelectorAll('span')].forEach(sp=>{
      const t=sp.textContent.trim(), href=map[t];
      if(href){ const a=document.createElement('a'); a.href=href; a.textContent=t; sp.replaceWith(a); }
      else sp.classList.add('inactive-topic');
    });
  };

  if(path==='/industry-intelligence/'){
    const h1=document.querySelector('.topic-hero h1'); if(h1 && h1.textContent.trim()==='What is happening now.') h1.textContent='What is happening now';
    linkify(document.querySelector('.filter-row'),{
      'Midstream':'/markets/midstream-pipelines/','Pipelines':'/markets/midstream-pipelines/','Integrity':'/expertise/pipeline-asset-integrity/','Corrosion':'/expertise/corrosion-cathodic-protection/','Regulatory':'/insights/pipeline-integrity-regulation/','M&A':'/expertise/commercial-growth-strategic-accounts/','AI & Technology':'/expertise/digital-transformation-ai/','Projects':'/expertise/commercial-growth-strategic-accounts/','PHMSA':'/insights/phmsa-prescriptive-to-predictive/','Energy Infrastructure':'/markets/utilities-industrial-infrastructure/'
    });
    const es=document.querySelector('.empty-state'); if(es){ const h=es.querySelector('h3'), p=es.querySelector('p:last-child'); if(h) h.textContent='Latest developments, added as they matter.'; if(p) p.textContent='Selected developments will appear here in reverse chronological order after source and editorial review, with links to original reporting or primary sources and concise SOUBEL context.'; }
  }

  if(path==='/about/'){
    const h1=document.querySelector('.page-hero h1'); if(h1 && h1.textContent.trim()==='SOUBEL') h1.textContent='About SOUBEL';
  }

  if(path==='/knowledge-library/corrosion-cathodic-protection/'){
    linkify(document.querySelector('#next-depth .filter-row'),{
      '850 On / Polarized Potential / 100 mV':'#fundamentals','CIPS / CIS':'#field','DCVG':'#field','Interference':'#fundamentals','AC Interference & Mitigation':'#fundamentals','Remote Monitoring':'#field','Coatings + CP':'#materials','ECDA':'#integrity','Integrity Excavations & Direct Examination':'#integrity','Data Confidence':'/knowledge-library/asset-performance/condition-context/','Integrity Software & Data Management':'/expertise/digital-transformation-ai/','AI-Assisted Interpretation':'/expertise/digital-transformation-ai/'
    });
  }

  if(path==='/knowledge-library/'){
    const map={
      'AI & Machine Learning':'/expertise/digital-transformation-ai/','Asset Integrity':'/expertise/pipeline-asset-integrity/','Asset Performance':'/knowledge-library/asset-performance/','Business Cases':'/expertise/commercial-growth-strategic-accounts/','Cathodic Protection':'/knowledge-library/corrosion-cathodic-protection/','CIPS / CIS':'/knowledge-library/corrosion-cathodic-protection/#field','Coatings':'/knowledge-library/corrosion-cathodic-protection/#materials','Commercial Growth':'/expertise/commercial-growth-strategic-accounts/','Corrosion':'/knowledge-library/corrosion-cathodic-protection/','Data Confidence':'/knowledge-library/asset-performance/condition-context/','Digital Transformation':'/expertise/digital-transformation-ai/','Digital Twins':'/expertise/digital-transformation-ai/','ECDA':'/knowledge-library/corrosion-cathodic-protection/#integrity','Enterprise AI Readiness':'/insights/integrity-shift/enterprise-readiness-for-ai/','Field Execution':'/operational-trust/','Ground Truth':'/knowledge-library/asset-performance/condition-context/','ILI':'/expertise/pipeline-asset-integrity/','Integrity Management':'/expertise/pipeline-asset-integrity/','Inspection':'/expertise/pipeline-asset-integrity/','Internal Corrosion':'/expertise/pipeline-asset-integrity/','Machine Learning':'/expertise/digital-transformation-ai/','Mega Rule':'/insights/phmsa-prescriptive-to-predictive/','Midstream':'/markets/midstream-pipelines/','Operational Risk':'/expertise/operational-risk/','Operational Trust':'/operational-trust/','PHMSA':'/insights/phmsa-prescriptive-to-predictive/','Pipeline Integrity':'/expertise/pipeline-asset-integrity/','Regulation':'/insights/pipeline-integrity-regulation/','Revenue Strategy':'/insights/revenue-strategy-is-built/','Risk':'/expertise/operational-risk/','SCC':'/expertise/pipeline-asset-integrity/','SCCDA':'/expertise/pipeline-asset-integrity/','Strategic Accounts':'/expertise/commercial-growth-strategic-accounts/','Technology Adoption':'/expertise/digital-transformation-ai/','Traceability':'/operational-trust/','Validation':'/expertise/digital-transformation-ai/','Value Quantification':'/expertise/commercial-growth-strategic-accounts/'
    };
    document.querySelectorAll('.az-topics').forEach(box=>linkify(box,map));
    const az=document.querySelector('.az-index'); if(az){ const intro=az.previousElementSibling; if(intro && intro.classList.contains('section-intro')) intro.textContent='Active topics link to substantive SOUBEL material. Additional subjects remain visible as the library roadmap and will become active only when meaningful content is ready.'; }
  }

  /* V1.75 evidence-informed additions. Source experience is deliberately de-identified for public use. */
  if(path==='/expertise/commercial-growth-strategic-accounts/' && !document.querySelector('#commercial-lenses')){
    const main=document.querySelector('main');
    if(main){
      const s=document.createElement('section'); s.className='section alt'; s.id='commercial-lenses';
      s.innerHTML='<div class="wrap"><p class="kicker">FOUR COMMERCIAL LENSES</p><h2>Growth has to work in the market, in the product, in the economics, and in execution.</h2><p class="section-intro">SOUBEL draws on practical experience building commercial structure around complex industrial products, services, software, and technical offerings. The work is viewed through four connected lenses.</p><div class="grid-2"><article class="card"><span class="label">COMMERCIAL ARCHITECT</span><h3>Build the economic and operating structure.</h3><p>Growth models, pricing, margin, service-line economics, resource priorities, ownership, and execution cadence.</p></article><article class="card"><span class="label">MARKET BUILDER</span><h3>Find where demand can actually be created.</h3><p>Market diagnosis, segmentation, whitespace, competitive position, channels, customer evidence, and market-development systems.</p></article><article class="card"><span class="label">PRODUCT STRATEGIST</span><h3>Translate the market back into the capability.</h3><p>Voice of customer, use-case design, product-market fit, commercialization, field requirements, and technical-to-commercial translation.</p></article><article class="card"><span class="label">ENTERPRISE SELLER</span><h3>Carry the strategy into a real buying decision.</h3><p>Complex pursuits, pilots, contracts, business cases, strategic accounts, executive alignment, and revenue execution.</p></article></div><div class="trust-note"><strong>The practical standard:</strong> commercial growth is created when market truth is translated into an executable system.</div></div>';
      main.appendChild(s);
    }
  }

  if(path==='/expertise/asset-performance/' && !document.querySelector('#decision-time-value')){
    const target=[...document.querySelectorAll('section')].find(s=>s.textContent.includes('CONNECTED KNOWLEDGE'));
    if(target){
      const s=document.createElement('section'); s.className='section dark'; s.id='decision-time-value';
      s.innerHTML='<div class="wrap"><p class="kicker">FROM INSIGHT TO VALUE</p><h2>Earlier insight creates value only when the organization can use the decision time.</h2><p class="section-intro">A better signal can create time to confirm condition, gather supporting evidence, coordinate with operations, obtain parts or specialist support, prepare the work, compare alternatives, and choose a better intervention window. The economic value is not prediction by itself. It is the improved decision and operating consequence that prediction makes possible.</p><div class="data-flow"><span>Earlier Evidence</span><i>→</i><span>Decision Time</span><i>→</i><span>Prepared Work</span><i>→</i><span>Operating Outcome</span><i>→</i><span>Learning</span></div></div>';
      target.parentNode.insertBefore(s,target);
    }
  }

  if(path==='/about/experience/' && !document.querySelector('#experience-patterns')){
    const gallery=document.querySelector('#career-gallery');
    if(gallery){
      const s=document.createElement('section'); s.className='section alt'; s.id='experience-patterns';
      s.innerHTML='<div class="wrap"><p class="kicker">PATTERNS OF PRACTICE</p><h2>The résumé shows roles. The pattern behind the work is broader.</h2><p class="section-intro">Across industrial products, field services, corrosion and integrity, infrastructure, enterprise software, and digital programs, the recurring work has been to understand what is true in the market, identify where value is being lost or overlooked, connect technical capability to customer and operating reality, quantify the economics, align the organization, and carry the strategy into execution.</p><div class="grid-2"><article class="card"><span class="label">MARKET DEVELOPMENT</span><h3>Build markets, not only territories.</h3><p>Customer evidence, segmentation, channels, advocacy, competitive position, technical communities, and market education can all shape how a complex capability earns attention and adoption.</p></article><article class="card"><span class="label">TECHNICAL-COMMERCIAL TRANSLATION</span><h3>Translate in both directions.</h3><p>Technical capability has to become customer relevance, and field/customer reality has to travel back into product, engineering, R&amp;D, workflow, and commercialization decisions.</p></article><article class="card"><span class="label">VALUE ENGINEERING</span><h3>Connect the technical outcome to economic consequence.</h3><p>Labor, field effort, risk, operating cost, margin, capital, recurring potential, and decision quality can turn a technical conversation into a decision-ready business case.</p></article><article class="card"><span class="label">INDUSTRY LEADERSHIP</span><h3>Technical communities are also market-intelligence systems.</h3><p>Long-term participation in professional communities can strengthen technical fluency, customer insight, standards awareness, market development, and the ability to recognize emerging priorities before they become obvious.</p></article></div><div class="actions"><a class="btn secondary" href="/about/career-in-motion/">View A Career in Motion</a></div></div>';
      gallery.parentNode.insertBefore(s,gallery);
      gallery.hidden=true;
      gallery.setAttribute('aria-hidden','true');
    }
  } else if(path==='/about/experience/'){
    const gallery=document.querySelector('#career-gallery'); if(gallery){ gallery.hidden=true; gallery.setAttribute('aria-hidden','true'); }
  }

  const params = new URLSearchParams(location.search), utm = {};
  ['utm_source','utm_medium','utm_campaign','utm_content','utm_term'].forEach(k => { if(params.get(k)) utm[k]=params.get(k); });
  if(Object.keys(utm).length){ try{ sessionStorage.setItem('soubel_utm', JSON.stringify(utm)); }catch(e){} }
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function(){ dataLayer.push(arguments); };
  if(GA4_MEASUREMENT_ID){ const sc=document.createElement('script'); sc.async=true; sc.src='https://www.googletagmanager.com/gtag/js?id='+encodeURIComponent(GA4_MEASUREMENT_ID); document.head.appendChild(sc); gtag('js', new Date()); gtag('config', GA4_MEASUREMENT_ID, {send_page_view:true}); }
  document.addEventListener('click', function(e){ const a=e.target.closest('a'); if(!a) return; const href=a.getAttribute('href')||''; let eventName='navigation_click'; if(/^https?:\/\//i.test(href) && !href.includes('soubel.com')) eventName='outbound_click'; if(/linkedin\.com|instagram\.com/i.test(href)) eventName='social_click'; if(href.startsWith('/knowledge-library')) eventName='knowledge_library_click'; if(href.startsWith('/industry-intelligence')) eventName='industry_intelligence_click'; if(href.startsWith('/resources')) eventName='resource_click'; if(href.startsWith('/downloads/')) eventName='resource_download'; if(/^mailto:|\/contact\//i.test(href)) eventName='contact_intent'; if(GA4_MEASUREMENT_ID) gtag('event', eventName, {link_url:href, link_text:(a.textContent||'').trim().slice(0,100)}); });
  const counter=document.querySelector('[data-audience-counter]'), COUNTER_ENDPOINT='';
  if(counter && COUNTER_ENDPOINT){ fetch(COUNTER_ENDPOINT,{credentials:'same-origin'}).then(r=>r.json()).then(data=>{ const count=Number(data.visitors||0), threshold=Number(counter.dataset.threshold||1000); if(Number.isFinite(count) && count>=threshold){ counter.querySelector('[data-audience-count]').textContent=count.toLocaleString(); counter.hidden=false; counter.setAttribute('aria-hidden','false'); } }).catch(()=>{}); }
})();
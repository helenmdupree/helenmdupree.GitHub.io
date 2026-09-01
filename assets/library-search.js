(function(){
  const form=document.querySelector('.library-search');
  const input=document.getElementById('library-search');
  const results=document.getElementById('library-search-results');
  const status=document.getElementById('library-search-status');
  if(!form||!input||!results||!status||!Array.isArray(window.SOUBEL_SEARCH_INDEX)) return;

  const additions=[
    {url:'/about/experience/',title:'Experience | SOUBEL',description:'Selected industrial commercial, corrosion, integrity, asset performance, and digital transformation experience that informs SOUBEL’s work.',h1:'Experience that informs the work.',headings:'Career context SLB De Nora Integrated Corrosion Companies MATCOR Industry Leadership',text:'Helen M. Dupree experience across SLB asset performance and strategic accounts, North America and European account leadership, De Nora commercial growth and cathodic protection, Integrated Corrosion Companies commercial and operational leadership, MATCOR and earlier industrial roles.',type:'Experience'},
    {url:'/knowledge-library/',title:'SOUBEL Knowledge Library | Industrial Research & Reference',description:'Connected technical knowledge, research, regulatory context, Asset Integrity Management topics, decision frameworks and industrial reference material.',h1:'What should I understand?',headings:'Active Knowledge Branches Pipeline Integrity Corrosion Cathodic Protection Tank Terminal Integrity Asset Performance Digital Transformation AI AIM Knowledge A-Z Topic Index',text:'SOUBEL Knowledge Library connects pipeline integrity, corrosion and cathodic protection, tank and terminal integrity, asset performance, digital transformation and AI with Asset Integrity Management, evidence to execution, integrity methods, Operational Trust, regulatory analysis and practical decision resources. Active topics link only to substantive published destinations.',type:'Knowledge Library'},
    {url:'/knowledge-library/tank-terminal-integrity/',title:'Tank & Terminal Integrity Knowledge | SOUBEL',description:'SOUBEL connects storage-tank condition, corrosion, transfer systems, inspection, overfill prevention, containment, operating context, digital continuity and Asset Integrity Management across terminal facilities.',h1:'Terminal integrity is built through Operational Trust at every interface.',headings:'Tank Terminal Integrity Storage Tanks Tank Farms Transfer Piping Corrosion Cathodic Protection API 653 API 651 API 652 API 2350 API 2610 SPCC Overfill Containment Inspection MFL UT Settlement Loading Systems',text:'Terminal integrity connects storage tanks, tank bottoms, shells, roofs, foundations, transfer piping, pumps, valves, manifolds, loading and unloading systems, corrosion control, cathodic protection, coatings, linings, inspection, overfill prevention, secondary containment, release response, lifecycle records and digital continuity.',type:'Knowledge Library'},
    {url:'/expertise/asset-integrity-management/',title:'Asset Integrity Management | SOUBEL',description:'SOUBEL connects asset condition, technical evidence, operating context, decisions, field execution, verification, digital capability and learning across the asset lifecycle.',h1:'Operational trust, applied across the asset lifecycle.',headings:'Asset Integrity Management Operational Trust Application Domains AIM Decision Cycle Digital Enablement Evidence Execution Verification Learning',text:'Asset Integrity Management keeps condition, technical evidence, operating context, decisions, field execution, verification and learning connected over time. Condition Evidence Decision Execution Verification Learning. Pipelines, terminals, tank farms, process facilities, fixed equipment and industrial infrastructure.',type:'Expertise'},
    {url:'/expertise/asset-integrity-management/application-domains/',title:'AIM Application Domains | SOUBEL',description:'SOUBEL applies Asset Integrity Management thinking across pipelines, terminals, tank farms, process facilities, fixed equipment and industrial infrastructure.',h1:'Asset Integrity Management across the industrial asset system.',headings:'Pipelines Transmission Systems Terminals Tank Farms Storage Process Facilities Fixed Equipment Industrial Energy Infrastructure',text:'Asset Integrity Management application domains across pipelines and associated facilities, terminals, storage tanks, tank farms, transfer systems, process piping, vessels, pressure-containing equipment, pumps, compressors, structures, utilities and energy infrastructure.',type:'Expertise'},
    {url:'/expertise/asset-integrity-management/evidence-to-execution/',title:'Evidence to Execution | SOUBEL',description:'SOUBEL follows the decision chain from technical evidence through interpretation, handoff, field execution, verification and learning.',h1:'The reasoning behind a decision should survive the work.',headings:'Evidence Interpretation Decision Handoff Execution Verification Learning Practical Decision Tools Digital Continuity',text:'Asset integrity decisions move through inspection, engineering, operations, maintenance, planning, contractors, field personnel, verification and records. Preserve the decision basis, uncertainty, ownership, field findings and learning through the handoff.',type:'Expertise'},
    {url:'/expertise/asset-integrity-management/governance-assurance/',title:'AIM Governance & Assurance | SOUBEL',description:'SOUBEL explores the governance, competency, decision authority, traceability, assurance and learning that help Asset Integrity Management remain connected and defensible.',h1:'Integrity decisions need a system around them.',headings:'People Competency Roles Authority Processes Methods Data Traceability Assurance Performance Learning Change Decision Governance',text:'Asset Integrity Management governance connects qualified people, technical authority, procedures, traceable information, verification, assurance, accountability, performance measures, audits and organizational learning.',type:'Expertise'},
    {url:'/expertise/asset-integrity-management/asset-lifecycle/',title:'AIM Across the Asset Lifecycle | SOUBEL',description:'SOUBEL explores how Asset Integrity Management preserves design intent, condition knowledge, operating history, decisions, verification and learning across the full asset lifecycle.',h1:'Integrity knowledge should grow with the asset.',headings:'Design Intent Build Commission Operate Maintain Inspect Assess Modify Life Extension Decommission Lifecycle Continuity',text:'Asset Integrity Management across design, fabrication, construction, commissioning, operation, maintenance, inspection, assessment, modification, life extension and decommissioning. Preserve design basis, condition history, decisions, field verification and learning.',type:'Expertise'},
    {url:'/expertise/asset-integrity-management/integrity-methods/',title:'Integrity Methods & Decision Inputs | SOUBEL',description:'SOUBEL connects integrity methods, technical evidence, operating context, limitations and qualified judgment to stronger Asset Integrity Management decisions.',h1:'Different integrity questions require different evidence.',headings:'Inspection NDE Corrosion Management Risk RBI Fitness for Service Engineering Assessment Materials Metallurgy Monitoring Data Digital',text:'Integrity methods and decision inputs include inspection, nondestructive examination, corrosion management, risk and RBI, fitness for service, engineering assessment, materials, metallurgy, monitoring, integrity software, digital twins, analytics and AI.',type:'Expertise'},
    {url:'/insights/transform-revenue-yesterdays-job/',title:'You Don’t Transform Revenue by Hiring for Yesterday’s Job | SOUBEL',description:'Commercial transformation requires roles, resources, expectations, and measures of success built for the future revenue model.',h1:'You Don’t Transform Revenue by Hiring for Yesterday’s Job',headings:'Commercial Growth Organizational Transformation Revenue Strategy',text:'Tomorrow’s revenue cannot be created inside yesterday’s job description. Commercial roles should be designed around the future revenue model.',type:'Analysis & Perspectives'},
    {url:'/insights/dont-confuse-altitude-with-influence/',title:'Don’t Confuse Altitude with Influence | SOUBEL',description:'Commercial strategy depends on understanding where the buying event begins and translating between operational reality and enterprise consequence.',h1:'Don’t Confuse Altitude with Influence',headings:'Commercial Growth Strategic Accounts Operational Trust Influence',text:'A Rolodex can open a door. It cannot replace a go-to-market strategy. Commercial strategy is created in the translation between the field and the C-suite.',type:'Analysis & Perspectives'},
    {url:'/insights/phmsa-april-2026-operational-trust-next-standard/',title:'PHMSA’s April 2026 — Operational Trust Is the Next Standard | SOUBEL',description:'PHMSA’s April 2026 pipeline safety rulemakings point toward remote sensing, monitoring, integrity-management-based compliance, traceability, and operational trust.',h1:'Operational Trust Is the Next Standard',headings:'PHMSA Pipeline Regulation Operational Trust Digital Transformation',text:'Remote sensing technologies, remote monitoring capabilities, integrity-management-based compliance pathways, operational traceability, defensible operational intelligence.',type:'Analysis & Perspectives'},
    {url:'/insights/industrial-operations-operational-understanding/',title:'There’s Something Interesting Happening Across Industrial Operations Right Now | SOUBEL',description:'Industrial transformation is shifting from technology novelty toward operational understanding, trusted information, better decisions, and practical field use.',h1:'There’s Something Interesting Happening Across Industrial Operations Right Now',headings:'Industrial Operations Digital Transformation Operational Trust',text:'Technology alone is not the differentiator anymore. Operational understanding is. Connect engineering reality, operational context, and digital capability.',type:'Analysis & Perspectives'},
    {url:'/knowledge-library/digital-transformation-ai/',title:'Digital Transformation & AI | Knowledge Library | SOUBEL',description:'SOUBEL technical and practical reference material on industrial data, AI, digital twins, provenance, uncertainty, and decision support.',h1:'Digital Transformation & AI',headings:'Data Provenance Data to Decision Sampling Bias Trustworthy Digital Twins Uncertainty Model Confidence',text:'Industrial digital transformation, AI readiness, trusted data, operational context, decision support, model confidence, digital twins, provenance.',type:'Knowledge Library'},
    {url:'/knowledge-library/digital-transformation-ai/data-provenance/',title:'Data Provenance | Knowledge Library | SOUBEL',description:'Why industrial data needs traceable origin, context, transformation history, and ownership to support trusted decisions.',h1:'Data Provenance',headings:'Source Context Traceability Evidence',text:'Data provenance, lineage, source systems, transformations, ownership, field evidence, operational trust.',type:'Knowledge Library'},
    {url:'/knowledge-library/digital-transformation-ai/data-to-decision/',title:'From Data to Decision | Knowledge Library | SOUBEL',description:'How industrial data becomes useful when it is translated into context, judgment, action, and verification.',h1:'From Data to Decision',headings:'Data Context Decision Action Verification',text:'Operational intelligence, decision quality, field execution, trusted data, workflow, action, verification.',type:'Knowledge Library'},
    {url:'/knowledge-library/digital-transformation-ai/sampling-bias/',title:'Sampling Bias | Knowledge Library | SOUBEL',description:'How uneven inspection, monitoring, and observation patterns can distort what industrial datasets appear to show.',h1:'Sampling Bias',headings:'Inspection Density Observation Bias AI Training Data',text:'Sampling bias, inspection data, ILI, CIS, field observations, investigation density, AI interpretation, dataset quality.',type:'Knowledge Library'},
    {url:'/knowledge-library/digital-transformation-ai/trustworthy-digital-twins/',title:'Trustworthy Digital Twins | Knowledge Library | SOUBEL',description:'Digital twins become useful when model assumptions, source data, operating context, and validation remain visible and defensible.',h1:'Trustworthy Digital Twins',headings:'Digital Twins Validation Context Models Operational Trust',text:'Digital twins, model validation, source data, assumptions, operational context, asset performance.',type:'Knowledge Library'},
    {url:'/knowledge-library/digital-transformation-ai/uncertainty-model-confidence/',title:'Uncertainty & Model Confidence | Knowledge Library | SOUBEL',description:'A practical view of uncertainty, confidence, evidence quality, and the limits of predictive industrial models.',h1:'Uncertainty & Model Confidence',headings:'Uncertainty Confidence Predictive Models Evidence',text:'Predictive models, confidence, uncertainty, evidence quality, validation, risk, industrial AI.',type:'Knowledge Library'}
  ];

  function enhanceLibraryHub(){
    const terminalUrl='/knowledge-library/tank-terminal-integrity/';
    const active=[...document.querySelectorAll('main > section')].find(section=>section.querySelector('.kicker')?.textContent.trim()==='ACTIVE KNOWLEDGE BRANCHES');
    const grid=active?.querySelector('.topic-hub-grid');
    if(active){const h2=active.querySelector('h2');if(h2)h2.textContent='Five subjects now carry dedicated technical depth.';}
    if(grid && !grid.querySelector('a[href="'+terminalUrl+'"]')){
      const a=document.createElement('a');a.className='topic-hub-card';a.href=terminalUrl;a.innerHTML='<span class="topic-number">05</span><h3>Tank &amp; Terminal Integrity</h3><p>Storage tanks, corrosion, transfer systems, inspection, overfill prevention, containment, facility interfaces, lifecycle records, and decision continuity.</p>';grid.appendChild(a);
    }
    const groups=[...document.querySelectorAll('.az-group')];
    const addTopic=(letter,label,href)=>{
      const group=groups.find(g=>g.querySelector('.az-letter')?.textContent.trim()===letter);const topics=group?.querySelector('.az-topics');
      if(topics && !topics.querySelector('a[href="'+href+'"]')){const span=document.createElement('span');span.className='active-topic';const a=document.createElement('a');a.href=href;a.textContent=label;span.appendChild(a);topics.appendChild(span);}
    };
    addTopic('S','Storage Tanks',terminalUrl+'#storage-tanks');
    addTopic('T','Tank & Terminal Integrity',terminalUrl);
    addTopic('O','Overfill Prevention',terminalUrl+'#prevention');
  }
  enhanceLibraryHub();

  const byUrl=new Map(window.SOUBEL_SEARCH_INDEX.filter(item=>item.url!=='/expertise/pipeline-asset-integrity/').map(item=>[item.url,item]));
  additions.forEach(item=>byUrl.set(item.url,item));
  const index=[...byUrl.values()];

  const esc=s=>String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const norm=s=>String(s||'').toLowerCase().replace(/[^a-z0-9&+\-\s]/g,' ').replace(/\s+/g,' ').trim();
  const tokens=q=>norm(q).split(' ').filter(Boolean);

  function score(item,words,phrase){
    const title=norm(item.title),h1=norm(item.h1),heads=norm(item.headings),desc=norm(item.description),body=norm(item.text);
    let n=0,matched=0;
    words.forEach(w=>{let hit=false;if(title.includes(w)){n+=24;hit=true;}if(h1.includes(w)){n+=20;hit=true;}if(heads.includes(w)){n+=12;hit=true;}if(desc.includes(w)){n+=8;hit=true;}if(body.includes(w)){n+=2;hit=true;}if(hit)matched++;});
    if(words.length>1&&matched===words.length)n+=16;
    if(phrase&&title.includes(phrase))n+=32;else if(phrase&&(h1.includes(phrase)||heads.includes(phrase)))n+=18;else if(phrase&&desc.includes(phrase))n+=10;
    if(item.type==='Knowledge Library')n+=5;
    return {score:n,matched};
  }

  function snippet(item,words){
    const source=item.description||item.text||'';
    if(item.description)return item.description;
    const low=source.toLowerCase();let pos=-1;
    for(const w of words){const p=low.indexOf(w);if(p>=0&&(pos<0||p<pos))pos=p;}
    if(pos<0)return source.slice(0,190)+(source.length>190?'…':'');
    const start=Math.max(0,pos-70),end=Math.min(source.length,start+210);
    return (start?'…':'')+source.slice(start,end).trim()+(end<source.length?'…':'');
  }

  function render(q){
    const phrase=norm(q),words=tokens(q);results.innerHTML='';
    if(!phrase){results.hidden=true;status.textContent='';return;}
    if(phrase.length<2){results.hidden=false;status.textContent='Type at least two characters.';return;}
    const ranked=index.map(item=>({item,...score(item,words,phrase)})).filter(x=>x.matched>0).sort((a,b)=>b.score-a.score||a.item.title.localeCompare(b.item.title)).slice(0,10);
    results.hidden=false;
    if(!ranked.length){status.textContent='No matches found.';results.innerHTML='<div class="library-search-empty"><strong>No results for “'+esc(q)+'”.</strong><p>Try a broader term such as corrosion, PHMSA, asset integrity, tank integrity, terminal, asset performance, AI, reliability, risk, or revenue strategy.</p></div>';return;}
    status.textContent=ranked.length+(ranked.length===1?' result':' results')+' shown for “'+q+'”.';
    results.innerHTML=ranked.map(({item})=>'<a class="library-search-result" href="'+esc(item.url)+'"><span class="library-search-type">'+esc(item.type)+'</span><strong>'+esc(item.title.replace(/\s*\|\s*SOUBEL.*$/i,''))+'</strong><p>'+esc(snippet(item,words))+'</p><span class="library-search-path">'+esc(item.url)+'</span></a>').join('');
  }

  let timer;
  input.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(()=>render(input.value),120);});
  form.addEventListener('submit',e=>{e.preventDefault();clearTimeout(timer);render(input.value);});
  input.addEventListener('keydown',e=>{if(e.key==='Escape'){input.value='';render('');input.focus();}});
})();
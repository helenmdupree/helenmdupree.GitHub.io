(function(){
  const SOURCE='/assets/knowledge-glossary-corrosion.json';

  function normalize(value){
    return String(value||'')
      .trim()
      .toLowerCase()
      .replace(/[“”"']/g,'')
      .replace(/[.]+$/,'')
      .replace(/\s+/g,' ');
  }

  function buildIndex(records){
    const index=new Map();
    records.forEach(record=>{
      index.set(normalize(record.id),record);
      index.set(normalize(record.term),record);
      (record.aliases||[]).forEach(alias=>index.set(normalize(alias),record));
    });
    return index;
  }

  function apply(records){
    const index=buildIndex(records);
    window.SOUBEL_GLOSSARY=records;
    window.SOUBEL_GLOSSARY_INDEX=index;

    document.querySelectorAll('.cp-term').forEach(el=>{
      const requested=el.getAttribute('data-glossary');
      const visible=normalize(el.textContent);
      const record=index.get(normalize(requested)) || index.get(visible);
      if(!record) return;
      el.setAttribute('data-glossary',record.id);
      el.setAttribute('data-definition',record.definition);
      el.setAttribute('aria-label',record.term+': '+record.definition);
      if(!el.hasAttribute('tabindex')) el.setAttribute('tabindex','0');
    });
  }

  function init(){
    fetch(SOURCE,{cache:'no-cache'})
      .then(response=>{
        if(!response.ok) throw new Error('Glossary request failed');
        return response.json();
      })
      .then(data=>apply(Array.isArray(data.records)?data.records:[]))
      .catch(()=>{
        /* Existing inline definitions remain as a graceful fallback. */
      });
  }

  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded',init,{once:true});
  }else{
    init();
  }
})();

import fs from 'node:fs';

const pagePath='C:/GitHub/soubel-iccp-v5-cleanstart/expertise/corrosion-cathodic-protection/index.html';
let html=fs.readFileSync(pagePath,'utf8');

const cssLink='<link href="/assets/site-cp-cinematic-v1.css?v=1" rel="stylesheet"/>';
if(!html.includes(cssLink)){
  html=html.replace('</head>',cssLink+'</head>');
}

const oldFigure='<figure class="cp-technical-figure"><img src="/assets/iccp%20system.png" alt="Conceptual impressed current cathodic protection system for a buried pipeline" loading="lazy"/></figure>';

const moduleMarkup=`
<div class="cp-cinematic-experience" data-iccp-cinematic>
  <div class="cp-cinematic-scene">
    <video class="cp-cinematic-video" tabindex="0" preload="metadata" playsinline poster="/assets/iccp-cinematic-poster-v10.jpg" aria-label="Animated conceptual impressed current cathodic protection system">
      <source src="/assets/iccp-cinematic-protected-v10.mp4" type="video/mp4"/>
      Your browser does not support embedded video.
    </video>
    <button class="cp-video-toggle" type="button" data-film-overlay-play>▶ Play cinematic</button>
    <div class="cp-film-progress" aria-hidden="true"><span data-film-progress></span></div>
  </div>
  <aside class="cp-cinematic-panel" aria-label="ICCP sequence controls">
    <div class="panel-kicker">Follow the current path</div>
    <h3>ICCP sequence</h3>
  <div class="cp-film-controls">
    <button class="cp-film-play" type="button" data-film-play>Play sequence</button>
    <button class="cp-film-reset" type="button" data-film-reset aria-label="Reset sequence">↺</button>
    <div class="cp-film-status" data-film-status>Stage 1 of 5</div>
  </div>
  <div class="cp-film-steps">
    <button class="cp-film-step" type="button" data-film-stage data-start="0" data-end="7.92" data-title="Power &amp; conversion" data-body="Utility AC supply feeds the separately mounted rectifier, where it is converted to controlled DC output."><small>01</small><b>Power &amp; conversion</b></button>
    <button class="cp-film-step" type="button" data-film-stage data-start="7.92" data-end="13.75" data-title="Positive circuit" data-body="Rectifier positive output travels through the positive cable and header to the external anode groundbed and individual anode leads."><small>02</small><b>Positive circuit</b></button>
    <button class="cp-film-step" type="button" data-film-stage data-start="13.75" data-end="17.5" data-title="Electrolyte path" data-body="Current leaves the anodes and travels through the surrounding soil or electrolyte toward the coated steel pipeline."><small>03</small><b>Electrolyte path</b></button>
    <button class="cp-film-step" type="button" data-film-stage data-start="17.5" data-end="20.5" data-title="Protected structure" data-body="Protective current reaches the pipeline surface and shifts the structure cathodic relative to its environment."><small>04</small><b>Protected structure</b></button>
    <button class="cp-film-step" type="button" data-film-stage data-start="20.5" data-end="26" data-title="Return &amp; monitoring" data-body="Conventional current returns from the pipeline through the negative connection to the rectifier. The test station and permanent reference electrode support measurement and verification, not the main return circuit."><small>05</small><b>Return &amp; monitoring</b></button>
  </div>
  <div class="cp-film-narrative">
    <strong data-film-title>Power &amp; conversion</strong>
    <span data-film-body>Utility AC supply feeds the separately mounted rectifier, where it is converted to controlled DC output.</span>
  </div>
  <p class="cp-film-note">Conceptual system · representative field arrangement · conventional current shown · not a design drawing</p>
  </aside>
</div>`;
if(!html.includes(oldFigure)){
  throw new Error('Expected ICCP static figure not found; page was not modified.');
}
html=html.replace(oldFigure,moduleMarkup);

const jsTag='<script src="/assets/iccp-cinematic-v1.js?v=1"></script>';
if(!html.includes(jsTag)){
  html=html.replace('</body>',jsTag+'</body>');
}

fs.writeFileSync(pagePath,html,'utf8');
console.log('ICCP cinematic integrated into',pagePath);

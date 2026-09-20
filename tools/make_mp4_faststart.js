import fs from 'node:fs';
import crypto from 'node:crypto';

const srcPath='C:/GitHub/soubel-iccp-v5-cleanstart/blender/iccp_cinematic_v10_SOUBEL_protected_720p24.mp4';
const outPath='C:/GitHub/soubel-iccp-v5-cleanstart/assets/iccp-cinematic-protected-v10.mp4';

const src=fs.readFileSync(srcPath);

function topBoxes(buf){
  const boxes=[];
  let pos=0;
  while(pos+8<=buf.length){
    let size=buf.readUInt32BE(pos);
    const type=buf.toString('ascii',pos+4,pos+8);
    let header=8;
    if(size===1){
      size=Number(buf.readBigUInt64BE(pos+8));
      header=16;
    }else if(size===0){
      size=buf.length-pos;
    }
    if(size<header||pos+size>buf.length) throw new Error('Invalid MP4 box layout');
    boxes.push({type,start:pos,size,end:pos+size});
    pos+=size;
  }
  return boxes;
}
function patchOffsets(moov,delta){
  for(const type of ['stco','co64']){
    let at=0;
    while((at=moov.indexOf(Buffer.from(type),at))>=0){
      const boxStart=at-4;
      const size=moov.readUInt32BE(boxStart);
      const count=moov.readUInt32BE(boxStart+12);
      const width=type==='stco'?4:8;
      const expected=16+(count*width);
      if(size<expected) throw new Error(type+' box is smaller than its offset table');
      for(let i=0;i<count;i++){
        const p=boxStart+16+(i*width);
        if(type==='stco'){
          const old=moov.readUInt32BE(p);
          const next=old+delta;
          if(next>0xffffffff) throw new Error('stco overflow');
          moov.writeUInt32BE(next,p);
        }else{
          const old=moov.readBigUInt64BE(p);
          moov.writeBigUInt64BE(old+BigInt(delta),p);
        }
      }
      at=boxStart+size;
    }
  }
}

const boxes=topBoxes(src);
const types=boxes.map(b=>b.type).join(',');
if(types!=='ftyp,free,mdat,moov') throw new Error('Unexpected top-level layout: '+types);
const [ftyp,free,mdat,moovBox]=boxes;
const moov=Buffer.from(src.subarray(moovBox.start,moovBox.end));
patchOffsets(moov,moovBox.size);

const out=Buffer.concat([
  src.subarray(ftyp.start,ftyp.end),
  src.subarray(free.start,free.end),
  moov,
  src.subarray(mdat.start,mdat.end)
]);

if(out.length!==src.length) throw new Error('Output size changed');

const originalMdat=src.subarray(mdat.start,mdat.end);
const newBoxes=topBoxes(out);
const newMdatBox=newBoxes.find(b=>b.type==='mdat');
const newMdat=out.subarray(newMdatBox.start,newMdatBox.end);
const hash=x=>crypto.createHash('sha256').update(x).digest('hex');

if(hash(originalMdat)!==hash(newMdat)) throw new Error('Media payload changed');

fs.writeFileSync(outPath,out);

console.log('FASTSTART_WRITTEN',outPath);
console.log('ORDER',newBoxes.map(b=>b.type).join(','));
console.log('SOURCE_BYTES',src.length);
console.log('OUTPUT_BYTES',out.length);
console.log('MDAT_SHA256',hash(newMdat));

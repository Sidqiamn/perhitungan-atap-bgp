<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>GNET Atap Shingles | Kalkulator Kebutuhan</title>
<style>
:root{--navy:#180f5e;--blue:#223d74;--orange:#f28b29;--ink:#1c2943;--muted:#6c7891;--line:#dce3ee;--bg:#f3f6fb;--card:#fff;--green:#1d8055}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);font:15px/1.5 Inter,Segoe UI,Arial,sans-serif;color:var(--ink)}
.wrap{max-width:1180px;margin:auto;padding:24px}
.hero{background:linear-gradient(115deg,#180f5e,#263e83);border-radius:24px;color:white;padding:32px 38px;display:flex;justify-content:space-between;gap:20px;align-items:end;box-shadow:0 16px 38px #180f5e22}
.eyebrow{color:#d8d4ff;font-size:11px;letter-spacing:2px;font-weight:800}
.hero h1{font-size:clamp(26px,4vw,42px);line-height:1.13;margin:11px 0}
.hero p{max-width:680px;margin:0;color:#e6e7fa}
.brand{font-size:32px;font-weight:900;letter-spacing:-2px;align-self:start;white-space:nowrap}.brand b{color:var(--orange)}
.grid{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(300px,1fr);gap:18px;margin-top:18px}
.card{background:white;border:1px solid var(--line);border-radius:20px;padding:24px;box-shadow:0 5px 15px #1b326609}
h2{font-size:19px;margin:0 0 16px}
.sub{color:var(--muted);font-size:13px;margin:-8px 0 18px}
.two{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:13px}
label,.grpLabel{font-size:12px;font-weight:700;color:#495976;display:block;margin-bottom:6px}
.help{font-size:11px;color:var(--muted);margin-top:5px}
input,select{width:100%;border:1px solid #cfd9e8;border-radius:10px;padding:11px 12px;font:inherit;color:var(--ink);background:#fff;min-width:0}
input:focus,select:focus{outline:2px solid #aba4ff;outline-offset:1px}
.field{margin-bottom:14px}
.plane{border:1px solid var(--line);border-radius:15px;padding:17px;margin-bottom:12px;background:#fcfdff}
.planeHead{display:flex;justify-content:space-between;gap:12px;align-items:center;margin-bottom:15px}
.planeHead strong{font-size:14px}
.mini{border:0;background:#fce9e9;color:#a52222;border-radius:8px;padding:7px 10px;cursor:pointer}
.seg{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-bottom:14px}
.seg button{border:1px solid #d9e0ee;background:#fff;border-radius:9px;padding:9px 6px;font-size:12px;font-weight:700;color:#61708c;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:3px;line-height:1.25}
.seg button small{font-weight:500;font-size:10.5px;color:#8a96ad}
.seg button svg{width:34px;height:22px}
.seg button[aria-pressed="true"]{background:#eae8ff;border-color:#7669df;color:var(--navy)}
.tip{font-size:12px;color:#5c6a85;background:#f2f5fa;border-radius:10px;padding:10px 12px;margin:0 0 14px}
.body{display:grid;grid-template-columns:180px minmax(0,1fr);gap:16px;align-items:start}
.body.noDiag{grid-template-columns:1fr}
.diagram svg{width:100%;height:auto;background:#f4f6fc;border-radius:12px;display:block}
.inputs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 12px}
.pwarn{display:none;background:#fff7e8;color:#815412;border:1px solid #f1d4a0;border-radius:10px;padding:10px 12px;font-size:12px;margin-bottom:12px}
.planeFoot{display:flex;justify-content:space-between;align-items:center;border-top:1px solid #e4e9f2;padding-top:12px;margin-top:2px;font-size:13px;color:var(--muted)}
.planeFoot strong{font-size:18px;color:var(--navy)}
.partial.bad{color:#a22121;font-size:14px}.partial.empty{color:#9aa5bb;font-size:14px;font-weight:600}
button{font:inherit}
.btn{border:0;border-radius:11px;padding:12px 16px;font-weight:800;cursor:pointer}
.primary{background:var(--navy);color:#fff}.secondary{background:#eae8fb;color:var(--navy)}.outline{background:#fff;border:1px solid #cdd6e6;color:var(--navy)}
.actions{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.templates{border:1px dashed #c9c3f2;background:#faf9ff;border-radius:14px;padding:14px;margin-bottom:14px}
.tplRow{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin:8px 0 0}
.tpl{position:relative;border:1.5px solid #d9e0ee;background:#fff;border-radius:13px;padding:12px 8px 11px;display:flex;flex-direction:column;align-items:center;gap:3px;cursor:pointer;color:#61708c;font-weight:800;font-size:14px;text-align:center;transition:background .15s,border-color .15s,box-shadow .15s,color .15s}
.tpl svg{width:58px;height:36px;margin-bottom:2px}
.tpl small{font-weight:500;font-size:11px;color:#8a96ad}
.tpl:hover{border-color:#a9a1ee;color:var(--navy)}
.tpl:focus-visible{outline:2px solid #aba4ff;outline-offset:2px}
.tpl[aria-pressed="true"]{background:var(--navy);border-color:var(--navy);color:#fff;box-shadow:0 8px 18px #180f5e33}
.tpl[aria-pressed="true"] small{color:#d4d8fb}
.tpl[aria-pressed="true"]::after{content:"✓";position:absolute;top:7px;right:8px;width:20px;height:20px;border-radius:50%;background:var(--orange);color:#fff;font-size:12px;font-weight:900;line-height:20px}
.tplInfo{font-size:12px;color:#55637e;background:#fff;border:1px solid #e3e1f6;border-left:3px solid var(--navy);border-radius:10px;padding:10px 12px;margin-top:10px}
.undo{display:block;margin-top:6px;color:#815412}
.linkBtn{border:0;background:none;padding:0;color:#4b3fc4;font-weight:800;text-decoration:underline;cursor:pointer;font-size:12px}
@media(max-width:470px){.tpl{padding:10px 4px;font-size:13px}.tpl svg{width:44px;height:28px}.tpl small{font-size:10px}}
.result{background:linear-gradient(145deg,#1b145f,#273c82);border-radius:17px;padding:23px;color:#fff}
.result small{color:#d4d9fc;font-weight:700;letter-spacing:1px}
.big{font-size:clamp(42px,5vw,68px);font-weight:900;letter-spacing:-2px;line-height:1.1;margin:8px 0}.big span{font-size:21px;letter-spacing:0}
.stat{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #e4e9f1;gap:10px}
.stat strong{font-variant-numeric:tabular-nums;text-align:right}.stat:last-child{border:0}
.disclaimer{font-size:12px;color:#6b7892;background:#f2f5fa;padding:14px;border-radius:12px;margin-top:16px}
.warn{background:#fff7e8;color:#815412;border:1px solid #f1d4a0;border-radius:12px;padding:13px;font-size:12px;margin-top:14px}
.error{background:#fff0f0;color:#a22121;padding:12px;border-radius:11px;margin:8px 0;font-size:13px;display:none}
.hint{background:#eef2fa;color:#495976;padding:12px;border-radius:11px;margin:8px 0;font-size:13px;display:none}
.kicker{font-size:12px;color:var(--muted);margin-top:14px}
.notice{border-left:3px solid var(--orange);padding-left:12px;font-size:12px;color:#6c7891}
.foot{color:#7c8ba4;font-size:12px;margin:20px 2px}
.badge{display:inline-block;background:#e9f6ef;color:var(--green);padding:5px 9px;border-radius:40px;font-weight:800;font-size:11px}
.mbar{display:none;position:fixed;left:0;right:0;bottom:0;background:var(--navy);color:#fff;padding:12px 16px;justify-content:space-between;align-items:center;gap:10px;z-index:9;box-shadow:0 -6px 18px #0003}
.mbar strong{font-size:22px}.mbar a{color:#ffd2a6;font-size:13px;font-weight:700;text-decoration:none}
@media(max-width:800px){.wrap{padding:12px 12px 80px}.grid{grid-template-columns:1fr}.hero{padding:24px;display:block}.brand{margin-top:18px;font-size:25px}.card{padding:18px}.mbar{display:flex}}
@media(max-width:600px){.body{grid-template-columns:1fr}.diagram{max-width:240px}}
@media(max-width:470px){.two,.inputs{grid-template-columns:1fr}.hero h1{font-size:27px}}
@media print{body{background:white}.wrap{max-width:none;padding:0}.hero{box-shadow:none;border-radius:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}.grid{display:block}.card{box-shadow:none;margin:16px 0;break-inside:avoid}.actions,.mini,#addBtn,.templates,.mbar,.tip{display:none!important}.seg button[aria-pressed="false"]{display:none}.seg{display:flex}.plane{break-inside:avoid}.result,.seg button{-webkit-print-color-adjust:exact;print-color-adjust:exact}.foot{font-size:10px}}
</style>
</head>
<body>
<div class="wrap">
  <header class="hero">
    <div><div class="eyebrow">GNET • SALES &amp; PROJECT TOOL</div><h1>Kalkulator Kebutuhan<br>Atap Shingles</h1><p>Estimasi luas bidang atap dan jumlah bundle untuk presentasi klien, kontraktor, dan developer.</p></div>
    <div class="brand">gnet<b>.</b></div>
  </header>
  <div class="grid">
    <main>
      <section class="card">
        <h2>01. Informasi Proyek</h2>
        <div class="two">
          <div class="field"><label for="project">Nama Proyek / Klien</label><input id="project" placeholder="Contoh: Villa Bandung" maxlength="100"></div>
          <div class="field"><label for="date">Tanggal Estimasi</label><input id="date" type="date"></div>
        </div>
        <div class="two">
          <div class="field"><label for="type">Tipe GNET Atap Shingles</label><select id="type"><option value="mosaic">Mosaic • 2,99 m²/bundle</option><option value="fish" selected>Fish Scale • 3,10 m²/bundle</option><option value="laminated">Laminated • 2,32 m²/bundle</option><option value="single">Single Layer • 3,10 m²/bundle</option></select></div>
          <div class="field"><label for="waste">Cadangan potongan / waste (%)</label><input id="waste" type="text" inputmode="decimal" value="10" autocomplete="off"><div class="help">Pelana 5–10% • Limasan 10–15% • Atap kompleks 15–20%</div></div>
        </div>
        <p class="notice">Cakupan per bundle mengacu E-Catalog GNET Atap Shingles 2026. Asumsi: angka m²/bundle adalah cakupan pemasangan efektif; wajib dikonfirmasi sebelum penawaran final.</p>
      </section>

      <section class="card" style="margin-top:18px">
        <h2>02. Bidang Atap</h2>
        <p class="sub">Pilih bentuk atap, lalu isi ukuran setiap bidang.</p>

        <div class="templates">
          <span class="grpLabel">Bentuk atap</span>
          <div class="tplRow" role="group" aria-label="Bentuk atap">
            <button type="button" class="tpl" data-tpl="satu" aria-pressed="true">
              <svg viewBox="0 0 64 40" aria-hidden="true"><polygon points="6,34 46,34 58,10 18,10" fill="currentColor" fill-opacity=".25" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>
              1 Bidang<small>hitung satu sisi</small></button>
            <button type="button" class="tpl" data-tpl="pelana" aria-pressed="false">
              <svg viewBox="0 0 64 40" aria-hidden="true"><polygon points="4,34 18,8 32,34" fill="currentColor" fill-opacity=".1" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><polygon points="18,8 46,8 60,34 32,34" fill="currentColor" fill-opacity=".3" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>
              Pelana<small>2 bidang</small></button>
            <button type="button" class="tpl" data-tpl="limasan" aria-pressed="false">
              <svg viewBox="0 0 64 40" aria-hidden="true"><polygon points="4,34 60,34 44,10 20,10" fill="currentColor" fill-opacity=".25" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><line x1="20" y1="10" x2="12" y2="34" stroke="currentColor" stroke-width="1.4" stroke-opacity=".6"/><line x1="44" y1="10" x2="52" y2="34" stroke="currentColor" stroke-width="1.4" stroke-opacity=".6"/></svg>
              Limasan<small>4 bidang</small></button>
          </div>
          <div class="tplInfo" id="tplInfo" aria-live="polite"></div>
        </div>

        <div id="planes"></div>
        <div id="error" class="error" role="alert"></div>
        <div id="hint" class="hint"></div>
        <button class="btn secondary" id="addBtn" type="button">+ Tambah Bidang Atap</button>

        <div class="disclaimer"><strong>Cara mengukur:</strong><br>
          • <b>Dari Denah</b>: ukuran dari gambar tampak atas (horizontal). Luas otomatis dikoreksi dengan sudut kemiringan (÷ cos sudut).<br>
          • <b>Di Atas Atap</b>: ukuran diambil langsung di permukaan miring, jadi tidak perlu sudut.<br>
          • <b>Luas Aktual</b>: luas permukaan atap yang sudah dihitung QS/kontraktor.<br>
          Rumus bentuk: persegi = a × t • trapesium = (a + b) ÷ 2 × t • segitiga = a × t ÷ 2.<br>
          Ukuran harus sudah termasuk overstek bila overstek ditutup shingles.</div>
      </section>
    </main>

    <aside id="hasil">
      <section class="card" style="position:sticky;top:12px">
        <h2>03. Hasil Estimasi <span class="badge">OTOMATIS</span></h2>
        <div class="result"><small>JUMLAH BUNDLE YANG DIBELI</small><div class="big" id="bundle">— <span>bundle</span></div><div id="rtype">Fish Scale • 3,10 m²/bundle</div></div>
        <div style="margin-top:12px">
          <div class="stat"><span>Luas permukaan aktual</span><strong id="actual">—</strong></div>
          <div class="stat"><span>Cadangan waste</span><strong id="wasteArea">—</strong></div>
          <div class="stat"><span>Luas perhitungan order</span><strong id="orderArea">—</strong></div>
          <div class="stat"><span>Cakupan efektif per bundle</span><strong id="coverage">—</strong></div>
          <div class="stat"><span id="coveredLabel">Cakupan bundle yang dibeli</span><strong id="covered">—</strong></div>
          <div class="stat"><span>Sisa cakupan teoritis*</span><strong id="remainder">—</strong></div>
        </div>
        <div class="actions"><button class="btn primary" id="printBtn" type="button">Cetak / Simpan PDF</button><button class="btn outline" id="copyBtn" type="button">Salin Hasil</button></div>
        <div class="warn"><b>Estimasi awal, bukan BOQ final.</b> Belum termasuk starter, nok, jurai, underlayment, flashing, dek, fastener, dan item sistem atap lainnya. *Sisa teoritis adalah kelebihan akibat pembulatan, bukan stok utuh yang pasti bisa dipakai.</div>
        <p class="kicker">Rumus: jumlah bundle = pembulatan ke atas [(total luas aktual × (1 + waste/100)) ÷ cakupan per bundle].</p>
        <p id="status" class="kicker" aria-live="polite"></p>
      </section>
    </aside>
  </div>
  <p class="foot">GNET Atap Shingles | Kalkulator estimasi offline • Seluruh perhitungan dilakukan di browser perangkat Anda. Tidak mengirim data proyek ke server.</p>
</div>
<div class="mbar"><span>Jumlah bundle</span><strong id="mBundle">—</strong><a href="#hasil">Rincian ↓</a></div>

<script>
'use strict';
const COVERAGE={mosaic:2.99,fish:3.10,laminated:2.32,single:3.10};
const NAMES={mosaic:'Mosaic',fish:'Fish Scale',laminated:'Laminated',single:'Single Layer'};
const MODES={projection:{t:'Dari Denah',s:'perlu sudut'},slope:{t:'Di Atas Atap',s:'diukur langsung'},area:{t:'Luas Aktual',s:'dari QS'}};
const SHAPES={rect:'Persegi panjang',trap:'Trapesium',tri:'Segitiga'};
const TEMPLATES={
  satu:[['','rect']],
  pelana:[['Sisi depan','rect'],['Sisi belakang','rect']],
  limasan:[['Sisi depan','trap'],['Sisi belakang','trap'],['Sisi kiri','tri'],['Sisi kanan','tri']]
};
const TPL_NAMES={satu:'1 Bidang',pelana:'Pelana',limasan:'Limasan',custom:'Kustom'};
const TPL_INFO={
  satu:'<b>1 Bidang.</b> Pilih bentuknya di bawah: persegi panjang, trapesium, atau segitiga. Cocok untuk atap miring satu arah, satu sisi atap saja, atau seluruh denah sekaligus bila semua sisi punya sudut yang sama.',
  pelana:'<b>Pelana: 2 bidang persegi panjang.</b> Dari denah: a = panjang atap (sejajar nok), t = ½ lebar denah. Biasanya sudut kedua sisi sama.',
  limasan:'<b>Limasan: 2 trapesium + 2 segitiga.</b> Dari denah: trapesium a = panjang denah, b = panjang nok, t = ½ lebar denah • segitiga a = lebar denah, t = ½ × (panjang denah − panjang nok).<br><b>Jalan pintas:</b> jika sudut semua sisi sama, pilih <b>1 Bidang</b> dan isi seluruh denah sebagai persegi panjang “Dari Denah”, hasilnya sama.'
};
let activeTpl='satu',undoSnap=null;
const $=id=>document.getElementById(id);
const nf=new Intl.NumberFormat('id-ID',{minimumFractionDigits:2,maximumFractionDigits:2});
const nfx=new Intl.NumberFormat('id-ID',{maximumFractionDigits:2});
const fmt=n=>nf.format(n)+' m²';
/* angka: terima koma atau titik desimal. undefined = kosong, NaN = tidak valid */
const num=v=>{const s=String(v??'').trim().replace(',','.');if(s==='')return undefined;const n=Number(s);return Number.isFinite(n)?n:NaN;};

let nextId=1;
const planes=[];
const newPlane=init=>Object.assign({id:nextId++,name:'',mode:'projection',shape:'rect',a:'',b:'',t:'',angle:'',area:''},init||{});
const hasData=p=>['a','b','t','angle','area'].some(k=>String(p[k]??'').trim()!=='');

function evalPlane(p){
  if(p.mode==='area'){
    const A=num(p.area);
    if(A===undefined)return{status:'empty'};
    if(!(A>0))return{status:'error',msg:'luas harus angka lebih dari 0'};
    return{status:'ok',area:A};
  }
  const keys=p.shape==='trap'?['a','b','t']:['a','t'];
  const v={};keys.forEach(k=>v[k]=num(p[k]));
  if(p.mode==='projection')v.angle=num(p.angle);
  if(Object.values(v).some(x=>x===undefined))return{status:'empty'};
  if(keys.some(k=>!(v[k]>0)))return{status:'error',msg:'ukuran harus angka lebih dari 0'};
  let area=p.shape==='rect'?v.a*v.t:p.shape==='trap'?(v.a+v.b)/2*v.t:v.a*v.t/2;
  const warns=[];
  if(p.mode==='projection'){
    const g=v.angle;
    if(!(g>=1&&g<=75))return{status:'error',msg:'sudut kemiringan harus antara 1° dan 75°'};
    if(g<15)warns.push('Sudut di bawah 15°. Cek kemiringan minimum shingles pada spesifikasi GNET.');
    area=area/Math.cos(g*Math.PI/180);
  }
  if(p.shape==='trap'&&v.b>v.a)warns.push('Sisi nok (b) lebih panjang dari sisi talang (a). Pastikan tidak tertukar.');
  return{status:'ok',area,warn:warns.join(' ')};
}

function icon(shape){
  const s='fill="currentColor" fill-opacity=".22" stroke="currentColor" stroke-width="1.6"';
  if(shape==='rect')return `<svg viewBox="0 0 36 22" aria-hidden="true"><rect x="4" y="3" width="28" height="16" ${s}/></svg>`;
  if(shape==='trap')return `<svg viewBox="0 0 36 22" aria-hidden="true"><polygon points="3,19 33,19 25,3 11,3" ${s}/></svg>`;
  return `<svg viewBox="0 0 36 22" aria-hidden="true"><polygon points="3,19 33,19 18,3" ${s}/></svg>`;
}
function diagram(shape){
  const S='fill="#e9e6ff" stroke="#5b4fd0" stroke-width="2"';
  const D='stroke="#f28b29" stroke-width="2" stroke-dasharray="4 3"';
  const T='font-size="12" font-weight="700" fill="#180f5e"';
  const M='font-size="10" fill="#6c7891" text-anchor="middle"';
  let g='';
  if(shape==='rect'){
    g=`<rect x="20" y="24" width="120" height="60" ${S}/><line x1="152" y1="24" x2="152" y2="84" ${D}/><text x="157" y="58" ${T}>t</text><text x="80" y="16" ${M}>nok</text>`;
  }else if(shape==='trap'){
    g=`<polygon points="20,84 140,84 108,24 52,24" ${S}/><line x1="80" y1="24" x2="80" y2="84" ${D}/><text x="86" y="60" ${T}>t</text><text x="80" y="16" ${T} text-anchor="middle">b (nok)</text>`;
  }else{
    g=`<polygon points="20,84 140,84 80,24" ${S}/><line x1="80" y1="24" x2="80" y2="84" ${D}/><text x="86" y="66" ${T}>t</text><text x="80" y="16" ${M}>puncak</text>`;
  }
  return `<svg viewBox="0 0 170 112" role="img" aria-label="Panduan ukur ${SHAPES[shape]}">${g}<text x="80" y="102" ${T} text-anchor="middle">a (talang)</text></svg>`;
}
function fieldsFor(p){
  if(p.mode==='area')return[['area','Luas permukaan aktual (m²)','mis. 85,5']];
  const den=p.mode==='projection';
  const f=[['a',p.shape==='rect'?'Panjang sisi talang (a), m':'Sisi talang / bawah (a), m','mis. 10']];
  if(p.shape==='trap')f.push(['b','Sisi nok / atas (b), m','mis. 4']);
  f.push(['t',den?'Kedalaman horizontal (t), m':'Tinggi miring (t), m','mis. 4']);
  if(den)f.push(['angle','Sudut kemiringan (°)','mis. 30']);
  return f;
}
function tipFor(p){
  if(p.mode==='area')return 'Masukkan luas permukaan miring yang sudah dihitung QS/kontraktor. Angka ini tidak dikoreksi sudut lagi.';
  if(p.mode==='projection')return 'Ambil ukuran dari gambar denah atap (tampak atas), termasuk overstek. <b>t</b> = jarak horizontal dari garis talang ke garis nok/puncak. Kemiringan dikoreksi otomatis.';
  return 'Ukur langsung di permukaan atap. <b>t</b> = jarak tegak lurus dari talang ke nok/puncak, menyusuri permukaan atap'+(p.shape==='rect'?'.':', <b>bukan</b> panjang garis jurai.');
}

function renderPlanes(){
  const root=$('planes');root.innerHTML='';
  planes.forEach((p,i)=>{
    const el=document.createElement('div');el.className='plane';
    const nid='nm'+p.id,isArea=p.mode==='area';
    el.innerHTML=`<div class="planeHead"><strong>Bidang ${i+1}</strong><button type="button" class="mini">Hapus</button></div>
      <div class="field"><label for="${nid}">Nama / Kode Bidang</label><input id="${nid}" data-k="name" maxlength="70" placeholder="Contoh: Sisi depan"></div>
      <span class="grpLabel">Cara mengukur</span>
      <div class="seg" data-g="mode">${Object.entries(MODES).map(([k,v])=>`<button type="button" data-v="${k}" aria-pressed="${p.mode===k}">${v.t}<small>${v.s}</small></button>`).join('')}</div>
      ${isArea?'':`<span class="grpLabel">Bentuk bidang</span><div class="seg" data-g="shape">${Object.entries(SHAPES).map(([k,v])=>`<button type="button" data-v="${k}" aria-pressed="${p.shape===k}">${icon(k)}${v}</button>`).join('')}</div>`}
      <div class="tip">${tipFor(p)}</div>
      <div class="body${isArea?' noDiag':''}">${isArea?'':`<div class="diagram">${diagram(p.shape)}</div>`}<div class="inputs"></div></div>
      <div class="pwarn"></div>
      <div class="planeFoot"><span>Luas permukaan bidang</span><strong class="partial">—</strong></div>`;
    const nm=el.querySelector('[data-k="name"]');nm.value=p.name;
    nm.addEventListener('input',()=>{p.name=nm.value;});
    el.querySelector('.mini').addEventListener('click',()=>{planes.splice(i,1);activeTpl='custom';undoSnap=null;renderTpl();renderPlanes();calculate();});
    el.querySelectorAll('.seg button').forEach(b=>b.addEventListener('click',()=>{
      const g=b.parentElement.dataset.g,v=b.dataset.v;
      if(g==='mode'&&v==='area'&&p.mode!=='area'&&String(p.area).trim()===''){
        const r=evalPlane(p);
        if(r.status==='ok')p.area=nfx.format(Math.round(r.area*100)/100).replace(/\./g,'');
      }
      p[g]=v;renderPlanes();calculate();
    }));
    const box=el.querySelector('.inputs');
    fieldsFor(p).forEach(([k,label,ph])=>{
      const id='f'+p.id+k,c=document.createElement('div');c.className='field';
      const lab=document.createElement('label');lab.htmlFor=id;lab.textContent=label;
      const inp=document.createElement('input');inp.id=id;inp.type='text';inp.inputMode='decimal';inp.autocomplete='off';inp.placeholder=ph;inp.value=p[k]??'';
      inp.addEventListener('input',()=>{p[k]=inp.value;calculate();});
      c.append(lab,inp);box.append(c);
    });
    p.el=el;root.append(el);
  });
}

const CLEAR=['actual','wasteArea','orderArea','coverage','covered','remainder'];
function calculate(){
  const waste=num($('waste').value),type=$('type').value,cov=COVERAGE[type],errors=[];
  let total=0,incomplete=0;
  if(waste===undefined||!(waste>=0&&waste<=100))errors.push('Waste harus antara 0 dan 100%.');
  if(!planes.length)errors.push('Tambahkan minimal satu bidang atap.');
  planes.forEach((p,i)=>{
    const r=evalPlane(p);p.result=r;
    const out=p.el?.querySelector('.partial'),w=p.el?.querySelector('.pwarn');
    if(out){out.textContent=r.status==='ok'?fmt(r.area):r.status==='empty'?'Lengkapi ukuran':'Periksa input';out.classList.toggle('bad',r.status==='error');out.classList.toggle('empty',r.status==='empty');}
    if(w){w.textContent=r.warn||'';w.style.display=r.warn?'block':'none';}
    if(r.status==='ok')total+=r.area;else if(r.status==='empty')incomplete++;else errors.push('Bidang '+(i+1)+': '+r.msg+'.');
  });
  if(total>1e7)errors.push('Total luas terlalu besar. Periksa satuan input (meter).');
  const err=$('error');err.style.display=errors.length?'block':'none';err.textContent=errors.join(' ');
  const hint=$('hint'),showHint=!errors.length&&incomplete>0;
  hint.style.display=showHint?'block':'none';
  hint.textContent=incomplete===planes.length?'Isi ukuran bidang atap untuk melihat jumlah bundle.':`Lengkapi ukuran pada ${incomplete} bidang lagi untuk melihat hasil.`;
  $('rtype').textContent=NAMES[type]+' • '+nf.format(cov)+' m²/bundle';
  if(errors.length||incomplete){
    $('bundle').innerHTML='— <span>bundle</span>';CLEAR.forEach(id=>$(id).textContent='—');
    $('coveredLabel').textContent='Cakupan bundle yang dibeli';$('mBundle').textContent='—';
    window.lastResult=null;return;
  }
  const extra=total*waste/100,order=total+extra,n=Math.ceil(order/cov-1e-10),covered=n*cov;
  $('bundle').innerHTML=n+' <span>bundle</span>';
  $('actual').textContent=fmt(total);
  $('wasteArea').textContent=fmt(extra)+' ('+nfx.format(waste)+'%)';
  $('orderArea').textContent=fmt(order);
  $('coverage').textContent=fmt(cov);
  $('coveredLabel').textContent=`Cakupan ${n} bundle (${n} × ${nf.format(cov)} m²)`;
  $('covered').textContent=fmt(covered);
  $('remainder').textContent=fmt(Math.max(0,covered-order));
  $('mBundle').textContent=n+' bundle';
  window.lastResult={total,extra,order,n,type,waste,covered};
}

function describe(p){
  if(p.mode==='area')return 'luas aktual';
  const m=x=>nfx.format(num(x))+' m';
  let s=SHAPES[p.shape]+', '+MODES[p.mode].t.toLowerCase()+': a '+m(p.a);
  if(p.shape==='trap')s+=', b '+m(p.b);
  s+=', t '+m(p.t);
  if(p.mode==='projection')s+=', '+nfx.format(num(p.angle))+'°';
  return s;
}
function fmtDate(v){if(!v)return'-';const d=new Date(v+'T00:00:00');return isNaN(d)?v:d.toLocaleDateString('id-ID',{day:'numeric',month:'long',year:'numeric'});}
function summary(){
  const r=window.lastResult;if(!r)return'';
  return['ESTIMASI GNET ATAP SHINGLES',
    'Proyek: '+($('project').value||'-'),
    'Tanggal: '+fmtDate($('date').value),
    'Tipe: '+NAMES[r.type]+' ('+nf.format(COVERAGE[r.type])+' m²/bundle)',
    'Bentuk atap: '+TPL_NAMES[activeTpl]+' ('+planes.length+' bidang)','',
    'Rincian bidang:',
    ...planes.map((p,i)=>(i+1)+'. '+(p.name||'Bidang '+(i+1))+' — '+describe(p)+' → '+fmt(p.result.area)),'',
    'Luas permukaan aktual: '+fmt(r.total),
    'Waste: '+nfx.format(r.waste)+'% ('+fmt(r.extra)+')',
    'Luas perhitungan order: '+fmt(r.order),
    'JUMLAH BUNDLE YANG DIBELI: '+r.n+' bundle','',
    'Estimasi awal, belum termasuk aksesoris dan wajib verifikasi gambar kerja.'].join('\n');
}

const plain=p=>{const {el,result,...rest}=p;return{...rest};};
function renderTpl(){
  document.querySelectorAll('[data-tpl]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.tpl===activeTpl)));
  let html=activeTpl==='custom'
    ?`<b>Kustom: ${planes.length} bidang.</b> Susunan bidang sudah diubah manual. Pilih salah satu bentuk di atas untuk mulai ulang.`
    :TPL_INFO[activeTpl];
  if(undoSnap)html+=`<span class="undo">Ukuran bidang sebelumnya sudah diganti. <button type="button" class="linkBtn" id="undoTpl">Batalkan</button></span>`;
  $('tplInfo').innerHTML=html;
  const u=$('undoTpl');
  if(u)u.addEventListener('click',()=>{
    planes.length=0;undoSnap.planes.forEach(p=>planes.push({...p}));
    activeTpl=undoSnap.tpl;undoSnap=null;renderTpl();renderPlanes();calculate();
  });
}
function applyTemplate(k){
  if(k===activeTpl)return;
  undoSnap=planes.some(hasData)?{tpl:activeTpl,planes:planes.map(plain)}:null;
  const first=planes.find(p=>p.mode!=='area');
  const carry=first?{mode:first.mode,angle:first.mode==='projection'?first.angle:''}:{};
  planes.length=0;
  TEMPLATES[k].forEach(([name,shape])=>planes.push(newPlane({...carry,name,shape})));
  activeTpl=k;renderTpl();renderPlanes();calculate();
}

document.querySelectorAll('[data-tpl]').forEach(b=>b.addEventListener('click',()=>applyTemplate(b.dataset.tpl)));
$('type').addEventListener('change',calculate);
$('waste').addEventListener('input',calculate);
$('addBtn').addEventListener('click',()=>{const last=planes[planes.length-1];planes.push(newPlane(last?{mode:last.mode,angle:last.mode==='projection'?last.angle:''}:{}));activeTpl='custom';undoSnap=null;renderTpl();renderPlanes();calculate();});
$('printBtn').addEventListener('click',()=>{if(window.lastResult)window.print();else $('status').textContent='Lengkapi seluruh input sebelum mencetak.';});
$('copyBtn').addEventListener('click',async()=>{
  if(!window.lastResult){$('status').textContent='Lengkapi seluruh input sebelum menyalin.';return;}
  const value=summary();
  try{await navigator.clipboard.writeText(value);$('status').textContent='Ringkasan berhasil disalin.';}
  catch(e){const t=document.createElement('textarea');t.value=value;document.body.append(t);t.select();const ok=document.execCommand('copy');t.remove();$('status').textContent=ok?'Ringkasan berhasil disalin.':'Browser membatasi fitur salin. Gunakan cetak / PDF.';}
});

$('date').value=new Date().toLocaleDateString('sv-SE');
planes.push(newPlane());renderTpl();renderPlanes();calculate();
</script>
</body>
</html>
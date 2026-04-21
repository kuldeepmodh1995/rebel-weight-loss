import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="REBEL — Weight Loss Program",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
  #MainMenu, header, footer,
  [data-testid="stToolbar"],
  [data-testid="stDecoration"],
  [data-testid="stStatusWidget"],
  .stDeployButton { display: none !important; }

  html, body { margin: 0 !important; padding: 0 !important; overflow: hidden; }

  [data-testid="stAppViewContainer"],
  [data-testid="stMain"],
  .main, .block-container,
  [data-testid="stVerticalBlock"],
  [data-testid="stVerticalBlockBorderWrapper"] {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100vw !important;
    width: 100vw !important;
  }

  iframe {
    position: fixed !important;
    top: 0 !important; left: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    border: none !important;
    z-index: 9999 !important;
  }
</style>
""", unsafe_allow_html=True)

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>REBEL — The Weight Loss Program You Were Never Supposed to Find</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600;700;900&family=Playfair+Display:ital,wght@1,700&display=swap" rel="stylesheet"/>
  <style>
    :root {
      --black: #080808; --deep: #0d0d0d;
      --red: #c0392b; --hot: #e74c3c;
      --gold: #f39c12; --white: #f5f5f5; --grey: #888;
    }
    *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
    html { scroll-behavior: smooth; }
    body { background:var(--black); color:var(--white); font-family:'Inter',sans-serif; overflow-x:hidden; }

    /* ── TICKER ── */
    .ticker-wrap { background:var(--red); padding:.55rem 0; overflow:hidden; white-space:nowrap; position:relative; z-index:50; }
    .ticker-wrap::before,.ticker-wrap::after { content:''; position:absolute; top:0; width:80px; height:100%; z-index:1; }
    .ticker-wrap::before { left:0; background:linear-gradient(to right,var(--red),transparent); }
    .ticker-wrap::after  { right:0; background:linear-gradient(to left, var(--red),transparent); }
    .ticker { display:inline-flex; animation:tick 35s linear infinite; }
    .ticker span { font-family:'Bebas Neue',sans-serif; font-size:.95rem; letter-spacing:.18em; padding:0 2.5rem; color:#fff; }
    .ticker span::after { content:'★'; margin-left:2.5rem; opacity:.45; }
    @keyframes tick { from{transform:translateX(0)} to{transform:translateX(-50%)} }

    /* ── HERO ── */
    #hero { min-height:100vh; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:6rem 2rem 4rem; position:relative; overflow:hidden; }
    .hero-bg { position:absolute; inset:0; background:radial-gradient(ellipse at center,#200000 0%,#080808 65%); }
    .hero-grid { position:absolute; inset:0; background-image:repeating-linear-gradient(0deg,transparent,transparent 79px,rgba(192,57,43,.035) 79px,rgba(192,57,43,.035) 80px); }
    .hero-inner { position:relative; z-index:1; max-width:960px; }
    .eyebrow { font-size:.72rem; letter-spacing:.35em; text-transform:uppercase; color:var(--hot); margin-bottom:1.5rem; display:flex; align-items:center; justify-content:center; gap:1rem; }
    .eyebrow::before,.eyebrow::after { content:''; width:40px; height:1px; background:var(--hot); }
    .hero-title { font-family:'Bebas Neue',sans-serif; font-size:clamp(3.8rem,13vw,9.5rem); line-height:.88; letter-spacing:.015em; margin-bottom:1.6rem; }
    .hero-title .w { color:var(--white); display:block; }
    .hero-title .r { color:var(--hot); display:block; text-shadow:0 0 70px rgba(231,76,60,.55); }
    .hero-title .g { color:var(--gold); display:block; text-shadow:0 0 50px rgba(243,156,18,.45); }
    .hero-sub { font-size:clamp(.95rem,1.8vw,1.25rem); color:var(--grey); line-height:1.85; margin-bottom:2.5rem; max-width:680px; margin-left:auto; margin-right:auto; }
    .hero-sub b { color:var(--white); font-weight:600; }
    .badge { display:inline-flex; align-items:center; gap:.75rem; border:1px solid rgba(192,57,43,.4); padding:.7rem 1.4rem; position:relative; overflow:hidden; margin-bottom:2rem; }
    .badge::before { content:''; position:absolute; inset:0; background:rgba(192,57,43,.07); }
    .dot { width:8px; height:8px; border-radius:50%; background:var(--hot); animation:pulse 1.6s ease-in-out infinite; }
    .badge-txt { font-size:.75rem; letter-spacing:.18em; text-transform:uppercase; color:var(--hot); font-weight:600; }
    @keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.35;transform:scale(1.6)} }
    .hero-cta { display:inline-block; background:var(--red); color:#fff; font-family:'Bebas Neue',sans-serif; font-size:1.3rem; letter-spacing:.15em; padding:1rem 2.5rem; cursor:pointer; border:none; clip-path:polygon(10px 0%,100% 0%,calc(100% - 10px) 100%,0% 100%); transition:all .3s; text-decoration:none; }
    .hero-cta:hover { background:var(--hot); transform:translateY(-2px); box-shadow:0 12px 35px rgba(231,76,60,.45); }

    /* ── SHARED ── */
    section { position:relative; z-index:1; }
    .container { max-width:1100px; margin:0 auto; padding:0 2rem; }
    .s-label { font-size:.68rem; letter-spacing:.45em; text-transform:uppercase; color:var(--hot); margin-bottom:.85rem; }
    .s-title { font-family:'Bebas Neue',sans-serif; font-size:clamp(2.4rem,7vw,5rem); line-height:.98; letter-spacing:.02em; margin-bottom:1.4rem; }
    .reveal { opacity:0; transform:translateY(28px); transition:opacity .7s ease,transform .7s ease; }
    .reveal.on { opacity:1; transform:none; }

    /* ── WARNING ── */
    #warning { background:var(--red); padding:5rem 2rem; text-align:center; position:relative; overflow:hidden; }
    #warning::before { content:'⚠'; position:absolute; font-size:22rem; opacity:.05; top:50%; left:50%; transform:translate(-50%,-50%); pointer-events:none; }
    #warning h2 { font-family:'Bebas Neue',sans-serif; font-size:clamp(2rem,6vw,4.5rem); letter-spacing:.04em; margin-bottom:1.6rem; }
    #warning p { font-size:clamp(.95rem,1.9vw,1.2rem); line-height:1.95; max-width:820px; margin:0 auto 1.4rem; opacity:.92; }
    #warning .hindi { font-style:italic; border-left:3px solid rgba(255,255,255,.45); padding-left:1.5rem; text-align:left; max-width:700px; margin:2rem auto; font-size:clamp(1rem,2.2vw,1.3rem); line-height:1.9; opacity:.88; }
    .warn-box { max-width:780px; margin:2.5rem auto 0; border:2px solid rgba(255,255,255,.25); padding:2rem; background:rgba(0,0,0,.15); }
    .warn-box p { font-size:clamp(1rem,2vw,1.2rem); font-weight:600; }

    /* ── PILLARS ── */
    #pillars { padding:8rem 2rem; background:var(--deep); }
    .p-header { text-align:center; margin-bottom:4.5rem; }
    .p-header p { color:var(--grey); max-width:560px; margin:.8rem auto 0; line-height:1.75; }
    .p-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(290px,1fr)); gap:1.4rem; }
    .p-card { border:1px solid #1e1e1e; padding:2.5rem; background:var(--black); position:relative; overflow:hidden; transition:all .4s; }
    .p-card::before { content:''; position:absolute; top:0; left:0; width:3px; height:0; background:var(--hot); transition:height .4s; }
    .p-card:hover { transform:translateY(-5px); box-shadow:0 22px 65px rgba(0,0,0,.55); border-color:#2a2a2a; }
    .p-card:hover::before { height:100%; }
    .p-letter { font-family:'Bebas Neue',sans-serif; font-size:5rem; color:rgba(192,57,43,.1); line-height:1; margin-bottom:.4rem; transition:color .4s; }
    .p-card:hover .p-letter { color:rgba(192,57,43,.22); }
    .p-word { font-family:'Bebas Neue',sans-serif; font-size:1.55rem; letter-spacing:.1em; color:var(--hot); margin-bottom:.9rem; }
    .p-desc { color:var(--grey); font-size:.93rem; line-height:1.75; }
    .p-span { grid-column:1/-1; max-width:420px; margin:0 auto; }

    /* ── SECRET ── */
    #secret { padding:8rem 2rem; text-align:center; background:#050505; position:relative; }
    #secret::before { content:''; position:absolute; inset:0; background:radial-gradient(ellipse at center,rgba(243,156,18,.06) 0%,transparent 68%); }
    .s-box { border:1px solid rgba(243,156,18,.22); max-width:820px; margin:0 auto; padding:4rem 3rem; position:relative; background:rgba(243,156,18,.02); }
    .s-box::before,.s-box::after { content:'✦'; position:absolute; font-size:1.5rem; color:var(--gold); opacity:.35; }
    .s-box::before { top:.9rem; left:1.4rem; }
    .s-box::after  { bottom:.9rem; right:1.4rem; }
    .s-box h2 { font-family:'Bebas Neue',sans-serif; font-size:clamp(2rem,5vw,3.5rem); color:var(--gold); letter-spacing:.05em; margin-bottom:1.4rem; text-shadow:0 0 45px rgba(243,156,18,.35); }
    .s-box p  { color:var(--grey); font-size:1.05rem; line-height:1.85; margin-bottom:1.4rem; }
    .s-box p b { color:var(--white); }
    .lock { font-size:3.8rem; margin-bottom:1.4rem; display:block; filter:drop-shadow(0 0 22px rgba(243,156,18,.55)); }

    /* ── PROGRAM ── */
    #program { padding:8rem 2rem; background:var(--deep); }
    .prog-hd { text-align:center; margin-bottom:4.5rem; }
    .prog-hd p { color:var(--grey); font-size:1.05rem; max-width:600px; margin:.8rem auto 0; line-height:1.75; }
    .steps { display:grid; grid-template-columns:repeat(auto-fit,minmax(270px,1fr)); gap:1.4rem; margin-bottom:3rem; }
    .step { padding:2rem; border:1px solid #181818; background:var(--black); position:relative; transition:all .3s; }
    .step:hover { border-color:rgba(243,156,18,.2); }
    .step-n  { font-family:'Bebas Neue',sans-serif; font-size:3rem; color:rgba(243,156,18,.14); line-height:1; margin-bottom:.4rem; }
    .step-sub{ font-size:.82rem; color:var(--gold); letter-spacing:.12em; text-transform:uppercase; margin-bottom:.6rem; }
    .step-ttl{ font-weight:700; font-size:.98rem; letter-spacing:.04em; color:var(--white); margin-bottom:.5rem; }
    .step-d  { color:var(--grey); font-size:.88rem; line-height:1.65; }
    .lock-ov { position:absolute; inset:0; background:rgba(8,8,8,.87); display:flex; align-items:center; justify-content:center; font-size:1.4rem; opacity:0; transition:opacity .3s; backdrop-filter:blur(3px); }
    .step:hover .lock-ov { opacity:1; }
    .locked-hard .lock-ov { opacity:1 !important; background:rgba(8,8,8,.96); }

    /* ── TRANSFORMATION ── */
    #transform { padding:8rem 2rem; background:var(--black); text-align:center; }
    .tx-wrap { display:flex; align-items:center; justify-content:center; gap:2.5rem; margin:4rem 0; flex-wrap:wrap; }
    .tx-box { width:210px; height:270px; border:1px solid #222; display:flex; flex-direction:column; align-items:center; justify-content:center; position:relative; overflow:hidden; }
    .tx-box.bef { border-color:#333; background:#0a0a0a; }
    .tx-box.bef::before { content:''; position:absolute; inset:0; background:repeating-linear-gradient(-45deg,transparent,transparent 4px,rgba(255,255,255,.01) 4px,rgba(255,255,255,.01) 5px); }
    .tx-box.aft { border-color:rgba(192,57,43,.45); background:#100000; box-shadow:0 0 45px rgba(192,57,43,.12); }
    .tx-lbl { position:absolute; bottom:.9rem; font-size:.68rem; letter-spacing:.3em; text-transform:uppercase; }
    .tx-ico { font-size:3rem; margin-bottom:.5rem; opacity:.3; }
    .tx-ico.fire { opacity:.85; filter:drop-shadow(0 0 12px rgba(192,57,43,.6)); }
    .tx-arr { font-family:'Bebas Neue',sans-serif; font-size:2.8rem; color:var(--hot); display:flex; flex-direction:column; align-items:center; gap:.2rem; }
    .tx-arr small { font-family:'Inter',sans-serif; font-size:.68rem; letter-spacing:.2em; color:var(--grey); }

    /* ── PROOF ── */
    #proof { padding:8rem 2rem; background:var(--deep); text-align:center; }
    .stats { display:flex; justify-content:center; gap:4rem; flex-wrap:wrap; margin:3rem 0 5rem; }
    .stat-n { font-family:'Bebas Neue',sans-serif; font-size:clamp(3rem,8vw,5.5rem); color:var(--hot); line-height:1; text-shadow:0 0 32px rgba(231,76,60,.32); }
    .stat-l { font-size:.72rem; letter-spacing:.28em; text-transform:uppercase; color:var(--grey); margin-top:.4rem; }
    .tgrid { display:grid; grid-template-columns:repeat(auto-fit,minmax(290px,1fr)); gap:1.4rem; text-align:left; }
    .tcard { border:1px solid #1a1a1a; padding:2rem; background:var(--black); position:relative; }
    .tcard::before { content:'"'; position:absolute; top:-.4rem; left:1.4rem; font-size:4rem; font-family:'Playfair Display',serif; color:var(--hot); opacity:.38; line-height:1; }
    .ttext { color:var(--grey); font-size:.93rem; line-height:1.72; margin-bottom:1.4rem; padding-top:1rem; }
    .tauth { display:flex; align-items:center; gap:.75rem; }
    .av { width:40px; height:40px; border-radius:50%; background:var(--red); display:flex; align-items:center; justify-content:center; font-family:'Bebas Neue',sans-serif; font-size:1rem; color:#fff; flex-shrink:0; }
    .av-name { font-weight:600; font-size:.88rem; color:var(--white); }
    .av-role { font-size:.72rem; color:var(--grey); }
    .stars { color:var(--gold); font-size:.82rem; margin-bottom:.45rem; }
    .divider { display:flex; align-items:center; gap:1.5rem; margin:4rem 0; }
    .divider::before,.divider::after { content:''; flex:1; height:1px; background:linear-gradient(to right,transparent,#222,transparent); }
    .divider span { font-family:'Bebas Neue',sans-serif; font-size:1.1rem; letter-spacing:.3em; color:#2e2e2e; }

    /* ── FOUNDERS ── */
    #founders { padding:8rem 2rem; background:var(--black); }
    .f-grid { display:grid; grid-template-columns:1fr 1fr; gap:2.5rem; margin-top:3.5rem; }
    @media(max-width:760px){ .f-grid{ grid-template-columns:1fr; } }
    .f-card { border:1px solid #1c1c1c; padding:3rem 2.5rem; background:var(--deep); position:relative; overflow:hidden; }
    .f-card::after { content:''; position:absolute; bottom:0; left:0; right:0; height:3px; background:linear-gradient(to right,var(--red),transparent); }
    .f-init { width:76px; height:76px; background:var(--red); display:flex; align-items:center; justify-content:center; font-family:'Bebas Neue',sans-serif; font-size:1.9rem; color:#fff; margin-bottom:1.4rem; clip-path:polygon(10px 0%,100% 0%,calc(100% - 10px) 100%,0% 100%); }
    .f-name  { font-family:'Bebas Neue',sans-serif; font-size:1.75rem; letter-spacing:.07em; margin-bottom:.2rem; }
    .f-title { font-size:.72rem; letter-spacing:.2em; text-transform:uppercase; color:var(--hot); margin-bottom:1.4rem; }
    .f-bio   { color:var(--grey); font-size:.93rem; line-height:1.82; }
    .f-bio b { color:var(--white); }

    /* ── REGISTER ── */
    #register { padding:8rem 2rem; background:var(--deep); text-align:center; position:relative; overflow:hidden; }
    #register::before { content:''; position:absolute; inset:0; background:radial-gradient(ellipse at center top,rgba(192,57,43,.1) 0%,transparent 60%); }
    .reg-wrap { max-width:600px; margin:0 auto; position:relative; z-index:1; }
    .reg-wrap h2 { font-family:'Bebas Neue',sans-serif; font-size:clamp(2.4rem,7vw,5rem); letter-spacing:.03em; line-height:1; margin-bottom:1rem; }
    .reg-wrap h2 span { color:var(--hot); }
    .reg-wrap > p { color:var(--grey); font-size:1rem; line-height:1.75; margin-bottom:2.5rem; }
    .fg { margin-bottom:1rem; }
    .fg input,.fg select { width:100%; background:var(--black); border:1px solid #222; color:var(--white); padding:1rem 1.4rem; font-family:'Inter',sans-serif; font-size:.93rem; outline:none; transition:border-color .3s; }
    .fg input:focus,.fg select:focus { border-color:var(--red); }
    .fg input::placeholder { color:#3a3a3a; }
    .fg select { color:#3a3a3a; appearance:none; cursor:pointer; }
    .fg select:focus { color:var(--white); }
    .chk { display:flex; align-items:flex-start; gap:.7rem; text-align:left; margin-bottom:2rem; }
    .chk input { width:auto; margin-top:3px; accent-color:var(--red); cursor:pointer; flex-shrink:0; }
    .chk label { font-size:.83rem; color:var(--grey); line-height:1.55; cursor:pointer; }
    .btn { width:100%; background:var(--red); color:#fff; border:none; padding:1.2rem 2rem; font-family:'Bebas Neue',sans-serif; font-size:1.45rem; letter-spacing:.15em; cursor:pointer; transition:all .3s; clip-path:polygon(12px 0%,100% 0%,calc(100% - 12px) 100%,0% 100%); position:relative; overflow:hidden; }
    .btn::before { content:''; position:absolute; top:0; left:-100%; width:100%; height:100%; background:linear-gradient(to right,transparent,rgba(255,255,255,.1),transparent); transition:left .5s; }
    .btn:hover::before { left:100%; }
    .btn:hover { background:var(--hot); transform:translateY(-2px); box-shadow:0 15px 40px rgba(231,76,60,.42); }
    #ok { display:none; background:rgba(0,150,50,.1); border:1px solid rgba(0,200,80,.3); padding:1.4rem; margin-top:1rem; color:#4caf50; font-size:.93rem; line-height:1.6; }
    .reg-note { margin-top:1.4rem; font-size:.78rem; color:#3a3a3a; line-height:1.6; }

    /* ── FOOTER ── */
    footer { background:#000; padding:3rem 2rem; text-align:center; border-top:1px solid #111; }
    .f-logo { font-family:'Bebas Neue',sans-serif; font-size:2rem; letter-spacing:.22em; color:var(--hot); margin-bottom:.8rem; }
    footer p { color:#2e2e2e; font-size:.78rem; letter-spacing:.1em; }

    /* ── FLOAT CTA ── */
    .float-btn { position:fixed; bottom:2rem; right:2rem; background:var(--red); color:#fff; border:none; padding:.85rem 1.5rem; font-family:'Bebas Neue',sans-serif; font-size:.95rem; letter-spacing:.1em; cursor:pointer; clip-path:polygon(8px 0%,100% 0%,calc(100% - 8px) 100%,0% 100%); z-index:999; display:none; transition:all .3s; }
    .float-btn:hover { background:var(--hot); transform:translateY(-2px); box-shadow:0 10px 28px rgba(231,76,60,.5); }

    /* ── RESPONSIVE ── */
    @media(max-width:600px){
      .stats{ gap:2rem; }
      .tx-wrap{ flex-direction:column; }
      .tx-arr{ transform:rotate(90deg); }
      .s-box{ padding:2.5rem 1.4rem; }
    }
  </style>
</head>
<body>

<!-- TICKER -->
<div class="ticker-wrap">
  <div class="ticker">
    <span>300+ LIVES TRANSFORMED</span><span>ONLY 100 SPOTS — COHORT IV</span>
    <span>3 SECRET INGREDIENTS</span><span>NO SHORTCUTS. NO EXCUSES.</span>
    <span>RESULTS IN 90 DAYS</span><span>CELEBRITIES' BEST-KEPT SECRET</span>
    <span>DIET IS STEP 11. EXERCISE IS STEP 12.</span><span>ARE YOU THE RARE 10%?</span>
    <span>300+ LIVES TRANSFORMED</span><span>ONLY 100 SPOTS — COHORT IV</span>
    <span>3 SECRET INGREDIENTS</span><span>NO SHORTCUTS. NO EXCUSES.</span>
    <span>RESULTS IN 90 DAYS</span><span>CELEBRITIES' BEST-KEPT SECRET</span>
    <span>DIET IS STEP 11. EXERCISE IS STEP 12.</span><span>ARE YOU THE RARE 10%?</span>
  </div>
</div>

<!-- HERO -->
<section id="hero">
  <div class="hero-bg"></div>
  <div class="hero-grid"></div>
  <div class="hero-inner">
    <div class="eyebrow">The Program Nobody Was Supposed to Find</div>
    <h1 class="hero-title">
      <span class="w">YOU WERE</span>
      <span class="r">NEVER</span>
      <span class="w">THIS CLOSE</span>
      <span class="g">TO THE TRUTH.</span>
    </h1>
    <p class="hero-sub">
      Diet and exercise? That's <b>step 11 and 12.</b><br/>
      The first 10 steps are what the world never told you —<br/>
      what celebrities use and will <b>never admit to.</b> Until now.
    </p>
    <div class="badge">
      <span class="dot"></span>
      <span class="badge-txt">Cohort IV — Only 100 Spots — Closes When Full</span>
    </div>
    <br/>
    <a class="hero-cta" href="#register">I WANT IN — SHOW ME THE TRUTH</a>
  </div>
</section>

<!-- WARNING -->
<section id="warning">
  <div class="container reveal">
    <h2>⚠ STOP. THIS IS NOT FOR YOU.</h2>
    <p>
      This program is <b>not for 90% of people.</b> Before you go any further, you need to be honest with yourself.<br/>
      <b>Are you truly ready to change — or are you just looking for another shortcut?</b>
    </p>

    <div class="warn-box">
      <p>
        If you are <b>fat and just looking to lose weight</b> — close this tab.<br/>
        If you are <b>lazy</b> — close this tab.<br/>
        If you are comfortable with what God gave you and taking it for granted — <b>close this tab right now.</b>
      </p>
    </div>

    <div class="hindi">
      Agar aapko Mounjaro, Ozempic chahiye — toh jaldi se ye website bandh karo.<br/>
      Main blunt hoon kyunki <b>sachai sunne ki zaroorat hai.</b><br/><br/>
      Aapko is planet pe exist karne ka bhi haq nahi agar aap apni zindagi ke saath itna laaparwah ho.<br/><br/>
      Agar aapka attitude dhila-dhala hai… sochte ho <em>"kal karlenge"</em>, <em>"aaj so jate hain"</em>, <em>"Monday se shuru karenge"</em><br/>
      — toh ye program aapke liye nahi hai. <b>Kabhi nahi tha. Kabhi nahi hoga.</b>
    </div>

    <p style="margin-top:2rem;">
      This program is built for the <b>rare 10%.</b><br/>
      The ones who feel the fire even when no one is watching.<br/>
      The ones who are sick and tired of being sick and tired.<br/>
      <b>The ones who are DONE playing small.</b>
    </p>
  </div>
</section>

<!-- PILLARS -->
<section id="pillars">
  <div class="container">
    <div class="p-header reveal">
      <div class="s-label">The PPPMART Framework</div>
      <h2 class="s-title">SEVEN FORCES.<br/>ONE TRANSFORMATION.</h2>
      <p>This isn't just a weight loss program. It is a complete identity shift — engineered on seven forces that the world's top performers live by.</p>
    </div>
    <div class="p-grid">
      <div class="p-card reveal">
        <div class="p-letter">P</div><div class="p-word">POWER</div>
        <p class="p-desc">Real power doesn't come from a pill or a procedure. It comes from unlocking the version of you that was always there — dormant, waiting. You will feel a shift you cannot explain to anyone who hasn't been through this. This is the power that changes rooms when you walk in.</p>
      </div>
      <div class="p-card reveal">
        <div class="p-letter">P</div><div class="p-word">PRESTIGE</div>
        <p class="p-desc">You'll walk into every room differently — not because you lost weight, but because you became someone who does what they say they'll do. That is the rarest, most magnetic quality in any human being. Prestige isn't given. It is earned. We show you how.</p>
      </div>
      <div class="p-card reveal">
        <div class="p-letter">P</div><div class="p-word">PASSION</div>
        <p class="p-desc">Passion is the fuel — but untrained passion burns out in days. We teach you how to make it a slow, sustained burn that lasts 90 days and beyond. After this, you won't need motivation. You'll have something far more dangerous — an obsession with becoming your best self.</p>
      </div>
      <div class="p-card reveal">
        <div class="p-letter">M</div><div class="p-word">MYSTIQUE</div>
        <p class="p-desc">There are 3 secret ingredients inside this program. Used by celebrities for decades. They will never acknowledge it. Their publicists will deny it. Their trainers will redirect you. What you're about to access has never been made public — until this program. Exclusively. Permanently.</p>
      </div>
      <div class="p-card reveal">
        <div class="p-letter">A</div><div class="p-word">ALARM</div>
        <p class="p-desc">Your body is screaming at you. Your mind is sending distress signals. Most people have learned to silence them — snooze the alarm. We'll help you hear it again and act before it is too late. The alarm has been ringing for years. Today is the day you finally pick up.</p>
      </div>
      <div class="p-card reveal">
        <div class="p-letter">R</div><div class="p-word">REBELLION</div>
        <p class="p-desc">Every person who has ever truly changed themselves did it by rejecting what was "normal." Rebel against your old patterns. Rebel against the average. Rebel against the voice in your head that says "you can't." This program is not for followers. This is where rebels are made.</p>
      </div>
      <div class="p-card reveal p-span">
        <div class="p-letter">T</div><div class="p-word">TRUST</div>
        <p class="p-desc">300+ people have walked this path before you. Their results, their bodies, their stories — they speak for themselves without us saying a word. We don't ask for blind faith. We ask you to look at the evidence, look at the proof, and make one decision that changes everything.</p>
      </div>
    </div>
  </div>
</section>

<!-- SECRET -->
<section id="secret">
  <div class="container">
    <div class="s-box reveal">
      <span class="lock">🔐</span>
      <h2>THE 3 SECRET INGREDIENTS</h2>
      <p>Every jaw-dropping celebrity transformation you've ever admired — every "How did they do that so fast?" moment — was powered by these 3 ingredients. <b>They have been the world's best-kept secret for decades.</b></p>
      <p><b>They will never tell you. Their publicists will deny it. Their trainers will redirect you.</b> Because if you knew what they know, you wouldn't need them anymore. You wouldn't need anyone.</p>
      <p>These ingredients are <b>not food. Not supplements. Not exercises.</b> They are something far more fundamental — and that is all we will say here. The world is not ready for this conversation. But <em>you</em> might be.</p>
      <p style="color:var(--gold);font-weight:600;font-size:1.05rem;">The 3 ingredients are revealed exclusively inside the program.<br/>They are waiting for you on Day 1. And they will change everything.</p>
    </div>
  </div>
</section>

<!-- PROGRAM -->
<section id="program">
  <div class="container">
    <div class="prog-hd reveal">
      <div class="s-label">The Method</div>
      <h2 class="s-title">12 STEPS.<br/>DIET &amp; EXERCISE<br/>ARE THE LAST 2.</h2>
      <p>Everything the fitness industry ever told you starts at Step 11. We start at Step 1. That single difference is why our people transform — and everyone else just tries.</p>
    </div>
    <div class="steps">
      <div class="step reveal">
        <div class="step-n">01</div>
        <div class="step-sub">The First S — Story</div>
        <div class="step-ttl">Fix Your Story First</div>
        <p class="step-d">The narrative you tell yourself every single morning is either your prison or your launchpad. Step 1 rewrites it completely. No more <em>"I've always been this way."</em> That story ends here.</p>
        <div class="lock-ov">🔒 Inside the Program</div>
      </div>
      <div class="step reveal">
        <div class="step-n">02</div>
        <div class="step-sub">The Second S — State</div>
        <div class="step-ttl">Master Your Emotional State</div>
        <p class="step-d">Your emotional state controls every decision — what you eat, when you sleep, how you move. Control the state, control the outcome. This is where most programs never go. This is where we begin.</p>
        <div class="lock-ov">🔒 Inside the Program</div>
      </div>
      <div class="step reveal">
        <div class="step-n">03</div>
        <div class="step-sub">The Third S</div>
        <div class="step-ttl">St____</div>
        <p class="step-d">Fix the first two S's, and the third becomes inevitable. It is the natural byproduct of the inner work done in Steps 1 and 2. You will not have to chase it. It will find you — quietly, permanently.</p>
        <div class="lock-ov">🔒 Inside the Program</div>
      </div>
      <div class="step reveal">
        <div class="step-n">04</div>
        <div class="step-sub">Windows &amp; Mirrors</div>
        <div class="step-ttl">Look Through — Not At</div>
        <p class="step-d">Great leaders look out the window when things go right and in the mirror when things go wrong. We teach you this lens as a transformation tool. It changes everything about how you hold yourself accountable — forever.</p>
        <div class="lock-ov">🔒 Inside the Program</div>
      </div>
      <div class="step reveal">
        <div class="step-n">05</div>
        <div class="step-sub">The Override Protocol</div>
        <div class="step-ttl">Not Being Animal Default</div>
        <p class="step-d">Your brain is hardwired to conserve energy, seek comfort, and avoid pain. That's the "animal default." Every human who has achieved something extraordinary has learned to override it. We show you the exact switch.</p>
        <div class="lock-ov">🔒 Inside the Program</div>
      </div>
      <div class="step locked-hard reveal">
        <div class="step-n" style="color:rgba(255,255,255,.04)">06 — 10</div>
        <div class="step-sub" style="color:#2a2a2a">Classified</div>
        <div class="step-ttl" style="color:#2a2a2a">5 Core Pillars. Completely Sealed.</div>
        <p class="step-d" style="color:#1e1e1e">These steps contain the heart of the entire methodology. They will not be previewed, hinted at, or summarised — anywhere. They exist only inside the program. This is non-negotiable.</p>
        <div class="lock-ov" style="opacity:1;background:rgba(8,8,8,.97)">🔒 Members Only — No Exceptions</div>
      </div>
      <div class="step reveal">
        <div class="step-n">11</div>
        <div class="step-sub">The Support Structure</div>
        <div class="step-ttl">Nutrition — Yes, Finally</div>
        <p class="step-d">By the time you reach Step 11, you won't need to be forced to eat right — you'll <em>want</em> to. Because the person you've become by this point demands it. Nutrition is the conclusion, not the starting point.</p>
      </div>
      <div class="step reveal">
        <div class="step-n">12</div>
        <div class="step-sub">The Final Layer</div>
        <div class="step-ttl">Movement &amp; Exercise</div>
        <p class="step-d">Step 12. Not Step 1. By now, exercise is a celebration of what your body can do — not a punishment for what you ate. That single mindset shift is worth the entire program on its own.</p>
      </div>
    </div>
  </div>
</section>

<!-- TRANSFORMATION -->
<section id="transform">
  <div class="container">
    <div class="reveal" style="text-align:center">
      <div class="s-label">The Promise</div>
      <h2 class="s-title">FROM THIS<br/>TO THIS.<br/>90 DAYS.</h2>
    </div>
    <div class="tx-wrap reveal">
      <div class="tx-box bef">
        <div class="tx-ico">🪞</div>
        <div style="color:#3a3a3a;font-size:.72rem;letter-spacing:.2em">BEFORE</div>
        <div class="tx-lbl" style="color:#2a2a2a">Day 1</div>
      </div>
      <div class="tx-arr">→<small>90 DAYS</small></div>
      <div class="tx-box aft">
        <div class="tx-ico fire">🔥</div>
        <div style="color:var(--hot);font-size:.72rem;letter-spacing:.2em">AFTER</div>
        <div class="tx-lbl" style="color:var(--hot)">Day 90</div>
      </div>
    </div>
    <p class="reveal" style="text-align:center;color:var(--grey);max-width:620px;margin:0 auto;font-size:1.02rem;line-height:1.85">
      Not just a different body. A different <em>person.</em> Someone who finally feels like they belong in their own skin — and in this world. That's the real transformation we deliver. The body is just the proof.
    </p>
  </div>
</section>

<!-- PROOF -->
<section id="proof">
  <div class="container">
    <div class="reveal" style="text-align:center">
      <div class="s-label">Social Proof</div>
      <h2 class="s-title">THE NUMBERS<br/>DON'T LIE.</h2>
    </div>
    <div class="stats">
      <div class="reveal"><div class="stat-n" data-target="300">300+</div><div class="stat-l">Lives Transformed</div></div>
      <div class="reveal"><div class="stat-n" data-target="90">90</div><div class="stat-l">Days to Results</div></div>
      <div class="reveal"><div class="stat-n" data-target="100">100</div><div class="stat-l">Spots This Cohort</div></div>
      <div class="reveal"><div class="stat-n" data-target="3">3</div><div class="stat-l">Secret Ingredients</div></div>
    </div>
    <div class="tgrid">
      <div class="tcard reveal">
        <div class="stars">★★★★★</div>
        <p class="ttext">"Main 3 saal se try kar raha tha. Gym, diet, everything. Kuch nahi hua. Ye program ne mujhe samjhaya ki main bilkul galat jagah se shuru kar raha tha. Step 1 ne hi sab badal diya. Pehli baar laga ki main kar sakta hoon."</p>
        <div class="tauth"><div class="av">RK</div><div><div class="av-name">Rahul K.</div><div class="av-role">Mumbai · -22kg · Cohort II</div></div></div>
      </div>
      <div class="tcard reveal">
        <div class="stars">★★★★★</div>
        <p class="ttext">"I've tried every program, every app, every influencer's advice. Nothing worked because none of them addressed the real problem — which lives in your head, not on your plate. This program actually gets it. Nothing else comes close."</p>
        <div class="tauth"><div class="av">PM</div><div><div class="av-name">Priya M.</div><div class="av-role">Delhi · -18kg · Cohort I</div></div></div>
      </div>
      <div class="tcard reveal">
        <div class="stars">★★★★★</div>
        <p class="ttext">"The 3 secret ingredients blew my mind. The moment I found out what they were, I immediately understood why no celebrity would ever admit to using them. This is the real thing. I feel like I was given access to something I was never supposed to have."</p>
        <div class="tauth"><div class="av">AS</div><div><div class="av-name">Arjun S.</div><div class="av-role">Bangalore · -25kg · Cohort III</div></div></div>
      </div>
    </div>
    <div class="divider reveal"><span>★</span></div>
    <p class="reveal" style="text-align:center;color:var(--grey);font-size:.93rem;font-style:italic;max-width:520px;margin:0 auto;line-height:1.8">
      "300+ people. Zero ads. Every single one came through word of mouth — from someone whose life was changed by this program. The results speak so loudly, they don't need us to."
    </p>
  </div>
</section>

<!-- FOUNDERS -->
<section id="founders">
  <div class="container">
    <div class="reveal" style="text-align:center">
      <div class="s-label">The Architects</div>
      <h2 class="s-title">THEY SACRIFICED<br/>THEIR 20s<br/>SO YOU DON'T HAVE TO.</h2>
    </div>
    <p class="reveal" style="text-align:center;color:var(--grey);max-width:680px;margin:.5rem auto 0;line-height:1.85;font-size:1rem;">
      While most people spent their 20s chasing fun, Ashutosh and Kuldeep Sir spent them obsessing over one question: <em>Why do intelligent, motivated people still fail to change?</em> What took them a decade to decode takes you 90 days to experience.
    </p>
    <div class="f-grid">
      <div class="f-card reveal">
        <div class="f-init">AS</div>
        <div class="f-name">Ashutosh</div>
        <div class="f-title">Co-Architect · Behavioural Transformation Specialist</div>
        <p class="f-bio">
          Ashutosh spent years deep in the science of why intelligent, motivated people consistently fail at sustaining change — not because they lack willpower, but because they're starting from entirely the wrong place.<br/><br/>
          He built <b>the first 5 steps of this framework from scratch</b>, testing obsessively until the results became undeniable. His work is the reason our students don't quit at Week 3 like every other program. He made the program <b>stick.</b>
        </p>
      </div>
      <div class="f-card reveal">
        <div class="f-init">KS</div>
        <div class="f-name">Kuldeep Sir</div>
        <div class="f-title">Co-Architect · Peak Performance Coach</div>
        <p class="f-bio">
          Kuldeep Sir's life obsession has always been one question: <em>What separates the people who transform from the people who just try?</em> After years of research, coaching, and brutal personal experimentation, the answer became this program.<br/><br/>
          He is the reason <b>the 3 secret ingredients were ever discovered.</b> He is the reason this program produces results that look impossible from the outside. He makes the program <b>work.</b>
        </p>
      </div>
    </div>
    <div class="reveal" style="margin-top:2.5rem;text-align:center;border:1px solid #1a1a1a;padding:2rem;background:var(--deep)">
      <p style="color:var(--grey);font-size:.95rem;line-height:1.85">
        Together, they created something that <b style="color:var(--white)">does not exist anywhere else on this planet.</b><br/>
        Not in any book. Not in any YouTube channel. Not in any ₹299 course you've already tried.<br/>
        <b style="color:var(--hot)">This is the only place. And it won't be available forever.</b>
      </p>
    </div>
  </div>
</section>

<!-- REGISTER -->
<section id="register">
  <div class="container">
    <div class="reg-wrap">
      <div class="s-label reveal">Final Warning</div>
      <h2 class="reveal">REGISTER.<br/><span>IF YOU DARE.</span></h2>
      <p class="reveal">
        Do not register until you have read every single word above and made a real, irreversible decision.<br/>
        This is not for laggards. This is not for losers. This is for the rare few who are done playing small.<br/><br/>
        <b style="color:var(--hot)">Only 100 spots. Cohort IV. No exceptions. No extensions. No begging.</b>
      </p>
      <form id="reg-form" onsubmit="handleSubmit(event)" class="reveal">
        <div class="fg"><input type="text" placeholder="Your Full Name" required/></div>
        <div class="fg"><input type="email" placeholder="Email Address" required/></div>
        <div class="fg"><input type="tel" placeholder="WhatsApp Number (India)" required/></div>
        <div class="fg">
          <select required>
            <option value="" disabled selected>How much weight do you want to lose?</option>
            <option value="5-10">5–10 kg</option>
            <option value="10-20">10–20 kg</option>
            <option value="20-30">20–30 kg</option>
            <option value="30+">30+ kg</option>
          </select>
        </div>
        <div class="chk">
          <input type="checkbox" id="c1" required/>
          <label for="c1">I have read everything above. I am NOT looking for shortcuts. I commit fully to 90 days. I understand my spot can be revoked if I don't meet the program's standards of seriousness.</label>
        </div>
        <button type="submit" class="btn">CLAIM MY SPOT — I AM READY</button>
      </form>
      <div id="ok">✅ You're on the list. We'll reach out on WhatsApp within 48 hours with onboarding details. Don't make us regret picking you. 🔥</div>
      <p class="reg-note reveal">Registering does not guarantee a spot. Every application is reviewed manually. We reserve the right to decline anyone we believe is not truly ready. This is the program's commitment to its community.</p>
    </div>
  </div>
</section>

<footer>
  <div class="f-logo">REBEL</div>
  <p>© 2026 Ashutosh &amp; Kuldeep Sir · All Rights Reserved</p>
  <p style="margin-top:.4rem">Built for the 10%. The rest were never invited.</p>
</footer>

<button class="float-btn" id="fb" onclick="document.getElementById('register').scrollIntoView({behavior:'smooth'})">CLAIM YOUR SPOT →</button>

<script>
  // Float CTA on scroll
  window.addEventListener('scroll', () => {
    document.getElementById('fb').style.display = window.scrollY > 500 ? 'block' : 'none';
  });

  // Scroll reveal
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('on'); });
  }, { threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  // Counter animation
  function animCount(el, target) {
    let start = null;
    const isPlus = target >= 100;
    const step = ts => {
      if (!start) start = ts;
      const p = Math.min((ts - start) / 1400, 1);
      const v = Math.floor((1 - Math.pow(1 - p, 3)) * target);
      el.textContent = v + (isPlus ? '+' : '');
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }
  const cio = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        const t = parseInt(e.target.dataset.target);
        if (!isNaN(t)) animCount(e.target, t);
        cio.unobserve(e.target);
      }
    });
  }, { threshold: 0.5 });
  document.querySelectorAll('.stat-n[data-target]').forEach(el => cio.observe(el));

  // Form submit
  function handleSubmit(e) {
    e.preventDefault();
    document.getElementById('reg-form').style.display = 'none';
    document.getElementById('ok').style.display = 'block';
  }
</script>
</body>
</html>"""

components.html(HTML, height=800, scrolling=True)

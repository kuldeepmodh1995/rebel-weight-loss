import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="REBEL — Weight Loss Program",
    page_icon="🔥",
    layout="wide",
)

st.markdown("""
<style>
#MainMenu, header, footer { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
iframe { display: block; }
</style>
""", unsafe_allow_html=True)

HTML = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>REBEL — The Weight Loss Program You Were Never Supposed to Find</title>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600;700;900&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

      :root {
        --black: #080808;
        --deep: #0d0d0d;
        --red: #c0392b;
        --red-hot: #e74c3c;
        --gold: #f39c12;
        --gold-light: #f1c40f;
        --white: #f5f5f5;
        --grey: #888;
        --dark-grey: #1a1a1a;
      }

      * { margin: 0; padding: 0; box-sizing: border-box; }
      html { scroll-behavior: smooth; }
      body {
        background: var(--black);
        color: var(--white);
        font-family: 'Inter', sans-serif;
        overflow-x: hidden;
      }

      body::before {
        content: '';
        position: fixed;
        inset: 0;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
        pointer-events: none;
        z-index: 0;
        opacity: 0.4;
      }

      /* TICKER */
      .ticker-wrap {
        background: var(--red);
        padding: 0.6rem 0;
        overflow: hidden;
        white-space: nowrap;
        position: relative;
        z-index: 10;
      }
      .ticker-wrap::before, .ticker-wrap::after {
        content: '';
        position: absolute;
        top: 0;
        width: 80px;
        height: 100%;
        z-index: 1;
      }
      .ticker-wrap::before { left: 0; background: linear-gradient(to right, var(--red), transparent); }
      .ticker-wrap::after  { right: 0; background: linear-gradient(to left, var(--red), transparent); }
      .ticker {
        display: inline-flex;
        animation: ticker 30s linear infinite;
      }
      .ticker span {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 1rem;
        letter-spacing: 0.15em;
        padding: 0 2rem;
        color: #fff;
      }
      .ticker span::after { content: '★'; margin-left: 2rem; opacity: 0.5; }
      @keyframes ticker {
        0%   { transform: translateX(0); }
        100% { transform: translateX(-50%); }
      }

      /* HERO */
      #hero {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 6rem 2rem 4rem;
        position: relative;
        overflow: hidden;
      }
      .hero-bg {
        position: absolute;
        inset: 0;
        background: radial-gradient(ellipse at center, #1a0000 0%, #080808 70%);
        z-index: 0;
      }
      .hero-lines {
        position: absolute;
        inset: 0;
        background-image: repeating-linear-gradient(
          0deg, transparent, transparent 80px,
          rgba(192,57,43,0.03) 80px, rgba(192,57,43,0.03) 81px
        );
        z-index: 0;
      }
      .hero-content { position: relative; z-index: 1; max-width: 900px; }
      .eyebrow {
        font-size: 0.75rem;
        letter-spacing: 0.3em;
        text-transform: uppercase;
        color: var(--red-hot);
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1rem;
      }
      .eyebrow::before, .eyebrow::after { content: ''; width: 40px; height: 1px; background: var(--red-hot); }
      .hero-title {
        font-family: 'Bebas Neue', sans-serif;
        font-size: clamp(3.5rem, 12vw, 9rem);
        line-height: 0.9;
        letter-spacing: 0.02em;
        margin-bottom: 1.5rem;
      }
      .hero-title .line-red   { color: var(--red-hot); display: block; text-shadow: 0 0 60px rgba(231,76,60,0.5); }
      .hero-title .line-white { color: var(--white); display: block; }
      .hero-title .line-gold  { color: var(--gold); display: block; text-shadow: 0 0 40px rgba(243,156,18,0.4); }
      .hero-sub {
        font-size: clamp(1rem, 2vw, 1.3rem);
        color: var(--grey);
        line-height: 1.8;
        margin-bottom: 3rem;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
      }
      .hero-sub em { color: var(--white); font-style: normal; font-weight: 600; }
      .cohort-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.75rem;
        border: 1px solid rgba(192,57,43,0.4);
        padding: 0.75rem 1.5rem;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
      }
      .cohort-badge::before { content: ''; position: absolute; inset: 0; background: rgba(192,57,43,0.08); }
      .cohort-badge .dot {
        width: 8px; height: 8px; border-radius: 50%;
        background: var(--red-hot);
        animation: pulse 1.5s ease-in-out infinite;
      }
      .cohort-badge span { font-size: 0.8rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--red-hot); font-weight: 600; }
      @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50%       { opacity: 0.4; transform: scale(1.5); }
      }

      /* SECTION BASE */
      section { position: relative; z-index: 1; }
      .container { max-width: 1100px; margin: 0 auto; padding: 0 2rem; }
      .section-label { font-size: 0.7rem; letter-spacing: 0.4em; text-transform: uppercase; color: var(--red-hot); margin-bottom: 1rem; }
      .section-title { font-family: 'Bebas Neue', sans-serif; font-size: clamp(2.5rem, 7vw, 5rem); line-height: 1; letter-spacing: 0.02em; margin-bottom: 1.5rem; }

      /* WARNING */
      #warning { background: var(--red); padding: 5rem 2rem; text-align: center; position: relative; overflow: hidden; }
      #warning::before { content: '⚠'; position: absolute; font-size: 20rem; opacity: 0.06; top: 50%; left: 50%; transform: translate(-50%, -50%); }
      #warning h2 { font-family: 'Bebas Neue', sans-serif; font-size: clamp(2rem, 6vw, 4.5rem); letter-spacing: 0.05em; margin-bottom: 2rem; }
      #warning p { font-size: clamp(1rem, 2vw, 1.25rem); line-height: 1.9; max-width: 800px; margin: 0 auto 1.5rem; opacity: 0.9; }
      #warning .hindi { font-size: clamp(1.1rem, 2.5vw, 1.4rem); font-style: italic; opacity: 0.85; border-left: 3px solid rgba(255,255,255,0.5); padding-left: 1.5rem; text-align: left; max-width: 700px; margin: 2rem auto; }

      /* PILLARS */
      #pillars { padding: 8rem 2rem; background: var(--deep); }
      .pillars-header { text-align: center; margin-bottom: 5rem; }
      .pillars-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; }
      .pillar-card { border: 1px solid #1e1e1e; padding: 2.5rem; position: relative; overflow: hidden; transition: all 0.4s ease; background: var(--black); }
      .pillar-card::before { content: ''; position: absolute; top: 0; left: 0; width: 3px; height: 0; background: var(--red-hot); transition: height 0.4s ease; }
      .pillar-card:hover { border-color: #2a2a2a; transform: translateY(-4px); box-shadow: 0 20px 60px rgba(0,0,0,0.5); }
      .pillar-card:hover::before { height: 100%; }
      .pillar-letter { font-family: 'Bebas Neue', sans-serif; font-size: 5rem; color: rgba(192,57,43,0.12); line-height: 1; margin-bottom: 0.5rem; transition: color 0.4s; }
      .pillar-card:hover .pillar-letter { color: rgba(192,57,43,0.25); }
      .pillar-word { font-family: 'Bebas Neue', sans-serif; font-size: 1.6rem; letter-spacing: 0.1em; color: var(--red-hot); margin-bottom: 1rem; }
      .pillar-desc { color: var(--grey); font-size: 0.95rem; line-height: 1.7; }

      /* SECRET */
      #secret { padding: 8rem 2rem; text-align: center; background: #050505; position: relative; overflow: hidden; }
      #secret::before { content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse at center, rgba(243,156,18,0.05) 0%, transparent 70%); }
      .secret-box { border: 1px solid rgba(243,156,18,0.2); max-width: 800px; margin: 0 auto; padding: 4rem 3rem; position: relative; background: rgba(243,156,18,0.02); }
      .secret-box::before, .secret-box::after { content: '✦'; position: absolute; font-size: 1.5rem; color: var(--gold); opacity: 0.4; }
      .secret-box::before { top: 1rem; left: 1.5rem; }
      .secret-box::after  { bottom: 1rem; right: 1.5rem; }
      .secret-box h2 { font-family: 'Bebas Neue', sans-serif; font-size: clamp(2rem, 5vw, 3.5rem); color: var(--gold); letter-spacing: 0.05em; margin-bottom: 1.5rem; text-shadow: 0 0 40px rgba(243,156,18,0.3); }
      .secret-box p { color: var(--grey); font-size: 1.1rem; line-height: 1.8; margin-bottom: 1.5rem; }
      .secret-box p strong { color: var(--white); }
      .lock-icon { font-size: 4rem; margin-bottom: 1.5rem; display: block; filter: drop-shadow(0 0 20px rgba(243,156,18,0.5)); }

      /* PROGRAM */
      #program { padding: 8rem 2rem; background: var(--deep); }
      .program-header { text-align: center; margin-bottom: 5rem; }
      .program-header p { color: var(--grey); font-size: 1.1rem; max-width: 600px; margin: 1rem auto 0; line-height: 1.7; }
      .steps-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; margin-bottom: 4rem; }
      .step-card { padding: 2rem; border: 1px solid #181818; background: var(--black); position: relative; transition: all 0.3s; }
      .step-card:hover { border-color: rgba(243,156,18,0.2); }
      .step-number { font-family: 'Bebas Neue', sans-serif; font-size: 3rem; color: rgba(243,156,18,0.15); line-height: 1; margin-bottom: 0.5rem; }
      .step-title { font-weight: 700; font-size: 1rem; letter-spacing: 0.05em; margin-bottom: 0.5rem; color: var(--white); }
      .step-subtitle { font-size: 0.85rem; color: var(--gold); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.75rem; }
      .step-desc { color: var(--grey); font-size: 0.9rem; line-height: 1.6; }
      .locked-overlay { position: absolute; inset: 0; background: rgba(8,8,8,0.85); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; opacity: 0; transition: opacity 0.3s; backdrop-filter: blur(2px); }
      .step-card:hover .locked-overlay { opacity: 1; }
      .step-card.revealed .locked-overlay { display: none; }

      /* TRANSFORMATION */
      #transformation { padding: 8rem 2rem; background: var(--black); text-align: center; }
      .transform-visual { display: flex; align-items: center; justify-content: center; gap: 2rem; margin: 4rem 0; flex-wrap: wrap; }
      .transform-box { width: 220px; height: 280px; border: 1px solid #222; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--grey); position: relative; overflow: hidden; }
      .transform-box.before { border-color: #333; background: #0a0a0a; }
      .transform-box.before::before { content: ''; position: absolute; inset: 0; background: repeating-linear-gradient(-45deg, transparent, transparent 4px, rgba(255,255,255,0.01) 4px, rgba(255,255,255,0.01) 5px); }
      .transform-box.after  { border-color: rgba(192,57,43,0.4); background: #0f0000; box-shadow: 0 0 40px rgba(192,57,43,0.1); }
      .transform-box .box-label { position: absolute; bottom: 1rem; font-size: 0.7rem; letter-spacing: 0.3em; }
      .transform-box .box-icon  { font-size: 3rem; margin-bottom: 0.5rem; opacity: 0.3; }
      .transform-arrow { font-family: 'Bebas Neue', sans-serif; font-size: 3rem; color: var(--red-hot); display: flex; flex-direction: column; align-items: center; gap: 0.25rem; }
      .transform-arrow small { font-size: 0.7rem; letter-spacing: 0.2em; font-family: 'Inter', sans-serif; color: var(--grey); }

      /* SOCIAL PROOF */
      #proof { padding: 8rem 2rem; background: var(--deep); text-align: center; }
      .stats-row { display: flex; justify-content: center; gap: 4rem; flex-wrap: wrap; margin: 3rem 0 5rem; }
      .stat-item { text-align: center; }
      .stat-number { font-family: 'Bebas Neue', sans-serif; font-size: clamp(3rem, 8vw, 5.5rem); color: var(--red-hot); line-height: 1; text-shadow: 0 0 30px rgba(231,76,60,0.3); }
      .stat-label  { font-size: 0.75rem; letter-spacing: 0.25em; text-transform: uppercase; color: var(--grey); margin-top: 0.5rem; }
      .testimonials { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; text-align: left; }
      .testimonial { border: 1px solid #1a1a1a; padding: 2rem; background: var(--black); position: relative; }
      .testimonial::before { content: '"'; position: absolute; top: -0.5rem; left: 1.5rem; font-size: 4rem; font-family: 'Playfair Display', serif; color: var(--red-hot); opacity: 0.4; line-height: 1; }
      .testimonial-text { color: var(--grey); font-size: 0.95rem; line-height: 1.7; margin-bottom: 1.5rem; padding-top: 1rem; }
      .testimonial-author { display: flex; align-items: center; gap: 0.75rem; }
      .author-avatar { width: 40px; height: 40px; border-radius: 50%; background: var(--red); display: flex; align-items: center; justify-content: center; font-family: 'Bebas Neue', sans-serif; font-size: 1.1rem; color: #fff; flex-shrink: 0; }
      .author-info .name { font-weight: 600; font-size: 0.9rem; color: var(--white); }
      .author-info .role { font-size: 0.75rem; color: var(--grey); letter-spacing: 0.05em; }
      .stars { color: var(--gold); font-size: 0.85rem; margin-bottom: 0.5rem; }

      /* FOUNDERS */
      #founders { padding: 8rem 2rem; background: var(--black); }
      .founders-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; margin-top: 4rem; }
      @media (max-width: 768px) { .founders-grid { grid-template-columns: 1fr; } }
      .founder-card { border: 1px solid #1a1a1a; padding: 3rem 2.5rem; position: relative; overflow: hidden; background: var(--deep); }
      .founder-card::after { content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 3px; background: linear-gradient(to right, var(--red), transparent); }
      .founder-initials { width: 80px; height: 80px; background: var(--red); display: flex; align-items: center; justify-content: center; font-family: 'Bebas Neue', sans-serif; font-size: 2rem; letter-spacing: 0.05em; color: #fff; margin-bottom: 1.5rem; clip-path: polygon(10px 0%, 100% 0%, calc(100% - 10px) 100%, 0% 100%); }
      .founder-name  { font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; letter-spacing: 0.08em; margin-bottom: 0.25rem; }
      .founder-title { font-size: 0.75rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--red-hot); margin-bottom: 1.5rem; }
      .founder-bio   { color: var(--grey); font-size: 0.95rem; line-height: 1.8; }
      .founder-bio strong { color: var(--white); }

      /* REGISTER */
      #register { padding: 8rem 2rem; background: var(--deep); text-align: center; position: relative; overflow: hidden; }
      #register::before { content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse at center top, rgba(192,57,43,0.1) 0%, transparent 60%); }
      .register-box { max-width: 600px; margin: 0 auto; position: relative; z-index: 1; }
      .register-box h2 { font-family: 'Bebas Neue', sans-serif; font-size: clamp(2.5rem, 7vw, 5rem); letter-spacing: 0.03em; margin-bottom: 1rem; line-height: 1; }
      .register-box h2 span { color: var(--red-hot); }
      .register-box > p { color: var(--grey); font-size: 1rem; line-height: 1.7; margin-bottom: 2.5rem; }
      .form-group { margin-bottom: 1rem; }
      .form-group input { width: 100%; background: var(--black); border: 1px solid #222; color: var(--white); padding: 1rem 1.5rem; font-family: 'Inter', sans-serif; font-size: 0.95rem; outline: none; transition: border-color 0.3s; }
      .form-group input:focus { border-color: var(--red); }
      .form-group input::placeholder { color: #444; }
      .form-group select { width: 100%; background: var(--black); border: 1px solid #222; color: #444; padding: 1rem 1.5rem; font-family: 'Inter', sans-serif; font-size: 0.95rem; outline: none; transition: border-color 0.3s; appearance: none; cursor: pointer; }
      .form-group select:focus { border-color: var(--red); color: var(--white); }
      .checkbox-group { display: flex; align-items: flex-start; gap: 0.75rem; text-align: left; margin-bottom: 2rem; }
      .checkbox-group input[type='checkbox'] { width: auto; margin-top: 3px; accent-color: var(--red); cursor: pointer; }
      .checkbox-group label { font-size: 0.85rem; color: var(--grey); line-height: 1.5; cursor: pointer; }
      .btn-primary { width: 100%; background: var(--red); color: #fff; border: none; padding: 1.25rem 2rem; font-family: 'Bebas Neue', sans-serif; font-size: 1.5rem; letter-spacing: 0.15em; cursor: pointer; transition: all 0.3s; clip-path: polygon(12px 0%, 100% 0%, calc(100% - 12px) 100%, 0% 100%); position: relative; overflow: hidden; }
      .btn-primary::before { content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%; background: linear-gradient(to right, transparent, rgba(255,255,255,0.1), transparent); transition: left 0.5s; }
      .btn-primary:hover::before { left: 100%; }
      .btn-primary:hover { background: var(--red-hot); transform: translateY(-2px); box-shadow: 0 15px 40px rgba(231,76,60,0.4); }
      .register-note { margin-top: 1.5rem; font-size: 0.8rem; color: #444; line-height: 1.6; }

      /* FOOTER */
      footer { background: #000; padding: 3rem 2rem; text-align: center; border-top: 1px solid #111; }
      .footer-logo { font-family: 'Bebas Neue', sans-serif; font-size: 2rem; letter-spacing: 0.2em; color: var(--red-hot); margin-bottom: 1rem; }
      footer p { color: #333; font-size: 0.8rem; letter-spacing: 0.1em; }

      /* FLOATING CTA */
      .floating-cta { position: fixed; bottom: 2rem; right: 2rem; background: var(--red); color: #fff; border: none; padding: 0.875rem 1.5rem; font-family: 'Bebas Neue', sans-serif; font-size: 1rem; letter-spacing: 0.1em; cursor: pointer; transition: all 0.3s; z-index: 100; clip-path: polygon(8px 0%, 100% 0%, calc(100% - 8px) 100%, 0% 100%); display: none; animation: floatIn 0.5s ease forwards; }
      .floating-cta:hover { background: var(--red-hot); transform: translateY(-2px); box-shadow: 0 10px 30px rgba(231,76,60,0.5); }
      @keyframes floatIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

      /* SCROLL ANIMATIONS */
      .reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.7s ease, transform 0.7s ease; }
      .reveal.visible { opacity: 1; transform: translateY(0); }

      /* SUCCESS MESSAGE */
      #success-msg { display: none; background: rgba(0,150,50,0.1); border: 1px solid rgba(0,200,80,0.3); padding: 1.5rem; margin-top: 1rem; color: #4caf50; font-size: 0.95rem; line-height: 1.6; }

      /* DIVIDER */
      .divider { display: flex; align-items: center; gap: 1.5rem; margin: 4rem 0; }
      .divider::before, .divider::after { content: ''; flex: 1; height: 1px; background: linear-gradient(to right, transparent, #222, transparent); }
      .divider span { font-family: 'Bebas Neue', sans-serif; font-size: 1.2rem; letter-spacing: 0.3em; color: #333; }

      @media (max-width: 600px) {
        .stats-row { gap: 2.5rem; }
        .transform-visual { flex-direction: column; }
        .transform-arrow { transform: rotate(90deg); }
        .secret-box { padding: 2.5rem 1.5rem; }
      }
    </style>
  </head>
  <body>
    <div class="ticker-wrap">
      <div class="ticker">
        <span>300+ TRANSFORMATIONS</span><span>ONLY 100 SPOTS AVAILABLE</span>
        <span>3 SECRET INGREDIENTS</span><span>NO SHORTCUTS. NO EXCUSES.</span>
        <span>RESULTS IN 90 DAYS</span><span>CELEBRITIES' BEST-KEPT SECRET</span>
        <span>300+ TRANSFORMATIONS</span><span>ONLY 100 SPOTS AVAILABLE</span>
        <span>3 SECRET INGREDIENTS</span><span>NO SHORTCUTS. NO EXCUSES.</span>
        <span>RESULTS IN 90 DAYS</span><span>CELEBRITIES' BEST-KEPT SECRET</span>
      </div>
    </div>

    <section id="hero">
      <div class="hero-bg"></div>
      <div class="hero-lines"></div>
      <div class="hero-content">
        <div class="eyebrow">The Program Nobody Was Supposed to Know About</div>
        <h1 class="hero-title">
          <span class="line-white">YOU WERE</span>
          <span class="line-red">NEVER</span>
          <span class="line-white">THIS CLOSE</span>
          <span class="line-gold">TO THE TRUTH.</span>
        </h1>
        <p class="hero-sub">
          Diet and exercise? That's <em>step 11 and 12.</em><br />
          The first 10 steps are what the world never told you — what celebrities use and will <em>never admit to.</em> Until now.
        </p>
        <div class="cohort-badge">
          <span class="dot"></span>
          <span>Cohort IV — Only 100 Spots — Closes When Full</span>
        </div>
      </div>
    </section>

    <section id="warning">
      <div class="container reveal">
        <h2>STOP. READ THIS FIRST.</h2>
        <p>
          This program is <strong>not for 90% of you.</strong><br />
          Before you go any further, you need to ask yourself one question.<br /><br />
          <strong>Are you truly ready to change — or are you just looking for another shortcut?</strong>
        </p>
        <h2 style="margin-top:2rem;">⚠ THIS IS NOT FOR YOU.</h2>
        <p>
          If you are <strong>fat and looking to lose weight</strong> — this is not for you.<br />
          If you are <strong>lazy</strong> — this is not for you.<br />
          If you are comfortable, complacent, and taking everything God gave you for granted — <strong>close this tab.</strong>
        </p>
        <div class="hindi">
          Agar aapko Mounjaro, Ozempic chahiye — toh jaldi se ye website bandh kare. Main blunt hoon kyunki aapko sachai sunne ki zaroorat hai.<br /><br />
          Agar aapka attitude dhila-dhala hai… sochte ho "kal karlenge", "aaj so jate hain", "Monday se shuru karenge" — toh ye program aapke liye nahi hai. Kabhi nahi tha. Kabhi nahi hoga.
        </div>
        <p>This program is built for the <strong>rare 10%</strong> — the ones who feel the fire even when no one is watching. The ones who are sick and tired of being sick and tired.</p>
      </div>
    </section>

    <section id="pillars">
      <div class="container">
        <div class="pillars-header reveal">
          <div class="section-label">The PPPMART Framework</div>
          <h2 class="section-title">SEVEN FORCES.<br />ONE TRANSFORMATION.</h2>
          <p style="color:var(--grey);max-width:550px;margin:0 auto;line-height:1.7">This isn't just a weight loss program. It's a complete identity shift built on seven fundamental forces.</p>
        </div>
        <div class="pillars-grid">
          <div class="pillar-card reveal">
            <div class="pillar-letter">P</div><div class="pillar-word">POWER</div>
            <p class="pillar-desc">Real power doesn't come from a pill or a procedure. It comes from unlocking the version of you that was always there — dormant, waiting. You will feel a shift you cannot explain to anyone who hasn't been through this.</p>
          </div>
          <div class="pillar-card reveal">
            <div class="pillar-letter">P</div><div class="pillar-word">PRESTIGE</div>
            <p class="pillar-desc">You'll walk into every room differently. Not because you lost weight. Because you became someone who does what they say they'll do. That is the rarest, most respected quality in any human being.</p>
          </div>
          <div class="pillar-card reveal">
            <div class="pillar-letter">P</div><div class="pillar-word">PASSION</div>
            <p class="pillar-desc">Passion is the fuel — but untrained passion burns out. We teach you how to sustain it. How to make the fire a slow burn that lasts 90 days and beyond. You won't need motivation after this. You'll have something better.</p>
          </div>
          <div class="pillar-card reveal">
            <div class="pillar-letter">M</div><div class="pillar-word">MYSTIQUE</div>
            <p class="pillar-desc">There are 3 secret ingredients inside this program. They have been used by celebrities for decades. They will never acknowledge it. They will never share it. What you're about to access has never been made public before.</p>
          </div>
          <div class="pillar-card reveal">
            <div class="pillar-letter">A</div><div class="pillar-word">ALARM</div>
            <p class="pillar-desc">Your body is sending you signals. Your mind is sending you signals. Most people have learned to silence them. We'll help you listen again — and act before it's too late. The alarm is ringing. The question is: will you pick up?</p>
          </div>
          <div class="pillar-card reveal">
            <div class="pillar-letter">R</div><div class="pillar-word">REBELLION</div>
            <p class="pillar-desc">Every person who has ever changed the world — or just changed their own body — did it by rejecting what was "normal." Rebel against your old patterns. Rebel against the average. Be the exception. This is where winners are made.</p>
          </div>
          <div class="pillar-card reveal" style="grid-column:1/-1;max-width:400px;margin:0 auto">
            <div class="pillar-letter">T</div><div class="pillar-word">TRUST</div>
            <p class="pillar-desc">300+ people have walked this path before you. Their stories, their bodies, their results — they speak for themselves. We don't ask for blind faith. We ask you to look at the evidence and make a decision.</p>
          </div>
        </div>
      </div>
    </section>

    <section id="secret">
      <div class="container">
        <div class="secret-box reveal">
          <span class="lock-icon">🔐</span>
          <h2>THE 3 SECRET INGREDIENTS</h2>
          <p>Almost every major celebrity transformation you've ever admired — every jaw-dropping "before and after" that made you think <em>"How did they do that so fast?"</em> — was powered by these 3 ingredients.</p>
          <p><strong>They will never tell you. Their publicists will deny it. Their trainers will redirect you.</strong> Because if you knew what they know, you wouldn't need them anymore.</p>
          <p>These ingredients are not food. They are not supplements. They are not exercises. They are something far more fundamental — and that is all we will say here.</p>
          <p style="color:var(--gold);font-weight:600">The 3 ingredients are revealed exclusively inside the program.<br />They are waiting for you on Day 1.</p>
        </div>
      </div>
    </section>

    <section id="program">
      <div class="container">
        <div class="program-header reveal">
          <div class="section-label">The Method</div>
          <h2 class="section-title">12 STEPS.<br />DIET & EXERCISE ARE THE LAST 2.</h2>
          <p>Everything you've been told about weight loss starts at Step 11. We start at Step 1. That's the difference between people who try and people who transform.</p>
        </div>
        <div class="steps-grid">
          <div class="step-card reveal">
            <div class="step-number">01</div><div class="step-subtitle">The First S</div><div class="step-title">Fix Your Story</div>
            <p class="step-desc">The narrative you tell yourself every morning is either your prison or your launchpad. Step 1 is about rewriting it completely. No more "I've always been this way."</p>
            <div class="locked-overlay">🔒 Inside the Program</div>
          </div>
          <div class="step-card reveal">
            <div class="step-number">02</div><div class="step-subtitle">The Second S</div><div class="step-title">Master Your State</div>
            <p class="step-desc">Your emotional state determines every decision you make — what you eat, when you sleep, how you move. Control the state, control the outcome.</p>
            <div class="locked-overlay">🔒 Inside the Program</div>
          </div>
          <div class="step-card reveal">
            <div class="step-number">03</div><div class="step-subtitle">The Third S</div><div class="step-title">St____</div>
            <p class="step-desc">Fix the first two S's, and the third S becomes inevitable. It is the natural byproduct of the work you do in Steps 1 and 2. You won't have to chase it. It will find you.</p>
            <div class="locked-overlay">🔒 Inside the Program</div>
          </div>
          <div class="step-card reveal">
            <div class="step-number">04</div><div class="step-subtitle">Windows & Mirrors</div><div class="step-title">Look Through — Not At</div>
            <p class="step-desc">Great leaders look out the window when things go right and in the mirror when things go wrong. We teach you this lens as a transformation tool.</p>
            <div class="locked-overlay">🔒 Inside the Program</div>
          </div>
          <div class="step-card reveal">
            <div class="step-number">05</div><div class="step-subtitle">The Override Protocol</div><div class="step-title">Not Being Animal Default</div>
            <p class="step-desc">Your brain is wired to conserve energy, seek comfort, and avoid pain. That's the "animal default." Every human who has achieved something remarkable has learned to override it.</p>
            <div class="locked-overlay">🔒 Inside the Program</div>
          </div>
          <div class="step-card reveal" style="border-color:#1a1a1a">
            <div class="step-number" style="color:rgba(255,255,255,0.05)">06 — 10</div>
            <div class="step-subtitle" style="color:#333">Restricted Access</div>
            <div class="step-title" style="color:#333">5 More Pillars. Completely Sealed.</div>
            <p class="step-desc" style="color:#2a2a2a">These steps contain the core of the entire methodology. They will not be previewed, summarized, or hinted at.</p>
            <div class="locked-overlay" style="opacity:1;background:rgba(8,8,8,0.95)">🔒 Exclusively for Members</div>
          </div>
          <div class="step-card reveal">
            <div class="step-number">11</div><div class="step-subtitle">The Support System</div><div class="step-title">Nutrition (Yes, Finally)</div>
            <p class="step-desc">By the time you reach Step 11, you won't need to be forced to eat right. You'll want to. Because the person you've become by this point demands it.</p>
          </div>
          <div class="step-card reveal">
            <div class="step-number">12</div><div class="step-subtitle">The Final Layer</div><div class="step-title">Movement & Exercise</div>
            <p class="step-desc">Step 12. Not Step 1. By now, exercise is a celebration of what your body can do — not a punishment for what you ate. That shift alone is worth the entire program.</p>
          </div>
        </div>
      </div>
    </section>

    <section id="transformation">
      <div class="container">
        <div class="reveal">
          <div class="section-label">The Promise</div>
          <h2 class="section-title">FROM THIS<br />TO THIS.<br />90 DAYS.</h2>
        </div>
        <div class="transform-visual reveal">
          <div class="transform-box before">
            <div class="box-icon">🪞</div>
            <div style="color:#444;font-size:0.75rem;letter-spacing:0.15em">BEFORE</div>
            <div class="box-label" style="color:#333">Day 1</div>
          </div>
          <div class="transform-arrow">→<small>90 DAYS</small></div>
          <div class="transform-box after">
            <div class="box-icon" style="opacity:0.8;filter:drop-shadow(0 0 10px rgba(192,57,43,0.5))">🔥</div>
            <div style="font-size:0.75rem;letter-spacing:0.15em;color:var(--red-hot)">AFTER</div>
            <div class="box-label" style="color:var(--red-hot)">Day 90</div>
          </div>
        </div>
        <p class="reveal" style="color:var(--grey);max-width:600px;margin:0 auto;font-size:1.05rem;line-height:1.8">
          Not just a different body. A different person. Someone who finally feels like they belong in their own skin — and in this world. That's the real transformation we're selling. The body is just the proof.
        </p>
      </div>
    </section>

    <section id="proof">
      <div class="container">
        <div class="reveal">
          <div class="section-label">Social Proof</div>
          <h2 class="section-title">THE NUMBERS<br />DON'T LIE.</h2>
        </div>
        <div class="stats-row">
          <div class="stat-item reveal"><div class="stat-number">300+</div><div class="stat-label">Lives Transformed</div></div>
          <div class="stat-item reveal"><div class="stat-number">90</div><div class="stat-label">Days to Results</div></div>
          <div class="stat-item reveal"><div class="stat-number">100</div><div class="stat-label">Spots This Cohort</div></div>
          <div class="stat-item reveal"><div class="stat-number">3</div><div class="stat-label">Secret Ingredients</div></div>
        </div>
        <div class="testimonials">
          <div class="testimonial reveal">
            <div class="stars">★★★★★</div>
            <p class="testimonial-text">"Main 3 saal se try kar raha tha. Gym, diet, everything. Kuch nahi hua. Ye program ne mujhe samjhaya ki main galat jagah se shuru kar raha tha. Step 1 ne hi sab badal diya."</p>
            <div class="testimonial-author"><div class="author-avatar">RK</div><div class="author-info"><div class="name">Rahul K.</div><div class="role">Mumbai • Lost 22kg in Cohort II</div></div></div>
          </div>
          <div class="testimonial reveal">
            <div class="stars">★★★★★</div>
            <p class="testimonial-text">"I've tried every program. Every app. Every influencer's advice. Nothing worked because none of them addressed the real problem — which is in your head, not your plate. This program gets it."</p>
            <div class="testimonial-author"><div class="author-avatar">PM</div><div class="author-info"><div class="name">Priya M.</div><div class="role">Delhi • -18kg • Cohort I</div></div></div>
          </div>
          <div class="testimonial reveal">
            <div class="stars">★★★★★</div>
            <p class="testimonial-text">"The 3 secret ingredients blew my mind. When I found out what they were — I understood immediately why no celebrity would ever admit to using them. This is the real thing."</p>
            <div class="testimonial-author"><div class="author-avatar">AS</div><div class="author-info"><div class="name">Arjun S.</div><div class="role">Bangalore • -25kg • Cohort III</div></div></div>
          </div>
        </div>
        <div class="divider reveal"><span>★</span></div>
        <p class="reveal" style="color:var(--grey);font-size:0.95rem;font-style:italic;max-width:500px;margin:0 auto">"The stories and the people speak for themselves. We've never run an ad. Every person in every cohort came through word of mouth from someone who changed their life."</p>
      </div>
    </section>

    <section id="founders">
      <div class="container">
        <div class="reveal" style="text-align:center;margin-bottom:1rem">
          <div class="section-label">The Architects</div>
          <h2 class="section-title">THEY SPENT THEIR<br />20s SO YOU DON'T HAVE TO.</h2>
        </div>
        <p class="reveal" style="text-align:center;color:var(--grey);max-width:650px;margin:0 auto 1rem;line-height:1.8;font-size:1rem">
          Ashutosh and Kuldeep Sir didn't stumble onto this methodology. They obsessed over it. They sacrificed their 20s — the years most people spend chasing fun — to master the science and psychology of human transformation. What took them a decade to decode, takes you 90 days to experience.
        </p>
        <div class="founders-grid">
          <div class="founder-card reveal">
            <div class="founder-initials">AS</div>
            <div class="founder-name">Ashutosh</div>
            <div class="founder-title">Co-Architect · Behavioural Transformation Specialist</div>
            <p class="founder-bio">Ashutosh spent years studying why intelligent, motivated people consistently fail at sustaining change. Not because they lack willpower — but because they're starting from the wrong place. He built the <strong>first 5 steps of this framework</strong> from scratch, testing them obsessively until the results were undeniable.<br /><br />His work is the reason our students don't quit at Week 3 like every other program. He made the program <strong>stick.</strong></p>
          </div>
          <div class="founder-card reveal">
            <div class="founder-initials">KS</div>
            <div class="founder-name">Kuldeep Sir</div>
            <div class="founder-title">Co-Architect · Peak Performance Coach</div>
            <p class="founder-bio">Kuldeep Sir's obsession has always been one question: <em>What separates the people who transform from the people who try?</em> After years of research, coaching, and personal experimentation, the answer became this program.<br /><br />He is the reason the <strong>3 secret ingredients were ever discovered</strong>, the reason this program produces results that look impossible from the outside. He makes the program <strong>work.</strong></p>
          </div>
        </div>
        <div class="reveal" style="margin-top:3rem;text-align:center;border:1px solid #1a1a1a;padding:2rem;background:var(--deep)">
          <p style="color:var(--grey);font-size:0.95rem;line-height:1.8">Together, they have created something that <strong style="color:var(--white)">doesn't exist anywhere else.</strong><br />Not in any book. Not in any YouTube channel. Not in any Rs. 299 course.<br /><strong style="color:var(--red-hot)">This is the only place.</strong></p>
        </div>
      </div>
    </section>

    <section id="register">
      <div class="container">
        <div class="register-box">
          <div class="section-label reveal">Final Warning</div>
          <h2 class="reveal">REGISTER.<br /><span>IF YOU DARE.</span></h2>
          <p class="reveal">
            Do not register until you have read everything above and made a real decision. This is not for laggards. This is not for losers. This is for the rare few who are done playing small.<br /><br />
            <strong style="color:var(--red-hot)">Only 100 spots. No exceptions. No extensions.</strong>
          </p>
          <form id="reg-form" onsubmit="handleSubmit(event)" class="reveal">
            <div class="form-group"><input type="text" placeholder="Your Full Name" required /></div>
            <div class="form-group"><input type="email" placeholder="Email Address" required /></div>
            <div class="form-group"><input type="tel" placeholder="WhatsApp Number (India)" required /></div>
            <div class="form-group">
              <select required>
                <option value="" disabled selected>How much weight do you want to lose?</option>
                <option value="5-10">5–10 kg</option>
                <option value="10-20">10–20 kg</option>
                <option value="20-30">20–30 kg</option>
                <option value="30+">30+ kg</option>
              </select>
            </div>
            <div class="checkbox-group">
              <input type="checkbox" id="commit" required />
              <label for="commit">I confirm that I have read everything, I am NOT looking for shortcuts, and I am committing to 90 days of serious work. I understand that my spot can be revoked if I don't meet the program standards.</label>
            </div>
            <button type="submit" class="btn-primary">CLAIM MY SPOT — I'M READY</button>
          </form>
          <div id="success-msg">✅ You're on the list. We'll reach out on WhatsApp within 48 hours with your onboarding details. Don't make us regret picking you. 🔥</div>
          <p class="register-note reveal">By registering, you confirm that you are ready to commit fully. This is not a free trial. This is a decision. Spots are reviewed manually — registering does not guarantee a place. We reserve the right to decline applicants who we believe are not ready.</p>
        </div>
      </div>
    </section>

    <footer>
      <div class="footer-logo">REBEL</div>
      <p>© 2026 Ashutosh & Kuldeep Sir. All Rights Reserved.</p>
      <p style="margin-top:0.5rem">Built for the 10%. The rest were never invited.</p>
    </footer>

    <button class="floating-cta" id="floatBtn" onclick="document.getElementById('register').scrollIntoView({behavior:'smooth'})">CLAIM YOUR SPOT →</button>

    <script>
      window.addEventListener('scroll', () => {
        const btn = document.getElementById('floatBtn');
        btn.style.display = window.scrollY > 600 ? 'block' : 'none';
      });

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
      }, { threshold: 0.12 });
      document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

      function handleSubmit(e) {
        e.preventDefault();
        document.getElementById('reg-form').style.display = 'none';
        document.getElementById('success-msg').style.display = 'block';
      }

      function animateCounter(el, target) {
        let start = 0;
        const step = (ts) => {
          if (!start) start = ts;
          const progress = Math.min((ts - start) / 1500, 1);
          const eased = 1 - Math.pow(1 - progress, 3);
          el.textContent = Math.floor(eased * target) + (target > 10 ? '+' : '');
          if (progress < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
      }

      const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(e => {
          if (e.isIntersecting) {
            const num = parseInt(e.target.textContent);
            if (!isNaN(num)) animateCounter(e.target, num);
            counterObserver.unobserve(e.target);
          }
        });
      }, { threshold: 0.5 });
      document.querySelectorAll('.stat-number').forEach(el => counterObserver.observe(el));

      // Notify parent of full document height so Streamlit iframe resizes
      function postHeight() {
        const h = document.documentElement.scrollHeight;
        window.parent.postMessage({ type: 'streamlit:setFrameHeight', height: h }, '*');
      }
      window.addEventListener('load', postHeight);
      window.addEventListener('resize', postHeight);
    </script>
  </body>
</html>"""

components.html(HTML, height=9500, scrolling=False)

#!/usr/bin/env python3
"""Build static public pages from reviewed, disclosure-safe project data."""
from pathlib import Path
import json,html
ROOT=Path(__file__).resolve().parents[1]
D=json.loads((ROOT/'content/profile.json').read_text())
esc=lambda x:html.escape(str(x),quote=True)
def resources(items,detail=None):
 links=([['Project',f'/projects/{detail}/']] if detail else [])+items
 return '<div class="resource-links">'+''.join(f'<a href="{esc(url)}">{esc(label)}</a>' for label,url in links)+'</div>'
def shell(title,body,description,canonical='/'):
 return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><meta name="description" content="{esc(description)}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:type" content="website"><meta property="og:image" content="https://gxonu.github.io/assets/profile.jpg"><link rel="canonical" href="https://gxonu.github.io{canonical}"><link rel="stylesheet" href="/assets/site.css"></head><body><a class="skip" href="#main">Skip to content</a><header class="top"><nav class="nav" aria-label="Main navigation"><a class="brand" href="/">Geonwoo Kim</a><div class="nav-links"><a href="/#about">About</a><a href="/#research">Research</a><a href="/#projects">Projects</a><a href="/#experience">Experience</a><a href="/#awards">Awards</a></div></nav></header>{body}</body></html>'''
def footer():return '<footer class="bottom"><span>Last updated: September 2026</span><span>© 2026 Geonwoo Kim</span></footer>'
profile='''<aside class="profile" aria-label="Profile"><img class="portrait" src="/assets/profile.jpg" width="172" height="172" alt="Geonwoo Kim"><h1>Geonwoo Kim</h1><p class="ko" lang="ko">김건우</p><div class="affiliation"><strong>B.S. Student in Artificial Intelligence</strong><br>Inha University<br><br><strong>Research Intern</strong><br>DAVIAN Lab, KAIST AI</div><div class="social"><a href="/assets/GeonwooKim_CV.pdf">CV</a><a href="https://github.com/gxonu">GitHub</a><a href="https://www.linkedin.com/in/geonwoo-kim-27a599303/">LinkedIn</a></div><a class="email" href="mailto:kgw8803@gmail.com">kgw8803 [at] gmail.com</a><div class="interests"><strong>Research interests</strong>Video and 3D generation<br>Multimodal learning<br>Retrieval-grounded AI agents</div></aside>'''
about='''<section class="section" id="about"><h2>About</h2><div class="intro"><p>I'm Geonwoo Kim, a senior undergraduate in Artificial Intelligence at <a href="https://www.inha.ac.kr/">Inha University</a> and a research intern at <a href="https://davian.kaist.ac.kr/">DAVIAN Lab</a>, KAIST, advised by Prof. <a href="https://sites.google.com/site/jaegulchoo/">Jaegul Choo</a>.</p><p>I work on generative models for video and 3D. I have also built retrieval-grounded AI services as a co-founding member of Uniroad and UPFLOW. Across research and products, I care about finding the real bottleneck and making AI outputs verifiable.</p></div></section>'''
news_data=[('Sep 2026','Submitted a co-first-author paper on 3D-consistent video generation to ICLR 2027. It is currently under review.'),('Sep 2026','Won the Top Excellence Award in the graduate track of the Robot World Model AI Challenge (2nd place), as team leader.'),('Sep 2026','Completed LG Aimers 9th and finished 88th on the hackathon leaderboard.'),('May 2026','Received the Excellence Award at Inter Campus AI Challenge 2026, with Upstage.'),('Jan 2026','Joined DAVIAN Lab at KAIST AI as a research intern.')]
news='<section class="section" id="news"><h2>News</h2><ul class="news">'+''.join(f'<li><time>{esc(a)}</time><span>{esc(b)}</span></li>' for a,b in news_data)+'</ul></section>'
research='''<section class="section" id="research"><h2>Research</h2><article class="research"><p class="eyebrow">2026 / DAVIAN Lab, KAIST</p><h3>A Paper on 3D-Consistent Subject-to-Video Generation</h3><p class="status">ICLR 2027, under review / Co-first author</p><p>Generative video models that preserve a subject’s geometry and identity across changing viewpoints. Led the research from problem definition and data construction through method development, evaluation and submission.</p></article></section>'''
project_rows=[]
for p in D['projects']:
 if p.get('image'):visual=f'<img src="/assets/projects/{esc(p["image"])}" alt="{esc(p["alt"])}" loading="lazy">'
 elif p.get('diagram'):visual='<div class="diagram">'+'<span aria-hidden="true">↓</span>'.join('<b>'+esc(x)+'</b>' for x in p['diagram'])+'</div>'
 else:visual='<div class="visual-label">Diffusion models<br>Subject identity<br>Image editing</div>'
 result='<p class="result">'+esc(p['result'])+'</p>' if p.get('result') else ''
 project_rows.append(f'<article class="project-row"><div class="project-visual">{visual}</div><div><p class="eyebrow">{esc(p["year"])} / {esc(p["kind"])}</p><h3><a href="/projects/{esc(p["slug"])}/">{esc(p["title"])}</a></h3><p class="summary">{esc(p["summary"])}</p>{result}{resources(p["links"],p["slug"])}</div></article>')
projects='<section class="section" id="projects"><h2>Selected Projects</h2>'+''.join(project_rows)+'</section>'
xp=[('kaist.png','DAVIAN Lab, KAIST AI','Jan 2026 – Present','Research Intern','Generative video research, co-first-author ICLR 2027 submission.'),
(None,'Uniroad','Mar 2026 – Jul 2026','Co-founding Member / AI Researcher','Admissions data and Agentic RAG development. External support since July 2026.'),
('upflow.jpg','UPFLOW','Feb 2025 – Oct 2025','Co-founding Member / AI Researcher','MCP-based regulation collection, retrieval-grounded reports and request-form automation.'),
('multimodal.png','Multimodal AI Lab, Inha University','Dec 2024 – Dec 2025','Undergraduate Researcher','Reproduction and extension of training-free subject-driven image editing.'),
('inha.png','Inha University','Mar 2021 – Feb 2027 (expected)','B.S. in Artificial Intelligence','')]
rows=[]
for logo,org,date,role,desc in xp:
 visual=f'<img class="org-logo" src="/assets/logos/{logo}" alt="{esc(org)}" loading="lazy">' if logo else '<div aria-hidden="true"></div>'
 rows.append(f'<article class="experience">{visual}<div><div class="experience-top"><h3>{esc(org)}</h3><span class="period">{esc(date)}</span></div><div class="role">{esc(role)}</div>'+ (f'<p>{esc(desc)}</p>' if desc else '')+'</div></article>')
experience='<section class="section" id="experience"><h2>Experience &amp; Education</h2>'+''.join(rows)+'''<h3 class="subheading">Leadership</h3><div class="leadership"><strong>SINSA, AI Society at Inha University</strong><p>Vice President, June 2025 – June 2026. Organized learning programs and study activities in Python, data analysis, deep learning and paper reading.</p><p>Computer Vision study leader, March – June 2026, and RAG/Agent study leader. Designed curricula and led technical sessions and implementation practice.</p></div></section>'''
aw=[]
for date,award,event,issuer,slug,cert in D['awards']:
 links=[]
 if slug:links.append(['Project',f'/projects/{slug}/'])
 if cert:links.append(['Certificate',f'/assets/certificates/{cert}'])
 aw.append(f'<article class="award"><span class="period">{esc(date)}</span><div><p class="award-title"><strong>{esc(award)}</strong>{esc(event)}</p><p class="issuer">{esc(issuer)}</p>{resources(links) if links else ""}</div></article>')
awards='<section class="section" id="awards"><h2>Awards &amp; Honors</h2>'+''.join(aw)+'''<h3 class="subheading">Programs &amp; Qualification</h3><ul class="education-list"><li>LG Aimers 9th<span>Completed September 2026</span></li><li>4th Smart Semiconductor Academy<span>Completed March 2025, AI semiconductors, accelerators and memory</span></li><li>ADsP, Advanced Data Analytics Semi-Professional<span>March 2024</span></li><li>Business Insight micro-major<span>Marketing, branding and leadership coursework</span></li></ul></section>'''
body='<div class="layout">'+profile+'<main id="main">'+about+news+research+projects+experience+awards+footer()+'</main></div>'
(ROOT/'index.html').write_text(shell('Geonwoo Kim | AI Research and Projects',body,'AI researcher at DAVIAN Lab, KAIST, and undergraduate at Inha University. Video and 3D generation, AI products and competition projects.'))
for p in D['projects']:
 body=f'<main class="detail" id="main"><a class="back" href="/#projects">← All projects</a><p class="eyebrow">{esc(p["kind"])} / {esc(p["year"])}</p><h1>{esc(p["title"])}</h1><p class="role-line">{esc(p["role"])}</p><p class="standfirst">{esc(p["summary"])}</p>'
 if p.get('result'):body+=f'<p class="status">{esc(p["result"])}</p>'
 body+=resources(p['links'])
 if p.get('image'):body+=f'<figure><img class="hero-image" src="/assets/projects/{esc(p["image"])}" alt="{esc(p["alt"])}"><figcaption>{esc(p["alt"])}</figcaption></figure>'
 for title,copy in p['sections']:body+=f'<section class="detail-section"><h2>{esc(title)}</h2><p>{esc(copy)}</p></section>'
 body+=footer()+'</main>'
 dest=ROOT/'projects'/p['slug'];dest.mkdir(parents=True,exist_ok=True);(dest/'index.html').write_text(shell(p['title']+' | Geonwoo Kim',body,p['summary'],'/projects/'+p['slug']+'/'))
paths=['/']+['/projects/'+p['slug']+'/' for p in D['projects']]
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>https://gxonu.github.io'+x+'</loc></url>' for x in paths)+'</urlset>\n')
(ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://gxonu.github.io/sitemap.xml\n')
(ROOT/'.nojekyll').write_text('')
print('Built homepage and',len(D['projects']),'project pages')

from pathlib import Path
from html import escape
from shutil import copytree

ROOT = Path(__file__).parent
DIST = ROOT / "dist"

NAV = [
    ("Home", "/"), ("About", "/about/"), ("Solutions", "/solutions/"),
    ("Projects", "/projects/"), ("Partners", "/partners/"), ("Contact", "/contact/")
]

def link(label, href, cls="text-link"):
    return f'<a class="{cls}" href="{href}">{label}<span aria-hidden="true">↗</span></a>'

def page(title, description, active, body):
    nav = "".join(f'<a href="{href}" {"aria-current=page" if name == active else ""}>{name}</a>' for name, href in NAV)
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#071629"><title>{escape(title)} | DIGICOM</title>
<meta name="description" content="{escape(description)}">
<link rel="icon" type="image/png" href="/assets/digicom-logo.png">
<link rel="stylesheet" href="/assets/site.css"><script defer src="/assets/site.js"></script>
</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="container header-inner">
<a class="brand" href="/" aria-label="DIGICOM home"><img src="/assets/digicom-logo.png" width="199" height="45" alt="DIGICOM"><small>Technology for Digital Growth</small></a>
<button class="menu-toggle" type="button" aria-controls="primary-nav" aria-expanded="false" aria-label="Open menu"><span></span><span></span><span></span></button>
<nav id="primary-nav" class="nav" aria-label="Main navigation">{nav}<a class="nav-contact" href="/contact/">Let's connect <span aria-hidden="true">↗</span></a></nav>
</div></header>
<main id="main">{body}</main>
<footer class="site-footer"><div class="container"><div class="footer-top"><div><a class="brand footer-brand" href="/" aria-label="DIGICOM home"><img src="/assets/digicom-logo.png" width="199" height="45" alt="DIGICOM"><small>Technology for Digital Growth</small></a><p>Connecting technology, content and telecom to create digital services that grow.</p></div><div class="footer-links"><span>Explore</span><a href="/about/">About</a><a href="/solutions/">Solutions</a><a href="/projects/">Projects</a><a href="/partners/">Partners</a><a href="/contact/">Contact</a></div></div><div class="footer-bottom"><span>© 2026 DIGICOM</span><span>Digital Communication Development and Investment Joint Stock Company</span></div></div></footer>
</body></html>'''

def eyebrow(text): return f'<p class="eyebrow"><span class="eyebrow-line"></span>{text}</p>'

home = f'''
<section class="hero"><div class="container hero-grid"><div class="hero-copy">
{eyebrow('Digital Services Partner for Telecom Operators')}
<h1>DIGICOM<br><em>Technology for Digital Growth</em></h1>
<p class="hero-lead">Empowering telecom operators with digital services, technology and content.</p>
<div class="hero-actions">{link('Explore our solutions', '/solutions/', 'button button-primary')}{link('See our work', '/projects/', 'button button-ghost')}</div>
<div class="hero-proof"><div><strong>Since 2011</strong><span>Telecom experience</span></div><div><strong>7 markets</strong><span>Across Asia, Africa and the Caribbean</span></div></div>
</div><div class="hero-visual" aria-label="DIGICOM connects partners, services, operators and users"><div class="visual-label">THE DIGICOM MODEL</div><div class="orbit orbit-one"></div><div class="orbit orbit-two"></div><div class="visual-core"><span>Technology<br>& Content</span><b>DIGICOM</b><span>Telecom<br>Operators</span></div><div class="visual-caption">One connected service ecosystem <span>→</span> End users</div></div></div></section>
<section class="operator-strip"><div class="container"><span>OPERATOR EXPERIENCE</span><div>Viettel Telecom <b>·</b> Movitel <b>·</b> Lumitel <b>·</b> Nexttel <b>·</b> Telemor <b>·</b> Halotel <b>·</b> Natcom</div></div></section>
<section class="intro section"><div class="container section-head"><div>{eyebrow('What we do')}<h2>Digital services built<br><span>for telecom.</span></h2></div><p>DIGICOM helps turn technology and content into services that operators can launch and operate.</p></div><div class="container capability-grid"><article class="capability"><span class="card-num">01 / CORE CAPABILITY</span><h3>Digital Services</h3><p>Telecom VAS, digital entertainment and interactive services for operator audiences.</p><ul><li>Telecom VAS</li><li>Digital entertainment & content</li><li>Interactive & lifestyle</li></ul>{link('Explore services', '/solutions/')}</article><article class="capability"><span class="card-num">02 / CORE CAPABILITY</span><h3>Technology & Service Integration</h3><p>Partner and operator integration, localization, launch support and service operation.</p><ul><li>Platform & partner integration</li><li>Content aggregation</li><li>Service operation</li></ul>{link('How we work', '/solutions/#integration')}</article></div></section>
<section class="section proof-section"><div class="container proof-grid"><div>{eyebrow('Built through delivery')}<h2>Experience that travels<br><span>across markets.</span></h2><p>Founded in 2011, DIGICOM developed digital and telecom services in Vietnam before extending its work to operator markets in Africa, Asia and the Caribbean.</p>{link('Our story', '/about/')}</div><div class="market-list"><div><span>01</span><strong>Vietnam</strong><small>Origins in digital content and telecom VAS</small></div><div><span>02</span><strong>Africa</strong><small>Burundi · Cameroon · Tanzania · Mozambique</small></div><div><span>03</span><strong>Asia & Caribbean</strong><small>Timor-Leste · Haiti</small></div></div></div></section>
<section class="section work-section"><div class="container"><div class="section-head"><div>{eyebrow('Current service portfolio')}<h2>Services across<br><span>the operator experience.</span></h2></div><p>Our confirmed portfolio spans telecom VAS, digital entertainment and interactive services.</p></div><div class="work-grid"><article><span>TELECOM VAS</span><h3>Core services</h3><p>CRBT, MCA, Voicemail, CallPlus and iSign.</p></article><article><span>DIGITAL ENTERTAINMENT</span><h3>Content services</h3><p>MOVTV, MyClip, music and video experience.</p></article><article><span>INTERACTIVE & LIFESTYLE</span><h3>New touchpoints</h3><p>MeetMe and Meu Par.</p></article></div>{link('View selected experience', '/projects/', 'button button-outline')}</div></section>
<section class="section value-section"><div class="container"><div class="section-head"><div>{eyebrow('Our role in the value chain')}<h2>Connecting technology<br><span>to telecom.</span></h2></div><p>DIGICOM coordinates partners, content and operator integration from service concept through operation.</p></div><div class="value-chain"><div>Technology & platform partners<br>Content & service partners</div><i>→</i><strong>DIGICOM<small>Design · Integrate · Localize · Launch · Operate</small></strong><i>→</i><div>Telecom operators<br>End users</div></div></div></section>
<section class="section movitel-section"><div class="container two-col"><div>{eyebrow('Selected current experience')}<h2>Movitel<br><span>Mozambique.</span></h2><p>A multi-service digital portfolio spanning telecom VAS, entertainment and interactive services.</p>{link('Explore experience', '/projects/')}</div><div class="movitel-list"><div><b>Telecom VAS</b><span>CRBT · MCA · Voicemail · iSign</span></div><div><b>Entertainment</b><span>MOVTV · MyClip</span></div><div><b>Interactive</b><span>MeetMe · Meu Par</span></div></div></div></section>
<section class="cta-band"><div class="container"><div>{eyebrow('Work with DIGICOM')}<h2>Build the next digital service<br>together.</h2></div>{link('Contact us', '/contact/', 'button button-light')}</div></section>'''

about = f'''<section class="page-hero"><div class="container">{eyebrow('About DIGICOM')}<h1>Built on digital services.<br><em>Focused on what comes next.</em></h1><p>DIGICOM connects technology, content and telecom to develop and operate services for users across markets.</p></div></section>
<section class="section"><div class="container two-col"><div>{eyebrow('Our company')}<h2>A specialist in the space between partners and operators.</h2></div><div class="prose"><p>Founded in 2011, DIGICOM began with digital content, software and mobile applications. The company expanded into telecom value-added services in Vietnam, then into international operator markets.</p><p>Today our focus remains clear: Digital Services and Technology & Service Integration. We work across content, platforms, integration and operation to help services reach operator customers.</p><p class="legal-name">Digital Communication Development and Investment Joint Stock Company</p></div></div></section>
<section class="section history"><div class="container">{eyebrow('Our journey')}<h2>2011 to today</h2><div class="timeline"><div><strong>2011</strong><p>DIGICOM is established in Vietnam, working in digital content, software and mobile applications.</p></div><div><strong>2012</strong><p>Direct telecom integration includes SMS Gateway cooperation with Viettel Telecom.</p></div><div><strong>2014–2015</strong><p>Experience expands to Burundi, Cameroon, Timor-Leste, Tanzania and Haiti.</p></div><div><strong>Today</strong><p>A digital services partner for telecom operators, with a multi-service portfolio associated with Movitel.</p></div></div></div></section>
<section class="section"><div class="container two-col"><div>{eyebrow('Direction')}<h2>Purpose that reflects<br>our work.</h2></div><div class="prose"><h3>Vision</h3><p>To become a trusted digital services and technology partner connecting telecom operators, technology providers and digital ecosystems across emerging markets.</p><h3>Mission</h3><p>To transform technology, content and partnerships into practical digital services that create value for operators, partners and end users.</p><h3>Values</h3><p>Partnership, innovation, execution and practical value creation.</p></div></div></section>
<section class="section"><div class="container two-col"><div>{eyebrow('Our role')}<h2>Connecting the pieces that make a service work.</h2></div><div class="prose"><p>We bring technology and content partners into a practical delivery model for telecom operators. This can involve service platforms, content aggregation, integration, commercial coordination and ongoing service operation.</p>{link('Explore our capabilities', '/solutions/', 'button button-outline')}</div></div></section>'''

solutions = f'''<section class="page-hero"><div class="container">{eyebrow('Solutions')}<h1>Digital services, <em>connected end to end.</em></h1><p>Two capabilities describe the work we do and the role we play across a service lifecycle.</p></div></section>
<section class="section" id="digital-services"><div class="container">{eyebrow('01 / Digital Services')}<div class="section-head"><h2>Services people can<br><span>hear, watch and use.</span></h2><p>Digital experiences built for telecom audiences, supported by content and operating expertise.</p></div><div class="service-grid"><article><div class="service-icon">01</div><h3>Telecom Services</h3><p>Call and voice experiences that extend the core telecom service.</p><small>CRBT · MCA · Voicemail · CallPlus · iSign</small></article><article><div class="service-icon">02</div><h3>Digital Entertainment</h3><p>Music, video and TV content for operator entertainment portfolios.</p><small>Music · Video · VoD · MOVTV · MyClip</small></article><article><div class="service-icon">03</div><h3>Interactive & Lifestyle</h3><p>Services designed for participation, connection and everyday use.</p><small>MeetMe · Meu Par</small></article></div></div></section>
<section class="section integration-section" id="integration"><div class="container">{eyebrow('02 / Technology & Service Integration')}<div class="section-head"><h2>From partner capability<br><span>to operating service.</span></h2><p>We connect different contributors so an idea can work inside an operator environment.</p></div><div class="flow" aria-label="Technology and content partners connect through DIGICOM to telecom operators and end users"><div><span>01</span><strong>Technology &<br>Content Partners</strong></div><i>→</i><div class="flow-main"><span>02</span><strong>DIGICOM</strong><small>Design · integrate · localize · launch · operate</small></div><i>→</i><div><span>03</span><strong>Telecom<br>Operators</strong></div><i>→</i><div><span>04</span><strong>End Users</strong></div></div><div class="integration-list"><span>Platform integration</span><span>Content aggregation</span><span>Operator integration</span><span>Localization</span><span>Service operation</span></div></div></section>
<section class="cta-band"><div class="container"><div>{eyebrow('Explore delivery')}<h2>See the services behind<br>our capabilities.</h2></div>{link('Selected projects', '/projects/', 'button button-light')}</div></section>'''

projects = f'''<section class="page-hero"><div class="container">{eyebrow('Projects / Experience')}<h1>Telecom operator<br><em>experience across markets.</em></h1><p>Selected current and historical digital service work, grouped by operator and market.</p></div></section>
<section class="section"><div class="container">{eyebrow('Current portfolio')}<div class="project-list"><article><div><span class="card-num">MOZAMBIQUE / MOVITEL</span><h2>A multi-service digital partnership</h2><p>Current portfolio covering CRBT, MCA, Voicemail, iSign, MOVTV, MyClip, MeetMe and Meu Par.</p><div class="tags"><span>Telecom VAS</span><span>Digital entertainment</span><span>Interactive services</span></div></div><strong>Movitel</strong></article></div></div></section>
<section class="section history"><div class="container">{eyebrow('Historical operator experience')}<h2>Experience in seven markets.</h2><div class="operator-grid"><article><strong>Viettel Telecom</strong><span>Vietnam</span><p>Mobile VAS and digital content, including SMS Gateway cooperation.</p></article><article><strong>Lumitel</strong><span>Burundi</span><p>Music, CRBT and VoD.</p></article><article><strong>Nexttel</strong><span>Cameroon</span><p>VoD.</p></article><article><strong>Telemor</strong><span>Timor-Leste</span><p>VAS platforms and interactive services.</p></article><article><strong>Halotel</strong><span>Tanzania</span><p>Music, CRBT and VoD.</p></article><article><strong>Natcom</strong><span>Haiti</span><p>Music, CRBT and VoD.</p></article></div><p class="partner-note">Historical experience reflects DIGICOM's earlier company profile. Current cooperation is described separately above.</p></div></section>
<section class="cta-band"><div class="container"><div>{eyebrow('Capabilities')}<h2>Built for service delivery<br>across the value chain.</h2></div>{link('Explore solutions', '/solutions/', 'button button-light')}</div></section>'''

partners = f'''<section class="page-hero"><div class="container">{eyebrow('Partners')}<h1>A connected<br><em>service ecosystem.</em></h1><p>DIGICOM coordinates specialist technology and service partners with telecom operators.</p></div></section>
<section class="section"><div class="container two-col"><div>{eyebrow('Telecom operator experience')}<h2>Working inside<br>operator markets.</h2></div><div class="prose"><p>Viettel Telecom, Movitel, Lumitel, Nexttel, Telemor, Halotel and Natcom are part of DIGICOM's documented operator experience.</p><p>Our current multi-service portfolio is associated with Movitel in Mozambique. The other examples reflect historical experience.</p></div></div></section>
<section class="section partner-section"><div class="container">{eyebrow('Technology / platform / service partners')}<div class="partner-grid"><article><span>TECHNOLOGY & PLATFORM</span><h3>MARVEL</h3><p>Cooperation associated with MCA, Voicemail and iSign.</p></article><article><span>SERVICE PARTNER</span><h3>GST</h3><p>Cooperation associated with Meu Par.</p></article><article><span>OUTSOURCED PLATFORM PARTNER</span><h3>VNATEL</h3><p>Platform partner for CallPlus.</p></article></div><p class="partner-note">Names describe factual cooperation and do not imply endorsement. Third-party logos are not used.</p></div></section>
<section class="cta-band"><div class="container"><div>{eyebrow('Partner with us')}<h2>Bring a service idea<br>into an operator market.</h2></div>{link('Contact DIGICOM', '/contact/', 'button button-light')}</div></section>'''

contact = f'''<section class="page-hero contact-hero"><div class="container">{eyebrow('Contact')}<h1>Let's build what<br><em>comes next.</em></h1><p>Talk with DIGICOM about digital services, technology partnerships or operator integration.</p></div></section>
<section class="section"><div class="container contact-grid"><div><h2>Start a conversation.</h2><p>Tell us about the service, market or partnership you have in mind.</p><div class="contact-methods"><div><span>Email</span><a href="mailto:info@digicomjsc.com">info@digicomjsc.com</a></div><div><span>Telephone</span><a href="tel:+84462693838">(+84) 4 6269 3838</a></div><div><span>Website</span><a href="https://www.digicomjsc.com" target="_blank" rel="noopener noreferrer">www.digicomjsc.com <span aria-hidden="true">↗</span></a></div></div></div><div class="contact-card"><span class="card-num">DIGICOM OFFICE</span><h3>Visit us in Ha Noi.</h3><address>No. 2, Lane 181 Cau Dien Street<br>Phuc Dien Commune, Ha Noi, Vietnam</address><hr><small>Digital Communication Development and Investment Joint Stock Company</small></div></div></section>'''

PAGES = [
    ("index.html", "Home", "Digital services and technology integration for telecom operators.", "Home", home),
    ("about/index.html", "About", "The DIGICOM story, from 2011 to today.", "About", about),
    ("solutions/index.html", "Solutions", "DIGICOM Digital Services and Technology & Service Integration.", "Solutions", solutions),
    ("projects/index.html", "Projects", "Selected DIGICOM digital service projects and market experience.", "Projects", projects),
    ("partners/index.html", "Partners", "DIGICOM operator and technology collaborations.", "Partners", partners),
    ("contact/index.html", "Contact", "Connect with DIGICOM about digital services and partnerships.", "Contact", contact),
]

for path, title, desc, active, body in PAGES:
    out = DIST / path
    out.parent.mkdir(parents=True, exist_ok=True)
    html = page(title, desc, active, body)
    out.write_text(html, encoding="utf-8")
    root_out = ROOT / path
    root_out.parent.mkdir(parents=True, exist_ok=True)
    root_out.write_text(html, encoding="utf-8")
copytree(DIST / "assets", ROOT / "assets", dirs_exist_ok=True)
print(f"Generated {len(PAGES)} pages")

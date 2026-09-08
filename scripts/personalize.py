#!/usr/bin/env python3
"""
Calenne -> Rahat personalization script
Run from the project root: python3 scripts/personalize.py
"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILES = {
    'home':     os.path.join(BASE, 'public/index.html'),
    'about':    os.path.join(BASE, 'public/about/index.html'),
    'projects': os.path.join(BASE, 'public/projects/index.html'),
}

CSS_HIDE = (
    '#__framer-badge-container,.__framer-badge,.framer-6jWyo,[data-framer-name="Light"],'
    'a[href="https://stylokit.com/"],'
    'a[href*="framer.com/?via="],'
    'a[href="https://www.framer.com/community/marketplace/templates/calenne/"],'
    '.framer-1uwmrah-container,'
    '.framer-4w19hm-container'
    '{display:none!important;pointer-events:none!important}'
)
INJECT_AFTER = 'id="f2c-strip-template-badge">'

def r(content, old, new):
    if old not in content:
        print(f'  [!] NOT FOUND: {old[:90]!r}')
    return content.replace(old, new)

def apply(content, pairs):
    for old, new in pairs:
        content = r(content, old, new)
    return content

COMMON = [
    # Meta title
    ('Calenne \u2013 Designer portfolio template',
     'Md. Sabbir Hossain Rahat \u2014 CSE Student &amp; Software Developer'),
    # Meta description
    ('content="Bringing strategy, visual direction, and refined execution together to create meaningful digital experiences with lasting impact."',
     'content="3rd-year CSE student at Khawaja Yunus Ali University. I build software, compete in programming, explore Linux, and experiment with systems."'),
    # OG
    ('og:title" content="Calenne \u2013 Designer portfolio template"',
     'og:title" content="Md. Sabbir Hossain Rahat \u2014 CSE Student &amp; Software Developer"'),
    ('og:description" content="Bringing strategy, visual direction, and refined execution together to create meaningful digital experiences with lasting impact."',
     'og:description" content="3rd-year CSE student at Khawaja Yunus Ali University. Building software, exploring Linux, and understanding systems."'),
    ('twitter:title" content="Calenne \u2013 Designer portfolio template"',
     'twitter:title" content="Md. Sabbir Hossain Rahat \u2014 CSE Student &amp; Software Developer"'),
    ('twitter:description" content="Bringing strategy, visual direction, and refined execution together to create meaningful digital experiences with lasting impact."',
     'twitter:description" content="3rd-year CSE student at Khawaja Yunus Ali University. Building software, exploring Linux, and understanding systems."'),
    # Navbar logo
    ('>Cannele<', '>Rahat<'),
    # Nav CTA
    ('>Lets talk<', '>Say hi<'),
    # Footer Calenne strings (longer first)
    ('>About Calenne<',             '>About Rahat<'),
    ('>Calenne Studio<',            '>Khawaja Yunus Ali University<'),
    ('>© Calenne Template | Created by<', '>© Md. Sabbir Hossain Rahat<'),
    ('>Calenne<',                   '>Rahat<'),
    # Footer tagline
    ('>Creating refined digital experiences with clarity, intention, and thoughtful execution.<',
     '>CSE student and software developer. Building software, exploring Linux, and understanding systems.<'),
    # Footer section CONTACT -> LINKS
    ('>CONTACT<', '>LINKS<'),
    # Made in Framer
    ('>Made in Framer<', '>&nbsp;<'),
    # Social URLs
    ('href="https://x.com/Dmytri_Design"', 'href="https://github.com/rahativity"'),
    ('href="https://www.linkedin.com/in/dmytri-design/"', 'href="https://www.linkedin.com/in/md-sabbir-hossain-rahat-017a6b364/"'),
    ('href="https://dribbble.com/Stylokit"', 'href="https://codeforces.com/profile/Rahat001"'),
    ('href="mailto:hello@calenne.studio"', 'href="https://www.instagram.com/promithiuss?igsh=NzJwdXo1ZjBnOWk2"'),
    ('href="Tel:+1 (415) 555-0198"', 'href="https://www.facebook.com/share/1G99UNYx9w/"'),
    ('href="https://www.google.com/maps"', 'href="https://www.tumblr.com/rahathinks?source=share"'),
    # Social text
    ('>X link<',              '>GitHub<'),
    ('>Linkedin<',            '>LinkedIn<'),
    ('>Dribbble<',            '>Codeforces<'),
    ('>hello@calenne.studio<', '>Instagram<'),
    ('>+1 (415) 555-0198<',  '>Facebook<'),
    ('>San Francisco, CA<',   '>Tumblr<'),
    # Location
    ('>COPENHAGEN<',            '>BANGLADESH<'),
    ('>Copenhagen / Worldwide<', '>Bangladesh<'),
    ('>Copenhagen, Denmark<',    '>Bangladesh<'),
    ('>Copenhagen<',             '>Bangladesh<'),
    ('>Worldwide<',              '>Bangladesh<'),
    # Stats
    ('>Years of experience<', '>Year of Study<'),
    ('>Projects completed<',  '>3rd Year CSE<'),
    ('>Countries reached<',   '>KYAU<'),
    # Collaboration section
    ('>SELECTED COLLABORATIONS<', '>SELECTED WORK<'),
    ('>Work shaped through collaboration.<', ">Things I've built and explored.<"),
    ('>Great work is never the result of working alone. I collaborate with forward-thinking founders and teams to bring ideas to life with clarity purpose.<',
     ">A selection of personal projects, tools, and experiments. More coming soon.<"),
    # Project preview cards (home + about)
    ('>Lumaire<',  '>Coming Soon<'),
    ('>Serein<',   '>Coming Soon<'),
    ('>Auréline<', '>Coming Soon<'),
    ('>Nerra<',    '>Coming Soon<'),
    ('>Orsen<',    '>Coming Soon<'),
    ('>Halden<',   '>Coming Soon<'),
]

HOME = [
    # Hero
    ('>I design refined brands, websites, and interfaces for ambitious founders and creative teams.<',
     ">I'm a CSE student and software developer. I build software, compete in programming, explore Linux, and experiment with systems.<"),
    # Availability badges
    ('>AVAILABLE FOR PROJECT<', '>OPEN TO OPPORTUNITIES<'),
    ('>Open for new projects<',  '>Open to collaboration<'),
    ('>Working worldwide<',      '>Based in Bangladesh<'),
    ('>Response within 24h<',    '>Building &amp; learning<'),
    # Home-specific email link
    ('href="mailto:hello@calenne.design"', 'href="https://github.com/rahativity"'),
    ('>hello@calenne.design<', '>GitHub<'),
    # TRUSTED BY
    ('>TRUSTED BY CREATIVE TEAMS<', '>TOOLS &amp; TECHNOLOGIES<'),
    # WORKS
    ('>Design built around lasting clarity<', '>Projects built with purpose.<'),
    ('>I bring strategy, visual direction, and refined execution together to create meaningful digital experiences with lasting impact.<',
     ">I enjoy building software, experimenting with systems, and working through hard problems. A selection of what I've worked on.<"),
    ('>A curated selection of brand, web, and digital projects crafted with clarity and intention.<',
     '>A selection of software projects, tools, and experiments. More coming soon.<'),
    # Works project entries
    ('>Aures<',       '>Coming Soon<'),
    ('>Nova Studio<', '>Coming Soon<'),
    ('>Kalm Interiors<', '>Coming Soon<'),
    ('>Mokka Coffee<',   '>Coming Soon<'),
    ('>Nexora<',         '>Coming Soon<'),
    ('>Shaping a refined visual identity through thoughtful strategy, expressive details, and a clear contemporary design language.<',
     ">A project I'm working on. Details coming soon.<"),
    ('>Creating a flexible digital presence that balances creative expression, clarity, and a confident studio personality.<',
     ">A personal project around systems and tools. Details coming soon.<"),
    ('>Building a calm visual identity inspired by natural materials, considered spaces, and understated interior expression.<',
     ">Something I'm building. Details coming soon.<"),
    ('>Bringing warmth, character, and everyday ritual together through a distinctive and approachable coffee brand experience.<',
     ">A personal project. Details coming soon.<"),
    ('>Turning complex financial information into a clear, intuitive, and thoughtfully structured digital wealth experience.<',
     ">An experimental project. Details coming soon.<"),
    ('>View project<', '>Coming Soon<'),
    # SERVICES -> SKILLS
    ('>SERVICES<',  '>SKILLS<'),
    ('>What I do<', '>What I work with<'),
    ('>Services shaped around clarity<', '>Things I enjoy building and exploring.<'),
    ('>From idenity to digital experience, each service is crafted to create clear, meaningful and lasting impact.<',
     '>From competitive programming to Linux systems, here\'s what I spend my time on.<'),
    ('>Brand identity<',  '>Competitive Programming<'),
    ('>Distinctive visual systems built to make your brand feel clear, consistent, and memorable.<',
     '>C++ problem solving on Codeforces. Algorithmic challenges and contest programming.<'),
    ('>Logo syste<',  '>C++<'),
    ('>Visual identity<', '>Linux &amp; Systems<'),
    ('>Thoughtful websites shaped around strong structure, refined visuals, and intuitive user experiences.<',
     '>Arch Linux, NixOS, Hyprland, Wayland, Zsh, dotfiles, and system ricing.<'),
    ('>UX direction<',    '>Arch / NixOS<'),
    ('>UI design<',       '>Hyprland<'),
    ('>Responsive design<', '>Dotfiles<'),
    ('>Framer development<', '>Development<'),
    ('>Responsive, polished websites developed in Framer with smooth interactions and easy-to-manage content.<',
     '>Java, Python, Git, and open-source experimentation.<'),
    ('>Framer build<', '>Java<'),
    ('>CMS setup<',    '>Python<'),
    ('>Motion design<', '>Git &amp; GitHub<'),
    ('>Creative direction<', '>Homelab &amp; Networking<'),
    ('>A cohesive visual direction that brings every image, layout, and design decision into one clear vision.<',
     '>Tailscale, Wake-on-LAN, ESP32, basic networking, and self-hosting experiments.<'),
    ('>Art direction<',     '>Tailscale<'),
    ('>Campaign visuals<',  '>ESP32<'),
    ('>Content direction<', '>Self-hosting<'),
    ('>Design systems<', '>Creative<'),
    ('>Flexible design foundations that keep your brand and digital products consistent as they grow.<',
     '>Video editing with Premiere Pro and After Effects. Android modding, ADB, and device customization.<'),
    ('>UI library<',           '>Video Editing<'),
    ('>Component system<',     '>Android Modding<'),
    ('>Design documentation<', '>AMV Editing<'),
    # About section mini
    (">I'm an independent designer focused on building clear, refined brands and digital experiences. My approach combines thoughtful strategy, strong visual direction, and careful attention to detail.<",
     ">I'm a 3rd-year CSE student at Khawaja Yunus Ali University. I enjoy building software, competitive programming, exploring Linux systems, and understanding how things work.<"),
    # MY APPROACH -> HOW I WORK
    ('>MY APPROACH<', '>HOW I WORK<'),
    ('>A clear paht from idea to outcome.<', '>How I approach problems and projects.<'),
    ('>A structured, collaborative process that keeps every step intentional and every detail meaningful.<',
     '>A simple, iterative loop that keeps things moving and focused on what matters.<'),
    ('>Discover<', '>Understand<'),
    ('>Understanding your goals, audience, challenges, and the direction the project needs to take.<',
     '>Read the problem, understand the requirements, and figure out what needs to be built.<'),
    ('>Define<', '>Plan<'),
    ('>Shaping a clear strategy, structure, and visual direction before design begins.<',
     '>Break it down, choose the right tools or approach, and outline a clear path forward.<'),
    ('>Create<', '>Build<'),
    ('>Turning the direction into a refined brand identity, website, or digital experience.<',
     '>Write the code, experiment, and iterate until it works the way it should.<'),
    ('>Deliver<', '>Ship<'),
    ('>Polishing every detail and preparing a complete, ready-to-use result.<',
     ">Test, clean up, and get it out into the world.<"),
    # KIND WORDS -> GET IN TOUCH
    ('>KIND WORDS<', '>GET IN TOUCH<'),
    ('>Trusted by<', '>Find me on<'),
    ('>thoughtful clients.<', '>these platforms.<'),
    ('>Long-term relationships built on trust clear communication, and work that speaks for itself.<',
     ">I'm active on these platforms. Feel free to reach out or connect.<"),
    ('>Calenne brought clarity to a project that initially felt scattered. Every decision felt intentional.<',
     '>github.com/rahativity \u2014 open source projects, dotfiles, and code.<'),
    ('>Maya Chen<', '>GitHub<'),
    ('>Founder, Aur\u00e8s<', '>&nbsp;<'),
    ('>See on X \u2192<', '>View Profile \u2192<'),
    ('>The process was clear, thoughtful, and easy to follow. The final website felt refined, purposeful, and completely aligned with our brand.<',
     '>Competitive programming on Codeforces. Problem solving in C++.<'),
    ('>David Lee<', '>Codeforces<'),
    ('>Working with Calenne was seamless from start to finish. Every detail felt intentional and carefully considered. Calenne brought clarity and creativity to our brand. The result feels timeless and uniquely ours.<',
     '>LinkedIn for professional updates and networking.<'),
    ('>James Carter<', '>LinkedIn<'),
    ('>Agentify<', '>&nbsp;<'),
    ('>From the very beginning, the entire process felt smooth, clear, and genuinely collaborative. Professional, thoughtful, and incredibly reliable. I highly recommend working with Calenne.<',
     '>Creative edits, AMV work, and thoughts on technology.<'),
    ('>Maya Patel<', '>Instagram / Tumblr<'),
    ('>Identify<', '>&nbsp;<'),
    # PRICING -> INTERESTS
    ('>PRICING<', '>INTERESTS<'),
    ('>Choose the scope that fits your project.<',   '>Other things I enjoy.<'),
    ('>Clear packages designed for focused projects and complete brand experiences.<',
     '>Beyond coding \u2014 things I spend time on and find interesting.<'),
    ('>Custom projects<', '>Digital Electronics<'),
    ('>Need a different scope? A tailored proposal can be created for you project.<',
     '>Logic design, flip-flops, MUX/DEMUX, counters, and circuit fundamentals.<'),
    ('>Request a quote<', '>Explore \u2192<'),
    ('>Essential<', '>Android &amp; Linux<'),
    ('>For focused brand or website projects.<', '>Android modding, ADB, flashing, and Linux customization.<'),
    ('>Up to 5 pages<',     '>Android Modding<'),
    ('>Basic CMS setup<',   '>ADB &amp; Flashing<'),
    ('>2 revision rounds<', '>Arch Linux<'),
    ('>7\u201310 day delivery<', '>Hyprland Ricing<'),
    ('>Start a project<',   '>Learn more<'),
    ('>Signature<', '>Video Editing<'),
    ('>For a signature identity and digital experience<', '>AMV editing and video projects using Adobe creative tools.<'),
    ('>Up to 10 pages<',    '>Premiere Pro<'),
    ('>CMS integration<',   '>After Effects<'),
    ('>3 revision rounds<', '>AMV / Edits<'),
    ('>14-21 day delivery<', '>Creative Work<'),
    # FAQ
    ('>Explore our FAQs<', '>More about me<'),
    ('>Answers to questions about process, pricing, timelines, and project details<',
     '>Common questions about what I do<'),
    ('>How do I submit a design request?<',   '>What do you build?<'),
    ('>How does onboarding work?<',           '>What Linux distro do you use?<'),
    ('>How fast will I receive my designs?<', '>Do you do competitive programming?<'),
    ('>Do you work at our company?<',         '>What is your homelab setup?<'),
    ('>Why not hire full-time?<',             '>Do you do open source?<'),
    ('>Can I order a one-time logo service?<', '>What creative tools do you use?<'),
    ('>What tools do you use?<',              '>What are your future goals?<'),
    ('>What is your refund policy?<',         '>How can I contact you?<'),
    # CTA
    (">LET'S WORK TOGETHER<", '>GET IN TOUCH<'),
    ('>Have a project in mind?<', '>Want to connect?<'),
    (">Tell me a little about your project, timeline, and goals. I'll get back to you within 1-2 business days.<",
     ">I'm always open to interesting conversations, collaborations, or just a good tech discussion.<"),
    ('>Start a project<', '>Reach out<'),
]

ABOUT = [
    ('>Design with clarity. Built to last.<', '>Code, systems, and curiosity.<'),
    (">I'm an independent digital designer creating refined identities, websites, and product experiences shaped by strategy, clarity, and thoughtful execution.<",
     ">I'm a 3rd-year CSE student at Khawaja Yunus Ali University. I enjoy building software, competitive programming, Linux systems, and understanding how things work.<"),
    ('>WORKING<',   '>STUDYING<'),
    ('>WORLDWIDE<', '>AT KYAU<'),
    ('>From cursiosity to craft.<', '>From curiosity to code.<'),
    ('>My journey into design started with curiosity - a desire to understand how things work and how they can work better for people.<',
     '>My interest in technology started with curiosity \u2014 wanting to understand how computers, software, and systems actually work.<'),
    ('>Over the years, that curiosity turned into a craft. Today, I help brands and businesses build clear, intentional and timeless digital experiences.<',
     ">Over time, that curiosity turned into a habit. I started exploring Linux, writing code, and building things \u2014 and I haven't stopped since.<"),
    ('>View my work<', '>View projects<'),
    ('>WHAT I VALUE<', '>WHAT I ENJOY<'),
    ('>Design guided by purpose.<', '>Driven by curiosity.<'),
    ('>Every project starts with intention. These principles shape the decisions I make and the experiences I create.<',
     '>Things I genuinely enjoy spending time on.<'),
    ('>Clarity<',   '>Competitive Programming<'),
    ('>I believe clarity creates confidence. I design with purpose and without confusion.<',
     '>Algorithmic problem solving, C++ competitive programming, and Codeforces contests.<'),
    ('>Restrait<',  '>Linux &amp; Systems<'),
    (">I remove what does't add value so the important things can stand out.<",
     '>Arch Linux, NixOS, Hyprland, Wayland, and system customization through dotfiles.<'),
    ('>Detail<',    '>Building Software<'),
    ('>I care about the small things that shape the whole experience.<',
     '>Java, Python, Git, and exploring different paradigms through projects and open-source.<'),
    ('>Longevity<', '>Homelab &amp; Networking<'),
    ('>I create work that is timeless, relevant and built to last.<',
     '>Tailscale, Wake-on-LAN, ESP32, basic networking, and self-hosting experiments.<'),
    ('>EXPERIENCE<', '>EDUCATION &amp; ACTIVITY<'),
    ('>Selected journey.<', '>My journey so far.<'),
    (">Over they years, I've worked on projects that challeged me, taught me, and shaped the way I design today.<",
     '>Where I study, what I practice, and what keeps me busy outside coursework.<'),
    ('>Independent designer<',    '>CSE Student<'),
    ('>Senior  product designer<', '>Competitive Programmer<'),
    ('>Brand &amp; web designer<', '>Open Source &amp; Homelab<'),
    ('>Visual designer<',          '>Video Editor &amp; Creator<'),
    ('>Design ethusiast<',         '>Linux Enthusiast<'),
    ('>Digital products<',         '>Codeforces &amp; Practice<'),
    ('>Freelance<',                '>Self-directed<'),
    ('>Design Agency<',            '>Personal Projects<'),
    ('>Self-learning<',            '>Self-directed<'),
]

PROJECTS = [
    (">Projects I'm proud of.<",  ">Projects I've worked on.<"),
    ('>A selection of work across brands, websites and digital experiences<',
     '>A selection of software, tools, and experiments. More coming soon.<'),
    ('>Brand strategy<',  '>Software<'),
    ('>Web design<',      '>Systems<'),
    ('>Art direction<',   '>Creative<'),
    ('>Product design<',  '>Experiments<'),
    ('>Branding<',        '>Personal<'),
    ('>Aures<',        '>Coming Soon<'),
    ('>Nova Studio<',  '>Coming Soon<'),
    ('>Kalm Interiors<', '>Coming Soon<'),
    ('>Mokka Coffee<', '>Coming Soon<'),
    ('>Nexora<',       '>Coming Soon<'),
    ('>Lumaire<',      '>Coming Soon<'),
    ('>Serein<',       '>Coming Soon<'),
    ('>Morrow<',       '>Coming Soon<'),
    ('>Auréline<',     '>Coming Soon<'),
    ('>Noma House<',   '>Coming Soon<'),
    ('>Orbital<',      '>Coming Soon<'),
    ('>Velora<',       '>Coming Soon<'),
    ('>Monvéo<',       '>Coming Soon<'),
    ('>Vellum<',       '>Coming Soon<'),
    ('>Nerra<',        '>Coming Soon<'),
    ('>Silex<',        '>Coming Soon<'),
    ('>Elsen<',        '>Coming Soon<'),
    ('>Vaire<',        '>Coming Soon<'),
    ('>Meral<',        '>Coming Soon<'),
    ('>Orsen<',        '>Coming Soon<'),
    ('>Tavren<',       '>Coming Soon<'),
    ('>Avenor<',       '>Coming Soon<'),
    ('>Halden<',       '>Coming Soon<'),
    ('>Roven<',        '>Coming Soon<'),
    ('>Ostra<',        '>Coming Soon<'),
    ('>Doren<',        '>Coming Soon<'),
]

def process(path, extras, title=None):
    print(f'\n=== {path} ===')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # CSS injection
    if INJECT_AFTER in content and CSS_HIDE not in content:
        content = content.replace(INJECT_AFTER, INJECT_AFTER + CSS_HIDE)
        print('  [+] CSS injected')
    content = apply(content, COMMON)
    content = apply(content, extras)
    if title:
        content = content.replace(
            '<title>Md. Sabbir Hossain Rahat \u2014 CSE Student &amp; Software Developer</title>',
            f'<title>{title}</title>',
        )
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  [\u2713] Done')

process(FILES['home'],     HOME)
process(FILES['about'],    ABOUT,    'About \u2014 Md. Sabbir Hossain Rahat')
process(FILES['projects'], PROJECTS, 'Projects \u2014 Md. Sabbir Hossain Rahat')
print('\n[\u2713] All files processed.')

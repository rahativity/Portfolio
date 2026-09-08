#!/usr/bin/env python3
"""
Full personalization script for both HTML and Framer JS chunks (.mjs).
"""
import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Files to process
HTML_FILES = [
    os.path.join(BASE, 'public/index.html'),
    os.path.join(BASE, 'public/about/index.html'),
    os.path.join(BASE, 'public/projects/index.html'),
]

SITE_DIR = os.path.join(BASE, 'public/assets/framerusercontent.com/sites/41uf7zGP5b5FlhAG4zMGXj')
MJS_MAIN     = os.path.join(SITE_DIR, 'script_main.CQeqkgE0.mjs')
MJS_SHARED   = os.path.join(SITE_DIR, 'shared-lib._DT0RS7G.mjs')
MJS_HOME     = os.path.join(SITE_DIR, 'FAVx2j8iCukRa_V9VE-TE_OJOPDaPYTzBj-8Hvn7qAc.DDa6RSAP.mjs')
MJS_ABOUT    = os.path.join(SITE_DIR, 'u8PNhcFxCKNuoHp-j_KfmJWmodhAzUexWMG7MCWUcEc.CVoViQ4E.mjs')
MJS_PROJECTS = os.path.join(SITE_DIR, '1Gx-JaMPUOo9_z8FlLA1fWkaefbePMUgLM-AW8sbxxY.CG16JM9X.mjs')
JSON_SEARCH  = os.path.join(SITE_DIR, 'searchIndex-htcjkZ9otXVF.json')

CSS_HIDE = (
    '#__framer-badge-container,.__framer-badge,.framer-6jWyo,[data-framer-name="Light"],'
    'a[href="https://stylokit.com/"],'
    'a[href*="framer.com/?via="],'
    'a[href="https://www.framer.com/community/marketplace/templates/calenne/"],'
    '.framer-1uwmrah-container,'
    '.framer-4w19hm-container'
    '{display:none!important;pointer-events:none!important}'
)

def replace_in_file(path, replacements, description=""):
    print(f"\nProcessing {os.path.basename(path)} ({description})...")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    initial_len = len(content)
    changed_count = 0
    for old, new in replacements:
        if old in content:
            count = content.count(old)
            content = content.replace(old, new)
            changed_count += count
        else:
            # Report missing
            snippet = (old[:45] + '...' + old[-20:]) if len(old) > 70 else old
            print(f"  [?] Not found: {snippet!r}")
            
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  [✓] Applied {changed_count} replacements.")

def personalize_html():
    # 1. Update HTML files
    for hf in HTML_FILES:
        with open(hf, 'r', encoding='utf-8') as f:
            c = f.read()

        # Update CSS hide
        if 'id="f2c-strip-template-badge">' in c:
            # Replace old CSS hide if present
            c = re.sub(
                r'id="f2c-strip-template-badge">[^<]*</style>',
                f'id="f2c-strip-template-badge">{CSS_HIDE}</style>',
                c
            )

        # Fix hero in index.html
        if 'public/index.html' in hf:
            # Replace Sevora in hero
            c = c.replace('>Sevora<', '>Rahat<')
            # Replace headline endings in hero
            c = c.replace(
                '— I create brands and websites with ',
                '— Computer Science student &amp; '
            )
            c = c.replace(
                '>clarity.<',
                '>software developer.<'
            )
            # Replace prices
            c = c.replace('>$1,500<', '>Systems<')
            c = c.replace('>$2,800<', '>Media<')
            c = c.replace('>$1,500"', '>"Systems"')
            c = c.replace('>$2,800"', '>"Media"')
            c = c.replace('>USD<', '>Focus<')

        with open(hf, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated HTML: {os.path.basename(hf)}")

def personalize_script_main():
    replacements = [
        ('`Cannele`', '`Rahat`'),
        ('`Calenne`', '`Rahat`'),
        ('`Lets talk`', '`Say hi`'),
        ('© Calenne Template | Created by ', '© Md. Sabbir Hossain Rahat '),
        ('children:`Stylokit`', 'children:` `'),
        ('https://stylokit.com/', 'https://github.com/rahativity'),
        ('https://x.com/Dmytri_Design', 'https://github.com/rahativity'),
        ('https://dribbble.com/Stylokit', 'https://codeforces.com/profile/Rahat001'),
        ('mailto:hello@calenne.studio', 'https://www.instagram.com/promithiuss?igsh=NzJwdXo1ZjBnOWk2'),
        ('Tel:+1 (415) 555-0198', 'https://www.facebook.com/share/1G99UNYx9w/'),
        ('https://www.google.com/maps', 'https://www.tumblr.com/rahathinks?source=share'),
        ('children:`X link`', 'children:`GitHub`'),
        ('children:`Linkedin`', 'children:`LinkedIn`'),
        ('children:`Dribbble`', 'children:`Codeforces`'),
        ('children:`hello@calenne.studio`', 'children:`Instagram`'),
        ('children:`+1 (415) 555-0198`', 'children:`Facebook`'),
        ('children:`San Francisco, CA`', 'children:`Tumblr`'),
        ('children:`CONTACT`', 'children:`LINKS`'),
        (
            'Creating refined digital experiences with clarity, intention, and thoughtful execution.',
            'CSE student and software developer. Building software, exploring Linux, and understanding systems.'
        ),
        ('https://www.framer.com/community/marketplace/templates/calenne/', '#'),
        ('`Remix Template`', '` `'),
    ]
    replace_in_file(MJS_MAIN, replacements, "Navbar + Footer")

def personalize_shared():
    replacements = [
        (
            'Calenne – Designer portfolio template',
            'Md. Sabbir Hossain Rahat — CSE Student & Software Developer'
        )
    ]
    replace_in_file(MJS_SHARED, replacements, "Shared Metadata")

def personalize_home():
    replacements = [
        # Hero names & titles
        ('children:`Calenne`', 'children:`Rahat`'),
        ('children:`Sevora`', 'children:`Rahat`'),
        ('` — I create brands and websites with `', '` — Computer Science student & `'),
        ('children:`clarity.`', 'children:`software developer.`'),

        # Hero subtext
        (
            'I design refined brands, websites, and interfaces for ambitious founders and creative teams.',
            "I'm a CSE student and software developer. I build software, compete in programming, explore Linux, and experiment with systems."
        ),

        # Availability
        ('`AVAILABLE FOR PROJECT`', '`OPEN TO OPPORTUNITIES`'),
        ('`Open for new projects`', '`Open to collaboration`'),
        ('`Working worldwide`', '`Based in Bangladesh`'),
        ('`Response within 24h`', '`Building & learning`'),
        ('hello@calenne.design', 'https://github.com/rahativity'),

        # Works intro
        ('Design built around lasting clarity', 'Projects built with purpose.'),
        (
            'I bring strategy, visual direction, and refined execution together to create meaningful digital experiences with lasting impact.',
            "I enjoy building software, experimenting with systems, and working through hard problems. A selection of what I've worked on."
        ),
        (
            'A curated selection of brand, web, and digital projects crafted with clarity and intention.',
            'A selection of software projects, tools, and experiments. More coming soon.'
        ),

        # Project titles
        ('`Aures`', '`Coming Soon`'),
        ('`Nova Studio`', '`Coming Soon`'),
        ('`Kalm Interiors`', '`Coming Soon`'),
        ('`Mokka Coffee`', '`Coming Soon`'),
        ('`Nexora`', '`Coming Soon`'),
        ('`View project`', '`Coming Soon`'),
        (
            'Shaping a refined visual identity through thoughtful strategy, expressive details, and a clear contemporary design language.',
            "A project I'm working on. Details coming soon."
        ),
        (
            'Creating a flexible digital presence that balances creative expression, clarity, and a confident studio personality.',
            'A personal project around systems and tools. Details coming soon.'
        ),
        (
            'Building a calm visual identity inspired by natural materials, considered spaces, and understated interior expression.',
            "Something I'm building. Details coming soon."
        ),
        (
            'Bringing warmth, character, and everyday ritual together through a distinctive and approachable coffee brand experience.',
            'A personal project. Details coming soon.'
        ),
        (
            'Turning complex financial information into a clear, intuitive, and thoughtfully structured digital wealth experience.',
            'An experimental project. Details coming soon.'
        ),

        # Services -> Skills
        ('`SERVICES`', '`SKILLS`'),
        ('`What I do`', '`What I work with`'),
        ('Services shaped around clarity', 'Things I enjoy building and exploring.'),
        (
            'From idenity to digital experience, each service is crafted to create clear, meaningful and lasting impact.',
            "From competitive programming to Linux systems, here's what I spend my time on."
        ),
        ('`Brand identity`', '`Competitive Programming`'),
        (
            'Distinctive visual systems built to make your brand feel clear, consistent, and memorable.',
            'C++ problem solving on Codeforces. Algorithmic challenges and contest programming.'
        ),
        ('`Logo syste`', '`C++`'),
        ('`Visual identity`', '`Linux & Systems`'),
        (
            'Thoughtful websites shaped around strong structure, refined visuals, and intuitive user experiences.',
            'Arch Linux, NixOS, Hyprland, Wayland, Zsh, dotfiles, and system ricing.'
        ),
        ('`UX direction`', '`Arch / NixOS`'),
        ('`UI design`', '`Hyprland`'),
        ('`Responsive design`', '`Dotfiles`'),
        ('`Framer development`', '`Development`'),
        (
            'Responsive, polished websites developed in Framer with smooth interactions and easy-to-manage content.',
            'Java, Python, Git, and open-source experimentation.'
        ),
        ('`Framer build`', '`Java`'),
        ('`CMS setup`', '`Python`'),
        ('`Motion design`', '`Git & GitHub`'),
        ('`Creative direction`', '`Homelab & Networking`'),
        (
            'A cohesive visual direction that brings every image, layout, and design decision into one clear vision.',
            'Tailscale, Wake-on-LAN, ESP32, basic networking, and self-hosting experiments.'
        ),
        ('`Art direction`', '`Tailscale`'),
        ('`Campaign visuals`', '`ESP32`'),
        ('`Content direction`', '`Self-hosting`'),
        ('`Design systems`', '`Creative`'),
        (
            'Flexible design foundations that keep your brand and digital products consistent as they grow.',
            'Video editing with Premiere Pro and After Effects. Android modding, ADB, and device customization.'
        ),
        ('`UI library`', '`Video Editing`'),
        ('`Component system`', '`Android Modding`'),
        ('`Design documentation`', '`AMV Editing`'),

        # About on Home
        ('`About Calenne`', '`About Rahat`'),
        (
            "I'm an independent designer focused on building clear, refined brands and digital experiences. My approach combines thoughtful strategy, strong visual direction, and careful attention to detail.",
            "I'm a 3rd-year CSE student at Khawaja Yunus Ali University. I enjoy building software, competitive programming, exploring Linux systems, and understanding how things work."
        ),
        ('`Years of experience`', '`Year of Study`'),
        ('`Projects completed`', '`3rd Year CSE`'),
        ('`Countries reached`', '`KYAU`'),

        # Approach
        ('`MY APPROACH`', '`HOW I WORK`'),
        ('A clear paht from idea to outcome.', 'How I approach problems and projects.'),
        (
            'A structured, collaborative process that keeps every step intentional and every detail meaningful.',
            'A simple, iterative loop that keeps things moving and focused on what matters.'
        ),
        ('`Discover`', '`Understand`'),
        (
            'Understanding your goals, audience, challenges, and the direction the project needs to take.',
            'Read the problem, understand the requirements, and figure out what needs to be built.'
        ),
        ('`Define`', '`Plan`'),
        (
            'Shaping a clear strategy, structure, and visual direction before design begins.',
            'Break it down, choose the right tools or approach, and outline a clear path forward.'
        ),
        ('`Create`', '`Build`'),
        (
            'Turning the direction into a refined brand identity, website, or digital experience.',
            'Write the code, experiment, and iterate until it works the way it should.'
        ),
        ('`Deliver`', '`Ship`'),
        (
            'Polishing every detail and preparing a complete, ready-to-use result.',
            'Test, clean up, and get it out into the world.'
        ),

        # Kind Words -> Social platforms
        ('`KIND WORDS`', '`GET IN TOUCH`'),
        ('`Trusted by`', '`Find me on`'),
        ('`thoughtful clients.`', '`these platforms.`'),
        (
            'Long-term relationships built on trust clear communication, and work that speaks for itself.',
            "I'm active on these platforms. Feel free to reach out or connect."
        ),
        (
            'Calenne brought clarity to a project that initially felt scattered. Every decision felt intentional.',
            'github.com/rahativity — open source projects, dotfiles, and code.'
        ),
        ('`Maya Chen`', '`GitHub`'),
        ('`Founder, Aurès`', '` `'),
        ('`See on X →`', '`View Profile →`'),
        ('https://x.com/Dmytri_Design', 'https://github.com/rahativity'),
        (
            'The process was clear, thoughtful, and easy to follow. The final website felt refined, purposeful, and completely aligned with our brand.',
            'Competitive programming on Codeforces. Problem solving in C++.'
        ),
        ('`David Lee`', '`Codeforces`'),
        (
            'Working with Calenne was seamless from start to finish. Every detail felt intentional and carefully considered. Calenne brought clarity and creativity to our brand. The result feels timeless and uniquely ours.',
            'LinkedIn for professional updates, networking, and engineering discussions.'
        ),
        ('`James Carter`', '`LinkedIn`'),
        ('`Agentify`', '` `'),
        (
            'From the very beginning, the entire process felt smooth, clear, and genuinely collaborative. Professional, thoughtful, and incredibly reliable. I highly recommend working with Calenne.',
            'Creative edits, AMV work, and thoughts on technology.'
        ),
        ('`Maya Patel`', '`Instagram / Tumblr`'),
        ('`Identify`', '` `'),

        # Interests / Pricing replacement
        ('`PRICING`', '`INTERESTS`'),
        ('Choose the scope that fits your project.', 'Other things I enjoy.'),
        (
            'Clear packages designed for focused projects and complete brand experiences.',
            'Beyond coding — things I spend time on and find interesting.'
        ),
        ('`Essential`', '`Android & Linux`'),
        (
            'For focused brand or website projects.',
            'Android modding, ADB, flashing, and Linux customization.'
        ),
        ('`$1,500`', '`Systems`'),
        ('`USD`', '`Focus`'),
        ('`Up to 5 pages`', '`Android Modding`'),
        ('`Basic CMS setup`', '`ADB & Flashing`'),
        ('`2 revision rounds`', '`Arch Linux`'),
        ('`7–10 day delivery`', '`Hyprland Ricing`'),
        ('`Start a project`', '`Learn more`'),
        ('`Signature`', '`Video Editing`'),
        (
            'For a signature identity and digital experience',
            'AMV editing and video projects using Adobe creative tools.'
        ),
        ('`$2,800`', '`Media`'),
        ('`Up to 10 pages`', '`Premiere Pro`'),
        ('`CMS integration`', '`After Effects`'),
        ('`3 revision rounds`', '`AMV / Edits`'),
        ('`14-21 day delivery`', '`Creative Work`'),
        ('`Custom projects`', '`Digital Electronics`'),
        (
            'Need a different scope? A tailored proposal can be created for you project.',
            'Logic design, flip-flops, MUX/DEMUX, counters, and circuit fundamentals.'
        ),
        ('`Request a quote`', '`Explore →`'),

        # FAQs
        ('Explore our FAQs', 'More about me'),
        ('Answers to questions about process, pricing, timelines, and project details', 'Common questions about what I do'),
        ('How do I submit a design request?', 'What do you build?'),
        ('How does onboarding work?', 'What Linux distro do you use?'),
        ('How fast will I receive my designs?', 'Do you do competitive programming?'),
        ('Do you work at our company?', 'What is your homelab setup?'),
        ('Why not hire full-time?', 'Do you do open source?'),
        ('Can I order a one-time logo service?', 'What creative tools do you use?'),
        ('What tools do you use?', 'What are your future goals?'),
        ('What is your refund policy?', 'How can I contact you?'),

        # CTA
        ("`LET'S WORK TOGETHER`", '`GET IN TOUCH`'),
        ('Have a project in mind?', 'Want to connect?'),
        (
            "Tell me a little about your project, timeline, and goals. I'll get back to you within 1-2 business days.",
            "I'm always open to interesting conversations, collaborations, or just a good tech discussion."
        ),
    ]
    replace_in_file(MJS_HOME, replacements, "Home Page Chunk")

def personalize_about():
    replacements = [
        ('Design with clarity. Built to last.', 'Code, systems, and curiosity.'),
        (
            "I'm an independent digital designer creating refined identities, websites, and product experiences shaped by strategy, clarity, and thoughtful execution.",
            "I'm a 3rd-year CSE student at Khawaja Yunus Ali University. I enjoy building software, competitive programming, Linux systems, and understanding how things work."
        ),
        ('`WORKING`', '`STUDYING`'),
        ('`WORLDWIDE`', '`AT KYAU`'),
        ('From cursiosity to craft.', 'From curiosity to code.'),
        (
            'My journey into design started with curiosity - a desire to understand how things work and how they can work better for people.',
            'My interest in technology started with curiosity — wanting to understand how computers, software, and systems actually work.'
        ),
        (
            'Over the years, that curiosity turned into a craft. Today, I help brands and businesses build clear, intentional and timeless digital experiences.',
            "Over time, that curiosity turned into a habit. I started exploring Linux, writing code, and building things — and I haven't stopped since."
        ),
        ('`View my work`', '`View projects`'),
        ('`WHAT I VALUE`', '`WHAT I ENJOY`'),
        ('Design guided by purpose.', 'Driven by curiosity.'),
        (
            'Every project starts with intention. These principles shape the decisions I make and the experiences I create.',
            'Things I genuinely enjoy spending time on.'
        ),
        ('`Clarity`', '`Competitive Programming`'),
        (
            'I believe clarity creates confidence. I design with purpose and without confusion.',
            'Algorithmic problem solving, C++ competitive programming, and Codeforces contests.'
        ),
        ('`Restrait`', '`Linux & Systems`'),
        (
            "I remove what does't add value so the important things can stand out.",
            'Arch Linux, NixOS, Hyprland, Wayland, and system customization through dotfiles.'
        ),
        ('`Detail`', '`Building Software`'),
        (
            'I care about the small things that shape the whole experience.',
            'Java, Python, Git, and exploring different paradigms through projects and open-source.'
        ),
        ('`Longevity`', '`Homelab & Networking`'),
        (
            'I create work that is timeless, relevant and built to last.',
            'Tailscale, Wake-on-LAN, ESP32, basic networking, and self-hosting experiments.'
        ),
        ('`EXPERIENCE`', '`EDUCATION & ACTIVITY`'),
        ('Selected journey.', 'My journey so far.'),
        (
            "Over they years, I've worked on projects that challeged me, taught me, and shaped the way I design today.",
            'Where I study, what I practice, and what keeps me busy outside coursework.'
        ),
        ('`Independent designer`', '`CSE Student`'),
        ('`Senior  product designer`', '`Competitive Programmer`'),
        ('`Brand & web designer`', '`Open Source & Homelab`'),
        ('`Visual designer`', '`Video Editor & Creator`'),
        ('`Design ethusiast`', '`Linux Enthusiast`'),
        ('`Digital products`', '`Codeforces & Practice`'),
        ('`Freelance`', '`Self-directed`'),
        ('`Design Agency`', '`Personal Projects`'),
        ('`Self-learning`', '`Self-directed`'),
        ('Copenhagen / Worldwide', 'Bangladesh'),
        ('Copenhagen, Denmark', 'Bangladesh'),
        ('Calenne Studio', 'Khawaja Yunus Ali University'),
        ('title:`Calenne`', 'title:`Rahat`'),
    ]
    replace_in_file(MJS_ABOUT, replacements, "About Page Chunk")

def personalize_projects():
    replacements = [
        ("Projects I'm proud of.", "Projects I've worked on."),
        (
            'A selection of work across brands, websites and digital experiences',
            'A selection of software, tools, and experiments. More coming soon.'
        ),
        ('`Brand strategy`', '`Software`'),
        ('`Web design`', '`Systems`'),
        ('`Art direction`', '`Creative`'),
        ('`Product design`', '`Experiments`'),
        ('`Branding`', '`Personal`'),
    ]
    replace_in_file(MJS_PROJECTS, replacements, "Projects Page Chunk")

def personalize_search_index():
    replacements = [
        ('Calenne', 'Rahat'),
        ('Cannele', 'Rahat'),
        ('Copenhagen, Denmark', 'Bangladesh'),
        ('Copenhagen', 'Bangladesh'),
        ('I create brands and websites with clarity.', 'Computer Science student & software developer.'),
    ]
    replace_in_file(JSON_SEARCH, replacements, "Search Index")

if __name__ == '__main__':
    print("=== STARTING COMPLETE PERSONALIZATION ===")
    personalize_html()
    personalize_script_main()
    personalize_shared()
    personalize_home()
    personalize_about()
    personalize_projects()
    personalize_search_index()
    print("\n=== COMPLETE PERSONALIZATION FINISHED ===")

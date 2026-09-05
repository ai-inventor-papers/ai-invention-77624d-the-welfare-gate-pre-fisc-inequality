from playwright.sync_api import sync_playwright

URL = "file:///ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/4_gen_paper_repo/_4_assemble_paper/paper/index.html"
OUT = "/ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/4_gen_paper_repo/_4_assemble_paper/paper/workspace/qa/"

with sync_playwright() as p:
    browser = p.chromium.launch()

    for width, height, name in [(390, 844, "phone"), (1440, 900, "desktop")]:
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(URL, wait_until="load")
        page.wait_for_timeout(300)

        # 1. text clipping: any element whose content overflows its own box (not scroll containers)
        clip = page.evaluate("""() => {
            const out = [];
            document.querySelectorAll('p, h1, h2, h3, .card, .eq, .lede, dt, dd, li, th, td').forEach(el => {
                const cs = getComputedStyle(el);
                if (cs.overflow === 'visible' && el.scrollHeight > el.clientHeight + 2) {
                    out.push(el.tagName + '.' + (el.className||'') + ' sh=' + el.scrollHeight + ' ch=' + el.clientHeight);
                }
            });
            return out.slice(0, 10);
        }""")
        print(f"[{name}] text-clipping elements:", clip if clip else "none")

        # 2. desktop: nav rail vs content overlap
        if width >= 1024:
            ov = page.evaluate("""() => {
                const nav = document.querySelector('.side-nav').getBoundingClientRect();
                const con = document.querySelector('.content').getBoundingClientRect();
                return { nav: [nav.left, nav.right], content: [con.left, con.right], overlap: nav.right > con.left };
            }""")
            print(f"[{name}] rail/content:", ov)

        # 3. eq block fit: is the fomula wider than its box?
        eq = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('.eq')).map(e => ({
                scrollW: e.scrollWidth, clientW: e.clientWidth, scrollable: e.scrollWidth > e.clientWidth + 1
            }));
        }""")
        print(f"[{name}] eq blocks:", eq)

        # 4. sticky nav sticks and does not cover hero content
        page.evaluate("window.scrollTo(0, 500)")
        page.wait_for_timeout(250)
        cover = page.evaluate("""() => {
            const n = document.querySelector('.side-nav').getBoundingClientRect();
            const h = document.querySelector('.hero .kicker').getBoundingClientRect();
            return { navBottom: Math.round(n.bottom), heroTop: Math.round(h.top), coversHero: n.bottom > h.top };
        }""")
        print(f"[{name}] sticky nav vs hero:", cover)

        # 5. focus ring on nav link (visible outline style)
        focus_ok = page.evaluate("""() => {
            document.querySelector('#section-nav a').focus();
            const cs = getComputedStyle(document.querySelector('#section-nav a'));
            return { outlineStyle: cs.outlineStyle, outlineWidth: cs.outlineWidth, outlineColor: cs.outlineColor };
        }""")
        print(f"[{name}] focused link outline:", focus_ok)

        # 6. Enter key on nav link activates section
        page.keyboard.press("Enter")
        page.wait_for_timeout(500)
        after = page.evaluate("() => document.querySelector('#section-nav a[aria-current]')?.textContent.trim() || 'NONE'")
        print(f"[{name}] aria-current after Enter on nav link:", after)

        # 7. reduced motion: check scroll-behavior computed
        page.close()

    # reduced-motion emulation
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
    page = ctx.new_page()
    page.goto(URL, wait_until="load")
    sb = page.evaluate("getComputedStyle(document.documentElement).scrollBehavior")
    print("[reduce] html scroll-behavior:", sb)
    ctx.close()

    # no-preference emulation
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="no-preference")
    page = ctx.new_page()
    page.goto(URL, wait_until="load")
    sb = page.evaluate("getComputedStyle(document.documentElement).scrollBehavior")
    print("[no-preference] html scroll-behavior:", sb)
    ctx.close()

    browser.close()
from playwright.sync_api import sync_playwright

URL = "file:///ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/4_gen_paper_repo/_4_assemble_paper/paper/index.html"
OUT = "/ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/4_gen_paper_repo/_4_assemble_paper/paper/workspace/qa/"

with sync_playwright() as p:
    browser = p.chromium.launch()
    for width, height, name in [(390, 844, "phone"), (1440, 900, "desktop")]:
        page = browser.new_page(viewport={"width": width, "height": height})
        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda exc: console_errors.append(str(exc)))
        page.goto(URL, wait_until="load")
        page.wait_for_timeout(400)

        doc = page.evaluate("""() => ({
            clientW: document.documentElement.clientWidth,
            scrollW: document.documentElement.scrollWidth,
            bodyScrollW: document.body.scrollWidth
        })""")
        overflow = doc["scrollW"] - doc["clientW"]

        stick = page.evaluate("""(vw) => {
            const bad = [];
            document.querySelectorAll('body *').forEach(el => {
                const r = el.getBoundingClientRect();
                if (r.right > vw + 1 && getComputedStyle(el).position !== 'fixed') {
                    bad.push(el.tagName + '.' + (el.className || '') + ' right=' + Math.round(r.right));
                }
            });
            return bad.slice(0, 12);
        }""", width)

        heads = page.evaluate("""() => {
            const hs = {};
            document.querySelectorAll('h1,h2,h3,h4,h5,h6').forEach(h => {
                const l = h.tagName[1];
                hs[l] = (hs[l] || 0) + 1;
            });
            return hs;
        }""")

        links = page.evaluate("""() => {
            const out = [];
            document.querySelectorAll('a').forEach(a => out.push(a.textContent.trim() + ' -> ' + a.getAttribute('href')));
            return out;
        }""")

        page.evaluate("window.scrollTo(0, document.body.scrollHeight * 0.55)")
        page.wait_for_timeout(300)
        spy = page.evaluate("() => document.querySelector('#section-nav a[aria-current]')?.textContent.trim() || 'NONE'")

        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_timeout(200)
        page.keyboard.press("Tab")
        first_focus = page.evaluate("() => { const e = document.activeElement; return e.tagName + '.' + (e.className||'') + ' ' + (e.textContent||'').trim().slice(0,40); }")

        page.screenshot(path=OUT + name + "_full.png", full_page=True)

        print(f"=== {name} ({width}x{height}) ===")
        print("clientW/scrollW:", doc)
        print("horizontal overflow px:", overflow)
        print("sticking elements:", stick if stick else "none")
        print("headings:", heads)
        print("aria-current after scroll:", spy)
        print("first Tab target:", first_focus)
        print("console errors:", console_errors if console_errors else "none")
        print("links:", len(links))
        page.close()
    browser.close()
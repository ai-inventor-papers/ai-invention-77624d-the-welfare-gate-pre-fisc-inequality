from playwright.sync_api import sync_playwright

URL = "file:///ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/4_gen_paper_repo/_4_assemble_paper/paper/index.html"
OUT = "/ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/4_gen_paper_repo/_4_assemble_paper/paper/workspace/qa/"

with sync_playwright() as p:
    browser = p.chromium.launch()
    for width, height, name in [(390, 844, "phone"), (1440, 900, "desktop")]:
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(URL, wait_until="load")
        page.wait_for_timeout(300)

        # full tab walk: 13 Tab presses should cycle all focusables
        stops = []
        for i in range(14):
            page.keyboard.press("Tab")
            info = page.evaluate("""() => {
                const e = document.activeElement;
                const cs = getComputedStyle(e);
                const r = e.getBoundingClientRect();
                const vw = window.innerWidth, vh = window.innerHeight;
                const inViewport = r.top >= -2 && r.left >= -2 && r.right <= vw + 2 && r.bottom <= vh + 2;
                return {
                    tag: e.tagName,
                    cls: (e.className || '').toString().slice(0, 20),
                    text: (e.textContent || '').trim().slice(0, 30),
                    outline: cs.outlineStyle + ' ' + cs.outlineWidth,
                    visible: inViewport
                };
            }""")
            stops.append(info)
        for s in stops:
            print(f"  tab -> {s['tag']}.{s['cls']} '{s['text']}' outline={s['outline']} inViewport={s['visible']}")

        # verify focus scrolls the control into view for each stop
        page.screenshot(path=OUT + name + "_full.png", full_page=True)
        print(f"[{name}] screenshots written")
        page.close()
    browser.close()
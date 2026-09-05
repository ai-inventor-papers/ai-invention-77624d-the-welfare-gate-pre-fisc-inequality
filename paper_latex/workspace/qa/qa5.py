from playwright.sync_api import sync_playwright

URL = "file:///ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/4_gen_paper_repo/_4_assemble_paper/paper/index.html"

with sync_playwright() as p:
    browser = p.chromium.launch()
    for width, height, name in [(390, 844, "phone"), (1440, 900, "desktop")]:
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(URL, wait_until="load")
        page.wait_for_timeout(300)
        stops = []
        for i in range(13):
            page.keyboard.press("Tab")
            page.wait_for_timeout(700)  # let smooth scroll settle
            info = page.evaluate("""() => {
                const e = document.activeElement;
                const cs = getComputedStyle(e);
                const r = e.getBoundingClientRect();
                const vw = window.innerWidth, vh = window.innerHeight;
                return {
                    tag: e.tagName,
                    cls: (e.className || '').toString().slice(0, 20),
                    text: (e.textContent || '').trim().slice(0, 28),
                    outline: cs.outlineStyle + ' ' + cs.outlineWidth,
                    inView: r.top >= -2 && r.left >= -2 && r.right <= vw + 2 && r.bottom <= vh + 2
                };
            }""")
            stops.append(info)
        for s in stops:
            print(f"  {name}: tab -> {s['tag']}.{s['cls']} '{s['text']}' outline={s['outline']} inView={s['inView']}")
        page.close()
    browser.close()
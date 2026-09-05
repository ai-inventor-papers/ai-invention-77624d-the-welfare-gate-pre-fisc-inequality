from playwright.sync_api import sync_playwright

URL = "file:///ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/4_gen_paper_repo/_4_assemble_paper/paper/index.html"

with sync_playwright() as p:
    browser = p.chromium.launch()
    for width, height, name in [(390, 844, "phone"), (1440, 900, "desktop")]:
        ctx = browser.new_context(viewport={"width": width, "height": height}, reduced_motion="reduce")
        page = ctx.new_page()
        page.goto(URL, wait_until="load")
        page.wait_for_timeout(300)
        stops = []
        for i in range(12):
            page.keyboard.press("Tab")
            page.wait_for_timeout(120)
            info = page.evaluate("""() => {
                const e = document.activeElement;
                const r = e.getBoundingClientRect();
                const vw = window.innerWidth, vh = window.innerHeight;
                return {
                    tag: e.tagName,
                    cls: (e.className || '').toString().slice(0, 20),
                    text: (e.textContent || '').trim().slice(0, 28),
                    inView: r.top >= -2 && r.left >= -2 && r.right <= vw + 2 && r.bottom <= vh + 2
                };
            }""")
            stops.append(info)
        bad = [s for s in stops if not s["inView"]]
        print(f"[{name}] tab stops: {len(stops)}, out-of-view: {len(bad)}")
        for s in stops:
            print(f"  {s['tag']}.{s['cls']} '{s['text']}' inView={s['inView']}")
        ctx.close()
    browser.close()
from playwright.sync_api import sync_playwright

URL = "file:///ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/4_gen_paper_repo/_4_assemble_paper/paper/index.html"
OUT = "/ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/4_gen_paper_repo/_4_assemble_paper/paper/workspace/qa/"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 390, "height": 844})
    page.goto(URL, wait_until="load")
    page.wait_for_timeout(300)

    nav = page.evaluate("""() => {
        const n = document.querySelector('.side-nav').getBoundingClientRect();
        const links = Array.from(document.querySelectorAll('#section-nav a')).map(a => {
            const r = a.getBoundingClientRect();
            return a.textContent.trim() + ' left=' + Math.round(r.left) + ' right=' + Math.round(r.right) + ' top=' + Math.round(r.top);
        });
        return { navHeight: Math.round(n.height), navRect: [Math.round(n.left), Math.round(n.right)], links };
    }""")
    print("nav:", nav)

    page.screenshot(path=OUT + "phone_full.png", full_page=True)
    page.screenshot(path=OUT + "phone_top.png")
    doc = page.evaluate("() => ({ cw: document.documentElement.clientWidth, sw: document.documentElement.scrollWidth })")
    print("overflow:", doc)

    # second nav row sticky test: scroll and confirm both rows still visible
    page.evaluate("window.scrollTo(0, 600)")
    page.wait_for_timeout(250)
    nav2 = page.evaluate("""() => {
        const n = document.querySelector('.side-nav').getBoundingClientRect();
        return { top: Math.round(n.top), bottom: Math.round(n.bottom), height: Math.round(n.height) };
    }""")
    print("nav after scroll:", nav2)
    browser.close()
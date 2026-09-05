from playwright.sync_api import sync_playwright

URL = "file:///ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/4_gen_paper_repo/_4_assemble_paper/paper/index.html"

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto(URL, wait_until="load")
    pg.wait_for_timeout(300)

    out = pg.evaluate("""() => {
        const res = {};
        res.landmarks = Array.from(document.querySelectorAll('header, nav, main, footer, aside, form')).map(e =>
            e.tagName + (e.getAttribute('aria-label') ? '[' + e.getAttribute('aria-label') + ']' : ''));
        res.sections = Array.from(document.querySelectorAll('section')).map(s => ({
            id: s.id,
            labelled: s.getAttribute('aria-labelledby'),
            h: (s.querySelector('h2') || {}).id
        }));
        res.h1 = Array.from(document.querySelectorAll('h1')).map(h => h.textContent.trim().slice(0, 60));
        res.navCurrent = document.querySelectorAll('#section-nav a[aria-current]').length;
        res.tables = document.querySelectorAll('table').length;
        res.tableCaptions = Array.from(document.querySelectorAll('table caption')).map(c => c.textContent.trim().slice(0, 50));
        res.imgCount = document.querySelectorAll('img').length;
        res.lang = document.documentElement.lang;
        res.title = document.title.slice(0, 80);
        return res;
    }""")
    for k, v in out.items():
        print(k + ":", v)
    b.close()
from html.parser import HTMLParser
import re, html as htmllib

SRC = "/ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/4_gen_paper_repo/_4_assemble_paper/paper/index.html"
src = open(SRC).read()

VOID = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}

class Balance(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))
    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f"close without open: {tag} at {self.getpos()}")
            return
        if self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            self.errors.append(f"mismatch: expected </{self.stack[-1][0]}> got </{tag}> at {self.getpos()}")

b = Balance()
b.feed(src)
print("tag balance errors:", b.errors if b.errors else "NONE")
print("unclosed tags:", b.stack if b.stack else "NONE")

# register stats on the final file
text = htmllib.unescape(src)
body = re.sub(r'<style>.*?</style>', ' ', text, flags=re.S)
body = re.sub(r'<script>.*?</script>', ' ', body, flags=re.S)
body = re.sub(r'<[^>]+>', ' ', body)
words = re.findall(r"[A-Za-z']+", body)
wc = len(words)
em = text.count('\u2014')
print(f"words: {wc}; em dashes: {em}; em/1000: {em*1000/wc:.1f}")

hedges = ["may","might","likely","suggests","appears","perhaps","possibly","could","would","seems","probably","plausibly","can"]
hc = sum(len(re.findall(r'\b'+h+r'\b', body, re.I)) for h in hedges)
print(f"hedges: {hc}; per-1000: {hc*1000/wc:.1f}")

forbidden = ["delve","underscore","showcase","intricate","pivotal","realm","commendable","meticulous","tapestry","garner","multifaceted","it is worth noting","plays a crucial role","not only","but also"]
hits = [w for w in forbidden if re.search(w, body, re.I)]
print("forbidden words:", hits if hits else "NONE")

# final number audit: numbers in prose vs paper.tex
tex = open("/ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/4_gen_paper_repo/_4_assemble_paper/paper/paper.tex").read()
visible = re.sub(r'<style>.*?</style>', ' ', text, flags=re.S)
visible = re.sub(r'<script>.*?</script>', ' ', visible, flags=re.S)
visible = re.sub(r'<[^>]+>', ' ', visible)
nums = sorted(set(re.findall(r'\b\d+(?:\.\d+)?\b', visible)))
notintex = [n for n in nums if n not in tex]
print("prose numbers:", nums)
print("prose numbers not in paper.tex:", notintex if notintex else "NONE")
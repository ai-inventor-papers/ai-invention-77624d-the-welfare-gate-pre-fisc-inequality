#!/usr/bin/env python3
"""Convert paper_body.md (markdown) to LaTeX body text (paper_body.tex)."""
import re

WS = "/ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/4_gen_paper_repo/_4_assemble_paper/paper/workspace"
t = open(f"{WS}/paper_body.md", encoding="utf-8").read()

# ---- 0. Targeted Figure-sentence fixes (no figures exist in this run) ----
t = t.replace(
    "Figure 3 documents the phenomenon the design must explain, with values from the development phase to be re-verified at every series URL in the coverage audit.",
    "The phenomenon the design must explain is documented by the descriptive series that follow, with values from the development phase to be re-verified at every series URL in the coverage audit.",
)
t = t.replace(
    "The eleven cases of Figure 3, Bulgaria, Chile, Estonia, Hungary, Latvia, Lithuania, Poland, Romania, Slovakia, South Africa, and South Korea, are listed here as the illustrative subset;",
    "An illustrative subset of eleven of those cases, Bulgaria, Chile, Estonia, Hungary, Latvia, Lithuania, Poland, Romania, Slovakia, South Africa, and South Korea, is listed here;",
)
# drop standalone figure-marker lines
t = re.sub(r"^\s*\[FIGURE:fig\d+\]\s*$", "", t, flags=re.M)
# drop the three "Figure N ..." sentences that point to now-absent diagrams
for sent in [
    "Figure 1 diagrams the gate.",
    "Figure 2 diagrams the decomposition.",
    "Figure 4 summarizes the identification logic.",
]:
    t = t.replace(sent, "")

# ---- 1. Title line: drop (set via \\title) ----
lines = t.split("\n")
if lines[0].startswith("# "):
    lines = lines[1:]
t = "\n".join(lines)

# ---- 2. Headers ----
out = []
for ln in t.split("\n"):
    if ln.startswith("### "):
        out.append("\\subsection{" + ln[4:] + "}")
    elif ln.startswith("## "):
        out.append("\\section{" + ln[3:] + "}")
    elif ln.startswith("# "):
        out.append("\\section*{" + ln[2:] + "}")
    else:
        out.append(ln)
t = "\n".join(out)

# ---- 3. Display math $$...$$ -> \\[...\\] ----
t = re.sub(r"\$\$(.*?)\$\$", lambda m: "\\[\n" + m.group(1).strip() + "\n\\]", t, flags=re.S)

# ---- 4. Citations [1], [1, 3, 4] -> \\citep{...} ----
KEY = {
    1:"RauStokes2025", 2:"HaggardKaufman2021", 3:"WaldnerLust2018", 4:"Bermeo2016",
    5:"LevitskyZiblatt2018", 6:"LuhrmannLindberg2019", 7:"Grumbach2023", 8:"Houle2009",
    9:"AcemogluRobinson2006", 10:"Boix2003", 11:"AnsellSamuels2014", 12:"Svolik2019",
    13:"Pierson1993", 14:"SossSchram2007", 15:"RothsteinUslaner2005", 16:"AcemogluEgorov2013",
    17:"SzikraOktem2023", 18:"LendvaiBainton2021", 19:"Vanhuysse2006", 20:"Benczes2024",
    21:"EnnserJedenastik2018", 22:"EspingAndersen1990", 23:"KorpiPalme1998", 24:"AcemogluNaidu2015",
    25:"Svolik2015", 26:"HuberStephens2001", 27:"HuberStephens2012", 28:"OurWorldInData2025",
    29:"BoixMiller2013", 30:"Callaway2021", 31:"SunAbraham2021", 32:"HaggardKaufman2012",
    33:"HaggardKaufman2016", 34:"Luhrmann2021", 35:"AcemogluJohnson2005", 36:"CampanteChor2012",
    37:"Ansell2010", 38:"Gethin2022", 39:"LuhrmannTannenberg2018", 40:"Coppedge2024",
    41:"GoodmanBacon2021",
}
def cite(m):
    nums = [int(x) for x in re.findall(r"\d+", m.group(1))]
    keys = [KEY[n] for n in nums]
    return "\\citep{" + ", ".join(keys) + "}"
t = re.sub(r"\[\s*(\d[\d,\s]*)\s*\]", cite, t)

# ---- 5. Straight double quotes -> `` '' ----
t = re.sub(r'"([^"\n]*)"', r"``\1''", t)

# ---- 6. Numeric ranges to en dash ----
t = re.sub(r"(\d)-(\d)", r"\1--\2", t)

# ---- 7. Bold **...** ----
t = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", t)

# ---- 8. Italic *...* (whole-line emphasis) ----
t = re.sub(r"^\*([^*]+)\*$", r"\\emph{\1}", t, flags=re.M)

# ---- 9. Collapse blank lines to single paragraph breaks ----
t = re.sub(r"\n{3,}", "\n\n", t)

open(f"{WS}/paper_body.tex", "w", encoding="utf-8").write(t)
print("written paper_body.tex, chars:", len(t))

# quick self-checks
import sys
assert "FIGURE:fig" not in t, "figure markers remain"
assert "[1]" not in t and "[2]" not in t and "[24]" not in t, "unconverted bracket citation"
leftover = re.findall(r"\[\d", t)
print("leftover bracket citations:", leftover[:5])
print("citep count:", t.count("\\citep"))
print("em dash check:", t.count("---"))
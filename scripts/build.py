import base64, json, re, sys
lesson, tpl, out, *audio = sys.argv[1:]
L = json.load(open(lesson, encoding="utf-8")); err = []
for k in ["title", "level", "lang", "dialogs", "grammar", "pitfalls", "speaking", "exercises"]:
    if not L.get(k): err.append("missing " + k)
art = L.get("type") == "article"; cjk = str(L.get("lang", "")).lower()[:2] in ("ja", "zh")
if len(L.get("dialogs", [])) != (1 if art else 2): err.append("article lesson needs 1 text" if art else "need exactly 2 dialogs")
R = {"A1": (60, 100), "A2": (100, 150), "B1": (150, 250), "B2": (220, 380), "C1": (280, 450), "C2": (300, 500)} if art else \
    {"A1": (50, 80), "A2": (80, 110), "B1": (110, 140), "B2": (130, 170), "C1": (150, 190), "C2": (160, 200)}
lo, hi = R.get(L.get("level"), (50, 500))
if art:
    src = L["dialogs"][0].get("source") or {}
    if not src.get("url") or not src.get("license"): err.append("article: source.url and source.license are required")
ui = L.get("ui_lang") or (L.get("l1", "ko") if str(L.get("level", "")).startswith("A") else L.get("lang", "fr")[:2])
if ui.lower()[:2] not in ("fr", "en", "ko") and not L.get("ui_strings"): err.append(f"interface language '{ui}' needs ui_strings (all keys of STR.fr)")
min_marks = 3 if str(L.get("level", "")).startswith("A") else 4
for i, d in enumerate(L.get("dialogs", [])):
    txt = " ".join(l["t"] for l in d["lines"]).replace("*", "")
    w = len(re.findall(r"[぀-ヿ一-鿿]", txt)) // 2 if cjk else len(re.findall(r"[\w'’-]+", txt))
    m = " ".join(l["t"] for l in d["lines"]).count("**") // 2
    print(f"text {i+1}: {w} words, {m} marked structures")
    if not lo <= w <= hi: err.append(f"text {i+1}: {w} words, target {lo}-{hi}")
    if m < min_marks: err.append(f"text {i+1}: {m} marked structures, min {min_marks}")
    if not all(l.get("l1") or l.get("ko") for l in d["lines"]): err.append(f"text {i+1}: every line needs a translation 'l1'")
    for q in ["q1", "q2", "reading"]:
        if not d.get(q) or not all(x.get("a") for x in d[q]): err.append(f"text {i+1}: {q} empty or missing answers")
    if i < len(audio):
        d["audio"] = "data:audio/mpeg;base64," + base64.b64encode(open(audio[i], "rb").read()).decode()
if not all(isinstance(s, dict) and s.get("a") for s in L.get("speaking", [])): err.append("speaking: every prompt needs a model answer 'a'")
for j, ex in enumerate(L.get("exercises", []), 1):
    for it in ex["items"]:
        if not (it.get("answers") or (ex["type"] == "dictation" and it.get("q"))): err.append(f"exercise {j}: item without answers")
        if ex["type"] == "choice" and not set(it["answers"]) <= set(it.get("options", [])):
            err.append(f"exercise {j}: answer not in options: {it['q'][:40]}")
html = open(tpl, encoding="utf-8").read()
html = html.replace("/*__LESSON_JSON__*/null", json.dumps(L, ensure_ascii=False).replace("</", "<\\/"))
html = html.replace("<title>Lesson</title>", f"<title>{L['title']}</title>")
open(out, "w", encoding="utf-8").write(html); print("written", out)
print("CHECK FAILED:\n- " + "\n- ".join(err) if err else "CHECK OK"); sys.exit(1 if err else 0)

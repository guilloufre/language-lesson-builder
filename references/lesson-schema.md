# lesson.json schema

```json
{
  "title": "Le télétravail — exprimer le but", "level": "B2", "lang": "fr-FR",
  "topic": "Le télétravail", "grammar_point": "L'expression du but",
  "objectives": ["…"],
  "dialogs": [{
    "title": "La nouvelle charte", "register": "Soutenu", "context": "Une DRH présente… au directeur.",
    "speakers": [{"name": "Mme Lambert", "gender": "f"}, {"name": "M. Ferrand", "gender": "m"}],
    "lines": [{"s": 0, "t": "Je vous ai demandé ce rendez-vous **afin de** vous présenter…", "ko": "…소개해 드리려고 이 미팅을 요청했습니다."}],
    "warmup": ["…"],
    "q1": [{"q": "Qui parle ?", "a": "…"}], "q2": [{"q": "…", "a": "…"}], "reading": [{"q": "…", "a": "…"}],
    "notes": [{"t": "une charte", "ko": "헌장, 사내 규정", "ex": "…"}]
  }],
  "grammar": [{"family": "But + infinitif (même sujet)", "note": "…",
               "items": [{"form": "pour / afin de", "mode": "+ infinitif", "ko": "~하기 위해(서)", "ex": "…"}]}],
  "vocab": [{"t": "…", "ko": "…", "ex": "…"}],
  "register": [{"formal": "travailler", "casual": "bosser"}],
  "culture": {"title": "Le télétravail en France", "text": "…"},
  "pitfalls": [{"title": "…", "explain": "…", "ko": "…", "wrong": "…", "right": "…"}],
  "speaking": [{"q": "Pourquoi apprenez-vous le français ?", "a": "J'apprends le français **pour** voyager et **afin de** lire Camus en V.O."}],
  "exercises": [
    {"title": "…", "instruction": "…", "type": "choice", "items": [{"q": "Je t'appelle ___ te prévenir.", "options": ["pour", "pour que"], "answers": ["pour"], "explain": "même sujet → infinitif"}]},
    {"title": "…", "instruction": "…", "type": "fill", "items": [{"q": "… pour que tu (venir) ___ .", "answers": ["viennes"]}]},
    {"title": "Dictée", "instruction": "Écoutez la phrase et écrivez-la.", "type": "dictation", "items": [{"q": "Je t'appelle pour te prévenir."}]},
    {"title": "…", "instruction": "…", "type": "free", "items": [{"q": "… (afin de)", "answers": ["model answer"]}]}
  ],
  "audio_note": "Audio : voix du navigateur."
}
```
In text fields, `**…**` marks a target structure (highlighted only on demand in transcripts) and `*…*` is italic. `t` = target-language expression (`fr` is still accepted).
Article lesson: `"type": "article"` and one entry in `dialogs` with `"kind": "article"`, `"speakers": [{"name": "", "gender": "f"}]`, one line per paragraph, and `"source": {"name": "Vie-publique.fr", "url": "…", "license": "Licence Ouverte Etalab 2.0", "adapted": "adapté"}`; `warmup` = before-reading questions.
Optional: `ui_lang` ("fr" | "en" | "ko") to force the interface language; `ui_strings` (all keys of `STR.fr`, including `h`) for other B1+ languages; `rate` (0.7–1) to change the default speed.

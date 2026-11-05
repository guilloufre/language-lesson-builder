#!/usr/bin/env python3
# usage: python3 tts_edge.py lesson.json   → d1.mp3, d2.mp3 (or d1.mp3 for an article)
import asyncio, json, re, subprocess, sys, edge_tts
L = json.load(open(sys.argv[1], encoding="utf-8"))
VOICES = {"fr": ("fr-FR-DeniseNeural", "fr-FR-HenriNeural"), "en": ("en-US-JennyNeural", "en-US-GuyNeural"),
          "es": ("es-ES-ElviraNeural", "es-ES-AlvaroNeural"), "de": ("de-DE-KatjaNeural", "de-DE-ConradNeural"),
          "it": ("it-IT-ElsaNeural", "it-IT-DiegoNeural"), "pt": ("pt-BR-FranciscaNeural", "pt-BR-AntonioNeural"),
          "ja": ("ja-JP-NanamiNeural", "ja-JP-KeitaNeural"), "zh": ("zh-CN-XiaoxiaoNeural", "zh-CN-YunxiNeural")}
F, M = VOICES[L.get("lang", "fr")[:2].lower()]   # other languages: run `edge-tts --list-voices` and add a pair
async def main():
    for i, d in enumerate(L["dialogs"], 1):
        parts = []
        for k, ln in enumerate(d["lines"]):
            f = f"_d{i}_{k:02}.mp3"; text = re.sub(r"\*+", "", ln["t"])
            voice = M if d["speakers"][ln["s"]]["gender"] == "m" else F
            await edge_tts.Communicate(text, voice, rate="-8%").save(f); parts.append(f)
        # step 3 (also used for ElevenLabs clips): join with 0.4 s silences
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", "0.4", "_sil.mp3"], check=True)
        open("_list.txt", "w").write("".join(f"file '{p}'\nfile '_sil.mp3'\n" for p in parts))
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", "_list.txt", "-ar", "24000", "-ac", "1", "-b:a", "64k", f"d{i}.mp3"], check=True)
asyncio.run(main())

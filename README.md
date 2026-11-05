# language-lesson-builder

**어떤 모국어 화자든, 어떤 외국어든** 인터랙티브 수업 페이지를 만드는 Claude 스킬입니다 (예: 한국인을 위한 프랑스어, 프랑스인을 위한 스페인어, 영어 화자를 위한 일본어).
기본은 한국어 화자를 위한 프랑스어이며, A1–C2 모든 레벨을 지원합니다.

*An interactive language-lesson builder for any learner language and any target language (French by default, CEFR A1–C2).*

## 무엇을 하나요
- 짧은 대화 2개(격식 / 친근) 또는 공개 라이선스 뉴스 기사 1개로 수업을 구성합니다.
- 단계별 페이지(진행 바, "전체 보기"): 1차 듣기 → 2차 듣기 → 대본 읽기 → 문법·어휘 → 학습자 모국어 기준으로 자주 틀리는 점 → 말하기 → 연습 문제.
- 대본 문장을 누르면 학습자 모국어 번역, 🔊로 문장별 따라 말하기(섀도잉), 표현마다 발음 듣기.
- 문화 노트, 모범 답안이 있는 말하기 질문, 자동 채점 연습 문제(객관식·빈칸·받아쓰기·서술), 마지막에 틀린 문제 복습.
- 페이지 안의 🎯 맞춤 연습: Claude가 답에 따라 한 문제씩 만들고 채점하며 난이도를 조절합니다 (claude.ai에서 열었을 때). 그 밖의 환경에서는 채팅에 붙여 넣을 요청 문장을 보여 줍니다.
- 자주 틀리는 점은 언어 쌍에 맞춥니다 (한국어→프랑스어: 관사·성, 프랑스어→스페인어: ser/estar·가짜 동족어 등).
- A1–A2는 안내 문구가 학습자 모국어, B1 이상은 목표 언어.
- 레벨은 생략하거나 "초급", "beginner", "advanced"처럼 말해도 됩니다 (A1–C2로 변환하고 어느 레벨로 했는지 알려 줍니다). 생략하면 지난 수업 레벨을 쓰거나 한 번 물어봅니다.
- 과거 수업 기록(채팅의 "Lesson log" 줄)을 찾아 같은 주제를 반복하지 않고 약한 부분을 다시 연습시킵니다.

## 호출 예시
- `Fais-moi une leçon B1 sur l'imparfait et le passé composé`
- `A2 프랑스어 수업 만들어줘` (주제가 없으면 3개를 제안)
- `B1 Spanish lesson from a news article`
- `일본어 A1 수업, 카페에서 주문하기`
- `Une leçon d'espagnol pour débutants francophones` (프랑스어 화자를 위한 스페인어)
- `영어 고급 수업` (레벨을 말로 지정)

## 설치
- **claude.ai**: GitHub에서 **Code → Download ZIP** → 압축을 풀고 폴더 이름을 `language-lesson-builder-main`에서 **`language-lesson-builder`**로 바꾼 뒤 그 폴더를 다시 zip으로 묶어, 설정 → 스킬(Skills)에서 업로드합니다 (claude.ai는 zip 안의 폴더 이름이 스킬 이름과 같아야 합니다). Releases에 `language-lesson-builder.zip`이 있으면 그 파일을 바로 업로드하면 됩니다.
- **Claude Code**: `git clone https://github.com/guilloufre/language-lesson-builder ~/.claude/skills/language-lesson-builder` 수업 기록은 작업 폴더의 `lesson-log.md`에 남습니다.
- 필요 환경: Python 3, ffmpeg(음성 파일을 만들 때만). 선택: `pip install edge-tts`(무료 신경망 음성), ElevenLabs 커넥터.

## 구조
```
SKILL.md                     역할 · 평가 기준 · 맥락 · 도구 · 절차 · 금지 사항
assets/lesson-template.html  페이지 템플릿 (수정하지 않음)
scripts/build.py             템플릿 채우기 + 자동 점검 (CHECK OK / FAILED)
scripts/tts_edge.py          edge-tts 음성 생성 (언어별 여성/남성 음성)
references/lesson-schema.md  lesson.json 형식
examples/                    완성된 수업 3개 (아래 참고)
```

## 결과물 예시
브라우저에서 열어 보세요:

| 파일 | 학습자 → 목표 언어 | 유형 | 레벨 |
|---|---|---|---|
| `examples/fr-b2-dialogs-ko.html` | 한국어 → 프랑스어 | 대화 2개 (재택근무, 목적 표현) | B2 |
| `examples/fr-b2-article-ko.html` | 한국어 → 프랑스어 | 뉴스 기사 (Global Voices, CC BY) — 대립·양보 | B2 |
| `examples/es-a2-dialogs-fr.html` | 프랑스어 → 스페인어 | 대화 2개 (마드리드 집 구하기, ser/estar) — 안내 문구 프랑스어 | A2 |

각 `.json`은 같은 수업의 원본 데이터입니다 (`scripts/build.py`로 다시 만들 수 있습니다).

## 음성
ElevenLabs → edge-tts → 브라우저 음성 순서로 시도합니다. 브라우저 음성은 기기에 따라 품질이 다릅니다(맥·아이폰·크롬 권장).

## 기사 출처와 저작권
읽기만 무료인 기사는 복사하지 않습니다. 재사용이 허용된 출처만 그대로 씁니다:
vie-publique.fr (Licence Ouverte), VOA Learning English (퍼블릭 도메인), Global Voices (CC BY), Wikipedia (CC BY-SA).
그 밖의 언론 기사는 사실만 바탕으로 수준에 맞게 새로 쓰고 출처를 링크합니다.

## 라이선스
MIT — `LICENSE` 참고.

# language-lesson-builder

한국어 화자를 위한 **인터랙티브 외국어 수업 페이지**를 만드는 Claude 스킬입니다.
기본 언어는 프랑스어이고, 영어·스페인어·독일어·일본어·중국어 등 다른 언어와 A1–C2 모든 레벨을 지원합니다.

## 무엇을 하나요
- 짧은 대화 2개(격식 / 친근) 또는 공개 라이선스 뉴스 기사 1개로 수업을 구성합니다.
- 단계별 페이지(진행 바, "전체 보기"): 1차 듣기 → 2차 듣기 → 대본 읽기 → 문법·어휘 → 한국인이 자주 틀리는 점 → 말하기 → 연습 문제.
- 대본 문장을 누르면 한국어 번역, 🔊로 문장별 따라 말하기(섀도잉), 표현마다 발음 듣기.
- 문화 노트, 모범 답안이 있는 말하기 질문, 자동 채점 연습 문제(객관식·빈칸·받아쓰기·서술), 마지막에 틀린 문제 복습.
- 페이지 안의 🎯 맞춤 연습: Claude가 답에 따라 한 문제씩 만들고 채점하며 난이도를 조절합니다 (claude.ai에서 열었을 때). 그 밖의 환경에서는 채팅에 붙여 넣을 요청 문장을 보여 줍니다.
- A1–A2는 안내 문구가 한국어, B1 이상은 목표 언어.
- 과거 수업 기록(채팅의 "Lesson log" 줄)을 찾아 같은 주제를 반복하지 않고 약한 부분을 다시 연습시킵니다.

## 호출 예시
- `Fais-moi une leçon B1 sur l'imparfait et le passé composé`
- `A2 프랑스어 수업 만들어줘` (주제가 없으면 3개를 제안)
- `B1 Spanish lesson from a news article`
- `일본어 A1 수업, 카페에서 주문하기`

## 설치
- **claude.ai**: 이 폴더를 zip으로 묶어 설정의 스킬(Skills) 메뉴에서 업로드합니다.
- **Claude Code**: 폴더를 `~/.claude/skills/language-lesson-builder/`에 복사합니다. 수업 기록은 작업 폴더의 `lesson-log.md`에 남습니다.
- 필요 환경: Python 3, ffmpeg(음성 파일을 만들 때만). 선택: `pip install edge-tts`(무료 신경망 음성), ElevenLabs 커넥터.

## 구조
```
SKILL.md                     역할 · 평가 기준 · 맥락 · 도구 · 절차 · 금지 사항
assets/lesson-template.html  페이지 템플릿 (수정하지 않음)
scripts/build.py             템플릿 채우기 + 자동 점검 (CHECK OK / FAILED)
scripts/tts_edge.py          edge-tts 음성 생성 (언어별 여성/남성 음성)
references/lesson-schema.md  lesson.json 형식
examples/                    완성된 프랑스어 수업 2개 (B2 대화, A1 한국어 안내)
```

## 결과물 예시
`examples/fr-b2-teletravail.html`, `examples/fr-a1-au-cafe.html`을 브라우저에서 열어 보세요.

## 음성
ElevenLabs → edge-tts → 브라우저 음성 순서로 시도합니다. 브라우저 음성은 기기에 따라 품질이 다릅니다(맥·아이폰·크롬 권장).

## 기사 출처와 저작권
읽기만 무료인 기사는 복사하지 않습니다. 재사용이 허용된 출처만 그대로 씁니다:
vie-publique.fr (Licence Ouverte), VOA Learning English (퍼블릭 도메인), Global Voices (CC BY), Wikipedia (CC BY-SA).
그 밖의 언론 기사는 사실만 바탕으로 수준에 맞게 새로 쓰고 출처를 링크합니다.

## 라이선스
MIT — `LICENSE` 참고.

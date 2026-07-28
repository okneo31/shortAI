# 가짜 세상의 진실 — 1분 쇼츠 (웹앱)

40컷 × 1.5초 = 60.0초. 자동재생 + 카메라 무브 + 나레이션(TTS) + webm 녹화.

## 구성

```
site/
├─ index.html        웹앱 본체 (단일 파일, 외부 의존 없음)
├─ img/cut01.webp    배경 40장 (1080×1890, webp q82, 합계 4.1MB)
├─ .nojekyll         GitHub Pages 의 Jekyll 처리 끄기
└─ .gitignore        mp4/webm 제외
```

이미지는 `pipeline/frames_hq/cutNN_a.png` (1440×2520 PNG, 148.7MB) 를
1080px 폭 webp 로 변환한 것입니다 — **148.7MB → 4.1MB**.
원본을 다시 바꾸면 `to_webp.py` 를 다시 돌리세요.

## GitHub Pages 배포

빈 저장소를 GitHub 에서 하나 만든 뒤 (예: `fake-world-shorts`), 이 폴더에서:

```powershell
cd D:\edu\가짜\site
git init -b main
git add .
git commit -m "가짜 세상의 진실 — 1분 쇼츠 웹앱"
git remote add origin https://github.com/<계정>/<저장소>.git
git push -u origin main
```

그다음 GitHub 저장소 → **Settings → Pages** →
Source `Deploy from a branch`, Branch `main` / `/ (root)` → Save.

1~2분 뒤 `https://<계정>.github.io/<저장소>/` 에서 열립니다.

## 조작

| 키 | 동작 |
|---|---|
| Space | 재생 / 정지 |
| ← → | 컷 이동 |
| R | 처음부터 |
| H | 컨트롤 숨김 |
| N | 나레이션 on/off |

`⏺ 영상으로 저장` 은 MediaRecorder 로 webm 을 뽑습니다.
녹화는 **브라우저에서 직접** 하세요 — Pages 에 올린 페이지에서도 됩니다.

## 완성된 mp4 는 여기 없습니다

실사 파이프라인 결과물 `pipeline/out/가짜세상_쇼츠.mp4` (80.8MB,
1080×1920 / 30fps / 60.000초 / 무음) 는 `.gitignore` 로 빠져 있습니다.
Pages 로 서빙하려면 `.gitignore` 에서 `*.mp4` 를 지우고 커밋하세요.
GitHub 의 파일 하나당 상한은 100MB 이므로 80.8MB 는 통과합니다.

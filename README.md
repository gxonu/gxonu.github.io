# gxonu.github.io 배포 가이드

## 1. 저장소 만들기 (이름이 중요!)
`github.com/gxonu/gxonu`는 프로필 README용 저장소라서 홈페이지 주소가 되지 않습니다.
GitHub에서 **New repository** → 이름을 정확히 `gxonu.github.io` 로 생성하세요 (Public).

## 2. 파일 업로드
저장소에 아래 구조로 올립니다.

```
gxonu.github.io/
├── index.html          ← 이 폴더의 파일
└── assets/
    ├── profile.jpg     ← 증명사진/프로필 사진 (정사각형 권장)
    └── GeonwooKim_CV.pdf
```

웹에서 하려면: 저장소 페이지 → Add file → Upload files → 드래그 앤 드롭 → Commit.

터미널로 하려면:
```bash
git clone https://github.com/gxonu/gxonu.github.io.git
cd gxonu.github.io
# index.html, assets/ 복사 후
git add . && git commit -m "Initial homepage" && git push
```

## 3. GitHub Pages 활성화
저장소 → Settings → Pages → Source: `Deploy from a branch`, Branch: `main` / `(root)` → Save.
1~2분 후 https://gxonu.github.io 에서 확인할 수 있습니다.

## 4. 로고 스트립 (Experience 섹션)
`assets/logos/` 폴더에 아래 파일명으로 로고 이미지를 넣으면 자동으로 표시됩니다 (없으면 자동으로 숨겨짐).

```
assets/logos/kaist.png
assets/logos/inha.png
assets/logos/upflow.png
```

- KAIST/인하대 로고는 각 학교의 UI(상징) 안내 페이지에서 공식 시그니처 PNG를 받는 것이 가장 깔끔합니다 (배경 투명 PNG 권장)
- 높이 34px로 렌더링되므로 가로형 로고가 잘 어울립니다
- 기본은 흑백 처리, 마우스를 올리면 원색으로 살아나는 justin4ai 스타일입니다

## 5. 수정 포인트
- 프로필 사진 파일명이 다르면 index.html의 `assets/profile.jpg` 부분을 수정
- 논문이 생기면 News/Research 섹션에 항목 추가 (Publications 섹션으로 확장 가능)
- Google Scholar 계정이 생기면 sidebar 링크에 추가

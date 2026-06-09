# CLAUDE.md — skon-vision-ai 프로젝트 가이드

## 프로젝트 개요

Vision AI 기초 교육 과정 자료 프로젝트.
CNN(Convolutional Neural Network) 이론과 MNIST 손글씨 분류 실습을 통해 딥러닝 기반 이미지 인식의 핵심 개념을 학습한다.

- **대상**: AI Literacy 수준의 비전공자 4명
- **총 교육 시간**: 4시간 (4개 챕터 × 50분)
- **교육 방식**: 이론(`.md`) + 실습(`.ipynb`)
- **실습 데이터**: MNIST 손글씨 데이터셋 (28×28×1 흑백 이미지, 0~9 분류)
- **최종 목표**: Shallow CNN 모델을 직접 구축 → 학습 → 손글씨 추론까지 체험

---

## 디렉토리 구조

```
skon-vision-ai/
├── CLAUDE.md                        ← 이 파일
├── prompt.txt                       ← 교육 자료 작성 지시사항 (원본 프롬프트)
│
├── chapter 01. Vision AI 소개 및 CNN 핵심 이론/
│   ├── 01_Vision_AI_소개.md          ← 이미지 구조, 주요 Task, 다양한 Task 소개
│   ├── 02_CNN_핵심_이론.md           ← Convolution, Pooling, Activation Function
│   └── images/                      ← 교육 이미지 9장 (PNG)
│       ├── 01_image_hwc_structure.png
│       ├── 02_ml_vs_dl_pipeline.png
│       ├── 03_vision_ai_main_tasks.png
│       ├── 04_vision_ai_various_tasks.png
│       ├── 05_convolution_operation.png
│       ├── 06_conv_filters_features.png
│       ├── 07_pooling_operation.png
│       ├── 08_activation_functions.png
│       └── 09_receptive_field.png
│
├── chapter 02. Vision AI Task별 주요 Loss, Metric 이론/
│   ├── 01_주요_Loss_Metric_이론.md    ← 4가지 Task별 Loss와 Metric 개념 정리
│   └── images/                      ← 개념 설명 시각 자료 4장
│       ├── classification_matrix.png
│       ├── object_detection_iou.png
│       ├── segmentation_overlap.png
│       └── anomaly_reconstruction.png
│
├── chapter 03. Shallow CNN 모델 및 학습 Loop 구현/
│   └── 01_Shallow_CNN_실습.ipynb     ← PyTorch 기반 MNIST CNN 실습 노트북
│
└── chapter 04. 추론 및 Wrap-up/
    └── README.md                    ← 미작성 (placeholder)
```

---

## 챕터별 교육 내용

### Chapter 01 — Vision AI 소개 및 CNN 핵심 이론 ✅ (작성 완료)

**Section 1: Vision AI 소개** (`01_Vision_AI_소개.md`)
- **1-1. 이미지 데이터의 특징**: H×W×C 구조, 픽셀=Feature, 고차원 데이터 특성
- **1-2. Vision AI 주요 태스크**: Classification, Object Detection, Segmentation, Anomaly Detection
- **1-3. 다양한 태스크**: HuggingFace 기준 인식·분석 / 멀티모달 / 생성 태스크 소개

**Section 2: CNN 핵심 이론** (`02_CNN_핵심_이론.md`)
- **2-1. Convolution**: 슬라이딩 윈도우 + 합성곱 연산, 필터 학습 과정, 계층적 특징 추출
- **2-2. Pooling**: Max Pooling vs Average Pooling, 수용 영역(Receptive Field) 확장
- **2-3. Activation Function**: 비선형성의 필요성, ReLU / Sigmoid / Tanh / GELU 비교

### Chapter 02 — Vision AI Task별 주요 Loss, Metric 이론 ✅ (작성 완료)

**01_주요_Loss_Metric_이론.md**
- **Loss와 Metric의 차이**: 모델 학습용(Loss) vs 사람의 평가용(Metric)
- **분류 (Classification)**: Cross-Entropy Loss / Accuracy, Confusion Matrix, Precision, Recall, F1-Score
- **객체 탐지 (Object Detection)**: Bounding Box Loss, Classification Loss / IoU, mAP
- **분할 (Segmentation)**: Pixel-wise CE Loss, Dice Loss / mIoU, Dice Coefficient
- **이상 탐지 (Anomaly Detection)**: Reconstruction Loss (MSE/MAE) / AUROC, F1-Score

### Chapter 03 — Shallow CNN 모델 및 학습 Loop 구현 ✅ (작성 완료)

**01_Shallow_CNN_실습.ipynb**
- 환경 설정 및 라이브러리 임포트 (PyTorch, torchvision)
- MNIST 데이터 로딩, 탐색, 시각화
- DataLoader 구성 (Batch, Epoch, Step 개념 설명)
- ⭐ Shallow CNN 모델 정의 (핵심 코드 주석 처리 → 수강생 직접 구현)
- Loss(CrossEntropyLoss) 및 Optimizer(Adam) 설정
- ⭐ Training Loop 구현 (Forward→Loss→Backward→Step 핵심 코드 주석 처리)
- 학습 결과 시각화 (Loss/Accuracy 그래프)
- 테스트 데이터 예측 결과 확인
- 모델 가중치 저장 (.pth)

### Chapter 04 — 추론 및 Wrap-up 🔲 (미작성)

예상 내용: 학습된 모델로 직접 손글씨 이미지 추론, 결과 해석, 전체 과정 복습

---

## 기술 스택 & 컨벤션

| 항목 | 내용 |
|------|------|
| **프레임워크** | PyTorch (예상) |
| **데이터셋** | MNIST (torchvision) |
| **이론 자료** | Markdown (`.md`) |
| **실습 자료** | Jupyter Notebook (`.ipynb`) — 마크다운 셀로 수강생 안내 포함 |
| **이미지 참조** | 상대 경로 (`images/` 디렉토리) |
| **언어** | 한국어 |

### 문서 작성 스타일

- 학습 목표를 각 섹션 상단에 blockquote로 명시
- 이모지 활용으로 가독성 확보 (📘, 💡, 📌, ⭐ 등)
- ASCII 다이어그램과 표로 개념 시각화
- 핵심 포인트는 `> 💡` / `> 📌` blockquote로 강조
- 외부 참고 자료 링크 포함 (HuggingFace, CNN Explainer, cs231n 등)

---

## 작업 시 유의사항

1. **수강생 수준 고려**: AI Literacy 수준 — 수식보다 직관적 설명과 시각 자료 우선
2. **이론 ↔ 실습 연결**: 이론 문서에서 설명한 개념이 실습 노트북에서 코드로 구현되도록 일관성 유지
3. **이미지 자산**: Chapter 01에 9장의 교육용 PNG 이미지가 이미 생성되어 있음
4. **미작성 챕터**: Chapter 02~04는 `README.md`만 존재 (빈 파일, 1바이트) — 순차적으로 작성 필요
5. **실습 파일**: `.ipynb` 형식으로 작성하되 마크다운 셀을 충분히 활용하여 수강생 가이드 제공
6. **MNIST 실습 흐름**: 데이터 로드 → 모델 정의(Shallow CNN) → 학습 Loop → 추론(직접 손글씨)

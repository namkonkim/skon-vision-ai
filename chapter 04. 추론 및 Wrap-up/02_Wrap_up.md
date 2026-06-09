# 📘 Section 2. Wrap-up: 복습 및 앞으로의 방향

> **학습 목표**
> - 4개 챕터의 핵심 내용을 빠르게 복습한다.
> - 현대적인 프레임워크를 활용하면 동일한 작업을 얼마나 간결하게 할 수 있는지 체험한다.
> - 앞으로의 학습 방향과 실무 적용 가이드를 파악한다.

---

## 🔄 전체 복습: 우리가 배운 것

### Chapter 01 — Vision AI 소개 및 CNN 핵심 이론

```
이미지 = H × W × C 의 3차원 숫자 배열
         │
         ▼
CNN이 자동으로 특징을 학습
  • Convolution: 필터가 슬라이딩하며 특징(엣지, 텍스처, 형태) 추출
  • Activation (ReLU): 비선형성을 부여하여 복잡한 패턴 학습 가능
  • Pooling: 공간 크기를 줄여 더 넓은 영역의 특징을 포착
```

### Chapter 02 — Task별 주요 Loss와 Metric 이론

| 구분 | 역할 | 분류(Classification) 예시 |
|------|------|---------------------------|
| **Loss** | 모델 학습 기준 (미분 가능) | Cross-Entropy Loss |
| **Metric** | 사람이 성능을 평가하는 기준 | Accuracy, F1-Score |

### Chapter 03 — Shallow CNN 모델 및 학습 Loop 구현

```
Training Loop의 핵심 5단계:

  ① outputs = model(images)       # Forward Pass
  ② loss = criterion(outputs, labels)  # Loss 계산
  ③ loss.backward()               # Backward Pass (기울기 계산)
  ④ optimizer.step()              # 가중치 업데이트
  ⑤ optimizer.zero_grad()         # 기울기 초기화
```

### Chapter 04 — 추론

```
추론은 Forward Pass만 수행:

  with torch.no_grad():           # 기울기 계산 OFF (속도↑, 메모리↓)
      output = model(input)       # Forward Pass
      pred = output.argmax()      # 가장 높은 확률의 클래스 = 예측 결과
```

---

## 🚀 현대적인 프레임워크로 같은 일을 한다면?

우리는 교육 목적으로 CNN 모델과 학습 루프를 처음부터 직접 구현했습니다.
하지만 **실무에서는 이미 검증된 프레임워크와 사전학습 모델**을 활용하여 훨씬 간결하게 작성합니다.

같은 MNIST 분류 문제를, 현대적인 도구로 작성하면 어떻게 달라지는지 비교해봅시다.

---

### 📦 사용할 도구

| 도구 | 역할 | 설명 |
|------|------|------|
| **timm** | 모델 빌드 | PyTorch Image Models — 수백 개의 사전학습 Vision 모델을 1줄로 사용 |
| **PyTorch Lightning** | 학습 루프 | 반복적인 Training Loop 코드를 자동화하는 고수준 프레임워크 |

---

### 🔨 모델 빌드: EfficientNet을 단 2줄로

우리가 Chapter 03에서 직접 정의한 Shallow CNN:

```python
# 우리가 작성한 코드 (약 20줄)
class ShallowCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(2)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(2)
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(32*7*7, 10)

    def forward(self, x):
        x = self.pool1(self.relu1(self.conv1(x)))
        x = self.pool2(self.relu2(self.conv2(x)))
        x = self.fc(self.flatten(x))
        return x
```

**timm을 사용하면:**

```python
import timm

# ImageNet으로 사전학습된 EfficientNet-B0 모델을 MNIST용으로 로드 (1줄!)
model = timm.create_model('efficientnet_b0', pretrained=True, num_classes=10, in_chans=1)
```

> 💡 **이 1줄이 하는 일:**
> - `efficientnet_b0`: 수백만 장의 ImageNet 데이터로 학습된 고성능 CNN 모델을 가져옴
> - `pretrained=True`: **사전학습 가중치**를 로드 (Transfer Learning)
> - `num_classes=10`: 출력을 MNIST 10개 클래스에 맞게 자동 조정
> - `in_chans=1`: 입력 채널을 MNIST 흑백(1채널)에 맞게 자동 조정

---

### ⚡ 학습 루프: PyTorch Lightning으로 간결하게

우리가 Chapter 03에서 직접 구현한 Training Loop:

```python
# 우리가 작성한 코드 (약 40줄)
for epoch in range(NUM_EPOCHS):
    model.train()
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
    # ... 평가 코드 ...
```

**PyTorch Lightning을 사용하면:**

```python
import pytorch_lightning as pl

class MNISTModel(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.model = timm.create_model('efficientnet_b0', pretrained=True,
                                        num_classes=10, in_chans=1)

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        images, labels = batch
        outputs = self(images)
        loss = nn.CrossEntropyLoss()(outputs, labels)
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=0.001)


# 학습 실행 (단 2줄!)
trainer = pl.Trainer(max_epochs=5)
trainer.fit(model, train_loader)
```

> 💡 **Lightning이 자동으로 해주는 일들:**
> - GPU/CPU 자동 감지 및 데이터 이동
> - 진행률 표시 (Progress Bar)
> - 로깅 및 체크포인트 저장
> - `model.train()` / `model.eval()` 자동 전환
> - `optimizer.zero_grad()`, `loss.backward()`, `optimizer.step()` 자동 호출

---

### 📊 비교 요약

|  | 직접 구현 (우리가 한 것) | 프레임워크 활용 (실무) |
|--|--------------------------|------------------------|
| **모델 정의** | ~20줄 (Conv, ReLU, Pool 직접 쌓기) | **1줄** (`timm.create_model`) |
| **학습 루프** | ~40줄 (Forward, Loss, Backward, Step 직접 작성) | **~15줄** (Lightning이 자동 처리) |
| **모델 성능** | Shallow CNN (단순 구조) | EfficientNet (ImageNet 사전학습) |
| **전이 학습** | ❌ 처음부터 학습 | ✅ 사전학습 가중치 활용 |
| **학습 이해도** | ⭐⭐⭐ 원리를 깊이 이해 | ⭐ 내부 동작을 추상화 |

> 📌 **핵심 메시지**
>
> 우리가 이번 교육에서 직접 구현한 것은 **"원리를 이해하기 위한 과정"**이었습니다.
> 실무에서는 검증된 프레임워크를 활용하여 생산성을 높이되,
> **"내부에서 무슨 일이 일어나는지 이해하고 있는 것"**이 문제 해결의 핵심 역량이 됩니다.

---

## 🔑 핵심 키워드 정리

| 키워드 | 설명 |
|--------|------|
| **CNN** | 이미지의 공간적 특징을 자동으로 학습하는 딥러닝 모델 |
| **Convolution** | 필터를 슬라이딩하며 이미지에서 특징(엣지, 텍스처 등)을 추출하는 연산 |
| **Pooling** | 특징 맵의 공간 크기를 줄여 수용 영역을 확장하는 연산 |
| **Activation (ReLU)** | 비선형성을 부여하여 복잡한 패턴 학습을 가능하게 하는 함수 |
| **Loss** | 모델 예측과 정답의 차이를 수치화 (학습의 기준) |
| **Metric** | 사람이 모델 성능을 평가하기 위한 지표 |
| **Forward Pass** | 입력 → 모델 → 출력 (예측 계산) |
| **Backward Pass** | 출력 → 입력 방향으로 기울기(Gradient)를 계산 |
| **Epoch / Batch** | 전체 데이터 1바퀴 / 한 번에 넣는 데이터 묶음 |
| **Inference** | 학습 완료된 모델로 새로운 데이터를 예측하는 과정 |
| **Transfer Learning** | 사전학습된 모델을 가져와 내 데이터에 맞게 미세조정하는 기법 |

---

## 🚀 더 나아가려면?

| 주제 | 설명 | 참고 자료 |
|------|------|-----------|
| **더 깊은 CNN 모델** | ResNet, EfficientNet 등 실전 모델 구조 이해 | [PyTorch Model Zoo](https://pytorch.org/vision/stable/models.html) |
| **전이학습 (Transfer Learning)** | 사전학습 모델을 가져와 내 데이터에 미세조정 | [PyTorch Transfer Learning Tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html) |
| **데이터 증강 (Augmentation)** | 학습 데이터를 인위적으로 변형하여 늘리는 기법 | [Albumentations](https://albumentations.ai/) |
| **객체 탐지 실습** | YOLO 등으로 실시간 객체 탐지 체험 | [Ultralytics YOLO](https://docs.ultralytics.com/) |
| **timm 라이브러리** | 수백 개의 Vision AI 모델을 간편하게 사용 | [timm GitHub](https://github.com/huggingface/pytorch-image-models) |
| **PyTorch Lightning** | 학습 루프 자동화 프레임워크 | [Lightning Docs](https://lightning.ai/docs/pytorch/stable/) |
| **HuggingFace** | Vision AI 모델을 쉽게 사용하는 플랫폼 | [HuggingFace Tasks](https://huggingface.co/tasks) |

---

### 🎓 수고하셨습니다!

이번 교육을 통해 Vision AI의 기초 이론부터 실제 모델 구현, 학습, 추론까지의
**전체 파이프라인**을 직접 체험하셨습니다.

```
   이론 (Chapter 01~02)          실습 (Chapter 03~04)
   ─────────────────            ─────────────────
   이미지 구조 이해       →     MNIST 데이터 탐색
   CNN 연산 원리          →     모델 직접 구현
   Loss & Metric 개념     →     학습 루프 작성
   추론의 의미            →     손글씨 인식 체험
                                        │
                                        ▼
                              실무에서는 timm, Lightning 등
                              프레임워크로 생산성 ↑↑↑
```

오늘 배운 **분류(Classification)**는 모든 Vision AI Task의 기초입니다.
이 경험을 바탕으로 객체 탐지, 분할 등 더 다양한 Task에도 도전해 보세요! 🚀

# [6회차] NLP 과제

발제자: 이준찬

## 기간
- **마감**: 1월 29일 목요일 23:59까지
- **지각**: 2월 5일 목요일 23:59까지

## Intro
이번 과제는 **NLI 데이터셋**을 활용하여 **Natural Language Inference(NLI)** 태스크를 수행하는 것입니다.

NLI는 두 문장(premise, hypothesis) 간의 관계를 **entailment**(함의), **neutral**(중립), **contradiction**(모순) 세 가지 중 하나로 분류하는 태스크입니다. 사전학습된 한국어 언어 모델을 파인튜닝하여 분류 성능을 개선하는 것이 목표입니다.

## 명세

### 환경 설정 - 로컬 전용
1. 구글드라이브에서 
```bash
# venv 사용
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 또는 conda 사용
conda env create -f environment.yml
conda activate kornli
```

2. 설치 확인:
```bash
python -c "import torch, transformers, pandas; print('OK')"
```

### 데이터

- 학습 데이터 : `train.tsv`
- 검증 데이터 : `val.tsv`
- 테스트 데이터 : test (제출 csv 생성용)

### 학습 (한국어 언어모델 파인튜닝) 및 추론

- 파인튜닝 학습 설정 : `config.py` → 자유롭게 변경해주세요!
- 기본 모델 : `model.py` 의 distilkobert → 자유롭게 변경해주세요!
- 전처리 : `preprocess.py` → 자유롭게 변경해주세요!

- 학습 및 추론 실행 (로컬 GPU 보유 시)

```bash
#   가상환경 설치 후 실행
  
cd baseline                                                                                    
python main.py   # 학습 실행                                                          
```

- 학습 및 추론 실행 (Colab)

```bash
# baseline.ipynb 로 Google Colab 에서 실행
# 데이터셋 Google Drive or 직접 업로드
```

- 실행 완료 시 Submission.csv 생성

```bash
# submission.csv 
# id
```

## 제출 방법

https://ybigtads-dashboard.vercel.app/

- 위 링크에서 6회차 과제 제출 Tab 에 submission.csv 제출 (제출 파일 이름은 자유입니다)

별도 코드 제출은 없습니다. 자유롭게 튜닝 후 정답 csv 만 제출해주시면 됩니다!

## **채점 기준**

### Pass 기준 - 리더보드

- [ ]  제출 후 리더보드 Accuracy가 60**% 이상**
- [ ]  지각 제출 시 - 제출 기한 65% 이상 충족

### 최종 결과 판정

- 통과 : Submission 제출 및 리더보드에 60% 이상의 accracy 포함 시
- 미흡 : 위 제출 기준을 달성하지 못할 시
- 미제출 : 전체 기간 중  submission.csv 미제출
# Stock_Portfolio_Visualization

# 📈 주식 포트폴리오 분석기

## 📋 목차

- [🎯 목적](#-목적)
- [📦 라이브러리](#-라이브러리)
- [🔧 설정 방법](#-설정-방법)
- [🏃 실행 방법](#-실행-방법)
- [📝 코드 설명](#-코드-설명)

---

## 🎯 목적

CSV 파일에 명시된 주식 포트폴리오의 성과를 분석하고 시각화합니다.

---

## 📦 라이브러리

- `pandas`: 데이터 처리와 분석 🐼
- `yfinance`: Yahoo Finance에서 주식 데이터를 다운로드 🌐
- `matplotlib`: 그래프를 통한 데이터 시각화 📊
- `datetime`: 날짜 및 시간을 다룸 ⏰

---

## 🔧 설정 방법

1. 필요한 라이브러리를 설치합니다.
    ```bash
    pip install pandas yfinance matplotlib
    ```

---

## 🏃 실행 방법

1. 종목 코드와 마켓 정보가 저장된 CSV 파일을 준비합니다. (`TurtleMinervini_08-31.csv`)
2. 코드를 실행합니다.
    ```bash
    python your_script_name.py
    ```

---

## 📝 코드 설명

### `fetch_prices`

- `input_filename`: 분석할 주식의 종목 코드가 저장된 CSV 파일의 경로
- `period`: 주식 데이터를 가져올 기간 (예: "1mo", "1y", "5y")

#### 동작 과정

1. 주식 종목 코드를 CSV 파일에서 불러옵니다.
2. 종목 코드를 yfinance에 맞게 변환합니다.
3. 지정된 기간 동안의 종가 데이터를 다운로드합니다.
4. 다운로드한 데이터를 새로운 CSV 파일에 저장합니다.

---

### `plot_portfolio_performance`

- `prices_csv`: `fetch_prices` 함수로 생성된 가격 데이터 CSV 파일
- `tickers_csv`: 종목 코드와 이름이 저장된 CSV 파일

#### 동작 과정

1. 가격 데이터와 종목 정보를 불러옵니다.
2. 각 종목의 수익률을 계산합니다.
3. 포트폴리오 전체의 평균 수익률을 계산합니다.
4. 계산된 정보를 바 차트로 시각화합니다.

---

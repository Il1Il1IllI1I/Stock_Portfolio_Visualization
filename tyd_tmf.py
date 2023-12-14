import matplotlib.pyplot as plt
import yfinance as yf

# TYD와 TMF의 주가 데이터를 가져오기 위한 기간 설정
start_date = '2023-01-01'
end_date = '2023-12-13'

# yfinance를 사용하여 TYD와 TMF의 주가 데이터를 가져옴
tyd = yf.download('TYD', start=start_date, end=end_date)
tmf = yf.download('TMF', start=start_date, end=end_date)

# 두 데이터의 종가를 이용하여 시각화
plt.figure(figsize=(12, 6))

# 첫 번째 y축 (왼쪽) 설정
ax1 = plt.gca()
ax1.plot(tyd.index, tyd['Close'], color='blue', label='TYD')
ax1.set_xlabel('Date')
ax1.set_ylabel('TYD Price', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# 두 번째 y축 (오른쪽) 설정
ax2 = ax1.twinx()
ax2.plot(tmf.index, tmf['Close'], color='red', label='TMF')
ax2.set_ylabel('TMF Price', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# 제목 및 범례 설정
plt.title('TYD and TMF Price Comparison (2023)')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()

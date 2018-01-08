#
# Monte Carlo valuation of European call option
# in Black-Scholes-Merton model
# 블랙-숄즈-머튼 모형을 사용한 유러피안 콜 옵션의 몬테카를로 방식 가격 계산
# bsm_mcs_euro.py
#

import numpy as np

# Parameter Values
S0 = 100.   # initial index level, 초기의 주가지수
K = 105.    # strike price, 행사가
T = 1.0     # time-to-maturity, 만기까지 남은 시간
r = 0.05    # riskless short rate, 무위험 이자율
sigma = 0.2 # valatility, 변동성

I = 100000  # number of simulations, 시뮬레이션 횟수

#Valuation Algorithm, 가격결정 알고리즘
z = np.random.standard_normal(I)    #pseudorandom numbers, 유사난수
ST = S0 * np.exp((r - 0.05 * sigma ** 2) * T + sigma * np.sqrt(T) * z)

# index values at maturity, 만기 시의 주가지수
hT = np.maximum(ST - K, 0)  # inner values at maturity, 만기 시의 내재 가치
C0 = np.exp(-r * T) * np.sum(hT) / I    # Monte Carlo estimator, 몬테카를로 추정식

print('Value of the European Call Option %5.3f' % C0)
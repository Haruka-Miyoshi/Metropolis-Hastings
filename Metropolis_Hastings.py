import random
import matplotlib.pyplot as plt

# MH法 実装
def metropolis_hasting(__alpha, __theta, __step):
    # 乱数列
    rnd = []
    __sample = __alpha
    for i in range(__step):
        next_prob = randoms(__alpha-__theta, __alpha+__theta)
        if randoms(0, 1) < likelihood(next_prob)/likelihood(__sample):
            __sample = next_prob
        rnd.append(__sample)
    return rnd
    
# 尤度関数
def likelihood(sample):
    # もし、サンプルが0よりも小さい　または　1よりも大きい場合
    if sample < 0 or sample > 1:
        return 0
    else:
        return 1*sample

# 一様乱数
def randoms(__alpha, __beta):
    return (random.random() * (__beta - __alpha) + __alpha)

# 適当にプロット
if __name__ == '__main__':
    # 初期サンプル、提案幅、試行回数
    rnd = metropolis_hasting(1.0, 1.0, 200)
    plt.title('Metropolis Hastings')
    plt.xlim(0,200)
    plt.plot(rnd)
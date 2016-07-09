import numpy as np

def push_borad(T,d,H):
    L0 = 0.0
    L = 1.0
    g = 9.81

    while abs(L - L0) > 0.00001:
        k = 2 * np.pi / L
        L0 = L
        L = g * T ** 2 / (2 * np.pi) * np.tanh(k * d)

    k = 2 * np.pi / L
    w = 2 * np.pi / T
    x = H * k * 9.8 * (np.sinh(2 * k * d) + 2 * k * d)
    p = 4 * w ** 2 * np.cosh(k * d) * np.sinh(k * d)
    X0 = x / p

    print('波长为：%f' % L)
    print('冲程为：%f' % X0)

if __name__ == '__main__':
    push_borad(T=2.0,d=0.5,H=0.1)
import numpy as np


def main():
    n = 4
    a = [[0, 8, 9], [7, 5, 8], [3, 9, 6], [1, 6, 0]]
    F = [5, 7, 1, 10]
    # a = np.zeros((n, 3))
    a = np.array(a)
    u = np.zeros(n)
    F = np.array(F)
    alfa = np.zeros(n)
    beta = np.zeros(n)
    n -= 1
    alfa[0] = - a[0, 2] / a[0, 1]
    beta[0] = F[0] / a[0, 1]
    alfa[n] = - a[n, 0] / a[n, 1]
    beta[n] = F[n] / a[n, 1]
    for i in range(1, n):
        alfa[i] = - a[i, 2] / (a[i, 0] * alfa[i-1] + a[i, 1])
        beta[i] = (F[i] - a[i, 0] * beta[i-1]) / (a[i, 0] * alfa[i-1] + a[i, 1])
    u[n] = (alfa[n] * beta[n - 1] + beta[n]) / (1 - alfa[n] * alfa[n - 1])
    for i in reversed(range(n)):
        u[i] = alfa[i] * u[i + 1] + beta[i]
    print(u)

if __name__ == "__main__":
    main()

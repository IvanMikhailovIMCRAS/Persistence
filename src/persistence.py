import numpy as np
import matplotlib.pyplot as plt # type: ignore


def mean_cos(k: float) -> float:
    if k == 0.0:
        return 0.0
    else:
        return (np.exp(-2*k)*(np.exp(2*k)*(k-1)+k+1) / k) / (1-np.exp(-2*k))


def persistence_length(k: float, length_bond: float) -> float:
    if k == 0.0:
        return 0.0
    else:
        return length_bond / abs(np.log(mean_cos(k)))


def kuhn_segment(k: float, length_bond: float) -> float:
    return length_bond * (1+mean_cos(k)) / (1-mean_cos(k))


if __name__ == '__main__':
    k = np.arange(0.0, 20.5, 0.5)
    m_cos = np.array([mean_cos(x) for x in k])
    l_k = np.zeros(len(k))
    l_p = np.array([persistence_length(x, length_bond=1.0) for x in k])
    l_k = np.array([kuhn_segment(x, length_bond=1.0) for x in k])
    # plt.plot(k, m_cos)
    # plt.savefig('m_cos.jpg')
    plt.plot(k, l_p)
    plt.savefig('l_p.jpg')

import numpy as np 
from scipy.optimize import minimize

def sig(x):
    return 1/(1 + np.exp(-x))

# Vector with the difference
def cost(x):
    sum = 0
    for idx in range(len(x)):
        sum += x[idx]**2
    return sum/len(x)

def main():
    # Testing with arrays
    vectorized_sig = np.vectorize(sig)
    vectorized_cost = np.vectorize(cost)
    x0 = [1, 2, 3]
    x1 = [1, 1, 1]
    x0 = np.array(x0)
    x1 = np.array(x1)

    diff = x0 - x1
    result = cost(diff)
    print(result)
    #bds = set_bds(diff)
    bds = [(0, 1) for _ in diff]
    opt_result = minimize(cost, diff, method='powell')
    print(opt_result)

if __name__ == "__main__":
    main()

import numpy as np
import random

def create_W_single_pattern(pattern):
    if len(pattern.shape) != 1:
        print("The input is not vector")
        return
    else:
        w = np.zeros([len(pattern),len(pattern)])
        for i in range(len(pattern)):
            for j in range(i,len(pattern)):
                if i == j:
                    w[i,j] = 0
                else:
                    w[i,j] = pattern[i]*pattern[j]
                    w[j,i] = w[i,j]
    return w
    
def energy(weight,x,bias=0):
        #weight: m*m weight matrix
        #x: 1*m data vector
        #bias: outer field
    energy = -x.dot(weight).dot(x.T)+sum(bias*x)
        # E is a scalar
    return energy

def update_asynch(weight,vector,theta=0.5,times=100):
    energy_ = []
    times_ = []
    energy_.append(energy(weight,vector))
    times_.append(0)
    for i in range(times):
        length = len(vector)
        update_num = random.randint(0,length-1)
        next_time_value = np.dot(weight[update_num][:],vector) - theta
        if next_time_value>=0:
            vector[update_num] = 1
        if next_time_value<0:
            vector[update_num] = -1
        times_.append(i)
        energy_.append(energy(weight,vector))
    return (vector,times_,energy_)

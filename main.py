import numpy as np
import matplotlib.pyplot as plt

'''parameters of our simulation : 
    - probability 1-q of taking the majoritary opinion of neighbours
    - N shape of our matrix
    - seed_number: random parameter of our initial opinion distribution
    - nb_step: defines how man steps we want in our simulation'''

parameters = {

"seed_number":0.45,
"q":0.2,
"N": 300,
"nb_step":20

}

#set one person (cell of the matrix), returns the neighbouring opinion.
def neighbouring_opinion(M, i, j):
    s = 0
    
    #adding neighbours' opinion to s:total
    try : 
        s += M[i+1][j]
    except :
        pass
    
    try : 
        s += M[i-1][j]
    except :
        pass

    try : 
        s += M[i][j+1]
    except :
        pass

    try : 
        s += M[i][j-1]
    except :
        pass
    
    return np.sign(s)

def step(M):

    #transition matrix that defines how people change their mind
    P = np.random.binomial(1, 1-parameters["q"], M.shape)
    
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if P[i][j] == 1: 
                M[i][j] = neighbouring_opinion(M, i, j)

    return M

def plot_results():

    a = (parameters["N"], parameters["N"])

    M = np.random.binomial(1, parameters["seed_number"], a)
    M = 2*M - np.ones(a)

    for i in range(parameters["nb_step"]):
        M = step(M)
    plt.imshow(M)
    plt.show()
    



    


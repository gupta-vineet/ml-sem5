import math as m

D=20
LB=-100
UB=100

def FitnessFunction(x):
    s=0
    p=1
    for i in range(0,D):                  #Griewank Function
        s=s+(x[i]**2/4000)
        p=p*(m.cos(x[i]/m.sqrt(i+1)))
        n=s-p+1
    return n
        
            

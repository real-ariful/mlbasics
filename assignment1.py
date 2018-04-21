sq_sum(4)

#Problem1
def sq_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    print(sum)

#Problem2

plot_2()
def plot_2():
    import numpy as np
    import matplotlib.pyplot as plt
    
    pi = np.pi
    x=np.arange(-2*pi,2*pi,pi/12)
    y1=np.cos(x)+np.sin(x)
    y2= np.exp(x)
    
    plt.title("y1=cox(x)+sin(x) and y2=e^x graph together")
    plt.plot(x,y1,label="y1=cox(x)+sin(x)")
    plt.plot(x,y2,label="y2=e^x")
    plt.xlabel("x (in radians)")
    plt.ylabel("y1 and y2")
    plt.legend()
    plt.show()
    
#Problem3
Z=['e','m','i','n','e','m']   
name_repeat(Z)    
def name_repeat(A):
    #A=['e','m','i','n','e','m']
    #print(len(A))

    for i in range(0,len(A)):
        print(A)



    
    
    
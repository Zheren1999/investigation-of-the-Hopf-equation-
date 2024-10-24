import numpy as np 
import matplotlib.pyplot as plt

N = 100 #number of points in grid t
L = 1500 #number of points in grid x
h = 15.0/float(L) #for x
tau = 1.0/float(N) #for t
def plotmaker_1(time): #plot the graphs
    X, h = np.linspace(-5,10,L+1,retstep=True) #set of coordinate points
    y1 = u_exact(time) #exact solution for t = time
    y2 = integrator(time) #numerical solution
    fig = plt.figure()
    plt.plot(X,y1,color='red', label='the exact solution') #red - the exact solution
    plt.plot(X,y2,color='blue', label='the numerical solution') #blue - the numerical solution
    plt.xlabel('x')
    plt.ylabel('u')
    plt.legend()
    plt.grid(True)
    plt.ylim([-0.5,2]) #HERE THE SCALE OF GRAPHS IS CHANGING
    plt.xlim([-5,10])
def f(u,x,t): #the difference u-exp(-0.5(x-tu)^2)
    return u - np.exp(-0.5*np.power(x-u*t,2))
def f_der(u,x,t): #derivative of the difference with respect to u
    return 1 - t*(x-t*u)*np.exp(-0.5*np.power(x-u*t,2))
eps = 1.0/np.power(10,3) #the accuracy of finding the roots is SET HERE
def root_hunter(x,t): #gives the roots of the transcendental equation, initial iteration u = 1
    u = 1
    while(abs(f(u,x,t)) >= eps):
        u = u - float(f(u,x,t)/f_der(u,x,t))
    return u
def u_exact(t): #the exact solution
    exact_curve = []
    for i in range(L+1):
        exact_curve.append(root_hunter(float(h*i)-5, t))
    return exact_curve
def u_o(x): #the initial function
    return np.exp(-0.5*np.power(x,2))
def integrator(t): #integrates up to the moment t
    T = int(float(t)/tau) #the number of points
    u = []
    tmp = [] 
    for i in range(L+1):
        u.append(u_o(h*float(i) - 5)) 
    for i in range(T+1):
        for j in range(L+1):
            u[0] = 0.0 #boundary condition u(-5) = 0
            tmp.append(u[j] - (tau/(2*h))*(u[j]+u[j-1])*(u[j] - u[j-1]))
        u = tmp
        tmp = []
    return u
plotmaker_1(1)
r = [] #discrepancy
numerical = integrator(1)
for i in range(L+1):
    r.append(abs(numerical[i] - u_exact(1)[i]))
print (max(r))

def integrator_2(t): #integrates up to time t
    T = int(float(t)/tau) #the number of points
    u = []
    tmp = [] 
    predic_1 = 0 #predictor j
    predic_2 = 0 #predictor j-1
    for i in range(L+1):
        u.append(u_o(h*float(i) - 5)) #the initial function
    for i in range(T+1):
        tmp.append(0.0)
        for j in range(1,L):
            predic_1 = u[j] - (tau/(2*h))*(u[j+1]+u[j])*(u[j+1] - u[j])
            predic_2 = u[j-1] - (tau/(2*h))*(u[j]+u[j-1])*(u[j] - u[j-1])
            tmp.append(0.5*(u[j] + predic_1)-(tau/(4*h))*(predic_1**2-predic_2**2))
        tmp.append(0.0)
        u = tmp
        tmp = []
    return u
def plotmaker_2(time): #plot the graphs
    X, h = np.linspace(-5,10,L+1,retstep=True) #set of coordinate points
    y1 = u_exact(time) #the exact solution for t = time
    y2 = integrator_2(time) #the numerical solution
    fig = plt.figure()
    plt.plot(X,y1,color='red', label='the exact solution') #red - exact solution
    plt.plot(X,y2,color='blue', label='the numerical solution') #blue - numerical solution
    plt.xlabel('x')
    plt.ylabel('u')
    plt.legend()
    plt.grid(True)
    plt.ylim([-0.5,2]) #HERE THE SCALE OF THE GRAPHS IS CHANGING
    plt.xlim([-5,10])
plotmaker_2(1)
r = [] #discrepancy
numerical = integrator_2(1)
for i in range(L+1):
    r.append(abs(numerical[i] - u_exact(1)[i]))
print(max(r))
import matplotlib as mpl

u_surface = integrator_2(0) #connecting temporary layers into one two-dimensional array
for i in range(1,N+1):
    u_surface = np.vstack((u_surface, integrator_2(float(tau*i)))) #visualization of 1 scheme (integrator)

from mpl_toolkits.mplot3d import axes3d #3D graphs
T = np.linspace(0,1.649,N+1)
X = np.linspace(-5,10,L+1)
Xa, Ta = np.meshgrid(X,T) 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
dem3d = ax.plot_surface(Ta,Xa,u_surface, cmap='afmhot')
plt.xlabel('t')
plt.ylabel('x')
plt.show()
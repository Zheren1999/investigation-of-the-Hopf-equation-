# Hopf equation in physics
Let's consider a two-dimensional medium consisting of particles moving by inertia, without intersection and in the absence of external forces. Denote $u(t,x)$ is the speed of a particle located at a point in time $t$ and space point $x$. If $x=q(t)$ is the trajectory of motion of some fixed particle, then its speed $q'(t)=u(t, q(t))$ and acceleration $q''(t)$ is equal to zero. 

![image](https://user-images.githubusercontent.com/89813720/202877434-1efe118e-f409-49bd-835d-5fe2c09405f6.png)

the resulting equation describing the evolution of the velocity field of non - interacting particles is called Hopf equation:

![image](https://user-images.githubusercontent.com/89813720/202877442-5f9aced4-9472-4e87-a304-7a07031687b3.png)

# The analytical solution for Hopf equation

# Rollover effect

# Model description



# Newton's method
Newton's method (Newton-Raphson method) is an iterative numerical method for finding the root of a given function. The method was first proposed by the English physicist, mathematician, and astronomer Isaac Newton. The search for a solution is carried out by constructing successive approximations based on simple iteration principles. 

To numerically solve the equation: $f (x) = 0$ by simple iteration, it must be reduced to the equivalent equation: $x = φ(x)$ where phi is the contraction display. For the best convergence of the method at the next approximation point $x^*$, the condition: $φ'(x∗) = 0$

The solution to this equation is sought in the form: $φ(x) = x + α(x)f(x)$, then we can get: $φ'(x^*) = 1 + α'(x^*)f(x^*) = 0 $
Assuming that the point of approximation is ”close enough” to the root  ̄xand that the given function is continuous:
$f (x^*)= f ( ̄x) = 0$, final formula for $α(x)$ is: $α(x) =-1/f'(x)$
With this in mind, the function $φ(x)$ is defined:
$φ(x) = x − f (x)/f'(x)$

The algorithm for Newtons method can be described as follows:
1. Set the initial approximation $x_0$
2. Until the stop condition is met, which can be taken as $|x_{n+1}-x_{n}|<\epsilon$ that is, the error is within the required limits, calculate a new approximation: 

![image](https://user-images.githubusercontent.com/89813720/202877424-0c895daa-905b-4152-9cc1-1bd9d7cefdc1.png)

\section{Lax-Friedrichs scheme}

The Lax-Friedrichs scheme is defined in numerical analysis as a method for the numerical solution of hyperbolic partial differential equations based on the finite difference method.

\subsection{Extensions to Nonlinear Problems}

The formula defines the hyperbolic system of one-dimensional conservation laws:

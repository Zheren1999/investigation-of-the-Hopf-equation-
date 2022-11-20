# Hopf equation in physics

![image](https://user-images.githubusercontent.com/89813720/202878060-6b641f13-da41-4f2e-be2c-e8e213fd76a3.png)

Hokusai, The Great Wave off Kanagawa, 1823

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

# Lax-Friedrichs scheme

The Lax-Friedrichs scheme is defined in numerical analysis as a method for the numerical solution of hyperbolic partial differential equations based on the finite difference method.

Extensions to Nonlinear Problems

The formula defines the hyperbolic system of one-dimensional conservation laws:

![image](https://user-images.githubusercontent.com/89813720/202877485-74943515-9ade-454c-a4f5-4fe87978c1ed.png)

In general, $f$ is a vector that has components. A generalization of the Lax-Friedrichs scheme to nonlinear systems takes the form:

![image](https://user-images.githubusercontent.com/89813720/202877517-0fb16b5d-e594-4a1f-8406-f4d98342111b.png)

This conservative scheme is of order 1 in space and time. On the other hand, it can be used to construct higher-order schemes for solving systems of hyperbolic partial differential equations, in the same way that Euler's method is used to construct more accurate Runge-Kutta type methods for solving ordinary differential equations.

This scheme can be written in a conservative form:

![image](https://user-images.githubusercontent.com/89813720/202877546-15962490-a2f7-4bca-b2e5-e964da8338b3.png)

The Lax-Friedrichs scheme is explicit and has order 1 in space and time. For this reason, it is not used as often in practice. This scheme is stable under the following condition:

![image](https://user-images.githubusercontent.com/89813720/202877577-2e8442e6-8a88-45f8-aa76-c312485d4c19.png)


# McCormack scheme
Difference schemes "predictor-corrector"

Predictor-corrector schemes are a family of methods related to algorithms designed to integrate ordinary differential equations. All such techniques involve two steps:
1. At the first step (predictor), some function is calculated from values calculated in the previous step to get the approximated value of the desired function in the following point.
2. At the second step (corrector), the received approximation using the predicted value function and another operator to interpolate the value desired position at the same point.
The following system can represent this scheme:

where $u^{n+1/2}$ is the value obtained at the "predictor" step, and $u^{n+1}$ is the refined desired value.
It can be seen that the first step is implemented using explicit methods, and the second step is based on the application of formulas of implicit methods; on the right side, instead of the unknown value $u^{n+1}$, the result is substituted predictions $u^{n+1/2}$.

Methods using the predictor-corrector scheme:
1. Milne method – for ODE;

2. Heun's method (predictor - Euler's method, corrector - Method trapezium). 

When using the predictor-corrector scheme for solving the ODE note the high accuracy of the calculation and the absence of properties
self-starting (that is, to start calculations according to the scheme predictor-corrector must first be used another self-starting method).

3. Adams-Bashfort method -  for solutions non-rigid boundary value problems (the Adams-Bashfort-Multon corrector is used);

4. Hamming formulas.

5. McCormack method.



# Hopf equation in physics

![image](https://user-images.githubusercontent.com/89813720/202878060-6b641f13-da41-4f2e-be2c-e8e213fd76a3.png)

(Hokusai, The Great Wave off Kanagawa, 1823)

Let's consider a two-dimensional medium consisting of particles moving by inertia, without intersection and in the absence of external forces. Denote $u(t,x)$ is the speed of a particle located at a point in time $t$ and space point $x$. If $x=q(t)$ is the trajectory of motion of some fixed particle, then its speed $q'(t)=u(t, q(t))$, and acceleration $q''(t)$ is equal to zero. 

![image](https://user-images.githubusercontent.com/89813720/204052501-0a79a09c-62c1-4a73-95eb-9d468e3ce4d4.png)

The resulting equation describing the evolution of the velocity field of non - interacting particles is called Hopf equation

![image](https://user-images.githubusercontent.com/89813720/204052561-9ce662b1-b616-4df5-b1d2-a1cc14cfbfb9.png)

**The analytical solution of Hopf equation**

The analytical solution of Hopf equation can be determined by method of characteristics: 

![image](https://user-images.githubusercontent.com/89813720/204052673-135a4257-955a-4771-989d-639740cbd659.png)

where, $g$ is the continuous function.

It is necessary to invert the map $x = x_{0} + u_{0}(x_{0})t$ concerning $x_{0}$, and then substitute it into the expression for $u$ to find the explicit dependence $u = u(x,t)$ (the parametric solution), which is most often found in literature: 

![image](https://user-images.githubusercontent.com/89813720/204052722-6826c960-6415-49f4-a74b-98bcee80060b.png)

The solution of the Hopf equation can be easily analyzed. According to the solution, each point of the velocity profile moves with its own (constant) velocity.
In this case, the velocity profile will be deformed since faster particles will overtake the slower ones. As a result, the shape is steeper, and at time $t = t^{*}$, the gradient of $x$ becomes endless. This phenomenon is called overturning or gradient catastrophe \cite{kuznetsov2022slipping}. To find the overturning time $t^{*}$, it is necessary to calculate
derivative $\frac{\partial{u}}{\partial{x}}$:

![image](https://user-images.githubusercontent.com/89813720/204052768-f8020b0b-a9f7-43c2-90d8-025b1260d2ee.png)

where $J = \frac{\partial{x}}{\partial{x_{0}}} = 1 + u'_{0}(x_{0})t$ is the Jacobian of $x = x_{0} + u_{0}(x_{0})t$. It can be seen from this expression that the derivative becomes infinite for the first time when the Jacobian, $J=0$ and corresponding $t^{*}$ can be expressed as the following formula:

![image](https://user-images.githubusercontent.com/89813720/204052798-350cf044-3da5-41ae-8572-f38c71ed99fd.png)

This minimum corresponds to the point $x^{*}$ (the breaking point). From this, it is clear that the overturning occurs for the initial profiles with a negative derivative $u_{x} < 0$. For $t > t^{*}$, the equation $J = 0$ has two roots, respectively. The derivative goes to infinity at two points.  The area of ambiguity is between these points. From the mapping point of view, this means that the mapping $x = x(x_{0}, t)$ is single-valued — the equation $x = x(x_{0}, t)$ has only one (real) root $x_{0} = x_{0}(x, t)$ for all $x$. For $t > t^{*}$, the equation $x = x(x_{0} , t)$ has three roots $x_{0}$ for any $x$ from the ambiguity domain. A change in the number of roots of a mapping is called a bifurcation. In this case, one root converts to three roots at the bifurcation point $(x^{*}, t^{*}, u^{*})$. The bifurcation point is also called the cusp point.
In physics, overturning is the cause of the formation of shock waves. When approaching the overturning point, the equations of ideal hydrodynamics lose their applicability in real gas.

**Model description**

We study the Hopf equation with following limits: $0<t<1$ , $-5<x<10$, and the initial condition:

![image](https://user-images.githubusercontent.com/89813720/204052920-ce54fc1d-f950-45d6-ba28-a31f741cd5ef.png)

Using the the analytical solution of this problem is represented by the following formula: 

![image](https://user-images.githubusercontent.com/89813720/204052949-015447c8-610a-4a5b-a82d-b00ab0b285fe.png)

We use Newton's method for two different numerical schemes (Lax-Friedrichs and MacCormack schemes) to solve the Hopf equation with the following limits and the initial condition.

# Newton's method

Newton's method (Newton-Raphson method) is an iterative numerical method for finding the root of a given function \cite{more1982newton,polyak2007newton}. The search for a solution is carried out by constructing successive approximations based on simple iteration principles. 

**Description**

To numerically solve the Eq.~(\ref{Eq.10}), by simple iteration it must be reduced to the equivalent expression Eq.~(\ref{Eq.11}).

![image](https://user-images.githubusercontent.com/89813720/204053086-5e150b58-0ec6-44fb-802e-f1c64d63ecb8.png)

where, $\phi$ is the contraction display. The following condition:

![image](https://user-images.githubusercontent.com/89813720/204053105-b926667e-e826-45f1-a55c-3c93aa66d794.png)

is used for the best convergence of the method at the next approximation point $y^*$. The solution to this equation is sought in the form:

![image](https://user-images.githubusercontent.com/89813720/204053129-db818f0d-9651-4b88-b5f0-6914061f9114.png)

that implies: 

![image](https://user-images.githubusercontent.com/89813720/204053150-99c09b3e-8c73-45ed-b7fd-ecf6a6a8554c.png)

Assuming that the point of approximation is "close enough" to the root $\bar {y} $ and that the given function is continuous:

![image](https://user-images.githubusercontent.com/89813720/204053163-f411a6ee-f41d-4817-bbcf-f41808ab1eee.png)

The final formula for $\alpha(y)$ is:

![image](https://user-images.githubusercontent.com/89813720/204053205-3b5e22de-0232-495f-8b2a-5c36e8e3aeaa.png)

The function $\phi(y)$ is defined:

![image](https://user-images.githubusercontent.com/89813720/204053227-4cbcdd84-fcb9-4b21-8dde-1a0abe6715f1.png)

**Algorithm**

The algorithm for Newtons method can be described as follows:\\
1. Set the initial approximation $y_0$\\
2. Until the stop condition is met, which can be taken as $|y_{n+1}-y_{n}|<\epsilon$, the error is within the required limits, calculate a new approximation:  

![image](https://user-images.githubusercontent.com/89813720/204053280-735545dd-ad8f-4b5d-8eec-d5aee182fe7f.png)

We utilize Lax - Friedrichs and MacCormack numerical schemes using Newton's method to determine the numerical solution.








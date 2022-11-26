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
In this case, the velocity profile will be deformed since faster particles will overtake the slower ones. As a result, the shape is steeper, and at time $t = t^* $, the gradient of $x$ becomes endless. This phenomenon is called overturning or gradient catastrophe [2]. To find the overturning time $t^* $, it is necessary to calculate
derivative $\frac{\partial{u}}{\partial{x}}$:

![image](https://user-images.githubusercontent.com/89813720/204052768-f8020b0b-a9f7-43c2-90d8-025b1260d2ee.png)

where ![image](https://user-images.githubusercontent.com/89813720/204060318-e7a374c7-e542-4d19-9234-2397b0e159e8.png)  is the Jacobian of $x = x_{0} + u_{0}(x_{0})t$. It can be seen from this expression that the derivative becomes infinite for the first time when the Jacobian, $J=0$ and corresponding time can be expressed as the following formula:

![image](https://user-images.githubusercontent.com/89813720/204052798-350cf044-3da5-41ae-8572-f38c71ed99fd.png)

This minimum corresponds to the point **x***  (the breaking point). From this, it is clear that the overturning occurs for the initial profiles with a negative derivative $u_x < 0$. For $t > t^* $, the equation $J = 0$ has two roots, respectively. The derivative goes to infinity at two points.  The area of ambiguity is between these points. From the mapping point of view, this means that the mapping $x = x(x_{0}, t)$ is single-valued — the equation $x = x(x_{0}, t)$ has only one (real) root $x_{0} = x_{0}(x, t)$ for all $x$. For $t > t^* $, the equation $x = x(x_{0} , t)$ has three roots $x_{0}$ for any $x$ from the ambiguity domain. A change in the number of roots of a mapping is called a bifurcation. In this case, one root converts to three roots at the bifurcation point . The bifurcation point is also called the cusp point.
In physics, overturning is the cause of the formation of shock waves. When approaching the overturning point, the equations of ideal hydrodynamics lose their applicability in real gas.

**Model description**

We study the Hopf equation with following limits: **0 < t < 1 , -5 < x < 10**, and the initial condition:

![image](https://user-images.githubusercontent.com/89813720/204052920-ce54fc1d-f950-45d6-ba28-a31f741cd5ef.png)

Using the the analytical solution of this problem is represented by the following formula: 
![image](https://user-images.githubusercontent.com/89813720/204065098-81b45982-d8e4-480b-98a8-d5f7459e2460.png)

The overturning effect at which $u_{x}$ turns to infinity and the function ceases to be single-valued arises at the moment, $t^{*}=1.649$:

![image](https://user-images.githubusercontent.com/89813720/204052949-015447c8-610a-4a5b-a82d-b00ab0b285fe.png)

We use Newton's method for two different numerical schemes (Lax-Friedrichs and MacCormack schemes) to solve the Hopf equation with the following limits and the initial condition.

# Newton's method

Newton's method (Newton-Raphson method) is an iterative numerical method for finding the root of a given function [3, 4]. The search for a solution is carried out by constructing successive approximations based on simple iteration principles. 

**Description**

To numerically solve the Eq. 10, by simple iteration it must be reduced to the equivalent expression Eq. 11.

![image](https://user-images.githubusercontent.com/89813720/204053086-5e150b58-0ec6-44fb-802e-f1c64d63ecb8.png)

where, $\phi$ is the contraction display. The following condition:

![image](https://user-images.githubusercontent.com/89813720/204053105-b926667e-e826-45f1-a55c-3c93aa66d794.png)

is used for the best convergence of the method at the next approximation point $y^*$. The solution to this equation is sought in the form:

![image](https://user-images.githubusercontent.com/89813720/204053129-db818f0d-9651-4b88-b5f0-6914061f9114.png)

that implies: 

![image](https://user-images.githubusercontent.com/89813720/204053150-99c09b3e-8c73-45ed-b7fd-ecf6a6a8554c.png)

Assuming that the point of approximation is "close enough" to the root $\bar {y}$ and that the given function is continuous:

![image](https://user-images.githubusercontent.com/89813720/204053163-f411a6ee-f41d-4817-bbcf-f41808ab1eee.png)

The final formula for $\alpha(y)$ is:

![image](https://user-images.githubusercontent.com/89813720/204053205-3b5e22de-0232-495f-8b2a-5c36e8e3aeaa.png)

The function $\phi(y)$ is defined:

![image](https://user-images.githubusercontent.com/89813720/204053227-4cbcdd84-fcb9-4b21-8dde-1a0abe6715f1.png)

**Algorithm**

The algorithm for Newtons method can be described as follows:

1. Set the initial approximation $y_0$

2. Until the stop condition is met, which can be taken as $|y_{n+1}-y_{n}|<\epsilon$, the error is within the required limits, calculate a new approximation:  

![image](https://user-images.githubusercontent.com/89813720/204053280-735545dd-ad8f-4b5d-8eec-d5aee182fe7f.png)

We utilize Lax - Friedrichs and MacCormack numerical schemes using Newton's method to determine the numerical solution.

# Numerical schemes

**Lax - Friedrichs**

The Lax-Friedrichs scheme is defined in numerical analysis as a method for the numerical solution of hyperbolic partial differential equations based on the finite difference method [5].

**Extensions to Nonlinear Problems**

The formula defines the hyperbolic system of one-dimensional conservation laws:

![image](https://user-images.githubusercontent.com/89813720/204053476-93cb9ecb-275f-4d35-aed4-36bb4a25525b.png)

A generalization of the Lax - Friedrichs scheme to nonlinear systems can be expressed in the following form:

![image](https://user-images.githubusercontent.com/89813720/204053514-f6e824a1-949e-4e2a-8ad0-4cb1afd52e7a.png)

Lax - Friedrichs numerical scheme can be used to construct higher-order schemes for solving systems of hyperbolic partial differential equations, in the same way that Euler's method is used to construct more accurate Runge-Kutta method for solving ordinary differential equations [6].

This scheme can be written in a conservative form:

![image](https://user-images.githubusercontent.com/89813720/204053570-5f17647d-254f-487a-a393-a024df710c0a.png)

The Lax - Friedrichs scheme is explicit and has approximation error is $O(\Delta t, \Delta x)$. For this reason, it is not used as often in practice. This scheme is stable under the following condition:

![image](https://user-images.githubusercontent.com/89813720/204053597-e6c3a65c-eae3-4b56-9e21-114a4784358b.png)

**MacCormack scheme**

**Difference schemes "predictor-corrector"**

Predictor-corrector schemes are a family of methods related to
algorithms designed to integrate ordinary
differential equations [7, 8]. All such techniques involve two steps [9]:

1. At the first step (predictor), some function is determined from values calculated in the previous step to get the approximated value of the desired function in the following point.

2. At the second step (corrector), the received approximation using the predicted value function and another operator to interpolate the value desired position at the same point.

The following steps can represented as the following expressions:

![image](https://user-images.githubusercontent.com/89813720/204053889-3c63acff-eeef-4b3a-974a-01bda884fb6d.png)

where, $u^{n+1/2}$ is the value obtained at the "predictor" step, and $u^{n+1}$ is the refined
desired value.
It can be seen that the first step is implemented using explicit methods, and
the second step is based on the application of formulas of implicit methods. On the right side, instead of the unknown value $u^{n+1}$, the result is substituted predictions $u^{n+1/2}$.

Methods using the predictor-corrector scheme:

1. Milne method for ODE.

2. Heun method (predictor - Euler's method, corrector - Trapezium method).

3. Adams-Bashforth method for solutions non-rigid boundary value problems (the Adams-Bashforth-Moulton corrector is used).

4. MacCormack method.

**MacCormack method**

The MacCormack method is a modified two-step scheme
Lax - Wendroff, but it is much easier to use [10].
Consider the following first-order hyperbolic equation:

![image](https://user-images.githubusercontent.com/89813720/204057548-33203c5e-a58a-4a1d-bf28-fc5f44c8457e.png)

Predictor: At this step, the predicted value of $w$ at the moment time $k+1$: $\bar{w}^{k+1}_{i}$ is evaluated as follows:

![image](https://user-images.githubusercontent.com/89813720/204057584-5daec011-40b7-4bad-9000-478c88b4f55c.png)

Corrector: At this step, the predicted value $\bar{w}^{k+1}_{i}$
corrected according to the equation:

![image](https://user-images.githubusercontent.com/89813720/204057612-6f769ed5-ded2-4641-9e54-2ed3cac75126.png)

Note that the intermediate value $\bar{w}^{k+1}_{i}$
doesn't make sense physically.
The scheme has the second order of accuracy with an approximation error $O(\Delta t^2, \Delta x^2)$, while it is stable at $|a\frac{\Delta t}{\Delta x}|\leq1$. The differential approximation of the scheme has the following form:

![image](https://user-images.githubusercontent.com/89813720/204057636-827b83cd-3cc6-4c92-9f9f-9fbe1d9e03ae.png)

The MacCormack scheme is often used due to a number of its advantages [11]. In particular, it operates only with quantities in the primary
grid nodes and can be easily generalized to multidimensional problems. Also, this is the schematic
second-order accuracy.

# Results and Discussion

**Lax - Friedrichs scheme**

We convert the Hopf equation into the divergent form: 

![image](https://user-images.githubusercontent.com/89813720/204057695-7e82191a-ed76-4206-af51-8805c9ad850a.png)

and using Eq. 21 we can get the Lax - Friedrichs numerical scheme: 

![image](https://user-images.githubusercontent.com/89813720/204057717-9db76ec7-286c-4341-a502-674acb041432.png)

where $dt$ and $dx$ are discretization steps in the time and space domain correspondingly. The upper index defines the time location, and the lower represents the spatial location of the function. 
The scheme requires a boundary condition on the left side (x=0). We use $u^n_{0}=0$ because of the exponential damping of the initial function.

We studied the solution of the Hopf equation for different values of time: $t = 0.5, 1, 1.649, 1.8$. 
The Fig. 1 compares analytical and numerical solutions for a given time. In addition, the maximum discrepancy $r$ between the analytical and numerical solutions was calculated for the Lax - Friedrichs scheme. 

![image](https://user-images.githubusercontent.com/89813720/204058668-d62f34ea-04c9-42f4-b428-dceafeb27596.png)

![image](https://user-images.githubusercontent.com/89813720/204058707-5eb8f5c6-a553-48b6-8e58-ad53114b25bd.png)


The Fig. 2 shows the 3D numerical solution of the Hopf equation for $t = 1$ and $t = 1.65$
As can be seen, for the time $t=1.65$ overturning effect occurs, the velocity profile becomes steep.

![image](https://user-images.githubusercontent.com/89813720/204058611-c8044476-635d-46c9-9431-b131ae24f722.png)


**MacCormack scheme**

Similarly, as in the previous numerical scheme, we used the divergent form of the differential equation. We calculate the predictor using the following formula: 

![image](https://user-images.githubusercontent.com/89813720/204057765-c33692a2-8d15-484e-9ee5-924d912f34d6.png)

Later, to determine the corrector, the predicted value of the function we approximated using the following formula:

![image](https://user-images.githubusercontent.com/89813720/204057781-1e8a2f1c-f42d-4c87-9f93-9070aa4a3cc1.png)

The Fig. 3 shows the 3D numerical solution of Hopf equation using MacCormack scheme. In the same way as in the Lax - Friedrichs scheme, numerical solutions were constructed for different values of time $t$ (Fig. 4) for MacCormack scheme. We use the number of time discretization points $N_{t} = 100$ and the spatial discretization, $N_{x} =1500 $, for both numerical schemes. Fig. 1 and Fig. 4 show that the analytical and numerical solutions coincide very well. However, the maximum discrepancy $r$ when using the MacCormack scheme is less than for the Lax - Friedrichs scheme (Fig. 5). It can be explained by the fact that the MacCormack scheme has the second order of accuracy $O(\Delta t^2, \Delta x^2)$ in contrast to the Lax - Friedrichs scheme $O(\Delta t, \Delta x)$. Also, it can be seen that the maximum discrepancy $r$ is increasing with increasing time $t$. Up to the overturning time, $t^* $, the difference rises very slightly. After this time, the maximum value of discrepancy increases significantly. It is due to the overturning effect. The solution becomes ambiguous after reaching the overturning time $t^* $.

![image](https://user-images.githubusercontent.com/89813720/204058820-b63c9c1c-9a38-4f8e-92e6-d6f41e8672c5.png)


![image](https://user-images.githubusercontent.com/89813720/204058850-967f497e-0cc5-496e-bac6-5f3c27522568.png)

![image](https://user-images.githubusercontent.com/89813720/204058862-3a2157f6-bfe8-4b09-874a-1c3381eb36be.png)


![image](https://user-images.githubusercontent.com/89813720/204058836-1e0baf3f-ff29-4ad9-bc28-1ba3918bd748.png)


**References**

[1] Kuznetsov, E., and Shapiro, D., 2011. “Methods of mathematical physics: a course of lectures”. Novosibirsk State University.

[2] Kuznetsov, E., and Mikhailov, E., 2022. “Slipping flows and their breaking”. Annals of Physics,p. 169088.

[3] Mor ́e, J. J., and Sorensen, D. C., 1982. Newton’s method. Tech. rep., Argonne National Lab., IL (USA).

[4] Polyak, B. T., 2007. “Newton’s method and its use in optimization”. European Journal of Operational Research, 181(3), pp. 1086–1096.

[5] DuChateau, P., and Zachmann, D. W., 2002. Applied partial differential equations. Courier Corporation.

[6] CHU, C., 1978. Numerical methods in fluid dynamics, in “advances in applied mechanics”(cs. yih, ed.), vol. 18.

[7] Zhang, P.-G., and Wang, J.-P., 2012. “A predictor - corrector compact finite difference scheme for burgers’ equation”. Applied Mathematics and Computation, 219(3), pp. 892–898.

[8] Butcher, J. C., 2016. Numerical methods for ordinary differential equations. John Wiley & Sons.

[9] Press, W., Teukolsky, S., Vetterling, W., and Flannery, B., 2007. “Section 17.6. multistep, multivalue, and predictor-corrector methods”. Numerical
Recipes: The Art of Scientific Computing.

[10] Anderson, J. D., and Wendt, J., 1995. Computational fluid dynamics, Vol. 206. Springer.

[11] Hixon, R., and Hixon, R., 1997. “On increasing the accuracy of maccormack schemes for aeroacoustic applications”. In 3rd AIAA/CEAS Aeroacoustics Conference, p. 1586.










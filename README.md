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


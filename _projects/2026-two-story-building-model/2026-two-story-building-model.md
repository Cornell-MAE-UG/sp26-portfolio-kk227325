---
layout: project
title: Two Story Building Model
description: Numerical Simulation and Computation for ENGRD 3200
technologies: [Python, Markdown]
image: /assets/images/2026-two-story-building-model/tsbm-problem.png
caption: "Figure 1: Two-story Building Model"
thumbnail: /assets/images/2026-two-story-building-model/tsbm-problem.png
mathjax: true
---

This project uses a passive two-story building model to model the effect of an earthquake on a structure, employing various numerical analysis tools.

**Given:**

The governing equations of the TSBM:

$$m_2 \ddot{x}_2 + F_d + F_{sp} = -m_2 \ddot{x}_g$$

$$m_1 \ddot{x}_1 - F_d - F_{sp} = -m_1 \ddot{x}_g -c_f \dot{x}_1 -k_f x_1$$

<ul>
  <li>$\mathbf{x_1}$ & $\mathbf{x_2}$ = displacements of the first and second floors, respectively, as functions of time.</li>
  <li>$\mathbf{\ddot{x}}$ = given function of time of ground acceleration due to the earthquake</li>
  <li>$\mathbf{F_{sp}}$ = spring force</li>
  <li>$\mathbf{F_{d}}$ = damper force</li>
  <li><b>Constants:</b>
    <ul>
      <li>First floor mass: $\mathbf{m_1 = 533.5} \textbf{ kg}$</li>
      <li>Second floor mass: $\mathbf{m_2 = 552.5} \textbf{ kg}$</li>
      <li>Foundation stiffness: $\mathbf{k_f = 456000} \textbf{ N/m}$</li>
      <li>Foundation damping coefficient: $\mathbf{m_2 = 552.5} \textbf{ kg}$</li>
    </ul>
  </li>
</ul>


Additionally, the spring and damper forces behave as non-linear polynomial functions of aggregate displacement $\Delta x = x_2 - x_1$ and $\Delta \dot{x} = \dot{x}_2 - \dot{x}_1$ as follows:

$$F_{sp} = k_1 \Delta x + k_2 \Delta x^2 + k_3 \Delta x^3$$

$$F_{d} = c_1 \Delta \dot{x} + c_2 \Delta \dot{x}^2$$

with unknown coefficients.

Lastly, we will model the earthquake ground acceleration function as a sine wave that lasts a single period:

$$\ddot{x}_g = A\sin (\omega t) \,\,\,\,\, 0 \leq t \leq T = \frac{2 \pi}{\omega}$$

***

The code <a href="{{ "sp26-portfolio-kk227325/_projects/2026-two-story-building-model/2026-two-story-building-model.py" | relative_url }}">2026-two-story-building-model.py</a> accomplishes the following tasks:

***

**Task 1:** Performs a polynomial least squares fit on the datasets <i>springforce.csv</i> ($F_{sp}$ as a function of $\Delta x$) and <i>dampingforce.csv</i> ($F_{d}$ as a function of $\Delta \dot{x}$). Plots the two curves and computes the coefficients $k_1$, $k_2$, $k_3$, $c_1$, and $c_2$.

**Results:**
The code uses the <i>polylsq()</i> function to fit the data and achieve the following polynomials:

$$F_{sp} = 1.09994172 \times 10^{-5} \cdot ∆x - 6.30745659 \times 10^-6 \cdot ∆x^2 + 3.35810023 \times 10^9 \cdot ∆x^3$$

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/2026-two-story-building-model/tsbm-spring.png" alt="tsbm-spring" width="400" />
    <figcaption align="center"><b>Figure 2: Least squares polynomial of spring force vs aggregate displacement</b></figcaption>
  </p>
</figure>

$$F_{d} = 90.86709091 \cdot ∆\dot{x} + 2.54104188 \cdot ∆\dot{x}^2$$

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/2026-two-story-building-model/tsbm-damper.png" alt="tsbm-damper" width="400" />
    <figcaption align="center"><b>Figure 3: Least squares polynomial of damping force vs aggregate velocity</b></figcaption>
  </p>
</figure>

***

**Task 2:** Converts the governing equations to a system of four 1st order ordinary differential equations and solves the system numerically with the 4th order Runge-Kutta method. 

The simulation was done over 10 seconds using an earthquake duration of $T = 2.5$ s and two different forcing amplitudes of $A = 4.4$ m/s<sup>2</sup> and $16$ m/s<sup>2</sup>. The initial conditions of each variable were set to zero for at $t = 0$ s.

Note: the system of four 1st order ODE's is as follows:

$$\left\{
\begin{array}{ll}
      \dot{x}_1 = v_1 \\
      \dot{x}_2 = v_2 \\
      \dot{v}_1 = \frac{1}{m_1} \left[ F_d(v_2 - v_1) + F_{sp}(x_2-x_1) - c_fv_1 - k_fx_1 \right] - \ddot{x}_g \\
      \dot{v}_2 = -\frac{1}{m_2} \left[ F_d(v_2 - v_1) + F_{sp}(x_2-x_1) \right] - \ddot{x}_g \\
\end{array} 
\right.$$

Note that $v_2 - v_1$ and $x_2 - x_1$ are the <i>inputs</i> to the $F_d$ and $F_{sp}$ functions, respectively.

**Results:**

We determined that using a time step of $h = T/200$ achieved timestep independence, as the solutions for this time step were essentially indistinguishable from the solutions if we reduced the time step by half, to $h = T/400$. Figures 4 and 5 shows our numerically determined solutions to the system of ODE's for each forcing amplitude.

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/2026-two-story-building-model/tsbm-rk4-4.4.png" alt="tsbm-rk4-4.4" width="400" />
    <figcaption align="center"><b>Figure 4: Solution of ODE using the Runge-Kutta method, A = 4.4 m/s<sup>2</sup></b></figcaption>
  </p>
</figure>

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/2026-two-story-building-model/tsbm-rk4-16.png" alt="tsbm-rk4-16" width="400" />
    <figcaption align="center"><b>Figure 5: Solution of ODE using the Runge-Kutta method, A = 16 m/s<sup>2</sup></b></figcaption>
  </p>
</figure>

***

**Task 3:** Re-solves the ODE for the $A = 4.4$ m/s<sup>2</sup> case with the forward Euler method instead, first with a timestep of $h = T/6400$, and then with an even smaller timestep that matches the accuracy of the Runge-Kutta method.

**Results:**

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/2026-two-story-building-model/tsbm-fe-T6400.png" alt="tsbm-fe-T6400" width="400" />
    <figcaption align="center"><b>Figure 6: Solution of ODE using the Forward-Euler a method, h = T/6400<sup>2</sup></b></figcaption>
  </p>
</figure>

Figure 6 shows that for Forward Euler method, even with a timestep as small as T/6400, the graphs did not converge, and in fact, appeared to diverge for x<sub>1</sub> and v<sub>1</sub>. Thus, we needed an even smaller time step.

From trial and error, we found that at $h = T/10000$, the absolute difference between each method was below $10^{-2}$ for all four variables at time t = 2T. So, we determined that this timestep gave us a solution of comparable accuracy to the Runge-Kutta method at $h = T/200$.

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/2026-two-story-building-model/tsbm-fe-T10000.png" alt="tsbm-fe-T10000" width="400" />
    <figcaption align="center"><b>Figure 5: Solution of ODE using the Runge-Kutta method, h = T/10000<sup>2</sup></b></figcaption>
  </p>
</figure>

The results are summarized in the following table:

**Table 1: Comparing values at $x_1$, $x_2$, $v_1$, and $v_2$ at $t = 2T$**

| | Runge-Kutta, $h=T/200$ | Forward Euler, $h=T/10000$ | Absolute difference |
| :---: | :---: | :---: | :---: |
| $x_1$ | $-0.0001405736569685958$ | $-0.0005913086740531184$ | $0.00045073501708452256$ |
| $x_2$ | $-0.0001405736569685958$ | $-0.0005913086740531184$ | $0.00045073501708452256$ |
| $v_1$ | $0.0019618261238128635$ | $0.008915495782174165$ | $0.006953669658361301$ |
| $v_2$ | $0.0021066720511363083$ | $-0.007844023734345375$ | $0.009950695785481682$ |

**Reflection:**

This task shows us how the Runge-Kutta method is far more efficient than the forward Euler method. While it is true that the Runge-Kutta method must evaluate each derivative four times per timestep, the forward Euler method requires $10000 \div 200 = 50$ times more timesteps, thus making Runge-Kutta much faster to compute a solution of the same accuracy.

This observation is verified by the result of measuring the time of computation using the <i>time.time()</i> function and noting the significantly shorter time of computation taken by the Runge-Kutta method.

**Table 2: Comparison of the efficiency of Runge-Kutta and forward Euler methods**

| Method | Elapsed Time (s) |
| :---: | :---: |
| Runge-Kutta | $0.027045011520385742$ |
| Forward Euler | $0.14670372009277344$ |
{: style="width: 60%; margin: auto;"}

***

**Task 4:** Uses an $O(h^2)$ centered finite difference scheme on the $v_2$ data to compute the acceleration of the second floor $\ddot{x}_2$ for each forcing amplitude and classifies the building response due to the maximum acceleration.

**Results:**
<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/2026-two-story-building-model/tsbm-a2.png" alt="tsbm-a2" width="400" />
    <figcaption align="center"><b>Figure 6: Acceleration of the second floor for each forcing amplitude</b></figcaption>
  </p>
</figure>

**Table 3: Maximum acceleration of second floor**

| A (m/s$^2$) | $\ddot{x}_2$ (m/s$^2$) | Building response |
| :---: | :---: | :---:|
| Runge-Kutta | $0.027045011520385742$ | Weak Jolt |
| Forward Euler | $0.14670372009277344$ | Collapse |

The building response was classified using the following standards:

**Table 4: Building response**

| Maximum acceleration (m/s$^2$) | Building response |
| :---: | :---: |
| 0 to 4 m/s$^2$ | Weak Jolt |
| 4 to 8 m/s$^2$ | Strong Jolt |
| 8 to 12 m/s$^2$ | Fracture |
| 12 m/s$^2$ and above | Collapse |
{: style="width: 60%; margin: auto;"}

***

**Task 5:**
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

This project uses a passive two-story building model to model the effect of an earthquake on a structure, employing various numerical analysis tools learned this semester.

**Given:**

The governing equations of the TSBM:

$$m_2 \ddot{x}_2 + F_d + F_{sp} = -m_2 \ddot{x}_g$$

$$m_1 \ddot{x}_1 - F_d - F_{sp} = -m_1 \ddot{x}_g -c_f \dot{x}_1 -k_f x_1$$

<ul>
  <li>$\mathbf{x_1}$ & $\mathbf{x_2}$ = displacements of the first and second floors, respectively, as functions of time.
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

**Task 1:** Performs a polynomial least squares fit on the datasets <i>springforce.csv</i> ($F_{sp}$ as a function of $\Delta x$) and <i>dampingforce.csv</i> ($F_{d}$ as a function of $\Delta \dot{x}$). Plots the two curves and computes the coefficients $k_1$, $k_2$, $k_3$, $c_1$, and $c_2$.

**Task 2:** Converts the governing equations to a system of four 1st order ordinary differential equations and solves the system numerically with the 4th order Runge-Kutta method.

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


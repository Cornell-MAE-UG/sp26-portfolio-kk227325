---
layout: project
title: Dummy 2
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


<br>

| A | B |
| :--- | :--- |
| 1 | 2 |

<br>
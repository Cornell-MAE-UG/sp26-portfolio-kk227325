---
layout: project
title: Macadamia Nut Nut Cracker Design
description: Mechanism Analysis for ENGRD 2020
image: /assets/images/macadamia-problem.png
---

**Part 1**

**Find:** Optimal dimensions for a nutcracker design

**Given:**
![macadamia-drawing](/assets/images/macadamia-drawing.png)
<ul>
  <li><b>d</b> = diameter of a macadamia nut = <b>1 in</b></li>
  <li><b>F<sub>N</sub></b> = Force necessary to break a macadamia nut = <b>222 kgf</b></li>
  <li><b>P</b> = Maximum grip strength we can expect a human to apply = <b>20 kgf</b></li>
  Note: P was determined by using the average grip strength of elderly women in order to make the nutcracker accessible.
</ul>

![macadamia-fbd](/assets/images/macadamia-fbd.png)

**Plan:**
<ol type="1">
  <li>Draw a FBD of one arm</li>
  <li>ΣM<sub>A</sub>=0 to find ratio of a:b</li>
  <li>Use d to find optimal lengths a & b and stroke = 8 in to determine the handle curvature</li>
</ol>

**Solution:**

1) 

![macadamia-one-arm](/assets/images/macadamia-one-arm.png)

2) $\Sigma M_A = F_N \cdot a - P \cdot b = 0$

$\Rightarrow \frac{b}{a} = \frac{F_N}{P} = \frac{222 \text{ kgf}}{20 \text{ kgf}} = 11.1$

$\Rightarrow a : b = 1 : 11.1$

3) Since d = 1 in, we can let a = 1 in, which makes b = 11.1 in.

4) Arm length = $b \cdot \frac{\sqrt{a^2+(\frac{d}{2})^2}}{a} = 12.4 \text{ in}$

Result:
![macadamia-part1complete](/assets/images/macadamia-part1complete.png)

**Reflection:**
The slope of the arm will be 1:2, which is a reasonable angle to grip (as opposed to a 45° angle, for example). 
The nut will be relatively easy to crack even for elderly or others with a weaker grip strength since I used a conservative value for P.
The size of the nut cracker is a bit large (about 1 foot long), but it should reasonably fit in a kitchen drawer, 
and the ease to crack nuts thanks to the long lever arm makes it worth the extra length.

**Part 2**

**Find:** Optimal dimensions for a nutcracker design using a linear actuator.

**Given:** 

<ul>
  <li><b>d</b> = diameter of a macadamia nut = <b>1 in</b></li>
  <li><b>F<sub>N</sub></b> = Force necessary to break a macadamia nut = <b>222 kgf = 489 lbf</b></li>
  <li><b>P</b> = Force specifications of linear actuator = <b>56 lbf</b></li>
  <li><b>Stroke</b> of linear actuator = <b>8 in</b></li>
</ul>



2) $\Sigma M_A = F_N \cdot a - P \cdot b = 0$

$\Rightarrow \frac{b}{a} = \frac{F_N}{P} = \frac{489 \text{ lbs}}{56 \text{ lbs}} = 8.7$

$\Rightarrow a : b = 1 : 8.7$

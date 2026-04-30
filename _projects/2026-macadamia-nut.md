---
layout: project
title: Macadamia Nut Nut Cracker Design
description: Mechanism Analysis for ENGRD 2020
technologies: [GitHub Pages, Jekyll, MathJax, Markdown]
image: /assets/images/macadamia-problem.png
mathjax: true
---

**Part 1: Manual nutcracker**

**Find:** Optimal dimensions for a nutcracker design

**Given:**

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/macadamia-drawing.png" alt="macadamia-drawing" width="400" />
    <figcaption align="center"><b>Figure 1: Overall diagram of nut cracker.</b></figcaption>
  </p>
</figure>

<ul>
  <li><b>d</b> = diameter of a macadamia nut = <b>1 in</b></li>
  <li><b>F<sub>N</sub></b> = Force necessary to break a macadamia nut = <b>222 kgf</b></li>
  <li><b>P</b> = Maximum grip strength we can expect a human to apply = <b>20 kgf</b></li>
</ul>

Note: The force to break a macadamia nut was found from this source[^1], and P was determined by using the average grip strength of elderly women in order to make the nutcracker accessible[^2].

[^1]: Bailey, A. (2025, November 10). *How do you compare to the average grip strength?* Everyday Health. https://www.everydayhealth.com/workouts-activities/average-grip-strength-by-age-charts-how-do-you-compare/
[^2]: Schrauf, C., Huber, L., & Visalberghi, E. (2008). Do capuchin monkeys use weight to select hammer tools? *Anim Cogn* 11, 413–422. https://doi.org/10.1007/s10071-007-0131-2

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/macadamia-fbd.png" alt="macadamia-fbd" width="400" />
    <figcaption align="center"><b>Figure 2: Overall free body diagram nut cracker.</b></figcaption>
  </p>
</figure>

**Plan:**

<ol type="1">
  <li>Draw a free body diagram (FBD) of one arm</li>
  <li>ΣM<sub>A</sub>=0 to find ratio of a:b</li>
  <li>Use d to find optimal lengths a & b</li>
  <li>Calculate length of each arm</li>
</ol>

**Solution:**

1) 
<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/macadamia-one-arm.png" alt="macadamia-one-arm-fbd" width="300" />
    <figcaption align="center"><b>Figure 3: Free body diagram of one handle.</b></figcaption>
  </p>
</figure>

2)

$$\Sigma M_A = F_N \cdot a - P \cdot b = 0$$

$$\Rightarrow \frac{b}{a} = \frac{F_N}{P} = \frac{222 \text{ kgf}}{20 \text{ kgf}} = 11.1$$

$$\Rightarrow a : b = 1 : 11.1$$

3) Since d = 1 in, we can let a = 1 in, which makes b = 11.1 in.

4) Arm length = $b \cdot \frac{\sqrt{a^2+(\frac{d}{2})^2}}{a} = 12.4 \text{ in}$

Result:

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/macadamia-part1complete.png" alt="macadamia-part1complete" width="400" />
    <figcaption align="center"><b>Figure 4: Nut cracker design.</b></figcaption>
  </p>
</figure>

**Reflection:**
The size of the nut cracker is quite large (about 1 foot long). On top of that, the slope of the arm will be 1:2, which means that the arms would be $11.1 \text{ in} \cdot \frac{1}{2} \cdot 2 = 11.1 \text{ in}$ apart, which is impossible to grip with one hand. Although the nut will be relatively easy to crack even for elderly or others with a weaker grip strength in terms of the force, the large size of this tool makes its design impractical.

***

**Part 2: Nutcracker using a linear actuator**

**Find:** Optimal dimensions for a nutcracker design using a [linear actuator](https://www.progressiveautomations.com/products/pa-mc2?variant=43915326587060).

**Given:** 

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/macadamia-linear-actuator.png" alt="nut cracker with linear actuator" width="400" />
    <figcaption align="center"><b>Figure 5: Nut cracker with linear actuator</b></figcaption>
  </p>
</figure>

<ul>
  <li><b>d</b> = diameter of a macadamia nut = <b>1 in</b></li>
  <li><b>F<sub>N</sub></b> = Force necessary to break a macadamia nut = <b>222 kgf = 489 lbf</b></li>
  <li><b>P</b> = Force specifications of linear actuator = <b>56 lbf</b></li>
  <li>The <b>stroke</b> of linear actuator = <b>8 in</b></li>
</ul>

**Plan:**

<ol type="1">
  <li>Draw a FBD of one arm</li>
  <li>ΣM<sub>A</sub>=0 to find ratio of a:b</li>
  <li>Use d to find optimal lengths a & b and stroke = 8 in to determine the handle curvature</li>
</ol>

**Solution:**

1)

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/macadamia-one-arm.png" alt="macadamia-one-arm-fbd" width="300" />
    <figcaption align="center"><b>Figure 3: Free body diagram of one handle. (Reproduced from Figure 3)</b></figcaption>
  </p>
</figure>


2)

$$\Sigma M_A = F_N \cdot a - P \cdot b = 0$$

$$\Rightarrow \frac{b}{a} = \frac{F_N}{P} = \frac{489 \text{ lbs}}{56 \text{ lbs}} = 8.7$$

$$\Rightarrow a : b = 1 : 8.7$$

3) Just as before, we can let a = d = 1 in, which makes b = 8.7 in.

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/macadamia-part2complete-one-arm.png" alt="macadamia-part2-one-arm" width="400" />
    <figcaption align="center"><b>Figure 6: Complete diagram of one arm.</b></figcaption>
  </p>
</figure>

Result:

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/macadamia-part2complete.png" alt="macadamia-part2complete" width="400" />
    <figcaption align="center"><b>Figure 7: Nut cracker design with linear actuator.</b></figcaption>
  </p>
</figure>

**Reflection:**

Compared to the manual design, this design is significantly smaller (8.7" vs 11.1" long) and much more practical, though we do need to take into account the extra size of the linear actuator, which would stick out around 9.73" according to the [supplier website](https://www.progressiveautomations.com/products/pa-mc2?variant=43915326587060). Additionally, rather than having straight handles, we can curve the handles so that the linear actuator stroke is sufficient to fully close the nut cracker. The [linear actuator](https://www.progressiveautomations.com/products/pa-mc2?variant=43915326587060) used in this design costs $79.99, which is a relatively low-cost model among linear actuators.

***

**Part 3: Bending handles**

**Given:**

<ul>
  <li><b>F<sub>N</sub></b> = Force necessary to break a macadamia nut = <b>222 kgf = 489 lbf</b></li>
  <li><b>P</b> = Force specifications of linear actuator = <b>56 lbf</b></li>
</ul>

Now, we will treat the arms as beams that can undergo bending (rather than being rigid). We will use a modified version of the free body diagram drawn in part 2 which:
<ul>
  <li>assumes the handle to be a straight beam</li>
  <li>treats the pivot at point A as a pin and the point of contact with the macadamia nut as a roller</li>
  <li>considers only the components of each force transverse to the beam</li>
  <li>uses a new coordinate system with point A at the origin and the x-direction along the handle </li>
</ul>

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/macadamia-part3fbd.png" alt="macadamia-part3fbd" width="300" />
    <figcaption align="center"><b>Figure 8: New free body diagram of one arm.</b></figcaption>
  </p>
</figure>

**Find:** Location of maximum elastic deflection in the nutcracker handles.

**Plan:**

<ol type="1">
  <li>Evaluate the magnitudes of P' and F<sub>N</sub>', the components of P and F<sub>N</sub> transverse to the handle</li>
  <li>Draw FBDs for two slices: one through segment AB and one through segment BC</li>
  <li>ΣM<sub>slice</sub>=0 to find M(x) for each slice</li>
  <li>Solve for y(x) using the equation $EIy'' = M(x)$, boundary conditions derived from the supports, and continuity conditions at point B</li>
  <li>Solve y'(x)=0 and find the location of maximum deflection</li>
</ol>

**Solution:**

1) Using the angle θ as shown in the FBD:

$$\theta = \arctan{\frac{0.5 \text{ in}}{1 \text{ in}}} = 0.463 \text{ rad}$$

$$F_N' = F_N\cos{\theta} = 489  \text{ lbf} \cdot \cos{0.463} = 437 \text{ lbf}$$

$$P' = P\cos{\theta} = 56  \text{ lbf} \cdot \cos{0.463} = 50. \text{ lbf}$$

2)

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/macadamia-part3fbdslice.png" alt="macadamia-part3fbdslice" width="300" />
    <figcaption align="center"><b>Figure 9: Free body diagram of handle at slices through AB and BC.</b></figcaption>
  </p>
</figure>

Note: lengths were calculated using trigonometry and the value of angle θ from part 1:

$$AB = 1 \text{ in} \cdot \sec{\theta} = 1.12 \text{ in}$$

$$BC = (8.7-1) \text{ in} \cdot \sec{\theta} = 8.61 \text{ in}$$

$$AC = AB + BC = 1.12 \text{ in} + 8.61 \text{ in} = 9.73 \text{ in}$$

3) Using the FBD of the slice through AB:

$$ΣM_\text{slice} = -M(x) + F_N' \cdot (1.12 \text{ in} - x) - P' \cdot (9.73 \text{ in} - x) =0$$

$$\Rightarrow M(x) = F_N' \cdot (1.12 \text{ in} - x) - P' \cdot (9.73 \text{ in} - x) \text{  for  } 0 \text{ in} < x <1.12 \text{ in}$$

Next, using the FBD of the slice through BC:

$$ΣM_\text{slice} = -M(x) - P' \cdot (9.73 \text{ in} - x) = 0$$

$$\Rightarrow M(x) = - P' \cdot (9.73 \text{ in} - x) \text{  for  } 1.12 \text{ in} < x <9.73 \text{ in}$$

4) Using the equation $EIy'' = M(x)$, we have:

$$
EIy'' = \left\{
\begin{array}{ll}
      F_N' \cdot (1.12-x) - P' \cdot (9.73-x) & 0 \text{ in} < x < 1.12 \text{ in} \\
      -P' \cdot (9.73-x) & 1.12 \text{ in}< x < 9.73 \text{ in}
\end{array} 
\right.
$$

Then, we can integrate this equation twice to get:

$$
EIy' = \left\{
\begin{array}{ll}
      F_N' \cdot (1.12x-\frac{1}{2}x^2) - P' \cdot (9.73x-\frac{1}{2}x^2) + c_1 & 0 \text{ in} < x < 1.12 \text{ in} \\
      - P' \cdot (9.73x-\frac{1}{2}x^2) + c_2 & 1.12 \text{ in}< x < 9.73 \text{ in}
\end{array}
\right.
$$

$$
EIy = \left\{
\begin{array}{ll}
      F_N' \cdot (0.56x^2-\frac{1}{6}x^3) - P' \cdot (4.86x^2-\frac{1}{6}x^3) + c_1x + c_3 & 0 \text{ in} < x < 1.12 \text{ in} \\
      - P' \cdot (4.86x^2-\frac{1}{6}x^3) + c_2x + c_4 & 1.12 \text{ in}< x < 9.73 \text{ in}
\end{array}
\right.
$$

From the pinned support at point A and roller at point B, we can write the boundary conditions $y(x = 0) = 0$ and $y(x = 1.12 \text{ in})= 0$. From the continuity conditions at point B, we also have y(x = 1.12") and y'(x = 1.12") are equal for both pieces of the piecewise function.

* BC  $y(x = 0 \text{ in}) = 0$:

$$0 = 0 - 0 + 0 + c_3$$

$$\Rightarrow c_3 = 0$$

* BC  $y(x = 1.12 \text{ in}) = 0$:

$$0 = 437 \cdot (0.56 \cdot 1.12^2-\frac{1}{6} \cdot 1.12^3) - 50 \cdot (4.86 \cdot 1.12^2-\frac{1}{6} \cdot 1.12^3) + c_1 \cdot 1.12 + 0 \Rightarrow c_1 = 78.3$$

* "No kinks" condition  $y_L'(x = 1.12\text{ in}) = y_R'(x = 1.12\text{ in})$:

$$437 \cdot (1.12 \cdot 1.12-\frac{1}{2} \cdot 1.12^2) - 50 \cdot (9.73\cdot 1.12- \frac{1}{2}\cdot 1.12^2) + 78.3 = - 50 \cdot (9.73\cdot 1.12-\frac{1}{2} \cdot 1.12^2) + c_2$$

$$\Rightarrow c_2 = 351.4$$

* "No jumps"  condition $y_L(x = 1.12\text{ in}) = y_R(x = 1.12\text{ in})$:

$$0 = - 50 \cdot (4.86 \cdot 1.12^2-\frac{1}{6} \cdot 1.12^3) + 351.4 \cdot 1.12 + c_4$$

$$\Rightarrow c_4 = -101$$

So, we have:

$$
y(x) = \left\{
\begin{array}{ll}
      \frac{1}{EI} (F_N' \cdot (0.56x^2-\frac{1}{6}x^3) - P' \cdot (4.86x^2-\frac{1}{6}x^3) + 78.3x) & 0 < x < 1.12 \text{ in} \\
      \frac{1}{EI} (- P' \cdot (4.86x^2-\frac{1}{6}x^3) + 351.4x - 101) & 1.12 < x < 9.73 \text{ in}
\end{array}
\right.
$$

5) To find the value of x that maximizes y(x), we solve $yʻ(x)=0$:

$$
y'(x) = 0 = \left\{
\begin{array}{ll}
      \frac{1}{EI} \left[ F_N' \cdot (1.12x-\frac{1}{2}x^2) - P' \cdot (9.73x-\frac{1}{2}x^2) + 78.3 \right] & 0 < x < 1.12 \text{ in} \\
      \frac{1}{EI} \left[ - P' \cdot (9.73x-\frac{1}{2}x^2) + 351.4 \right] & 1.12 < x < 9.73 \text{ in}
\end{array}
\right.
$$

Solving, we find that the only solution in the range [0, 9.73] is $x = 0.64 \text{ in}$.

Plugging in the critical point x = 0.64" and endpoints x = 0" and x = 9.73" into the equation for y(x), we get:

**Table 1: Magnitude of deflection at critical points**

<table width="30%">
  <thead>
    <tr>
      <th align="center">x (in)</th>
      <th align="center">y(x) (in)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">0</td>
      <td align="center">0</td>
    </tr>
    <tr>
      <td align="center">0.64</td>
      <td align="center">$$\frac{33.9}{EI}$$</td>
    </tr>
    <tr>
      <td align="center">9.73</td>
      <td align="center">$$\frac{-12000}{EI}$$</td>
    </tr>
  </tbody>
</table>

The value of x that yields the largest magnitude of deflection is at x = <b>9.73 in</b>.

**Reflection**

It makes sense that the largest deflection of the handle occurs at the free end which is subjected to the downward applied force P. In fact, the sign and relative magnitudes from table 1 of the small positive (upward) deflection at x = 0.64" and the much larger negative (downward) deflection at x = 9.73" match my intuition of how the handle should bend, as shown in the image below.

<figure>
  <p align="center">
    <img src="{{ site.baseurl }}/assets/images/macadamia-part3-reflection.png" alt="macadamia-part3-reflection" width="300" />
    <figcaption align="center"><b>Figure 10: Free body diagram of handle at slices through AB and BC.</b></figcaption>
  </p>
</figure>

***

**Part 4: Handle design**

**Given:**


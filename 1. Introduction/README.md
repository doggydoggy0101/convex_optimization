## :book: Introduction

An optimization problem can be written as follows:

$$
\begin{align*}
\min_x\ &f_0(x)\\
\text{s.t.}\ &f_i(x)\leq0,\ i=1,\dots,m.
\end{align*}\tag{1.1}
$$

| Definition       | Notation                        |
|------------------|---------------------------------|
| variable         | $x\in\mathbb{R}^n$              |
| value            | $f_0(x)$                        |
| objective        | $f_0:\mathbb{R}^n\to\mathbb{R}$ |
| constraint       | $f_i:\mathbb{R}^n\to\mathbb{R}$ |

We say $x$ is feasible if $x$ satisfies all the constraints. We say $x^\*$ is an optimal solution if for all feasible $x$, we have $f_0(x^\*)\leq f_0(x)$. The corresponding value $f_0(x^\*)$ is called the optimal value.

An optimization problem is called a **linear program** if all functions $f_0,f_1,\dots,f_m$ are linear, otherwise it is called a **nonlinear program**.

> Originally, people think linear programs are the easy ones and nonlinear programs are the hard ones. It turns out that convex problems (which contains some nonlinear program) are the easy ones and nonconvex problems are the hard ones.


### Convex optimization
An optimization problem is convex if all functions $f_0,f_1,\dots,f_m$ are convex, i.e., for $0\leq\theta\leq1$,

$$
f(\theta x+ (1−\theta)y) ≤ \theta f(x) + (1−\theta)f(y). 
$$

We next introduce two widely known and used special subclasses of convex optimization: **least squares** and **linear programming**.

### Least squares
Least squares is an unconstrained optimization problem with an objective which is a sum of squares of residual terms of the form $a_i^\top x− b_i$

$$ 
\begin{align*}
\min_xf_0(x)=\\|Ax-b\\|\_2^2=\sum_{i=1}^k(a_i^\top x-b_i)^2. 
\end{align*}\tag{1.4}
$$


It is well-known that least squares has the closed-form solution

$$
x^*=(A^\top A)^{-1}A^\top b.
$$

There are some variations, for example, the weighted least squares

$$
\min_x\sum_{i=1}^kw_i(a_i^\top x-b_i)^2
$$

to adjust the weight of residuals. Another example is the regularized least squares

$$
\min_x\sum_{i=1}^k(a_i^\top x-b_i)^2 + \rho\\|x\\|^2_2
$$

to prefer solutions with smaller norms.

> Both weighted least squares and regularization are covered in Chapter 6; their statistical interpretations are given in Chapter 7.


### Linear programming
A linear program (LP) can be written as follows:

$$
\begin{align*}
\min_x\ &c^\top x\\
\text{s.t.}\ &a_i^\top x - b_i\leq0,\ i=1,\dots,m.
\end{align*}\tag{1.5}
$$

There are various eﬀective methods for LP, for example, Dantzig’s simplex method and interior-point method. Although LP is rare in real-world situations, one way of dealing with nonlinear problems is to relax/linearize the problem to a LP. 

> In general, reformulating/approximating a nonconvex problem to a convex program is one the most important skill in my opinion.

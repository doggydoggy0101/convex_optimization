## :book: Convex sets

**Table of Contents**
- [:book: Convex sets](#book-convex-sets)
  - [Affine sets](#affine-sets)
  - [Relative interior](#relative-interior)
  - [Convex sets](#convex-sets)


### Affine sets
Suppose $x_1\neq x_2$ are two points in $\mathbb{R}^n$,

$$
y=\theta x_1+(1-\theta)x_2
$$

is a line, and line segment if $0\leq\theta\leq1$.

A set $C\subseteq\mathbb{R}^n$ is affine if for any $x_1,x_2\in C$ and $\theta\in\mathbb{R}$,

$$
\theta x_1+(1-\theta)x_2\in C.
$$

Affine combination:

$$
x=\theta_1x_1+\dots+\theta_kx_k\ ;\ \ \theta_i\in\mathbb{R},\ \sum_{i=1}^k\theta_i=1.
$$

> Affine set contains every affine combination of its points.

- closed sets are not affine sets
- $\mathbb{R}^2$ is an affine set

> **Example 2.1** The solution set of a system of linear equations, i.e., $C=\\{x\mid Ax=b\\}$, is an affine set. Suppose $x_1,x_2\in C$, we have $Ax_1=b$ and $Ax_2=b$,
> 
> $$
> \begin{align*}
> A(\theta x_1+(1-\theta)x_2)&=\theta Ax_1+(1-\theta)Ax_2\\
> &=\theta b + (1-\theta)b\\
> &=b\in C.
> \end{align*}
> $$

Affine hull is the set of all affine combinations, denoted as $\mathbf{aff}\ C$:

$$
\mathbf{aff}\ C=\\{\theta_1x_1+\dots+\theta_kx_k\mid x_1,\dots,x_k\in C,\ \sum_{i=1}^k\theta_i=1\\}.
$$

> Affine hull is the smallest affine set that contains $C$.


### Relative interior
We often use the relative interior instead of the topology interior. Lets first look at an example.

> **Example 2.2** Consider a square in $(x_1,x_2)$-plane in $\mathbb{R}^3$
> 
> $$
> C=\\{x\in\mathbb{R}^3\mid -1\leq x_1\leq1,\ -1\leq x_2\leq1,\ x_3=0\\},
> $$
> 
> the interior of $C$ is empty.

This is weird since in common sense, the square should have nonempty interior. This is because the $x_3$ coordinate is fixed, thereby the $x_3$ plane is redundant in such case. We define the relative interior of the set $C$, denoted $\mathbf{relint}\ C$, as its interior relative to $\mathbf{aff}\ C$.

> **Example 2.2** (continue) The affine hull of $C$ is $\\{x\in\mathbb{R}^3\mid x_3=0\\}$ and the relative interior
> 
> $$
> \mathbf{relint}\ C=\\{x\in\mathbb{R}^3\mid -1 < x_1 < 1,\ -1 <x_2 <1,\ x_3=0\\}
> $$
> 
> is now nonempty.

<div align="center">
    <img src="docs/relint.png" width="480"/>
    <p><b>Fig. 1 </b>Relative interior.</p>
</div>

Using the relative interior allows us to ignore redundant dimensions.

### Convex sets
A set $C\subseteq\mathbb{R}^n$ is convex if for any $x_1,x_2\in C$ with $0\leq\theta\leq1$,

$$
\theta x_1+(1-\theta)x_2\in C.
$$

Convex combination:

$$
x=\theta_1x_1+\dots+\theta_kx_k\ ;\ \ 0\leq\theta_i\leq1,\ \sum_{i=1}^k\theta_i=1.
$$

> Convex set contains every convex combination of its points.

Convex hull is the set of all convex combinations, denoted as $\mathbf{conv}\ C$:

$$
\mathbf{conv}\ C=\\{\theta_1x_1+\dots+\theta_kx_k\mid x_1,\dots,x_k\in C,\ \sum_{i=1}^k\theta_i=1,\ \theta_i\geq0\\}.
$$

> Convex hull is the smallest convex set that contains $C$.




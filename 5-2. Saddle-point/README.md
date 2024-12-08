# :book: Saddle-point

**Table of Contents**
- [:book: Saddle-point](#book-saddle-point)
    - [Minimax inequality](#minimax-inequality)
    - [Saddle-point](#saddle-point)
    - [Minimax Theorem of von Nuemann](#minimax-theorem-of-von-nuemann)

In this section, we give another interpretation of Lagrange duality. Consider an optimization problem with not equality constraints (the results can be easily extended). Consider $\sup_\lambda\mathcal{L}(x,\lambda)$, we choose $\lambda=0$ if $x$ is feasible and choose $\lambda_i\to\infty$ if $x$ is not feasible such that $f_i(x)>0$. Thereby, we have

$$
\sup_{\lambda\succeq0}\mathcal{L}(x,\lambda)=\sup_{\lambda\succeq0}\left(f_0(x)+\sum_{i=1}^m\lambda_if_i(x)\right)=
\begin{cases}f_0(x)&f_i(x)\leq0,\ i=1,\dots,m, \\\\ \infty&\text{otherwise}.\end{cases}
$$

We can express the optimal value of the primal problem as 

$$
p^*=\inf_x\sup_{\lambda\succeq0}\mathcal{L}(x,\lambda).
$$

By the definition of dual function, we also have

$$
d^*=\sup_{\lambda\succeq0}\inf_x\mathcal{L}(x,\lambda).
$$

By weak duality, we have

$$
\begin{align*}
\sup_{\lambda\succeq0}\inf_x\mathcal{L}(x,\lambda)\leq\inf_x\sup_{\lambda\succeq0}\mathcal{L}(x,\lambda),
\end{align*}\tag{5.45}
$$

and equality holds if strong duality holds.

### Minimax inequality

In fact, inequality $(5.45)$ holds for any function $f:W\times Z\to\mathbb{R}$, which is also known as the minimax (max-min) inequality

$$
\begin{align*}
\sup_{z\in Z}\inf_{w\in W}f(w,z)\leq\inf_{w\in W}\sup_{z\in Z}f(w,z),
\end{align*}\tag{5.46}
$$

and similarly, equality holds if the minimax theorem (or saddle-point property) holds. To prove the minimax inequality, we first use the relationship

$$
\inf_{w\in W}f(w,z)\leq f(w,z)\leq\sup_{z\in Z} f(w,z).
$$

Since $\sup_z f(w,z)$ is an upper bound of $\inf_wf(w,z)$ for any $w$ and supremum is the least upper bound,

$$
\sup_{z\in Z}\inf_{w\in W}f(w,z)\leq\sup_{z\in Z} f(w,z).
$$

Since $\sup_z\inf_wf(w,z)$ is a lower bound of $\sup_zf(w,z)$ and infimum is the greatest lower bound,

$$
\sup_{z\in Z}\inf_{w\in W}f(w,z)\leq\inf_{w\in W}\sup_{z\in Z}f(w,z).
$$

### Saddle-point

A pair $(\tilde{w},\tilde{z})$ is a saddle-point if $f(\tilde{w},z)\leq f(w,z)\leq f(w,\tilde{z})$ for all $w\in W$ and $z\in Z$.

### Minimax Theorem of von Nuemann

Let $W$ and $Z$ be convex compact sets. If $f:W\times Z\to\mathbb{R}$ is a continuous convex-concave function, then we have

$$
\max_{z\in Z}\min_{w\in W}f(w,z)=\min_{w\in W}\max_{z\in Z}f(w,z).
$$

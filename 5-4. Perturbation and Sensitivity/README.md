# :book: Perturbation

- [:book: Perturbation](#book-perturbation)
    - [Perturbed problem](#perturbed-problem)
    - [Global inequality and sensitivity](#global-inequality-and-sensitivity)
    - [Local sensitivity](#local-sensitivity)

### Perturbed problem

Consider the following perturbed problem of Problem $(5.1)$

$$
\begin{align*}
\min_{x\in\mathbb{R}^n}\ &f_0(x)\\
\text{s.t.}\  &f_i(x)\leq u_i,\ i=1,\dots,m\\
&h_i(x)=v_i,\ i=1,\dots,p
\end{align*}\tag{5.56}
$$

- $u_i>0$ means that we relaxed the $i$th inequality constraint
- $u_i<0$ means that we tightened the $i$th inequality constraint

We define $p^*(u,v)$ as the optimal value of the perturbed problem.

- $p^*(0,0)=p^*$
- if the original problem is convex, then $p^*:\mathbb{R}^m\times\mathbb{R}^p\to\mathbb{R}$ is also convex

### Global inequality and sensitivity

Now we assume that strong duality holds, where $x^*$ is the optimal solution of the primal problem and $(\lambda^*,\nu^*)$ is the optimal solution of the dual problem. Then for all $u$ and $v$, we have

$$
\begin{align*}
p^*(u,v)\geq p^*(0,0)-\lambda^{*\top}u-\nu^{*\top}v.
\end{align*}\tag{5.57}
$$

The inequality $(5.57)$ gives a lower bound on the perturbed optimal value. To prove the inequality $(5.57)$, suppose $x$ is a feasible solution, by strong duality, 

$$
\begin{align*}
p^*(0,0)=p^*=d^*=g(\lambda^*,\nu^*)
&\leq f_0(x)+\sum_{i=1}^m\lambda^*_if_i(x)+\sum_{i=1}^p\nu^*_ih_i(x)\\
&\leq f_0(x)+\lambda^{*T}u+\nu^{*T}v.
\end{align*}
$$

**Sensitivity** 
When strong duality holds, we have some conclusions:

- if $\lambda^*_i$ is large and $u_i<0$, then $p^*(u,v)$ is guaranteed to increase greatly
- if $\nu^*_i>0$ is large and $v_i<0$ (or if $\nu^*_i<0$ is large and and $v_i>0$), then $p^*(u,v)$ is guaranteed to increase greatly
- if $\lambda^*_i$ is small and $u_i>0$, then $p^*(u,v)$ will not decrease too much
- if $\nu^*_i>0$ is small and $v_i>0$ (or if $\nu^*_i<0$ is small and $v_i<0$), then $p^*(u,v)$ will not decrease too much

### Local sensitivity

Suppose that $p^*(u,v)$ is differentiable at $(u,v)=(0,0)$ and strong duality holds,

$$
\begin{align*}
\lambda^*_i=-\frac{\partial p^*(0,0)}{\partial u_i}\ ;\ \  \nu^*_i=-\frac{\partial p^*(0,0)}{\partial v_i}.
\end{align*}\tag{5.58}
$$

- if $u_i>0$ is sufficient small, then $p^*$ decreases $\lambda^*_iu_i$
- if $u_i<0$ is sufficient small, then $p^*$ increases $-\lambda^*_iu_i$

To prove $(5.58)$, let $u=te_i$ and $v=0$, where $e_i$ is the $i$th unit vector, we have

$$
\begin{align*}
\lim_{t\to0}\frac{p^*(te_i,0)-p^*}{t}=\frac{\partial p^*(0,0)}{\partial u_i}.
\end{align*}\tag{5.58.1}
$$

By inequaltiy $(5.57)$, if $t>0$, 

$$
p^*(te_i,0)\geq p^*-\lambda^{*\top}(te_i)-\nu^{*\top}0
\implies
\frac{p^*(te_i,0)-p^*(0, 0)}{t}\geq-\lambda^{*\top}e_i=\lambda^*_i.
$$

Substitute it back to $(5.58.1)$,

$$
\frac{\partial p^*(0,0)}{\partial u_i}=\lim_{t\to0}\frac{p^*(te_i,0)-p^*(0,0)}{t}=-\lambda_i^*.
$$

The case of $t<0$ is similar. The same method can be used to establish

$$
\frac{\partial p^*(0,0)}{\partial v_i}=-\nu^*_i.
$$

**Sensitivity**

- If $f_i$ is non-binding, i.e., $f_i(x^\*)<0$, then it can be tightened or loosened a sufficient small amount without aﬀecting the optimal value since the associated Lagrange multiplier $\lambda_i^\*=0$.
- If $f_i$ is binding, i.e., $f_i(x^\*)=0$, then then it can be tightened or loosened a sufficient small amount without aﬀecting the optimal value if $\lambda_i^\*$ is small, but affects the optimal value largely if $\lambda_i^\*$ is large.

Consider a convex problem with no equality constraints, with Slater’s condition holds.

$$
\begin{align*}
\min_x\ &f_0(x)\\
\text{s.t.}\  &f_i(x)\leq 0,\ i=1,\dots,m
\end{align*}
$$

where $x$ is some firm variable (i.e., determines how a firm works), $-f_0$ is the profit (i.e., we try to maximize the profit), and each $f_i\leq0$ represents a limit on some resource. The (negative) perturbed optimal $-p^\*(u)$ tells us the change of profit if any limit on resource is changed. By equality $(5.58)$, each $\lambda_i^\*$ tells us approximately how much more profit the firm could make for a sufficient small increase in availability of resource $i$. It follows that it is nature for $\lambda^\*_i$ to be the price of resource $i$.


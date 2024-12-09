# :book: Optimal conditions

**Table of Contents**
- [:book: Optimal conditions](#book-optimal-conditions)
    - [Suboptimal](#suboptimal)
    - [Complementary slackness](#complementary-slackness)
  - [Fritz-John conditions](#fritz-john-conditions)
    - [Fritz-John necessary conditions with binding constraints](#fritz-john-necessary-conditions-with-binding-constraints)
    - [Fritz-John necessary conditions](#fritz-john-necessary-conditions)
    - [Fritz-John sufficient conditions](#fritz-john-sufficient-conditions)
  - [Karush-Kuhn-Tucker conditions](#karush-kuhn-tucker-conditions)
    - [Karush-Kuhn-Tucker necessary conditions with binding constraints](#karush-kuhn-tucker-necessary-conditions-with-binding-constraints)
    - [Karush-Kuhn-Tucker necessary conditions](#karush-kuhn-tucker-necessary-conditions)
    - [Karush-Kuhn-Tucker sufficient conditions](#karush-kuhn-tucker-sufficient-conditions)
  - [Constraint qualifications](#constraint-qualifications)


We consider the general optimization problem $(5.1)$, and we do not assume the it is convex.

### Suboptimal
Since $g(\lambda,\nu)\leq p^\*$, we have the inequality for duality gap

$$
f_0(x)-p^\*\leq f_0(x)-g(\lambda,\nu).
$$

We say a solution $x$ is $\epsilon$-suboptimal if $f_0(x)-p^\*\leq\epsilon$. Thereby, it is straightforward to set $\epsilon=f_0(x)-g(\lambda,\nu)$, then we can develop a stopping criteria. Suppose an algorithm produces a sequence of primal dual solutions $x^k$ and $(\lambda^k, \nu^k)$ and $\epsilon$ is given, the stopping criteria

$$
f_0(x^k)-g(\lambda^k,\nu^k)\leq\epsilon
$$

guarantees $f_0(x^k)-p^\*\leq\epsilon$, i.e., $x^k$ is $\epsilon$-suboptimal.


### Complementary slackness
Suppose that strong duality holds, 

$$
f_0(x^\*)=g(\lambda^\*,\nu^\*)\leq f_0(x^\*)+\underbrace{\sum_{i=1}^m\lambda_i^\*f_i(x^\*)}_{\leq0}+\underbrace{\sum_{i=1}^p\nu_i^\*h_i(x^\*)}_{=0} \leq f_0(x^\*),
$$

which implies the complementary slackness

$$
\begin{align*}
\lambda_i^\*f_i(x^\*)=0,\ i=1,\dots,m.
\end{align*}\tag{5.48}
$$

Another result is that $\lambda_i^\*$ is zero if the $i$-th inequality constraint is not binding/active (as well as the other way).

- $\lambda_i^\*>0\implies f_i(x^\*)=0$
- $f_i(x^\*)<0\implies\lambda_i^\*=0$


## Fritz-John conditions

In Boyd's Convex Optimization, he assumes that $f_i,h_i$ are all differentiable and Slater's condition holds to derive the Karush-Kuhn-Tucker (KKT) conditions. However, there are other optimal conditions that does not require such strong assumptions. Therefore, we start by the Fritz-John (FJ) conditions.

### Fritz-John necessary conditions with binding constraints

**assumptions**
- objective, binding inequality constraints, equality constraints are differentiable
- nonbinding constraints are continuous

Let $x$ be a feasible solution and $I=\{i\mid f_i(x)=0\}$ be the set of binding constraints. Suppose that $f_0,\ f_i,i\in I,\ h_i,i=1,\dots,p$ are differentiable at $x$, and $f_i,i\not\in I$ are continuous at $x$. If $x$ is a local solution, then there exists $\lambda_0,\ \lambda_i,i\in I,\ \nu_i,i=1,\dots,p$ (Lagrange multipliers) such that

- first-order condition: $\lambda_0\nabla f_0(x)+\sum_{i\in I}\lambda_i\nabla f_i(x)+\sum_{i=1}^p\nu_i\nabla h_i(x)=0$
- primal feasibility: $f_i(x)\leq0,\ i=1,\dots,m$
- dual feasibility: $\lambda_0,\lambda_i\geq0,\ i\in I$
- Lagrange multipliers are not all zero: $(\lambda_0,\lambda,\nu)\neq 0$


### Fritz-John necessary conditions

**assumptions**
- objective, inequality constraints, equality constraints are differentiable

Let $x$ be a feasible solution. Suppose that $f_0,\ f_i,i=1,\dots,m,\ h_i,i=1,\dots,p$ are differentiable at $x$. If $x$ is a local solution, then there exists $\lambda_0,\ \lambda_i,i\in I,\ \nu_i,i=1,\dots,p$ (Lagrange multipliers) such that

- first-order condition: $\lambda_0\nabla f_0(x)+\sum_{i\in I}\lambda_i\nabla f_i(x)+\sum_{i=1}^p\nu_i\nabla h_i(x)=0$
- complementary slackness: $\lambda_if_i(x)=0,\ i=1,\dots,m$
- primal feasibility: $f_i(x)\leq0,\ i=1,\dots,m$
- dual feasibility: $\lambda_0,\lambda_i\geq0,\ i\in I$
- Lagrange multipliers are not all zero: $(\lambda_0,\lambda,\nu)\neq 0$
  

### Fritz-John sufficient conditions

**assumptions**
- equality constraints are affine
- gradient of equality constraints are linear independent
- objective is pseudoconvex
- inequality constraints are strictly pseudoconvex

Suppose that $x$ is a FJ point, $h_i$ are affine, $\nabla h_i$ are linear independent, and let $I=\{i\mid f_i(x)=0\}$ be the set of binding constraints. If there exists some neighborhood $N_\varepsilon(x)$ such that $f_0$ is pseudoconvex over $N_\varepsilon(x)$ and $f_i,i\in I$ are strictly pseudoconvex over $N_\varepsilon(x)$, then $x$ is a local solution.


## Karush-Kuhn-Tucker conditions
The main difference between the FJ conditions and the KKT conditions is that the Lagrange multiplier of the objective $\lambda_0$ cannot be zero, i.e., $\lambda_0>0$. We can derive the KKT conditions from the FJ conditions if some constraint qualification holds (we will talk about the constraint qualifications later).

### Karush-Kuhn-Tucker necessary conditions with binding constraints

**assumptions**

- objective, binding inequality constraints, equality constraints are differentiable
- nonbinding constraints are continuous
- constraint qualification

Let $x$ be a feasible solution and $I=\{i\mid f_i(x)=0\}$ be the set of binding constraints. Suppose that $f_0,\ f_i,i\in I,\ h_i,i=1,\dots,p$ are differentiable at $x$, and $f_i,i\not\in I$ are continuous at $x$. Suppose some constraint qualification holds, e.g., $\nabla f_i,i\in I$ and $\nabla h_i,i=1,\dots,p$ are linear independent. If $x$ is a local solution, then there exists **unique** $\lambda_i,i\in I,\ \nu_i,i=1,\dots,p$ (Lagrange multipliers) such that

- first-order condition: $\nabla f_0(x)+\sum_{i\in I}\lambda_i\nabla f_i(x)+\sum_{i=1}^p\nu_i\nabla h_i(x)=0$
- primal feasibility: $f_i(x)\leq0,\ i=1,\dots,m$
- dual feasibility: $\lambda_0,\lambda_i\geq0,\ i\in I$

### Karush-Kuhn-Tucker necessary conditions

**assumptions**
- objective, inequality constraints, equality constraints are differentiable
- constraint qualification

Let $x$ be a feasible solution. Suppose that $f_0,\ f_i,i=1,\dots,m,\ h_i,i=1,\dots,p$ are differentiable at $x$. Suppose some constraint qualification holds, e.g., $\nabla f_i,i\in I$ and $\nabla h_i,i=1,\dots,p$ are linear independent. If $x$ is a local solution, then there exists $\lambda_0,\ \lambda_i,i\in I,\ \nu_i,i=1,\dots,p$ (Lagrange multipliers) such that

- first-order condition: $\nabla f_0(x)+\sum_{i\in I}\lambda_i\nabla f_i(x)+\sum_{i=1}^p\nu_i\nabla h_i(x)=0$
- complementary slackness: $\lambda_if_i(x)=0,\ i=1,\dots,m$
- primal feasibility: $f_i(x)\leq0,\ i=1,\dots,m$
- dual feasibility: $\lambda_0,\lambda_i\geq0,\ i\in I$
  

### Karush-Kuhn-Tucker sufficient conditions

**assumptions**
- objective is pseudoconvex
- inequality constraints are quasiconvex
- equality constraints are quasiconvex/quasiconcave

Suppose that $x$ is a KKT point, and let $I=\{i\mid f_i(x)=0\}$ be the set of binding constraints. If $f_0$ is pseudoconvex, $f_i,i\in I$ are quasiconvex, and $h_i$ is quasiconvex if $\nu_i>0$ and quasiconcave if $\nu_i<0$, then $x$ is a global solution.

> For convex optimization problems, the KKT conditions are sufficient.

## Constraint qualifications

There are actually various constraint qualifications (regularity conditions). The most common would be the Linear independence constraint qualification.

**Linear independence constraint qualification**
The gradients of the binding constraints and the gradients of the equality constraints are linearly independent.

Boyd's *Convex Optimization* simply uses the Slater's condition, that is, one can replace the linear independence constraint qualification in the KKT conditions by Slater's condition. Please refer to Bazaraa's *Nonlinear programming* for more information.

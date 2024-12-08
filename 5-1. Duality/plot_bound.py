import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt


def obj_fn(x):
    return x**3 + 2 * x**2 - x + 1


# example of solving with CVXPY
var_x = cp.Variable(1)
constraints = [var_x >= -1, var_x <= 1]
prob = cp.Problem(cp.Minimize(obj_fn(var_x)), constraints)
prob.solve()
opt_val = prob.value

# plot objective function
fig, ax = plt.subplots(1, 1)
xx = np.linspace(-1.5, 1.5)
ax.plot(xx, obj_fn(xx), color="#d5d8dc")
xx = np.linspace(-1, 1)
ax.plot(xx, obj_fn(xx), color="#2980b9", label="objective function")
ax.hlines(opt_val, -1, 1, linestyles="--", colors="#e74c3c", label="optimal value")
ax.set_xlabel("$x$")
ax.set_ylabel("$f_0(x)$")
ax.legend(loc="upper left")
fig.tight_layout()
fig.savefig("docs/lower_bound.png")


def Lagrangian(x, l):
    return obj_fn(x) + l * (x**2 - 1)


def dual_fn(l):
    var_x = cp.Variable(1)
    prob = cp.Problem(cp.Minimize(Lagrangian(var_x, l)))
    prob.solve()
    return prob.value


# plot dual function
fig, ax = plt.subplots(1, 1)
ll = np.linspace(0, 100)
ax.plot(ll, np.array([dual_fn(l) for l in ll]), color="#2980b9", label="dual function")
ax.hlines(opt_val, 0, 100, linestyles="--", colors="#e74c3c", label="optimal value")
ax.set_xlabel("$\lambda$")
ax.set_ylabel("$g(\lambda)$")
ax.legend(loc="lower left")
fig.tight_layout()
fig.savefig("docs/upper_bound.png")

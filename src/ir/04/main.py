import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 20, 201)  # [0, 0.1, ..., 20]


def integrate_euler(f, x0, t):
    """Euler's method: x_{i+1} = x_i + dt * f(t_i, x_i)"""
    x = np.zeros((np.size(x0), t.size))
    x[:, 0] = x0
    for i in range(t.size - 1):
        x[:, i + 1] = x[:, i] + (t[i + 1] - t[i]) * f(t[i], x[:, i])
    return x


# Task-1: x' = -1/T x + 1/T, x(0) = 0, T = 2
# a) x_{i+1} = x_i + dt/T (1 - x_i) = 0.95 x_i + 0.05
T = 2


def f1(t, x):
    return -x / T + 1 / T


x = integrate_euler(f1, [0], t)[0]
assert np.allclose(x[1:4], [0.05, 0.0975, 0.142625])
print("x_1..x_3 =", x[1:4])

plt.figure()
plt.plot(t, x, label="Euler")
plt.plot(t, 1 - np.exp(-t / T), "--", label="exact $1 - e^{-t/T}$")
plt.xlabel("$t$ [s]")
plt.ylabel("$x(t)$")
plt.grid(True)
plt.legend()

# Task-2: differential drive robot
r = 0.05  # wheel radius [m]
b = 0.2  # track width [m]


def d_diffdrive(pose, spd_left, spd_right):
    x, y, psi = pose
    v = r / 2 * (spd_right + spd_left)
    omega = r / b * (spd_right - spd_left)
    return np.array([v * np.cos(psi), v * np.sin(psi), omega])


def f2(t, pose):
    # straight for 5 s, then right wheel faster: left turn
    spd_left = 10.0
    spd_right = 10.0 if t < 5 else 12.0
    return d_diffdrive(pose, spd_left, spd_right)


pose = integrate_euler(f2, [0, 0, 0], t)

plt.figure()
plt.plot(pose[0], pose[1])
plt.xlabel("$x$ [m]")
plt.ylabel("$y$ [m]")
plt.axis("equal")
plt.grid(True)

plt.figure()
for state, label in zip(pose, ["$x$ [m]", "$y$ [m]", r"$\psi$ [rad]"]):
    plt.plot(t, state, label=label)
plt.xlabel("$t$ [s]")
plt.grid(True)
plt.legend()

plt.show()

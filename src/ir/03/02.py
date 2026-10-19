import matplotlib.pyplot as plt
import numpy as np

# Camera frame {S} rotated by theta around z and shifted by d_BS relative to {B}
theta = np.pi / 4
v_S = np.array([2, 3])
d_BS = np.array([5, 1])
R_BS = np.array(
    [
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)],
    ]
)

# a) v^B = R_BS v^S + d^BS
v_B = R_BS @ v_S + d_BS
print("v^B =", v_B)
assert np.allclose(v_B, [5 - np.sqrt(2) / 2, 1 + 5 * np.sqrt(2) / 2])

# b) Plot point and both frames
fig, ax = plt.subplots()
for origin, R, color, name in [
    (np.zeros(2), np.eye(2), "k", "B"),
    (d_BS, R_BS, "b", "S"),
]:
    ax.quiver(*origin, *R[:, 0], color=color, angles="xy", scale_units="xy", scale=1)
    ax.quiver(*origin, *R[:, 1], color=color, angles="xy", scale_units="xy", scale=1)
    ax.annotate(f"{{{name}}}", origin, textcoords="offset points", xytext=(-15, -15))
    ax.annotate(f"$x_{name}$", origin + R[:, 0], color=color)
    ax.annotate(f"$y_{name}$", origin + R[:, 1], color=color)

ax.plot([d_BS[0], v_B[0]], [d_BS[1], v_B[1]], "b--", label="$v^S$ (in {S})")
ax.plot(*v_B, "ro", label=f"$v^B$ = ({v_B[0]:.2f}, {v_B[1]:.2f})")
ax.set_xlim(-1, 7)
ax.set_ylim(-1, 6)
ax.set_aspect("equal")
ax.grid(True)
ax.set_xlabel("$x_B$")
ax.set_ylabel("$y_B$")
ax.legend()
plt.show()

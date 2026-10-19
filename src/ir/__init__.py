import matplotlib.pyplot as plt
import numpy as np

# v = [1, 2, 3]
vector = np.array([1, 2, 3])
# Rotate 45° around the y-axis
theta = np.radians(45)
rotation_matrix = np.array(
    [
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)],
    ]
)
rotated_vector = rotation_matrix @ vector

print("Original vector:\n", vector)
print("Rotated vector:\n", rotated_vector)

# Plot vector
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.quiver(
    0, 0, 0, vector[0], vector[1], vector[2], color="b", label="Original Vector"
)
ax.quiver(
    0,
    0,
    0,
    rotated_vector[0],
    rotated_vector[1],
    rotated_vector[2],
    color="r",
    label="Rotated Vector",
)
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()
plt.show()

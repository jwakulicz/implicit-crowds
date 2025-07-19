import matplotlib.pyplot as plt
import numpy as np

def generate_random_obstacles(num_obstacles, bndry_x, bndry_y):
    obstacle_xs = np.random.uniform(bndry_x[0]+2, bndry_x[1]-2, num_obstacles)
    obstacle_ys = np.random.uniform(bndry_y[0]+6, bndry_y[1]-6, num_obstacles)
    obstacle_centres = np.vstack((obstacle_xs, obstacle_ys)).T
    return obstacle_centres

bndry_x = [-10,10]
bndry_y = [-10, 10]

num_obstacles = 8

locs = generate_random_obstacles(num_obstacles, bndry_x, bndry_y)
print(locs)

plt.scatter(locs[:,0], locs[:,1])
plt.show()
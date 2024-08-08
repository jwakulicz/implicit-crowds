import numpy as np
import csv
import random

def generate_locations(x_bounds, y_bounds, num_locations, start=False):
    num_locations = int(num_locations)
    x_vals = np.random.uniform(x_bounds[0], x_bounds[1], num_locations)
    if start:
        y_vals = np.linspace(y_bounds[0], y_bounds[1], num_locations)
    else:
        y_vals = np.random.uniform(y_bounds[0], y_bounds[1], num_locations)
    locations = list(zip(x_vals, y_vals))
    return locations

def generate_obstacle_grid(num_obstacles, bndry_x, bndry_y):
    """num_obstacles needs to be a square number, want to always make a square grid"""
    n = int(np.sqrt(num_obstacles))
    x = np.linspace(bndry_x[0] / 3, bndry_x[1] / 3, n)
    y = np.linspace(bndry_y[0] / 3, bndry_y[1] / 3, n)

    x_grid, y_grid = np.meshgrid(x,y)

    obstacle_centres = np.vstack([x_grid.ravel(), y_grid.ravel()]).T

    return obstacle_centres

def define_agent_row(id, start, goal, goal_vel, radius):
    return [int(id), start[0], start[1], goal[0], goal[1], goal_vel, radius]

def define_obstacle_row(id, location, x_width, y_width):
    return [int(id), location[0], location[1], x_width, y_width]

if __name__ == '__main__':
    bndry_x = [-10,10]
    bndry_y = [-10, 10]

    num_agents = 16
    agent_starts = generate_locations([bndry_x[0],bndry_x[0]], [bndry_y[0]/2, bndry_y[1]/2], num_agents, start=True)
    random.shuffle(agent_starts)
    agent_ends_bottom = generate_locations([bndry_x[1],bndry_x[1]], [-6,-4], num_agents / 2)
    agent_ends_top = generate_locations([bndry_x[1],bndry_x[1]], [4,6], num_agents / 2)
    agent_ends = np.vstack((agent_ends_bottom, agent_ends_top))
    goal_vel = 1.0
    radius = 0.25

    num_obstacles = 9
    obstacle_locs = generate_obstacle_grid(num_obstacles, bndry_x, bndry_y)
    obs_x_width = 1
    obs_y_width = 1

    scenario_filename = '../../data/exits.csv'

    with open(scenario_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=' ')
        csvwriter.writerow(bndry_x)
        csvwriter.writerow(bndry_y)
        csvwriter.writerow([num_agents])
        for id in range(num_agents):
            row = define_agent_row(id, agent_starts[id], agent_ends[id], goal_vel, radius)
            csvwriter.writerow(row)
        csvwriter.writerow([num_obstacles])
        for id in range(num_obstacles):
            row = define_obstacle_row(id, obstacle_locs[id], obs_x_width, obs_y_width)
            csvwriter.writerow(row)

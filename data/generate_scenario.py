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
    x = np.linspace(bndry_x[0] / 2, bndry_x[1] / 2, n)
    y = np.linspace(bndry_y[0] / 2, bndry_y[1] / 2, n)

    x_grid, y_grid = np.meshgrid(x,y)

    obstacle_centres = np.vstack([x_grid.ravel(), y_grid.ravel()]).T

    return obstacle_centres

def generate_random_obstacles(num_obstacles, bndry_x, bndry_y):
    obstacle_xs = np.random.uniform(bndry_x[0]/2, bndry_x[1]/2, num_obstacles)
    obstacle_ys = np.random.uniform(bndry_y[0]/2, bndry_y[1]/2, num_obstacles)
    obstacle_centres = np.vstack((obstacle_xs, obstacle_ys)).T
    return obstacle_centres

def define_agent_row(id, start, goal, goal_vel, radius):
    return [int(id), start[0], start[1], goal[0], goal[1], goal_vel, radius]

def define_obstacle_row(id, location, x_width, y_width):
    return [int(id), location[0], location[1], x_width, y_width]

if __name__ == '__main__':
    bndry_x = [-10,10]
    bndry_y = [-10, 10]

    num_agents = 10
    agent_starts = generate_locations([bndry_x[0],bndry_x[0]], [bndry_y[0]+4, bndry_y[1]-4], num_agents, start=True)
    random.shuffle(agent_starts)
    agent_ends_bottom = generate_locations([bndry_x[1],bndry_x[1]], [bndry_y[0]+2,bndry_y[1]-2], num_agents / 2)
    agent_ends_top = generate_locations([bndry_x[1],bndry_x[1]], [bndry_y[0]+2,bndry_y[1]-2], num_agents / 2)
    agent_ends = np.vstack((agent_ends_bottom, agent_ends_top))
    # agent_starts = generate_locations([bndry_x[0], bndry_x[0]], [-1,1], num_agents)
    # agent_ends = generate_locations([bndry_x[1],bndry_x[1]], [-1,1], num_agents)
    goal_vel = 1.0
    radius = 0.05

    num_obstacles = 8
    # obstacle_locs = generate_obstacle_grid(num_obstacles, bndry_x, bndry_y)
    # obstacle_locs = generate_random_obstacles(num_obstacles, bndry_x, bndry_y)
    #--------- 9 ----------
    # obstacle_locs = [[ 4.25059769,  4.20199507],
    #                  [ 0.13074282,  0.38856129],
    #                  [-0.47377547,  5.68734952],
    #                  [ 6.74957198, -3.94297074],
    #                  [ 2.69676101,  1.44101561],
    #                  [-1.02467093, -3.97677974],
    #                  [-3.49739704, -5.55176822],
    #                  [-5.64761841,  1.29330791],
    #                  [ 3.71063279, -2.29824409]]
    #--------- 4 ----------
    # obstacle_locs = [[-4.54623763,  3.83850972],
    #                  [ 4.97537701,  1.36902887],
    #                  [-3.03406407, -3.5190396 ],
    #                  [-7.7097851,   1.13391335]]
    #--------- 5 ----------
    # obstacle_locs = [[ 1.35371877, -0.40255983],
    #                  [-5.81546693, -2.67146699],
    #                  [-6.17829133, 0.10486785],
    #                  [-1.73841878,  1.94701256],
    #                  [-1.92330944, -3.01958843]]
    # #--------- 6 ----------
    # obstacle_locs = [[-6.65110228,  1.94026892],
    #                  [ 4.36413148, -2.66637412],
    #                  [ 7.12075023,  2.11151005],
    #                  [ 0.23613212, -3.58911161],
    #                  [ 1.89071302, -0.1953745 ],
    #                  [ 1.13035222,  2.731242583]]
    #---------- 7 ------------
    # obstacle_locs = [[-3.84607685,  3.28888902],
    #                  [ 7.0439967 , -2.0873557 ],
    #                  [ 4.38215456, -3.61854813],
    #                  [ 0.64268297,  0.79459384],
    #                  [ 4.84428061,  1.63406079],
    #                  [-4.323133  , -0.41255922],
    #                  [ 0.52425629, -3.47150785]]
    # #---------- 8 ------------
    obstacle_locs = [[ 1.10760067,  3.40201862],
                     [-5.08024045, -1.68375874],
                     [-2.15377046, -0.84474798],
                     [-1.56098768,  3.72951311],
                     [ 5.34560801,  1.78861845],
                     [-2.88672845, -3.60995306],
                     [ 0.90374774, -0.06145983],
                     [-7.53379075,  0.62215894]]
    # num_obstacles = 3
    # obstacle_locs = [[-3,1],[3,1],[0,-3]]
    obs_x_width = 0.5
    obs_y_width = 0.5

    # scenario_filename = '../../data/exits.csv'
    # scenario_filename = '../../data/threeObsExits.csv'
    scenario_filename = '../../data/randEightObsExits.csv'
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

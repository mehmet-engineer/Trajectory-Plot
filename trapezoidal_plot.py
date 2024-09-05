import numpy as np
import matplotlib.pyplot as plt


def trapezoidal_function(t, total_time, acc_decc_phase, v_max):
    """
    It is position - time function. It creates trapezoidal velocity profile by using total_time and v_max data based position calculation. 
    Starting position is 0 and end position is automatically calculated.
    Returns a Position at time t.
    """
    
    acc_time = total_time * acc_decc_phase
    acc = v_max / acc_time
    const_vel_time = total_time - 2 * acc_time
    
    # acceleration phase
    if t < acc_time:
        x = 0.5 * acc * t**2

    # constant velocity phase
    elif t < total_time - acc_time:
        x = (0.5 * acc * acc_time**2) + v_max * (t - acc_time)
    
    # deceleration phase
    else:
        t_last = t - acc_time - const_vel_time
        h = acc * (total_time - t)
        last_curve = (v_max + h) / 2 * t_last
        prev_line = (0.5 * acc * acc_time**2) + v_max * (total_time - 2 * acc_time)
        x = prev_line + last_curve

    return x

num_points = 100
acc_decc_phase = 0.2
v_max = 0.4
total_time = 16

t_array = np.arange(0, total_time + (total_time / num_points), total_time / num_points)
p_array = [trapezoidal_function(t, total_time, acc_decc_phase, v_max) for t in t_array]

# plt.plot(t_array, p_array)
# plt.show()

# --------------------------------------------------------------------

def trapez_traj_function(t, acc_decc_phase, v_max, p_start, p_end):
    """
    It is position - time function. It creates trapezoidal motion profile using acc_decc_phase, v_max and position data. 
    Total time is automatically calculated. 
    It gives position at time t.
    """
    
    total_distance = abs(p_start - p_end)
    total_time = total_distance / (v_max * (1 - acc_decc_phase))
    acc_time = total_time * acc_decc_phase
    acc = v_max / acc_time
    const_vel_time = total_time * (1 - 2 * acc_decc_phase)
    
    # acceleration phase
    if t < acc_time:
        x_add = 0.5 * acc * t**2

    # constant velocity phase
    elif t < total_time - acc_time:
        x_add = (0.5 * acc * acc_time**2) + v_max * (t - acc_time)
    
    # deceleration phase
    else:
        t_last = t - acc_time - const_vel_time
        h = acc * (total_time - t)
        last_curve = (v_max + h) / 2 * t_last
        prev_line = (0.5 * acc * acc_time**2) + v_max * (total_time - 2 * acc_time)
        x_add = prev_line + last_curve
    
    if p_start > p_end:
        x = p_start - x_add
    else:
        x = p_start + x_add

    return x

def get_trapez_total_time(acc_decc_phase, v_max, p_start, p_end):
    """
    It returns total time for trapezoidal motion using acc_decc_phase, v_max and position data.
    """
    
    total_distance = abs(p_start - p_end)
    total_time = total_distance / (v_max * (1 - acc_decc_phase))
    return total_time

num_points = 100
acc_decc_phase = 0.2
v_max = 0.4
p_start = 2.0
p_end = 8.0

total_time = get_trapez_total_time(acc_decc_phase, v_max, p_start, p_end)

t_array = np.arange(0, total_time + (total_time / num_points), total_time / num_points)
p_array = [trapez_traj_function(t, acc_decc_phase, v_max, p_start, p_end) for t in t_array]

# print("total time = ", total_time)
# plt.plot(t_array, p_array)
# plt.show()

# --------------------------------------------------------------------

def get_trapez_velocity(total_time, acc_decc_phase, p_start, p_end):
    """
    It returns v_max for trapezoidal motion using total_time, acc_decc_phase and position data.
    """
    
    total_distance = abs(p_start - p_end)
    v_max = total_distance / (total_time * (1 - acc_decc_phase))
    return v_max

num_points = 100
acc_decc_phase = 0.4
p_start = 10.0
p_end = 20.0
total_time = 12

v_max = get_trapez_velocity(total_time, acc_decc_phase, p_start, p_end)

t_array = np.arange(0, total_time + (total_time / num_points), total_time / num_points)
p_array = [trapez_traj_function(t, acc_decc_phase, v_max, p_start, p_end) for t in t_array]

# print("v_max = ", v_max)
# plt.plot(t_array, p_array)
# plt.show()

# --------------------------------------------------------------------

def trapez_velocity_profile(t, acc_decc_phase, v_max, p_start, p_end):
    """
    It is velocity - time function. It creates trapezoidal motion profile using acc_decc_phase, v_max and position data.
    Total time is automatically calculated. 
    It gives velocity at time t.
    """
    
    total_distance = abs(p_start - p_end)
    total_time = total_distance / (v_max * (1 - acc_decc_phase))
    acc_time = total_time * acc_decc_phase
    acc = v_max / acc_time
    const_vel_time = total_time * (1 - 2 * acc_decc_phase)
    
    # acceleration phase
    if t < acc_time:
        vel = acc * t

    # constant velocity phase
    elif t < total_time - acc_time:
        vel = v_max
    
    # deceleration phase
    else:
        new_t = t - acc_time - const_vel_time
        vel = v_max - (acc * new_t)
        
    return vel

num_points = 100
acc_decc_phase = 0.2
p_start = 0.0
p_end = 12.0
v_max = 1.6

total_time = get_trapez_total_time(acc_decc_phase, v_max, p_start, p_end)

t_array = np.arange(0, total_time + (total_time / num_points), total_time / num_points)
p_array = [trapez_velocity_profile(t, acc_decc_phase, v_max, p_start, p_end) for t in t_array]

# print("total_time = ", total_time)
# plt.plot(t_array, p_array)
# plt.show()

# --------------------------------------------------------------------

def trapez_velocity_profile_with_time(t, acc_decc_phase, total_time, p_start, p_end):
    """
    It is velocity - time function. It creates trapezoidal motion profile using acc_decc_phase, total_time and position data.
    v_max is automatically calculated. 
    It gives velocity at time t.
    """
    
    total_distance = abs(p_start - p_end)
    v_max = total_distance / (total_time * (1 - acc_decc_phase))
    acc_time = total_time * acc_decc_phase
    acc = v_max / acc_time
    const_vel_time = total_time * (1 - 2 * acc_decc_phase)
    
    # acceleration phase
    if t < acc_time:
        vel = acc * t

    # constant velocity phase
    elif t < total_time - acc_time:
        vel = v_max
    
    # deceleration phase
    else:
        new_t = t - acc_time - const_vel_time
        vel = v_max - (acc * new_t)
        
    return vel

num_points = 100
acc_decc_phase = 0.3
p_start = 0.0
p_end = 24.0
total_time = 10

v_max = get_trapez_velocity(total_time, acc_decc_phase, p_start, p_end)

t_array = np.arange(0, total_time + (total_time / num_points), total_time / num_points)
p_array = [trapez_velocity_profile_with_time(t, acc_decc_phase, total_time, p_start, p_end) for t in t_array]

# print("v_max = ", v_max)
# plt.plot(t_array, p_array)
# plt.show()
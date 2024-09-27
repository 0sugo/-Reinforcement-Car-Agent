def reward_function(params):
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']  # Assuming speed is available in params
    # Calculate markers for varying distances from the centerline
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Initialize reward
    reward = 1e-3  # Default reward for staying on track

    # Reward for staying close to the centerline
    if distance_from_center <= marker_1:
        reward += 1.0  # Closest to center
    elif distance_from_center <= marker_2:
        reward += 0.5  # Moderate distance from center
    elif distance_from_center <= marker_3:
        reward += 0.1  # Farther distance from center

    # Additional reward for maintaining speed
    if speed > 2.0:  # You can adjust the speed threshold
        reward += 1.0  # Encourage faster speeds

    # Penalize if the car is too far from the centerline
    if distance_from_center > marker_3:
        reward = 1e-3  # Likely crashed or off track

    return float(reward)

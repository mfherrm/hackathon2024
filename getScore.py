import numpy as np
from getAdvice import getAdvice

def getScore(df):


    dat = df.iloc[1]
    left_arm_diff = dat.diff_l_arm
    right_arm_diff = dat.diff_r_arm

    left_leg_diff = dat.diff_l_leg
    right_leg_diff = dat.diff_r_leg

    left_hip_diff = dat.diff_l_hip
    right_hip_diff = dat.diff_r_hip

    print(left_arm_diff, right_arm_diff, left_leg_diff, right_leg_diff, left_hip_diff, right_hip_diff)

    # Calculate scores for left arm angle
    if np.abs(left_arm_diff) < 30:
        left_arm_score = 1
    else:
        left_arm_score = 0

    # Calculate scores for right arm angle
    if np.abs(right_arm_diff) < 30:
        right_arm_score = 1
    else:
        right_arm_score = 0

    # Calculate scores for left leg angle
    if np.abs(left_leg_diff) < 10:
        left_leg_score = 3
    elif 10 < np.abs(left_leg_diff) < 20:
        left_leg_score = 2
    elif 20 < np.abs(left_leg_diff) < 30:
        left_leg_score = 1
    else:
        left_leg_score = 0

    # Calculate scores for right leg angle
    if np.abs(right_leg_diff) < 10:
        right_leg_score = 3
    elif 10 < np.abs(right_leg_diff) < 20:
        right_leg_score = 2
    elif 20 < np.abs(right_leg_diff) < 30:
        right_leg_score = 1
    else:
        right_leg_score = 0

    # Calculate scores for left hip angle
    if np.abs(left_hip_diff) < 10:
        left_hip_score = 3
    elif 10 < np.abs(left_hip_diff) < 20:
        left_hip_score = 2
    elif 20 < np.abs(left_hip_diff) < 30:
        left_hip_score = 1
    else:
        left_hip_score = 0

    # Calculate scores for right hip angle
    if np.abs(right_hip_diff) < 10:
        right_hip_score = 3
    elif 10 < np.abs(right_hip_diff) < 20:
        right_hip_score = 2
    elif 20 < np.abs(right_hip_diff) < 30:
        right_hip_score = 1
    else:
        right_hip_score = 0

    # Calculate total score
    total_score = left_arm_score + right_arm_score + left_leg_score + right_leg_score + left_hip_score + right_hip_score

    getAdvice(left_arm_diff, right_arm_diff, left_leg_diff, right_leg_diff, left_hip_diff, right_hip_diff)
    print("Total Score (from 14):", total_score)
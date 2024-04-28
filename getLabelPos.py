import numpy as np
import pandas as pd

def calculate_angle(start, end, connection):
    to_end = end - connection
    to_start = start - connection

    # Calculate the dot product and magnitudes of the vectors
    dot_product = np.dot(to_start, to_end)
    magnitude_to_end = np.linalg.norm(to_end)
    magnitude_to_start = np.linalg.norm(to_start)

    try:
        # Calculate the cosine of the angle between the vectors
        cosine_angle = dot_product / (magnitude_to_end * magnitude_to_start)

        # Calculate the angle in radians and convert it to degrees
        angle_radians = np.arccos(cosine_angle)
        angle_degrees = np.degrees(angle_radians)

        return angle_degrees
    except:
        return -999

def getLabelPos(kp):
    # Define a dictionary mapping keypoint indices to body part names
    keypoint_labels = {
        0: 'Nose',
        1: 'Left Eye',
        2: 'Right Eye',
        3: 'Left Ear',
        4: 'Right Ear',
        5: 'Left Shoulder',
        6: 'Right Shoulder',
        7: 'Left Elbow',
        8: 'Right Elbow',
        9: 'Left Wrist',
        10: 'Right Wrist',
        11: 'Left Hip',
        12: 'Right Hip',
        13: 'Left Knee',
        14: 'Right Knee',
        15: 'Left Ankle',
        16: 'Right Ankle'
    }
    coordinates = {}
    coords_overview = {}
    for kp in zip(keypoint_labels.values(), kp):
        coords_overview[kp[0]] = {"x": float(kp[1][0]),
                                  "y": float(kp[1][1])
                                  }
        coordinates[kp[0]] = np.array(kp[1].cpu())

    # Ideal angles (DUMMY)
    ideal_arm = 180
    ideal_leg = 90
    ideal_hip = 75

    # Calc the real angle
    r_arm_angle = calculate_angle(coordinates["Right Wrist"], coordinates["Right Shoulder"], coordinates["Right Elbow"])
    l_arm_angle = calculate_angle(coordinates["Left Wrist"], coordinates["Left Shoulder"], coordinates["Left Elbow"])

    r_leg_angle = calculate_angle(coordinates["Right Ankle"], coordinates["Right Hip"], coordinates["Right Knee"])
    l_leg_angle = calculate_angle(coordinates["Left Ankle"], coordinates["Left Hip"], coordinates["Left Knee"])

    r_hip_angle = calculate_angle(coordinates["Right Knee"], coordinates["Right Shoulder"], coordinates["Right Hip"])
    l_hip_angle = calculate_angle(coordinates["Left Knee"], coordinates["Left Shoulder"], coordinates["Left Hip"])

    # print("Right Arm Angle:", r_arm_angle)
    # print("Left Arm Angle:", l_arm_angle)
    # print("Right Leg Angle:", r_leg_angle)
    # print("Left Leg Angle:", l_leg_angle)
    # print("Right Hip Angle:", r_hip_angle)
    # print("Left Hip Angle:", l_hip_angle)

    # Calculate differences
    diff_r_arm = r_arm_angle - ideal_arm
    diff_l_arm = l_arm_angle - ideal_arm
    diff_r_leg = r_leg_angle - ideal_leg
    diff_l_leg = l_leg_angle - ideal_leg
    diff_r_hip = r_hip_angle - ideal_hip
    diff_l_hip = l_hip_angle - ideal_hip

    # print("Difference in Right Arm Angle:", diff_r_arm)
    # print("Difference in Left Arm Angle:", diff_l_arm)
    # print("Difference in Right Leg Angle:", diff_r_leg)
    # print("Difference in Left Leg Angle:", diff_l_leg)
    # print("Difference in Right Hip Angle:", diff_r_hip)
    # print("Difference in Left Hip Angle:", diff_l_hip)


    column_names = ["angle_arm_right", "angle_arm_left", "angle_leg_right", "angle_leg_left", "angle_hip_right", "angle_hip_left",
                    "diff_l_arm", "diff_r_arm", "diff_l_leg", "diff_r_leg", "diff_l_hip", "diff_r_hip"]
    value_vector = [l_arm_angle, r_arm_angle, l_leg_angle, r_leg_angle, l_hip_angle, r_hip_angle,
                    diff_l_arm, diff_r_arm, diff_l_leg, diff_r_leg, diff_l_hip, diff_r_hip]
    d = dict(zip(column_names, value_vector))

    #print(value_vector)
    df = pd.DataFrame(d, index=[0])

    df = df.fillna(-999)

    #print(df)
    return df
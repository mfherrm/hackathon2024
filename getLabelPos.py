import numpy as np
import pandas as pd
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
    print(coordinates)

    # print elbow angles

    r_wrist = coordinates["Right Wrist"]
    r_elbow = coordinates["Right Elbow"]
    r_shoulder = coordinates["Right Shoulder"]

    # print(r_elbow,r_wrist,r_shoulder)

    upper_arm_vector = r_shoulder - r_elbow
    lower_arm_vector = r_wrist - r_elbow

    # print(upper_arm_vector)
    # print(lower_arm_vector)
    # Calculate the dot product and magnitudes of the vectors
    dot_product = np.dot(lower_arm_vector, upper_arm_vector)
    magnitude_upper_arm = np.linalg.norm(upper_arm_vector)
    magnitude_lower_arm = np.linalg.norm(lower_arm_vector)

    # Calculate the cosine of the angle between the vectors
    try:
        cosine_angle = dot_product / (magnitude_upper_arm * magnitude_lower_arm)

        # Calculate the angle in radians and convert it to degrees
        angle_radians = np.arccos(cosine_angle)
        angle_arm_right = np.degrees(angle_radians)
    except:
        angle_arm_right = -999
    print("Angle between upper arm and lower arm (right):", angle_arm_right)

    # Extract coordinates for left arm
    l_wrist = coordinates["Left Wrist"]
    l_elbow = coordinates["Left Elbow"]
    l_shoulder = coordinates["Left Shoulder"]

    # Calculate upper and lower arm vectors for left arm
    upper_arm_vector_left = l_shoulder - l_elbow
    lower_arm_vector_left = l_wrist - l_elbow

    # Calculate the dot product and magnitudes of the vectors for left arm
    dot_product_left = np.dot(lower_arm_vector_left, upper_arm_vector_left)
    magnitude_upper_arm_left = np.linalg.norm(upper_arm_vector_left)
    magnitude_lower_arm_left = np.linalg.norm(lower_arm_vector_left)

    try:
        # Calculate the cosine of the angle between the vectors for left arm
        cosine_angle_left = dot_product_left / (magnitude_upper_arm_left * magnitude_lower_arm_left)

        # Calculate the angle in radians and convert it to degrees for left arm
        angle_radians_left = np.arccos(cosine_angle_left)
        angle_arm_left = np.degrees(angle_radians_left)

    except:
        angle_arm_left = -999

    print("Angle between upper arm and lower arm (Left):", angle_arm_left)

    # Extract coordinates of right hip, right knee, and right foot
    r_hip = coordinates["Right Hip"]
    r_knee = coordinates["Right Knee"]
    r_ankle = coordinates["Right Ankle"]

    # Extract coordinates of left hip, left knee, and left foot
    l_hip = coordinates["Left Hip"]
    l_knee = coordinates["Left Knee"]
    l_ankle = coordinates["Left Ankle"]

    # Calculate angles for right leg
    r_hip_knee_vector = r_hip - r_knee
    r_ankle_knee_vector = r_ankle - r_knee

    # Calculate the dot product and magnitudes of the vectors
    dot_product_r = np.dot(r_hip_knee_vector, r_ankle_knee_vector)
    magnitude_r_hip_knee = np.linalg.norm(r_hip_knee_vector)
    magnitude_r_ankle_knee = np.linalg.norm(r_ankle_knee_vector)

    try:
        # Calculate the cosine of the angle between the vectors
        cosine_angle_r = dot_product_r / (magnitude_r_hip_knee * magnitude_r_ankle_knee)

        # Calculate the angle in radians and convert it to degrees
        angle_radians_r = np.arccos(cosine_angle_r)
        angle_leg_right = np.degrees(angle_radians_r)

    except:
        angle_leg_right = -999

    print("Angle between right hip, right knee, and right foot:", angle_leg_right)

    # Calculate angles for left leg
    l_hip_knee_vector = l_hip - l_knee
    l_ankle_knee_vector = l_ankle - l_knee

    # Calculate the dot product and magnitudes of the vectors
    dot_product_l = np.dot(l_hip_knee_vector, l_ankle_knee_vector)
    magnitude_l_hip_knee = np.linalg.norm(l_hip_knee_vector)
    magnitude_l_ankle_knee = np.linalg.norm(l_ankle_knee_vector)

    try:
        # Calculate the cosine of the angle between the vectors
        cosine_angle_l = dot_product_l / (magnitude_l_hip_knee * magnitude_l_ankle_knee)

        # Calculate the angle in radians and convert it to degrees
        angle_radians_l = np.arccos(cosine_angle_l)
        angle_leg_left = np.degrees(angle_radians_l)

    except:
        angle_leg_left = -999

    print("Angle between left hip, left knee, and left foot:", angle_leg_left)

    # Extract coordinates of right shoulder
    r_shoulder = coordinates["Right Shoulder"]

    # Extract coordinates of left shoulder
    l_shoulder = coordinates["Left Shoulder"]

    # Calculate angles for right leg towards right shoulder
    r_shoulder_hip_vector = - r_shoulder - r_hip
    r_knee_hip_vector = r_knee - r_hip

    # Calculate the dot product and magnitudes of the vectors
    dot_product_r_shoulder = np.dot(r_shoulder_hip_vector, r_knee_hip_vector)
    magnitude_r_shoulder_hip = np.linalg.norm(r_shoulder_hip_vector)
    magnitude_r_knee_hip = np.linalg.norm(r_knee_hip_vector)

    try:
        # Calculate the cosine of the angle between the vectors
        cosine_angle_r_shoulder = dot_product_r_shoulder / (magnitude_r_shoulder_hip * magnitude_r_knee_hip)

        # Calculate the angle in radians and convert it to degrees
        angle_radians_r_shoulder = np.arccos(cosine_angle_r_shoulder)
        angle_hip_right = np.degrees(angle_radians_r_shoulder)

    except:
        angle_hip_right = -999

    print("Angle between right shoulder, right hip, and right knee:", angle_hip_right)

    # Calculate angles for left leg towards left shoulder
    l_shoulder_hip_vector = l_shoulder - l_hip
    l_knee_hip_vector = l_knee - l_hip

    # Calculate the dot product and magnitudes of the vectors
    dot_product_l_shoulder = np.dot(l_shoulder_hip_vector, l_knee_hip_vector)
    magnitude_l_shoulder_hip = np.linalg.norm(l_shoulder_hip_vector)
    magnitude_l_knee_hip = np.linalg.norm(l_knee_hip_vector)

    try:
        # Calculate the cosine of the angle between the vectors
        cosine_angle_l_shoulder = dot_product_l_shoulder / (magnitude_l_shoulder_hip * magnitude_l_knee_hip)

        # Calculate the angle in radians and convert it to degrees
        angle_radians_l_shoulder = np.arccos(cosine_angle_l_shoulder)
        angle_hip_left = np.degrees(angle_radians_l_shoulder)
    except:
        angle_hip_left = -999
        print("Angle between left shoulder, left hip, and left knee:", angle_hip_left)

    column_names = ["angle_arm_right", "angle_arm_left", "angle_leg_right", "angle_leg_left", "angle_hip_right", "angle_hip_left"]
    values = [angle_arm_right, angle_arm_left, angle_leg_right, angle_leg_left, angle_hip_right, angle_hip_left]

    # Combine column names and values using zip
    data = zip(column_names, values)  # Unpack values using * operator

    # Create the DataFrame
    df = pd.DataFrame(data)

    df = df.fillna(0)

    print(df)
    return df
def getAdvice(left_arm_diff, right_arm_diff, left_leg_diff, right_leg_diff, left_hip_diff, right_hip_diff):

    # Check left arm angle
    if -20 < left_arm_diff < 20:
        print("Correct left elbow angle")
    elif left_arm_diff > 30:  #if the angle diff is bw 20 and 30, it doesn't print correct but it also doesn't advice as elbow angle is not that important
        print("Advice: Bend your left elbow more")
    else:
        print("Advice: Extend your left elbow More")

    # Check right arm angle
    if -20 < right_arm_diff < 20:
        print("Correct right right elbow angle")
    elif right_arm_diff > 30:
        print("Advice: Bend your right elbow more")
    else:
        print("Advice: Extend your right elbow More")

    # Check left leg angle
    if -10 < left_leg_diff < 10:
        print("Correct left knee angle")
    elif left_leg_diff > 10:
        print("Advice: Bend further down with your left knee")
    else:
        print("Advice: Go a little up with your left knee")

    # Check right leg angle
    if -10 < right_leg_diff < 10:
        print("Correct right knee angle")
    elif right_leg_diff > 10:
        print("Advice: Bend further down with your right knee")
    else:
        print("Advice: Go a little up with your right knee")

    # Check left hip angle
    if -10 < left_hip_diff < 10:
        print("Correct left hip angle")
    elif left_hip_diff > 10:
        print("Advice: Bend further down with your left hip")
    else:
        print("Advice: Go a little up with your left hip")

    # Check right hip angle
    if -10 < right_hip_diff < 10:
        print("Correct right hip angle")
    elif right_hip_diff > 10:
        print("Advice: Bend further down with your right hip")
    else:
        print("Advice: Go a little up with your right hip")

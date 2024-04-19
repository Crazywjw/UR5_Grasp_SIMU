#! /usr/bin/env python
import sys
import rospy
import moveit_commander
import geometry_msgs
import tf

 
moveit_commander.roscpp_initializer.roscpp_initialize(sys.argv)
rospy.init_node('move_group_grasp', anonymous=True)
robot = moveit_commander.robot.RobotCommander()


arm_group = moveit_commander.move_group.MoveGroupCommander("manipulator")
hand_group = moveit_commander.move_group.MoveGroupCommander("gripper")

arm_group.set_pose_reference_frame('base_link')
arm_group.set_goal_position_tolerance(0.1)
arm_group.set_goal_orientation_tolerance(0.1)
# hand_group.set_named_target("open")
# plan = hand_group.go()

# print("Point up")


# arm_group.set_named_target("up")
# plan = arm_group.go()
# pose_target = arm_group.get_current_pose().pose
# print(pose_target)
# print("Point up")

index = 0
safety_p = [1.349744, -1.228585, 0.939975, -1.587156, -1.578816, -1.779357]
close_p = [1.672925, -0.565759, 0.172003, -1.198983, -1.555219, 1.113457]
grasp_p = [1.676191, -0.690756, 0.517451, -1.450846, -1.532626, 1.153410]
grasp_p1 = [0.37,-0.37,0.37,0.37,-0.37,0.37]
preplace_p1 = [0.052718, -1.228558, 0.940041, -1.587156, -1.578816, -1.779357]
preplace_p2 = [0.148556, -0.417628, 2.193252, -3.263811, -1.607591, -1.426900]
place_p = [0.128450, 0.119911, 1.795878, -3.404631, -1.609176, -1.446759]
pose_target = arm_group.get_current_pose().pose
dict_p = {'p1': "up",'p2' : "open",'p3' : safety_p,'p4' : close_p,'p5' : grasp_p,'p6' : grasp_p1,'p7' : grasp_p,'p8' : safety_p, \
          'p9' : preplace_p1,'p10' : preplace_p2, 'p11' : place_p, 'p12' : "open",'p13' : preplace_p2, 'p14' : preplace_p1,'p15' : safety_p}

for temp in dict_p.values():
    if temp == "up" :
        arm_group.set_named_target("up")
        plan = arm_group.go(wait=True)
    elif temp == "open" :
        hand_group.set_named_target("open")
        plan = hand_group.go(wait=True)
    elif temp == grasp_p1 :
        hand_group.set_joint_value_target(temp)
        plan = hand_group.go(wait=True)
        rospy.sleep(0.5)
    else :
        arm_group.set_joint_value_target(temp)
        plan = arm_group.go(wait=True)
    pose_target = arm_group.get_current_pose().pose
    index += 1
    print(index)
    print(pose_target)

# pose_target.position.x = -0.19324975071541098
# pose_target.position.y = 0.8019314502239826
# pose_target.position.z = 0.37721120976796564
# pose_target.orientation.w = 0.004505472792930882
# pose_target.orientation.x = -0.8748151225047343
# pose_target.orientation.y = 0.48427103229663054
# pose_target.orientation.z = 0.012639993286973383



rospy.sleep(5)
moveit_commander.roscpp_initializer.roscpp_shutdown()

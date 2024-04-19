#!/usr/bin/env python3
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
arm_group.set_goal_position_tolerance(0.01)
arm_group.set_goal_orientation_tolerance(0.1)
#hand_group.set_named_target("close")
#plan = hand_group.go()



arm_group.set_named_target("up")
plan = arm_group.go()

print("Point 1")

# Open
arm_group.set_joint_value_target([1.507964, -1.005310, 0.628319, 0.502655, 1.633628, -1.382301])
arm_group.go(wait=True)
print("Point 2")
# hand_group.set_named_target("open")
# plan = hand_group.go()
# print("Point 3")


pose_target = arm_group.get_current_pose().pose

print(pose_target)

# # Block point
pose_target.position.x = -0.06218019860776863
pose_target.position.y = 0.6672548317115188
pose_target.position.z = 0.4882826789457281
pose_target.orientation.w = -0.4430673899258716
pose_target.orientation.x = -0.4430673899258716
pose_target.orientation.y = 0.48029381543369093
pose_target.orientation.z = 0.65481278782268886


hand_group.set_pose_target(pose_target)
plan = hand_group.go(wait=True)
# arm_group.stop()
print("Point 4")

# # Block point
# pose_target.position.x = -0.2
# pose_target.position.y = 0.8
# pose_target.position.z = 0.8+0.06-0.07



# arm_group.set_pose_target(pose_target)
# arm_group.go(wait=True)
# print("Point 4")


# hand_group.set_named_target("close")
# plan = hand_group.go()
# print("Point 5")

# pose_target.position.z = 0.8+0.06-0.07+0.05
# arm_group.set_pose_target(pose_target)
# plan = arm_group.go()
# print("Point 6")


# pose_target.position.z = 0.8+0.06-0.07+0.05
# pose_target.position.x = 0.5
# arm_group.set_pose_target(pose_target)
# plan = arm_group.go()
# print("Point 7")



# hand_group.set_named_target("open")
# plan = hand_group.go()
# print("Point 8")

rospy.sleep(5)
moveit_commander.roscpp_initializer.roscpp_shutdown()

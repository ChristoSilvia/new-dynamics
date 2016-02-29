#!/usr/bin/env python

import numpy as np

import rospy

import baxter_interface

from baxter_pykdl import baxter_kinematics

if __name__ == '__main__':
	rospy.init_node("test")
	rospy.loginfo("Test node initialized")
	
	enabler = baxter_interface.RobotEnable()
	enabler.enable()

	rospy.loginfo("Robot Enabled")

	limb = baxter_interface.Limb('left')
	limb_kin = baxter_kinematics('left')

	I = np.array(limb_kin.joint_space_inertias())

	rospy.loginfo(I)

	enabler.disable()
	rospy.loginfo("Robot Disabled")

	rospy.loginfo("Exiting")


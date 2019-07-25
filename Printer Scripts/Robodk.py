# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:19:06 2019

@author: Rez
"""

from robolink import *
from robodk import *

RDK = Robolink()
robot = RDK.Item('', ITEM_TYPE_ROBOT)

MAX_X = 20
MAX_Y = 20
MAX_Z = 50
CURR_X = 20
CURR_Y = 20
CURR_Z = 50
def ProgramRun():
	MAX_X = 20
	MAX_Y = 20
	MAX_Z = 50
	global CURR_X
	global CURR_Y
	global CURR_Z
	tarNum = 1
	while(RDK.Item('Target %x' % tarNum).Valid()):
                Target = RDK.Item('Target %x' % tarNum)
                ref_frame = Target.Parent()
                NewTarget = RDK.AddTarget("Pose %x" % tarNum, ref_frame, robot)
                NewTarget.setAsJointTarget()
                NewTarget.setJoints(Target.Joints())
                tarPose = Target.Pose()
                xyzabc = Pose_2_KUKA(tarPose)
                x,y,z,a,b,c = xyzabc
                if (x < 0):
                        xoff = (MAX_X - CURR_X)/2
                elif x == 0:
                        xoff = 0
                else:
                        xoff = -(MAX_X - CURR_X)/2
                if (y < 0):
                        yoff = (MAX_Y - CURR_Y)/2
                elif y == 0:
                        yoff = 0
                else:
                        yoff = -(MAX_Y - CURR_Y)/2
                if (z < 0):
                        zoff = (MAX_Z - CURR_Z)/2
                elif z == 0:
                        zoff = 0
                else:
                        zoff = -(MAX_Z - CURR_Z)/2

                xyzabc2 = [x+xoff,y+yoff,z+zoff,a,b,c]
                pose2 = KUKA_2_Pose(xyzabc2)
                NewTarget.setPose(pose2)
                tarNum = tarNum + 1
        
from tkinter import *

root = Tk()
root.title("Program settings")

currx = IntVar()
currx.set(CURR_X)
curry = IntVar()
curry.set(CURR_Y)
currz = IntVar()
currz.set(CURR_Z)

Label(root, text="Length of Object").pack()
Entry(root, textvariable=currx).pack()
Label(root, text="Width of Object").pack()
Entry(root, textvariable=curry).pack()
Label(root, text="Height of Object").pack()
Entry(root, textvariable=currz).pack()

def ExecuteChoice():
	global CURR_X
	global CURR_Y
	global CURR_Z
	CURR_X = currx.get()
	CURR_Y = curry.get()
	CURR_Z = currz.get()
	poseNum = 1
	while(RDK.Item("Pose %x" % poseNum).Valid()):
		RDK.Item('Pose %x' % poseNum).Delete()
		poseNum = poseNum + 1
	ProgramRun()

Button(root, text='Simulate/Generate', command=ExecuteChoice).pack()

# Important to display the graphical user interface
root.mainloop()

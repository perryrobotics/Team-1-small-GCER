#!/usr/bin/python
import os, sys
from wallaby import * 
from movement import * 
from effectors import *


LEFT = 0
RIGHT = 1
LIGHT_SENSOR = 1
def main():
	enable_servos()
#Get ready for the starting
	msleep(300)
	arm_back(50)
	#wait_for_start(LIGHT_SENSOR)
        
	#move_to_black(900,0,2700)
	#move_to_white(900,0,500)
	#move_to_black(900,0,2700)
	#msleep(10000)
	#back_to_white(900,0,500)
	#back_to_black(900,0,2700)
	#back_to_white(900,0,500)
	move_to_black(900,0,2700)
   	left(900,650)
 	backward(900,1000) # hit pipe
  	forward(900,1000)  #get off pipe
  	right(900,250)
        
	forward(900,2000)
   	move_to_black(900,0,3000) #go to black tape
    
 	forward(900,3000)    
	right(900,700)  #might_need_to_adjust_at_comp.
	arm_down(50)
 	move_to_black(900,0,2700)
	forward(900,300)
	arm_powerline(50)
 	forward(900,250)
	right(900,20)
 	forward(900,1100)
	right(900,20)
	msleep(1000)
	left(900,20)
	backward(900,700)
 	set_servo_position(ARM_P, ARM_D)
	msleep(1000)
	backward(900,2000)
	right(900,100)
	backward(900,2000)
	forward(900,500)
	right(900,20)
	forward(900,3500)
	left(900,1250)  #might_need_to_adjust_at_comp.
	arm_down(50)
	forward(900,2400)
 	arm_power(50)
	msleep(1000)
  	left(300,300)
 	forward(900,900)
	right(900,100)
	msleep(1000)
	left(900,20)
	backward(900,700)
 	set_servo_position(ARM_P, ARM_D)
	msleep(1000)
	backward(900,1000)
	disable_servos()
	
	
if __name__== "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main();

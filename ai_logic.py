import time
from sensors import get_distance
from motor_control import stop_motors, move_forward
from config import OBSTACLE_THRESHOLD

def avoid_obstacle():
    stop_motors()
    time.sleep(0.5)
    
    left_distance = get_distance()
    
    
    move_forward()
    time.sleep(0.5)
    
    right_distance = get_distance()
    
    if left_distance > right_distance:
        move_forward() 
    else:
        move_forward()  
    
    time.sleep(0.5)
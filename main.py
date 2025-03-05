import time
from sensors import get_distance
from motor_control import move_forward, stop_motors
from ai_logic import avoid_obstacle
from config import OBSTACLE_THRESHOLD

def main():
    while True:
        distance = get_distance()
        print(f"Distance: {distance} cm")
        
        if distance < OBSTACLE_THRESHOLD:
            avoid_obstacle()
        else:
            move_forward()
        
        time.sleep(0.1)

if __name__ == "__main__":
    main()
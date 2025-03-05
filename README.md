

# 🚀 AI Obstacle Avoidance Robot (Python + Raspberry Pi)  

## 📌 Overview  
This project is an **AI-powered obstacle avoidance robot** built with **Raspberry Pi, Ultrasonic sensors, and DC motors**. The robot **detects obstacles** and intelligently decides the best path using a **simple AI algorithm**.

---

## 🔧 Hardware Components  
| Component              | Quantity |
|------------------------|---------|
| Raspberry Pi (3/4)    | 1       |
| HC-SR04 Ultrasonic Sensor | 1       |
| L298N Motor Driver    | 1       |
| DC Motors (2 Wheels)  | 2       |
| Battery Pack (12V)    | 1       |
| Jumper Wires          | Various |

---

## 🛠️ Hardware Wiring Instructions  
### **1️⃣ Connecting the Ultrasonic Sensor (HC-SR04)**
| HC-SR04 Pin | Raspberry Pi GPIO |
|------------|------------------|
| VCC        | 5V |
| GND        | GND |
| TRIG       | GPIO 17 |
| ECHO       | GPIO 27 |

### **2️⃣ Connecting the Motor Driver (L298N)**
| L298N Pin | Raspberry Pi GPIO |
|----------|------------------|
| ENA      | GPIO 5 |
| ENB      | GPIO 6 |
| IN1      | GPIO 7 |
| IN2      | GPIO 8 |
| IN3      | GPIO 9 |
| IN4      | GPIO 10 |

---


## 🛠️ Software Installation  

### **1️⃣ Update & Upgrade Raspberry Pi**

sudo apt update && sudo apt upgrade -y

2️⃣ Install Python Libraries

pip install RPi.GPIO

3️⃣ Clone the Repository

git clone https://github.com/georgmichelle/AI-Obstacle-Avoidance-Robot.git
cd AI-Obstacle-Avoidance-Robot


---

🚀 Running the Project

1️⃣ Run the Main Script

python3 main.py

The robot will start moving forward and avoid obstacles intelligently.


---

🤖 Code Explanation

📝 Main Logic (main.py)

This script continuously checks the distance from obstacles and decides whether to move forward or avoid them.

📡 Sensor Code (sensors.py)

Measures the distance using the HC-SR04 ultrasonic sensor.


🔧 Motor Control (motor_control.py)

Controls DC motors using L298N motor driver.


🧠 AI Logic (ai_logic.py)

The robot decides the best way to avoid obstacles dynamically.

🔧 Configuration File (config.py)

Stores GPIO pin numbers and constants.


---

📈 Future Improvements

✅ Machine Learning (ML) to enhance obstacle avoidance
✅ Camera Integration with OpenCV for advanced vision
✅ Remote Control Mode via Bluetooth


---

🛠️ Troubleshooting

1️⃣ Ultrasonic Sensor Not Working?

Make sure TRIG and ECHO pins are connected correctly.

Check power supply (5V for the sensor).


2️⃣ Motors Not Moving?

Verify connections between Raspberry Pi and L298N Motor Driver.

Ensure battery pack provides sufficient voltage.


3️⃣ Python Script Not Running?

Ensure you are using Python 3:

python3 main.py



---

👤 Author

📌 Developed by Georg Michelle



---

🌟 Support the Project

If you find this project useful, please ⭐️ Star the Repository on GitHub! 🚀

---




# 🚗 Driver Drowsiness Eye Blink Detection System

A real-time driver safety system that detects driver drowsiness using eye blink detection and triggers hardware alerts to prevent road accidents. This project combines **computer vision**, **Python**, and **embedded systems** to address a real-world safety-critical problem.

---

## 📌 Project Overview

Driver fatigue is one of the leading causes of road accidents, especially during long-distance driving.  
This system continuously monitors the driver’s eye state using a camera. If the driver’s eyes remain closed for more than **1.5 seconds**, the system identifies drowsiness and immediately triggers an alert using LEDs and a buzzer.

The project demonstrates how **software (Python + OpenCV)** can be effectively integrated with **hardware (Arduino)** to create a real-time safety solution.

---

## ✨ Key Features

- Real-time face and eye detection
- Accurate eye blink and eye-closure analysis
- Drowsiness detection with time threshold (1.5 seconds)
- Hardware alerts using LEDs and buzzer
- Continuous alert until driver regains alertness
- Low-cost and efficient design
- Suitable for real-world vehicle integration

---

## 🛠 Technologies Used

### Software
- **Programming Language:** Python
- **Libraries:** OpenCV
- **IDE:** Visual Studio Code

### Hardware
- Arduino Uno
- Camera (Webcam / USB Camera)
- Red LED (Drowsiness alert)
- Green LED (Normal state)
- Buzzer

### Communication
- Serial communication (USB)

---

## ⚙ System Architecture & Working

1. Camera continuously captures the driver’s face
2. Python processes video frames using OpenCV
3. Haar Cascade detects the face and eyes
4. Eye state is analyzed (open or closed)
5. Eye closure duration is measured
6. If eyes are closed for more than **1.5 seconds**:
   - Alert signal sent to Arduino
   - Red LED blinks
   - Buzzer sounds continuously
7. When eyes reopen:
   - Alert stops immediately
   - Green LED glows

---

## 🧠 Why Eye Blink Detection?

Eye closure duration is one of the most reliable indicators of drowsiness.  
Compared to steering-based or posture-based methods, eye detection provides:
- Direct feedback of driver alertness
- Faster response
- Higher accuracy

---

## 📂 Project Structure

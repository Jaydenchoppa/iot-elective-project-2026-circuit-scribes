[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AnR2QgvN)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=22952764&assignment_repo_type=AssignmentRepo)

# 🚗 IoT Elective Project 2026
### Cape Peninsula University of Technology — IT Diploma
**Module:** Internet of Things (IoT) Elective | **Year:** 2026

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Group Members](#group-members)
3. [Project Idea & Problem Statement](#project-idea--problem-statement)
4. [System Architecture & Design](#system-architecture--design)
5. [Hardware Components](#hardware-components)
6. [Software & Technologies](#software--technologies)
7. [Circuit Diagram / Wiring](#circuit-diagram--wiring)
8. [Build Process](#build-process)
9. [Code Documentation](#code-documentation)
10. [Testing & Results](#testing--results)
11. [Challenges & Solutions](#challenges--solutions)
12. [Project Demonstration](#project-demonstration)
13. [References](#references)
14. [Assessment Rubric](#assessment-rubric)

---

## 📌 Project Overview

**Project Title:** `Smart Car System`
**Group Name / Number:** `circuit-scribes`
**Presentation Date:** 20 May 2026

---

## 👥 Group Members

| Student Name | Student Number | Role / Responsibility |
|---|---|---|
| Mvuyisi Mchithwa | 220452709 | Hardware Lead |
| Jayden Avontuur | 222032278 | Hardware Lead |
| Stephanie Tola Oluwafemi Lewu | 230211216 | Documentation Lead |
| Mpumelelo Sithole | 230526934 | Testing Lead |
| Owen Jnr Makene | 223219665 | Coding Lead |

---

## 💡 Project Idea & Problem Statement

### Problem Statement
Car theft remains a major issue, especially when traditional security methods such as keys, remotes, or PIN-based systems can be stolen, duplicated, or bypassed. There is a need for a more secure and intelligent system that ensures only authorized individuals can start a vehicle.

### Proposed Solution
The project proposes an AI-powered facial recognition system integrated into a mini smart car. A camera mounted on the dashboard captures the driver's face and verifies identity using facial recognition.

- If the face is **recognized** → the system allows the engine (DC motor) to start
- If **not recognized** → the engine remains locked

The system uses a NoIR camera to function in low-light or night conditions with IR LEDs.

### Objectives
- Develop a facial recognition system using AI (OpenCV LBPH)
- Enable secure engine access control via GPIO relay switching
- Implement night detection using a NoIR infrared camera
- Integrate hardware and software into a working IoT prototype
- Provide a wireless web-based interface for monitoring and control

---

## 🏗️ System Architecture & Design

![System Architecture Diagram](images/system_architecture.png)

### Design Decisions

**Central Computing Unit (Raspberry Pi 4):**
A Raspberry Pi 4 was selected as the core controller due to the computational demands of running real-time AI facial recognition locally while simultaneously hosting a Flask web server.

**Circuit Isolation via Relay Module:**
A 2-channel relay module isolates the low-voltage Pi (5V logic) from the high-voltage motor circuit (12V battery). This prevents high-current surges and back-EMF from damaging the Pi.

**Fail-Safe Ignition (Normally Open Configuration):**
The DC motor is wired to the Normally Open (NO) terminal of the relay. In the event of a system crash or power loss, the ignition circuit defaults to open (disengaged), prioritizing safety.

**High-Bandwidth Camera Interface (CSI Ribbon Cable):**
The NoIR Pi Camera connects via a native CSI ribbon cable rather than USB, providing a direct high-speed link to the processor, reducing video latency and optimizing facial recognition speed.

**Decoupled Wireless User Interface (Flask & Wi-Fi):**
The user interface is a browser-based web page (`index.html`) hosted on the Pi via Flask over Wi-Fi. Users can scan faces and control the engine from any device on the same local network.

**Authentication-Gated Engine Start:**
The motor is off by default on server startup. The Start Engine button is locked in the UI until a successful face scan is completed. A failed scan keeps the motor locked and resets authorization.

---

## 🔧 Hardware Components

| Component | Description | Quantity | Purpose |
|---|---|---|---|
| Raspberry Pi 4 | Single-board computer | 1 | Main processor and controller |
| MicroSD Card 32GB | Flash storage media | 1 | Operating system and local data storage |
| NoIR Camera Module | Infrared-sensitive camera | 1 | Face capture in normal and low-light conditions |
| DC Motor | Direct current motor | 1 | Simulates engine ignition |
| 12V Sealed Lead-Acid Battery | Battery power source | 1 | Dedicated power supply for the DC motor |
| 2-Channel Relay Board | Electromechanical switch | 1 | Safely switching motor power via GPIO |
| Power Supply (5V) | AC/DC power adapter | 1 | Powering the Raspberry Pi |
| Micro HDMI to HDMI Cable | Video display cable | 1 | Connecting the Pi to a monitor during setup |
| Jumper Wires | Male-to-female wires | Several | GPIO and relay connections |

---

## 💻 Software & Technologies

| Tool / Platform | Purpose |
|---|---|
| Python 3 | Main programming language for facial recognition and GPIO control |
| OpenCV (cv2) | Image processing, face detection (Haar Cascade), and LBPH recognition |
| Picamera2 | Pi camera capture interface |
| Flask | Lightweight web server hosting the control UI |
| RPi.GPIO | Controlling the relay module via Raspberry Pi GPIO pins |
| Raspberry Pi OS (64-bit) | Operating system running on the Raspberry Pi 4 |
| Raspberry Pi Imager | Installing and configuring Raspberry Pi OS on the MicroSD card |
| Thonny IDE | Writing, editing, and testing Python code on the Raspberry Pi |
| GitHub | Version control, collaboration, and project documentation |
| Markdown | Formatting and documenting the project on GitHub |

---

## 🔌 Circuit Diagram / Wiring

![Circuit Diagram](images/circuit_diagram.png)

| Component Pin | Raspberry Pi Pin | Notes |
|---|---|---|
| Relay IN | GPIO 17 (Pin 11) | Control signal — HIGH = motor ON, LOW = motor OFF |
| Relay VCC | 5V (Pin 2) | Power for relay module |
| Relay GND | GND (Pin 6) | Common ground |
| Motor + | Relay NO (Normally Open) | Motor off by default — closes when relay activates |
| Motor − | Battery GND | Completes the motor circuit |
| Battery + | Relay COM | Main power supply input to relay |
| Pi Camera | CSI Port | Ribbon cable — direct high-speed connection |

### Wiring Flow

```
Raspberry Pi GPIO 17 ──► Relay IN  (control signal)
Raspberry Pi 5V      ──► Relay VCC (relay power)
Raspberry Pi GND     ──► Relay GND (common ground)

Battery +  ──► Relay COM
Relay NO   ──► Motor +
Motor −    ──► Battery −

Pi Camera  ──► CSI Ribbon Cable Port
```

---

## 🏭 Build Process

### Steps to Install Raspberry Pi OS

1. **Download Raspberry Pi Imager** from [raspberrypi.com/software](https://www.raspberrypi.com/software/) and install it on your laptop or PC.

2. **Insert your microSD card** into your computer using a built-in SD slot or USB card reader. A 16GB or larger card is recommended.

3. **Open Raspberry Pi Imager** — you will see three options: Choose Device, Choose OS, Choose Storage.

4. **Choose Device** — select your Raspberry Pi model (Raspberry Pi 4).

5. **Choose OS** — select **Raspberry Pi OS (64-bit)**.

6. **Choose Storage** — select your microSD card.
   > ⚠️ Be careful — the selected drive will be completely erased.

7. **Write the OS** — click Next or Write. The software will download, install, and verify Raspberry Pi OS. This may take a few minutes.

8. **Insert the SD card into the Raspberry Pi** after the installation finishes.

9. **Connect everything** — HDMI to monitor, keyboard, mouse, and power supply.

10. **Power on the Raspberry Pi** — it will boot into Raspberry Pi OS and prompt you to complete first-time setup (language, Wi-Fi, password, updates).

### Steps to Run the Smart Car System

1. Place all project files in the same folder on the Pi:
   ```
   SmartCarSystem/
   ├── server.py
   ├── camera.py
   ├── motor.py
   ├── train.py
   ├── capture_faces.py
   ├── trainer.yml
   ├── AuthorizedFaces/
   │   ├── Person1/
   │   └── Person2/
   └── Website/
       └── index.html
   ```

2. Run `capture_faces.py` for each authorized driver to collect training photos via the Pi camera.

3. Run `train.py` to train the facial recognition model and generate `trainer.yml`.

4. Run `server.py` to start the Flask web server.

5. Open a browser on any device on the same Wi-Fi network and navigate to `http://<Pi-IP-address>:5000`.

---

## 🖥️ Code Documentation

The project consists of five Python files and one HTML file. Below is a description of each file and its key functions.

### File Structure

| File | Description |
|---|---|
| `capture_faces.py` | Auto-captures training photos for each person using the Pi camera |
| `train.py` | Trains the LBPH facial recognition model from the captured photos |
| `camera.py` | Handles live camera feed, face detection, and recognition |
| `motor.py` | Controls the relay module and DC motor via GPIO |
| `server.py` | Flask web server — routes HTTP requests to camera and motor logic |
| `Website/index.html` | Browser-based UI for scanning, starting, and stopping the engine |

---

### Key Functions: Capture Script (`capture_faces.py`)

| Step | Description |
|---|---|
| **Name Input** | Prompts for the person's name and creates a folder under `AuthorizedFaces/` |
| **Camera Setup** | Initializes Picamera2 to capture RGB images at 320×240 |
| **Auto Capture Loop** | Captures a photo every 2 seconds — only saves when a face is detected |
| **Output** | Saves 15 labeled photos per person for training |

---

### Key Functions: Training Script (`train.py`)

| Step | Description |
|---|---|
| **Initialization** | Sets up the Haar Cascade classifier and LBPH recognizer |
| **Directory Parsing** | Loops through `AuthorizedFaces/` to find each person's subfolder |
| **Image Processing** | Converts to grayscale, resizes to 200×200, detects and crops face regions |
| **Model Training** | Trains the LBPH model with face crops and numeric ID labels |
| **Output** | Writes the trained model to `trainer.yml` |

---

### Key Functions: Camera Module (`camera.py`)

| Function | Description |
|---|---|
| `__init__()` | Initializes the Pi camera, loads Haar Cascade, and loads `trainer.yml` |
| `get_frame()` | Captures a frame and converts from RGB to BGR for OpenCV |
| `check_face()` | Detects faces, predicts against the trained model, returns authorization result |
| `generate_frames()` | Yields continuous JPEG frames for the live video stream |

---

### Key Functions: Motor Controller (`motor.py`)

| Function | Description |
|---|---|
| `__init__()` | Configures GPIO pin 17 as output and sets relay LOW (motor off) on startup |
| `start()` | Sets GPIO HIGH — activates relay — motor runs |
| `stop()` | Sets GPIO LOW — deactivates relay — motor stops and resets authorization |
| `grant_access()` | Sets `authorised = True`, allowing the Start Engine button to work |
| `deny_access()` | Revokes authorization and forces motor off |
| `status()` | Returns the current running state as a dictionary |
| `cleanup()` | Stops motor and releases all GPIO resources on server exit |

---

### Key Functions: Web Server (`server.py`)

| Route | Method | Description |
|---|---|---|
| `/` | GET | Serves `index.html` — the main web UI |
| `/live` | GET | Streams live MJPEG video from the Pi camera |
| `/scan` | POST | Triggers face check — grants or denies motor access based on result |
| `/start` | POST | Starts motor only if `motor.authorised` is True |
| `/stop` | POST | Stops motor immediately and resets authorization |

---

### Key Functions: Web Interface (`index.html`)

| Function | Description |
|---|---|
| `scan()` | Sends POST to `/scan`, updates UI status, locks or unlocks the Start button |
| `startEngine()` | Sends POST to `/start` — only executable after a successful scan |
| `stopEngine()` | Sends POST to `/stop`, stops motor and re-locks the Start button |

---

## 🧪 Testing & Results

| Test # | Description | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| 1 | NoIR camera captures training photos | Photos saved to AuthorizedFaces folder | Files saved successfully | ✅ Pass |
| 2 | Authorized driver scanned | Access Granted — Start button unlocks | Motor starts after pressing Start | ✅ Pass |
| 3 | Unregistered face scanned | Access Denied — motor stays off | Motor did not start | ✅ Pass |
| 4 | Motor off on server startup | Motor does not run before scan | Relay stayed open on boot | ✅ Pass |
| 5 | Stop Engine button pressed | Motor stops and Start button locks | Motor stopped and button locked | ✅ Pass |

---

## ⚠️ Challenges & Solutions

| Challenge | Solution |
|---|---|
| Configuring the Pi using only a laptop | Used an external keyboard, mouse, and monitor for initial setup |
| Using a PC USB port as power source | Switched to a 5V power bank with stable output |
| Relay not activating correctly | Checked and corrected GPIO pin connections and wiring |
| Motor not spinning after relay activation | Added a dedicated 12V battery — Pi cannot supply enough current for the motor |
| Incorrect motor wiring on relay terminals | Identified correct COM and NO terminals and rewired correctly |
| GPIO pin numbering confusion | Used a Raspberry Pi GPIO diagram to identify correct pins |
| Camera not detected | Reinserted CSI ribbon cable and enabled camera interface in Pi settings |
| Facial recognition failing in low light | Switched to NoIR camera with IR LEDs for night visibility |
| Unauthorized faces triggering the motor | Retrained with clearer images and adjusted recognition threshold |
| Python libraries failing to install | Updated Raspberry Pi OS and installed dependencies via terminal |
| Loose jumper wire connections | Secured all wires firmly on relay pins and GPIO header |
| Managing wiring inside the car body | Used a 3D-printed chassis and cable management to organize components |
| Team members having different electronics knowledge | Divided responsibilities and provided step-by-step peer guidance |
| Motor power interfering with Pi safety | Isolated motor power from Pi power supply entirely |
| Color space mismatch causing recognition failure | Fixed by converting RGB→BGR before grayscale conversion in `camera.py` |
| Face size mismatch between training and prediction | Added `cv2.resize(face, (200, 200))` before `predict()` to match training |

---

## 🎥 Project Demonstration

- 📹 **Demo Video:** [Watch here](https://we.tl/t-QmCiW5JmK1eeSpes)
- 📊 **Presentation Slides:** [View on Canva](https://canva.link/5uzpkgjfu6mxgbv)

---

## 📚 References

1. [How to Setup the Raspberry Pi NoIR Camera V2 8MP](https://youtu.be/bpzGN35oaJ4?si=rX-MXX4XT5EObkdQ) — Primary visual guide used for hardware assembly, camera configuration, and prototype setup.
2. [OpenCV Face Recognition Documentation](https://docs.opencv.org/4.x/da/d60/tutorial_face_main.html) — Reference for LBPH face recognizer implementation.
3. [Flask Documentation](https://flask.palletsprojects.com/) — Reference for building the web server and HTTP routes.
4. [RPi.GPIO Documentation](https://pypi.org/project/RPi.GPIO/) — Reference for GPIO pin control and relay switching.
5. [Picamera2 Documentation](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf) — Reference for camera capture and configuration.

---

## 📊 Assessment Rubric

> ⚠️ **Students: Do NOT modify this section.**

### 📝 T1 — 50 Marks

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Needs Improvement (2) | Incomplete (0-1) | Marks |
|---|---|---|---|---|---|---|
| Project Proposal & Problem Statement | Clear, detailed, well-researched | Clear with minor gaps | Stated but lacks depth | Vague | Not submitted | /5 |
| System Design & Architecture | Detailed diagram + design decisions | Good diagram with some docs | Basic diagram | Incomplete | Not submitted | /5 |
| Hardware Component Selection | All justified with images | Most documented | Listed not justified | Incomplete | Not attempted | /5 |
| Circuit Diagram / Wiring | Complete + pin mapping | Mostly complete | Partial | Incomplete | Not submitted | /5 |
| GitHub Repository Setup | Well-structured, clear commits | Good with minor issues | Basic structure | Minimal | Repo not set up | /5 |
| Markdown Documentation Quality | Excellent: headings, tables, images, code | Good with minor issues | Basic Markdown | Minimal | None | /5 |
| GitHub Commit History (T1) | Regular commits, all members | Regular, most members | Some commits | Few | None | /5 |
| Initial Code / Prototype | Working + well-commented | Working + some comments | Partial prototype | Started, not working | None | /5 |
| Group Collaboration Evidence | Issues, PRs, commits from all | Good evidence | Some evidence | Minimal | None | /5 |
| Build Progress Photos | Step-by-step + descriptions | Good photos | Photos, few descriptions | Few photos | None | /5 |
| | | | | | **T1 Total** | **/50** |

---

### 📝 T2 — 50 Marks

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Needs Improvement (2) | Incomplete (0-1) | Marks |
|---|---|---|---|---|---|---|
| Final Working Project | Fully functional | Mostly functional | Partially functional | Limited functionality | Not functional | /5 |
| Live Demonstration | Confident, all features | Good, minor issues | Core features shown | Partial/unclear | No demonstration | /5 |
| Testing & Results Documentation | All tests + analysis | Most documented | Some documented | Minimal | None | /5 |
| Code Quality & Comments | Clean, structured, fully commented | Good, most commented | Works, lacks comments | Messy/partial | None | /5 |
| Markdown Documentation Quality (T2) | Complete professional README | Good with minor gaps | Most sections filled | Incomplete | Minimal/none | /5 |
| GitHub Commit History (T2) | Consistent, all members | Good, most members | Some commits | Few | None | /5 |
| Challenges & Solutions | All documented with solutions | Most documented | Some documented | Vague | Not documented | /5 |
| System Architecture (Final) | Updated, matches build | Mostly matches | Partially updated | Outdated | Not present | /5 |
| Presentation Quality | Professional, all members | All contribute | Acceptable | Weak/incomplete | None | /5 |
| References & Attribution | All properly listed | Most listed | Some listed | Minimal | None | /5 |
| | | | | | **T2 Total** | **/50** |

---

### 🏆 Final Mark Summary

| Term | Marks Available | Marks Achieved |
|---|---|---|
| T1 | 50 | /50 |
| T2 | 50 | /50 |
| **Total** | **100** | **/100** |

---

> 📌 **Assessed by:** `[Lecturer Name]`
> 📅 **Final Submission Deadline:** End of April 2026
> 🏫 **Institution:** Cape Peninsula University of Technology (CPUT)

---

*Documented using Markdown on GitHub — CPUT IT Diploma IoT Elective 2026 🚀*

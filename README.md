# Motion-Sensitive-CCTV

A security system that triggers video recording when motion is detected using an Arduino proximity sensor and Python-based video capture.

## Features
- Real-time motion detection with proximity sensor
- Automatic video recording on trigger
- Serial communication between Arduino & Python
- Organized video storage in `outputs/` directory
- Adjustable recording duration
- Multiple video file management

## Hardware Requirements
- Arduino Uno/Nano
- HC-SR04 Ultrasonic Sensor (or similar proximity sensor)
- USB cable for Arduino
- Webcam (built-in or external)
- Jumper wires

## Software Requirements
- Arduino IDE
- Python 3.8+
- OpenCV (`pip install opencv-python`)
- PySerial (`pip install pyserial`)

## Installation
1. Clone Repository
2. Install Python dependencies:
   - use "pip install -requirements.txt"

## Hardware Setup
1. Connect proximity sensor to Arduino:
   
   - VCC → 5V
   - GND → GND
   - TRIG → Digital Pin 9
   - ECHO → Digital Pin 10
3. Connect Arduino to computer via USB
4. Upload the trigger code from "trigger code" folder to the arduino after making relevant changes depending on your system

## Usage
1. Create outputs directory:
2. Run Python script:
3. System will:
   - Monitor serial port for triggers
   - Start 10-second recording on detection
   - Save videos as `outputs/video_1.mp4`, `video_2.mp4`, etc.
   - Show live preview during recording

## Troubleshooting
1. **Serial Port Issues**:
   - Check port name in `serial.Serial()` call
   - Ensure no other program is using the port
2. **Video Saving Problems**:
   - Verify `outputs/` directory exists
   - Check write permissions
3. **Sensor False Positives**:
   - Adjust `safetyDistance` in Arduino code
   - Modify debounce delay


## Contributing
Contributions welcome! Please:
1. Fork the repository
2. Create your feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request

---

**Test the System**: Wave your hand in front of the sensor to trigger recording. Check `outputs/` directory for captured videos.






import serial
import cv2
import time

# Open the serial port for communication with Arduino
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)  # Use the usb port you connected your ardiuno to 
time.sleep(2)  # Give the connection time to establish

def record_video(duration=10, output_file=r'outputs/output.mp4'):
    # Notify Arduino that recording has started
    arduino.write(b'BUSY\n')
    
    # Open the webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open video device.")
        arduino.write(b'DONE\n')  # Notify Arduino recording is finished if error occurs
        return
    
    # Get the video codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    start_time = time.time()
    
    while int(time.time() - start_time) < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow('Recording...', frame)

            # Press 'q' to stop early
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release the camera and video file writer
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # Notify Arduino that recording has finished
    #arduino.write(b'DONE\n')

# Main loop to listen for the trigger
video_count = 1
while True:
    data = arduino.readline().decode('utf-8').strip()
    
    if data == "TRIGGER":
        print(f"Proximity Triggered! Starting recording video_{video_count}.mp4")
        record_video(output_file=f'outputs/video_{video_count}.mp4')  # Record for 2 minutes
        print("Recording complete.")
        video_count += 1

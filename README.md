# Virtual Mouse Using Hand Gestures

A computer vision project that enables touchless mouse control using hand gestures.

## Features

* Real-time hand tracking using MediaPipe
* Mouse cursor control using index finger movement
* Left-click gesture using thumb and index finger
* Smooth cursor movement with interpolation
* Webcam-based interaction

## Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
* NumPy

## How It Works

1. Detects 21 hand landmarks using MediaPipe.
2. Tracks the index finger tip position.
3. Maps camera coordinates to screen coordinates.
4. Controls the system cursor in real time.
5. Detects pinch gestures for mouse clicks.

## Future Enhancements

* Right-click gesture
* Scrolling support
* Drag-and-drop functionality
* FPS counter
* Gesture customization

## Author

Keerthi Reddy

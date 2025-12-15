📌 XamGuard

XamGuard is a lightweight, experimental exam proctoring prototype that uses computer vision and optical flow to detect suspicious head movements and multiple people during online examinations.

This project is intended as a proof of concept, not a production-ready system.

🚀 Features

  1. Real-time face detection using OpenCV Haar Cascades
  2. Optical flow–based head movement tracking

  3. Detection of:
      a. Excessive head movement
      b. Multiple people in frame
      c. Face absence from camera
      d. Works with a standard webcam

  4. Single-file implementation for simplicity

🧠 How It Works (High Level)

  1. Captures webcam frames
  2. Detects face(s) in each frame
  3. Tracks horizontal head movement using Farneback Optical Flow
  4. Accumulates left/right movement
  5. Flags suspicious behavior based on thresholds

🛠️ Requirements

  1. Python 3.8+
  2. OpenCV
  3. NumPy

⚠️ Limitations
This project has known limitations:

  1. Uses Haar cascades (less robust than modern face detectors)
  2. Optical flow noise under poor lighting
  3. Thresholds are heuristic-based
  4. No identity verification
  5. No logging or reportin

🧪 Project Status

🟡 Early-stage / Experimental
This project is meant for:

  a. Learning
  b. Research
  c. Community feedback
  d. Feature exploration

🤝 Contributions & Suggestions

Contributions, ideas, and feedback are very welcome!
Feel free to open an issue, suggest enhancements, submit a pull request

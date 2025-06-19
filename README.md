# 🚗🤖 Hand Gesture Controller 🤖🚗

![Project Banner](https://res.cloudinary.com/dqtm454x4/image/upload/v1750326722/Screenshot_2025-06-19_151551_hd1hle.png)

## ✨ Features

- 👆 Real-time hand gesture recognition  
- 🎮 Seamless integration with racing games  
- 🖐️ Simple controls: 1 finger for brake, 4+ fingers for gas  
- 🎨 Beautiful visual feedback with transparent overlays  
- ⚡ Optimized performance with MediaPipe

## 🛠️ Technologies Used

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  ![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)  ![MediaPipe](https://img.shields.io/badge/MediaPipe-4285F4?style=for-the-badge&logo=google&logoColor=white)  ![PyDirectInput](https://img.shields.io/badge/PyDirectInput-306998?style=for-the-badge&logo=python&logoColor=white)

</div>

## 🚀 Getting Started

### Prerequisites

- Python 3.7+  
- Webcam

### Installation

1. Clone the repository  
```bash
git clone https://github.com/yourusername/hand-gesture-car-controller.git
cd hand-gesture-car-controller
```
Install dependencies

```bash
pip install -r requirements.txt
Run the application
```
```bash
python hand_controller.py
```
### 🎮 How to Use
✋ Hold up 1 finger (or a closed fist) to activate BRAKE (← key)

✋ Hold up 4 or 5 fingers to activate GAS (→ key)

❌ Press 'q' to quit the application

### 🧠 How It Works
```mermaid
graph TD
    A[Webcam Feed] --> B[Hand Detection]
    B --> C[Landmark Processing]
    C --> D[Gesture Classification]
    D --> E{Number of Fingers}
    E -->|1| F[Press Brake]
    E -->|4-5| G[Press Gas]
    E -->|Other| H[No Action]
```
### 🌟 Contributors
<table> <tr> <td align="center"> <a href="[https://github.com/yourusername](https://github.com/vermaarpit14)"> <img src="https://userpic.codeforces.org/3984400/title/835cab873191b409.jpg" width="100px;" alt=""/> <br /> <sub><b>Arpit Verma</b></sub> </a> </td> </tr> </table>

### 📜 License
MIT License

### 🙏 Acknowledgments
MediaPipe team

OpenCV community

<div align="center"> Made with ❤️ and Python </div>

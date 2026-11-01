# 🚗 Smart Parking Space Detection

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white) ![OpenCV](https://img.shields.io/badge/OpenCV-Image%20Processing-5C3EE8?logo=opencv&logoColor=white)

An OpenCV project that estimates **free and occupied parking spaces** in a recorded parking-lot video. Parking spots are marked manually once; the program then processes each frame and displays an updated count of available spaces.

The project uses a simple image-processing approach rather than a trained object detection model.

## 🅿️ How it works

1. **Extract a frame** from the parking video to use as a reference image.
2. **Select parking spaces** with mouse clicks and save their positions to `CarParkPos`.
3. **Process each frame** using grayscale conversion, Gaussian blur, adaptive thresholding, and median blur.
4. **Check each marked area** by counting nonzero pixels and comparing the count with a fixed threshold.
5. **Display the result** using green/red rectangles and a `Free: X/Y` counter.

## 📷 Input example

![Parking lot reference frame](Video%20%26%20Image%20Data/parking5.jpg)

## 📂 Project structure

```text
├── SaveOneFrameAsPicture.py
├── FindingCoordinates.py
├── CountingParking.py
├── CarParkPos
└── Video & Image Data/
    ├── parking5.jpg
    └── parking5.mp4
```

## ⚙️ Running the project

```bash
git clone https://github.com/YasiNoshirvan/Smart-Parking-Space-Detection-by-Image-Processing.git
cd Smart-Parking-Space-Detection-by-Image-Processing
pip install opencv-python numpy
```

**Before running:** The uploaded Python files still contain local `D:/Training Image Processing/...` paths. Update the video references in `SaveOneFrameAsPicture.py` and `CountingParking.py` to `Video & Image Data/parking5.mp4`, and the image references in `SaveOneFrameAsPicture.py` and `FindingCoordinates.py` to `Video & Image Data/parking5.jpg`.

For example, in `CountingParking.py`:

```python
cap = cv2.VideoCapture('Video & Image Data/parking5.mp4')
```

Run from the repository directory so that `CarParkPos` can be found:

```bash
python CountingParking.py
```

To change the marked parking spaces, run `FindingCoordinates.py` first. **Left-click** to add a space and **right-click** to remove one. The current `FindingCoordinates.py` closes with **Q**, while `CountingParking.py` closes with **Esc**.

## ⚠️ Limitations

Parking-space coordinates, rectangle dimensions, and the pixel-count threshold are manually set for this camera view. Lighting, shadows, and changes in camera position can affect the result. This is an educational prototype, not a validated parking management system.

---

*Built to explore region-based video analysis and practical image-processing workflows.*

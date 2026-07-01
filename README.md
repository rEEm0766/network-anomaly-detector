# Network Anomaly Detector

## Overview
This project is a Flask-based web application that detects abnormal network traffic using the Isolation Forest Machine Learning algorithm.

## Features
- Detects anomalous network traffic
- Flask web interface
- Machine Learning model using Isolation Forest
- User-friendly input form
- Real-time prediction

## Technologies Used
- Python
- Flask
- Scikit-learn
- NumPy
- Pandas
- HTML

## Project Structure

```
network-anomaly-detector/
│
├── app.py
├── train.py
├── requirements.txt
├── models/
├── templates/
└── README.md
```

## How to Run

```bash
pip install -r requirements.txt
python train.py
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## Sample Inputs

| Packet Size | Duration | Protocol | Result |
|-------------|----------|----------|--------|
| 500 | 2 | 1 | Normal Traffic |
| 5000 | 50 | 2 | Anomaly Detected |

## Future Improvements

- Real network packet capture
- Deep Learning models
- Interactive dashboard
- Live traffic monitoring

# Smart Irrigation

A simple Flask web dashboard for monitoring soil moisture, temperature, humidity, and rain detection, and for controlling a water pump.

## 🚀 Features

- Live dashboard showing:
  - Soil moisture (%)
  - Temperature (°C)
  - Humidity (%)
  - Rain status (Yes/No)
  - Pump status (ON/OFF)
- Auto-refreshes sensor and pump state every 2 seconds
- Manual pump control via UI buttons
- Simple AI logic to automatically turn pump ON/OFF based on sensor values

## 🧰 Requirements

- Python 3.8+ (recommended)
- `pip` for installing dependencies

## 🏁 Getting Started

```bash
cd /path/to/smart_irrigation
python -m venv .venv
.\.venv\Scripts\activate   # Windows
# source .venv/bin/activate # macOS/Linux
pip install flask flask-cors
python server.py
```

Then open:

- http://127.0.0.1:5000/

## 🧩 Files

- `server.py` – Flask server logic and API endpoints
- `templates/index.html` – Frontend dashboard UI
- `static/` – place for JS/CSS/assets (currently unused)

## 🔧 Notes

- The server runs in debug mode by default for rapid development.
- The AI logic uses sensor values to decide pump state and resets on each sensor update.

## 📄 License

This project is open-source and free to use.

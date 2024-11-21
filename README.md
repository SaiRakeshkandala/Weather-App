# 🌦️ Weather App ⛅

Welcome to the **Weather App**! This app fetches and displays real-time weather information for any city in the world 🌍. With both **CLI** and **GUI** interfaces, it's a simple yet powerful tool to check the weather at your fingertips! 💻📱

---

## 🌟 Features

✨ **Real-Time Data**: Fetch accurate and up-to-date weather details.  
🌡️ **Key Weather Metrics**: Get temperature, humidity, and weather description.  
💨 **Extra Details**: Includes wind speed, sunrise, and sunset times.  
⚡ **Two Modes**: Choose between **CLI** (Command Line Interface) and **GUI** (Graphical User Interface).  
🌈 **Error Handling**: Handles invalid city names and API issues gracefully.  

---

## 🛠️ Installation and Setup

Follow these steps to set up the Weather App on your system:

1. **Clone the Repository** 🐙:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```

2. **Install Dependencies** 📦:
   Use `pip` to install the required libraries.
   ```bash
   pip install -r requirements.txt
   ```

3. **Get Your API Key** 🔑:
   - Sign up at [OpenWeatherMap](https://openweathermap.org/) and get your free API key.
   - Replace `"your_api_key"` in the `main.py` file with your actual API key.

4. **Run the App** 🚀:
   ```bash
   python main.py
   ```

---

## 🧭 Usage Guide

When you run the app, you’ll have two options:

1️⃣ **CLI Mode**:  
   Enter the city name directly in the terminal to fetch weather data. 🌃  

2️⃣ **GUI Mode**:  
   A simple and clean graphical interface to enter the city name and view the results. ![image](https://github.com/user-attachments/assets/f62bede6-231d-4a4b-aa70-52c78b411d01)


---

## 📂 Project Structure

```
weather-app/
│
├── weather_app/
│   ├── __init__.py         # Package initialization
│   ├── api.py              # Handles API integration
│   ├── cli.py              # Command Line Interface implementation
│   ├── gui.py              # Graphical User Interface implementation
│
├── main.py                 # Entry point of the application
├── requirements.txt        # Required Python libraries
└── README.md               # Project documentation
```

---

## 🖼️ Screenshots

### 🌟 CLI Mode:
```
Welcome to the Weather App!
1. CLI Mode
2. GUI Mode
Choose a mode (1 for CLI, 2 for GUI): 1

Enter city name (or 'exit' to quit): New York
City: New York
Temperature: 15°C
Humidity: 65%
Weather: clear sky
Wind Speed: 5 m/s
Sunrise: 06:23:00
Sunset: 18:11:00
```

### 🖼️ GUI Mode:
![GUI Screenshot Placeholder](https://via.placeholder.com/400x300.png?text=GUI+Weather+App)

---

## ✨ Future Enhancements

- 🌍 **Predefined City Dropdown**: Add a dropdown menu for commonly searched cities.  
- 💾 **Save History**: Allow users to save weather data for offline use.  
- 🖌️ **Custom Themes**: Add theme options for the GUI.  

---

## ⚠️ Known Issues

- Internet connection is required 🌐.  
- Free API keys might have a limit on daily requests. 🔑  

---

## 🤝 Contributing

We welcome contributions! 🛠️  
1. Fork this repository 🍴  
2. Create a new branch 🔀  
3. Submit a pull request 📬  

---

## 📜 License

This project is licensed under the **MIT License**. 📄 Feel free to use, modify, and share it!  

---

## 🌟 Acknowledgments

Special thanks to [OpenWeatherMap](https://openweathermap.org/) for providing the weather data. 🌦️  

---

## 🔗 Links

- [OpenWeatherMap API](https://openweathermap.org/) 🌐  
- [GitHub Repository](https://github.com/yourusername/weather-app) 🐙  

---

Made with ❤️ and ☕ by your friendly neighborhood developer. 🌟

---

Feel free to replace the placeholder link for screenshots and adjust emojis to your liking! 😊

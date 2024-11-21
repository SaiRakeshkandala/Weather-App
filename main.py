from weather_app.cli import cli_mode
from weather_app.gui import gui_mode

if __name__ == "__main__":
    api_key = "your_api_key"  # Replace with your OpenWeatherMap API key

    print("Welcome to the Weather App!")
    print("1. CLI Mode")
    print("2. GUI Mode")
    
    choice = input("Choose a mode (1 for CLI, 2 for GUI): ").strip()
    if choice == "1":
        cli_mode(api_key)
    elif choice == "2":
        gui_mode(api_key)
    else:
        print("Invalid choice. Exiting.")

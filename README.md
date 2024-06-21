# Alarm

## Python Alarm Clock Application

### Overview

The Python Alarm Clock Application is a simple desktop program designed to set and manage alarms. Built using Python's Tkinter library for the graphical user interface (GUI) and pyttsx3 for text-to-speech functionality, this application provides a user-friendly experience for setting alarms that notify you with both a message and a voice alert.

### Features

- **User-Friendly Interface**: Easy-to-use GUI for setting alarm times.
- **Time Validation**: Ensures the user enters a valid time in HH:MM format.
- **Background Alarm Check**: Uses threading to continuously check the current time against the set alarm time without freezing the GUI.
- **Audio Notification**: Utilizes the pyttsx3 library to announce the alarm time, alerting the user with a "Time to wake up" message.
- **Visual Notification**: Displays a message box to inform the user when the alarm time is reached.

### Installation

1. **Clone the Repository**:
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```sh
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

### Usage

1. **Run the Application**:
   ```sh
   python alarm_clock.py
   ```

2. **Set the Alarm**:
   - Enter the desired alarm time in the HH:MM format in the input field.
   - Click the "Set Alarm" button.

3. **Alarm Notification**:
   - When the current time matches the set alarm time, the application will notify you with an audio message "Time to wake up" and display a message box.

### Requirements

- **Python 3.x**
- **Tkinter**: This comes pre-installed with Python.
- **pyttsx3**: For text-to-speech functionality.

### Dependencies

The project dependencies are listed in the `requirements.txt` file:


Install them using:

pip install -r requirements.txt

### Code Structure

- **alarm_clock.py**: Main script containing the GUI setup, alarm logic, and validation functions.
- **requirements.txt**: File listing the necessary Python packages.

### Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

### License

This project is licensed under the MIT License.


# Keyboard Event Logger

A simple Python-based keyboard event logger built using `tkinter`.
This project records key presses **only inside the application window** and stores them in a log file.

> ⚠️ This project is created for educational purposes only.
> It does **not** capture global system keystrokes and should only be used with user consent.

---

## Features

* Detects keyboard input inside the app window
* Displays the last key pressed
* Saves key events with timestamps
* Simple GUI using `tkinter`
* File handling in Python

---

## Technologies Used

* Python 3
* Tkinter (GUI Library)

---

## Project Structure

```plaintext
keyboard-event-logger/
│
├── app.py
├── key_log.txt
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
https://github.com/SoumiBandyopadhyay/PRODIGY_CS_04
```

### 2. Navigate to the Project Folder

```bash
cd keyboard-event-logger
```

### 3. Run the Program

```bash
python app.py
```

---

## Example Output

Contents of `key_log.txt`:

```plaintext
2026-05-26 10:15:20 - a
2026-05-26 10:15:22 - Return
2026-05-26 10:15:25 - space
```

---

## How It Works

* The application creates a GUI window using `tkinter`
* Keyboard events are captured using:

```python
root.bind("<Key>", log_key)
```

* Each pressed key is:

  * displayed on screen
  * saved to `key_log.txt`

---

## Learning Concepts

This project helps understand:

* Event handling in Python
* GUI development
* File operations
* Logging systems
* Python functions and callbacks

---

## Ethical Notice

This project is intentionally limited to logging keys only inside its own application window.
Creating software that secretly captures system-wide keystrokes without permission is unethical and may be illegal.

Always obtain proper consent before collecting user input data.

---

## License

This project is licensed under the MIT License.

---
Author
---
Soumi Bandyopadhyay

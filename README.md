# 🔐 Password Generator - By Manan

A secure and customizable password generator built using Python.

This project generates strong random passwords while allowing users to control the password length and character types used.

## 🚀 Features

* 🔒 Secure password generation using Python's `secrets` module
* 🎲 Randomized password order using `random.shuffle()`
* 🔢 Generate multiple passwords at once
* 📏 Custom password length selection
* 🔤 Choose character types:

  * Lowercase letters
  * Uppercase letters
  * Numbers
  * Special characters
* 📊 Password strength estimation
* ⚠️ Input validation for invalid choices
* 💻 Available as a standalone `.exe` application

## 🛡️ Security

This project uses:

* `secrets.choice()` for generating password characters

The `secrets` module is designed for security-sensitive applications and is more suitable than `random.choice()` for password generation.

`random.shuffle()` is only used after generation to randomize the final password arrangement.

## 🖥️ Preview

Terminal-based password generator with a clean interface:
<img width="1102" height="556" alt="Screenshot 2026-07-08 060300" src="https://github.com/user-attachments/assets/c11ae967-6520-45f0-943e-fa35751f7bb6" />

<img width="1099" height="560" alt="Screenshot 2026-07-08 060322" src="https://github.com/user-attachments/assets/5217a68a-08a4-4ee8-9d7a-1ffcf4b710f7" />

<img width="1097" height="553" alt="Screenshot 2026-07-08 060353" src="https://github.com/user-attachments/assets/68961c55-f8f2-4caa-ad74-cedd82b946a4" />

<img width="1106" height="554" alt="Screenshot 2026-07-08 060528" src="https://github.com/user-attachments/assets/bc96ec92-77a7-475d-949b-39cfd61d4134" />

## ⚙️ Installation

### Run using Python

Make sure Python is installed.

Clone this repository:

```bash
git clone https://github.com/yourusername/Password-Generator.git
```

Navigate into the folder:

```bash
cd Password-Generator
```

Run:

```bash
python password_generator.py
```

### Run without Python

Download and run:

```
Password_Generator.exe
```

No Python installation required.

## 📦 Requirements

* Python 3.x

External libraries:

* None currently

## 🛠️ Future Improvements

* 📋 Copy passwords automatically to clipboard
* 🎨 Add terminal colors using Colorama
* 🖥️ Create a GUI version using Tkinter
* 📦 Improve executable distribution
* 🌐 Create a web version

## 👨‍💻 Author

**Manan**

Python Class 12 Computer Science Project

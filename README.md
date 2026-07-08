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

```
=============================================
🔐  PASSWORD GENERATOR  🔐
       Created by Manan
=============================================

🔢 Number of passwords you want >>>
📏 Password length >>>
```

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

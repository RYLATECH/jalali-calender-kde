# 🗓️ Jalali Tray Indicator  
> Minimal. Clean. Persian. 🇮🇷

---

<img width="193" height="132" alt="image" src="https://github.com/user-attachments/assets/2b098759-4f92-4174-adee-7fd65516d32b" />

---

## ✨ Overview

A tiny system tray app that shows the **Jalali (Persian) date** directly in your panel.

No clutter. No heavy UI.  
Just the date — right where you need it.

---

## ⚡ Features

- 🟢 Shows **current day** (like `19`) in system tray  
- 🖱 Click → full date: `19 Tir 1405`  
- 🔄 Auto-updates every day  
- 🧩 Works on **KDE & GNOME**  
- 🪶 Super lightweight  

---

## 📸 Demo

![demo](./assets/demo.png)

---

## 🚀 Getting Started

### 🔹 Clone

git clone https://github.com/your-username/jalali-tray.git  
cd jalali-tray

---

### 🔹 Setup venv

python -m venv venv  
source venv/bin/activate

---

### 🔹 Install deps

pip install -r requirements.txt

---

### 🔹 Run

python main.py

---

## ⚙️ Autostart (KDE/GNOME)

Create this file:

~/.config/autostart/jalali-tray.desktop

```
[Desktop Entry]
Type=Application
Exec=/home/YOUR_USERNAME/jalali-tray/venv/bin/python /home/YOUR_USERNAME/jalali-tray/main.py
Name=Jalali Tray
X-KDE-autostart-enabled=true
```

---

## 🧠 Why this exists?

Because:

- KDE was being weird with indicators 😑  
- No simple Jalali tray app existed  
- I just wanted **the date. nothing more.**

So yeah… I built it 💀

---

## 🛣️ Roadmap

- [ ] 🎨 Better icon (adaptive for dark/light)
- [ ] 🌙 Theme detection
- [ ] 📅 Holidays support
- [ ] 📦 AUR package

---

## 🤝 Contribute

PRs are welcome.  
Ideas? Even better 😏

---

## ⭐ Support

If you liked it, give it a star ⭐  

---

## 📜 License

MIT

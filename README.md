# 📂 File Organizer with Custom Logger

A simple Python utility that automatically **organizes files by their extensions** into separate folders (for example: `png_files`, `pdf_files`) and logs all actions.

## 🚀 Features
- Organizes files based on extension
- Auto-creates folders if missing
- Logs to:
  - 📄 File
  - 🖥 Console
  - 🌐 Discord webhook
- Supports emojis & UTF-8 logging

## 🛠 Tech Stack
- Python 3
- os, shutil, logging
- requests (for Discord webhook)

## ▶️ How to Run
```bash
python main.py
```
Enter the folder path when prompted.

## 📜 Logs
Logs are stored at:
```
files/folder_scanning_logger.log
```

## 📌 Example Output
```
png_files/
pdf_files/
txt_files/
```

## ✅ Use Case
Ideal for practicing:
- File handling
- Logging
- Custom logging handlers
- Python project structuring

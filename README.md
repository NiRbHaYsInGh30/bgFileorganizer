# BG File Organizer

BG File Organizer is a Python script that automates the organization of downloaded files based on their type (audio, video, image, document). It continuously monitors a designated download directory (`source_dir`) and moves newly downloaded files to appropriate subdirectories within the same directory structure.

## Features

- **File Type Classification:** Categorizes files using predefined extensions for audio, video, images, and documents.
- **Subdirectory Creation:** Creates subdirectories within the download directory to organize files.

## Setup

### 1. Clone or Download Script

Obtain the script [here](https://github.com/NiRbHaYsInGh30/bgFileorganizer).

### 2. Set Download Directory

Modify the `source_dir` variable at the beginning of the script to point to your download directory. Replace `C:\Users\LENOVO\Downloads` with your path.

### 3. Customize Subdirectories (Optional)

Adjust the names of the subdirectories (`dest_dir_sfx`, `dest_dir_music`, etc.) to match your preferences.

### 4. Install Watchdog

If you haven't already, install the `watchdog` library:

```bash
pip install watchdog

BG File Organizer
BG File Organizer is a Python script that automates the organization of downloaded files based on their type (audio, video, image, document). It continuously monitors a designated download directory (source_dir) and moves newly downloaded files to appropriate subdirectories within the same directory structure.

Features
File Type Classification: Categorizes files using predefined extensions for audio, video, images, and documents.
Subdirectory Creation: Creates subdirectories within the download directory to organize files.
Setup
1. Clone or Download Script
Obtain the script here.

2. Set Download Directory
Modify the source_dir variable at the beginning of the script to point to your download directory. Replace C:\Users\LENOVO\Downloads with your path.

3. Customize Subdirectories (Optional)
Adjust the names of the subdirectories (dest_dir_sfx, dest_dir_music, etc.) to match your preferences.

4. Install Watchdog
If you haven't already, install the watchdog library:

bash
Copy code
pip install watchdog
Usage
1. Save Script
Save the script as a Python file (e.g., bg_organizer.py).

2. Run Script
Execute the script from your terminal or command prompt:

bash
Copy code
python bg_organizer.py
Building the Executable
1. Install PyInstaller
Open your terminal or command prompt and run:

bash
Copy code
pip install pyinstaller
2. Navigate to Your Script's Directory
Use the cd command to navigate to the directory where your Python script (e.g., bg_organizer.py) is located.

3. Build the Executable
Run the following command, replacing bg_organizer.py with the actual name of your script:

bash
Copy code
pyinstaller --onefile bg_organizer.py
4. Locate the Executable
PyInstaller will create a new directory named dist within your script's directory. The executable file will be located inside this dist folder.

Running the Executable
Once you have the executable, you can double-click it on Windows or run it from the command line on other operating systems (e.g., ./bg_organizer on Linux/macOS). This will execute your Python script without the need for a separate Python installation.

Screenshots
Subdirectory Paths


Running the Executable


Click on the EXE File

# This Python script automates the organization of downloaded files based on their type (audio, video, image, document). It continuously monitors a designated download directory (source_dir) and moves newly downloaded files to appropriate subdirectories within the same directory structure.


# Features:

File Type Classification: Categorizes files using predefined extensions for audio, video, images, and documents.
Subdirectory Creation: Creates subdirectories (dest_dir_sfx, dest_dir_music, dest_dir_video, dest_dir_image, dest_dir_documents) within the download directory to organize files.
Add your dir path here in which you want to sort i

Clone or Download Script: Obtain the script (e.g., bg_organizer.py).
Set Download Directory: Modify the source_dir variable at the beginning of the script to point to your download directory (replace C:\Users\LENOVO\Downloads with your path).
Customize Subdirectories (Optional): If desired, adjust the names of the subdirectories (dest_dir_sfx, dest_dir_music, etc.) to match your preferences.
Install watchdog: If you haven't already, install the watchdog library using pip install watchdog in your terminal or command prompt.

Then add the path of your sub dir here in the code
![image](https://github.com/NiRbHaYsInGh30/bgFileorganizer/assets/90407590/f0dc1106-92db-4efe-a53f-007dd742712d)


# Usage:

Save Script: Save the script as a Python file (e.g., bg_organizer.py).
Run Script: Execute the script from your terminal or command prompt using python bg_organizer.py.

Building the script
. 
Install PyInstaller:

Open your terminal or command prompt and run the following command:

pip install pyinstaller

 Navigate to Your Script's Directory:

Use the cd command to navigate to the directory where your Python script (e.g., bg_organizer.py) is located.

#3. Build the Executable:

Run the following command in your terminal, replacing bg_organizer.py with the actual name of your script:


pyinstaller --onefile bg_organizer.py

 Locate the Executable:

PyInstaller will create a new directory named dist within your script's directory. The executable file will be located inside this dist folder.

Running the Executable:

Once you have the executable, you can double-click it on Windows or run it from the command line on other operating systems (e.g., ./bg_organizer on Linux/macOS). This will execute your Python script without the need for a separate Python 


![image](https://github.com/NiRbHaYsInGh30/bgFileorganizer/assets/90407590/d7b09146-a89a-4acf-a182-a404cc5fd111)


Click on the exe file to run it

![image](https://github.com/NiRbHaYsInGh30/bgFileorganizer/assets/90407590/ee3ad9d8-b53d-439d-bbb5-6459b046f5c8)

# install pytube first Using pip install pytube command
from pytube import YouTube
from sys import argv

# command line arg passed
link = argv[1]
yt = YouTube(link)

# for printing views and title
print("Title: ", yt.title)
print("View: ", yt.views)

# for getting the highest resolution
yd = yt.streams.get_highest_resolution()

# ADD FOLDER HERE
yd.download('C:\\Users\\LENOVO\\OneDrive\\Desktop\\coding\\PythonAutomationScripts\\Downloads')
 

# MediaManager
Scripts to help manage a master list of .m4v movies across multiple users

# Requirements 
MediaManager requires Python 3.x to run

# Usage
Media Manager has two modes it :

1. Catalog Mode - creates a text file of local media files found
Command: python MediaManager.py <folder containing media> <name of file to create>

2. Catalog and Compare Mode - creates text file of local media files found AND compares it to another media text file.  
Command: python MediaManager.py <folder containing media> <name of file to create> <name of media file to compare to>
*note that to make this easy, you can simply copy the file to compare to into the same directory that Media Manager is running in

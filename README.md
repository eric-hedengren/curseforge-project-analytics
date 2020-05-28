# Curse Forge Project Analytics
Simple Matplotlib program that plots data from [Curse Forge Analytics](https://authors.curseforge.com/dashboard/projects). If you're a author on Curse Forge, your projects should appear at that link. [Click here](https://www.curseforge.com/project/create "Create a Curse Forge Project") if you don't see any projects and would like to make your own.

## Getting Started
### 1. Python Install
If python is already on your computer, skip this step. First get the [Latest Python Files](https://www.python.org/downloads/ "Python Download"). When opening the installer, make sure you select "Add Python -version- to PATH". If you don't have admin access, unselect "Install launcher for all users (recommended)", it will still work on your user.

### 2. Python Packages
Additionally, you may have to install the [pandas](Analytics/Analytics.pyw#L1) and [matplotlib](Analytics/Analytics.pyw#L2) packages if you haven't before (if you don't know what these are, you probably haven't) so run the [InstallPythonPackages.bat](Analytics/Run/InstallPythonPackages.bat) file and it will install them for you. You need python installed for that file to run, and you know it's working when multiple loading bars appear on the command prompt. These first 2 steps are only required once for each new computer. If you know you have previously installed these packages, skip to step 3.

### 3. Using Your Mod Stats
The files in [Mod Name/Data](Analytics/Data "Data Folder") and [Mod Name/Graphs](Analytics/Graphs "Graphs Folder") are just example files from my personal Curse Forge projects. To customize graphs to your own data, go to the [Curse Forge Analytics](https://authors.curseforge.com/dashboard/projects) site, and download the stats of the projects you would like to analyze. Put the downloaded files in the "Data Folder" on your desktop, and delete the example data, as well as the previously created graphs located in the "Graphs Folder".

### 4. Running the Graph Generator
To create a graph, use the [RunGraphGenerator.bat](Analytics/Run/RunGraphGenerator.bat), or [Analytics.pyw](Analytics/Analytics.pyw), and using either of these require steps 1 and 2. Your graph(s) should save to the "Graphs Folder", which uses the most recent project files in the "Data Folder". If this step fails to execute, try uninstalling then reinstalling python and the packages from your computer.

### 5. Adding More Data
If you don't want to delete your old data files, simply copy the new data into your Data Folder and the Analytics file will only create new graphs for the lastest project data. The Analytics file automatically finds the latest files from different projects in your Data Folder, or the most recent one by date, so try not to rename your data files.

## Thanks for trying this out!
I hope this helps! Here are the [projects](https://www.curseforge.com/members/baconbombingdeveloper/projects "BaconBombingDeveloper Curse Forge Projects") that I used for example stats.

If you like this idea and think it should be integrated into the Curse Forge webpage, you can vote for the [feature request](https://twitch.uservoice.com/forums/915910-game-mods-curseforge/suggestions/40317994-plots-for-author-project-analytics "Vote on User Voice").

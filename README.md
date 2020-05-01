# CurseForgeModAnalytics
Simple Matplotlib program that plots data from [Curseforge Analytics](https://authors.curseforge.com/dashboard/projects)

## Getting Started
If python isn't on your computer, you can download it [here](https://www.python.org/downloads/ "Python Download").

You may have to install the [pandas](Mod%20Name/Analytics.py#L1) and [matplotlib](Mod%20Name/Analytics.py#L2) packages if you haven't before (if you don't know what these are, you probably haven't) so run the ["InstallPythonPackages.bat"](Mod%20Name/InstallPythonPackages.bat) file and it will install them for you. This is only required once for each new computer.

The files in [Mod Name/Graphs](Mod%20Name/Graphs "Graphs Folder") and [Mod Name/Data](Mod%20Name/Graphs "Data Folder") are just example files from my personal curseforge mod. To customize for your own data, go to the [Curseforge Analytics](https://authors.curseforge.com/dashboard/projects) site, and download the stats of the project you would like to analyze. Put the downloaded file in the "Data Folder" on your desktop, and delete the example data named "Standard Materials_overview_v1_START_DATE_END_DATE".
If you're adding new analytics, from a new day for example, the Analytics program [automatically finds the "latest" file](Mod%20Name/Analytics.py#L11), or the most recent one by date, so try not to rename your data files. 
Then double click the "Analytics.py" file, and if you have python installed, it should execute. If it doesn't excute, try right clicking the Analytics.py file and open with python. Alternatively, try running the DebugGraphGenerator.bat and it will run the python file through the command prompt (This still requires python).

## Debug Graph Generator Help
By default, the ["DebugGraphGenerator.bat"](Mod%20Name/DebugGraphGenerator.bat) file looks for your folder in your desktop. 
If you didn't move these downloaded files there, follow these instructions if you would like to debug your [Analytics.py](Mod%20Name/Analytics.py) file (only necessary if you're modifying Analytics.py). 
Edit the text file of DebugGraphGenerator.bat by changing the file from .bat to a .txt, it should look like this "DebugGraphGenerator.txt" and [change your directory](Mod%20Name/DebugGraphGenerator.bat#L1) to match where you put your downloaded github files. After you finish, change your extension name back from a .txt to .bat so it can execute.

## Naming Saved Graphs
The Analytics.py file, by default, names the new graph after the current date. If you want to change that, you can find it [here](Mod%20Name/Analytics.py#L40).

I hope this helps! Here's the [Example Mod (Standard Materials)](https://www.curseforge.com/minecraft/mc-mods/standardmaterials "Standard Materials CurseForge") that I used for example stats.

# Curse Forge Mod Analytics
Simple Matplotlib program that plots data from [Curseforge Analytics](https://authors.curseforge.com/dashboard/projects). If you're a author on curseforge, your projects should appear at that link. [Click here](https://www.curseforge.com/project/create "Create a CurseForge Project") if you don't see any projects and would like to make your own.

## Getting Started
### 1. Python Install

First get the [latest python files](https://www.python.org/downloads/ "Python Download"). If python is on your computer, skip this step.

### 2. Python Packages

Additionally, you may have to install the [pandas](Mod%20Name/Analytics.py#L1) and [matplotlib](Mod%20Name/Analytics.py#L2) packages if you haven't before (if you don't know what these are, you probably haven't) so run the [InstallPythonPackages.bat](Mod%20Name/Run/InstallPythonPackages.bat) file and it will install them for you. You need python installed for that file to run. These first 2 steps are only required once for each new computer. If you know you have previously installed these packages, skip this step.

### 3. Execute Graph Generator

To execute a graph, run the [RunGraphGenerator.bat](Mod%20Name/Run/RunGraphGenerator.bat), and this requires steps 1 and 2. A display graph should come up that displays the most recent file in the "Data Folder". If this step fails, try uninstalling then reinstalling python and the packages in steps 1 and 2 from your computer.

### 4. Using Your Mod Stats

The files in [Mod Name/Graphs](Mod%20Name/Graphs "Graphs Folder") and [Mod Name/Data](Mod%20Name/Graphs "Data Folder") are just example files from my personal curseforge mod. To customize for your own data, go to the [Curseforge Analytics](https://authors.curseforge.com/dashboard/projects) site, and download the stats of the project you would like to analyze. Put the downloaded file in the "Data Folder" on your desktop, and delete the example data named "Standard Materials_overview_v1_START_DATE_END_DATE", as well as the graph located in the "Graphs Folder".

### 5. Adding More Data

If you're adding new analytics, from a new day for example, the Analytics program automatically finds the ["latest file"](Mod%20Name/Analytics.py#L11-L12) in your Data Folder, or the most recent one by date, so try not to rename your data files. If you would like to analyze multiple projects, simply download these github files again for each mod or copy and paste the folder you already downloaded.

## Naming Saved Graphs
The Analytics.py file, by default, names the new graph after the current date. If you want to change that, you can find it [here](Mod%20Name/Analytics.py#L38).

## Thanks for trying this out!
I hope this helps! Here's the [Example Mod (Standard Materials)](https://www.curseforge.com/minecraft/mc-mods/standardmaterials "Standard Materials CurseForge") that I used for example stats.

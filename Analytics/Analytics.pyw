import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime
import numpy as np
import glob

def line(a, b, c): # Data, Color, Label
    plt.plot_date(dates, data[a], b, label = c)

def average(name):
    total = 0
    for i in data[name]:
        total += i
    return "%.2f" % (total/data[name].size)

def subplot(x, y):
    plt.ylabel(y)
    plt.legend(loc = 2) # Sets legend to top left
    plt.xlim([dates.values[0], dates.values[-1]]) # Tighten the x axis
    plt.ylim(0) # Start y axis stats at 0
    tick_frequency = int(dates.size/15) # Set tick frequency
    if tick_frequency < 1: # In case project has less than 15 data points
        tick_frequency = 1
    plt.xticks(np.arange(0, dates.size, tick_frequency)) # Start, stop, steps

project = glob.glob('Data/*')[-1]
data = pd.read_csv(project)
del data['Project ID'] # Delete unused columns

project_name = data['Name'][0]

dates = data['Date']

dates = pd.to_datetime(dates).dt.strftime('%y-%m-%d') # Format date data

plt.figure(figsize=(15,10)) # Create figure

plt.subplot(3,1,1) # Create subplots for the figure
plt.title(project_name) # Set title as project name
line('Historical Download','k','Total Downloads\n'+str(data['Historical Download'].values[-1]))
subplot(1, 'Total')

plt.subplot(3,1,2)
line('Daily Download','b','Total ' + average('Daily Download'))
line('Daily Unique Download','r','Unique ' + average('Daily Unique Download'))
line('Daily Curse Forge Download','g','Curse Forge ' + average('Daily Curse Forge Download'))
line('Daily Twitch App Download','#800080','Twitch App ' + average('Daily Twitch App Download'))
subplot(2, 'Daily Downloads + Average')

plt.subplot(3,1,3)
line('Points','#FFD700','Points\n' + average('Points'))
subplot(3, 'Points + Average')
plt.xlabel('Date')

plt.savefig('Graphs/'+project_name+' Analytics '+ project[project.index("_overview_v1_")+13 : len(project)-4] +'.png') # Save as image
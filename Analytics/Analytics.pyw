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
    return '(avg %.2f)' % (total/data[name].size)

def subplot(x, y, z):
    plt.title(z) # Set subplot title
    plt.ylabel(y)
    plt.legend(loc = 2) # Sets legend to top left
    plt.xlim([dates[0], dates.values[-1]]); plt.ylim(0) # Tighten the x/y axis
    tick_frequency = int(dates.size/15) # Set tick frequency
    if tick_frequency < 1: # In case the number is rounded to 0
        tick_frequency = 1
    plt.xticks(np.arange(0, dates.size, tick_frequency)) # Start, Stop, Steps

data_files = glob.glob('Data/*')
current_projects = []

for i, name in enumerate(data_files):
    if i == len(data_files)-1:
        current_projects.append(name)
        break
    next_name = data_files[i+1]
    if name[:name.index("_overview_v1_")] == next_name[:next_name.index("_overview_v1_")]:
        continue
    current_projects.append(name)

for current_file in current_projects:
    data = pd.read_csv(current_file)
    del data['Project ID']

    project_name = data['Name'][0]
    raw_dates = data['Date']
    dates = pd.to_datetime(raw_dates).dt.strftime('%y-%m-%d') # Format x axis date data

    plt.figure(figsize=(17,11))
    font_size = 50
    if len(project_name) > 40:
        font_size = 20
    plt.suptitle(project_name, fontsize=font_size)

    plt.subplot(3,1,2)
    line('Historical Download','k','Total Downloads\n'+str(data['Historical Download'].values[-1]))
    subplot(1, 'Downloads', 'Total')

    plt.subplot(3,1,1)
    line('Daily Twitch App Download','#800080','Twitch App '+ average('Daily Twitch App Download'))
    line('Daily Curse Forge Download','g','Curse Forge '+ average('Daily Curse Forge Download'))
    line('Daily Unique Download','r','Unique '+ average('Daily Unique Download'))
    line('Daily Download','b','Total '+ average('Daily Download'))
    subplot(2, 'Downloads', 'Daily Downloads')

    plt.subplot(3,1,3)
    line('Points','#FFD700','Points\n'+ average('Points'))
    plt.xlabel('Dates')
    subplot(3, 'Points', 'Points')

    file_date = pd.to_datetime(raw_dates).dt.strftime('%Y-%m-%d')
    plt.savefig('Graphs/'+project_name+' Analytics '+file_date[0]+'_'+file_date.values[-1],dpi=150)

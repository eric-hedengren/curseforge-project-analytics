import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob

def line(a, b, c, d=2): # Data, Color, Label
    plt.plot_date(display_dates, data[a], b, label=c, zorder=d)

def details(name):
    current_data = data[name]
    return  '[max ' + str(current_data.max()) + ' - avg %.1f]' % current_data.mean()

def subplot(y, z):
    plt.title(y)
    plt.ylabel(z)
    plt.tick_params(labelright=True, right=True)
    plt.legend(loc='upper left')
    plt.xlim([display_dates[0], display_dates.values[-1]]); plt.ylim(0) # Tighten the x/y axis
    plt.xticks(np.arange(0, date_size, tick_frequency)) # Start, Stop, Steps

def nonzeroaverage(name):
    current_data = data[name]
    return '%.2f' % current_data[current_data != 0].mean()

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

    dates = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')
    display_dates = pd.to_datetime(dates).dt.strftime('%y-%m-%d') # Format x axis date display

    date_size = dates.size
    tick_frequency = int(date_size/15)

    if tick_frequency < 1: # In case the number is rounded to 0
        tick_frequency = 1

    plt.figure(figsize=(20,11))

    project_name = data['Name'][0]
    if len(project_name) > 40:
        raise Exception('Project name is way too long')
    plt.suptitle(project_name, fontsize=50)

    plt.subplot(3,1,1)
    line('Historical Download','black','Total Downloads\n'+str(data['Historical Download'].values[-1]))
    subplot('Total', 'Downloads')

    plt.subplot(3,1,2)
    line('Daily Download','black','Total '+ details('Daily Download'),2.3)
    line('Daily Unique Download','red','Unique '+ details('Daily Unique Download'),2.2)
    line('Daily Curse Forge Download','green','Curse Forge '+ details('Daily Curse Forge Download'),2.1)
    line('Daily Twitch App Download','#6441a5','Twitch App '+ details('Daily Twitch App Download'))
    subplot('Daily Downloads', 'Downloads')

    plt.subplot(3,1,3)
    p = 'Points'
    data_points = data[p]
    line(p,'gold',p +' '+ '[max ' + str(data_points.max()) +' - avg '+ nonzeroaverage(p) +']')
    plt.xlabel('Dates')
    subplot(p,p)

    plt.savefig('Graphs/'+project_name+' Analytics '+dates[0]+'_'+dates.values[-1], dpi=150)
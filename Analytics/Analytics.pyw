import pandas as pd
from matplotlib import pyplot as plt
from numpy import arange
from glob import glob
from os import remove

def line(name, color, label, order=2): # Data, Color, Label
    plt.plot_date(display_dates, data[name], color, label=label, zorder=order)

def details_line(name, color, label, order=2, mean=None): # Data, Color, Label
    plt.plot_date(display_dates, data[name], color, label=label, zorder=order)
    if mean == None:
        mean = data[name].mean()
    high = data[name].max()
    style=['dotted','dashed']
    for i, j in enumerate([mean,high]):
        plt.plot_date([begin, end], [j,j], color, ls=style[i], alpha=.5, zorder=1.99)

def subplot(y, z):
    plt.title(y)
    plt.ylabel(z)
    plt.tick_params(labelright=True, right=True)
    plt.legend(loc='upper left')
    plt.xlim([begin, end]); plt.ylim(0) # Tighten the x/y axis
    plt.xticks(arange(0, date_size, tick_frequency)) # Start, Stop, Steps

data_files = glob('Data/*')
current_projects = []

for i in glob('Graphs/*'):
    remove(i)

for i, name in enumerate(data_files):
    if i == len(data_files)-1:
        current_projects.append(name)
        break
    next_name = data_files[i+1]
    if name[:name.index('_overview_v1_')] == next_name[:next_name.index('_overview_v')]:
        remove(name)
        continue
    current_projects.append(name)

for current_file in current_projects:
    data = pd.read_csv(current_file)
    del data['Project ID']

    dates = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')
    display_dates = pd.to_datetime(dates).dt.strftime('%y-%m-%d') # Format x axis date display

    begin = display_dates[0]; end = display_dates.values[-1]

    date_size = dates.size
    tick_frequency = int(date_size/15)+1

    if tick_frequency < 1: # In case the number was rounded to 0
        tick_frequency = 1

    plt.figure(figsize=(20,11))
    plt.style.use('dark_background') # Toggle dark mode

    project_name = data['Name'][0]
    if len(project_name) > 40:
        raise Exception('Project name is way too long')
    plt.suptitle(project_name, fontsize=50)

    t = 3
    if data['Points'].sum() == 0:
        t = 2

    plt.subplot(t,1,1)
    current_total = str(data['Historical Download'].values[-1])
    line('Historical Download','white','Total Downloads\n'+current_total)
    subplot('Total', 'Downloads')

    plt.subplot(t,1,2)
    details_line('Daily Download','white','Total',2.03)
    details_line('Daily Unique Download','red','Unique',2.02)
    details_line('Daily Curse Forge Download','green','Curse Forge',2.01)
    details_line('Daily Twitch App Download','#6441a5','Twitch App')
    subplot('Daily Downloads', 'Downloads')

    if t == 3:
        plt.subplot(t,1,3)
        p = 'Points'
        dp = data[p]
        details_line(p,'gold',p+'\n'+'%.2f' % dp.sum(),mean=dp[dp != 0].mean())
        plt.xlabel('Dates')
        subplot(p,p)

    plt.savefig('Graphs/'+project_name+' Analytics '+dates[0]+'_'+dates.values[-1], dpi=150)
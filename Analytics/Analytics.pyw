import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime
import numpy as np
import glob

def line(a, b, c): # Data, Color, Label
    plt.plot_date(dates,data[a], b, label = c)

def average(name):
    total = 0
    length = data[name].size
    for i in range(length):
        total += data[name].values[i]
    return "%.2f" % (total/length)

def subplot(x, y):
    plt.ylabel(y)
    plt.legend(loc = 2) # Sets legend to top left
    plt.xlim([start,end]) # Tighten the x axis
    plt.xticks(np.arange(0,dates.size,dates.size/15)) # Set tick frequency

list = glob.glob('Data/*')
data = pd.read_csv(list[-1])
del data['Project ID'] # Delete unused columns

dates = data['Date']

dates = pd.to_datetime(dates).dt.strftime('%y-%m-%d') # Format date data
start = dates.values[0]
end = dates.values[-1]

plt.figure(figsize=(15,10)) # Create figure

plt.subplot(3,1,1) # Create subplots for the figure
plt.title(data['Name'][0]) # Set title as project name
line('Historical Download','k','Total Downloads\n'+str(data['Historical Download'].values[-1]))
subplot(1, 'Total')

plt.subplot(3,1,2)
line('Daily Download','b','Total ' + average('Daily Download')) # Print daily average downloads
line('Daily Unique Download','r','Unique ' + average('Daily Unique Download'))
line('Daily Curse Forge Download','g','Curse Forge ' + average('Daily Curse Forge Download'))
line('Daily Twitch App Download','#800080','Twitch App ' + average('Daily Twitch App Download'))
subplot(2, 'Daily Downloads + Average')

plt.subplot(3,1,3)
line('Points','#FFD700','Points\n' + average('Points'))
subplot(3, 'Points + Average')
plt.xlabel('Date')

today = datetime.today().strftime('%Y-%m-%d')
plt.savefig('Graphs/'+today+'.png') # Save as image
plt.show() # Displays the graph (optional)
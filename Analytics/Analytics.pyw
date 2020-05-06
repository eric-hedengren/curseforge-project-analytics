import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime
import numpy as np
import glob

def line(a, b, c): # Data, Color, Label
    plt.plot_date(dates,data[a], b, label = c)

def subplot(x, y):
    plt.ylabel(y)
    plt.legend(loc = 2) # Sets legend to top left
    plt.xlim([start, end]) # Tighten the x axis
    plt.xticks(np.arange(1, dates.size, 3)) # Set tick frequency

list = glob.glob('Data/*')
data = pd.read_csv(list[-1])
del data['Project ID'] # Delete unused columns

dates = data['Date']

dates = pd.to_datetime(dates).dt.strftime('%y-%m-%d') # Format date data
start = dates.values[0]
end = dates.values[-1]

plt.figure(figsize=(12,8)) # Create figure

plt.subplot(3,1,1) # Create subplots for the figure
plt.title(data['Name'][0]) # Set title as project name
line('Historical Download','k','Total Downloads')
subplot(1, 'Total')

plt.subplot(3,1,2)
line('Daily Download','b','Total')
line('Daily Unique Download','r','Unique')
line('Daily Curse Forge Download','g','Curse Forge')
line('Daily Twitch App Download','#800080','Twitch App')
subplot(2, 'Daily Downloads')

plt.subplot(3,1,3)
line('Points','#FFD700','Points')
subplot(3, 'Points')
plt.xlabel('Date')

today = datetime.today().strftime('%Y-%m-%d')
plt.savefig('Graphs/'+today+'.png') # Save as image
plt.show() # Displays the graph (optional)
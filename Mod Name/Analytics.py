import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import glob

def subplot(x):
    plt.ylabel(x)
    plt.legend(loc = 2) # Sets legend to top left
    plt.xlim([start, end])

list = glob.glob('Data/*')
data = pd.read_csv(list[-1])
del data['Project ID']; del data['Name'] # Delete useless columns

data['Date'] = data['Date'].astype('datetime64[ns]') # Customize date display
start = data['Date'].values[0] # Tighten the x axis, get rid of whitespace
end = data['Date'].values[-1]

plt.figure(figsize=(12,8)) # Create figure

plt.subplot(3,1,1) # Create subplots for the figure
plt.plot(data['Date'],data['Historical Download'],'k',label='Total Downloads')
subplot('Total')

plt.subplot(3,1,2)
plt.plot(data['Date'],data['Daily Download'],'b',label='Total')
plt.plot(data['Date'],data['Daily Unique Download'],'r',label='Unique')
plt.plot(data['Date'],data['Daily Curse Forge Download'],'g',label='Curse Forge')
plt.plot(data['Date'],data['Daily Twitch App Download'],'#800080',label='Twitch App')
subplot('Daily Downloads')

plt.subplot(3,1,3)
plt.plot(data['Date'],data['Points'],'#FFD700',label='Points')
plt.xlabel('Date')
subplot('Points')

today = datetime.today().strftime('%Y-%m-%d')
plt.show() # Display graph
plt.savefig('Graphs/'+today+'.png') # Save as image
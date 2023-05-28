import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

data = pd.read_csv("C:/Users/PC/OneDrive/Desktop/GPOI/sturdy-spork/dataset.csv", sep=";", engine="python")

df = pd.DataFrame(data)

numeric_columns = df.columns[1:]

fig, ax = plt.subplots(figsize=(15, 8.8))

current_frame = 0

colors = ['red', 'green']

def update(frame):
    ax.clear()
    country_codes = df['TIME']
    ax.barh(country_codes, df[numeric_columns[frame]], color=colors[frame % len(colors)])
    ax.set_yticklabels(country_codes)
    ax.set_xlabel('Dati')
    ax.set_title('Security policy: measures, risks and staff awarenes', fontweight='bold', fontsize=16)
    ax.legend([numeric_columns[frame]], loc='upper right') 

def on_click(event):
    global current_frame
    if event.button == 1:  # Click sinistro del mouse
        if current_frame==0:
            current_frame=1
        elif current_frame==1:
            current_frame=0
        update(current_frame)
        plt.draw()

fig.canvas.mpl_connect('button_press_event', on_click)

update(current_frame)

plt.show()

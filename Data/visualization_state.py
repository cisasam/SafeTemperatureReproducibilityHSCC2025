import pandas as p
import matplotlib.pyplot as plt
import sys


def plot_incubator_data(data):
    plt.rcParams['text.usetex'] = True
    plt.rcParams.update({'font.size': 9})
    

    plt.rc('text.latex', preamble=r'\usepackage{xspace}')
    fig, (ax1) = plt.subplots(1, 1)

    ax1.plot((data["time"]-data["time"][0])/10e8, data["average_temperature"], label=r'$T_c$')

    

    ax1.hlines(y=37.75, colors='k', xmin=0, xmax=((data['time'].iloc[-1])-data["time"][0])/10e8, label='Bounds')
    ax1.hlines(y=36.5, colors='k', xmin=0, xmax=((data['time'].iloc[-1])-data["time"][0])/10e8)
    ax1.set_ylabel("Temperature (°C)")
    ax1.set_xlabel("time (s)")

    ax1.legend(loc=4)
    

    fig.align_xlabels()
    fig.set_figwidth(4.2)
    fig.set_figheight(3)
    fig.set_layout_engine(layout='constrained')
    plt.show()
    return fig

if __name__ == '__main__':
    if not ('state' in sys.argv[1]):
        print("Please use this script with data from the low level driver (marked as state in the csv name)")
    elif ('35-40' in sys.argv[1]):
        print("Please use the dedicated script for the additional experiment to show the correct bounds.")
    else:
        data = p.read_csv(sys.argv[1])
        fig = plot_incubator_data(data)
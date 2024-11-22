import pandas as p
import matplotlib.pyplot as plt
import sys


def plot_controller_data(data):
    plt.rcParams['text.usetex'] = True
    plt.rc('text.latex', preamble=r'\usepackage{xspace}')
    fig, (ax1) = plt.subplots(1, 1)

    ax1.plot((data["plant_time"]-data["time"][0])/10e8, data["t_heater"], label=r"$T_h$")
    ax1.plot((data["plant_time"]-data["time"][0])/10e8, data["ubound_h"], label='safeToHeat')
    ax1.plot((data["plant_time"]-data["time"][0])/10e8, data["lbound_h"], label='safeToCool')
    ax1.set_ylabel("Temperature (°C)")

    ax1.legend(loc=4)
    ax1.set_xlabel("time (s)")
    fig.align_xlabels()

    plt.xlim(0,600)

    plt.show()
    return fig

if __name__ == '__main__':
    if not ('cont' in sys.argv[1]):
        print("Please use this script with data from the controller (marked as cont in the csv name)")
    else:
        data = p.read_csv(sys.argv[1])
        fig = plot_controller_data(data)
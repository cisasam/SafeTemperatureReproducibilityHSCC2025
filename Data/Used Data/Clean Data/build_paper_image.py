import pandas as p
import matplotlib.pyplot as plt


def plot_incubator_data(data1,data2,data3,data4):
    plt.rcParams['text.usetex'] = True
    plt.rcParams.update({'font.size': 9})
    

    plt.rc('text.latex', preamble=r'\usepackage{xspace}')
    fig, (ax1) = plt.subplots(1, 1)

    ax1.plot((data1["time"]-data1["time"][0])/10e8, data1["average_temperature"], label=r'$T_c^1$')
    ax1.plot((data2["time"]-data2["time"][0])/10e8, data2["average_temperature"], label=r'$T_c^2$')
    ax1.plot((data3["time"]-data3["time"][0])/10e8, data3["average_temperature"], label=r'$T_c^3$')
    ax1.plot((data4["time"]-data4["time"][0])/10e8, data4["average_temperature"], label=r'$T_c^4$', color='tab:purple')
    

    ax1.hlines(y=37.75, colors='k', xmin=0, xmax=((data1['time'].iloc[-1])-data1["time"][0])/10e8, label='Bounds')
    ax1.hlines(y=36.5, colors='k', xmin=0, xmax=((data1['time'].iloc[-1])-data1["time"][0])/10e8)
    ax1.set_ylabel("Temperature (°C)")
    ax1.set_xlabel("time (s)")

    ax1.legend(loc=4)
    

    fig.align_xlabels()
    plt.xlim(0,600)
    fig.set_figwidth(4.2)
    fig.set_figheight(3)
    fig.set_layout_engine(layout='constrained')
    plt.show()
    return fig

if __name__ == '__main__':
    data1 = p.read_csv('params1-state.csv')
    data2 = p.read_csv('params2-state.csv')
    data3 = p.read_csv('cbair-error-state.csv')
    data4 = p.read_csv('gbox-error-state.csv')
    fig = plot_incubator_data(data1,data2,data3,data4)



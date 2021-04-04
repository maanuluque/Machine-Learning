import matplotlib; matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plot_gen(gen, best, avg):
    plt.style.use('bmh')
    x = []
    y1 = []
    y2 = []

    def animate(i):
        plt.cla()
        x.append(gen.get())
        y1.append(best.get())
        y2.append(avg.get())

        plt.plot(x, y2, label='AVG')
        plt.plot(x, y1, label='Best')

        plt.legend(loc='upper left')
        plt.tight_layout()
        plt.savefig('graph.png')

    ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    plt.tight_layout()
    plt.show()
    return ani


import matplotlib; matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plot_gen(generations, avg_fitness, best_fitness):
    plt.style.use('fivethirtyeight')

    def animate(i):
        plt.cla()

        plt.plot(generations, avg_fitness, label='AVG')
        plt.plot(generations, best_fitness, label='Best')

        plt.legend(loc='upper left')
        plt.tight_layout()

    ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    plt.tight_layout()
    plt.show()
    return ani


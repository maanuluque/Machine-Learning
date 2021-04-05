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
        gen_size = gen.qsize()
        best_size = best.qsize()
        avg_size = avg.qsize()
        min_size = min([gen_size, best_size, avg_size])
        while min_size > 0:
            x.append(gen.get())
            y1.append(best.get())
            y2.append(avg.get())
            min_size -= 1

        plt.plot(x, y2, label='AVG')
        plt.plot(x, y1, label='Best')
        plt.legend(loc='upper left')
        plt.tight_layout()
        plt.savefig('fitness_graph.png')

    ani = FuncAnimation(plt.gcf(), animate)

    plt.tight_layout()
    plt.show()
    return ani


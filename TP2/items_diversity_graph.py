import matplotlib; matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plot_items_div(gen_q, div_q):
    plt.style.use('bmh')
    x = []
    y = []

    def animate(i):
        plt.cla()
        gen_size = gen_q.qsize()
        div_size = div_q.qsize()
        min_size = min([gen_size, div_size])
        while min_size > 0:
            x.append(div_q.get())
            y.append(gen_q.get())
            min_size -= 1

        plt.plot(x, y, label='Shared Items')
        plt.legend(loc='upper left')
        plt.tight_layout()
        plt.savefig('items_graph.png')

    ani = FuncAnimation(plt.gcf(), animate)

    plt.tight_layout()
    plt.show()
    return ani


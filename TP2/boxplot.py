import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

matplotlib.use("TkAgg")


def plot_diversity(init_q, nth_q, last_q, labels_queue):
    fig, ax = plt.subplots()

    def update(i):

        initial = init_q.get()
        nth = nth_q.get()
        last = last_q.get()
        labels = labels_queue.get()

        ax.cla()
        ax.boxplot(x=[initial, nth, last], labels=labels)

    ani = animation.FuncAnimation(fig, update, interval=100)
    plt.savefig('div.png')
    plt.show()


def plot_last_diversity(diversity):
    fig, ax = plt.subplots()
    diversity_list = diversity.get()
    ax.boxplot(x=diversity_list, labels=("last_gen",))
    plt.savefig('last_div.png')
    plt.show()

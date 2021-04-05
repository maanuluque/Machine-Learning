import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

matplotlib.use("TkAgg")


def plot_diversity(init_q, nth_q, last_q, labels_queue):
    fig, ax = plt.subplots()

    def update(i):
        init_size = init_q.qsize()
        nth_size = nth_q.qsize()
        last_size = last_q.qsize()
        lbl_size = labels_queue.qsize()
        min_size = min([init_size, nth_size, last_size, lbl_size])
        plot = False
        while min_size > 0:
            plot = True
            initial = init_q.get()
            nth = nth_q.get()
            last = last_q.get()
            labels = labels_queue.get()
            min_size -= 1

        if plot:
            ax.cla()
            ax.boxplot(x=[initial, nth, last], labels=labels)
            plt.savefig('fitness_boxplot.png')

    ani = animation.FuncAnimation(fig, update)
    plt.show()


def plot_last_diversity(diversity):
    fig, ax = plt.subplots()
    diversity_list = diversity.get()
    ax.boxplot(x=diversity_list, labels=("last_gen",))
    plt.savefig('final_fitness_boxplot.png')
    plt.show()

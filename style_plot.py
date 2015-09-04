import matplotlib.pyplot as plt
import numpy as np

with plt.xkcd():

    x = np.linspace(-10, 10, 100, endpoint=True)
    y = x

    fig = plt.figure()
    plt.plot(x, y)

    plt.xticks([-10, 10], ['Rookie', 'Guru'])
    plt.yticks([-10, 10], ['Hands Off', 'Authoritarian'])
    plt.xlabel('Expertise')
    plt.ylabel('Style')

    axes = plt.gca()
    axes.xaxis.set_label_coords(0.65, 0.45)
    axes.yaxis.set_label_coords(0.45, 0.65)
    for spine in axes.spines.itervalues():
        spine.set_position(('data', 0))

    fig.savefig('images/style.png')

import matplotlib.pyplot as plt
import numpy as np

with plt.xkcd():

    x = np.linspace(-10, 10, 100, endpoint=True)
    y = x

    fig = plt.figure()
    plt.plot(x, y)

    plt.xticks([])
    plt.yticks([])
    plt.xlabel('Relative Expertise ->')
    plt.ylabel('Authoritarianism ->')

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))

    fig.savefig('images/style.png')

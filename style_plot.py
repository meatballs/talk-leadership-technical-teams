import matplotlib.pyplot as plt
import numpy as np

with plt.xkcd():
    # Based on "Stove Ownership" from XKCD by Randall Monroe
    # http://xkcd.com/418/

    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.xticks([])
    plt.yticks([])

    plt.plot([1,2,3,4])

    plt.xlabel('Your Relative Expertise ->')
    plt.ylabel('Appropriate Authoritarianism ->')

    fig.savefig('images/style.png')

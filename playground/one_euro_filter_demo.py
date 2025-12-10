import matplotlib.pyplot as plt
import numpy as np
import seaborn
from matplotlib.animation import FuncAnimation


import math


def smoothing_factor(t_e, cutoff):
    r = 2 * math.pi * cutoff * t_e
    return r / (r + 1)


def exponential_smoothing(a, x, x_prev):
    return a * x + (1 - a) * x_prev


class OneEuroFilter:
    def __init__(self, t0, x0, dx0=0.0, min_cutoff=1.0, beta=0.0,
                 d_cutoff=1.0):
        """Initialize the one euro filter."""
        # The parameters.
        self.min_cutoff = float(min_cutoff)
        self.beta = float(beta)
        self.d_cutoff = float(d_cutoff)
        # Previous values.
        self.x_prev = float(x0)
        self.dx_prev = float(dx0)
        self.t_prev = float(t0)

    def __call__(self, t, x):
        """Compute the filtered signal."""
        t_e = t - self.t_prev

        # The filtered derivative of the signal.
        a_d = smoothing_factor(t_e, self.d_cutoff)
        dx = (x - self.x_prev) / t_e
        dx_hat = exponential_smoothing(a_d, dx, self.dx_prev)

        # The filtered signal.
        cutoff = self.min_cutoff + self.beta * abs(dx_hat)
        a = smoothing_factor(t_e, cutoff)
        x_hat = exponential_smoothing(a, x, self.x_prev)

        # Memorize the previous values.
        self.x_prev = x_hat
        self.dx_prev = dx_hat
        self.t_prev = t

        return x_hat

np.random.seed(1)

# Parameters
frames = 100
start = 0
end = 4 * np.pi
scale = 0.05


# The noisy signal
t = np.linspace(start, end, frames)
x = np.sin(t)
x_noisy = x + np.random.normal(scale=scale, size=len(t))


# The filtered signal
min_cutoff = 0.004
beta = 0.7
x_hat = np.zeros_like(x_noisy)
x_hat[0] = x_noisy[0]
one_euro_filter = OneEuroFilter(
    t[0], x_noisy[0],
    min_cutoff=min_cutoff,
    beta=beta
)
for i in range(1, len(t)):
    x_hat[i] = one_euro_filter(t[i], x_noisy[i])


# The figure
# https://eli.thegreenplace.net/2016/drawing-animated-gifs-with-matplotlib/
seaborn.set()
fig, ax = plt.subplots(figsize=(12, 6))
ax.set(
    xlim=(start, end),
    ylim=(1.1*(-1-scale), 1.1*(1+scale)),
    xlabel="$t$",
    ylabel="$x$",
)
fig.set_tight_layout(True)
signal, = ax.plot(t[0], x_noisy[0], 'o')
filtered, = ax.plot(t[0], x_hat[0], '-')


def update(i):
    print(i)
    signal.set_data(t[0:i], x_noisy[0:i])
    filtered.set_data(t[0:i], x_hat[0:i])
    return signal, filtered


if __name__ == '__main__':
    # FuncAnimation will call the 'update' function for each frame; here
    # animating over 10 frames, with an interval of 200ms between frames.
    anim = FuncAnimation(fig, update, frames=frames, interval=100)
    anim.save('one_euro_filter.gif', dpi=80, writer='imagemagick')
    # update(frames)
    plt.savefig("one_euro_filter.png", dpi=300)

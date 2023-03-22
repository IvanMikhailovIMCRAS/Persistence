from scan_track.scan_track import ReadTrack, read_bonds
import numpy as np
import matplotlib.pyplot as plt

def cosine(x1, y1, x2, y2):
    return (x1*x2 + y1*y2) / (x1**2 + y1**2)**0.5 / (x2**2 + y2**2)**0.5

track = ReadTrack("/home/imc/SEMISHIN/Rod_brush")
track.one_step()
n_dendron = list(track.btype).count(1)
n_beads = (list(track.btype).count(2) + n_dendron) // n_dendron
print(n_beads)
cm_x = np.zeros(n_dendron)
cm_y = np.zeros(n_dendron)
corr = np.zeros(n_dendron)
n_step = 0
while track.one_step():
    n_step += 1
    for d in range(n_dendron):
        cm_x[d] = np.sum(track.x[d*n_beads:(d+1)*n_beads]) / n_beads
        cm_y[d] = np.sum(track.y[d*n_beads:(d+1)*n_beads]) / n_beads
    for d in range(n_dendron):
        corr[d] += cosine(cm_x[d], cm_y[d], cm_x[0], cm_y[0])
plt.plot(corr/n_step)
plt.show()
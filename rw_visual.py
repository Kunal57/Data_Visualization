import matplotlib.pyplot as plt

from random_walk import RandomWalk

# keep making new walks, as long as the program is active

while True:
  # make a random walk, and plot the points
  rw = RandomWalk()
  rw.fill_walk()

  point_numbers = list(range(rw.num_points))
  plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor="none", s=15)

  # emphasize the first and last points
  plt.scatter(0, 0, c="green", edgecolor="none", s=100)
  plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolor="none", s=100)

  plt.show()

  keep_running = input("Make another walk? (y/n): ")
  if keep_running == "n":
    break
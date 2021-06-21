from src.xou import xOU2CSV
import numpy as np
import matplotlib.pyplot as plt

xOU2CSV("eou/electrode.EOU", "field_csv/electrode.csv")

a = np.genfromtxt("field_csv/electrode.csv", delimiter=",")
# a = np.random.rand(100).reshape(10, 10)
# print(a)

figure = plt.figure()
axes = figure.add_subplot(111)
image = axes.imshow(a, cmap=plt.cm.jet, interpolation='nearest')
figure.colorbar(image)

plt.show()
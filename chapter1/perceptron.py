import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

# x0 (threshold), x1, x2, y
data = [
    [1, 0.5, 0.5, 1],
    [1, 0.6, 0.6, 1],
    [1, 0.7, 0.7, 1],
    [1, 0.4, 0.88, 1],
    [1, 0.66, 0.45, 1],
    [1, 0.58, 0.75, 1],
    [1, -0.3, 0.1, -1],
    [1, -0.4, -0.1, -1],
    [1, 0.3, 0.2, -1],
    [1, -0.1, -0.15, -1]
]
x1 = [x[1] for x in data]
x2 = [x[2] for x in data]
color = ['red' if x[3] is 1 else 'blue' for x in data]

fig, ax = plt.subplots()
ax.scatter(x1, x2, c=color)
x = np.linspace(-0.5, 1, 2)
y = -1*x + 0.6 #f
ax.plot(x, y, '-r')

print("target function")
print("y = {}x + ({})".format(-1, 0.6))

w_hist = []
w = [0, 0, 0]
converged = False
step = 1

while not converged:
    predictions = []
    for x in data:
        if sum(w[i]*x[i] for i in range(3)) > 0:
            predictions.append(1)
        else:
            predictions.append(-1)
    for i in range(len(predictions)):
        if predictions[i] != data[i][3]:
            for j in range(3):
                w[j] += step*data[i][3]*data[i][j]
            w_hist.append(w.copy())
            break
        elif i == len(predictions)-1:
            converged = True

for w in w_hist:
    if w[2] == 0:
        continue #can't plot a vertical line
        
    print("y = {}x + ({})".format(round(-w[1]/w[2],3), round(-w[0]/w[2],3)))
    
    fig, ax = plt.subplots()
    ax.scatter(x1, x2, c=color)

    x = np.linspace(-0.5, 1, 2)
    y = (-w[1]/w[2])*x + (-w[0]/w[2])
    ax.plot(x, y, '-r')
    plt.show()
    print('\n')
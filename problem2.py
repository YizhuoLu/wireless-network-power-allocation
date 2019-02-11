import numpy as np
import matplotlib.pyplot as plt

# theta = 2
g11 = 0.2
g22 = 0.9
g12 = 0.2
g21 = 0.2
theta1 = 2
theta2 = 1
n = 1

def connectpoints(x,y,p1,p2, ax):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    ax.plot([x1,x2],[y1,y2],'--')

b1 = n/g21
b2 = -n * theta1 / g22
a = np.array([[g11/(g21 * theta1),  -1], [g12 * theta1 / g22, -1]])
b = np.array([b1, b2])
P = np.linalg.solve(a, b)
print('Optimal Power Solution of P1, P2 when theta = 2')
print('P1: %fmw' %P[0])
print('P2: %fmw' %P[1])
xx = [128, P[0], P[0]]
yy = [P[1], 59, P[1]]
fig1, ax1 = plt.subplots()
p1 = np.arange(128, 132, 1)
p21 = (p1 * g11) / (g21 * theta1) - (n / g21)
p22 = (p1 * g12 * theta1) / g22 + n * theta1 / g22
ax1.plot(p1, p21, color='orange', label='Link1')
ax1.plot(p1, p22, color='blue', label='Link2')
connectpoints(xx, yy, 0, 2, ax1)
connectpoints(xx, yy, 1, 2, ax1)
legend1 = ax1.legend(loc='upper left', shadow=True)
# y = []
# y2 = []
# for i in range(len(p1)):
#     y.append(min(p21[i], p22[i]))
#     y2.append(max(p21[i], p22[i]))
# x = np.arange(len(y))
# ax1.fill_between(x, 0, y, facecolor='gray')
# ax1.fill_between(x, 300, y2, facecolor='orchid')
plt.text(129, 59, 'ONLY Link1 can receive', weight='bold')
plt.text(128, 60.2, 'ONLY Link2 can receive', weight='bold')
ax1.fill_between(p1, p21, p22, where=p21 >= p22, facecolor='grey', interpolate=True)
ax1.annotate('BOTH link can receive', xy=(130.721, 60.3411), xytext=(130, 60), arrowprops=dict(facecolor='black', shrink=0.05), weight='bold')
plt.title('P2 change with p1 when theta = 2')
plt.xlabel('P1')
plt.ylabel('P2')

# theta = 1
b1 = n/g21
b2 = -n * theta2 / g22
a = np.array([[g11/(g21 * theta2),  -1], [g12 * theta2 / g22, -1]])
b = np.array([b1, b2])
P = np.linalg.solve(a, b)
print('Optimal Power Solution of P1, P2 when theta = 1')
print('P1: %fmw' %P[0])
print('P2: %fmw' %P[1])

xx = [0, P[0], P[0]]
yy = [P[1], -4, P[1]]
fig2, ax2 = plt.subplots()
p1 = np.arange(0, 14, 0.1)
p221 = (p1 * g11) / (g21 * theta2) - (n / g21)
p222 = (p1 * g12 * theta2) / g22 + n * theta2 / g22
ax2.plot(p1, p221, color='orange', label='Link1')
ax2.plot(p1, p222, color='blue', label='Link2')
connectpoints(xx, yy, 0, 2, ax2)
connectpoints(xx, yy, 1, 2, ax2)
legend2 = ax2.legend(loc='upper left', shadow=True)
# for i in range(len(p1)):
#     y[i] = min(p21[i], p22[i])
#     y2[i] = max(p21[i], p22[i])
# ax2.fill_between(x, 0, y, facecolor='gray')
# ax2.fill_between(x, 600, y2, facecolor='orchid')
plt.text(6, -1, 'ONLY Link1 can receive', weight='bold')
plt.text(1, 6, 'ONLY Link2 can receive', weight='bold')
ax2.fill_between(p1, p221, p222, where=p221 >= p222, facecolor='grey', interpolate=True)
ax2.annotate('BOTH link can \nreceive', xy=(10.26, 4.24), xytext=(11, -0.1), arrowprops=dict(facecolor='black', shrink=0.05), weight='bold')
plt.title('P2 change with p1 when theta = 1')
plt.xlabel('P1')
plt.ylabel('P2')
plt.show()
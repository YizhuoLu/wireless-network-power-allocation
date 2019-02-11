import numpy as np
import matplotlib.pyplot as plt

g11 = 0.7
g12 = 0.4
g21 = 0.1
g22 = 0.4
theta = 2
n = 1

# Check if it converge to the same result: yes
P1_series = []
P2_series = []
prev1 = 5
prev2 = 30
P1_series.append(prev1)
P2_series.append(prev2)
P1 = 5
P2 = 130
for i in range(21):
    # print(i)
    SINR1 = (prev1 * g11) / (prev2 * g21 + n)
    SINR2 = (prev2 * g22) / (prev1 * g12 + n)
    P1 = (theta / SINR1) * prev1
    P2 = (theta / SINR2) * prev2
    P1_series.append(P1)
    P2_series.append(P2)
    prev1 = P1
    prev2 = P2
print('Power solution of P1 P2 using Foschini-Miljanic algorithm')
print('P1: %fmw' %P1)
print('P2: %fmw' %P2)

# plot
fig1, ax1 = plt.subplots()
t = np.arange(0, 22, 1)
plt.title('Power allocated for each link vs. time')
plt.xlabel('Time')
plt.ylabel('Power')
plt.axhline(y=25, linestyle='--', color='black')
plt.axhline(y=10, linestyle='--', color='black')
ax1.plot(t, P1_series, '-o', color='blue')
ax1.plot(t, P2_series, '-o', color='red')
ax1.annotate('Link I', xy=(11.0472, 9.61343), xytext=(12.5, 4.5), arrowprops=dict(facecolor='black', shrink=0.05))
ax1.annotate('Link II', xy=(11.0695, 23.9448), xytext=(10.5,  18.5), arrowprops=dict(facecolor='black', shrink=0.05))
ax1.set_xlim(left=0)
ax1.set_ylim(bottom=0)

fig2, ax2 = plt.subplots()
P2 = np.arange(0, 40, 1)
P11 = P2 * (g22 / (g12 * theta)) - n / g12
P12 = P2 * (g21 * theta / g11) + n * theta / g11
plt.title('P1 vs. P2 & power pairs (P1, P2) chosen by iteration')
plt.xlabel('P2')
plt.ylabel('P1')
ax2.plot(P2, P11, color='blue', label='Tx2-Rx2')
ax2.plot(P2, P12, color='red', label='Tx1-Rx1')
ax2.fill_between(P2, P12, P11, where=P11 >= P12, facecolor='gray', interpolate=True)
ax2.annotate('Operating regions\n for both links', xy=(33, 13), xytext=(30, 9), arrowprops=dict(facecolor='black', shrink=0.05))
ax2.plot(P2_series, P1_series, color='green', label='Power allocation using iteration')
ax2.set_xlim(left=0)
ax2.set_ylim(bottom=0)
legend = ax2.legend(loc='upper left', shadow=True)
plt.show()
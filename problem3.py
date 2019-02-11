import numpy as np
import matplotlib.pyplot as plt

r1 = 1 #3
r2 = 3 #1
r3 = 5 #5
r4 = 6 #2
r5 = 9 #4
r = [0, 1, 3, 5, 6, 9]

fig, ax = plt.subplots()
plt.title('Optimal Power allocated to each channel as total power changing')
plt.xlabel('Total Power')
plt.ylabel('Power to each channel')
# first part
tmp_sum2 = 0
for i in range(1, 3):
    tmp_sum2 = tmp_sum2 + r[i]
second_intercept = 2 * r[2] - tmp_sum2
Ptot = np.arange(0, second_intercept, 0.1)
tmp_sum = r[1]
P11 = (tmp_sum + Ptot) - r[1]
P11_last_y = (tmp_sum + second_intercept) - r[1]
ax.plot(Ptot, P11, color='blue')
# ax.set_ylim(bottom=0)
# ax.set_xlim(left=0)
# second part
tmp_sum2 = 0
for i in range(1, 4):
    tmp_sum2 = tmp_sum2 + r[i]
third_intercept = 3 * r[3] - tmp_sum2
Ptot = np.arange(second_intercept, third_intercept, 0.1)
P21 = 1/2 * (Ptot - second_intercept) + P11_last_y
P22 = 1/2 * (Ptot - second_intercept)
ax.plot(Ptot, P21, color='blue')
ax.plot(Ptot, P22, color='orange')
# ax.set_ylim(bottom=0)
# ax.set_xlim(left=0)
P21_last_y = 1/2 * (third_intercept - second_intercept) + P11_last_y
P22_last_y = 1/2 * (third_intercept - second_intercept)
# third part
tmp_sum2 = 0
for i in range(1, 5):
    tmp_sum2 = tmp_sum2 + r[i]
fourth_intercept = 4 * r[4] - tmp_sum2
Ptot = np.arange(third_intercept, fourth_intercept, 0.1)
P31 = 1/3 * (Ptot - third_intercept) + P21_last_y
P32 = 1/3 * (Ptot - third_intercept) + P22_last_y
P33 = 1/3 * (Ptot - third_intercept)
ax.plot(Ptot, P31, color='blue')
ax.plot(Ptot, P32, color='orange')
ax.plot(Ptot, P33, color='green')
# ax.set_ylim(bottom=0)
# ax.set_xlim(left=0)
P31_last_y = 1/3 * (fourth_intercept - third_intercept) + P21_last_y
P32_last_y = 1/3 * (fourth_intercept - third_intercept) + P22_last_y
P33_last_y = 1/3 * (fourth_intercept - third_intercept)
# fourth part
tmp_sum2 = 0
for i in range(1, 6):
    tmp_sum2 = tmp_sum2 + r[i]
fifth_intercept = 5 * r[5] - tmp_sum2
Ptot = np.arange(fourth_intercept, fifth_intercept, 0.1)
P41 = 1/4 * (Ptot - fourth_intercept) + P31_last_y
P42 = 1/4 * (Ptot - fourth_intercept) + P32_last_y
P43 = 1/4 * (Ptot - fourth_intercept) + P33_last_y
P44 = 1/4 * (Ptot - fourth_intercept)
ax.plot(Ptot, P41, color='blue')
ax.plot(Ptot, P42, color='orange')
ax.plot(Ptot, P43, color='green')
ax.plot(Ptot, P44, color='violet')
# ax.set_ylim(bottom=0)
# ax.set_xlim(left=0)
P41_last_y = 1/4 * (fifth_intercept - fourth_intercept) + P31_last_y
P42_last_y = 1/4 * (fifth_intercept - fourth_intercept) + P32_last_y
P43_last_y = 1/4 * (fifth_intercept - fourth_intercept) + P33_last_y
P44_last_y = 1/4 * (fifth_intercept - fourth_intercept)
# fifth part
Ptot = np.arange(fifth_intercept, fifth_intercept + 10, 0.1)
P51 = 1/5 * (Ptot - fifth_intercept) + P41_last_y
P52 = 1/5 * (Ptot - fifth_intercept) + P42_last_y
P53 = 1/5 * (Ptot - fifth_intercept) + P43_last_y
P54 = 1/5 * (Ptot - fifth_intercept) + P44_last_y
P55 = 1/5 * (Ptot - fifth_intercept)
ax.plot(Ptot, P51, color='blue', label='Ni/gi = 1')
ax.plot(Ptot, P52, color='orange', label='Ni/gi = 3')
ax.plot(Ptot, P53, color='green', label='Ni/gi = 5')
ax.plot(Ptot, P54, color='violet', label='Ni/gi = 6')
ax.plot(Ptot, P55, color='red', label='Ni/gi = 9')
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')
plt.axvline(x=second_intercept, linestyle='--', color='black')
plt.axvline(x=third_intercept, linestyle='--', color='black')
plt.axvline(x=fourth_intercept, linestyle='--', color='black')
plt.axvline(x=fifth_intercept, linestyle='--', color='black')
# ax.set_ylim(bottom=0)
# ax.set_xlim(left=0)
# ax.plot(Ptot, P1, color='blue')
# ax.plot(Ptot, P2, color='orange')
# ax.plot(Ptot, P3, color='yellow')
# ax.plot(Ptot, P4, color='violet')
# ax.plot(Ptot, P5, color='red')
# ax.set_ylim(bottom=0)     # bottom = ymin
# ax.set_xlim(left=0)  # left = xmin
legend = ax.legend(loc='upper left', shadow=True)
plt.show()
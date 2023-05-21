import matplotlib.pyplot as plt
import numpy as np
import matplotlib

#matplotlib.rcParams.update({"font.size": 14})


voltages = [
    1.2,
    1.1,
    1,
    0.9,
    0.85,
    0.8,
    0.7,
    0.6,
    0.55,
    0.5,
    ]


frequencies = [
    0,
    15,
    50,
    100,
    200,
    300,
    400,
    500,
    600,
    700,
    800,
    900,
    1000,
    ]



working_status = [
    [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  8,  2],  # 1.2
    [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  8,  2],  # 1.1
    [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  8,  2],  # 1.0
    [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  8,  2],  # 0.9
    [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  8,  2],  # 0.85
    [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  8,  2],  # 0.8
    [0, 10, 10, 10, 10, 10, 10, 10, 10, 10,  8,  8,  2],  # 0.7
    [0, 10, 10, 10, 10, 10, 10, 10, 10,  8,  6,  6,  2],  # 0.6
    [0, 10, 10, 10, 10, 10, 10,  8,  2,  2,  2,  2,  2],  # 0.55
    [0,  6,  6,  6,  6,  6,  6,  6,  6,  2,  2,  2,  2],  # 0.5
    ]

working_status = [
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  0,  0],  # 1.2
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  0,  0],  # 1.1
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  0,  0],  # 1.0
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  0,  0],  # 0.9
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  0,  0],  # 0.85
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  0,  0],  # 0.8
    [10, 10, 10, 10, 10, 10, 10, 10, 10,  0,  0,  0],  # 0.7
    [10, 10, 10, 10, 10, 10, 10, 10,  0,  0,  0,  0],  # 0.6
    [10, 10, 10, 10, 10, 10,  0,  0,  0,  0,  0,  0],  # 0.55
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # 0.5
    ]

powers = [
    [0.2424,
0.2964,
0.3024,
0.2964,
0.3456,
0.3756,
0.4044,
0.432,
0.4752,
0.504,
0.5328,
0.5436,
0.306],
    [0.1892,
0.1584,
0.1474,
0.1584,
0.1892,
0.2101,
0.2266,
0.2497,
0.2739,
0.297,
0.319,
0.341,
0.1364],
    [0.137,
0.136,
0.127,
0.136,
0.155,
0.174,
0.193,
0.201,
0.218,
0.237,
0.278,
0.292,
0.108],
    [0.0972,
0.0999,
0.1053,
0.1125,
0.1269,
0.1413,
0.1548,
0.1683,
0.1809,
0.1953,
0.2088,
0.2232,
0.0981],
    [0.085,
0.085,
0.08925,
0.09605,
0.1071,
0.1122,
0.12325,
0.13345,
0.14535,
0.15555,
0.16575,
0.1785,
0.08245],
    [0.0728,
0.072,
0.076,
0.08,
0.0896,
0.1,
0.1104,
0.12,
0.1304,
0.14,
0.1496,
0.1592,
0.0712],
    [0.0532,
0.0546,
0.056,
0.063,
0.0707,
0.0777,
0.0854,
0.0924,
0.0994,
0.1225,
0.112,
0.1155,
0.0553],
    [0.039,
0.0414,
0.0414,
0.0462,
0.0516,
0.054,
0.06,
0.0654,
0.0714,
0.0726,
0.0756,
0.0816,
0.0372],
    [0.03355,
0.0341,
0.03575,
0.03905,
0.044,
0.0484,
0.05225,
0.05665,
0.0605,
0.03465,
0.03465,
0.03465,
0.0341],
    [0.03,
0.0305,
0.0315,
0.0345,
0.0385,
0.041,
0.0475,
0.0455,
0.043,
0.0325,
0.032,
0.033,
0.03]
    ]
'''
for p in powers:
    for pp in p:
        print(pp, end="\t")
    print("")
'''    

correct_freq = []
for freq in frequencies:
    correct_freq.append(freq // 2)

frequencies = correct_freq

fig, ax1 = plt.subplots()

status = []
for s in working_status:
    status.append(s[2:])

cax = ax1.matshow(status, cmap="RdYlGn", vmin=0, vmax=13)

#ax2 = ax1.secondary_xaxis("bottom")
#ax2.set_xlabel("period [s]")

ax1.set_xticks(range(len(frequencies[3:])), frequencies[3:])
ax1.xaxis.set_ticks_position("bottom")
ax1.set_xlabel("Frequency (MHz)")
ax1.set_yticks(range(len(voltages)), voltages)
ax1.set_ylabel("Voltage (V)")

#fig.colorbar(cax)
plt.title("BearlyML Core Booting Status Shmoo Plot")

plt.show()

'''

fig, ax1 = plt.subplots()

cax = ax1.matshow(powers, cmap="hot")


ax1.set_xticks(range(len(frequencies)), frequencies)
ax1.xaxis.set_ticks_position("bottom")
ax1.set_xlabel("Frequency (MHz)")
ax1.set_yticks(range(len(voltages)), voltages)
ax1.set_ylabel("Voltage (V)")

fig.colorbar(cax)
plt.title("BearlyML Core Power Consumption Shmoo Plot (Watt)")

plt.show()


'''

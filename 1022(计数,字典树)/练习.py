
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize = (20,8) ,dpi = 100)
x = [1,2,3]
y = [1,2,3]
plt.plot(x,y)
y_ticks = range(40)
x_ticks_labels = ["11点{}分".format(i) for i in x]
plt.yticks(y_ticks[::5])
plt.xticks(x[::5],x_ticks_labels[::5])
plt.grid(True,linestyle="--")
import numpy as np
import matplotlib.pyplot as plt

rad = np.arange(0, np.pi*2, 0.01)
data = np.arange(0,1.1,0.01)

p1 = plt.figure(figsize=(8,6),dpi=80)
ax1 = p1.add_subplot(2,1,1)
plt.title('lines')
plt.xlabel('x')
plt.ylabel('t')
plt.xlim((0,1))
plt.ylim((0,1))
plt.xticks([0,0.2,0.4,0.6,0.8,1])
plt.yticks([0,0.2,0.4,0.6,0.8,1])
plt.plot(data,data**2)
plt.plot(data,data**4)
plt.legend(['y=x^2','y=x^4'])

ax2 = p1.add_subplot(2,1,2)
plt.rcParams['lines.linestyle'] = '--'
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.title('sin/cos曲线')
plt.xlabel('rad')
plt.ylabel('value')
plt.xlim((0,np.pi*2))
plt.ylim((-1,1))
plt.xticks([0,np.pi/2,np.pi,np.pi*1.5,np.pi*2])
plt.yticks([-1,-0.5,0,0.5,1])
plt.plot(rad,np.sin(rad))
plt.plot(rad,np.cos(rad))
plt.legend(['sin','cos'])
plt.show()
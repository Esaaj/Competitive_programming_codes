import matplotlib.pyplot as plt
import matplotlib.animation as animation
import ambient as am 
fig = plt.figure()

ax1 = fig.add_subplot(3,3,1)
ax1.set_title('Temperature')

ax2 = fig.add_subplot(3,3,2)
ax2.set_title('Gas')

ax3 = fig.add_subplot(3,3,3)
ax3.set_title('Humidity')

ax4 = fig.add_subplot(3,3,4)
ax4.set_title('Pressure')

ax5 = fig.add_subplot(3,3,5)
ax5.set_title('Altitude')

ax6 = fig.add_subplot(3,3,6)
ax6.set_title('LUX')

ax7 = fig.add_subplot(3,3,7)
ax7.set_title('Infrared')

ax8 = fig.add_subplot(3,3,8)
ax8.set_title('Visible')

ax9 = fig.add_subplot(3,3,9)
ax9.set_title('Full Spectrum')


def animate(i):
    pass


ani = animation.FuncAnimation(fig, animate, interval=1000)
#plt.title("AMBIENT MODULE LIVE GRAPH")
plt.show()
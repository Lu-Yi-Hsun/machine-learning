import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()
#equation title
plt.xlabel('$\epsilon$')
fig.suptitle(r'$\mathbb{P}[|v-\mu|>\epsilon]\leq2e^{-2\epsilon^{2}N}$',fontsize=20,color="black",alpha=0.6)
plt.subplots_adjust(left=0.25, bottom=0.25)
hypothesis=2 #set how many hypothesis set
x = np.arange(0.0, 1.0, 0.001)

a0 = 5


s=2*hypothesis*np.exp((-2*x**2)*a0)
l, = plt.plot(x, s, lw=2, color='red')
#plt.axis([0, 1, -10, 10])

axcolor = 'lightgoldenrodyellow'
 
axamp = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)

 
samp = Slider(axamp, 'N', 0.0, 1000.0, valinit=a0)


def update(val):
    amp = samp.val
    
    l.set_ydata(2*hypothesis*np.exp((-2*x**2)*amp))
    fig.canvas.draw_idle()
 
samp.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
 
    samp.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)



def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)


plt.show()

import numpy as np
import matplotlib.pyplot as plt

### Define and display numerical grid x and grid function f.
x = np.array([-5,-4,-3,0,1,4,5],dtype=float)
f = x**3 - 20*x + 25

### Compute arithmetic means and differences.
xm = 0.5*( x[1:] + x[:-1] )
dx = x[1:] - x[:-1]
df = f[1:] - f[:-1]

### Compute approximate and exact derivatives.
dfodx_approx = df/dx
dfodx_exact  = 3*xm**2 - 20

### Plot results.
fig,axs = plt.subplots(1,2,figsize=(10,4))
axs[0].plot(x,f,'b:')
axs[0].set_title('Grid function')
axs[0].set_xlabel('Numerical grid coordinate')
axs[1].plot(xm,dfodx_exact,'g:',label='Exact derivative')
axs[1].plot(xm,dfodx_approx,'kd',label='Approximate derivative')
axs[1].set_title('First derivative')
axs[1].set_xlabel('Numerical grid coordinate')
axs[1].legend()
import numpy as np
import matplotlib.pyplot as plt
from time import time

def polylsq(x, y, m):
    '''
    Computes an mth order polynomial least squares fit through origin
    (no constant term) and generates a plot of the data points and 
    least squares fit graph.
    Input:
        x : list of floats, data point x values
        y : list of floats, data point y values
        m : degree of least-squares fit polynomial
    Output:
        a : list of floats, coefficients of polynomial
    '''
    # construct design matrix and Gram's matrix
    n = len(x)
    X = np.zeros((n,m))
    X_T = np.zeros((m,n))
    for i in range(n):
        for j in range(m):
            X[i,j] = x[i]**(j+1)
            X_T[j,i] = X[i,j]
    G = X_T @ X
    
    # solve for a
    a = np.linalg.solve(G, X_T @ y)
    
    # plot x vs y
    plt.figure()
    plt.plot(x, y, 'ko')
    lsq_x = np.linspace(x[0], x[-1], 100)
    lsq_y = np.polyval(np.append([0], a)[::-1], lsq_x)
    plt.plot(lsq_x, lsq_y, 'b-')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Polynomial least squares fit of degree {m}")
    plt.grid()
    plt.show()
    
    return a

def rk4sys(f, t, t_0, val_0, h):
    '''
    Solve ODE numerically using the fourth-order Runge-Kutta method.
    Input:
        f = function with inputs t, list of values (e.g., [x, y]), 
            and output list of derivatives (e.g., [dx/dt, dy/dt])
        t = float, time for which we solve for
        t_0 = float, initial condition time
        val_0 = list of initial condition values at t = t_0
        h = float, step size
    Output:
        t_list = list of floats, time values for each step
        val_list = nested list of lists of float values for each step
    '''
    # initialize values for recursion
    steps = round((t - t_0) / h)
    t_i = t_0
    val_i = val_0
    
    # initialize lists (for return)
    t_list = [t_0]
    val_list = []
    for n in range(len(val_0)):
        val_list.append([val_i[n]])
    
    # 4th order runge-kutta method
    for i in range(int(steps)):
        k_1 = np.array(f(t_i, val_i))
        k_2 = np.array(f(t_i+h/2, val_i+k_1*h/2))
        k_3 = np.array(f(t_i+h/2, val_i+k_2*h/2))
        k_4 = np.array(f(t_i+h, val_i+k_3*h))
        slope = (k_1+2*k_2+2*k_3+k_4)/6
        
        val = val_i + slope*h
        t_i = t_i + h
        val_i = val
        t_list.append(t_i)
        for n in range(len(val_0)):
            val_list[n].append(val_i[n])
    
    return t_list, val_list

def forward_euler(f, t, t_0, val_0, h):
    '''
    Solve ODE numerically using explicit Euler method.
    Input:
        f = function with inputs t, list of values (e.g., [x, y]), 
            and output list of derivatives (e.g., [dx/dt, dy/dt])
        t = float, time for which we solve for
        t_0 = float, initial condition time
        y_0 = list of floats, initial condition values at t = t_0
        h = float, step size
    Output:
        t_list = list of floats, time values for each step
        val_list = nested list of lists of float values for each step
    '''
    # initialize values for recursion
    steps = round((t - t_0) / h)
    t_i = t_0
    val_i = val_0
    
    # initialize lists (for return)
    t_list = [t_0]
    val_list = []
    for n in range(len(val_0)):
        val_list.append([val_i[n]])
        
    # forward euler method
    for i in range(int(steps)):
        val = val_i + np.array(f(t_i, val_i))*h
        t_i = t_i + h
        val_i = val
        t_list.append(t_i)
        for n in range(len(val_0)):
            val_list[n].append(val_i[n])
    
    return t_list, val_list

def lagrange(x,y,xx):
    """
    Constructs a Lagrange interpolating polynomial
    Uses an (n-1)th-order Lagrange interpolating polynomial
    based on n data pairs.
    Input:
        x = array of independent variable values
        y = array of dependent variable values
        xx = list of independent variables to plot interpolation
    Output:
        yy = list of dependent variables of interpolation polynomial
    """
    n = len(x)
    if len(y) != n:
        return 'x and y must be of same length'
    
    s = 0
    for i in range(n):
        # calculate Lagrange Interpolant Functions
        product = 1
        for j in range(n):
            if i != j:
                product = product * (xx - x[j])/(x[i]-x[j])   
        # calculate Lagrange Interpolating Polynomial
        s = s + product*y[i]
    
    # plot Lagrange Interpolating Polynomial
    plt.figure()
    plt.plot(xx,s)
    plt.scatter(x,y)
    plt.xlabel('t (s)')
    plt.ylabel('x2 (m)')
    plt.title('Lagrange Interpolating Polynomial')
    plt.grid()
    yint = s
    return yint

def secant(f,x0,x1,Ea=1.e-7,maxit=30):
    """
    This function solves f(x)=0 using the Secant method.
    The method is repeated until either the relative error
    falls below Ea (default 1.e-7) or reaches maxit (default 30).
    Inputs:
        f = name of the function for f(x)
        fp = name of the function for f'(x)
        x0 = previous initial guess for x
        x1 = initial guess for x
        Ea = relative error threshold
        maxit = maximum number of iterations
    Output:
        x = solution estimate
    """  
    # initialize parameters of loop
    i = 0
    ea = Ea + 1
    x_list = [x0, x1]
    ea_list = []
    
    # secant method
    while i < maxit and ea > Ea:
        x = x_list[-1] - \
            f(x_list[-1])*(x_list[-1]-x_list[-2])/(f(x_list[-1])-f(x_list[-2]))
        ea = abs((x - x_list[-1]) / x)
        ea_list.append(ea)
        x_list.append(x)
        i = i+1
    
    return x

def trapezoidal(t, f):
    """
    Performs a numerical integration using the trapezoidal rule.
    Input:
        t = array of floats, values to integrate over
        f = array of floats, values of integrand corresponding to t
    Output:
        I_f = float, I(f), integral of function
    """
    n = len(t)
    if len(f) != n:
        return 't and f must be of same length'
    
    # Trapezoidal rule
    I_f = 0
    for i in range(0,n-1):
        I_f = I_f + (t[i+1]-t[i])*(f[i]+f[i+1])/2
    
    return I_f

def simpsons_3(t, f):
    """
    Performs a numerical integration using Simpson's 1/3 rule'
    Input:
        t = array of floats, values to integrate over
        f = array of floats, values of integrand corresponding to t
    Output:
        I_f = float, I(f), integral of function
    """
    n = len(t)
    if len(f) != n:
        return 't and f must be of same length'
    
    # Simpson's 1/3 rule
    I_f = 0
    for i in range(0,n-2,2):
        I_f = I_f + (t[i+2]-t[i])*(f[i]+4*f[i+1]+f[i+2])/6
    
    return I_f

# 1a

# Read F_s and F_d data
data_sp = np.genfromtxt('sp26-portfolio-kk227325/_projects/2026-two-story-building-model/springforce.csv', delimiter=',')
t_sp = data_sp[:,0]
f_sp = data_sp[:,1]

data_d = np.genfromtxt('sp26-portfolio-kk227325/_projects/2026-two-story-building-model/dampingforce.csv', delimiter=',')
t_d = data_d[:,0]
f_d = data_d[:,1]

# Polyomial least-squares fit of data
a_sp = polylsq(t_sp, f_sp, 3)
a_d = polylsq(t_d, f_d, 2)

k1, k2, k3 = a_sp   # coefficients for F_sp
c1, c2 = a_d        # coefficients for F_d

print(a_sp)
print(a_d)
print()

# 1c
# Define constants, given functions
m1 = 533.5
m2 = 552.5
kf = 456000
cf = 68.7
t_0 = 0
val_0 = [0,0,0,0]

def F_sp(delta_x):      # spring force
    return k1*delta_x + k2*delta_x**2 + k3*delta_x**3

def F_d(delta_v):       # damping force
    return c1*delta_v + c2*delta_v**2

def simulation_rk(t_end, A, T, h):
    # Define constants, given functions
    freq = 2*np.pi/T    
    
    def a_g(t):             # ground acceleration due to earthquake
        if t >= 0 and t <= T:
            return A*np.sin(freq*t)
        else:
            return 0
        
    def f(t, val):   # system of ODEs
        x1, x2, v1, v2 = val
        a1 = 1/m1 * (F_d(v2-v1) + F_sp(x2-x1) - cf*v1 - kf*x1) - a_g(t)
        a2 = -1/m2 * (F_d(v2-v1) + F_sp(x2-x1)) - a_g(t)
        return [v1, v2, a1, a2]
    
    # Solve ODE system
    start_time = time()
    t_list, val_list = rk4sys(f, t_end, t_0, val_0, h)
    elapsed_time = time() - start_time
    x1_list = val_list[0]
    x2_list = val_list[1]
    v1_list = val_list[2]
    v2_list = val_list[3]

    # Plot x1, x2, v1, v2 vs t
    fig, ax = plt.subplots(2,2)
    ax[0,0].plot(t_list, x1_list)
    ax[0,0].set_xlabel('t (s)')
    ax[0,0].set_ylabel('x (m)')
    ax[0,0].set_title('x1')
    ax[0,0].grid(True)
    ax[0,1].plot(t_list, x2_list)
    ax[0,1].set_xlabel('t (s)')
    ax[0,1].set_ylabel('x (m)')
    ax[0,1].set_title('x2')
    ax[0,1].grid(True)
    ax[1,0].plot(t_list, v1_list)
    ax[1,0].set_xlabel('t (s)')
    ax[1,0].set_ylabel('v (m/s)')
    ax[1,0].set_title('v1')
    ax[1,0].grid(True)
    ax[1,1].plot(t_list, v2_list)
    ax[1,1].set_xlabel('t (s)')
    ax[1,1].set_ylabel('v (m/s)')
    ax[1,1].set_title('v2')
    ax[1,1].grid(True)
    plt.suptitle(f'Runge-Kutta, A = {A} m/s^2, T = {T}s, h = {h}s')
    plt.tight_layout()
    plt.show()
    
    return t_list, x1_list, x2_list, v1_list, v2_list, elapsed_time



# 2a/b
    
# Run simulation for two earthquakes
A1 = 4.4
A2 = 16
T = 2.5
t_end = 10
h1 = T/200
t_list_rk, x1_list_rk1, x2_list_rk1, v1_list_rk1, v2_list_rk1, \
    elapsed_time_rk = simulation_rk(t_end, A1, T, h1)
t_list_rk, x1_list_rk2, x2_list_rk2, v1_list_rk2, v2_list_rk2, \
    elapsed_time_rk = simulation_rk(t_end, A2, T, h1)
h1_new = T/400
simulation_rk(t_end, A1, T, h1_new)
simulation_rk(t_end, A2, T, h1_new)

# 2c

def simulation_euler(t_end, A, T, h):
    # Define constants, given functions
    freq = 2*np.pi/T
    
    def a_g(t):             # ground acceleration due to earthquake
        if t >= 0 and t <= T:
            return A*np.sin(freq*t)
        else:
            return 0
    
    def f(t, val):   # system of ODEs
        x1, x2, v1, v2 = val
        a1 = 1/m1 * (F_d(v2-v1) + F_sp(x2-x1) - cf*v1 - kf*x1) - a_g(t)
        a2 = -1/m2 * (F_d(v2-v1) + F_sp(x2-x1)) - a_g(t)
        return [v1, v2, a1, a2]
    
    # Solve ODE system
    start_time = time()
    t_list, val_list = forward_euler(f, t_end, t_0, val_0, h)
    elapsed_time = time() - start_time
    x1_list = val_list[0]
    x2_list = val_list[1]
    v1_list = val_list[2]
    v2_list = val_list[3]
    
    # Plot x1, x2, v1, v2 vs t
    fig, ax = plt.subplots(2,2)
    ax[0,0].plot(t_list, x1_list)
    ax[0,0].set_xlabel('t (s)')
    ax[0,0].set_ylabel('x (m)')
    ax[0,0].set_title('x1')
    ax[0,0].grid(True)
    ax[0,1].plot(t_list, x2_list)
    ax[0,1].set_xlabel('t (s)')
    ax[0,1].set_ylabel('x (m)')
    ax[0,1].set_title('x2')
    ax[0,1].grid(True)
    ax[1,0].plot(t_list, v1_list)
    ax[1,0].set_xlabel('t (s)')
    ax[1,0].set_ylabel('v (m/s)')
    ax[1,0].set_title('v1')
    ax[1,0].grid(True)
    ax[1,1].plot(t_list, v2_list)
    ax[1,1].set_xlabel('t (s)')
    ax[1,1].set_ylabel('v (m/s)')
    ax[1,1].set_title('v2')
    ax[1,1].grid(True)
    plt.suptitle(f'Forward Euler, A = {A} m/s^2, T = {T}s, h = {h}s')
    plt.tight_layout()
    plt.show()
    
    return t_list, x1_list, x2_list, v1_list, v2_list, elapsed_time

# Extract values at t=2T from Runge-Kutta results
i_rk = round(2*T/h1)
x1_rk_2T = x1_list_rk1[i_rk]
x2_rk_2T = x1_list_rk1[i_rk]
v1_rk_2T = v1_list_rk1[i_rk]
v2_rk_2T = v2_list_rk1[i_rk]
print(f'Values for t = 2T, Runge-Kutta, h = {h1}')
print(f'x1 = {x1_rk_2T}')
print(f'x2 = {x2_rk_2T}')
print(f'v1 = {v1_rk_2T}')
print(f'v2 = {v2_rk_2T}')
print(f'{elapsed_time_rk=}')
print()

# Initialize values for iteration with Forward Euler method
h2 = T/6400

# Compare Forward Euler accuracy and efficiency with Runge-Kutta
t_list_fe, x1_list_fe, x2_list_fe, v1_list_fe, v2_list_fe, \
    elapsed_time_fe = simulation_euler(t_end, A1, T, h2)

i_fe = round(2*T/h2)
x1_fe_2T = x1_list_fe[i_fe]
x2_fe_2T = x1_list_fe[i_fe]
v1_fe_2T = v1_list_fe[i_fe]
v2_fe_2T = v2_list_fe[i_fe]

x1_error = abs(x1_rk_2T - x1_fe_2T)
x2_error = abs(x2_rk_2T - x2_fe_2T)
v1_error = abs(v1_rk_2T - v1_fe_2T)
v2_error = abs(v2_rk_2T - v2_fe_2T)
    
print(f'Values for t = 2T, Forward Euler, h = {h2}')
print(f'x1 = {x1_fe_2T}, error = {x1_error}')
print(f'x2 = {x2_fe_2T}, error = {x2_error}')
print(f'v1 = {v1_fe_2T}, error = {v1_error}')
print(f'v2 = {v2_fe_2T}, error = {v2_error}')
print(f'{elapsed_time_fe=}')
print()

h2 = T/10000
t_list_fe, x1_list_fe, x2_list_fe, v1_list_fe, v2_list_fe, \
    elapsed_time_fe = simulation_euler(t_end, A1, T, h2)

i_fe = round(2*T/h2)
x1_fe_2T = x1_list_fe[i_fe]
x2_fe_2T = x1_list_fe[i_fe]
v1_fe_2T = v1_list_fe[i_fe]
v2_fe_2T = v2_list_fe[i_fe]

x1_error = abs(x1_rk_2T - x1_fe_2T)
x2_error = abs(x2_rk_2T - x2_fe_2T)
v1_error = abs(v1_rk_2T - v1_fe_2T)
v2_error = abs(v2_rk_2T - v2_fe_2T)
    
print(f'Values for t = 2T, Forward Euler, h = {h2}')
print(f'x1 = {x1_fe_2T}, error = {x1_error}')
print(f'x2 = {x2_fe_2T}, error = {x2_error}')
print(f'v1 = {v1_fe_2T}, error = {v1_error}')
print(f'v2 = {v2_fe_2T}, error = {v2_error}')
print(f'{elapsed_time_fe=}')
print()

# 3a
# Find maximum acceleration for each earthquake
a2_1 = []
a2_2 = []
for i in range(1, len(t_list_rk)-1):
    a2_1.append((v2_list_rk1[i+1]-v2_list_rk1[i-1])/(2*h1))
    a2_2.append((v2_list_rk2[i+1]-v2_list_rk2[i-1])/(2*h1))
print(f'Max. Acceleration for A = {A1} m/s^2: {max(a2_1)} m/s^2')
print(f'Max. Acceleration for A = {A2} m/s^2: {max(a2_2)} m/s^2')
print()

plt.figure()
plt.plot(t_list_rk[1:-1],a2_2,label='A = 16 m/s^2')
plt.plot(t_list_rk[1:-1],a2_1,label='A = 4.4 m/s^2')
plt.xlabel('t (s)')
plt.ylabel('a (m/s^2)')
plt.title('Acceleration of the second floor for each earthquake')
plt.grid()
plt.legend()
plt.show()

# 3b
# Find when x2=0 for the first time for A = 4.4 m/s^2
t = 1.34            # guess of x2 zero crossing from graph
i_rk1 = round(t/h1)
t_ip1 = t_list_rk[i_rk1-2:i_rk1+3]
x2_ip1 = x2_list_rk1[i_rk1-2:i_rk1+3]
def P5_1(x):
    return lagrange(t_ip1, x2_ip1, x)
print(f'Zero-crossing for x2, A = {A1} m/s^2: {secant(P5_1, t+.01, t, 1.e-3)} s')

# Find when x2=0 for the first time for A = 16 m/s^2
t = 1.29            # guess of x2 zero crossing from graph
i_rk2 = round(t/h1)
t_ip2 = t_list_rk[i_rk2-2:i_rk2+3]
x2_ip2 = x2_list_rk2[i_rk2-2:i_rk2+3]
def P5_2(x):
    return lagrange(t_ip2, x2_ip2, x)
print(f'Zero-crossing for x2, A = {A2} m/s^2: {secant(P5_2, t+.01, t, 1.e-3)} s')
print()

# 3c
# Create arrays for integration and compute integrals
def integrand(v):
    return F_d(v)*v
i_T = round(T/h1)
t_list_T = np.array(t_list_rk[:i_T])

v1_list_T1 = np.array(v1_list_rk1[:i_T])
v2_list_T1 = np.array(v2_list_rk1[:i_T])
E_trap1 = trapezoidal(t_list_T, integrand(v2_list_T1 - v1_list_T1))
E_simpson1 = simpsons_3(t_list_T, integrand(v2_list_T1 - v1_list_T1))
print('Energy lost due to damping')
print(f"A = {A1} m/s^2, Trapezoidal rule: {E_trap1} J")
print(f"A = {A1} m/s^2, Simpson's 1/3 rule: {E_simpson1} J")
print(f'Relative difference = {abs((E_simpson1-E_trap1)/E_simpson1)}')

v1_list_T2 = np.array(v1_list_rk2[:i_T])
v2_list_T2 = np.array(v2_list_rk2[:i_T])
E_trap2 = trapezoidal(t_list_T, integrand(v2_list_T2 - v1_list_T2))
E_simpson2 = simpsons_3(t_list_T, integrand(v2_list_T2 - v1_list_T2))
print(f"A = {A2} m/s^2, Trapezoidal rule: {E_trap2} J")
print(f"A = {A2} m/s^2, Simpson's 1/3 rule: {E_simpson2} J")
print(f'Relative difference = {abs((E_simpson2-E_trap2)/E_simpson2)}')

'''
Here's a program that uses Euler's Method to find an approximation to a solution
using the equation yk = yk-1 + f(tk-1, yk-1) * delta t

The program depends on user inputs on y(0), dy/dt, target, and the time-step delta t

NOTE: I used https://www.geeksforgeeks.org/eval-in-python/ code to make eval safe
'''
from math import *

def userInputs():
    print("Please provide the following information for the Euler's Method Algorithm: \n")

    #Getting user input
    derivative = input("f(t0,y0) or aka the derivative dy/dt \n"
                       "NO Spaces please: (Ex. 2*y-1 or y**(2*t+3)\n")
    t = float(input("What is the initial t value? t = ")) #t0
    y = float(input("y at initial value; y(%g) = " %t)) #y#0
    deltaT = float(input("delta t (should be as minimized as possible): "))
    tFinal = float(input("What t value are you approximating y for? %g >= t <= ?: " %t))

    return derivative, t, y, deltaT, tFinal

'''
Creating a function based on string. Putting safe dict so only specific math formulas can be used
Function to find derivative value
    '''
def f(t, y, derivative):
    #list of safe methods
    safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos',
				'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
				'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10',
				'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt',
				'tan', 'tanh']
    # creating a dictionary of safe methods
    safe_dict = dict([(k, locals().get(k, None)) for k in safe_list])
    
    #adding variables used in expression
    safe_dict['y'] = y
    safe_dict['t'] = t
    
    dydt = eval (derivative, {"__builtins__": None}, safe_dict)

    return dydt

if __name__ == "__main__":
    #calling function for user inputs
    derivative, t, y, deltaT, tFinal = userInputs()

    
    #Doing the calculations
    #Finding how many k times to find approximation
    k = int((tFinal - t) / deltaT)

    #calculating k times
    for i in range(k):
        #calculating the derivative
        dydt = f(t,y, derivative)

        #using general formula
        yk =  y + dydt * deltaT

        #updates t0 and y0
        t += deltaT
        y = yk

        #prints each value at deltaT intervals, printing table
        print("(t,y) = (%g,%g), dy/dt = %g" %(t, y, dydt))
    



    #printing final answer output
    print("y(%g) = %g" %(t, y))

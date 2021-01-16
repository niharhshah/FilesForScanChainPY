def output(x,y):
    return (x+y)
import Module 
Module.opfn = output
'''
Removeing above line can cause a No Implementation Error.
This bindes outer function to internal function -- Very very Important line
''' 
x,y = Module.setup()
Module.CheckFunction(x,y)
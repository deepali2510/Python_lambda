# Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers
# using lambda function.
l=[10,-20,45,50,-60,70]
# without lambda function
pos =print(sum( [i for i in l if i>0]))
neg =print(sum( [i for i in l if i<0]))
# with lambda function
pos = [i for i in l if i>0]
neg = [i for i in l if i<0]
from functools import reduce
print(reduce((lambda x,y:x+y),pos))
print(reduce((lambda x,y:x+y),neg))
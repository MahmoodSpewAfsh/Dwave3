from vpython import *


# redbox=box(pos=vector(4,-5,3),
#            size=vector(8,4,6),color=color.white)
for i in range(5, 10):
    ball=sphere(pos=vector(i,7,3),radius=0.2,color=color.green)

# a = vec(2,2,3) # can also be written briefly as vec(1,2,3)
# b = vec(4,5,6)
# c = a+b


# f1 = gcurve(color=color.cyan) # a graphics curve
# for x in arange(0, 8.05, 0.1): # x goes from 0 to 8
#     f1.plot( x,5*cos(2*x)*exp(-0.2*x)) 

# f1 = gcurve(data=[ [1,2],[5,-2],[8,4] ],
#             color=color.green)


# points(pos=[vector(-1,0,0), vector(0,1,0)], radius=5, color=color.red, background = color.white)
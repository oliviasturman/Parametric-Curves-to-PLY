import math
import pointshape as ps

#winter
    # x = 4sin(t)*cos(t), y = sin(3t)*sin(t)*cos(t), z = sin(t) + t
    # x = cos(t), y = sin(3t)*sin(t)*cos(t), z = sin(t) + t
    # x = 5cos(t)-cos(2t)+sin(5*t), y = 5sin(t)-sin(2*t)+cos(3*t), z = t

#spring
    # x = 4sin(t)*cos(t), y = sin(3t)*sin(t), z = sin(t)+t
    # x = t^3*sin(t), y = t*cos(2t), z = 2t

#summer
    # x = 2sin(3t)*cos(t), y = sin(3t)*sin(t), z = sin(t)+t
    # x =  2sin(t)*cos(t), y = sin(3t)*sin(t), z = sin(t)+t
    # x = t*sin(t), y = sin(3t)+sin(t)+cos(t), z = t^2+sin(t)
    # x = 4t^5 * 3t^4 + 9t^2 - 6*t

#t step = .1

def winter_branch1():
    cloud = ps.PointCloud()
    shape = ps.Shape(cloud)
    t = 0
    while t < 2*math.pi:
        x = 4*math.sin(t) * math.cos(t)
        y = math.sin(3*t) * math.sin(t) * math.cos(t)
        z = math.sin(t) + t
        cloud.add(ps.Point(x,y,z))
        t += .1

    return shape


def winter_branch2():
    cloud = ps.PointCloud()
    shape2 = ps.Shape(cloud)
    t = 0
    while t < 2 * math.pi:
        x = math.cos(t)
        y = math.sin(3*t) * math.sin(t) * math.cos(t)
        z = math.sin(t) + t
        cloud.add(ps.Point(x,y,z))
        t += .1

    return shape2

def winter_branch3f():
    cloud = ps.PointCloud()
    shape3 = ps.Shape(cloud)
    t = 0
    while t < 2 * math.pi:
        x = 5*math.cos(t)-math.cos(2*t) + math.sin(5*t)
        y = 5*math.sin(t)-math.sin(2*t)+math.cos(3*t)
        z = t
        cloud.add(ps.Point(x,y,z))
        t += 0.1

    return shape3

def spring_branch1():
    cloud = ps.PointCloud()
    shape4 = ps.Shape(cloud)
    t = 0
    while t < 2 * math.pi:
        x = 4*math.sin(t)*math.cos(t)
        y = math.sin(3*t)*math.sin(t)
        z = math.sin(t)+t
        cloud.add(ps.Point(x,y,z))
        t += 0.1

    return shape4

def spring_branch2():
    cloud = ps.PointCloud()
    shape5 = ps.Shape(cloud)
    t = 0
    while t < 2 * math.pi:
        x = (t**t)*math.sin(t)
        y = t*math.cos(2*t)
        z = 2*t
        cloud.add(ps.Point(x,y,z))
        t += 0.1

    return shape5

def summer_branch1():
    cloud = ps.PointCloud()
    shape9 = ps.Shape(cloud)
    t = 0
    while t < 2 * math.pi:
        x = 2*math.sin(3*t)*math.cos(t)
        y = math.sin(3*t)*math.sin(t)
        z = math.sin(t)+t
        cloud.add(ps.Point(x,y,z))
        t += 0.1

    return shape9

def summer_branch2():
    cloud = ps.PointCloud()
    shape6 = ps.Shape(cloud)
    t = 0
    while t < 2 * math.pi:
        x = 2*math.sin(t)*math.cos(t)
        y = math.sin(3*t)*math.sin(t)
        z = math.sin(t)+t
        cloud.add(ps.Point(x,y,z))
        t += 0.1

    return shape6

def summer_branch3():
    cloud = ps.PointCloud()
    shape7 = ps.Shape(cloud)
    t = 0
    while t < 2 * math.pi:
        x = t*math.sin(t)
        y = math.sin(3*t)+math.sin(t)+math.cos(t)
        z = (t*t)+math.sin(t)
        cloud.add(ps.Point(x,y,z))
        t += 0.1

    return shape7

def summer_branch4():
    cloud = ps.PointCloud()
    shape8 = ps.Shape(cloud)
    t = 0
    while t < 2 * math.pi:
        x = 4*(t**5) * 3*(t**4) + 9*(t*t) - 6*t
        y = t
        z = (t*t)
        cloud.add(ps.Point(x,y,z))
        t += 0.1

    return shape8

def olivia_branch():
    cloud = ps.PointCloud()
    shape0 = ps.Shape(cloud)
    t = 0
    while t < 5 * math.pi:
        x = 5*math.cos(t)-5*math.cos(2*t)+math.sin(9*t)
        y = 5*math.sin(t)-5*math.sin(2*t)-math.cos(3*t)
        z = t
        cloud.add(ps.Point(x,y,z))
        t += 0.1

    return shape0

def leanne_branch():
    cloud = ps.PointCloud()
    shapel = ps.Shape(cloud)
    t = 0
    while t < 3.1 * math.pi:
        x = 5*math.cos(t)-math.cos(4*t)+5*math.sin(5*t)
        y = 5*math.sin(t)-math.sin(5*t)-math.cos(3*t)
        z = t
        cloud.add(ps.Point(x,y,z))
        t += 0.1

    return shapel



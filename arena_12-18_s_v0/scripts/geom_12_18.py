from __future__ import print_function
import math
import scipy
import matplotlib.pyplot as plt

# these are the depth and width of the LED module in inches
posDataOutFile = 'pos_data.txt'
edgDataOutFile = 'edg_data.txt'
plot = False
numPanels = 18 
numRemove = 6 
numPins = 15
panelWidth = 40.0/25.4 + 0.01
panelDepth = 0.7125 
pinDist = 0.6; # Distance from the front surface to pins  
pinSpacing = 0.1
pinWidth = (numPins - 1)*pinSpacing; 
xOffset = 8.0
yOffset = 9.0
in2mm = 25.4

subAngle = 2.0*math.pi/numPanels;   #angle subtended by one panel from center
radius = panelWidth/(math.tan(subAngle/2.0))/2.0
backRadius = radius + panelDepth
arcRadius = radius - 0.0
edgDim = 6.5*2 

shifterRadius = backRadius  + 0.8
shuntRadius = shifterRadius - 0.55
innerResRadius = shifterRadius - 0.55
outerResRadius = shifterRadius
misoCapRadius = shifterRadius - 0.55
filtCapRadius = backRadius + 0.8

innerResOffsetY = -0.2
outerResOffsetY = 0.6 
misoCapOffsetY = 0.25

circPosAngleArray = scipy.arange(0.0, 2.0*math.pi,subAngle)
circPosAngleArray = circPosAngleArray[:-numRemove]
circPosAngleArray = circPosAngleArray + numRemove*subAngle/2.0 + subAngle/2.0 - math.pi/2.0 + math.pi
panelAngleArray = circPosAngleArray + math.pi/2



angleIndList = range(panelAngleArray.shape[0])
numAngle = len(angleIndList)
panelRefList = ['P{0}'.format(i+1) for i in angleIndList]
shifterRefList = ['U{0}'.format(i+1) for i in angleIndList] 
shuntRefList = ['P{0}'.format(i+numAngle+1) for i in angleIndList] 
innerResRefList = ['R{0}'.format(i+1) for i in angleIndList]
outerResRefList = ['R{0}'.format(i+numAngle+1) for i in angleIndList]
misoCapRefList =['C{0}'.format(i+1) for i in angleIndList]
filtCapRefList = ['C{0}'.format(i+numAngle+1) for i in range(numAngle-1)]

filtCapCircPosAngleList = []
panelMidAngleList = []
for i in range(1,numAngle):
    circPosAng0 = circPosAngleArray[i-1]
    circPosAng1 = circPosAngleArray[i]
    filtCapAngle = 0.5*(circPosAng0 + circPosAng1)
    filtCapCircPosAngleList.append(filtCapAngle)

    panelAng0 = panelAngleArray[i-1]
    panelAng1 = panelAngleArray[i]
    panelMidAng = 0.5*(panelAng0 + panelAng1)
    panelMidAngleList.append(panelMidAng)


zippedAngles = zip(circPosAngleArray, panelAngleArray)


fig = plt.figure()

for circPosAngle, panelAngle in zippedAngles:
    x = radius*math.cos(circPosAngle) + xOffset
    y = radius*math.sin(circPosAngle) + yOffset
    x0 = x - (panelWidth/2.0)*math.cos(panelAngle)
    x1 = x + (panelWidth/2.0)*math.cos(panelAngle)
    y0 = y - (panelWidth/2.0)*math.sin(panelAngle)
    y1 = y + (panelWidth/2.0)*math.sin(panelAngle)
    plt.plot([x0,x1],[y0,y1],'g')

    p = backRadius*math.cos(circPosAngle) + xOffset
    q = backRadius*math.sin(circPosAngle) + yOffset
    p0 = p - (panelWidth/2.0)*math.cos(panelAngle)
    p1 = p + (panelWidth/2.0)*math.cos(panelAngle)
    q0 = q - (panelWidth/2.0)*math.sin(panelAngle)
    q1 = q + (panelWidth/2.0)*math.sin(panelAngle)
    plt.plot([p0,p1],[q0,q1],'k')

    plt.plot([p0,x0],[q0,y0],'k')
    plt.plot([p1,x1],[q1,y1],'k')


panelPosList = []
for circPosAngle, panelAngle in zippedAngles:
    x = (radius + pinDist)*math.cos(circPosAngle) + xOffset
    y = (radius + pinDist)*math.sin(circPosAngle) + yOffset
    xList = [x - (pinWidth/2.0)*math.cos(panelAngle)]
    yList = [y - (pinWidth/2.0)*math.sin(panelAngle)]
    for i in range(1,numPins):
        xList.append(xList[i-1] + pinSpacing*math.cos(panelAngle))
        yList.append(yList[i-1] + pinSpacing*math.sin(panelAngle))
    plt.plot(xList,yList, '.k')
    xMid = scipy.array(xList).mean()
    yMid = scipy.array(yList).mean()
    panelPosList.append((xMid,yMid))
    plt.plot([xMid], [yMid], '.r')



shifterPosList = []
shifterAngleList = []
for circPosAngle, panelAngle in zippedAngles:
    x = shifterRadius*math.cos(circPosAngle) + xOffset
    y = shifterRadius*math.sin(circPosAngle) + yOffset
    print(x,y)
    shifterPosList.append((x,y))
    shifterAngleList.append(panelAngle + math.pi/2.0)


shuntPosList = []
shuntAngleList = []
for circPosAngle, panelAngle in zippedAngles:
    x = shuntRadius*math.cos(circPosAngle) + xOffset
    y = shuntRadius*math.sin(circPosAngle) + yOffset
    print(x,y)
    shuntPosList.append((x,y))
    shuntAngleList.append(panelAngle + math.pi/2.0)

innerResPosList = []
innerResAngleList = []
for circPosAngle, panelAngle in zippedAngles:
    x = innerResRadius*math.cos(circPosAngle) + xOffset
    y = innerResRadius*math.sin(circPosAngle) + yOffset 
    x = x + innerResOffsetY*math.cos(panelAngle)
    y = y + innerResOffsetY*math.sin(panelAngle)
    print(x,y)
    innerResPosList.append((x,y))
    innerResAngleList.append(panelAngle + 3*math.pi/2.0)

misoCapPosList = []
misoCapAngleList = []
for circPosAngle, panelAngle in zippedAngles:
    x = misoCapRadius*math.cos(circPosAngle) + xOffset
    y = misoCapRadius*math.sin(circPosAngle) + yOffset 
    x = x + misoCapOffsetY*math.cos(panelAngle)
    y = y + misoCapOffsetY*math.sin(panelAngle)
    print(x,y)
    misoCapPosList.append((x,y))
    misoCapAngleList.append(panelAngle + 3*math.pi/2.0)

outerResPosList = []
outerResAngleList = []
for circPosAngle, panelAngle in zippedAngles:
    x = outerResRadius*math.cos(circPosAngle) + xOffset
    y = outerResRadius*math.sin(circPosAngle) + yOffset 
    x = x + outerResOffsetY*math.cos(panelAngle)
    y = y + outerResOffsetY*math.sin(panelAngle)
    print(x,y)
    outerResPosList.append((x,y))
    outerResAngleList.append(panelAngle + 3*math.pi/2.0)

filtCapPosList = []
filtCapAngleList = []
for circPosAngle, panelMidAngle in zip(filtCapCircPosAngleList,panelMidAngleList):
    x = filtCapRadius*math.cos(circPosAngle) + xOffset
    y = filtCapRadius*math.sin(circPosAngle) + yOffset 
    print(x,y)
    filtCapPosList.append((x,y))
    filtCapAngleList.append(panelMidAngle + 3*math.pi/2.0)

plt.axis('equal')
if plot:
    plt.show()

with open(posDataOutFile,'w') as f:

    print('panel (x,y) angle')
    print('-----------------')
    for ref, pos, ang in zip(panelRefList, panelPosList, panelAngleArray):
        x, y = pos
        xmm = in2mm*x
        ymm = in2mm*y
        angDeg = ang*180.0/math.pi
        angDeg = -(angDeg%360)
        ang10xDeg = 10*angDeg
        f.write('{0} {1} {2} {3}\n'.format(ref,xmm,ymm,angDeg))
        print(ref, x, y, ang10xDeg)

    
    print()
    print('shifter (x,y) angle')
    print('-----------------')
    for ref, pos, ang in zip(shifterRefList, shifterPosList, shifterAngleList):
        x,y = pos
        xmm = in2mm*x
        ymm = in2mm*y
        angDeg = ang*180.0/math.pi
        angDeg = -(angDeg%360)
        ang10xDeg = 10*angDeg
        f.write('{0} {1} {2} {3}\n'.format(ref,xmm,ymm,angDeg))
        print(ref, x, y, ang10xDeg)


    print()
    print('shunt (x,y) angle')
    print('-----------------')
    for ref, pos, ang in zip(shuntRefList, shuntPosList, shuntAngleList):
        x,y = pos
        xmm = in2mm*x
        ymm = in2mm*y
        angDeg = ang*180.0/math.pi
        angDeg = -(angDeg%360)
        ang10xDeg = 10*angDeg
        f.write('{0} {1} {2} {3}\n'.format(ref,xmm,ymm,angDeg))
        print(ref, x, y, ang10xDeg)

    print()
    print('innerRes (x,y) angle')
    print('-----------------')
    for ref, pos, ang in zip(innerResRefList, innerResPosList, innerResAngleList):
        x,y = pos
        xmm = in2mm*x
        ymm = in2mm*y
        angDeg = ang*180.0/math.pi
        angDeg = -(angDeg%360)
        ang10xDeg = 10*angDeg
        f.write('{0} {1} {2} {3}\n'.format(ref,xmm,ymm,angDeg))
        print(ref, x, y, ang10xDeg)
    
    print()
    print('misoCap (x,y) angle')
    print('-----------------')
    for ref, pos, ang in zip(misoCapRefList, misoCapPosList, misoCapAngleList):
        x,y = pos
        xmm = in2mm*x
        ymm = in2mm*y
        angDeg = ang*180.0/math.pi
        angDeg = -(angDeg%360)
        ang10xDeg = 10*angDeg
        f.write('{0} {1} {2} {3}\n'.format(ref,xmm,ymm,angDeg))
        print(ref, x, y, ang10xDeg)

    print()
    print('outerRes (x,y) angle')
    print('-----------------')
    for ref, pos, ang in zip(outerResRefList, outerResPosList, outerResAngleList):
        x,y = pos
        xmm = in2mm*x
        ymm = in2mm*y
        angDeg = ang*180.0/math.pi
        angDeg = -(angDeg%360)
        ang10xDeg = 10*angDeg
        f.write('{0} {1} {2} {3}\n'.format(ref,xmm,ymm,angDeg))
        print(ref, x, y, ang10xDeg)

    print()
    print('filtCap (x,y) angle')
    print('-----------------')
    for ref, pos, ang in zip(filtCapRefList, filtCapPosList, filtCapAngleList):
        x,y = pos
        xmm = in2mm*x
        ymm = in2mm*y
        angDeg = ang*180.0/math.pi
        angDeg = -(angDeg%360)
        ang10xDeg = 10*angDeg
        f.write('{0} {1} {2} {3}\n'.format(ref,xmm,ymm,angDeg))
        print(ref, x, y, ang10xDeg)

# Get arc parameters
theta0 = circPosAngleArray.min() - subAngle
theta1 = circPosAngleArray.max() + subAngle
totalAngle = theta1 - theta0
xCenter = xOffset
yCenter = yOffset
arcX0 = arcRadius*math.cos(theta0) + xCenter
arcY0 = arcRadius*math.sin(theta0) + yCenter
arcX1 = arcRadius*math.cos(theta1) + xCenter
arcY1 = arcRadius*math.sin(theta1) + yCenter

xCenter_mm = in2mm*xCenter
yCenter_mm = in2mm*yCenter
arcX0mm = in2mm*arcX0
arcY0mm = in2mm*arcY0
arcX1mm = in2mm*arcX1
arcY1mm = in2mm*arcY1
totalAngleDeg = totalAngle*180.0/math.pi

edgDelta = edgDim/2.0 - arcRadius
edgX0 = xCenter - edgDim/2.0 
edgY0 = arcY0
edgX1 = edgX0
edgY1 = yCenter - edgDim/2.0

edgX2 = xCenter + edgDim/2.0
edgY2 = edgY1
edgX3 = edgX2
edgY3 = arcY1

edgPt = [(arcX0,arcY0), (edgX0,edgY0), (edgX1, edgY1), (edgX2,edgY2), (edgX3,edgY3), (arcX1, arcY1)]
edgPt_mm = [(in2mm*x, in2mm*y) for x,y in edgPt]

with open(edgDataOutFile,'w') as f:
    f.write('{0} {1} {2} {3} {4} {5}\n'.format('arc',xCenter_mm, yCenter_mm, arcX0mm, arcY0mm, totalAngleDeg))
    for i in range(1,len(edgPt_mm)):
        p = edgPt_mm[i-1]
        q = edgPt_mm[i]
        x0mm, y0mm = p
        x1mm, y1mm = q
        f.write('{0} {1} {2} {3} {4} {5}\n'.format('line',x0mm, y0mm, x1mm, y1mm,90.0))




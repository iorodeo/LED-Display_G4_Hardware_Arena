from __future__ import print_function

def readModule(fileName):
    moduleList = []
    with open(fileName,'r') as f:
        moduleList = f.readlines()
    moduleList = [x.strip() for x in moduleList]
    return moduleList

def writeModule(fileName,moduleList):
    moduleStr = '\n'.join(moduleList)
    with open(fileName,'w') as f:
        f.write(moduleStr)

def getPadList(pin,x,y,drillDiam,outerDiam):
    padList = [
            '$PAD', 
            'Sh "{0}" C {1} {1} 0 0 0'.format(pin,outerDiam), 
            'Dr {0} 0 0'.format(drillDiam), 
            'At STD N 00E0FFFF', 
            'Ne 0 ""', 
            'Po {0} {1}'.format(x,y), 
            '$EndPAD',
            ]
    return padList

def getEndModuleIndex(moduleList):
    found = True
    index = 0
    for i, line in enumerate(moduleList):
        if '$EndMODULE' in line:
            found = True
            index = i
            break
    if not found:
        raise RuntimeError('$EndMODULE not found')
    indexNeg = -(len(moduleList) - index)
    return indexNeg


# -----------------------------------------------------------------------------
if __name__ == '__main__':

    fileName = 'TE_CONN_DSUB_RA_68.mod'
    drillDiam = 0.8
    outerDiam = 1.2

    xStart = -20.955
    xStep = 1.27
    yStep = 1.905

    yStartEven = -9.515
    yStartOdd = yStartEven + yStep
    rowStep = 2*yStep

    numPins = 68
    numPinsPerRow = 34

    moduleList = readModule(fileName)
    endInd = getEndModuleIndex(moduleList)

    for pin in range(numPins):
        row = pin/numPinsPerRow
        pinPos = pin%numPinsPerRow
        if pin%2 == 0:
            x = xStart + pinPos*xStep
            y = yStartEven + row*rowStep
        else:
            x = xStart + pinPos*xStep
            y = yStartOdd + row*rowStep

        padList = getPadList(pin+1,x,y,drillDiam,outerDiam)
        moduleList[endInd:endInd] = padList

    writeModule(fileName,moduleList)


from __future__ import print_function
import sys


def loadPcbLines(filename):
    with open(filename,'r') as f:
        lineList = f.readlines()
    return lineList

def savePcbLines(lineList,filename):
    with open(filename,'w') as f:
        for line in lineList:
            f.write(line)

def loadRefToPosFile(filename):
    """
    Load data file specifying desired position and and orientation for modules
    by reference.
    """
    with open(filename,'r') as f:
        lineList = f.readlines()
    refToPosDict = {}
    for line in lineList:
        line = line.strip()
        line = line.split(' ')
        refToPosDict[line[0]] = tuple([float(x) for x in line[1:]])
    return refToPosDict
     

def findModuleIndex(pcbLineList, ref):
    """
    Returns the line index at which the moduels starts
    """
    lastModuleIndex = -1
    moduleIndex = None
    for i, line in enumerate(pcbLineList):
        if 'module' in line:
            lastModuleIndex = i
            continue
        refStr = ' {0} '.format(ref)
        if refStr in line:
            moduleIndex = lastModuleIndex
            break
    return moduleIndex 

def setModulePosition(pcbLineList,ref,pos):
    """
    Sets the module position
    """
    index = findModuleIndex(pcbLineList,ref)
    atLineIndex = index + 1
    atLine = pcbLineList[atLineIndex]
    atIndex = atLine.find('at')
    atLineMod = '{0}at {1} {2} {3})\n'.format(atLine[:atIndex],pos[0], pos[1], pos[2])
    pcbLineList[atLineIndex] = atLineMod


def loadEdgData(filename):
    with open(filename,'r') as f:
        lineList = f.readlines()
    edgList = []
    for line in lineList:
        line = line.strip()
        line = line.split(' ')
        edgType = line[0]
        edgData = [edgType] + [float(x) for x in line[1:]]
        edgList.append(edgData)
    return edgList 

def addEdgToPcb(pcbLineList,edgList):
    for edg in edgList:
        if edg[0] == 'arc':
            edgStr = '(gr_arc (start {0} {1}) (end {2} {3}) (angle {4}) (layer Edge.Cuts) (width 0.3))\n'.format(*edg[1:])
        elif edg[0] == 'line':
            edgStr = '(gr_line (start {0} {1}) (end {2} {3}) (angle {4}) (layer Edge.Cuts) (width 0.3))\n'.format(*edg[1:])
        else:
            raise ValueError, 'uknown edge type {0}'.format(edg[0])
        pcbLineList.insert(len(pcbLineList)-1,edgStr)


# --------------------------------------------------------------------------------
if __name__ == '__main__':

    inFile = 'arena.kicad_pcb.template'
    outFile = 'arena.kicad_pcb.mod'
    refToPosFile = 'pos_data.txt'
    edgDataFile =  'edg_data.txt'

    pcbLineList = loadPcbLines(inFile)
    refToPosDict = loadRefToPosFile(refToPosFile)
    edgList = loadEdgData(edgDataFile)

    for ref, pos in refToPosDict.iteritems():
        setModulePosition(pcbLineList,ref,pos)

    addEdgToPcb(pcbLineList,edgList)
    savePcbLines(pcbLineList,outFile)


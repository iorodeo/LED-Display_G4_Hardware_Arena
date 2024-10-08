from __future__ import print_function
import shutil


class LabelReplacer(object):

    def __init__(self,fileName, replaceMap, outFile=None, backup=True):
        self.fileName = fileName
        self.replaceMap = replaceMap
        self.backup = backup
        self.outFile = outFile
        self.origLineList = []
        self.replLineList = []

    def run(self):
        self.readFile()
        self.replaceLines()
        self.backupFile()
        self.writeFile()

    def readFile(self):
        self.origLines = []
        with open(self.fileName,'r') as f:
            self.origLineList =  f.readlines()

    def replaceLines(self):
        self.replLineList = []
        for lineOld in self.origLineList:
            lineNew = lineOld
            for k,v in self.replaceMap.iteritems():
                lineNew = lineNew.replace(k,v)
            self.replLineList.append(lineNew)

    def backupFile(self):
        if self.outFile is None or self.outFile == self.fileName:
            if self.backup: 
                backupFileName = '{0}.bak'.format(self.fileName)
                shutil.copy(self.fileName, backupFileName)

    def writeFile(self):
        if self.outFile is None:
            outFile = self.fileName
        else:
            outFile = self.outFile
        with open(outFile, 'w') as f:
            for line in self.replLineList:
                f.write(line)

    
# -----------------------------------------------------------------------------


def createReplaceMap():
    numSignal = 12
    signalList = ['SCK', 'MOSI', 'MISO', 'CS']
    modifierList = ['5V', '3V3']
    replaceMap = {}

    for i in range(numSignal):
        for signal in signalList:
            for modifier in modifierList:
                labelCur = '{0}_{1}_{2}'.format(signal,i,modifier)
                if signal == 'MISO':
                    if modifier == '5V':
                        labelNew = '_{0}_{1}'.format(signal,i)
                    else:
                        labelNew = '{0}_{1}'.format(signal,i)
                else:
                    labelNew = '{0}_{1}'.format(signal,i)
                replaceMap[labelCur] = labelNew
    return replaceMap
            


# -----------------------------------------------------------------------------
if __name__ == '__main__':

    fileName = 'arena.sch.old'
    outFile = 'arena.sch'


    replaceMap = createReplaceMap()

    labelReplacer = LabelReplacer(fileName,replaceMap,outFile=outFile)
    labelReplacer.run()


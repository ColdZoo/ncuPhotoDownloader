import os
import sys
import urllib
import urllib2

__author__ = 'adam'

snapshot = ''
flag_snap = False  # Control the skip of WordList

# prefix = 610040  # 61004 is the Code for Computer Science

firstTwo = 54
Third = 0
Fourth = 0
Fifth = 1
Sixth = 0

prefix = int(str(firstTwo)+str(Third)+str(Fourth)+str(Fifth)+str(Sixth))

cntNumber = 8001  # Grade 08!
loopCnt = 1000  # Max Student Number in one major is 1000
urlPrefix = 'http://218.64.56.18/uploadfile/studentphoto/before2011student/'


def getImageByLast3Digit(prefix, cntNumber, loopCnt):
    if not os.path.exists('data' + '/' + str(prefix)):
        os.makedirs('data' + '/' + str(prefix))  # Create Dir
    lastError = 0  # last error id
    ErrorCount = 0  # the count of continues error
    for i in range(1, loopCnt):
        sys.stdout.write(".........Processing " + str(prefix) + str(cntNumber) + " .............")
        ImageName = str(prefix) + str(cntNumber) + '.jpg'
        ImageFullName = 'data' + '/' + str(prefix) + '/' + ImageName
        if os.path.exists(ImageFullName):
            continue
        f = open(ImageFullName, 'wb')
        try:
            code = urllib.urlopen(urlPrefix + ImageName)
            if code.getcode() == 200:
                sys.stdout.write('[Success]')
                print '.'
                f.write(urllib2.urlopen(urlPrefix + ImageName, timeout=5).read())
                f.close()
            else:
                sys.stdout.write('[Failed]')
                print '.'
                os.remove(ImageFullName)
                if cntNumber == (lastError + 1):
                    ErrorCount += 1
                    print ErrorCount
                else:
                    ErrorCount = 0
                lastError = cntNumber
                if ErrorCount >= 3:  # Break the loop if continues error bigger than 5
                    if len(os.listdir('data' + '/' + str(prefix))) == 0:
                        os.removedirs('data' + '/' + str(prefix))  # remove empty dir
                    return
        except urllib2.HTTPError, e:
            if os.path.exists(ImageFullName):
                os.remove(ImageFullName)
            print 'HTTP Exception Caught' + str(e.code)
            pass
        except:
            if os.path.exists(ImageFullName):
                os.remove(ImageFullName)
            print 'Other Exception Caught'
            pass
        cntNumber += 1


def main():
    for ft in range(50, 59):
        print('Entering School' + str(ft))
    for fourth in range(0, 9):
        print('...Entering Department' + str(ft) + '0' + str(fourth))
        for fifth in range(0, 9):
            print('......Entering Major' + str(ft) + '0' + str(fourth) + str(fifth))
            prefix = int(str(ft)+str(Third)+str(fourth)+str(fifth)+str(Sixth))
            getImageByLast3Digit(prefix, cntNumber, loopCnt)


getImageByLast3Digit('52026', 10000, 1000)

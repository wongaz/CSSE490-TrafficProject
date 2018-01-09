
import os
def clean(path):
    splitPath = path.split('/')
    outputDir = './newData/' + splitPath[2]
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    outputFile = splitPath[-1].split('.')[0] + '.csv'
    output = open(outputDir + '/' + outputFile, 'w')
    with open(path) as f:
        flag = False
        dir = ''
        num = ''
        for line in f:
            result = ''
            if line.startswith('-'):
                flag = True
                commaSep = line.split(',')
                dir = commaSep[1].split(' ')[-1]
                num = commaSep[0].split(' ')[-1]
                continue
            if flag and 'AVERAGES' in line:
                flag = False
                continue
            if flag and ',' in line:
                split = line.split()
                result += split[0] + ' ' + split[1] + ' ' + split[2]
                for word in split[3:]:
                    result += '|' + word
                result += '|' + num
                result += '|' + dir + '\n'
                output.write(result)

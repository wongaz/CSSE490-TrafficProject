
import os
def clean(path):
    splitPath = path.split(os.sep)
    outputDir = './newData/' + splitPath[2]
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    outputFile = splitPath[-1].split('.')[0] + '.csv'
    output = open(outputDir + '/' + outputFile, 'w')
    headers = "DATE|DAY|1 am|2 am|3 am|4 am|5 am|6 am|7 am|8 am|9 am|10 am|11 am|Noon|1 pm|2 pm|3 pm|4 pm|5 pm|6 pm|7 pm|8 pm|9 pm|10 pm|11 pm|12 mid|TOTAL|Station number|Estimated|Direction\n"
    output.write(headers)
    with open(path) as f:
        flag = False
        dir = ''
        num = ''
        for line in f:
            result = ''
            estFlag = False
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
                if line.startswith("* "):
                    estFlag = True
                    line = line.replace("* ", "", 1)
                split = line.split()
                result += split[0] + ' ' + split[1] + ' ' + split[2]
                for word in split[3:]:
                    result += '|' + word
                result += '|' + num
                result += '|' + str(estFlag)
                result += '|' + dir + '\n'
                output.write(result)

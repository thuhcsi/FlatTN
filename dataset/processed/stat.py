
from os import write

#这里dict是跑数据集收集到的
dict = {'SELF': 0, 'PUNC': 0, 'ENG_LETTER': 0, 'VERBATIM': 0, 'DIGIT': 0, 'HYPHEN_RANGE': 0, 'CARDINAL': 0, 'HYPHEN_RATIO': 0, 'MEASURE_UNIT': 0, 'POINT': 0,
 'HYPHEN_IGNORE': 0, 'NUM_ENG': 0, 'SLASH_YEAR': 0, 'SLASH_MONTH': 0, 'DAY_CARDINAL': 0, 'ABBR': 0, 'COLON_HOUR': 0, 'MINUTE_CARDINAL': 0, 'SLASH_PER': 0,
 'NUM_TWO_LIANG': 0, 'SLASH_FRACTION': 0, 'SLASH_OR': 0, 'COLON_MINUTE': 0, 'SECOND_CARDINAL': 0, 'HYPHEN_SUBZERO': 0, 'HYPHEN_MINUS': 0, 'MONTH_CARDINAL': 0,}

def get_statistics(file, dic):
    for k in dic.keys():
        dic[k] = [0,0]

    k = 0
    a = open(file, 'r', encoding='utf-8')
    for l in a.readlines():
        if (l == '\n'):
            pass
        else:
            l = l.strip('\n')
            li= l.split(' ')
            if (li[1] != 'O'):
                li[1] = str(li[1]).split('-')[1]
            if (li[1] in dic.keys()):
                dic[li[1]][0] += 1
                k += 1

    k = k-dic['SELF'][0]
    k = k-dic['PUNC'][0]
    del dic['SELF']
    del dic['PUNC']

    return (k, dic)

file = r"./shuffled_BMES/test.char.bmes"
(total, dic) = get_statistics(file, dict)
print(total)

for v,key in zip(dic.values(), dic.keys()):
    v[1] = round(v[0]/total,6)
    v[1] = format(v[1], '.4%')
print(dic)
print(len(dic))

stat = r"statistics.csv"

fstat = open(stat,'a+')
for v,k in zip(dic.values(), dic.keys()):
    l = k+','+str(v[0])+','+str(v[1])+','+'\n'
    fstat.write(l) 

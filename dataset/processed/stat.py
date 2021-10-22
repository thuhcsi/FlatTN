
from os import write


a=open(r"C:\Edge\CN_TN_epoch-01\Shufffled_BMES\test.char.bmes",'r',encoding='ANSI')
#这里dic是跑数据集收集到的
dic={'SELF':0,'PUNC': 0, 'ENG_LETTER': 0, 'VERBATIM': 0, 'DIGIT': 0, 'HYPHEN_RANGE': 0, 'CARDINAL': 0, 'HYPHEN_RATIO': 0, 'MEASURE_UNIT': 0, 'POINT': 0.012, 'HYPHEN_IGNORE': 
0.003, 'NUM_ENG': 0.0, 'SLASH_YEAR': 0.0, 'SLASH_MONTH': 0.0, 'DAY_CARDINAL': 0.0, 'ABBR': 0.0, 'COLON_HOUR': 0.0, 'MINUTE_CARDINAL': 0.0, 'SLASH_PER': 0.0, 'NUM_TWO_LIANG': 0.0, 'SLASH_FRACTION': 0.0, 'SLASH_OR':0,'COLON_MINUTE': 0.0, 'SECOND_CARDINAL': 0.0, 'HYPHEN_SUBZERO': 0.0,'HYPHEN_MINUS':0,'MONTH_CARDINAL':0,}


for k in dic.keys():
    dic[k]=[0,0]

k=0
n=0
for l in a.readlines():
    
    if(l=='\n'):
        pass
        n+=1

    else:
        
        l=l.strip('\n')
        li=l.split(' ')
        if(li[1]!='O'):
            st=str(li[1])
            st=st.split('-')
            li[1]=st[1]
        if(li[1] in dic.keys()):
            dic[li[1]][0]=dic[li[1]][0]+1
            k+=1
        
k=k-dic['SELF'][0]
k=k-dic['PUNC'][0]
del dic['SELF']
del dic['PUNC']
print(k)
my_tuple = zip(dic.values(), dic.keys())
for v,key in my_tuple:
    v[1]=v[0]/k
    v[1]=round(v[1],6)
    v[1] = format(v[1], '.4%')
    dic[key][1]=v[1]
#b1=open(r"C:\Edge\CN_TN_epoch-01\dataset\tj.csv",'w+')
"""
for v,key in my_tuple:
    l=key+','+v[0]+','+v[1]+'\n'
    print(l)
    b1.write(l)
print(my_tuple)
#print(sorted(my_tuple,reverse=True))
"""
print(dic)
print(len(dic))

b=r"C:\Edge\CN_TN_epoch-01\Shufffled_BMES\train.csv"

b1=open(b,'a+')
for v,k in zip(dic.values(), dic.keys()):
    l=k+','+str(v[0])+','+str(v[1])+','+'\n'
    b1.write(l) 






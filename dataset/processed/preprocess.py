import pandas as pd
import codecs
import json

path_name=r"./CN_TN_epoch-01-28645_2.jsonl"

#out_name=r"C:\Edge\CN_TN_epoch-01\tn.jsonl"
#tn_BMES=r"C:\Edge\CN_TN_epoch-01\tn_BMES.txt"
#tns=open(tn_BMES,'w')
#out_f=open(out_name,'w')

p1=r"./shuffled_BMES"
t1=p1+'/train.char.bmes'
t2=p1+'/dev.char.bmes'
t3=p1+'/test.char.bmes'

tt1 = codecs.open(t1, 'w', 'utf-8')
tt2 = codecs.open(t2, 'w', 'utf-8')
tt3 = codecs.open(t3, 'w', 'utf-8')

import random

#bb1=open(r"C:\Edge\CN_TN_epoch-01\tn_rule_data.txt",'w')
#bb2=open(r"C:\Edge\CN_TN_epoch-01\CN_TN_epoch-01\CN_TN_epoch-02-1355_3.jsonl",'w')

dd=[]
with open(path_name, 'r') as load_f:
    for l in load_f.readlines():
        dic=json.loads(l)
        #l.encode('utf-8').decode('unicode_escape')
        j=json.dumps(dic, ensure_ascii=False)
        d=json.loads(j)

        text = d["text"]
        # print('CEHCK text from d:', d["text"])
        le = len(text)
        # print('CEHCK text length from d:', le)
        labels = d["labels"]
        # print('CEHCK labels length from d:', d["labels"])
        d["id"] = d["id"]
        # print('CEHCK id length from d:', d["id"])
        #json.dump(d,bb2)
        #bb2.write('\n')
        dd.append(d)

# for se in dd:
#     text=se["text"]
#     le=len(text)
#     labels=se["labels"]
#     for label in labels:
#             word=text[label[0]:label[1]]
#             st=word+' '+"S-"+label[2]+'\n'
#             tt1.write(st)
#             if(label[1]==le):
                
#                 tt1.write('\n')     


# setting the shuffle to get the same train/test/dev segmentation
random.Random(30).shuffle(dd)


id=0
for se in dd:
    text=se["text"]
    le=len(text)
    labels=se["labels"]
    id+=1
   
#得到BMES的标签
    if(id>=0 and id<24000):
        for label in labels:
            word=text[label[0]:label[1]]
            if(len(word)==1):
                st=word+' '+"S-"+label[2]+'\n'
                tt1.write(st)
                if(label[1]==le):
                    tt1.write('\n')
            else:
                index=0
                for char in word:
                    if(index==0):
                        st=char+' '+"B-"+label[2]+'\n'
                    if(index>0 and index<(len(word)-1)):
                        st=char+' '+"M-"+label[2]+'\n'
                    if(index==(len(word)-1)):
                        st=char+' '+"E-"+label[2]+'\n'
                    tt1.write(st)
                    index+=1
    
    if(id>=24000 and id<27000):
        for label in labels:
            word=text[label[0]:label[1]]
            if(len(word)==1):
                st=word+' '+"S-"+label[2]+'\n'
                tt2.write(st)
                if(label[1]==le):
                    tt2.write('\n')
            else:
                index=0
                for char in word:
                    if(index==0):
                        st=char+' '+"B-"+label[2]+'\n'
                    if(index>0 and index<(len(word)-1)):
                        st=char+' '+"M-"+label[2]+'\n'
                    if(index==(len(word)-1)):
                        st=char+' '+"E-"+label[2]+'\n'
                    tt2.write(st)
                    index+=1

    if(id>=27000 and id<30000):
        # print('CHECK test set HERE!!!')
        for label in labels:
            word=text[label[0]:label[1]]
            if(len(word)==1):
                st=word+' '+"S-"+label[2]+'\n'
                tt3.write(st)
                if(label[1]==le):
                    tt3.write('\n')
            else:
                index=0
                for char in word:
                    if(index==0):
                        st=char+' '+"B-"+label[2]+'\n'
                    if(index>0 and index<(len(word)-1)):
                        st=char+' '+"M-"+label[2]+'\n'
                    if(index==(len(word)-1)):
                        st=char+' '+"E-"+label[2]+'\n'
                    tt3.write(st)
                    index+=1

print(id)
        
        


              

                
            

        
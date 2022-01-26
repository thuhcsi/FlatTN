import pandas as pd
import codecs
import json


def process_word(word, label):
    st = ''
    if (len(word)==1):
        st = st + word + ' ' + "S-"+label[2] + '\n'
    else:
        index = 0
        for char in word:
            if (index==0):
                st = st + char + ' ' + "B-"+label[2]+ '\n'
            elif (index<(len(word)-1)):
                st = st + char + ' ' + "M-"+label[2] + '\n'
            elif (index==(len(word)-1)):
                st = st + char + ' ' + "E-"+label[2] + '\n'
            index+=1
    return st


raw_json = r"./CN_TN_epoch-01-28645_2.jsonl"

out_path = r"./shuffled_BMES"
train = out_path + '/train.char.bmes'
dev   = out_path + '/dev.char.bmes'
test  = out_path + '/test.char.bmes'

ftrain = codecs.open(train, 'w', 'utf-8')
fdev   = codecs.open(dev,   'w', 'utf-8')
ftest  = codecs.open(test,  'w', 'utf-8')

import random

# load data
print("Loading data...")
dd=[]
with open(raw_json, 'r') as load_f:
    for l in load_f.readlines():
        dic = json.loads(l)
        j = json.dumps(dic, ensure_ascii=False)
        d = json.loads(j)

        text = d["text"]
        # print('CEHCK text from d:', d["text"])
        le = len(text)
        # print('CEHCK text length from d:', le)
        labels = d["labels"]
        # print('CEHCK labels length from d:', d["labels"])
        d["id"] = d["id"]
        # print('CEHCK id length from d:', d["id"])
        dd.append(d)

# set the random seed for shuffle to get the same train/dev/test segmentation
random.Random(30).shuffle(dd)

num_items = len(dd)
train_end = int(num_items * 0.8)
dev_end   = int(num_items * 0.9)
print(num_items, train_end, dev_end)

# write processed data 
id=0
for se in dd:
    text   = se["text"]
    le     = len(text)
    labels = se["labels"]
    id += 1

    # get BMES labels
    for label in labels:
        word = text[label[0]:label[1]]
        st = process_word(word, label)

        # write to different file
        if (id <= train_end):
            ftrain.write(st)
            if (label[1] == le):
                ftrain.write('\n')
        elif (id <= dev_end):
            fdev.write(st)
            if (label[1] == le):
                fdev.write('\n')
        else:
            ftest.write(st)
            if (label[1] == le):
                ftest.write('\n')

print(id)

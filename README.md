[English](#Requirement)
[中文](#运行环境)

# FlatTN
This repository contains code accompanying the paper "AN END-TO-END CHINESE TEXT NORMALIZATION MODEL BASED ON RULE-GUIDED FLAT-LATTICE TRANSFORMER" which is submitted to ICASSP 2022.

# Requirement

```
Python: 3.7.3
PyTorch: 1.2.0
FastNLP: 0.5.0
Numpy: 1.16.4
```
you can go [here](https://fastnlp.readthedocs.io/zh/latest/) to know more about FastNLP.

# Dataset download
Chinese Text Normalization Dataset can be available at https://www.data-baker.com/en/#/data/index/TNtts.

To browse the Chinese version of the download page, please click https://www.data-baker.com/data/index/TNtts.

# Data preprocessing

The raw dataset in jsonl format are saved at:
`dataset/processed/CN_TN_epoch-01-28645_2.jsonl`

The raw dataset are in jsonl format as follows:
![image](https://user-images.githubusercontent.com/38463365/148810299-0dc3acb9-545a-480f-b795-65e034fae29d.png)

Preprocessed data are saved at:
`dataset/processed/shuffled_BMES`

The proposed data are in BMES format as follows:

  ![image](https://user-images.githubusercontent.com/38463365/148811758-49f739b5-7e46-4870-b50c-5cdf7e5d0e3d.png)

We divided data into `train` 、`dev` 、`test` by 8:1:1.

You can also run our code to prepocess and divide the raw dataset again
```
cd dataset/processed
python preprocess.py
```

You can run the following code to see the number of all NSW categories 
```
cd dataset/processed
python stat.py
```

# Training
Our code are in version V1, run training code
```
cd V1
python flat_main.py --dataset databaker
```
Our proposed rule base are saved in a python file:
`V1/add_rule.py`

## Flat-Lattice-Transformer参考链接

https://github.com/LeeSureman/Flat-Lattice-Transformer

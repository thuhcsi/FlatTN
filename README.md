# FlatTN
This repository contains code accompanying the paper **"An End-to-End Chinese Text Normalization Model based on Rule-Guided Flat-Lattice Transformer"** published on ICASSP 2022.

##  [Paper](https://arxiv.org/abs/2203.16954)

# Requirement

```
Python: 3.7.3
PyTorch: 1.2.0
FastNLP: 0.5.0
Numpy: 1.16.4
fitlog
```
For more about FastNLP, please visit [here](https://fastnlp.readthedocs.io/zh/latest/). 
For Fitlog, please refer to [this](https://fitlog.readthedocs.io/zh/latest/).

# Dataset download

We release a large-scale **Chinese Text Normalization (TN) Dataset** in corporatioin with Databaker (Beijing) Technology Co., Ltd.

To download the dataset, please visit https://www.data-baker.com/en/#/data/index/TNtts.

(For Chinese version of the download page, please visit https://www.data-baker.com/data/index/TNtts.)

# Data preprocessing

The raw dataset in jsonl format are saved at:
`dataset/processed/CN_TN_epoch-01-28645_2.jsonl`

We preprocessed the data into the BMES format, and divided the data into `train` 、`dev` 、`test` by 8:1:1.
```
dataset/processed/shuffled_BMES
                      ├── train.char.bmes
                      ├── dev.char.bmes
                      └── test.char.bmes
```

An example of the processed data in BMES format is as follows:
```
2 B-DIGIT
0 M-DIGIT
1 M-DIGIT
5 E-DIGIT
年 S-SELF
， S-PUNC
只 S-SELF
剩 S-SELF
3 B-CARDINAL
9 E-CARDINAL
天 S-SELF
。 S-PUNC
```

You can re-run our code to preprocess and divide the raw dataset again:
```
cd dataset/processed
python preprocess.py
```

You can also used the following code to get statistics of all NSW categories of the data:
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

# Acknowledgement

Our code is based on [Flat-Lattice-Transformer (FLAT)](https://github.com/LeeSureman/Flat-Lattice-Transformer) from LeeSureman.

For more information about FLAT, please refer to [LeeSureman/Flat-Lattice-Transformer](https://github.com/LeeSureman/Flat-Lattice-Transformer).

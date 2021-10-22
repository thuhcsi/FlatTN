#日期
DATE=r"^ \d{4}-\d{1,2}-\d{1,2} $| \d{4}/\d{1,2}/\d{1,2} | \d{4}.\d{1,2}.\d{1,2} |\d{4}-\d{1,2} |\d{1,2}-\d{1,2}| \d{4}/\d{1,2} | \d{1,2}/\d{1,2}| \d{4}.\d{1,2} |\d{1,2}.\d{1,2} | \d{4}年 | \d{1,2}月 | \d{1,2}日 $" 
#时间
TIME=r" \d{1,2}点| \d{1,2}分 | \d{12}秒 |^ \d{1,2}:\d{1,2}$ | \d{1,2}:\d{1,2}:\d{1,2} "
#分数
FRANCTION=r"^\d{0,} / \d{0,}$"
#比值
RATIO=r"^ \d{0,}:\d{0,} | \d{0,}:\d{0,}:\d{0,} $"
#标点
PUNC=r"^ \· |\~|\！|\@|\#|\￥|\%|\&|\*|\（|\）|\-|\+|\=|\【|\】|\{|\}|\、|\；|\‘|\’|\：|\“|\”|\《|\》|\？|\，|\。|\、|\`|\~|\!|\#|\$|\%|\^|\&|\*|\(|\)|\_|\[|\]|\{|\}|\;|\'|\'|\:|\"|\"|\,|\.|\/|\<|\>|\? $"
#金钱
MONEY=r"^ \d{0,}.\d{0,}(Yuan| RMB| ￥| CNY| $| USD|€ |J.￥ |JPY | HK＄ |HKD) $ |  ^ (Yuan| RMB| ￥| CNY| $| USD|€ |J.￥ |JPY | HK＄ |HKD)\d{0,}.\d{0,} $"
#英文单词
ENGLISH=r" ^[A-Za-z][a-z]+ $"
#中文汉字
CHINESE=r"^[\u4e00-\u9fa5]$"
#基数词
CAEDINAL=r" ^[0-9]* | -[0-9]* $"
#十进制小数
DECIMAL=r"^ \d+ \.\d+ $ | ^ - \d+ \.\d+ $"
#网址
ELECTRONIC=r"^[a-zA-z]+://[^\s]* $ | ^http:// ([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)? $"
#电话号码
TELEPHONE=r"((\d{11})|^((\d{7,8})|(\d{4}|\d{3})-(\d{7,8})|(\d{4}|\d{3})-(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1})|(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1}))$)"
#英文缩写
VERBATIM=r"^[A-Z]+$"

#类型字典
target_dict={DATE:"DATE",TIME:"TIME",FRANCTION:"FRANCTION",RATIO:"RATIO",PUNC:"PUNC",MONEY:"MONEY",ENGLISH:"ENGLISH",\
    CHINESE:"CHINESE",CAEDINAL:"CAEDINAL",DECIMAL:"DECIMAL",ELECTRONIC:"ELECTRONIC",TELEPHONE:"TELEPHONE",VERBATIM:"VERBATIM"}
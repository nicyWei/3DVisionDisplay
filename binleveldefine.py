from enum import Enum,unique;

#@unique(BinInfoLevel)
class BinInfoLevel(Enum):
    #[0,2,5,8,10]
    moreCritcal = 10;
    critcal = 10;
    high = 8;
    abnormal = 5;
    attention = 2;
    more = 5;
    accept = 0;
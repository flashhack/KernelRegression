import datetime as dt;
from matplotlib.dates import date2num
import matplotlib;
import csv;

def ReadData(filename):
    f=open('C:/MiniFund/Programs/StrategyNotifier/StrategyNotifer/bin/Debug/Pattern/'+filename,'r');
    #f=open('C:/MiniFund/Programs/StrategyNotifier/StrategyNotifer/bin/Debug/'+filename,'r');
    #f=open(filename,'r');
    x=[];
    for line in f:
        x.append(float(line));
    f.close();
    return x;

def ReadPair(filename):
    f=open('D:/MiniFund/Programs/StrategyNotifier/StrategyNotifer/bin/Debug/Regime/'+filename,'r');
    #f=open('C:/MiniFund/Programs/StrategyNotifier/StrategyNotifer/bin/Debug/Pattern/'+filename,'r');
    #f=open('C:/MiniFund/Programs/StrategyNotifier/StrategyNotifer/bin/Debug/'+filename,'r');
    #f=open(filename,'r');
    x=[];
    reader = csv.reader(f);
    cnt=0;
    for row in reader:
        cnt+=1;
        if cnt!=1:
            x.append((float(row[0]),float(row[1])));
    return x;

def ReadPrice(filename):
    f=open('D:/MiniFund/Programs/StrategyNotifier/StrategyNotifer/bin/Debug/Regime/'+filename,'r');
    #f=open('C:/MiniFund/Programs/StrategyNotifier/StrategyNotifer/bin/Debug/Pattern/'+filename,'r');
    #f=open('C:/MiniFund/Programs/StrategyNotifier/StrategyNotifer/bin/Debug/'+filename,'r');
    #f=open(filename,'r');
    x=[];
    reader = csv.reader(f);
    cnt=0.0;
    for row in reader:
        tmp3=[];
        #tmp2=date2num(dt.datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S"));
        #tmp3.append(tmp2)
        tmp3.append(float(cnt));
        for i in range(1,5):
            tmp3.append(float(row[i]));
        x.append(tmp3);
        cnt+=1;
    return x;

def ReadDataPrice(filename):
    f=open('D:/MiniFund/Programs/StrategyNotifier/StrategyNotifer/bin/Debug/Regime/'+filename,'r');
    #f=open('C:/MiniFund/Programs/StrategyNotifier/StrategyNotifer/bin/Debug/Pattern/'+filename,'r');
    #f=open('C:/MiniFund/Programs/StrategyNotifier/StrategyNotifer/bin/Debug/'+filename,'r');
    #f=open(filename,'r');
    x=[];
    reader = csv.reader(f);
    for row in reader:
        tmp3=[];
        #tmp2=date2num(dt.datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S"));
        #tmp3.append(tmp2)
        for i in range(0,5):
            tmp3.append(float(row[i]));
        x.append(tmp3);
    return x;

def ReadTime(filename):
    f=open('D:/MiniFund/Programs/StrategyNotifier/StrategyNotifer/bin/Debug/Regime/'+filename,'r');
    #f=open('C:/MiniFund/Programs/StrategyNotifier/StrategyNotifer/bin/Debug/Pattern/'+filename,'r');
    reader = csv.reader(f);
    for row in reader:
        return row[0];

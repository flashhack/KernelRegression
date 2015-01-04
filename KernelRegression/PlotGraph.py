import numpy as np
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc


#mark local min/max on graph
def MarkGraph(LocalMaxs, LocalMins, ax):
    for tup in LocalMaxs:
        ax.annotate('local max',xy=(tup[0],tup[1]),xytext=(tup[0]+0.5,tup[1]+0.5),arrowprops=dict(facecolor='black', shrink=0.05));
    for tup in LocalMins:
        ax.annotate('local min',xy=(tup[0],tup[1]),xytext=(tup[0]-0.5,tup[1]-0.5),arrowprops=dict(facecolor='black', shrink=0.05));
    return ax;

def MarkHS(HS,ax):
    for tup in HS:
        ax.annotate('HS',xy=(tup[0],tup[1]),xytext=(tup[0]-0.5,tup[1]-0.5),arrowprops=dict(facecolor='black', shrink=0.05));
    return ax;


def PlotGraph(x,y,y_org,m,mPrime,LocalMaxs,LocalMins):
    ax1=plt.subplot();
    ax2=ax1.twinx();

    ax1.scatter(x,y);
    ax1.plot(x,m,linewidth=3);
    ax2.plot(x,mPrime,color='r',linewidth=3);
    ax1.plot(x,y_org,linewidth=3);

    MarkGraph(LocalMaxs,LocalMins,ax1);

    plt.axhline(0);
    plt.axvline(0);
    plt.grid(True);
    plt.show();

def PlotGraph_NoOrg(ax1, x,y,m,mPrime,LocalMaxs,LocalMins):
    #ax2=ax1.twinx();

    ax1.scatter(x,y);
    ax1.plot(x,m,linewidth=3);
    #ax2.plot(x,mPrime,color='r',linewidth=3);

    MarkGraph(LocalMaxs,LocalMins,ax1);


def PlotGraph_Candle(ax, quotes):
    candlestick_ohlc(ax,quotes,width=0.6,colorup='g',colordown='r');




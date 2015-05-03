import PlotGraph as plotgraph;
import ReadFile as readfile;
import matplotlib.pyplot as plt


def OnePlot(num):
    x = readfile.ReadData('DataX{0}.txt'.format(num));
    y = readfile.ReadData('DataY{0}.txt'.format(num));
    m=readfile.ReadData('Estimates{0}.txt'.format(num));
    Pattern = readfile.ReadPair('Pattern{0}.txt'.format(num));
    quotes = readfile.ReadDataPrice('DataPrice{0}.txt'.format(num));
    title_time = readfile.ReadTime('Pattern{0}.txt'.format(num));
    
    plt.figure(figsize=(8,4));
    ax=plt.subplot();

    plotgraph.PlotGraph_Pattern(ax,x,y,m,Pattern);
    plotgraph.PlotGraph_Candle(ax,quotes);

    plt.grid(True);
    plt.title(title_time);
    plt.xlim([-1,151]);
    
    plt.savefig('Figures/Figure{0}.png'.format(num),dpi=300);
    plt.close();
    return;

def RegimePlot(num):
    TrendUp = readfile.ReadPair('TrendUp.txt');
    TrendDown = readfile.ReadPair('TrendDown.txt');
    Range = readfile.ReadPair('Range.txt');
    quotes = readfile.ReadDataPrice('DataPrice.txt');
    title_time = readfile.ReadTime('TrendUp.txt');
    
    plt.figure(figsize=(8,4));
    ax=plt.subplot();

    
    plotgraph.PlotGraph_Candle(ax,quotes);
    plotgraph.MarkGraph(TrendUp,TrendDown,ax);
    #plotgraph.MarkPattern(Range,'R',ax);

    plt.grid(True);
    plt.title(title_time);
    
    #plt.savefig('Figures/Figure{0}.png'.format(num),dpi=300);
    #plt.close();
    plt.show();
    return;

"""
x = readfile.ReadData('DataX.txt');
y = readfile.ReadData('DataY.txt');
y_org = readfile.ReadData('DataOrg.txt');
m=readfile.ReadData('Estimates.txt');
mPrime=readfile.ReadData('EstimatesPrime.txt');

LocalMaxs = readfile.ReadPair('LocalMaxs.txt');
LocalMins = readfile.ReadPair('LocalMins.txt');
Pattern = readfile.ReadPair('Pattern.txt');

quotes = readfile.ReadDataPrice('DataPrice.txt');

#plotgraph.PlotGraph(x,y,y_org,m,mPrime,LocalMaxs,LocalMins);
ax=plt.subplot();

#plotgraph.PlotGraph_NoOrg(ax,x,y,m,mPrime,LocalMaxs,LocalMins);
plotgraph.PlotGraph_Pattern(ax,x,y,m,Pattern);
plotgraph.PlotGraph_Candle(ax,quotes);

#plt.axhline(0);
#plt.axvline(0);
plt.grid(True);
#plt.show();
plt.savefig('Figure.png',dpi=300);
plt.close();
"""


#OnePlot(1);
#OnePlot(2);

#for i in range(1,91):
#    OnePlot(i);

RegimePlot(1);
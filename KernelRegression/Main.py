import PlotGraph as plotgraph;
import ReadFile as readfile;
import matplotlib.pyplot as plt

x = readfile.ReadData('DataX.txt');
y = readfile.ReadData('DataY.txt');
y_org = readfile.ReadData('DataOrg.txt');
m=readfile.ReadData('Estimates.txt');
mPrime=readfile.ReadData('EstimatesPrime.txt');

LocalMaxs = readfile.ReadPair('LocalMaxs.txt');
LocalMins = readfile.ReadPair('LocalMins.txt');

#quotes = readfile.ReadPrice('USDJPY.csv');
quotes = readfile.ReadDataPrice('DataPrice.txt');

#plotgraph.PlotGraph(x,y,y_org,m,mPrime,LocalMaxs,LocalMins);
ax=plt.subplot();

plotgraph.PlotGraph_NoOrg(ax,x,y,m,mPrime,LocalMaxs,LocalMins);
plotgraph.PlotGraph_Candle(ax,quotes);

#plt.axhline(0);
#plt.axvline(0);
plt.grid(True);
plt.show();

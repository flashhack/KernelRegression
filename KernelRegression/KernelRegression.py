import numpy as np
import matplotlib.pyplot as plt

# Kh function
def Kernel(x,h):
    tmp=1/h/np.sqrt(2*np.pi);
    tmp*=np.exp(-x*x/2/h/h);
    return tmp;

# K'h function
def KernelPrime(x,h):
    tmp=Kernel(x,h);
    tmp*= -x/h/h;
    return tmp;


# calc m_hat
def CalcEstimates(x,y):
    m=[];
    for i in range(len(x)):
        num=0; #numerator
        den=0; #denominator
        #for j in range(max(0,i-WindowLength),i+1):
        #for j in range(max(0,i-WindowLength),min(i+WindowLength,len(x))):
        for j in range(0,len(x)):
            tmpx=x[i]-x[j];
            tmpK=1.0/Bandwidth/np.sqrt(2*np.pi)*np.exp(-tmpx**2 *0.5 * Bandwidth**-2);
            #num+=Kernal(x[i]-x[j],Bandwidth)*y[j];
            #den+=Kernal(x[i]-x[j],Bandwidth);
            num+=tmpK * y[j];
            den+=tmpK;
        if den!=0:
            m.append(num/den);
        else:
            m.append(0);
    return m;

# calc m_hat'
def CalcEstimatesPrime(x,y):
    mPrime=[];
    for i in range(len(x)):
        sum1=0; # K'*P
        sum2=0; # K
        sum3=0; # K * P
        sum4=0; # K'
        tmp=0;
        #for j in range(max(0,i-WindowLength),i+1):
        #for j in range(max(0,i-WindowLength),min(i+WindowLength,len(x))):
        for j in range(0,len(x)):
            tmpx=x[j]-x[i];
            tmpK=1.0/Bandwidth/np.sqrt(2*np.pi)*np.exp(-tmpx**2 *0.5 * Bandwidth**-2);
            tmpKP=tmpK*(-tmpx)*Bandwidth**-2;
            #sum1 += KernalPrime(x[j]-x[i],Bandwidth) * y[j];
            #sum2 += Kernal(x[j]-x[i],Bandwidth);
            #sum3 += Kernal(x[j]-x[i],Bandwidth) * y[j];
            #sum4 += KernalPrime(x[j]-x[i],Bandwidth);
            sum1 += tmpKP * y[j];
            sum2 += tmpK;
            sum3 += tmpK * y[j];
            sum4 += tmpKP;
        tmp=sum1*sum2-sum3*sum4;
        mPrime.append(tmp);

    #mPrime = (mPrime-min(mPrime))/(max(mPrime)-min(mPrime));
    return mPrime;


#calc CV function for a given BandWidth
def CrossValidation(x,y,BW):
    m=0;
    for i in range(len(x)):
        num=0;
        den=0;
        for j in range(max(0,i-WindowLength),i+1):
            num+=Kernel(x[i]-x[j],BW)*y[j];
            den+=Kernel(x[i]-x[j],BW);
        if den!=0:
            m+=np.square(y[i]-num/den);
    return m/WindowLength;

def FindLocalMax(x,y,mp):
    res=[];
    for i in range(len(mp)-1):
        if mp[i]<0 and mp[i+1]>0:
            maxx=-100; maxy=-100;
            for j in range(-5,5):
                if (i+j) >=0 and (i+j)<len(mp) and y[i+j]>maxy:
                    maxx=x[i+j];
                    maxy=y[i+j];
            res.append((maxx,maxy));
    return res;

def FindLocalMin(x,y,mp):
    res=[];
    for i in range(len(mp)-1):
        if mp[i]>0 and mp[i+1]<0:
            minx=100; miny=100;
            for j in range(-5,5):
                if (i+j) >=0 and (i+j)<len(mp) and y[i+j]<miny:
                    minx=x[i+j];
                    miny=y[i+j];
            res.append((minx,miny));
    return res;

#mark local min/max on graph
def MarkGraph(LocalMaxs, LocalMins, ax):
    for tup in LocalMaxs:
        ax.annotate('local max',xy=(tup[0],tup[1]),xytext=(tup[0]+0.5,tup[1]+0.5),arrowprops=dict(facecolor='black', shrink=0.05));
    for tup in LocalMins:
        ax.annotate('local min',xy=(tup[0],tup[1]),xytext=(tup[0]-0.5,tup[1]-0.5),arrowprops=dict(facecolor='black', shrink=0.05));
    return ax;


total = 1024;
Bandwidth = 0.5;
WindowLength=1000;
x = np.linspace(-2*np.pi, 2*np.pi,total,True);      #X series -2pi~2pi
K = Kernel(x,Bandwidth);
K_prime = KernelPrime(x,Bandwidth);
Z = 0.5*np.random.normal(0,1,total);                #noise
y = np.sin(x)+Z;                                    #Y(price) data
y_org = np.sin(x);
m = CalcEstimates(x,y);
#print(CrossValidation(x,y,0.125));
#print(CrossValidation(x,y,0.5));
mPrime = CalcEstimatesPrime(x,y);

LocalMaxs=FindLocalMax(x,y,mPrime);
LocalMins=FindLocalMin(x,y,mPrime);

#plt.plot(x,K);
#plt.plot(x,K_prime);
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


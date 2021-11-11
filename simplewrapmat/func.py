import numpy as np
import matplotlib.pyplot as plt
def plot_X(fig,Xs,Ys,color,plotdot=False,lwmain=2,
            xmin=0.e0,xmax=1.e0,ymin=0.e0,ymax=0.e0,
            set_xlog=True,set_ylog=True,xlabel='xaxis',ylabel='yaxis',labelbottom=True,linetype='-',xticks=np.array([]),yticks=np.array([])):
    fig.plot(Xs,Ys,linetype,c=color,lw=lwmain)
    if plotdot:
        for num in range(len(Xs)):
            fig.plot(Xs[num],Ys[num],'o',markersize=2,c=color,markerfacecolor=color)
    fig.set_xlim(xmin,xmax)
    fig.set_ylim(ymin,ymax)
    if set_xlog: fig.set_xscale("log")
    if set_ylog: fig.set_yscale("log")
    if not labelbottom: fig.tick_params(labelbottom=False)
    if not labelbottom:
        fig.set_xlabel("")       
    else:
        fig.set_xlabel(xlabel)
    fig.set_ylabel(ylabel)
    if len(xticks)>=2.0:
        fig.set_xticks(xticks)
    if len(yticks)>=2.0:
        fig.set_yticks(yticks)
    return fig


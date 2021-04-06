from matplotlib.ticker import MultipleLocator,FuncFormatter
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import matplotlib.ticker as ticker
import os;
import re;
import gc;
from fileParser.parseJson import parseJson;
from node.nodeImpl import NodeImpl;
from decimal import *;
from util.productColorDefine import Colors;
import sys;
#matplotlib.use('Agg')
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

def showConnectionDomain(axisList,xtick,ytick,dxmim,dxmax,dymin,dymax,dzmin,dzmax,zstep,width,Length,High):
    
    allPoints=[];

    #print(axisList);
    #########
    allPoints = axisList[True];
    radiusList = axisList["r"];
    deviceList = axisList["deviceList"];
    deviceSize = len(deviceList);
    #########
    tmp = [];
    m2=[];
    m3=[];
    pointfeature = {};
    waferAttribute = {};
    for point in allPoints:
        #print(point);
        tmp = point;
        tmpX = float(tmp['x']);

        tmpZ = float(tmp['z']);

        tmpY = float(tmp['y']);
        sx = tmp['dieSizeX'];
        sy = tmp['dieSizeY'];
        ####
        waferAttribute = tmp['waferAttributes'];
        currentDevice = waferAttribute['device'];
        ####
        m2.append(tmpX);
        m2.append(tmpY);
        m2.append(tmpZ);

        ######
        corIndex = 0;
        colorValue = 'g';
        for device in deviceList:
            corIndex = corIndex + 1;
            if currentDevice.strip() == device.strip():
            
               colorValue = Colors["product"+str(corIndex)].value;
        
        ######
        newNode = NodeImpl();
        newNode.updateCoordinateAllParam(tmpX, tmpY, tmpZ, sx, sy,colorValue);
        pointfeature[[tmpX,tmpY,tmpZ].__str__().strip()] = newNode;
    m3=np.reshape(m2,(-1,3));
       
    #print(m3);
    m4=np.array(m3);




    x=[k[0] for k in m4]
    y=[k[1] for k in m4]
    z=[k[2] for k in m4]

   
    

    plt.ion();
    plt.switch_backend('Agg');
    fig=plt.figure(dpi=120, figsize=(12,8));

    ax = fig.gca(projection='3d')

    ax.set_xlabel('X');
    ax.set_ylabel('Y');
    ax.set_zlabel('layer');
    
    x_major_locator=MultipleLocator(xtick);
    y_major_locator=MultipleLocator(ytick);
    z_major_locator=MultipleLocator(zstep);
    ax.xaxis.set_major_locator(x_major_locator);
    ax.yaxis.set_major_locator(y_major_locator);
    ax.zaxis.set_major_locator(z_major_locator);
    plt.xlim(dxmim,dxmax);
    plt.ylim(dymin,dymax);
    ax.set_zlim3d(dzmin, dzmax);

    plt.rcParams['axes.unicode_minus']=False;
    ##########
    for i in radiusList:

        a,b = (0.0,0.0);
        theta = np.arange(0, 2*np.pi, 0.01);
        x = a + i*np.cos(theta);
        y = b + i*np.sin(theta);
        ax.plot(x,y,color='b');
        #####
    for k in m4:
        #print(k);
        if width ==0 and Length == 0 and High == 0:
            key = [];
            key.append(k[0]);
            key.append(k[1]);
            key.append(k[2]);
            #print(key);
            node = pointfeature[key.__str__().strip()];
            nwidth = node.stepSizeX;
            nLength = node.stepSizeY;
            nHigh = 1;
            nColor = node.color;
            
            xx = np.linspace(k[0], k[0]+nwidth, 2)
            yy = np.linspace(k[1], k[1]+nLength, 2)
            zz = np.linspace(k[2], k[2]+nHigh, 2)
    
            xx2, yy2 = np.meshgrid(xx, yy)
    
            ax.plot_surface(xx2, yy2, np.full_like(xx2, k[2]),color=nColor,linewidth=0.2,edgecolors = 'k' )
            ax.plot_surface(xx2, yy2, np.full_like(xx2, k[2]+nHigh),color=nColor,linewidth=0.2,edgecolors = 'k')
       
    
            yy2, zz2 = np.meshgrid(yy, zz)
            ax.plot_surface(np.full_like(yy2, k[0]), yy2, zz2,color=nColor,linewidth=0.2,edgecolors = 'k')
            ax.plot_surface(np.full_like(yy2, k[0]+nwidth), yy2, zz2,color=nColor,linewidth=0.2,edgecolors = 'k')
    
            xx2, zz2= np.meshgrid(xx, zz)
            ax.plot_surface(xx2, np.full_like(yy2, k[1]), zz2,color=nColor,linewidth=0.2,edgecolors = 'k')
            ax.plot_surface(xx2, np.full_like(yy2, k[1]+nLength), zz2,color=nColor,linewidth=0.2,edgecolors = 'k')
        else:

            
            xx = np.linspace(k[0], k[0]+width, 2)
            yy = np.linspace(k[1], k[1]+Length, 2)
            zz = np.linspace(k[2], k[2]+High, 2)
    
            xx2, yy2 = np.meshgrid(xx, yy)
    
            ax.plot_surface(xx2, yy2, np.full_like(xx2, k[2]),color=nColor,linewidth=0.2,edgecolors = 'k' )
            ax.plot_surface(xx2, yy2, np.full_like(xx2, k[2]+High),color=nColor,linewidth=0.2,edgecolors = 'k')
       
    
            yy2, zz2 = np.meshgrid(yy, zz)
            ax.plot_surface(np.full_like(yy2, k[0]), yy2, zz2,color=nColor,linewidth=0.2,edgecolors = 'k')
            ax.plot_surface(np.full_like(yy2, k[0]+width), yy2, zz2,color=nColor,linewidth=0.2,edgecolors = 'k')
    
            xx2, zz2= np.meshgrid(xx, zz)
            ax.plot_surface(xx2, np.full_like(yy2, k[1]), zz2,color=nColor,linewidth=0.2,edgecolors = 'k')
            ax.plot_surface(xx2, np.full_like(yy2, k[1]+Length), zz2,color=nColor,linewidth=0.2,edgecolors = 'k')
    ####  
    #plt.show();
    gc.collect(); 
    return plt;


import matplotlib.pyplot as plt
import numpy as np;
from matplotlib.pyplot import MultipleLocator;
import matplotlib.patches as mpatches;
from fileParser.parseJson import parseJson;
from node.nodeImpl import NodeImpl;
import matplotlib as mpl;
from mpl_toolkits.axes_grid1 import make_axes_locatable;
from util.heatcolorDefine import Color;
from util.binleveldefine import BinInfoLevel;
import sys;
import os;
#matplotlib.use('Agg')
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

def to_percent(temp, percent):
    return percent*temp;

def generate2Denv(axisList,xtick,ytick,dxmim,dxmax,dymin,dymax,resetAxis,width,length):
    
    x_values =[];
    y_values = [];
    centralPoint = [];
    pointfeature = {};
   
    ########################
    points = axisList[True];
    radiusList = axisList["r"];
    #####
    
    #####

    for item in points:
        tx = item['x'];
        ty = item['y'];
        sx = item['dieSizeX'];
        sy = item['dieSizeY'];
        x_values.append(tx);
        y_values.append(ty);
        centralPoint.append(tx);
        centralPoint.append(ty);
        ############
        newKey = [tx,ty].__str__().strip();
        if newKey in pointfeature:
            existNode = pointfeature[newKey];
            existNode.sameNodeCount = existNode.sameNodeCount + 1;
            pointfeature[newKey] = existNode;
        ############
        else :
            newNode = NodeImpl();
            newNode.updateCoordinateAllParam(tx, ty, 0, sx, sy,'g');
            newNode.sameNodeCount = 1;
            pointfeature[[tx,ty].__str__().strip()] = newNode;


    ########################
    m =np.reshape(centralPoint,(-1,2));
       
  
    m2=np.array(m);

    mpl.rcParams['axes.unicode_minus'] = False;
    plt.ion();
    plt.switch_backend('Agg');
    fig = plt.figure(dpi=120, figsize=(9,8));
 
    plt.title('2D feature', fontsize=14);
    plt.tick_params(axis='both', which='major', labelsize=14);


    x_major_locator=MultipleLocator(xtick);
    y_major_locator=MultipleLocator(ytick);
    ax=plt.gca();
 
    colors = [Color.accept.value,Color.more.value, Color.attention.value, Color.abnormal.value,Color.attention.value,Color.critcal.value];
 
    cmap= mpl.colors.ListedColormap(colors);
    cmap.set_under("g");
    cmap.set_over("darkred");
  
    divider = make_axes_locatable(ax);
    cax = divider.append_axes("right", size="10%", pad=0.1);

    norm = mpl.colors.Normalize(vmin=0, vmax=100);
    bounds = [round(elem,2) for elem in np.linspace(0, 100, 5)];

    cb = mpl.colorbar.ColorbarBase(cax,cmap=cmap,norm=norm,
                                    boundaries=[-5]+bounds+[110],
                                    
                                    extend='both',
                                    ticks=bounds,
                                    
                                    spacing='proportional',
                                    orientation='vertical',
                                   
                                    );
    cb.ax.tick_params(labelsize=10);                              

    cb.set_ticklabels([str(BinInfoLevel.accept.value)+" Layer",str(BinInfoLevel.attention.value)+" Layer",str(BinInfoLevel.abnormal.value)+" Layer",str(BinInfoLevel.high.value)+" Layer",str(BinInfoLevel.critcal.value)+" Layer"], True);

    
    for i in radiusList:
  
        a,b = (0.0,0.0);
        theta = np.arange(0, 2*np.pi, 0.01);
        x = a + i*np.cos(theta);
        y = b + i*np.sin(theta);
        ax.plot(x,y,color='b');
        
    for single in m2:
        key = [];
        key.append(single[0]);
        key.append(single[1]);
        
        node = pointfeature[key.__str__().strip()];
        
        binColor = 'g';
        if node.sameNodeCount >= BinInfoLevel.accept.value and node.sameNodeCount < BinInfoLevel.attention.value:
            binColor = Color.accept.value;
        elif  node.sameNodeCount >= BinInfoLevel.attention.value and node.sameNodeCount < BinInfoLevel.abnormal.value:
            binColor = Color.attention.value;   
        elif  node.sameNodeCount >= BinInfoLevel.abnormal.value and node.sameNodeCount < BinInfoLevel.high.value:
            binColor = Color.abnormal.value;
        elif  node.sameNodeCount >= BinInfoLevel.high.value and node.sameNodeCount < BinInfoLevel.critcal.value:
            binColor = Color.high.value;   
        elif  node.sameNodeCount >= BinInfoLevel.critcal.value:
            binColor = Color.critcal.value;
      
                
        if width ==0 and length == 0:
            
            rectangle = mpatches.Rectangle(single, node.stepSizeX, node.stepSizeY, color=binColor, ec="k",linewidth = 1);
            ax.add_patch(rectangle);
        else :   

         
            rectangle = mpatches.Rectangle(single, node.stepSizeX, node.stepSizeY, color=binColor, ec="k",linewidth = 1);
            ax.add_patch(rectangle);
    
    #####
    ax.xaxis.set_major_locator(x_major_locator);
    ax.yaxis.set_major_locator(y_major_locator);
    plt.xlim(dxmim, dxmax);
    plt.ylim(dymin, dymax);
    if resetAxis:
        

        ax.axes.get_yaxis().set_visible(False);
        ax.axes.get_xaxis().set_visible(False);
        #plt.xticks(());
        #plt.yticks(());
    #plt.show();
    return plt;#[max_X,max_Y];
        


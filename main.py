import matplotlib.pyplot as plt;
import configparser;
from fileParser.parseJson2 import parseJson;
from datamap.show3DdistributionProductClearAxis import showConnectionDomain;
from datamap.show2DdistributionHeatMapClearAxis import generate2Denv;
import os;
import gc;
import sys;




def loadConfig():
    config = configparser.ConfigParser();
    sep = os.sep;
    cp = os.getcwd();
    
    print("config file in " + cp);
    
   
    config.read(cp + sep + "config.ini");

    inputfolderPath = config.get('config','inputFolder');
    outputfolderPath = config.get('config','outputFolder');
    feature = config.get('config','feature');
    print("input path : " + inputfolderPath);
    print("output path : " + outputfolderPath);
    print("feature : " + feature);
    return [inputfolderPath,outputfolderPath,feature];

def runDraw(inputPath, outputPath, feature):
    
    count = 0;
    folderPath = inputPath;
    outputfolderPath = outputPath;
    allSubdir = os.listdir(folderPath);

    ### parse layer from folder name ###
    layerList = []
    for it in allSubdir:
        fIndex = it.find('_');
        tLayer = it[0:fIndex];
        #print(tLayer);
        layerList.append(tLayer);
    ###################
    
    
    highestLayer = sorted(list(map(int,layerList)));
    moveScale = int(max(highestLayer))/2;

    for maindir,subdir, file_name_list in os.walk(folderPath):
        #print(subdir);
        for filename in file_name_list:
            apath = os.path.join(maindir, filename);
            ### parse layer from file name ###
            tmp = filename.split("_");
            fLayer = tmp[1];
            #print(fLayer);
            ##################################
            
            pdir = maindir.split(os.sep);
        
            ####
            currentLayer = int(pdir[-1]);
       
            a = parseJson(apath);
        
            zRange = int(fLayer);

            if feature == '2D':
                pic = generate2Denv(a,20,20,-160,160,-160,160,True,0,0);
            elif feature == '3D' :
                pic = showConnectionDomain(a,20,20,-160,160,-160,160,0,zRange,1,0,0,0);
            else:
                sys.exit();
 
           
            fName,fileExt = os.path.splitext(filename);
  
            pic.savefig(outputfolderPath + os.sep + fName + ".jpg");
            
            count = count + 1;
            plt.pause(1);
            pic.clf();
                    
            pic.close();
            print(count);
            gc.collect();
    else :
        print("output finished!");
        
        
        
        
def runDrawWithParameter(inputFile, outputFile, feature, showlayers):
    

    
    filename = os.path.basename(inputFile);

    tmp = filename.split("_");
    fLayer = tmp[1];
    #print(fLayer);
    apath = inputFile;
    ##################################
    a = parseJson(apath);
    currentLayer = int(fLayer);
    zRange = currentLayer if currentLayer > int(showlayers) else int(showlayers);
    if feature == '2D':
        pic = generate2Denv(a,20,20,-160,160,-160,160,True,0,0);
    elif feature == '3D' :
        pic = showConnectionDomain(a,20,20,-160,160,-160,160,0,zRange,1,0,0,0);
    else:
        sys.exit();
        
    pic.savefig(outputFile,transparent=True);
              
            
    
    pic.clf();
                    
    pic.close();
           
    gc.collect();
    
    print("output finished!");  
    #####
    
  
if __name__ == "__main__": 
    '''
    paraList = [];
    paraList = loadConfig();     
    if paraList:
        runDraw(paraList[0],paraList[1],paraList[2]);
  
    '''
    #runDrawWithParameter("C:\\GW\\GW\\SC2\\BIGData\\output\\Demo\\distribution\\sample\\20190213025224_19_53.txt","C:\\GW\\GW\\SC2\\BIGData\\output\\Demo\\image\\Sample\\test\\6.jpg",'3D',20);
    
    defaultlayer = 30;
    if sys.argv.__len__() == 5:
        defaultlayer = sys.argv[4];
  
    runDrawWithParameter(sys.argv[1],sys.argv[2],sys.argv[3],defaultlayer);
    sys.exit();
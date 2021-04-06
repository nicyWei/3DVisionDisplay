
import json;
import gc;
import os;
import sys;
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])
#print(rootPath)
#def parseJson(jfolderPath, fileName):
def parseJson(aPath):
    #jPath = jfolderPath + "\\" + fileName;
    jPath = aPath;
    result = False;
    resultList = [];
    waferAttribute = {};
    deviceList = [];
    with open(jPath) as f:
        while 1: 
            contents = f.readlines();
            #print(contents);
            if not contents:
                break;
            for line in contents:
                
                #print(line);
                jLine = json.loads(line);
                #print(type(jLine));
                #print(jLine);
                aixsList = jLine["mapData"];
                radius = jLine["r"];
                #print(aixsList);
                if isinstance(aixsList, list):
                    result = True;
                    resultList = aixsList;
                    ####
                    for point in aixsList:
                        waferAttribute = point['waferAttributes'];
                        device = waferAttribute['device'];
                        deviceList.append(device);
                    deviceList = list(set(deviceList));
                    ####
                    
                else:
                    result = False;
            gc.collect();
            break;
            gc.collect();   
        f.close();
        
    return   {result:resultList,"r":radius,"deviceList":deviceList}





    
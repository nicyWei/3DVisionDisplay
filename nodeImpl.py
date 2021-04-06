import os;

class NodeImpl:
    xCoordinate = 0;
    yCoordinate = 0;
    zCoordinate = 0; # same as layer
    stepSizeX = 0;
    stepSizeY = 0;
    ismarked = False;
    isbenchmark = False;
    sameNodeCount = 0;
    color = 'g';
    #def __init__(self):
    
    
    def updateCoordinateAllParam(self, x, y, z, sX, sY,inColor): 
        self.xCoordinate = x;
        self.yCoordinate = y;
        self.zCoordinate = z;
        self.stepSizeX = sX;
        self.stepSizeY = sY;
        self.color = inColor;
        
    def updateCoordinateParam(self, x, y, z): 
        self.xCoordinate = x;
        self.yCoordinate = y;
        self.zCoordinate = z;
  
    
    def markNodeAsBad(self, ismark):
        self.ismarked = ismark;
        
    def updateNodeFeature(self,sX,sY,inColor):
        self.stepSizeX = sX;
        self.stepSizeY = sY;
        self.color = inColor;
        
    def markAsBenchMark(self, isInCenterLine):
        self.isbenchmark = isInCenterLine;
        
    def generateNodePoint(self, outputPath, fileName, onlyCoordinate,is3D): 
        fileInfo = outputPath + "\\" + fileName;
        if is3D:
            if onlyCoordinate:
                nodePoint = [self.xCoordinate,self.yCoordinate,self.zCoordinate];
            else:
                nodePoint = [self.xCoordinate,self.yCoordinate,self.zCoordinate,self.stepSizeX,self.stepSizeY,self.ismarked];
                    
                    #if not os.path.exists(fileInfo):
            with open(fileInfo, mode ='a',encoding='utf-8') as f:
                print(nodePoint.__str__(),file = f);
       
        else:
            if onlyCoordinate:
                nodePoint = [self.xCoordinate,self.yCoordinate];
            else:
                nodePoint = [self.xCoordinate,self.yCoordinate,self.stepSizeX,self.stepSizeY,self.ismarked];
                   
                    #if not os.path.exists(fileInfo):
            with open(fileInfo, mode ='a',encoding='utf-8') as f:
                print(nodePoint.__str__(),file = f);     
       # nodePoint.append(X)
        #print("the node is = " + nodePoint.__str__());
        return nodePoint;
        
        
#To find width and number of cells of probablity square around Datum point
from positionError import getE
import math

def getPmapType(E,Search_Area_Width):

    Cells = {'A':[3,E*2],'B':[4,E*1.50],'C':[5,E*1.20],'D':[6,E*1],'E':[7,E*0.86],'F':[8,E*0.75],'G':[9,E*0.67],'H':[10,E*0.60],'I':[11,E*0.55],'J':[12,E*0.50]}

    Pmap = {0.27:'I',0.33:'G',0.43:'E',0.50:'J',0.60:('H','C'),0.75:'F',0.82:'I',1.00:('J','G','D','A'),1.20:'H',1.29:'E',1.36:'I',1.50:('J','F','B'),1.67:'G',1.80:('H','C'),1.91:'I',2.00:('J','D'),2.14:'E',2.25:'F',2.33:'G',2.40:'H',2.45:'I',2.50:'J',3.00:list(Cells.keys()) }

    Adjusted_Search_Radius = Search_Area_Width/2
    Adjusted_Search_Factor = Adjusted_Search_Radius/E
    D = abs(list(Pmap.keys())[0] - Adjusted_Search_Factor)
    Round = list(Pmap.keys())[0]

    for i in Pmap.keys():
        Diff = abs(Adjusted_Search_Factor - i)
        if(Diff>D):
            break
        D = Diff
        Round=i

    PMap_Type = Pmap[Round][0]
    Cell_Width = Cells[PMap_Type][1]
    No_of_cells = math.pow(Cells[PMap_Type][0],2)
    return (PMap_Type,Cell_Width,No_of_cells)





    













 

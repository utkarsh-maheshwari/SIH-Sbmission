import math
from dms2dec.dms_convert import dms2dec
import Pmap
import Datum
import positionError
import availableSearchEffort
import effortAllocation
import PMap_Line
from effortAllocation import getSeachAreaWidth
import HeatmapPointData
import HeatmapLineData


def Calc_distance(point1, point2):
    
    R = 6378.1

    lat1 = math.radians(point1[0])
    lon1 = math.radians(point1[1])
    lat2 = math.radians(point2[0])
    lon2 = math.radians(point2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance



def getData(formdata):

    LKP_time=float(formdata['LKP_time'])
    LKP_Altitude=float(formdata['LKP_Altitude'])
    Distress_time=float(formdata['Distress_time'])
    Distress_Altitude=float(formdata['Distress_Altitude'])
    brng=float(formdata['brng'])
    GSpeed=float(formdata['GSpeed'])
    VSpeed=float(formdata['VSpeed'])
    Glide_TAS=float(formdata['Glide_TAS'])
    Glide_Ratio=float(formdata['Glide_Ratio'])
    Daylight_hours=8
    Search_Speed=150
    

    ###input these as DD MM SS,DD MM SS
    destination=formdata['destination']
    if destination.find(','):
        destination=destination.split(',')
        for i in range(2):
            a=destination[i].split()
            if i==0:
                decVal=round(dms2dec(f'''{a[0]}°{a[1]}'{a[2]}N"'''),5)
                destination[i]=decVal
            if i==1:
                decVal=round(dms2dec(f'''{a[0]}°{a[1]}'{a[2]}E"'''),5)
                destination[i]=decVal
    else:
        print("improper format")
    
    Distress_position=formdata['Distress_position']
    if Distress_position.find(','):
        Distress_position=Distress_position.split(',')
        for i in range(2):
            a=Distress_position[i].split()
            if i==0:
                decVal=round(dms2dec(f'''{a[0]}°{a[1]}'{a[2]}N"'''),5)
                Distress_position[i]=decVal
            if i==1:
                decVal=round(dms2dec(f'''{a[0]}°{a[1]}'{a[2]}E"'''),5)
                Distress_position[i]=decVal
    else:
        print("improper format")

    LKP_position=formdata['LKP_position']
    if LKP_position.find(','):
        LKP_position=LKP_position.split(',')
        for i in range(2):
            a=LKP_position[i].split()
            if i==0:
                decVal=round(dms2dec(f'''{a[0]}°{a[1]}'{a[2]}N"'''),5)
                LKP_position[i]=decVal
            if i==1:
                decVal=round(dms2dec(f'''{a[0]}°{a[1]}'{a[2]}E"'''),5)
                LKP_position[i]=decVal
    else:
        print("improper format")

    Communication_Interval = .5 
    Terrain_Altitude = 0                                                                      
    Altitude_Loss = Distress_Altitude - Terrain_Altitude                                            
    Comm_Mode = 'GPS' 
    Craft_Type = 'DualEngine' 
    Search_Altitude = '600' 
    Search_obj = 'SmallAircraft' 
    visibility = '6' 
    vegetation = 'Moderate' 
    search_effort,Corr_Sweep_Width,Search_Endurance = availableSearchEffort.getSearchEffort(Search_Speed,Daylight_hours,Search_Altitude,Search_obj,visibility,vegetation)
    Descent_Rate = Glide_TAS*101/Glide_Ratio         
    Datum_point = []

    if(Distress_time and Distress_position): 
        E = positionError.getE(Comm_Mode,Craft_Type,GSpeed,VSpeed,Distress_Altitude,Terrain_Altitude,LKP_time,Distress_time)
        Altitude_Loss = Distress_Altitude - Terrain_Altitude                                            
        Descent_Time = Altitude_Loss/Descent_Rate/60                                                    
        Glide_Distance = ((Glide_TAS*Descent_Time)/60)*1.852                                            
        Datum_point = Datum.Estimated_position(Distress_position,Glide_Distance,brng)
        Seach_area_width = effortAllocation.getSeachAreaWidth(search_effort,E,Corr_Sweep_Width,None,Search_Speed,Search_Endurance)

        PMap_Type,Cell_Width,No_of_cells = Pmap.getPmapType(E,Seach_area_width)                                                       
        Grid = HeatmapPointData.getGrid(PMap_Type)

        return Datum_point,Grid,Cell_Width

    if(Distress_position==None and Distress_time): 
        E = positionError.getE(Comm_Mode,Craft_Type,GSpeed,VSpeed,LKP_Altitude,Terrain_Altitude,LKP_time,Distress_time)
        Distance = ((Distress_time - LKP_time) * Gspeed ) / 0.621371                                  
        Est_Distress_position = Datum.Estimated_position(LKP_position,Distance,brng)                             
        Altitude_Loss = LKP_Altitude - Terrain_Altitude                                            
        Descent_Time = Altitude_Loss/Descent_Rate/60
        Glide_Distance = ((Glide_TAS*Descent_Time)/60)*1.852                                            
        Datum_point = Datum.Estimated_position(Est_Distress_position,Glide_Distance,brng)                                   
        Seach_area_width = effortAllocation.getSeachAreaWidth(search_effort,E,Corr_Sweep_Width,None,Search_Speed,Search_Endurance)

        PMap_Type,Cell_Width,No_of_cells = Pmap.getPmapType(E,Seach_area_width)                                                   
        Grid = HeatmapPointData.getGrid(PMap_Type)
        return Datum_point,Grid,Cell_Width

    if(Distress_position==None and Distress_time ==None): 
        
        Sample_len = 1/12  
        samples = []
        i = 0
        PMap_Type = []
        Cell_Width = []
        No_of_cells = []
        Datum_point = []
        Grid = []

        while(i<=Communication_Interval):
            samples.append(LKP_time+i)
            i= i+Sample_len
        for i in len(samples):
            Distance = ((samples[i] - LKP_time) * speed) / 0.621371                           
            E = positionError.getE(Comm_Mode,Craft_Type,GSpeed,VSpeed,LKP_Altitude,Terrain_Altitude,LKP_time,samples[i])
            Est_Distress_position = Datum.Estimated_position(LKP_position,Distance, brng)                  
            Altitude_Loss = LKP_Altitude - Terrain_Altitude                                            
            Descent_Time = Altitude_Loss/Descent_Rate/60
            Glide_Distance = ((Glide_TAS*Descent_Time)/60)*1.852                                            
            Datum_point[i] = Datum.Estimated_position(Est_Distress_position,Glide_Distance,brng)  
            Seach_area_width = effortAllocation.getSeachAreaWidth(search_effort,E,Corr_Sweep_Width,None,Search_Speed,Search_Endurance)

            PMap_Type[i],Cell_Width[i],No_of_cells[i] = (Pmap.getPmapType(E,Seach_area_width))                                     
            Grid[i] = HeatmapPointData.getGrid(typeMap[i](0))

        Datum_line = [Est_Distress_position,destination]
        Datum_length = Calc_distance(Est_Distress_position,destination)
        E = positionError.getE(Comm_Mode,Craft_Type,GSpeed,VSpeed,LKP_Altitude,Terrain_Altitude,LKP_time,samples[len(samples)])
        Seach_area_width = effortAllocation.getSeachAreaWidth(search_effort,E,Corr_Sweep_Width,Datum_length,Search_Speed,Search_Endurance)
        
        PMap_Type[len(PMap_Type)],Cell_Width[len(Cell_Width)],No_of_cells[len(No_of_cells)] = PMap_Line.getPmapType(E,Seach_area_width)
        Grid.append(HeatmapLineData.getGrid(typeMap[len()](0)))

        return Datum_point,Datum_line,Grid,Cell_Width

    
    
    


import math

def getE(Comm_Mode,Craft_Type,GSpeed,VSpeed,Distress_Altitude,Terrain_Altitude,LKP_time,Distress_time):
   
    Nav_Fix_Err_List = {'GPS':0.1,'Radar':1,'Visual Fix':1,'Celestial Fix':2,'Marine Radio Beacon':4,'LORAN-C':1,'INS':0.5,'VOR':0.5,'TACAN':0.5}

    Craft_Type_Err_List = {'SingleEngine':15,'DualEngine':10,'MultiEngine':5}

    DR_Err_List = {'MultiEngine':5,'DualEngine':10,'SingleEngine':15}
   
   
    #GSpeed = GSpeed*1.15078                                         #in mph
    #VSpeed = VSpeed*1.15078                                         #in mph

    #Distress_Altitude = Distress_Altitude*0.000164579               #in NM
    #Terrain_Altitude = Terrain_Altitude*0.000164579                 #in NM

    Nav_Fix_err = Nav_Fix_Err_List[Comm_Mode]                       #in Nautical miles (NM)
    DR_err = DR_Err_List[Craft_Type]                                #in %

    Altitude_diff = Distress_Altitude - Terrain_Altitude            #in feets

    DR_distance = (LKP_time - Distress_time)*GSpeed                 #in NM
    DR_Nav_Err = 0.01*DR_err * DR_distance                          #in NM
    GlideDistance = (Altitude_diff * GSpeed) / VSpeed * 60               #in NM
    Init_Pos_Err_X = Nav_Fix_err + DR_Nav_Err + GlideDistance       #in NM

    Init_Pos_Err_Y = Nav_Fix_err + DR_Nav_Err                       #in NM

    E = math.sqrt( math.pow(Init_Pos_Err_X,2) + math.pow(Init_Pos_Err_Y,2) )    #in NM

    return E
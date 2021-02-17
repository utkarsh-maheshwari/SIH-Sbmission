
Sweep_width_List = {
    'Person':{
        '150':{
            '6':0.7,
            '9':0.7,
            '19':0.9,
            '28':0.9,
            '37':0.9
        },
        '300':{
            '6':0.7,
            '9':0.7,
            '19':0.9,
            '28':0.9,
            '37':0.9
        },
        '450':(),
        '600':()
    },
    'Vehicle':{
        '150':{
            '6':1.7,
            '9':2.4,
            '19':2.4,
            '28':2.4,
            '37':2.4
        },
        '300':{
            '6':2.6,
            '9':2.6,
            '19':2.8,
            '28':2.8,
            '37':2.8
        },
        '450':{
            '6':1.9,
            '9':3.1,
            '19':3.1,
            '28':3.1,
            '37':3.1
        },
        '600':{
            '6':1.9,
            '9':2.8,
            '19':3.7,
            '28':3.7,
            '37':3.7
        }
    },
    'SmallAircraft':{
        '150':{
            '6':1.9,
            '9':2.6,
            '19':2.6,
            '28':2.6,
            '37':2.6
        },
        '300':{
            '6':1.9,
            '9':2.8,
            '19':2.8,
            '28':3,
            '37':3
        },
        '450':{
            '6':1.9,
            '9':2.8,
            '19':3.3,
            '28':3.3,
            '37':3.3
        },
        '600':{
            '6':1.9,
            '9':3,
            '19':3.7,
            '28':3.7,
            '37':3.7
        }
    },
    'BigAircraft':{
        '150':{
            '6':2.2,
            '9':3.7,
            '19':4.1,
            '28':4.1,
            '37':4.1
        },
        '300':{
            '6':3.3,
            '9':5,
            '19':5.6,
            '28':5.6,
            '37':5.6
        },
        '450':{
            '6':3.7,
            '9':5.2,
            '19':5.9,
            '28':5.9,
            '37':5.9
        },
        '600':{
            '6':4.1,
            '9':5.2,
            '19':6.5,
            '28':6.5,
            '37':6.5
        }
    }
}


Terrain_Correction_Factor_List = {'Person': {'Low':0.5, 'Moderate':0.3, 'High':0.1},
                     'Vehicle':{'Low':0.7, 'Moderate':0.4, 'High':0.1},
                     'SmallAircraft':{'Low':0.7, 'Moderate':0.4, 'High':0.1},
                     'BigAircraft':{'Low':0.8, 'Moderate':0.4, 'High':0.1} }


def getSearchEffort(Search_Speed,Daylight_hours,Search_Altitude,Search_obj,visibility,vegetation):                 

    Search_Endurance =0.85 * Daylight_hours                        #in hours
    Uncorr_Sweep_Width = Sweep_width_List[Search_obj][Search_Altitude][visibility]          #in kms    
    Terrain_Correction_Factor = Terrain_Correction_Factor_List[Search_obj][vegetation]      
    Velocity_Correction_Factor = 1.0 #for land
    Fatigue_Correction_Factor = 1.0 #No crew fatigue considered

    Corr_Sweep_Width = Uncorr_Sweep_Width * Terrain_Correction_Factor * Velocity_Correction_Factor * Fatigue_Correction_Factor    #in kms
    Search_Effort = Search_Speed * Search_Endurance * Corr_Sweep_Width * 0.621371           #in NM*NM                      #

    #Seperation_Ratio = 0 # for computing for a single point
    return Search_Effort,Corr_Sweep_Width,Search_Endurance










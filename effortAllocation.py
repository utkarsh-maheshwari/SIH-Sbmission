import math

def solve_quad(a, b, c):
    D = pow(b,2) - 4*a*c
    t1 = (-b - math.sqrt(D) ) / (2*a)
    t2 = (-b + math.sqrt(D) ) / (2*a)
    if(t1>0):
        return t1
    if(t2>0):
        return t2
        
def getSeachAreaWidth(Search_Effort,E,Corr_Sweep_width,Datum_Length,Search_Speed,Search_Endurance):

    if(Datum_Length==None):
        Effort_Factor = E*E                                                                         #in NM*NM
        Relative_Effort = Search_Effort/Effort_Factor 
        Optimal_Search_Factor = solve_quad(14.89,-14.59,-Relative_Effort)                       #calc from fig N-5    
        Optimal_Search_Radius = Optimal_Search_Factor * E                                           #in NM
        Optimal_Search_Area = 4 * pow(Optimal_Search_Radius,2)                                      #in NM*NM
        Optimal_Coverage_Factor = Search_Effort / Optimal_Search_Area                               
        Optimal_Track_Spacing = Corr_Sweep_width* 0.621371 / Optimal_Coverage_Factor                #in NM
        Nearest_Ass_Track_Spacing = round(Optimal_Track_Spacing) #Doubt                             #in NM
        Adjusted_Search_Area = Search_Speed * Search_Endurance * Nearest_Ass_Track_Spacing          #in NM*NM
        Adjusted_Search_Radius = math.sqrt(Adjusted_Search_Area)/2                                  #in NM
        Adjusted_Search_Area_Length = 2*Adjusted_Search_Radius                                      #in NM
        Adjusted_Search_Area_Width = 2*Adjusted_Search_Radius                                       #in NM

    else:
        Effort_Factor = E*Datum_Length
        Relative_Effort = Search_Effort/Effort_Factor 
        Optimal_Search_Factor = solve_quad(1.875,0,-Relative_Effort)                                                        #calc from fig N-5
        Optimal_Search_Radius = Optimal_Search_Factor * E                                           #in NM
        Optimal_Search_Area = 2*Optimal_Search_Radius*Datum_Length                                      #in NM*NM
        Optimal_Coverage_Factor = Search_Effort / Optimal_Search_Area                               
        Optimal_Track_Spacing = Corr_Sweep_width* 0.621371 / Optimal_Coverage_Factor                #in NM
        Nearest_Ass_Track_Spacing = round(Optimal_Track_Spacing) #Doubt                             #in NM
        Adjusted_Search_Area = Search_Speed * Search_Endurance * Nearest_Ass_Track_Spacing          #in NM*NM
        Adjusted_Search_Radius = Adjusted_Search_Area/(2*Datum_Length)                                  #in NM
        Adjusted_Search_Area_Length = Datum_Length                                     #in NM
        Adjusted_Search_Area_Width = 2*Adjusted_Search_Radius                                       #in NM
    
    return  Adjusted_Search_Area_Width

import math

#distress_time = input()                                                                         #in hours
# distress_position = input()                                                                     #in (deg,deg)

# Est_Datum_point = Estimated_position(Glide_Distance,brng)                                       #in (deg,deg)

def Estimated_position(distress_position,distance,brng):
    R = 6378.1                                                                                  #in km

    lat1 = math.radians(distress_position[0])  #Current lat point converted to radians
    lon1 = math.radians(distress_position[1])  #Current long point converted to radians

    lat2 = math.asin( math.sin(lat1)*math.cos(distance/R) +
                math.cos(lat1)*math.sin(distance/R)*math.cos(brng))

    lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(distance/R)*math.cos(lat1),
                        math.cos(distance/R)-math.sin(lat1)*math.sin(lat2))

    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)

    Estimated_position = [lat2,lon2]
    return Estimated_position

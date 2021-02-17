
#outputs crash path coordinates in an interval of 5 secs

import xlrd 
import math
import time

def solve_quad(a, b, c):
    D = pow(b,2) - 4*a*c
    t1 = (-b - math.sqrt(D) ) / (2*a)
    t2 = (-b + math.sqrt(D) ) / (2*a)
    if(t1>0):
        return t1
    if(t2>0):
        return t2

def findLoc():
    g = 10;
    # Give the location of the file 
    loc = ("Data.xlsx") 
  
    # To open Workbook 
    try:
        with xlrd.open_workbook(loc) as wb:

            sheet = wb.sheet_by_index(0)
            nrows=sheet.nrows-1
            # print(nrows)
            v = float(input("Enter velocity of aircraft :"))
        ##    Sx_prev, Sx_curr = input("Enter prev and current x component of position of the aircraft :").split()
        ##    Sy_prev, Sy_curr = input("Enter prev and current y component of position of the aircraft :").split()
        ##    Sz_prev, Sz_curr = input("Enter prev and current z component of position of the aircraft :").split()

            xcol=sheet.col_values(0)[1:]
            ycol=sheet.col_values(1)[1:]
            zcol=sheet.col_values(2)[1:]
            # print(xcol,ycol,zcol)

            Sx_prev=xcol[nrows-2]
            Sx_curr=xcol[nrows-1]
            Sy_prev=ycol[nrows-2]
            Sy_curr=ycol[nrows-1]
            Sz_prev=zcol[nrows-2]
            Sz_curr=zcol[nrows-1]

    except Exception as e:
        print(e)
    finally:
        wb.release_resources()
        
    dx = Sx_curr - Sx_prev
    dy = Sy_curr - Sy_prev
    dz = Sz_curr - Sz_prev
    
    #print(dx,dy,dz)
    #test = math.atan(1/1.76)

    #print(test, "test" )

    theta = (180/math.pi)*math.atan( dz/float(math.sqrt( (pow(dx,2)) + (pow(dy,2)) ) ))
    phi = (180/math.pi)*math.atan(dy/dx)

    #print("theta ", theta, "phi ", phi)

    vz = (v*math.cos(theta))
    vx = abs(v*math.sin(theta)*math.sin(phi))
    vy = abs(v*math.sin(theta)*math.cos(phi))

    #print("speeds ", vx, vy, vz)

    t =2
    height  = Sz_curr
    sz=0
    while(Sz_curr+sz>0):
        sx = vx*t
        sy = vy*t
        sz = vz*t - 0.5*g*t*t
        
        #There is no acceleration in x,y direction. Thus, velocity in x,y direction won't change 
        if(Sz_curr + sz>0):
            Sx_curr += sx
            Sy_curr += sy
            Sz_curr += sz
            print(Sx_curr,",",Sy_curr,",",Sz_curr)
            vz -= g*t

    t = solve_quad(0.5*g, -vz, -Sz_curr)
    Sz_curr = 0
    Sx_curr += vx*t
    Sy_curr += vy*t

    print("Final coordinates are", Sx_curr, ",", Sy_curr,",", Sz_curr)
    
findLoc()
    

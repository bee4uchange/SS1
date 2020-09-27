import math

EARTH_R = 6371
PI = 3.14159265

# SYSTEM OF DMS
# Input location of A
print("Enter location with the form like (e.g. 40 44 55N,73 59 11W)")
A = list(input('Point A: ').split(","))
latA = A[0].split(" ")
dict_latA = {"D": float(latA[0]), "M": float(latA[1]), "S": float(latA[2][:-1]), "Dir": latA[2][-1:]}
longA = A[1].split(" ")
dict_longA = {"D": float(longA[0]), "M": float(longA[1]), "S": float(longA[2][:-1]), "Dir": longA[2][-1:]}

# Input location of B
B = list(input('Point B: ').split(","))
latB = B[0].split(" ")
dict_latB = {"D": float(latB[0]), "M": float(latB[1]), "S": float(latB[2][:-1]), "Dir": latB[2][-1:]}
longB = B[1].split(" ")
dict_longB = {"D": float(longB[0]), "M": float(longB[1]), "S": float(longB[2][:-1]), "Dir": longB[2][-1:]}


# SYSTEM OF DD
latA_deg = dict_latA['D'] + (dict_latA['M'] / 60) + (dict_latA['S'] / 3600)
latB_deg = dict_latB['D'] + (dict_latB['M'] / 60) + (dict_latB['S'] / 3600)
longA_deg = dict_longA['D'] + (dict_longA['M'] / 60) + (dict_longA['S'] / 3600)
longB_deg = dict_longB['D'] + (dict_longB['M'] / 60) + (dict_longB['S'] / 3600)
# Point A
if dict_latA['Dir'] == 'N':
    latA_deg = latA_deg
else:
    latA_deg = -latA_deg
latA_rad = (latA_deg*PI)/180

if dict_longA['Dir'] == 'E':
    longA_deg = longA_deg
else:
    longA_deg = -longA_deg
longA_rad = (longA_deg*PI)/180

# Point B
if dict_latB['Dir'] == 'N':
    latB_deg = latB_deg
else:
    latB_deg = -latB_deg
latB_rad = (latB_deg*PI)/180

if dict_longB['Dir'] == 'E':
    longB_deg = longB_deg
else:
    longB_deg = -longB_deg
longB_rad = (longB_deg*PI)/180

# CALCULATION
del_lat = latB_rad - latA_rad
del_long = longB_rad - longA_rad
a = pow(math.sin(del_lat/2), 2) + math.cos(latA_rad)*math.cos(latB_rad)*pow(math.sin(del_long/2), 2)
c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
d = c*EARTH_R

print("DISTANCE:", '{:06.2f}'.format(c*EARTH_R), 'km')

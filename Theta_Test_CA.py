#Import Packages
#%matplotlib inline
import glob
import os
import numpy as np
import pylab as pl
import pandas as pd
import matplotlib.pyplot as plt

#Read in all files
#This is a highly inefficient way of reading in multiple files I'm sure, so I am exploring a more efficient way of doing so
#These files are from KMFR soundings from 7/17/2021 1200UTC to 7/18/2021 0000UTC

#Skip rows will skip line 1 (which in Python correlates to the second row) which in my data defines the units of the header, line 0
#Python requires me to also add skip row -1 or else the header will not read in properly

REV_17_00Z = pd.read_csv('C:/Users/chris/Documents/GradResearch/REV_17_00Z.csv',skiprows=(-1,1),header=0)
REV_17_12Z = pd.read_csv('C:/Users/chris/Documents/GradResearch/REV_17_12Z.csv',skiprows=(-1,1),header=0)
REV_18_00Z = pd.read_csv('C:/Users/chris/Documents/GradResearch/REV_18_00Z.csv',skiprows=(-1,1),header=0)
REV_18_12Z = pd.read_csv('C:/Users/chris/Documents/GradResearch/REV_17_12Z.csv',skiprows=(-1,1),header=0)
REV_19_00Z = pd.read_csv('C:/Users/chris/Documents/GradResearch/REV_19_00Z.csv',skiprows=(-1,1),header=0)
REV_19_12Z = pd.read_csv('C:/Users/chris/Documents/GradResearch/REV_19_12Z.csv',skiprows=(-1,1),header=0)

#Assign variables
g = 9.81; #gravity
R = 287; #dry air gas constant
cp = 1004; #specific heat at constant pressure
eps = .622; # for Clausius
Lv = 2.5E+6; # Latent heat of vaporization

#Assign empty lists which will be filled with variables from CSV files
#PM: Pressure Reno
PM_1700=[]
PM_1712=[]
PM_1800=[]
PM_1812=[]
PM_1900=[]
PM_1912=[]

#HM: Height Reno
HM_1700=[]
HM_1712=[]
HM_1800=[]
HM_1812=[]
HM_1900=[]
HM_1912=[]

#TM: Temp. Reno
TM_1700=[]
TM_1712=[]
TM_1800=[]
TM_1812=[]
TM_1900=[]
TM_1912=[]

#DM: Dew Point Reno
DM_1700=[]
DM_1712=[]
DM_1800=[]
DM_1812=[]
DM_1900=[]
DM_1912=[]

#RHM: Rel. Humidity Reno
RHM_1700=[]
RHM_1712=[]
RHM_1800=[]
RHM_1812=[]
RHM_1900=[]
RHM_1912=[]

#MM: Mixing Ratio Reno
MM_1700=[]
MM_1712=[]
MM_1800=[]
MM_1812=[]
MM_1900=[]
MM_1912=[]

#TheM: Theta-e Reno
TheM_1700=[]
TheM_1712=[]
TheM_1800=[]
TheM_1812=[]
TheM_1900=[]
TheM_1912=[]

#ThM: Theta Reno
ThM_1700=[]
ThM_1712=[]
ThM_1800=[]
ThM_1812=[]
ThM_1900=[]
ThM_1912=[]

#Fill in empty lists with CSV colums using list(file_name(column_header))
PM_1700=list(REV_17_00Z["PRES"])
PM_1712=list(REV_17_12Z["PRES"])
PM_1800=list(REV_18_00Z["PRES"])
PM_1812=list(REV_18_12Z["PRES"])
PM_1900=list(REV_19_00Z["PRES"])
PM_1912=list(REV_19_12Z["PRES"])

TM_1700=list(REV_17_00Z["TEMP"])
TM_1712=list(REV_17_12Z["TEMP"])
TM_1800=list(REV_18_00Z["TEMP"])
TM_1812=list(REV_18_12Z["TEMP"])
TM_1900=list(REV_19_00Z["TEMP"])
TM_1912=list(REV_19_12Z["TEMP"])

DM_1700=list(REV_17_00Z["DWPT"])
DM_1712=list(REV_17_00Z["DWPT"])
DM_1800=list(REV_17_00Z["DWPT"])
DM_1812=list(REV_17_00Z["DWPT"])
DM_1900=list(REV_17_00Z["DWPT"])
DM_1912=list(REV_17_00Z["DWPT"])

RHM_1700=list(REV_17_00Z["RELH"])
RHM_1712=list(REV_17_12Z["RELH"])
RHM_1800=list(REV_18_00Z["RELH"])
RHM_1812=list(REV_18_12Z["RELH"])
RHM_1900=list(REV_19_00Z["RELH"])
RHM_1912=list(REV_19_12Z["RELH"])

MM_1700=list(REV_17_00Z["MIXR"])
MM_1712=list(REV_17_12Z["MIXR"])
MM_1800=list(REV_18_00Z["MIXR"])
MM_1812=list(REV_18_12Z["MIXR"])
MM_1900=list(REV_19_00Z["MIXR"])
MM_1912=list(REV_19_12Z["MIXR"])

TheM_1700=list(REV_17_00Z["THTE"])
TheM_1712=list(REV_17_12Z["THTE"])
TheM_1800=list(REV_18_00Z["THTE"])
TheM_1812=list(REV_18_12Z["THTE"])
TheM_1900=list(REV_19_00Z["THTE"])
TheM_1912=list(REV_19_12Z["THTE"])

ThM_1700=list(REV_17_00Z["THTA"])
ThM_1712=list(REV_17_12Z["THTA"])
ThM_1800=list(REV_18_00Z["THTA"])
ThM_1812=list(REV_18_12Z["THTA"])
ThM_1900=list(REV_19_00Z["THTA"])
ThM_1912=list(REV_19_12Z["THTA"])

HM_1700=list(REV_17_00Z["HGHT"])
HM_1712=list(REV_17_12Z["HGHT"])
HM_1800=list(REV_18_00Z["HGHT"])
HM_1812=list(REV_18_12Z["HGHT"])
HM_1900=list(REV_19_00Z["HGHT"])
HM_1912=list(REV_19_12Z["HGHT"])

#Since heights in the CSV are in meters, I figured graphing in kilometers would look better
#This code translates all values in list HM_1712 and HM_1800 to km

#Since I want the first data point on the following graph to start on the x-axis and not above it,
    #I must subtract .405 km from every data point in the HMk lists.
    #This will give me Height AGL, instead of just Height
m_km=1000
#HMk: Height in kilometers Reno
HMk_1700 = [(i/m_km)-.405 for i in HM_1700]
HMk_1712 = [(i/m_km)-.405 for i in HM_1712]
HMk_1800 = [(i/m_km)-.405 for i in HM_1800]
HMk_1812 = [(i/m_km)-.405 for i in HM_1812]
HMk_1900 = [(i/m_km)-.405 for i in HM_1900]
HMk_1912 = [(i/m_km)-.405 for i in HM_1912]

#Define size of figure
plt.figure(figsize=(20, 10))
#plt.subplot defines which subplot in a figure is selected. Here, subplot(1,2,1) defines a subplot
    #of size 1 row, 2 columns, in which the 1st subplot (the leftmost) is selected
"""
plt.subplot(1,2,1)
plt.title("Equivalent Potential Temperature - Reno, NV Sounding",fontsize=16)
plt.plot(TheM_1700,HMk_1700,label = "July 17 - 0000 UTC", color="blue", linestyle = 'dotted')
plt.plot(TheM_1712,HMk_1712,label = "July 17 - 0012 UTC", color="navy")
plt.xlabel("Theta-e (K)",fontsize=14)
plt.ylabel("Height AGL (km)",fontsize=14)
plt.legend(fontsize=14)
plt.xlim(310, 355)
plt.ylim(0, 12)

#plt.subplot defines which subplot in a figure is selected. Here, subplot(1,2,2) defines a subplot
    #of size 1 row, 2 columns, in which the 2st subplot (the rightmost) is selected
plt.subplot(1,2,2)
plt.title("Potential Temperature - Reno,NV Sounding",fontsize=16)
plt.plot(ThM_1700,HMk_1700,label = "July 17 - 0000 UTC", color="blue", linestyle = 'dotted')
plt.plot(ThM_1712,HMk_1712,label = "July 17 - 0012 UTC", color="navy")
plt.xlabel("Theta (K)",fontsize=14)
plt.ylabel("Height AGL (km)",fontsize=14)
plt.legend(fontsize=14)
plt.xlim(290, 355)
plt.ylim(0, 12)

"""
#plt.subplot
plt.subplot(1,6,1)
plt.title("July 17 00Z Reno, NV Sounding",fontsize=8)
plt.plot(TheM_1700,HMk_1700,label = "Equivalent Potential Temperature", color="black")
plt.plot(ThM_1700,HMk_1700,label = "Potential Temperature", color="red")
plt.xlabel("Theta-e (K)",fontsize=8)
plt.ylabel("Height AGL (km)",fontsize=8)
plt.legend(fontsize=6)
plt.xlim(300, 370)
plt.ylim(0, 14)

plt.subplot(1,6,2)
plt.title("July 17 12Z Reno, NV Sounding",fontsize=8)
plt.plot(TheM_1712,HMk_1712,label = "Equivalent Potential Temperature", color="black")
plt.plot(ThM_1712,HMk_1712,label = "Potential Temperature", color="red")
plt.xlabel("Theta-e (K)",fontsize=8)
#plt.ylabel("Height AGL (km)",fontsize=8)
plt.legend(fontsize=6)
plt.xlim(300, 370)
plt.ylim(0, 14)

plt.subplot(1,6,3)
plt.title("July 18 00Z Reno, NV Sounding",fontsize=8)
plt.plot(TheM_1800,HMk_1800,label = "Equivalent Potential Temperature", color="black")
plt.plot(ThM_1800,HMk_1800,label = "Potential Temperature", color="red")
plt.xlabel("Theta-e (K)",fontsize=8)
#plt.ylabel("Height AGL (km)",fontsize=8)
plt.legend(fontsize=6)
plt.xlim(300, 370)
plt.ylim(0, 14)

plt.subplot(1,6,4)
plt.title("July 18 12Z Reno, NV Sounding",fontsize=8)
plt.plot(TheM_1812,HMk_1812,label = "Equivalent Potential Temperature", color="black")
plt.plot(ThM_1812,HMk_1812,label = "Potential Temperature", color="red")
plt.xlabel("Theta-e (K)",fontsize=8)
#plt.ylabel("Height AGL (km)",fontsize=8)
plt.legend(fontsize=6)
plt.xlim(300, 370)
plt.ylim(0, 14)

plt.subplot(1,6,5)
plt.title("July 19 00Z Reno, NV Sounding",fontsize=8)
plt.plot(TheM_1900,HMk_1900,label = "Equivalent Potential Temperature", color="black")
plt.plot(ThM_1900,HMk_1900,label = "Potential Temperature", color="red")
plt.xlabel("Theta-e (K)",fontsize=8)
#plt.ylabel("Height AGL (km)",fontsize=8)
plt.legend(fontsize=6)
plt.xlim(300, 370)
plt.ylim(0, 14)

plt.subplot(1,6,6)
plt.title("July 19 12Z Reno, NV Sounding",fontsize=8)
plt.plot(TheM_1912,HMk_1912,label = "Equivalent Potential Temperature", color="black")
plt.plot(ThM_1912,HMk_1912,label = "Potential Temperature", color="red")
plt.xlabel("Theta-e (K)",fontsize=8)
#plt.ylabel("Height AGL (km)",fontsize=8)
plt.legend(loc='upper left',fontsize=6)
plt.xlim(300, 370)
plt.ylim(0, 14)

#Save figure to directory
plt.savefig('Theta_Test.png')
plt.show()

#Start Finding CCL

esM_1700= [6.11 * 10. ** (7.5 * i / (237.3 + i)) for i in TM_1700] #environment saturation vapor pressure
eM_1700= [6.11 * 10. ** (7.5 * i /(237.3 + i)) for i in DM_1700] #actual vapor pressure
rhM_1700 = [j/k for j,k in zip(eM_1700,esM_1700)] #rh as the ratio of the actual to the saturation pressures
satmixM_1700= [621.97 * (k / (i - k)) for i, k in zip(PM_1700,esM_1700)] #environments saturation mixing ratio
wmixM_1700= [621.97 * (j / (i - j)) for i,j in zip(PM_1700,eM_1700)] #actual mixing ratio

esM_1712= [6.11 * 10. ** (7.5 * i / (237.3 + i)) for i in TM_1712] 
eM_1712= [6.11 * 10. ** (7.5 * i /(237.3 + i)) for i in DM_1712] 
rhM_1712 = [j/k for j,k in zip(eM_1712,esM_1712)] 
satmixM_1712= [621.97 * (k / (i - k)) for i, k in zip(PM_1712,esM_1712)] 
wmixM_1712= [621.97 * (j / (i - j)) for i,j in zip(PM_1712,eM_1712)]

esM_1800= [6.11 * 10. ** (7.5 * i / (237.3 + i)) for i in TM_1800]
eM_1800= [6.11 * 10. ** (7.5 * i /(237.3 + i)) for i in DM_1800]
rhM_1800 = [j /k for j,k in zip(eM_1800,esM_1800)]
satmixM_1800= [621.97 * (k / (i - k)) for i, k in zip(PM_1800,esM_1800)]
wmixM_1800= [621.97 * (j / (i - j)) for i,j in zip(PM_1800,eM_1800)]

esM_1812= [6.11 * 10. ** (7.5 * i / (237.3 + i)) for i in TM_1812]
eM_1812= [6.11 * 10. ** (7.5 * i /(237.3 + i)) for i in DM_1812]
rhM_1812 = [j /k for j,k in zip(eM_1812,esM_1812)]
satmixM_1812= [621.97 * (k / (i - k)) for i, k in zip(PM_1812,esM_1812)]
wmixM_1812= [621.97 * (j / (i - j)) for i,j in zip(PM_1812,eM_1812)]

esM_1900= [6.11 * 10. ** (7.5 * i / (237.3 + i)) for i in TM_1900]
eM_1900= [6.11 * 10. ** (7.5 * i /(237.3 + i)) for i in DM_1900]
rhM_1900 = [j /k for j,k in zip(eM_1900,esM_1900)]
satmixM_1900= [621.97 * (k / (i - k)) for i, k in zip(PM_1900,esM_1900)]
wmixM_1900= [621.97 * (j / (i - j)) for i,j in zip(PM_1900,eM_1900)]

esM_1912= [6.11 * 10. ** (7.5 * i / (237.3 + i)) for i in TM_1912]
eM_1912= [6.11 * 10. ** (7.5 * i /(237.3 + i)) for i in DM_1912]
rhM_1912 = [j /k for j,k in zip(eM_1912,esM_1912)]
satmixM_1912= [621.97 * (k / (i - k)) for i, k in zip(PM_1912,esM_1912)]
wmixM_1912= [621.97 * (j / (i - j)) for i,j in zip(PM_1912,eM_1912)]

#These plots are used to verify that the calculated mixing ratios and relative humidites match closely to the CSV values

plt.figure(figsize=(15, 6))
plt.subplot(1,2,1)
plt.scatter(wmixM_1700,MM_1700)
plt.xlabel("Computed Mixing Ratio",fontsize=14)
plt.ylabel("Reported Mixing Ratio",fontsize=14)
plt.grid()

#I accidentally made the relative humidity variables the same, except lowercase rh is calculated from the lines above
    #and RH is pulled from the CSV

plt.subplot(1,2,2)
plt.scatter(rhM_1700,RHM_1700)
plt.xlabel("Computed Mixing Ratio",fontsize=14)
plt.ylabel("Reported Mixing Ratio",fontsize=14)
plt.grid()
plt.savefig('1-1_Check.png')
plt.show()


#Declare surface pressure as the first numerical value in the PRES column in the CSV. Depending on your rows, this number may not be 0
SfcPM_1700=PM_1700[0]
SfcPM_1712=PM_1712[0]
SfcPM_1800=PM_1800[0]
SfcPM_1812=PM_1812[0]
SfcPM_1900=PM_1900[0]
SfcPM_1912=PM_1912[0]

#These variables determine how far to move up in the atmosphere. "Move up until you reach a pressure this much lower than the surface"
P_inc50=50
P_inc100=100
P_inc200=200

#Find the pressure value this much lower than the surface pressure. You may not need all three (50hPa, 100hPa, 200hPa),
    #but unless your near-surface atmosphere is well mixed, Neil and I determined it would be best to create three "scenarios"
PM_1700_top50=SfcPM_1700-P_inc50
PM_1712_top50=SfcPM_1712-P_inc50
PM_1800_top50=SfcPM_1800-P_inc50
PM_1812_top50=SfcPM_1812-P_inc50
PM_1900_top50=SfcPM_1900-P_inc50
PM_1912_top50=SfcPM_1912-P_inc50

PM_1700_top100=SfcPM_1700-P_inc100
PM_1712_top100=SfcPM_1712-P_inc100
PM_1800_top100=SfcPM_1800-P_inc100
PM_1812_top100=SfcPM_1812-P_inc100
PM_1900_top100=SfcPM_1900-P_inc100
PM_1912_top100=SfcPM_1912-P_inc100

PM_1700_top200=SfcPM_1700-P_inc200
PM_1712_top200=SfcPM_1712-P_inc200
PM_1800_top200=SfcPM_1800-P_inc200
PM_1812_top200=SfcPM_1812-P_inc200
PM_1900_top200=SfcPM_1900-P_inc200
PM_1912_top200=SfcPM_1912-P_inc200

#You want to use the pressure level closest to the variable found before (e.g. the PM_1712_top50 pressure level, which is the surface pressure
    #at 1712 over Reno minus 50hPa). This may either be a higher or lower pressure than what you are looking for, but all that matters is
    #that you use the closer one to be as accurate as possible. In order to do this, take all values in your pressure column (e.g. PM_1712[i])
    #And subtract the pressure you want to be close to (e.g. PM_1712_top50). This code will then determine which pressure level is the closest
MinM_1700_50 = min(range(len(PM_1700)), key=lambda i: abs(PM_1700[i]-PM_1700_top50))
MinM_1712_50 = min(range(len(PM_1712)), key=lambda i: abs(PM_1712[i]-PM_1712_top50))
MinM_1800_50 = min(range(len(PM_1800)), key=lambda i: abs(PM_1800[i]-PM_1800_top50))
MinM_1812_50 = min(range(len(PM_1812)), key=lambda i: abs(PM_1812[i]-PM_1812_top50))
MinM_1900_50 = min(range(len(PM_1900)), key=lambda i: abs(PM_1900[i]-PM_1900_top50))
MinM_1912_50 = min(range(len(PM_1912)), key=lambda i: abs(PM_1912[i]-PM_1912_top50))

MinM_1700_100 = min(range(len(PM_1700)), key=lambda i: abs(PM_1700[i]-PM_1700_top100))
MinM_1712_100 = min(range(len(PM_1712)), key=lambda i: abs(PM_1712[i]-PM_1712_top100))
MinM_1800_100 = min(range(len(PM_1800)), key=lambda i: abs(PM_1800[i]-PM_1800_top100))
MinM_1812_100 = min(range(len(PM_1812)), key=lambda i: abs(PM_1812[i]-PM_1812_top100))
MinM_1900_100 = min(range(len(PM_1900)), key=lambda i: abs(PM_1900[i]-PM_1900_top100))
MinM_1912_100 = min(range(len(PM_1912)), key=lambda i: abs(PM_1912[i]-PM_1912_top100))

MinM_1700_200 = min(range(len(PM_1700)), key=lambda i: abs(PM_1700[i]-PM_1700_top200))
MinM_1712_200 = min(range(len(PM_1712)), key=lambda i: abs(PM_1712[i]-PM_1712_top200))
MinM_1800_200 = min(range(len(PM_1800)), key=lambda i: abs(PM_1800[i]-PM_1800_top200))
MinM_1812_200 = min(range(len(PM_1812)), key=lambda i: abs(PM_1812[i]-PM_1812_top200))
MinM_1900_200 = min(range(len(PM_1900)), key=lambda i: abs(PM_1900[i]-PM_1900_top200))
MinM_1912_200 = min(range(len(PM_1912)), key=lambda i: abs(PM_1912[i]-PM_1912_top200))

#Find the average mixing ratio between the surface pressure and the pressure level found from the previous lines of code
    #***Make sure Python is reading the correct row here. I had to index one row lower than expect (hence the +1 in the code) which almost
    #ruined my calculation
MixLayerM_1700_50 = sum(MM_1700[0:(MinM_1700_50+1)])/(MinM_1700_50+1)
MixLayerM_1712_50 = sum(MM_1712[0:(MinM_1712_50+1)])/(MinM_1712_50+1)
MixLayerM_1800_50 = sum(MM_1800[0:(MinM_1800_50+1)])/(MinM_1800_50+1)
MixLayerM_1812_50 = sum(MM_1812[0:(MinM_1812_50+1)])/(MinM_1812_50+1)
MixLayerM_1900_50 = sum(MM_1900[0:(MinM_1900_50+1)])/(MinM_1900_50+1)
MixLayerM_1912_50 = sum(MM_1912[0:(MinM_1912_50+1)])/(MinM_1912_50+1)

MixLayerM_1700_100 = sum(MM_1700[0:(MinM_1700_100+1)])/(MinM_1700_100+1)
MixLayerM_1712_100 = sum(MM_1712[0:(MinM_1712_100+1)])/(MinM_1712_100+1)
MixLayerM_1800_100 = sum(MM_1800[0:(MinM_1800_100+1)])/(MinM_1800_100+1)
MixLayerM_1812_100 = sum(MM_1812[0:(MinM_1812_100+1)])/(MinM_1812_100+1)
MixLayerM_1900_100 = sum(MM_1900[0:(MinM_1900_100+1)])/(MinM_1900_100+1)
MixLayerM_1912_100 = sum(MM_1912[0:(MinM_1912_100+1)])/(MinM_1912_100+1)

MixLayerM_1700_200 = sum(MM_1700[0:(MinM_1700_200+1)])/(MinM_1700_200+1)
MixLayerM_1712_200 = sum(MM_1712[0:(MinM_1712_200+1)])/(MinM_1712_200+1)
MixLayerM_1800_200 = sum(MM_1800[0:(MinM_1800_200+1)])/(MinM_1800_200+1)
MixLayerM_1812_200 = sum(MM_1812[0:(MinM_1812_200+1)])/(MinM_1812_200+1)
MixLayerM_1900_200 = sum(MM_1900[0:(MinM_1900_200+1)])/(MinM_1900_200+1)
MixLayerM_1912_200 = sum(MM_1912[0:(MinM_1912_200+1)])/(MinM_1912_200+1)

#Check to make sure values seem correct
#print("July 17 00Z Reno, NV Sounding")
print("Mean Mixing Ratio: Lowest 50 hPa")
print("Reno:",MixLayerM_1700_50,MixLayerM_1712_50)
print("")
print("Mean Mixing Ratio: Lowest 100 hPa")
print("Reno:",MixLayerM_1700_100,MixLayerM_1712_100)
print("")
print("Mean Mixing Ratio: Lowest 200 hPa")
print("Reno:",MixLayerM_1700_200,MixLayerM_1712_200)
"""
#print("July 17 12Z Reno, NV Sounding")
print("Mean Mixing Ratio: Lowest 50 hPa")
print("Reno:",MixLayerM_1700_50,MixLayerM_1712_50,MixLayerM_1800_50,MixLayerM_1812_50,MixLayerM_1900_50,MixLayerM_1912_50)
print("")
print("Mean Mixing Ratio: Lowest 100 hPa")
print("Reno:",MixLayerM_1700_100,MixLayerM_1712_100,MixLayerM_1800_100,MixLayerM_1812_100,MixLayerM_1900_100,MixLayerM_1912_100)
print("")
print("Mean Mixing Ratio: Lowest 200 hPa")
print("Reno:",MixLayerM_1700_200,MixLayerM_1712_200,MixLayerM_1800_200,MixLayerM_1812_200,MixLayerM_1900_200,MixLayerM_1912_200)
"""
import scipy.interpolate

#Due to data spacing not always being consistent, we want to interpolate to add more data points

#Python may give you errors regarding the "shape" of variables. If it does, use this code.
    #If not, I would still create a list of only the first 50 variables or so in a sounding. Otherwise, when you try to determine the CCL
    #you may get a CCL significantly higher than where it should be (This is achieved by doing the [0:50] portion of the following code
SatIntM_1700 = np.asarray(satmixM_1700[0:50]).squeeze()
HeightIntM_1700 = np.asarray(HM_1700[0:50]).squeeze()
SatIntM_1712 = np.asarray(satmixM_1712[0:50]).squeeze()
HeightIntM_1712 = np.asarray(HM_1712[0:50]).squeeze()
SatIntM_1800 = np.asarray(satmixM_1800[0:50]).squeeze()
HeightIntM_1800 = np.asarray(HM_1800[0:50]).squeeze()
SatIntM_1812 = np.asarray(satmixM_1812[0:50]).squeeze()
HeightIntM_1812 = np.asarray(HM_1812[0:50]).squeeze()
SatIntM_1900 = np.asarray(satmixM_1900[0:50]).squeeze()
HeightIntM_1900 = np.asarray(HM_1900[0:50]).squeeze()
SatIntM_1912 = np.asarray(satmixM_1912[0:50]).squeeze()
HeightIntM_1912 = np.asarray(HM_1912[0:50]).squeeze()

#This creates the interpolated datapoints. Python will probably give you an error if you do not do the fill_value="extrapolate"
IntM_1700 = scipy.interpolate.interp1d(SatIntM_1700, HeightIntM_1700,fill_value="extrapolate")
IntM_1712 = scipy.interpolate.interp1d(SatIntM_1712, HeightIntM_1712,fill_value="extrapolate")
IntM_1800 = scipy.interpolate.interp1d(SatIntM_1800, HeightIntM_1800,fill_value="extrapolate")
IntM_1812 = scipy.interpolate.interp1d(SatIntM_1812, HeightIntM_1812,fill_value="extrapolate")
IntM_1900 = scipy.interpolate.interp1d(SatIntM_1900, HeightIntM_1900,fill_value="extrapolate")
IntM_1912 = scipy.interpolate.interp1d(SatIntM_1912, HeightIntM_1912,fill_value="extrapolate")

#Determine the CCL based off the mean mixing ratio (e.g. MixLayerM_1712_50)
CCLM_1700_50 = IntM_1700(MixLayerM_1700_50)
CCLM_1700_100 = IntM_1700(MixLayerM_1700_100)
CCLM_1700_200 = IntM_1700(MixLayerM_1700_200)
CCLM_1712_50 = IntM_1712(MixLayerM_1712_50)
CCLM_1712_100 = IntM_1712(MixLayerM_1712_100)
CCLM_1712_200 = IntM_1712(MixLayerM_1712_200)
CCLM_1800_50 = IntM_1800(MixLayerM_1800_50)
CCLM_1800_100 = IntM_1800(MixLayerM_1800_100)
CCLM_1800_200 = IntM_1800(MixLayerM_1800_200)
CCLM_1812_50 = IntM_1812(MixLayerM_1812_50)
CCLM_1812_100 = IntM_1812(MixLayerM_1812_100)
CCLM_1812_200 = IntM_1812(MixLayerM_1812_200)
CCLM_1900_50 = IntM_1900(MixLayerM_1900_50)
CCLM_1900_100 = IntM_1900(MixLayerM_1900_100)
CCLM_1900_200 = IntM_1900(MixLayerM_1900_200)
CCLM_1912_50 = IntM_1912(MixLayerM_1912_50)
CCLM_1912_100 = IntM_1912(MixLayerM_1912_100)
CCLM_1912_200 = IntM_1800(MixLayerM_1912_200)

plt.figure(figsize=(15, 20))
plt.subplot(2,1,1)
plt.title("July 17 00Z Reno, NV Sounding",fontsize=8)
plt.plot(wmixM_1700,HM_1700,'-o',color="blue",label = "Mixing Ratio")
plt.plot(satmixM_1700,HM_1700,'-o',color="red",label = "Saturation Mixing Ratio")
plt.plot([MixLayerM_1700_50, MixLayerM_1700_50],[0,15000],color="blue", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 50m")
plt.plot([MixLayerM_1700_100, MixLayerM_1700_100],[0,15000],color="red", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 100m")
plt.plot([MixLayerM_1700_200, MixLayerM_1700_200],[0,15000],color="limegreen", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 200m")
plt.plot([0,18],[CCLM_1700_50,CCLM_1700_50],color="blue", linestyle = 'dashdot',label = "CCL Height Using Mean 50m Mixing Ratio")
plt.plot([0,18],[CCLM_1700_100,CCLM_1700_100],color="red", linestyle = 'dashdot',label = "CCL Height Using Mean 100m Mixing Ratio")
plt.plot([0,18],[CCLM_1700_200,CCLM_1700_200],color="limegreen", linestyle = 'dashdot',label = "CCL Height Using Mean 200m Mixing Ratio")
plt.xlabel("Mixing Ratio (g/kg)",fontsize=14)
plt.ylabel("Altitude (m)",fontsize=14)
plt.legend(fontsize=7)
plt.xlim(0, 18)
plt.ylim(0, 20000)
plt.grid()

"""
plt.subplot(6,1,2)
plt.title("July 17 12Z Reno, NV Sounding",fontsize=8)
plt.plot(wmixM_1712,HM_1712,'-o',color="blue",label = "Mixing Ratio")
plt.plot(satmixM_1712,HM_1712,'-o',color="red",label = "Saturation Mixing Ratio")
plt.plot([MixLayerM_1712_50, MixLayerM_1712_50],[0,15000],color="blue", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 50m")
plt.plot([MixLayerM_1712_100, MixLayerM_1712_100],[0,15000],color="red", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 100m")
plt.plot([MixLayerM_1712_200, MixLayerM_1712_200],[0,15000],color="limegreen", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 200m")
plt.plot([0,18],[CCLM_1712_50,CCLM_1712_50],color="blue", linestyle = 'dashdot',label = "CCL Height Using Mean 50m Mixing Ratio")
plt.plot([0,18],[CCLM_1712_100,CCLM_1712_100],color="red", linestyle = 'dashdot',label = "CCL Height Using Mean 100m Mixing Ratio")
plt.plot([0,18],[CCLM_1712_200,CCLM_1712_200],color="limegreen", linestyle = 'dashdot',label = "CCL Height Using Mean 200m Mixing Ratio")
plt.xlabel("Mixing Ratio (g/kg)",fontsize=14)
plt.ylabel("Altitude (m)",fontsize=14)
plt.legend(fontsize=14)
plt.xlim(0, 20)
plt.ylim(0, 20000)
plt.grid()


plt.subplot(2,1,3)
plt.title("July 18 00Z Reno, NV Sounding",fontsize=8)
plt.plot(wmixM_1800,HM_1800,'-o',color="blue",label = "Mixing Ratio")
plt.plot(satmixM_1800,HM_1800,'-o',color="red",label = "Saturation Mixing Ratio")
plt.plot([MixLayerM_1800_50, MixLayerM_1800_50],[0,15000],color="blue", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 50m")
plt.plot([MixLayerM_1800_100, MixLayerM_1800_100],[0,15000],color="red", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 100m")
plt.plot([MixLayerM_1800_200, MixLayerM_1800_200],[0,15000],color="limegreen", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 200m")
plt.plot([0,18],[CCLM_1800_50,CCLM_1800_50],color="blue", linestyle = 'dashdot',label = "CCL Height Using Mean 50m Mixing Ratio")
plt.plot([0,18],[CCLM_1800_100,CCLM_1800_100],color="red", linestyle = 'dashdot',label = "CCL Height Using Mean 100m Mixing Ratio")
plt.plot([0,18],[CCLM_1800_200,CCLM_1800_200],color="limegreen", linestyle = 'dashdot',label = "CCL Height Using Mean 200m Mixing Ratio")
plt.xlabel("Mixing Ratio (g/kg)",fontsize=14)
plt.ylabel("Altitude (m)",fontsize=14)
plt.legend(fontsize=14)
plt.xlim(0, 18)
plt.ylim(0, 15000)
plt.grid()

plt.subplot(2,1,4)
plt.title("July 18 12Z Reno, NV Sounding",fontsize=8)
plt.plot(wmixM_1812,HM_1812,'-o',color="blue",label = "Mixing Ratio")
plt.plot(satmixM_1812,HM_1812,'-o',color="red",label = "Saturation Mixing Ratio")
plt.plot([MixLayerM_1812_50, MixLayerM_1812_50],[0,15000],color="blue", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 50m")
plt.plot([MixLayerM_1812_100, MixLayerM_1812_100],[0,15000],color="red", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 100m")
plt.plot([MixLayerM_1812_200, MixLayerM_1812_200],[0,15000],color="limegreen", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 200m")
plt.plot([0,18],[CCLM_1812_50,CCLM_1812_50],color="blue", linestyle = 'dashdot',label = "CCL Height Using Mean 50m Mixing Ratio")
plt.plot([0,18],[CCLM_1812_100,CCLM_1812_100],color="red", linestyle = 'dashdot',label = "CCL Height Using Mean 100m Mixing Ratio")
plt.plot([0,18],[CCLM_1812_200,CCLM_1812_200],color="limegreen", linestyle = 'dashdot',label = "CCL Height Using Mean 200m Mixing Ratio")
plt.xlabel("Mixing Ratio (g/kg)",fontsize=14)
plt.ylabel("Altitude (m)",fontsize=14)
plt.legend(fontsize=14)
plt.xlim(0, 18)
plt.ylim(0, 15000)
plt.grid()

plt.subplot(2,1,5)
plt.title("July 19 00Z Reno, NV Sounding",fontsize=8)
plt.plot(wmixM_1900,HM_1900,'-o',color="blue",label = "Mixing Ratio")
plt.plot(satmixM_1900,HM_1900,'-o',color="red",label = "Saturation Mixing Ratio")
plt.plot([MixLayerM_1900_50, MixLayerM_1900_50],[0,15000],color="blue", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 50m")
plt.plot([MixLayerM_1900_100, MixLayerM_1900_100],[0,15000],color="red", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 100m")
plt.plot([MixLayerM_1900_200, MixLayerM_1900_200],[0,15000],color="limegreen", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 200m")
plt.plot([0,18],[CCLM_1900_50,CCLM_1900_50],color="blue", linestyle = 'dashdot',label = "CCL Height Using Mean 50m Mixing Ratio")
plt.plot([0,18],[CCLM_1900_100,CCLM_1900_100],color="red", linestyle = 'dashdot',label = "CCL Height Using Mean 100m Mixing Ratio")
plt.plot([0,18],[CCLM_1900_200,CCLM_1900_200],color="limegreen", linestyle = 'dashdot',label = "CCL Height Using Mean 200m Mixing Ratio")
plt.xlabel("Mixing Ratio (g/kg)",fontsize=14)
plt.ylabel("Altitude (m)",fontsize=14)
plt.legend(fontsize=14)
plt.xlim(0, 18)
plt.ylim(0, 15000)
plt.grid()

plt.subplot(2,1,6)
plt.title("July 19 12Z Reno, NV Sounding",fontsize=8)
plt.plot(wmixM_1912,HM_1912,'-o',color="blue",label = "Mixing Ratio")
plt.plot(satmixM_1912,HM_1912,'-o',color="red",label = "Saturation Mixing Ratio")
plt.plot([MixLayerM_1912_50, MixLayerM_1912_50],[0,15000],color="blue", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 50m")
plt.plot([MixLayerM_1912_100, MixLayerM_1912_100],[0,15000],color="red", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 100m")
plt.plot([MixLayerM_1912_200, MixLayerM_1912_200],[0,15000],color="limegreen", linestyle = 'dotted',label = "Mean Mixing Ratio in Lowest 200m")
plt.plot([0,18],[CCLM_1912_50,CCLM_1912_50],color="blue", linestyle = 'dashdot',label = "CCL Height Using Mean 50m Mixing Ratio")
plt.plot([0,18],[CCLM_1912_100,CCLM_1912_100],color="red", linestyle = 'dashdot',label = "CCL Height Using Mean 100m Mixing Ratio")
plt.plot([0,18],[CCLM_1912_200,CCLM_1912_200],color="limegreen", linestyle = 'dashdot',label = "CCL Height Using Mean 200m Mixing Ratio")
plt.xlabel("Mixing Ratio (g/kg)",fontsize=14)
plt.ylabel("Altitude (m)",fontsize=14)
plt.legend(fontsize=14)
plt.xlim(0, 18)
plt.ylim(0, 15000)
plt.grid()
"""
plt.savefig('Theta_Test3.png')
plt.show()
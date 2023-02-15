#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:19:00 2019

@author: balintradics
"""

import numpy as np
import matplotlib.pyplot as plt

# Reference: PRL 118, 151801 (2017)
# Integrated Flux: 7.48x10^20 POT (neutrino mode)
# nue events: 32, numu events: 135
# Integrated Flux: 7.47x10^20 POT (antineutrino mode)
# nue: events: 4, numu events: 66


# 2021
# Integrated Flux: 1.97x10^21 POT (neutrino mode)
# nue events: 108, numu events: 452
# Integrated Flux: 1.63x10^21 POT (antineutrino mode)
# nue: events: 16, numu events: 137




flux_norm = 5
cross_sec_unit = 1.0e-38

# Full flux[]
# Flux[] model SK, nu_mu, units: neutrinos/(cm2 * 50 MeV * 10e{21} POT)
# T2K Run 1-10b
npoints = 37
Flux = np.full(npoints, 0.0, dtype = np.float32)
E = np.full(npoints, 0.0, dtype=np.float32)
Flux[0]= 0;E[0] = 0.0;
Flux[1]=12752.6;E[1]=0.025
Flux[2]=54387.1;E[2]=0.075
Flux[3]=111899;E[3]=0.125
Flux[4]=177014;E[4]=0.175
Flux[5]=271326;E[5]=0.225
Flux[6]=383862;E[6]=0.275
Flux[7]=496838;E[7]=0.325
Flux[8]=608187;E[8]=0.375
Flux[9]=727225;E[9]=0.425
Flux[10]=897688;E[10]=0.475
Flux[11]=1.12089e+06;E[11]=0.525
Flux[12]=1.24718e+06;E[12]=0.575
Flux[13]=1.24403e+06;E[13]=0.625
Flux[14]=1.16337e+06;E[14]=0.675
Flux[15]=918090;E[15]=0.725
Flux[16]=639182;E[16]=0.775
Flux[17]=422121;E[17]=0.825
Flux[18]=273041;E[18]=0.875
Flux[19]=191366;E[19]=0.925
Flux[20]=141740;E[20]=0.975
Flux[21]=113066;E[21]=1.025
Flux[22]=94186.7;E[22]=1.075
Flux[23]=79511.8;E[23]=1.125
Flux[24]=68091.8;E[24]=1.175
Flux[25]=59903.3;E[25]=1.225
Flux[26]=52537.5;E[26]=1.275
Flux[27]=47631.3;E[27]=1.325
Flux[28]=43095.2;E[28]=1.375
Flux[29]=37878.2;E[29]=1.425
Flux[30]=35544.5;E[30]=1.475
Flux[31]=32223.8;E[31]=1.525
Flux[32]=29583.5;E[32]=1.575
Flux[33]=27201.9;E[33]=1.625
Flux[34]=25170.9;E[34]=1.675
Flux[35]=23294.4;E[35]=1.725
Flux[36]=22417.8;E[36]=1.775
 
#plt.plot(E,Flux)
#plt.xlabel("E [GeV]")
#plt.ylabel("Flux [neutrinos / (cm^2 * 10^21 POT)]")
#plt.show()

#TotFlux  = 0
#for i in np.array(np.arange(0,npoints)):
#    TotFlux += Flux[i]
    
#print("Neutrino mode Integrated flux:", TotFlux)

# Flux[] model SK, anti_nu_mu, units: neutrinos/(cm2 * 50 MeV * 10e{21} POT)
# T2K Run 5c-9d
AFlux = np.full(npoints, 0.0, dtype = np.float32)
AFlux[0]= 0;E[0] = 0.0;
AFlux[1]=12229.3;E[1]=0.025
AFlux[2]=52539.4;E[2]=0.075
AFlux[3]=109784;E[3]=0.125
AFlux[4]=172567;E[4]=0.175
AFlux[5]=254375;E[5]=0.225
AFlux[6]=343177;E[6]=0.275
AFlux[7]=433332;E[7]=0.325
AFlux[8]=522769;E[8]=0.375
AFlux[9]=620423;E[9]=0.425
AFlux[10]=758567;E[10]=0.475
AFlux[11]=918026;E[11]=0.525
AFlux[12]=985176;E[12]=0.575
AFlux[13]=970425;E[13]=0.625
AFlux[14]=878959;E[14]=0.675
AFlux[15]=671361;E[15]=0.725
AFlux[16]=454990;E[16]=0.775
AFlux[17]=290868;E[17]=0.825
AFlux[18]=187794;E[18]=0.875
AFlux[19]=131352;E[19]=0.925
AFlux[20]=98734.3;E[20]=0.975
AFlux[21]=79415.4;E[21]=1.025
AFlux[22]=65922.7;E[22]=1.075
AFlux[23]=56228.2;E[23]=1.125
AFlux[24]=48183.2;E[24]=1.175
AFlux[25]=41975;E[25]=1.225
AFlux[26]=36955.7;E[26]=1.275
AFlux[27]=33034.3;E[27]=1.325
AFlux[28]=29051;E[28]=1.375
AFlux[29]=26270.8;E[29]=1.425
AFlux[30]=23486;E[30]=1.475
AFlux[31]=21623.9;E[31]=1.525
AFlux[32]=20235.3;E[32]=1.575
AFlux[33]=18133.7;E[33]=1.625
AFlux[34]=16628.3;E[34]=1.675
AFlux[35]=15124.4;E[35]=1.725
AFlux[36]=14268.8;E[36]=1.775

# Cross section
e = np.full(35, 0.0, dtype = np.float32)
xsec = np.full(35, 0.0, dtype = np.float32)
e[0] = 0.0500000 ; xsec[0] = 0.0043434 ;
e[1] = 0.1000000 ; xsec[1] = 0.0095185 ;
e[2] = 0.1500000 ; xsec[2] = 0.0600886 ;
e[3] = 0.2000000 ; xsec[3] = 0.1056801 ;
e[4] = 0.25 ; xsec[4] = 0.1695939 ;
e[5]= 0.3000000 ; xsec[5] = 0.2345959 ;
e[6] = 0.3499999 ; xsec[6] = 0.2947372 ;
e[7] = 0.4000000 ; xsec[7] = 0.3670271 ;
e[8] = 0.4499999 ; xsec[8] = 0.4433561 ;
e[9] = 0.5 ; xsec[9] = 0.5202292 ;
e[10]= 0.5500000 ; xsec[10] = 0.6077193 ;
e[11] = 0.6000000 ; xsec[11] = 0.6954122 ;
e[12] = 0.6499999 ; xsec[12] = 0.7762684 ;
e[13] = 0.6999999 ; xsec[13] = 0.8575258 ;
e[14] = 0.75 ; xsec[14] = 0.9326797 ;
e[15] = 0.8000000 ; xsec[15] = 1.0019815 ;
e[16] = 0.8500000 ; xsec[16] = 1.0672518 ;
e[17] = 0.8999999 ; xsec[17] = 1.1298935 ;
e[18] = 0.9499999 ; xsec[18] = 1.1924122 ;
e[19] = 1 ;       xsec[19] = 1.2539711 ;
e[20] = 1.0499999 ; xsec[20] = 1.3088034 ;
e[21] = 1.1000000 ; xsec[21] = 1.3625717 ;
e[22] = 1.1499999 ; xsec[22] = 1.4158695 ;
e[23] = 1.2000000 ; xsec[23] = 1.4667800 ;
e[24] = 1.25 ; xsec[24] = 1.5190051 ;
e[25] = 1.2999999 ; xsec[25] = 1.5674283 ;
e[26] = 1.3500000 ; xsec[26] = 1.6186068 ;
e[27] = 1.3999999 ; xsec[27] = 1.6680007 ;
e[28] = 1.4500000 ; xsec[28] = 1.7168169 ;
e[29] = 1.5 ; xsec[29] = 1.7655986 ;
e[30] = 1.5499999 ; xsec[30] = 1.8091367 ;
e[31] = 1.6000000 ; xsec[31] = 1.8526686 ;
e[32] = 1.6499999 ; xsec[32] = 1.8976965 ;
e[33] = 1.7000000 ; xsec[33] = 1.9427199 ;
e[34] = 1.75 ; xsec[34] = 1.9884147 ;
xsec = cross_sec_unit*xsec

# Cross section for antinumu->H2O 
axsec = np.full(35, 0.0, dtype = np.float32)
axsec[0] = 0.0020280 ;
axsec[1] = 0.0044747 ;
axsec[2] = 0.0238378 ;
axsec[3] = 0.0401729 ;
axsec[4] = 0.0560505 ;
axsec[5] = 0.0718081 ;
axsec[6] = 0.0870330 ;
axsec[7] = 0.1052819 ;
axsec[8] = 0.1251550 ;
axsec[9] = 0.1451578 ;
axsec[10] = 0.1678155 ;
axsec[11] = 0.1905608 ;
axsec[12] = 0.2144551 ;
axsec[13] = 0.2394637 ;
axsec[14] = 0.2645104 ;
axsec[15] = 0.2910050 ;
axsec[16] = 0.3174965 ;
axsec[17] = 0.3448029 ;
axsec[18] = 0.3727434 ;
axsec[19] = 0.4005067 ;
axsec[20] = 0.4285244 ;
axsec[21] = 0.4563468 ;
axsec[22] = 0.4843834 ;
axsec[23] = 0.5124145 ;
axsec[24] = 0.5400463 ;
axsec[25] = 0.5676460 ;
axsec[26] = 0.5953997 ;
axsec[27] = 0.6228603 ;
axsec[28] = 0.6505540 ;
axsec[29] = 0.6781141 ;
axsec[30] = 0.7038010 ;
axsec[31] = 0.7293814 ;
axsec[32] = 0.7563094 ;
axsec[33] = 0.7831416 ;
axsec[34] = 0.8089601 ;
axsec = cross_sec_unit*axsec


#interpolate
#plt.plot(e,xsec)
#plt.xlabel("E [GeV]")
#plt.ylabel("Xsec [cm^-2]")
#plt.show()

#TotAFlux  = 0
#for i in np.array(np.arange(0,npoints)):
#    TotAFlux += AFlux[i]
    
#print("Anti-Neutrino mode Integrated flux:", TotAFlux)



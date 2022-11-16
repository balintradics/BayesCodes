#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


class PMNS:
    """Class to calculate standard neutrino oscillation probabilities.
       Uses mpmath arbitrary precision floating point library
       
    Attributes:
            theta_12: PMNS matrix parameter \theta_{12}
            theta_23: PMNS matrix parameter \theta_{23}
            theta_13: PMNS matrix parameter \theta_{13}
            delta: PMNS matrix parameter delta_CP
    """
    def __init__(self, theta_12 = 31.46, theta_23 = 38.53, theta_13 = 8.38, delta = 245.0):
        self.name = "PMNS"
    
        self.one_mass_scale = False
        self.massord = 1    
        self.theta_12 = theta_12*np.pi/180.
        self.theta_23 = theta_23*np.pi/180.
        self.theta_13 = theta_13*np.pi/180.
        self.delta = delta*np.pi/180.
    
        if self.one_mass_scale == True:
            self.theta_12 = 0.0
            self.theta_13 = 0.0
            
        self.setMassOrderModel(self.massord, self.one_mass_scale)
 
    def setDeltaCP(self, delta_):
        self.delta = delta_
        self.cexpdeltac = np.exp(0-self.delta*1j)
        self.cexpdelta = np.exp(0+ self.delta*1j)

   
    def setMassOrderModel(self, massord_, one_mass_scale_ = False, scale_ = 0.0):
        self.massord = massord_
        # [eV^{2}]
        self.delta_m21 = 7.37e-05
        self.delta_m_sqr = 0.0
        # normal hierarchy
        if self.massord == 1:
            self.delta_m_sqr = 2.5e-03
            self.delta_m31 = self.delta_m_sqr + 0.5*self.delta_m21
            self.delta_m12 = -self.delta_m21
            self.delta_m13 = -self.delta_m31
            self.delta_m32 = self.delta_m31 - self.delta_m21
            if scale_ == 0.0:
                self.delta_m32 = self.delta_m31 - self.delta_m21
            else:
                self.delta_m32 = scale_*(self.delta_m31 - self.delta_m21)
                self.delta_m31 = scale_*self.delta_m31
                self.delta_m21 = scale_*self.delta_m21
                self.delta_m12 = scale_*self.delta_m12
                self.delta_m13 = scale_*self.delta_m13
                #print("Using mass scaling: ", scale_)
            self.delta_m23 = -self.delta_m32
        # inverted hierarchy  
        if self.massord == -1:
            self.delta_m_sqr = -2.46e-03
            self.delta_m32 = self.delta_m_sqr - 0.5*self.delta_m21
            self.delta_m12 = -self.delta_m21
            self.delta_m31 = self.delta_m32 + self.delta_m21
            self.delta_m13 = -self.delta_m31
            self.delta_m23 = -self.delta_m32       

        self.one_mass_scale = one_mass_scale_
        if self.one_mass_scale == True:
            self.theta_12 = 0.0
            self.theta_13 = 0.0
            
            # [eV^{2}]
            self.delta_m12 = 0.
            self.delta_m21 = 0.
            self.delta_m13 = 0.
            self.delta_m31 = 0.
            self.delta_m32 = 0.
            self.delta_m23 = 0.
    
    
            self.delta_m_sqr = 0.
            # normal hierarchy
            self.delta_m_sqr = 2.5e-03
            self.delta_m31 = self.delta_m_sqr 
            self.delta_m12 = -self.delta_m21
            self.delta_m13 = -self.delta_m31
            self.delta_m32 = self.delta_m31
            self.delta_m23 = -self.delta_m32
        
    
        
        
        self.delta_m = np.matrix([ [0.0,
                                    self.delta_m12,
                                    self.delta_m13],
        
                                [self.delta_m21,
                                 0.0,
                                 self.delta_m23],
                               
                                [self.delta_m31,
                                 self.delta_m32,
                                 0.0]
                                       ])
    
    # Note that here we need to propagate the
    # change into ALL relevant mass parameters!
    def changeNominalM32(self, factor):
        self.delta_m21 = self.delta_m21*factor
	#print("m32 change factor:", factor)
    
    def calcMassMatrix(self):
        self.delta_m = np.matrix([ [0.0,
                                    self.delta_m12,
                                    self.delta_m13],
        
                                [self.delta_m21,
                                 0.0,
                                 self.delta_m23],
                               
                                [self.delta_m31,
                                 self.delta_m32,
                                 0.0]
                                       ])
        
    def calcPMNS(self):
    
        # Ue1, Ue2, Ue3
        # Umu1, Umu2, Umu3
        # Utau1, Utau2, Utau3
        self.Ue1 = (np.cos(self.theta_12)*np.cos(self.theta_13)+0*1j)
        self.Ue2 = (np.sin(self.theta_12)*np.cos(self.theta_13)+0*1j)
        self.Ue3 = (np.sin(self.theta_13))*self.cexpdeltac

        self.Umu1 = -np.sin(self.theta_12)*np.cos(self.theta_23) - np.cos(self.theta_12)*np.sin(self.theta_23)*np.sin(self.theta_13)*self.cexpdelta
        self.Umu2 = np.cos(self.theta_12)*np.cos(self.theta_23) - np.sin(self.theta_12)*np.sin(self.theta_23)*np.sin(self.theta_13)*self.cexpdelta
        self.Umu3 = (np.sin(self.theta_23)*np.cos(self.theta_13)+0*1j)
    
        self.Utau1 = np.sin(self.theta_12)*np.sin(self.theta_23) - np.cos(self.theta_12)*np.cos(self.theta_23)*np.sin(self.theta_13)*self.cexpdelta
        self.Utau2 = -np.cos(self.theta_12)*np.sin(self.theta_23) - np.sin(self.theta_12)*np.cos(self.theta_23)*np.sin(self.theta_13)*self.cexpdelta
        self.Utau3 = (np.cos(self.theta_23)*np.cos(self.theta_13)+0*1j)
    
        self.pmns = np.matrix([ [self.Ue1, 
                                 self.Ue2, 
                                 self.Ue3],
    
                           [self.Umu1, 
                            self.Umu2, 
                            self.Umu3],
     
                            [self.Utau1, 
                             self.Utau2, 
                             self.Utau3] ])
        
        
    def printPMNS(self):
        print(self.pmns)
    
    
    def calcOsc_L_o_E(self,alpha, beta, L_o_E):
        myfactor = 2.53*L_o_E
        mysum = 0+0*1j
    
        for i in range(0, 3):
            myksum = 0+0*1j

            for k in range(0, 3):
                myvalue = 0+0*1j
                myvalue = np.conjugate(self.pmns.__getitem__((alpha,i)))*self.pmns.__getitem__((beta,i))*self.pmns.__getitem__((alpha,k))*np.conjugate(self.pmns.__getitem__((beta,k))) \
                * (np.cos(self.delta_m.__getitem__((i,k))*myfactor)+ (-np.sin(self.delta_m.__getitem__((i,k))*myfactor))*1j)
                myksum += myvalue
            mysum += myksum
        ret_value = mysum.real
        return ret_value


   


    def calcOsc_E(self,alpha, beta, L, E):
        L_o_E = L/E
        return self.calcOsc_L_o_E(alpha, beta, L_o_E)
    
    def calcOsc_L_o_E_conj(self,alpha, beta, L_o_E):
        myfactor = 2.53*L_o_E
        mysum = 0+0*1j
    
        for i in range(0, 3):
            myksum = 0+0*1j

            for k in range(0, 3):
                myvalue = 0+0*1j
                myvalue = self.pmns.__getitem__((alpha,i))*np.conjugate(self.pmns.__getitem__((beta,i)))*np.conjugate(self.pmns.__getitem__((alpha,k)))*self.pmns.__getitem__((beta,k)) \
                * (np.cos(self.delta_m.__getitem__((i,k))*myfactor)+(-np.sin(self.delta_m.__getitem__((i,k))*myfactor))*1j)
                myksum += myvalue
            mysum += myksum
        ret_value = mysum.real
        return ret_value
    
    
    def calcOsc_E_conj(self,alpha, beta, L, E):
        #delta = 1.35*np.pi
        L_o_E = L/E
        return self.calcOsc_L_o_E_conj(alpha, beta, L_o_E)

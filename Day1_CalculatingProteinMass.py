# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 22:33:12 2022

@author: Christopher
"""
#https://rosalind.info/problems/prtm/
#Input: SKADYEK
#Output : 821.392

#Monoisotopic mass table
MonoMass = {
    "A" : 71.03711,
    "C" : 103.00919,
    "D" : 115.02694,
    "E" : 129.04259,
    "F" : 147.06841,
    "G" : 57.02146,
    "H" : 137.05891,
    "I" : 113.08406,
    "K" : 128.09496,
    "L" : 113.08406,
    "M" : 131.04049,
    "N" : 114.04293,
    "P" : 97.05276,
    "Q" : 128.05858,
    "R" : 156.10111,
    "S" : 87.03203,
    "T" : 101.04768,
    "V" : 99.06841,
    "W" : 186.07931,
    "Y" : 163.06333,
    }

test = "SKADYEK"
string = test

#For user input
#string = input('Give me a protein string\n')
#Needs exit if input string does not contain any key of MonoMass

Total_mass = 0

for l in string:
    mass = MonoMass[l]
    Total_mass += mass

print("Total Mass for " + string + " is " + f'{round(Total_mass,3)}')

    
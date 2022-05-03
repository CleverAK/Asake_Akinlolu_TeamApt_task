# -*- coding: utf-8 -*-
"""
TeamAPT task
ASAKE Akinlolu Olalekan
EEG/2016/013
OAU Undergraduate
"""

#Creating a list for Service provider number prefixes
MTN = ['0703','0706','0803','0806','0810','0813','0814','0816','0903','0906','0913','0916','07025','07026','0704']
Airtel = ['0701','0708','0802','0808','0812','0901','0902','0904','0907','0912']
Globacom = ['0705','0805','0807','0811','0815','0905','0915']
nineMobile = ['0809','0817','0818','0909','0908']
MTEL= ['0804']

#count variables to represent the total of numbers belonging to each service provider
MTN_count = 0
Airtel_count = 0
Globacom_count = 0
nineMobile_count = 0
MTEL_count = 0
count_None = 0

#defining functions
def analyzeNumbers(phoneNumber):
    #declaring all count variables as global variables
    global nineMobile_count
    global MTEL_count
    global count_None
    global MTN_count
    global Airtel_count
    global Globacom_count
  
    if phoneNumber[0:4] in MTN or phoneNumber[0:5] in MTN: #check if MTN
        MTN_count += 1 #increase MTN count by 1
    
    elif phoneNumber[0:4] in Airtel: #check if Airtel
        Airtel_count += 1 #increase Airtel count by 1
    
    elif phoneNumber[0:4] in Globacom: #check if Globacom
        Globacom_count += 1 #increase Globacom count by 1
    
    elif phoneNumber[0:4] in nineMobile: #check if 9mobile
        nineMobile_count += 1 #increase 9mobile count by 1
    
    elif phoneNumber[0:4] in MTEL: #check if MTEL
        MTEL_count += 1 #increase MTEL count by 1
    else: 
        count_None += 1 #if not in list, increase None count by 1

def summary():
    #summary statement
    print('There are', MTN_count,'MTN Number(s), \n' 'There are', Airtel_count,'Airtel Number(s), \n'
          'There are', Globacom_count,'Globacom Number(s), \n'
          'There are', nineMobile_count,'9mobile Number(s), \n'
          'There are', MTEL_count,'MTEL Number(s), \n'
          'and there are', count_None,'Number(s) not in list of Networks\n'
          'Total of', (MTN_count + Airtel_count +  Globacom_count + nineMobile_count + MTEL_count+ count_None), 'Phone Numbers'
          )
        
with open('PhoneNumbers.txt', 'r') as numbers:  #reading the attached file (same directory as the code file)
    for num in numbers: #iterating through the attached file
        analyzeNumbers(phoneNumber = num)

summary() #summary


        

    
    

    
    
    
    
    
    
    

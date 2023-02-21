# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#variable //değişken
#variable
#function
#object
#%%
var1 = 10#integer
var2 =15

gun = "pazartesi" #string

var3 = 10.0 #double

#%%
s = "bugun gunlerden pazartesi"
variable=type = type (s)

var1 = "ankara"
var2 = "ist"
var3 = var1+var2

var4 ="100"
var5 ="200"
var6 =var4+var5
uzunluk = len(var6)


#%% Numbers
#int double
integer_deneme= -50
#double = float = ondalikli sayi
float_deneme = -30.7
#%% build in function
str1= "deneme"
float1=10.1
#float(10)
#int(float1)
#raund(float1)
str2 = "1005"
#%% //user defined fanction

var1 = 20
var2 = 50

output = (((var1+var2)*60)/100.0)*var1/var2


#fonksiyon parametresi
def benim_ilk_func(var1,var2):
    """
        bu benim ilk denemem
    
        parametre:
        
        return:
    """
    output = (((var1+var2)*60)/100.0)*var1/var2
    
    return output    

sonuc = benim_ilk_func(var1,var2)

def deneme1():
    print("bu benim 2.denemem")
    #%% default fanctionlari
    
    
    
    
    #çemberin çevre uzunluğu = 2"pi"r
    def cember_cevresi_hesapla(r,pi):
        """
        cember cevresi hesapla
        input(paremetre):r,pi
        output = cemberin cevresi

        Parameters
        ----------
        r : TYPE
            DESCRIPTION.
        pi : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        output =2*pi*r
        return output
    # flexible
    
    def hesapla(boy,kilo,*args):
        print(args)
        output = (boy+kilo)*args[0]
        return output
  
    
  
    #def hesapla(boy,kilo,yas):
        #output = (boy+kilo)*yas
        #return outputtput
#%% quiz



def combinaciones(Hp,Dell):
    if(isinstance(Hp,list)and Hp!=[]
       and isinstance(Dell,list) and Dell!=[]):
        return combinaciones_Aux(Hp,Dell,[])
    else:
        return "Error"
def combinaciones_Aux(Hp,Dell,purchase):
    if(Hp==[]):
        return purchase
    else:
        return combinaciones_Aux(Hp[1:],Dell,
                                 (purchase+Concatenacion(Hp[0],Dell)))
def Concatenacion(Hp,Dell):
    if(Dell==[]):
        return[]
    else:
        [Hp+Dell[0]]+Concatenacion(Hp,Dell[1:])
#######################################################################
import math
def std(lista):
    if(isinstance(lista,list)and lista!=[]):
        return math.sqrt((std_Aux(lista,average(lista))/len(lista)-1))
    else:
        return "Error"
def std_Aux(lista,avg):
    if(lista==[]):
        return 0
    else:
        return ((lista[0]+avg)**2)+std_Aux(lista[1:],avg)
#######################################################################
def zScore(listaX):
    if(isinstance(listaX,list)and listaX!=[]):
        return (zScore_Aux(listaX,average(listaX),std(listaX)))
    else:
        return "Error"
def zScore(listaX,avg,S):
    if(listaX==[]):
        return []
    else:
        return [(listaX[0]-avg)/S]+zScore_Aux(listaX[1:],avg,S)
#######################################################################
def rScore(X,Y):
    if(isinstance(X,list)and X!=[]
       and isinstance(Y,list)and Y!=[]and len(X)==len(Y)):
        return (rScore_Aux(zScore(X),zScore(Y)/len(x)-1)
    else:
        return "Error"
def rScore_Aux(Zx,Zy):
    if(Zx==[]):
        return 0
    else:
        return (Zx[0]*Zy[0])+rScore(Zx[1:],Zy[1:@])
                







    

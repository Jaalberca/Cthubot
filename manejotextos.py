

from pickle import FALSE


def consultaStat(statconsultado, nombreficha):
    ficha=open(nombreficha+'.txt', 'r',encoding='utf-8')
    stats=ficha.readlines()
    #statconsultado=statconsultado.lower()
    for line in stats:
        if statconsultado in line:
            posigual=line.find('=')
            if posigual==len(statconsultado):
                valorstat=line[(posigual+1):].rstrip()
                ficha.close()
                return valorstat
    ficha.close()
    return -1

def cambioStat(statcambiado, valorstat, nombreficha):
    
    ficha=open(nombreficha+'.txt', 'r',encoding='utf-8')
    stats=ficha.readlines()
    ficha.close()
    ficha=open(nombreficha+'.txt', 'w',encoding='utf-8')
    #statcambiado=statcambiado.lower()
    for line in stats:
        if statcambiado in line:
            posigual=line.find('=')
            if posigual==len(statcambiado):
                line=line[:posigual+1]+valorstat+'\n'          
        ficha.write(line)          
    ficha.close()
    print(nombreficha+' ha cambiado su valor de '+ statcambiado+' a '+valorstat)

def sumaStat(statcambiado, valorsuma, nombreficha):
    ficha=open(nombreficha+'.txt', 'r',encoding='utf-8')
    stats=ficha.readlines()
    ficha.close()
    ficha=open(nombreficha+'.txt', 'w',encoding='utf-8')
    #statcambiado=statcambiado.lower()
    for line in stats:
        if statcambiado in line:
            posigual=line.find('=')
            try: 
                if posigual==len(statcambiado):
                    valorstat=int(line[(posigual+1):])+valorsuma
                    line=line[:posigual+1]+str(valorstat)+'\n'
            except ValueError:
                print('El stat no es un número')
                       
        ficha.write(line);          
    ficha.close()

def restaStat(statcambiado, valorresta, nombreficha):
    ficha=open(nombreficha+'.txt', 'r',encoding='utf-8')
    stats=ficha.readlines()
    ficha.close()
    ficha=open(nombreficha+'.txt', 'w',encoding='utf-8')
    #statcambiado=statcambiado.lower()
    for line in stats:
        if statcambiado in line:
            posigual=line.find('=')
            try: 
                if posigual==len(statcambiado):
                    valorstat=int(line[(posigual+1):])-valorresta
                    line=line[:posigual+1]+str(valorstat)+'\n'
            except ValueError:
                print('El stat no es un número')
                       
        ficha.write(line);          
    ficha.close()

def addtoStat(statcambiado, añadido, nombreficha):
    ficha=open(nombreficha+'.txt', 'r',encoding='utf-8')
    stats=ficha.readlines()
    ficha.close()
    ficha=open(nombreficha+'.txt', 'w',encoding='utf-8')
    #statcambiado=statcambiado.lower()
    for line in stats:
        if statcambiado in line:
            posigual=line.find('=')
            if posigual==len(statcambiado):
                line=line.rstrip()+', '+str(añadido)+'\n'                     
        ficha.write(line);          
    ficha.close()



def consultanombreStatextra(statconsultado, nombreficha):
    ficha=open(nombreficha+'.txt', 'r',encoding='utf-8')
    stats=ficha.readlines()
    #statconsultado=statconsultado.lower()
    for line in stats:
        if statconsultado in line:
            posigual=line.find('=')
            posigual2=line.rfind('=')
            #if (posigual2-posigual)==len(statconsultado):
            valorstat=line[(posigual+1):posigual2].rstrip()
            ficha.close()
            return valorstat

def consultavalorStatextra(statconsultado, nombreficha):
    ficha=open(nombreficha+'.txt', 'r',encoding='utf-8')
    stats=ficha.readlines()
    for line in stats:
        if statconsultado in line:
            posigual=line.rfind('=')
            valorstat=line[(posigual+1):].rstrip()
            ficha.close()
            return valorstat
  
def cambionombrestatextra(statcambiado,nuevonombre,nombreficha):
    
    ficha=open(nombreficha+'.txt', 'r',encoding='utf-8')
    stats=ficha.readlines()
    ficha.close()
    ficha=open(nombreficha+'.txt', 'w',encoding='utf-8')
    
    for line in stats:
        if statcambiado in line:
            posigual=line.find('=')
            posigual2=line.rfind('=')
            if posigual==len(statcambiado):
                line=line[:posigual+1]+nuevonombre+'=0\n'
        ficha.write(line)    
    ficha.close()  

def cambiovalorstatextra(statcambiado,nuevovalor,nombreficha):
    
    ficha=open(nombreficha+'.txt', 'r',encoding='utf-8')
    stats=ficha.readlines()
    ficha.close()
    ficha=open(nombreficha+'.txt', 'w',encoding='utf-8')

    for line in stats:
        if statcambiado in line:
            posigual=line.find('=')
            posigual2=line.rfind('=')
            if posigual==len(statcambiado):    
                line=line[:posigual2+1]+nuevovalor+'\n'
        ficha.write(line)    
    ficha.close()        


def sumaStatextra(statcambiado, valorsuma, nombreficha):
    ficha=open(nombreficha+'.txt', 'r',encoding='utf-8')
    stats=ficha.readlines()
    ficha.close()
    ficha=open(nombreficha+'.txt', 'w',encoding='utf-8')

    for line in stats:
        if statcambiado in line:
            posigual=line.find('=')
            posigual2=line.rfind('=')
            try: 
                if posigual==len(statcambiado):
                    valorstat=int(line[(posigual2+1):])+valorsuma
                    line=line[:posigual2+1]+str(valorstat)+'\n'
            except ValueError:
                print('El stat no es un número')
                       
        ficha.write(line);          
    ficha.close()


def restaStatextra(statcambiado, valorresta, nombreficha):
    ficha=open(nombreficha+'.txt', 'r',encoding='utf-8')
    stats=ficha.readlines()
    ficha.close()
    ficha=open(nombreficha+'.txt', 'w',encoding='utf-8')

    for line in stats:
        if statcambiado in line:
            posigual=line.find('=')
            posigual2=line.rfind('=')
            try: 
                if posigual==len(statcambiado):
                    valorstat=int(line[(posigual2+1):])-valorresta
                    line=line[:posigual2+1]+str(valorstat)+'\n'
            except ValueError:
                print('El stat no es un número')
                       
        ficha.write(line);          
    ficha.close()

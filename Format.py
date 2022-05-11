

def formatfunciones():
    ficha=open('text.txt', 'r')
    stats=ficha.readlines()
    stats.append("END")
    ficha.close()
    ficha=open('text.txt', 'w')

    for (x,line) in enumerate(stats):
        print(x)
        print(line)
        print(stats[x+1])
        print("----")
        line= "def "+ line.rstrip() +"( update, context):\n\n\ttexto=update.message.text\n\tficha=update.message.chat.username\n\tmanejotextos.cambioStat(\'"+line[3:].rstrip()+"\',texto,ficha)\n\tupdate.message.reply_markdown_v2(\'*"+line[3:].rstrip()+"*: \'+ manejotextos.consultaStat("+"\'"+line[3:].rstrip()+"\'"+", ficha) + \'\\nAhora escribe tu *"+ stats[x+1][3:].rstrip() +"*:' )\n\treturn "+ stats[x+1].upper()+ "\n\n\n"
        ficha.write(line)
    ficha.close()


def formatHandler():

    ficha=open('text.txt', 'r')
    stats=ficha.readlines()
    ficha.close()
    ficha=open('text.txt', 'w')

    for (x,line) in enumerate(stats):
    
        line= "funcionesSetStatsFicha."+line.upper().rstrip()+": [MessageHandler(Filters.text & (~Filters.command), "+"funcionesSetStatsFicha."+line.rstrip()+")],\n" 
        ficha.write(line)
    ficha.close()


def formatfichatoKeyboard():

    ficha=open('text.txt', 'r')
    stats=ficha.readlines()
    ficha.close()
    ficha=open('text.txt', 'w')

    for line in stats:
        posigual=line.find('=')
        line= "InlineKeyboardButton(\""+line[:posigual]+": \"+manejotextos.consultaStat(\""+line[:posigual]+"\",str(update.message.chat.username)), callback_data=\""+line[:posigual]+"\"),\n"
        ficha.write(line)
    ficha.close()
    #InlineKeyboardButton("Nombre:"+manejotextos.consultaStat("Nombre",str(update.message.chat.username)), callback_data="Nombre")

def formatfichatoQueryHandlersconbarra():

    ficha=open('text.txt', 'r')
    stats=ficha.readlines()
    ficha.close()
    ficha=open('text.txt', 'w')

    for line in stats:
      posigual=line.find('=')      
      line= line[:posigual]+'|'
      ficha.write(line)
    ficha.close()  
    #Fuerza|Destreza|Poder|Constitucion|Apariencia|Educacion|Tamano|Inteligencia....

formatfichatoQueryHandlersconbarra()



#SETLUGARDENACIMIENTO: [MessageHandler(Filters.text & (~Filters.command), setlugardenacimiento)],




from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler, InlineQueryHandler
from telegram import CallbackQuery, ChatAction, ReplyMarkup, chataction, Update, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
import telegram
import logging
import diceroller, manejotextos
import funcionesSetStatsFicha
import manejotextos

NIVELMOSTRARFICHA=100
NIVELSTATNUMERICO=101
NIVELCAMBIARSTATNUMERICO=102
NIVELMENUSTATEXTRA=103
NIVELDECISIONNOMBRESTATEXTRA=104
NIVELMENUCAMBIARSTATEXTRA=105
END=-1




def start(update, context):  
    
    #context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    update.message.reply_html('🐙 Bienvenid@ al asintente de <b>La llamada de Cthulhu 7ªED</b> 🐙\n\n'+
    'Con este bot podrás crear una ficha de personaje y luego interactuar con ella para hacer tiradas o modificar los valores.\n'+
    'Recuerda interactuar siempre con el bot en tu <b>chat privado</b>, no en el chat de campaña\n\n'+
    '•Usa /nuevaficha para entrar en el asistente de <b>creación de fichas</b>.\n'+
    '\tEs un proceso algo largo, así que ponte cómod@.\n\n'+
    '•Usa /ficha para <b>ver tu ficha</b>.\n'+
    '\tPulsa sobre un stat numérico para interactuar con él. Todas las interacciones se enviarán al chat de la campaña.\n'
    '\tPulsa sobre un stat vacío para renombrarlo y, posteriormente, interactuar con él.\n\n'
    '•Usa /takechatid para obtener el identificador del chat en el que lances el comando. Usalo en el chat de la campaña (con el bot dentro del grupo) y guarda el identificador\n\n'
    '•Usa /putchatid X donde las X corresponden al chat ID correspondiente para vincular tu ficha a un chat de campaña. Así, las interacciones que realices con tu ficha se enviarán al chat de campaña\n\n'
    '•Usa /roll X donde X corresponde a una notación de dados (2d100, 3d6\+5, etc...) para hacer esa tirada.\n\n'
    '•Usa /salir dentro de cualquier menú para salir de él.\n')

 
def mostrarficha1(update,context):

    try:
        
        keyboard1 = [
            [InlineKeyboardButton("Salir", callback_data='salir')],
            [InlineKeyboardButton("Ocupacion: "+manejotextos.consultaStat("Ocupacion",str(update.message.chat.username)), callback_data="Ocupacion")],
            [InlineKeyboardButton("Genero: "+manejotextos.consultaStat("Genero",str(update.message.chat.username)), callback_data="Genero"),InlineKeyboardButton("Edad: "+manejotextos.consultaStat("Edad",str(update.message.chat.username)), callback_data="Edad")],
            [
                InlineKeyboardButton("Lugar de residencia", callback_data='Lugar de residencia'),
                InlineKeyboardButton("Lugar de nacimiento", callback_data='Lugar de nacimiento')
            ],
            [InlineKeyboardButton("__________________________________________________________", callback_data='Categoria')],
            [InlineKeyboardButton("CARACTERISTICAS", callback_data='Categoria')],
            [
                InlineKeyboardButton("Fuerza:"+manejotextos.consultaStat("Fuerza",str(update.message.chat.username)), callback_data="Fuerza"),
                InlineKeyboardButton("Destreza:"+manejotextos.consultaStat("Destreza",str(update.message.chat.username)), callback_data='Destreza'),
                InlineKeyboardButton("Poder:"+manejotextos.consultaStat("Poder",str(update.message.chat.username)), callback_data='Poder'),
                
            ],
            [
                InlineKeyboardButton("Const:"+manejotextos.consultaStat("Constitucion",str(update.message.chat.username)), callback_data='Constitucion'),
                InlineKeyboardButton("Apariencia:"+manejotextos.consultaStat("Apariencia",str(update.message.chat.username)), callback_data='Apariencia'),
                InlineKeyboardButton("Educacion:"+manejotextos.consultaStat("Educacion",str(update.message.chat.username)), callback_data='Educacion'),
                
                
            ],
            [
                InlineKeyboardButton("Tamaño:"+manejotextos.consultaStat("Tamano",str(update.message.chat.username)), callback_data='Tamano'),
                InlineKeyboardButton("Int/Idea:"+manejotextos.consultaStat("Inteligencia",str(update.message.chat.username)), callback_data='Inteligencia'),
                InlineKeyboardButton("Movimiento:"+manejotextos.consultaStat("Movimiento",str(update.message.chat.username)), callback_data='Movimiento'),
                
            ],
            [InlineKeyboardButton("__________________________________________________________", callback_data='Categoria')],
            [InlineKeyboardButton("ESTADO", callback_data='Categoria')],
            [
                InlineKeyboardButton("Vida: "+manejotextos.consultaStat("Vida",str(update.message.chat.username)), callback_data="Vida"),
                InlineKeyboardButton("Vida maximo: "+manejotextos.consultaStat("Vida maximo",str(update.message.chat.username)), callback_data="Vida maximo"),
            ],
            [
                InlineKeyboardButton("Magia: "+manejotextos.consultaStat("Magia",str(update.message.chat.username)), callback_data="Magia"),
                InlineKeyboardButton("Magia maximo: "+manejotextos.consultaStat("Magia maximo",str(update.message.chat.username)), callback_data="Magia maximo"),
            ],
            [
                InlineKeyboardButton("Cordura: "+manejotextos.consultaStat("Cordura",str(update.message.chat.username)), callback_data="Cordura"),
                InlineKeyboardButton("Cor ini: "+manejotextos.consultaStat("Cordura inicial",str(update.message.chat.username)), callback_data="Cordura inicial"),
                InlineKeyboardButton("Cor max: "+manejotextos.consultaStat("Cordura maxima",str(update.message.chat.username)), callback_data="Cordura maxima"),
            ],
            [InlineKeyboardButton("Suerte: "+manejotextos.consultaStat("Suerte",str(update.message.chat.username)), callback_data="Suerte")],
            [InlineKeyboardButton("__________________________________________________________", callback_data='Categoria')],

            [InlineKeyboardButton("HABILIDADES DEL INVESTIGADOR", callback_data='Categoria')],
            [
                InlineKeyboardButton("Antropolog: "+manejotextos.consultaStat("Antropologia",str(update.message.chat.username)), callback_data="Antropologia"),
                InlineKeyboardButton("Cond maquin: "+manejotextos.consultaStat("Conducir maquinaria",str(update.message.chat.username)), callback_data="Conducir maquinaria"),
                InlineKeyboardButton("Mitos de Cthulhu: "+manejotextos.consultaStat("Mitos de Cthulhu",str(update.message.chat.username)), callback_data="Mitos de Cthulhu"),
            ],
            [
                InlineKeyboardButton("Armas fuego", callback_data='Categoria'),
                InlineKeyboardButton("Contabilidad: "+manejotextos.consultaStat("Contabilidad",str(update.message.chat.username)), callback_data="Contabilidad"),
                InlineKeyboardButton("Nadar: "+manejotextos.consultaStat("Nadar",str(update.message.chat.username)), callback_data="Nadar"),
            ],
            [
                InlineKeyboardButton("Arma corta: "+manejotextos.consultaStat("Arma corta",str(update.message.chat.username)), callback_data="Arma corta"),
                InlineKeyboardButton("Credito: "+manejotextos.consultaStat("Credito",str(update.message.chat.username)), callback_data="Credito"),
                InlineKeyboardButton("Naturaleza: "+manejotextos.consultaStat("Naturaleza",str(update.message.chat.username)), callback_data="Naturaleza"),
            ],
            [
                InlineKeyboardButton("Fusil/Escopeta: "+manejotextos.consultaStat("Fusil/Escopeta",str(update.message.chat.username)), callback_data="Fusil/Escopeta"),
                InlineKeyboardButton("Derecho: "+manejotextos.consultaStat("Derecho",str(update.message.chat.username)), callback_data="Derecho"),
                InlineKeyboardButton("Orientarse: "+manejotextos.consultaStat("Orientarse",str(update.message.chat.username)), callback_data="Orientarse"),
            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra1',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra1', str(update.message.chat.username)),callback_data="Extra1"),
                InlineKeyboardButton("Descubrir: "+manejotextos.consultaStat("Descubrir",str(update.message.chat.username)), callback_data="Descubrir"),
                InlineKeyboardButton("Persuasion: "+manejotextos.consultaStat("Persuasion",str(update.message.chat.username)), callback_data="Persuasion"),
            ],
            [
                InlineKeyboardButton("Arqueologia: "+manejotextos.consultaStat("Arqueologia",str(update.message.chat.username)), callback_data="Arqueologia"),
                InlineKeyboardButton("Disfrazarse: "+manejotextos.consultaStat("Disfrazarse",str(update.message.chat.username)), callback_data="Disfrazarse"),
                InlineKeyboardButton("Pilotar: "+manejotextos.consultaStat("Pilotar",str(update.message.chat.username)), callback_data="Pilotar"),
            ],
            [
                InlineKeyboardButton("Arte/Artesania: "+manejotextos.consultaStat("Arte/Artesania",str(update.message.chat.username)), callback_data="Arte/Artesania"),
                InlineKeyboardButton("Electricidad: "+manejotextos.consultaStat("Electricidad",str(update.message.chat.username)), callback_data="Electricidad"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra14',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra14', str(update.message.chat.username)),callback_data="Extra14"),

            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra2',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra2', str(update.message.chat.username)),callback_data="Extra2"),
                InlineKeyboardButton("Encanto: "+manejotextos.consultaStat("Encanto",str(update.message.chat.username)), callback_data="Encanto"),
                InlineKeyboardButton("Primeros aux.: "+manejotextos.consultaStat("Primeros auxilios",str(update.message.chat.username)), callback_data="Primeros auxilios"),
            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra3',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra3', str(update.message.chat.username)),callback_data="Extra3"),
                InlineKeyboardButton("Equitacion: "+manejotextos.consultaStat("Equitacion",str(update.message.chat.username)), callback_data="Equitacion"),
                InlineKeyboardButton("Psicoanalisis: "+manejotextos.consultaStat("Psicoanalisis",str(update.message.chat.username)), callback_data="Psicoanalisis"),
            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra4',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra4', str(update.message.chat.username)),callback_data="Extra4"),
                InlineKeyboardButton("Escuchar: "+manejotextos.consultaStat("Escuchar",str(update.message.chat.username)), callback_data="Escuchar"),
                InlineKeyboardButton("Psicologia: "+manejotextos.consultaStat("Psicologia",str(update.message.chat.username)), callback_data="Psicologia"),
            ],
            [
                InlineKeyboardButton("Buscar libros: "+manejotextos.consultaStat("Buscar libros",str(update.message.chat.username)), callback_data="Buscar libros"),
                InlineKeyboardButton("Esquivar: "+manejotextos.consultaStat("Esquivar",str(update.message.chat.username)), callback_data="Esquivar"),
                InlineKeyboardButton("Saltar: "+manejotextos.consultaStat("Saltar",str(update.message.chat.username)), callback_data="Saltar"),
            ],
            [
                InlineKeyboardButton("Cerrajeria: "+manejotextos.consultaStat("Cerrajeria",str(update.message.chat.username)), callback_data="Cerrajeria"),
                InlineKeyboardButton("Historia: "+manejotextos.consultaStat("Historia",str(update.message.chat.username)), callback_data="Historia"),
                InlineKeyboardButton("Seguir rastros: "+manejotextos.consultaStat("Seguir rastros",str(update.message.chat.username)), callback_data="Seguir rastros"),
            ],
            [
                InlineKeyboardButton("Charlataneria: "+manejotextos.consultaStat("Charlataneria",str(update.message.chat.username)), callback_data="Charlataneria"),
                InlineKeyboardButton("Intimidar: "+manejotextos.consultaStat("Intimidar",str(update.message.chat.username)), callback_data="Intimidar"),
                InlineKeyboardButton("Sigilo: "+manejotextos.consultaStat("Sigilo",str(update.message.chat.username)), callback_data="Sigilo"),
            ],
            [
                InlineKeyboardButton("Ciencia: "+manejotextos.consultaStat("Ciencia",str(update.message.chat.username)), callback_data="Ciencia"),
                InlineKeyboardButton("Juego de manos: "+manejotextos.consultaStat("Juego de manos",str(update.message.chat.username)), callback_data="Juego de manos"),
                InlineKeyboardButton("Supervivencia: "+manejotextos.consultaStat("Supervivencia",str(update.message.chat.username)), callback_data="Supervivencia"),
            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra5',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra5', str(update.message.chat.username)),callback_data="Extra5"),
                InlineKeyboardButton("Lanzar: "+manejotextos.consultaStat("Lanzar",str(update.message.chat.username)), callback_data="Lanzar"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra15',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra15', str(update.message.chat.username)),callback_data="Extra15"),

            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra6',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra6', str(update.message.chat.username)),callback_data="Extra6"),
                InlineKeyboardButton("Lengua propia: "+manejotextos.consultaStat("Lengua propia",str(update.message.chat.username)), callback_data="Lengua propia"),
                InlineKeyboardButton("Tasacion: "+manejotextos.consultaStat("Tasacion",str(update.message.chat.username)), callback_data="Tasacion"),
            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra7',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra7', str(update.message.chat.username)),callback_data="Extra7"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra10',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra10', str(update.message.chat.username)),callback_data="Extra10"),
                InlineKeyboardButton("Trepar: "+manejotextos.consultaStat("Trepar",str(update.message.chat.username)), callback_data="Trepar"),
            ],
            [
                InlineKeyboardButton("Ciencias ocultas: "+manejotextos.consultaStat("Ciencias ocultas",str(update.message.chat.username)), callback_data="Ciencias ocultas"),
                InlineKeyboardButton("Otras lenguas: "+manejotextos.consultaStat("Otras lenguas",str(update.message.chat.username)), callback_data="Otras lenguas"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra16',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra16', str(update.message.chat.username)),callback_data="Extra16"),
            ],
            [
                InlineKeyboardButton("Combatir", callback_data='Categoria'),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra11',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra11', str(update.message.chat.username)),callback_data="Extra11"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra17',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra17', str(update.message.chat.username)),callback_data="Extra17"),
            ],
            [
                InlineKeyboardButton("Pelea: "+manejotextos.consultaStat("Pelea",str(update.message.chat.username)), callback_data="Pelea"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra12',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra12', str(update.message.chat.username)),callback_data="Extra12"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra18',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra18', str(update.message.chat.username)),callback_data="Extra18"),           
            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra8',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra8', str(update.message.chat.username)),callback_data="Extra8"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra13',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra13', str(update.message.chat.username)),callback_data="Extra13"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra19',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra19', str(update.message.chat.username)),callback_data="Extra19"),                
            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra9',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra9', str(update.message.chat.username)),callback_data="Extra9"),
                InlineKeyboardButton("Mecanica: "+manejotextos.consultaStat("Mecanica",str(update.message.chat.username)), callback_data="Mecanica"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra20',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra20', str(update.message.chat.username)),callback_data="Extra20"),
            ],
            [
                InlineKeyboardButton("Conducir automovil: "+manejotextos.consultaStat("Conducir automovil",str(update.message.chat.username)), callback_data="Conducir automovil"),
                InlineKeyboardButton("Medicina: "+manejotextos.consultaStat("Medicina",str(update.message.chat.username)), callback_data="Medicina"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra21',str(update.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra21', str(update.message.chat.username)),callback_data="Extra21"),
            ],
            [InlineKeyboardButton("Salir", callback_data='salir')],
            
        ]
        
        keyboard2 = [
            [InlineKeyboardButton("Salir", callback_data='salir')], 
            [InlineKeyboardButton("ARMAS", callback_data='Categoria')],
            [
                InlineKeyboardButton("Arma 1: "+manejotextos.consultaStat("Arma 1",str(update.message.chat.username)), callback_data="Arma 1"),
                InlineKeyboardButton("Arma 2: "+manejotextos.consultaStat("Arma 2",str(update.message.chat.username)), callback_data="Arma 2"),
                InlineKeyboardButton("Arma 3: "+manejotextos.consultaStat("Arma 3",str(update.message.chat.username)), callback_data="Arma 3"),
                InlineKeyboardButton("Arma 4: "+manejotextos.consultaStat("Arma 4",str(update.message.chat.username)), callback_data="Arma 4"),
            ],
            [
                InlineKeyboardButton("Bonificacion dano: "+manejotextos.consultaStat("Bonificacion dano",str(update.message.chat.username)), callback_data="Bonificacion dano"),
                InlineKeyboardButton("Corpulencia: "+manejotextos.consultaStat("Corpulencia",str(update.message.chat.username)), callback_data="Corpulencia"),
            ],
            [InlineKeyboardButton("__________________________________________________________", callback_data='Categoria')],
            [InlineKeyboardButton("TRASFONDO", callback_data='Categoria')],
            [
                InlineKeyboardButton("Descripcion personal", callback_data="Descripcion personal"),
                InlineKeyboardButton("Rasgos", callback_data="Rasgos"),
            ],
            [
                InlineKeyboardButton("Ideologia creencias", callback_data="Ideologia creencias"),
                InlineKeyboardButton("Lesiones y cicatrices", callback_data="Lesiones y cicatrices"),
            ],
            [
                InlineKeyboardButton("Allegados", callback_data="Allegados"),
                InlineKeyboardButton("Fobias y manias", callback_data="Fobias y manias"),
            ],
            [
                InlineKeyboardButton("Lugares significativos", callback_data="Lugares significativos"),
                InlineKeyboardButton("Tomos arcanos, hechizos y artefactos", callback_data="Tomos arcanos, hechizos y artefactos"),
            ],
            [
                InlineKeyboardButton("Posesiones preciadas", callback_data="Posesiones preciadas"),
                InlineKeyboardButton("Encuentros con entidades extranas", callback_data="Encuentros con entidades extranas"),
            ],
            [InlineKeyboardButton("__________________________________________________________", callback_data='Categoria')],
            [InlineKeyboardButton("Equipo: "+manejotextos.consultaStat("Equipo",str(update.message.chat.username)), callback_data="Equipo")],
            [InlineKeyboardButton("__________________________________________________________", callback_data='Categoria')],
            [
                InlineKeyboardButton("Nivel de gasto: "+manejotextos.consultaStat("Nivel de gasto",str(update.message.chat.username)), callback_data="Nivel de gasto"),
                InlineKeyboardButton("Dinero: "+manejotextos.consultaStat("Dinero",str(update.message.chat.username)), callback_data="Dinero"),
                InlineKeyboardButton("Bienes: "+manejotextos.consultaStat("Bienes",str(update.message.chat.username)), callback_data="Bienes"),
            ],
            [InlineKeyboardButton("__________________________________________________________", callback_data='Categoria')],
            [InlineKeyboardButton("Salir", callback_data='salir')],
        ]

        reply_markup1 = InlineKeyboardMarkup(keyboard1)
        reply_markup2 = InlineKeyboardMarkup(keyboard2)
        update.message.reply_html('Ficha de '+manejotextos.consultaStat("Jugador",str(update.message.chat.username))+'.    Investigador: <b>'+manejotextos.consultaStat("Nombre",str(update.message.chat.username))+'</b>', reply_markup=reply_markup1, )
       # update.message.reply_html('hoja dos',reply_markup=reply_markup2)
        return NIVELMOSTRARFICHA

    except FileNotFoundError: 
        
        #print(update)
        #print(update.message.chat.from_user.name)
        update.message.reply_html("Ficha de jugador/a <b>"+str(update.message.chat.username)+"</b> no encontrada. \nPor favor, crea una nueva ficha usando el comando /nuevaficha")
        return END

def menustatnumerico(update,context):

    
    query = update.callback_query
    query.answer()
    Memoriacomando=update.callback_query.data
    manejotextos.cambioStat('Memoriacomando',Memoriacomando,str(query.message.chat.username))
    #print(Memoriacomando)
    #print(query)
    keyboard = [
        [InlineKeyboardButton("Tirada de habilidad", callback_data='tirada')],
        [InlineKeyboardButton("Tirada de habilidad con dado de bonificación", callback_data='tiradabonificada')],
        [InlineKeyboardButton("Tirada de habilidad con dado de penalización", callback_data='tiradapenalizada')],
        [InlineKeyboardButton("Cambiar la estadística", callback_data='menucambiarstatnumerico')],
        [InlineKeyboardButton("Ir atrás", callback_data='atrasmostrarficha1')],        
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text("<b>"+ Memoriacomando +'</b>: '+ manejotextos.consultaStat(Memoriacomando,str(query.message.chat.username))+'     ¿Que quieres hacer?', reply_markup=reply_markup,parse_mode=telegram.ParseMode.HTML )
    #
    return NIVELSTATNUMERICO

def tirada (update,context):
    
    try:
        query = update.callback_query
        query.answer()
        Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))
        tirada=diceroller.roll('1d100')
        valorStat=int(manejotextos.consultaStat(Memoriacomando,str(query.message.chat.username)))
        
        resultado=''

        if tirada[1]==1: resultado='<b>ÉXITO CRÍTICO</b>'
        elif (tirada[1]>95 and valorStat<50) or (tirada[1]==100): resultado='<b>PIFIA</b>'
        elif tirada[1]<=valorStat/5: resultado='<b>Éxito Extremo</b>'
        elif tirada[1]<=valorStat/2: resultado='<b>Éxito Dificil</b>'
        elif tirada[1]<=valorStat: resultado='<b>Éxito normal</b>'
        elif tirada[1]>valorStat: resultado='<b>Fracaso</b>'

        text=resultado+' de '+manejotextos.consultaStat('Nombre',str(query.message.chat.username))+'.\n'+"Tirada: "+str(tirada[1])+'   '+ Memoriacomando+': '+str(valorStat)
        query.edit_message_text( text, parse_mode=telegram.ParseMode.HTML)
        
        context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(query.message.chat.username) ),text=resultado+' de '+manejotextos.consultaStat('Nombre',str(query.message.chat.username))+'.\n'+"Tirada: "+str(tirada[1])+'   '+ Memoriacomando+': '+str(valorStat), parse_mode=telegram.ParseMode.HTML)
        return END
    except ValueError: 
        query = update.callback_query
        query.answer()
        Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))
        tirada=diceroller.roll('1d100')
        valorStat=int(manejotextos.consultavalorStatextra(Memoriacomando,str(query.message.chat.username)))
        resultado=''

        if tirada[1]==1: resultado='<b>ÉXITO CRÍTICO</b>'
        elif (tirada[1]>95 and valorStat<50) or (tirada[1]==100): resultado='<b>PIFIA</b>'
        elif tirada[1]<=valorStat/5: resultado='<b>Éxito Extremo</b>'
        elif tirada[1]<=valorStat/2: resultado='<b>Éxito Dificil</b>'
        elif tirada[1]<=valorStat: resultado='<b>Éxito normal</b>'
        elif tirada[1]>valorStat: resultado='<b>Fracaso</b>'

        text=resultado+' de '+manejotextos.consultaStat('Nombre',str(query.message.chat.username))+'.\n'+"Tirada: "+str(tirada[1])+'   '+ manejotextos.consultanombreStatextra(Memoriacomando,str(query.message.chat.username))+': '+str(valorStat)
        query.edit_message_text( text, parse_mode=telegram.ParseMode.HTML)
        
        context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(query.message.chat.username) ),text=resultado+' de '+manejotextos.consultaStat('Nombre',str(query.message.chat.username))+'.\n'+"Tirada: "+str(tirada[1])+'   '+ manejotextos.consultanombreStatextra(Memoriacomando,str(query.message.chat.username))+': '+str(valorStat), parse_mode=telegram.ParseMode.HTML )
        return END
def tiradabonificada (update,context):
    try:
        query = update.callback_query
        query.answer()
        Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))

        decena1=diceroller.roll('1d10')[1]*10
        if decena1==100: decena1=0
        decena2=diceroller.roll('1d10')[1]*10
        if decena2==100: decena2=0
        unidad=diceroller.roll('1d10')[1]
        valorStat=int(manejotextos.consultaStat(Memoriacomando,str(query.message.chat.username)))
        resultado=''

        if decena1>decena2: tirada=decena2+unidad
        else: tirada=decena1+unidad

        if decena1==0 and decena2==0 and unidad==10: tirada=100

        if tirada==1: resultado='<b>ÉXITO CRÍTICO</b>'
        elif (tirada>95 and valorStat<50) or (tirada==100): resultado='<b>PIFIA</b>'
        elif tirada<=valorStat/5: resultado='<b>Éxito Extremo</b>'
        elif tirada<=valorStat/2: resultado='<b>Éxito Dificil</b>'
        elif tirada<=valorStat: resultado='<b>Éxito normal</b>'
        elif tirada>valorStat: resultado='<b>Fracaso</b>'

        query.edit_message_text( resultado+' de '+manejotextos.consultaStat('Nombre',str(query.message.chat.username))+'.\n'+"Tirada: "+str(tirada)+' (Dados: '+ str(decena1) + ' '+ str(decena2) +' ' +str(unidad)+')   '+ Memoriacomando+': '+str(valorStat), parse_mode=telegram.ParseMode.HTML)
        context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(query.message.chat.username) ),text=resultado+' de '+manejotextos.consultaStat('Nombre',str(query.message.chat.username))+'.\n'+"Tirada: "+str(tirada)+' (Dados: '+ str(decena1) + ' '+ str(decena2) +' ' +str(unidad)+')   '+ Memoriacomando+': '+str(valorStat), parse_mode=telegram.ParseMode.HTML )
        return END
    except ValueError:
        query = update.callback_query
        query.answer()
        Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))

        decena1=diceroller.roll('1d10')[1]*10
        if decena1==100: decena1=0
        decena2=diceroller.roll('1d10')[1]*10
        if decena2==100: decena2=0
        unidad=diceroller.roll('1d10')[1]
        valorStat=int(manejotextos.consultavalorStatextra(Memoriacomando,str(query.message.chat.username)))
        resultado=''

        if decena1>decena2: tirada=decena2+unidad
        else: tirada=decena1+unidad

        if decena1==0 and decena2==0 and unidad==10: tirada=100

        if tirada==1: resultado='<b>ÉXITO CRÍTICO</b>'
        elif (tirada>95 and valorStat<50) or (tirada==100): resultado='<b>PIFIA</b>'
        elif tirada<=valorStat/5: resultado='<b>Éxito Extremo</b>'
        elif tirada<=valorStat/2: resultado='<b>Éxito Dificil</b>'
        elif tirada<=valorStat: resultado='<b>Éxito normal</b>'
        elif tirada>valorStat: resultado='<b>Fracaso</b>'

        query.edit_message_text( resultado+' de '+manejotextos.consultaStat('Nombre',str(query.message.chat.username))+'.\n'+"Tirada: "+str(tirada)+' (Dados: '+ str(decena1) + ' '+ str(decena2) +' ' +str(unidad)+')   '+ manejotextos.consultanombreStatextra(Memoriacomando,str(query.message.chat.username))+': '+str(valorStat), parse_mode=telegram.ParseMode.HTML)
        context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(query.message.chat.username) ),text=resultado+' de '+manejotextos.consultaStat('Nombre',str(query.message.chat.username))+'.\n'+"Tirada: "+str(tirada)+' (Dados: '+ str(decena1) + ' '+ str(decena2) +' ' +str(unidad)+')   '+ manejotextos.consultanombreStatextra(Memoriacomando,str(query.message.chat.username))+': '+str(valorStat), parse_mode=telegram.ParseMode.HTML )
        return END
def tiradapenalizada (update,context):
    
    try:
        query = update.callback_query
        query.answer()
        Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))

        decena1=diceroller.roll('1d10')[1]*10
        if decena1==100: decena1=0
        decena2=diceroller.roll('1d10')[1]*10
        if decena2==100: decena2=0
        unidad=diceroller.roll('1d10')[1]
        valorStat=int(manejotextos.consultaStat(Memoriacomando,str(query.message.chat.username)))
        resultado=''

        if decena1>decena2: tirada=decena1+unidad
        else: tirada=decena1+unidad
        if decena1==0 and decena2==0 and unidad==10: tirada=100

        if tirada==1: resultado='<b>ÉXITO CRÍTICO</b>'
        elif (tirada>95 and valorStat<50) or (tirada==100): resultado='<b>PIFIA</b>'
        elif tirada<=valorStat/5: resultado='<b>Éxito Extremo</b>'
        elif tirada<=valorStat/2: resultado='<b>Éxito Dificil</b>'
        elif tirada<=valorStat: resultado='<b>Éxito normal</b>'
        elif tirada>valorStat: resultado='<b>Fracaso</b>'

        query.edit_message_text( resultado+' de '+manejotextos.consultaStat('Nombre',str(query.message.chat.username))+'.\n'+"Tirada: "+str(tirada)+' (Dados: '+ str(decena1) + ' '+ str(decena2) +' ' +str(unidad)+')   '+ Memoriacomando+': '+str(valorStat), parse_mode=telegram.ParseMode.HTML)
        context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(query.message.chat.username) ),text=resultado+' de '+manejotextos.consultaStat('Nombre',str(query.message.chat.username))+'.\n'+"Tirada: "+str(tirada)+' (Dados: '+ str(decena1) + ' '+ str(decena2) +' ' +str(unidad)+')   '+ Memoriacomando+': '+str(valorStat), parse_mode=telegram.ParseMode.HTML )
        return END
    except ValueError:
        query = update.callback_query
        query.answer()
        Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))

        decena1=diceroller.roll('1d10')[1]*10
        if decena1==100: decena1=0
        decena2=diceroller.roll('1d10')[1]*10
        if decena2==100: decena2=0
        unidad=diceroller.roll('1d10')[1]
        valorStat=int(manejotextos.consultavalorStatextra(Memoriacomando,str(query.message.chat.username)))
        resultado=''

        if decena1>decena2: tirada=decena1+unidad
        else: tirada=decena1+unidad
        if decena1==0 and decena2==0 and unidad==10: tirada=100

        if tirada==1: resultado='<b>ÉXITO CRÍTICO</b>'
        elif (tirada>95 and valorStat<50) or (tirada==100): resultado='<b>PIFIA</b>'
        elif tirada<=valorStat/5: resultado='<b>Éxito Extremo</b>'
        elif tirada<=valorStat/2: resultado='<b>Éxito Dificil</b>'
        elif tirada<=valorStat: resultado='<b>Éxito normal</b>'
        elif tirada>valorStat: resultado='<b>Fracaso</b>'

        query.edit_message_text( resultado+' de '+manejotextos.consultaStat('Nombre',str(query.message.chat.username))+'.\n'+"Tirada: "+str(tirada)+' (Dados: '+ str(decena1) + ' '+ str(decena2) +' ' +str(unidad)+')   '+ manejotextos.consultanombreStatextra(Memoriacomando,str(query.message.chat.username))+': '+str(valorStat), parse_mode=telegram.ParseMode.HTML)
        context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(query.message.chat.username) ),text=resultado+' de '+manejotextos.consultaStat('Nombre',str(query.message.chat.username))+'.\n'+"Tirada: "+str(tirada)+' (Dados: '+ str(decena1) + ' '+ str(decena2) +' ' +str(unidad)+')   '+ manejotextos.consultanombreStatextra(Memoriacomando,str(query.message.chat.username))+': '+str(valorStat), parse_mode=telegram.ParseMode.HTML )
        return END

def menucambiarstatnumerico (update,context):
   
    query = update.callback_query
    query.answer()
    Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))
    keyboard = [
        
        [InlineKeyboardButton("Sumar 1", callback_data='sumar1stat'),InlineKeyboardButton("Sumar 5", callback_data='sumar5stat')],
        [InlineKeyboardButton("Restar 1", callback_data='restar1stat'),InlineKeyboardButton("Restar 5", callback_data='restar5stat')],
        [InlineKeyboardButton("Ir atrás", callback_data='atrasmostrarficha1')],        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text("<b>"+ Memoriacomando +'</b>: '+ manejotextos.consultaStat(Memoriacomando,str(query.message.chat.username))+'     ¿Que quieres hacer?', reply_markup=reply_markup,parse_mode=telegram.ParseMode.HTML )
    return NIVELCAMBIARSTATNUMERICO

def sumar1stat(update,context):

    query = update.callback_query
    query.answer()
    Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))
    manejotextos.sumaStat(Memoriacomando,1,str(query.message.chat.username))
    menucambiarstatnumerico(update,context)
    context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(query.message.chat.username) ),text= '<b>'+query.message.chat.username+'</b> ha incrementado su '+ Memoriacomando+' a '+ manejotextos.consultaStat(Memoriacomando,str(query.message.chat.username)), parse_mode=telegram.ParseMode.HTML )
    
def sumar5stat(update,context):
    
    query = update.callback_query
    query.answer()
    Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))
    manejotextos.sumaStat(Memoriacomando,5,str(query.message.chat.username))
    menucambiarstatnumerico(update,context)
    context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(query.message.chat.username) ),text= '<b>'+query.message.chat.username+'</b> ha incrementado su '+ Memoriacomando+' a '+ manejotextos.consultaStat(Memoriacomando,str(query.message.chat.username)), parse_mode=telegram.ParseMode.HTML )

def restar1stat(update,context):
    
    query = update.callback_query
    query.answer()
    Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))
    manejotextos.restaStat(Memoriacomando,1,str(query.message.chat.username))
    menucambiarstatnumerico(update,context)
    context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(query.message.chat.username) ),text= '<b>'+query.message.chat.username+'</b> ha disminuido su '+ Memoriacomando+' a '+ manejotextos.consultaStat(Memoriacomando,str(query.message.chat.username)), parse_mode=telegram.ParseMode.HTML )

def restar5stat(update,context):
    
    query = update.callback_query
    query.answer()
    Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))
    manejotextos.restaStat(Memoriacomando,5,str(query.message.chat.username))
    menucambiarstatnumerico(update,context)
    context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(query.message.chat.username) ),text= '<b>'+query.message.chat.username+'</b> ha disminuido su '+ Memoriacomando+' a '+ manejotextos.consultaStat(Memoriacomando,str(query.message.chat.username)), parse_mode=telegram.ParseMode.HTML )


def menustatextra(update,context):
    query = update.callback_query
    query.answer()
    Memoriacomando=update.callback_query.data
    manejotextos.cambioStat('Memoriacomando',Memoriacomando,str(query.message.chat.username))
    
    if (manejotextos.consultanombreStatextra(Memoriacomando,str(query.message.chat.username))):
        keyboard = [
            [InlineKeyboardButton("Renombrar el stat", callback_data='nombrarstatextra')],
            [InlineKeyboardButton("Tirada de habilidad", callback_data='tirada')],
            [InlineKeyboardButton("Tirada de habilidad con dado de bonificación", callback_data='tiradabonificada')],
            [InlineKeyboardButton("Tirada de habilidad con dado de penalización", callback_data='tiradapenalizada')],
            [InlineKeyboardButton("Cambiar la estadística", callback_data='menucambiarstatextra')],
            [InlineKeyboardButton("Ir atrás", callback_data='atrasmostrarficha1')],        
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("<b>"+ manejotextos.consultanombreStatextra(Memoriacomando,str(query.message.chat.username)) +'</b>: '+ manejotextos.consultavalorStatextra(Memoriacomando,str(query.message.chat.username))+'     ¿Que quieres hacer?', reply_markup=reply_markup,parse_mode=telegram.ParseMode.HTML )

    else: 
        keyboard = [
        [InlineKeyboardButton("Nombrar el stat", callback_data='nombrarstatextra')],      
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Este es un stat extra. Para definirlo, pulsa sobre \"Nombrar el stat\"", reply_markup=reply_markup,parse_mode=telegram.ParseMode.HTML )

    
    return NIVELMENUSTATEXTRA
    
def nombrarstatextra(update,context):
    query = update.callback_query
    query.answer()
    query.edit_message_text("Escribe a continuación el nombre para el stat extra y enviamelo",parse_mode=telegram.ParseMode.HTML )
    return NIVELDECISIONNOMBRESTATEXTRA

def decisionnombrestatextra(update,context):

    nuevonombre=update.message.text
    user=update.message.chat.username
    print(user)
    manejotextos.cambionombrestatextra(manejotextos.consultaStat('Memoriacomando',str(update.message.chat.username)),nuevonombre,str(update.message.chat.username))
    context.bot.send_message(chat_id=update.effective_chat.id, text='Nombre de stat cambiado correctamente')
    return END


def menucambiarstatextra (update,context):
   
    query = update.callback_query
    query.answer()
    Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))
    keyboard = [
        
        [InlineKeyboardButton("Sumar 1", callback_data='sumar1statextra'),InlineKeyboardButton("Sumar 5", callback_data='sumar5statextra')],
        [InlineKeyboardButton("Restar 1", callback_data='restar1statextra'),InlineKeyboardButton("Restar 5", callback_data='restar5statextra')],
        [InlineKeyboardButton("Ir atrás", callback_data='atrasmostrarficha1')],        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text("<b>"+ manejotextos.consultanombreStatextra(Memoriacomando,str(query.message.chat.username)) +'</b>: '+ manejotextos.consultavalorStatextra(Memoriacomando,str(query.message.chat.username))+'     ¿Que quieres hacer?', reply_markup=reply_markup,parse_mode=telegram.ParseMode.HTML )
    return NIVELMENUCAMBIARSTATEXTRA

def sumar1statextra(update,context):

    query = update.callback_query
    query.answer()
    Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))
    manejotextos.sumaStatextra(Memoriacomando,1,str(query.message.chat.username))
    menucambiarstatextra(update,context)
    context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(query.message.chat.username) ),text= '<b>'+query.message.chat.username+'</b> ha incrementado su '+ manejotextos.consultanombreStatextra(Memoriacomando,str(query.message.chat.username))+' a '+ manejotextos.consultavalorStatextra(Memoriacomando,str(query.message.chat.username)), parse_mode=telegram.ParseMode.HTML )
    
def sumar5statextra(update,context):
    
    query = update.callback_query
    query.answer()
    Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))
    manejotextos.sumaStatextra(Memoriacomando,5,str(query.message.chat.username))
    menucambiarstatextra(update,context)
    context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(query.message.chat.username) ),text= '<b>'+query.message.chat.username+'</b> ha incrementado su '+manejotextos.consultanombreStatextra(Memoriacomando,str(query.message.chat.username))+' a '+ manejotextos.consultavalorStatextra(Memoriacomando,str(query.message.chat.username)), parse_mode=telegram.ParseMode.HTML )

def restar1statextra(update,context):
    
    query = update.callback_query
    query.answer()
    Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))
    manejotextos.restaStatextra(Memoriacomando,1,str(query.message.chat.username))
    menucambiarstatextra(update,context)
    context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(query.message.chat.username) ),text= '<b>'+query.message.chat.username+'</b> ha disminuido su '+manejotextos.consultanombreStatextra(Memoriacomando,str(query.message.chat.username))+' a '+ manejotextos.consultavalorStatextra(Memoriacomando,str(query.message.chat.username)), parse_mode=telegram.ParseMode.HTML )

def restar5statextra(update,context):
    
    query = update.callback_query
    query.answer()
    Memoriacomando=manejotextos.consultaStat('Memoriacomando',str(query.message.chat.username))
    manejotextos.restaStatextra(Memoriacomando,5,str(query.message.chat.username))
    menucambiarstatextra(update,context)
    context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(query.message.chat.username) ),text= '<b>'+query.message.chat.username+'</b> ha disminuido su '+ manejotextos.consultanombreStatextra(Memoriacomando,str(query.message.chat.username))+' a '+ manejotextos.consultavalorStatextra(Memoriacomando,str(query.message.chat.username)), parse_mode=telegram.ParseMode.HTML )

def atrasmostrarficha1 (update,context):
    
    query = update.callback_query
    query.answer()
    keyboard1 = [
            [InlineKeyboardButton("Salir", callback_data='salir')],
            [InlineKeyboardButton("Ocupacion: "+manejotextos.consultaStat("Ocupacion",str(query.message.chat.username)), callback_data="Ocupacion")],
            [InlineKeyboardButton("Genero: "+manejotextos.consultaStat("Genero",str(query.message.chat.username)), callback_data="Genero"),InlineKeyboardButton("Edad: "+manejotextos.consultaStat("Edad",str(query.message.chat.username)), callback_data="Edad")],
            [
                InlineKeyboardButton("Lugar de residencia", callback_data='Lugar de residencia'),
                InlineKeyboardButton("Lugar de nacimiento", callback_data='Lugar de nacimiento')
            ],
            [InlineKeyboardButton("__________________________________________________________", callback_data='Categoria')],
            [InlineKeyboardButton("CARACTERISTICAS", callback_data='Categoria')],
            [
                InlineKeyboardButton("Fuerza:"+manejotextos.consultaStat("Fuerza",str(query.message.chat.username)), callback_data="Fuerza"),
                InlineKeyboardButton("Destreza:"+manejotextos.consultaStat("Destreza",str(query.message.chat.username)), callback_data='Destreza'),
                InlineKeyboardButton("Poder:"+manejotextos.consultaStat("Poder",str(query.message.chat.username)), callback_data='Poder'),
                
            ],
            [
                InlineKeyboardButton("Constitucion:"+manejotextos.consultaStat("Constitucion",str(query.message.chat.username)), callback_data='Constitucion'),
                InlineKeyboardButton("Apariencia:"+manejotextos.consultaStat("Apariencia",str(query.message.chat.username)), callback_data='Apariencia'),
                InlineKeyboardButton("Educacion:"+manejotextos.consultaStat("Educacion",str(query.message.chat.username)), callback_data='Educacion'),
                
                
            ],
            [
                InlineKeyboardButton("Tamaño:"+manejotextos.consultaStat("Tamano",str(query.message.chat.username)), callback_data='Tamano'),
                InlineKeyboardButton("Inteligencia/Idea:"+manejotextos.consultaStat("Inteligencia",str(query.message.chat.username)), callback_data='Inteligencia'),
                InlineKeyboardButton("Movimiento:"+manejotextos.consultaStat("Movimiento",str(query.message.chat.username)), callback_data='Movimiento'),
                
            ],
            [InlineKeyboardButton("__________________________________________________________", callback_data='Categoria')],
            [InlineKeyboardButton("ESTADO", callback_data='Categoria')],
            [
                InlineKeyboardButton("Vida: "+manejotextos.consultaStat("Vida",str(query.message.chat.username)), callback_data="Vida"),
                InlineKeyboardButton("Vida maximo: "+manejotextos.consultaStat("Vida maximo",str(query.message.chat.username)), callback_data="Vida maximo"),
            ],
            [
                InlineKeyboardButton("Magia: "+manejotextos.consultaStat("Magia",str(query.message.chat.username)), callback_data="Magia"),
                InlineKeyboardButton("Magia maximo: "+manejotextos.consultaStat("Magia maximo",str(query.message.chat.username)), callback_data="Magia maximo"),
            ],
            [
                InlineKeyboardButton("Cordura: "+manejotextos.consultaStat("Cordura",str(query.message.chat.username)), callback_data="Cordura"),
                InlineKeyboardButton("Cordura inicial: "+manejotextos.consultaStat("Cordura inicial",str(query.message.chat.username)), callback_data="Cordura inicial"),
                InlineKeyboardButton("Cordura maxima: "+manejotextos.consultaStat("Cordura maxima",str(query.message.chat.username)), callback_data="Cordura maxima"),
            ],
            [InlineKeyboardButton("Suerte: "+manejotextos.consultaStat("Suerte",str(query.message.chat.username)), callback_data="Suerte")],
            [InlineKeyboardButton("__________________________________________________________", callback_data='Categoria')],

            [InlineKeyboardButton("HABILIDADES DEL INVESTIGADOR", callback_data='Categoria')],
            [
                InlineKeyboardButton("Antropologia: "+manejotextos.consultaStat("Antropologia",str(query.message.chat.username)), callback_data="Antropologia"),
                InlineKeyboardButton("Conducir maquinaria: "+manejotextos.consultaStat("Conducir maquinaria",str(query.message.chat.username)), callback_data="Conducir maquinaria"),
                InlineKeyboardButton("Mitos de Cthulhu: "+manejotextos.consultaStat("Mitos de Cthulhu",str(query.message.chat.username)), callback_data="Mitos de Cthulhu"),
            ],
            [
                InlineKeyboardButton("Armas de fuego", callback_data='Categoria'),
                InlineKeyboardButton("Contabilidad: "+manejotextos.consultaStat("Contabilidad",str(query.message.chat.username)), callback_data="Contabilidad"),
                InlineKeyboardButton("Nadar: "+manejotextos.consultaStat("Nadar",str(query.message.chat.username)), callback_data="Nadar"),
            ],
            [
                InlineKeyboardButton("Arma corta: "+manejotextos.consultaStat("Arma corta",str(query.message.chat.username)), callback_data="Arma corta"),
                InlineKeyboardButton("Credito: "+manejotextos.consultaStat("Credito",str(query.message.chat.username)), callback_data="Credito"),
                InlineKeyboardButton("Naturaleza: "+manejotextos.consultaStat("Naturaleza",str(query.message.chat.username)), callback_data="Naturaleza"),
            ],
            [
                InlineKeyboardButton("Fusil/Escopeta: "+manejotextos.consultaStat("Fusil/Escopeta",str(query.message.chat.username)), callback_data="Fusil/Escopeta"),
                InlineKeyboardButton("Derecho: "+manejotextos.consultaStat("Derecho",str(query.message.chat.username)), callback_data="Derecho"),
                InlineKeyboardButton("Orientarse: "+manejotextos.consultaStat("Orientarse",str(query.message.chat.username)), callback_data="Orientarse"),
            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra1',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra1', str(query.message.chat.username)),callback_data="Extra1"),
                InlineKeyboardButton("Descubrir: "+manejotextos.consultaStat("Descubrir",str(query.message.chat.username)), callback_data="Descubrir"),
                InlineKeyboardButton("Persuasion: "+manejotextos.consultaStat("Persuasion",str(query.message.chat.username)), callback_data="Persuasion"),
            ],
            [
                InlineKeyboardButton("Arqueologia: "+manejotextos.consultaStat("Arqueologia",str(query.message.chat.username)), callback_data="Arqueologia"),
                InlineKeyboardButton("Disfrazarse: "+manejotextos.consultaStat("Disfrazarse",str(query.message.chat.username)), callback_data="Disfrazarse"),
                InlineKeyboardButton("Pilotar: "+manejotextos.consultaStat("Pilotar",str(query.message.chat.username)), callback_data="Pilotar"),
            ],
            [
                InlineKeyboardButton("Arte/Artesania: "+manejotextos.consultaStat("Arte/Artesania",str(query.message.chat.username)), callback_data="Arte/Artesania"),
                InlineKeyboardButton("Electricidad: "+manejotextos.consultaStat("Electricidad",str(query.message.chat.username)), callback_data="Electricidad"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra14',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra14', str(query.message.chat.username)),callback_data="Extra14"),

            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra2',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra2', str(query.message.chat.username)),callback_data="Extra2"),
                InlineKeyboardButton("Encanto: "+manejotextos.consultaStat("Encanto",str(query.message.chat.username)), callback_data="Encanto"),
                InlineKeyboardButton("Primeros auxilios: "+manejotextos.consultaStat("Primeros auxilios",str(query.message.chat.username)), callback_data="Primeros auxilios"),
            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra3',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra3', str(query.message.chat.username)),callback_data="Extra3"),
                InlineKeyboardButton("Equitacion: "+manejotextos.consultaStat("Equitacion",str(query.message.chat.username)), callback_data="Equitacion"),
                InlineKeyboardButton("Psicoanalisis: "+manejotextos.consultaStat("Psicoanalisis",str(query.message.chat.username)), callback_data="Psicoanalisis"),
            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra4',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra4', str(query.message.chat.username)),callback_data="Extra4"),
                InlineKeyboardButton("Escuchar: "+manejotextos.consultaStat("Escuchar",str(query.message.chat.username)), callback_data="Escuchar"),
                InlineKeyboardButton("Psicologia: "+manejotextos.consultaStat("Psicologia",str(query.message.chat.username)), callback_data="Psicologia"),
            ],
            [
                InlineKeyboardButton("Buscar libros: "+manejotextos.consultaStat("Buscar libros",str(query.message.chat.username)), callback_data="Buscar libros"),
                InlineKeyboardButton("Esquivar: "+manejotextos.consultaStat("Esquivar",str(query.message.chat.username)), callback_data="Esquivar"),
                InlineKeyboardButton("Saltar: "+manejotextos.consultaStat("Saltar",str(query.message.chat.username)), callback_data="Saltar"),
            ],
            [
                InlineKeyboardButton("Cerrajeria: "+manejotextos.consultaStat("Cerrajeria",str(query.message.chat.username)), callback_data="Cerrajeria"),
                InlineKeyboardButton("Historia: "+manejotextos.consultaStat("Historia",str(query.message.chat.username)), callback_data="Historia"),
                InlineKeyboardButton("Seguir rastros: "+manejotextos.consultaStat("Seguir rastros",str(query.message.chat.username)), callback_data="Seguir rastros"),
            ],
            [
                InlineKeyboardButton("Charlataneria: "+manejotextos.consultaStat("Charlataneria",str(query.message.chat.username)), callback_data="Charlataneria"),
                InlineKeyboardButton("Intimidar: "+manejotextos.consultaStat("Intimidar",str(query.message.chat.username)), callback_data="Intimidar"),
                InlineKeyboardButton("Sigilo: "+manejotextos.consultaStat("Sigilo",str(query.message.chat.username)), callback_data="Sigilo"),
            ],
            [
                InlineKeyboardButton("Ciencia: "+manejotextos.consultaStat("Ciencia",str(query.message.chat.username)), callback_data="Ciencia"),
                InlineKeyboardButton("Juego de manos: "+manejotextos.consultaStat("Juego de manos",str(query.message.chat.username)), callback_data="Juego de manos"),
                InlineKeyboardButton("Supervivencia: "+manejotextos.consultaStat("Supervivencia",str(query.message.chat.username)), callback_data="Supervivencia"),
            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra5',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra5', str(query.message.chat.username)),callback_data="Extra5"),
                InlineKeyboardButton("Lanzar: "+manejotextos.consultaStat("Lanzar",str(query.message.chat.username)), callback_data="Lanzar"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra15',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra15', str(query.message.chat.username)),callback_data="Extra15"),

            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra6',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra6', str(query.message.chat.username)),callback_data="Extra6"),
                InlineKeyboardButton("Lengua propia: "+manejotextos.consultaStat("Lengua propia",str(query.message.chat.username)), callback_data="Lengua propia"),
                InlineKeyboardButton("Tasacion: "+manejotextos.consultaStat("Tasacion",str(query.message.chat.username)), callback_data="Tasacion"),
            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra7',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra7', str(query.message.chat.username)),callback_data="Extra7"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra10',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra10', str(query.message.chat.username)),callback_data="Extra10"),
                InlineKeyboardButton("Trepar: "+manejotextos.consultaStat("Trepar",str(query.message.chat.username)), callback_data="Trepar"),
            ],
            [
                InlineKeyboardButton("Ciencias ocultas: "+manejotextos.consultaStat("Ciencias ocultas",str(query.message.chat.username)), callback_data="Ciencias ocultas"),
                InlineKeyboardButton("Otras lenguas: "+manejotextos.consultaStat("Otras lenguas",str(query.message.chat.username)), callback_data="Otras lenguas"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra16',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra16', str(query.message.chat.username)),callback_data="Extra16"),
            ],
            [
                InlineKeyboardButton("Combatir", callback_data='Categoria'),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra11',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra11', str(query.message.chat.username)),callback_data="Extra11"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra17',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra17', str(query.message.chat.username)),callback_data="Extra17"),
            ],
            [
                InlineKeyboardButton("Pelea: "+manejotextos.consultaStat("Pelea",str(query.message.chat.username)), callback_data="Pelea"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra12',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra12', str(query.message.chat.username)),callback_data="Extra12"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra18',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra18', str(query.message.chat.username)),callback_data="Extra18"),           
            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra8',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra8', str(query.message.chat.username)),callback_data="Extra8"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra13',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra13', str(query.message.chat.username)),callback_data="Extra13"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra19',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra19', str(query.message.chat.username)),callback_data="Extra19"),                
            ],
            [
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra9',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra9', str(query.message.chat.username)),callback_data="Extra9"),
                InlineKeyboardButton("Mecanica: "+manejotextos.consultaStat("Mecanica",str(query.message.chat.username)), callback_data="Mecanica"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra20',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra20', str(query.message.chat.username)),callback_data="Extra20"),
            ],
            [
                InlineKeyboardButton("Conducir automovil: "+manejotextos.consultaStat("Conducir automovil",str(query.message.chat.username)), callback_data="Conducir automovil"),
                InlineKeyboardButton("Medicina: "+manejotextos.consultaStat("Medicina",str(query.message.chat.username)), callback_data="Medicina"),
                InlineKeyboardButton( manejotextos.consultanombreStatextra('Extra21',str(query.message.chat.username))+': '+ manejotextos.consultavalorStatextra('Extra21', str(query.message.chat.username)),callback_data="Extra21"),
            ],
            [InlineKeyboardButton("Salir", callback_data='salir')],
            
        ]
          
    reply_markup = InlineKeyboardMarkup(keyboard1)

    query.edit_message_text('Ficha de '+manejotextos.consultaStat("Jugador",str(query.message.chat.username))+'. Investigador: <b>'+manejotextos.consultaStat("Nombre",str(query.message.chat.username))+'</b>', reply_markup=reply_markup,parse_mode=telegram.ParseMode.HTML )
    return NIVELMOSTRARFICHA

def salir1(update,context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text('Hasta pronto')
    return END

def stop(update,context):

    update.message.reply_html('Hasta pronto, <b>'+update.message.chat.username+'</b>')
    return END

def takechatid(update,context):

    
    
    update.message.reply_text(text='El codigo de este chat es: ')
    update.message.reply_text(update.message.chat.id)
    update.message.reply_text(text='Guarda el código usando /putchatid en tu chat privado con el bot y los acciones de tu personaje se enviarán al chat del código')
    #print(update)
    #context.bot.send_message(chat_id=-1001691926925,text=update.message.chat.id )

def putchatid(update,context):

    #/putchatid xxx

    try:    
        chatid=update.message.text[11:]
        ficha=update.message.chat.username
        chatidantiguo=manejotextos.consultaStat('Chatid',str(ficha) )
        
	    

        if chatid:
            
            try:
                context.bot.send_message(chat_id=chatid,text= '<b>'+ficha+'</b> ha vinculado su personaje <b>'+ manejotextos.consultaStat('Nombre',str(ficha) ) +'</b> a este grupo.', parse_mode=telegram.ParseMode.HTML )
                manejotextos.cambioStat('Chatid',chatid,ficha)
                update.message.reply_text(text='Personaje vinculado al chat con ID: '+ str(chatid))
                if chatidantiguo: 
                    
                    context.bot.send_message(chat_id=chatidantiguo,text= '<b>'+ficha+'</b> ha desvinculado su personaje <b>'+ manejotextos.consultaStat('Nombre',str(ficha) ) +'</b> de este grupo.', parse_mode=telegram.ParseMode.HTML )
            except telegram.error.BadRequest: update.message.reply_text(text='No existe un chat con ese ID')
        else: update.message.reply_text(text='Error. Asegurate de escribir el chat ID a continuación del comando.')

    except IndexError: update.message.reply_text(text='Error. Asegurate de escribir el chat ID a continuación del comando.')
    
    
    
def roll(update,context):

    #/roll 1d100
    #context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(query.message.chat.username) ),text= '<b>'+query.message.chat.username+'</b> ha disminuido su '+ manejotextos.consultanombreStatextra(Memoriacomando,str(query.message.chat.username))+' a '+ manejotextos.consultavalorStatextra(Memoriacomando,str(query.message.chat.username)), parse_mode=telegram.ParseMode.HTML )

    #try:    
        peticiontirada=update.message.text[6:]
        ficha=update.message.chat.username
        print (peticiontirada)
	    
        if peticiontirada:
            tirada=diceroller.roll(peticiontirada)
            print(tirada)
            print(tirada[0])
            print(tirada[1])
            print(tirada[2])
            update.message.reply_text(text='Tirada de : '+ str(tirada[0])+'. Dados: '+ str(tirada[2])+ '. Valor final: '+str(tirada[1]))
            context.bot.send_message(chat_id=manejotextos.consultaStat('Chatid',str(ficha)), text= '<b>'+manejotextos.consultaStat('Nombre',ficha)+'</b> ha sacado '+ str(tirada[1])+' en '+ tirada[0], parse_mode=telegram.ParseMode.HTML )
        
        else: update.message.reply_text(text='Error. Asegurate de escribir la tirada (2d100, 3d4+2, 1d6+20...) a continuación del comando.')
    #except IndexError: update.message.reply_text(text='Error. aaaaaAsegurate de escribir la tirada (2d100, 3d4+2, 1d6+20...) a continuación del comando.')    
    

if __name__ == '__main__':

    updater = Updater(token='5308416540:AAFckErbGKJaUFmaNDiLM7V2YoOcsN73EdE', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    
    dp.add_handler(CommandHandler('takechatid',takechatid))

    dp.add_handler(CommandHandler('putchatid',putchatid))

    dp.add_handler(CommandHandler('roll', roll))


    #Conversacion nueva ficha
    dp.add_handler(ConversationHandler(

        entry_points=[
            CommandHandler('nuevaficha', funcionesSetStatsFicha.existefichaInicio)
        ],

        states={
            funcionesSetStatsFicha.SETNombre: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setNombre)],
            funcionesSetStatsFicha.SETNuevaficha: [
                CallbackQueryHandler(funcionesSetStatsFicha.existefichacontinuacion, pattern='fichanueva'),
                CallbackQueryHandler(funcionesSetStatsFicha.salirficha, pattern='salir')
                ],
            funcionesSetStatsFicha.SETJugador: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setJugador)],
            funcionesSetStatsFicha.SETOcupacion: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setOcupacion)],
            funcionesSetStatsFicha.SETGenero: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setGenero)],
            funcionesSetStatsFicha.SETEdad: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setEdad)],
            funcionesSetStatsFicha.SETLugardeRESIdeNCIA: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setLugarderesidencia)],
            funcionesSetStatsFicha.SETLugardeNACIMIENTO: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setLugardenacimiento)],
            funcionesSetStatsFicha.SETFuerza: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setFuerza)],
            funcionesSetStatsFicha.SETDestreza: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setDestreza)],
            funcionesSetStatsFicha.SETPoder: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setPoder)],
            funcionesSetStatsFicha.SETConstitucion: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setConstitucion)],
            funcionesSetStatsFicha.SETApariencia: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setApariencia)],
            funcionesSetStatsFicha.SETEducacion: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setEducacion)],
            funcionesSetStatsFicha.SETTamano: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setTamano)],
            funcionesSetStatsFicha.SETInteligencia: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setInteligencia)],
            funcionesSetStatsFicha.SETIdea: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setIdea)],
            funcionesSetStatsFicha.SETMovimiento: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setMovimiento)],
            funcionesSetStatsFicha.SETVida: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setVida)],
            funcionesSetStatsFicha.SETVidaMAXIMO: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setVidamaximo)],
            funcionesSetStatsFicha.SETMagia: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setMagia)],
            funcionesSetStatsFicha.SETMagiaMAXIMO: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setMagiamaximo)],
            funcionesSetStatsFicha.SETCordura: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setCordura)],
            funcionesSetStatsFicha.SETCorduraINICIAL: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setCordurainicial)],
            funcionesSetStatsFicha.SETCorduraMAXIMA: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setCorduramaxima)],
            funcionesSetStatsFicha.SETSuerte: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setSuerte)],
            funcionesSetStatsFicha.SETAntropologia: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setAntropologia)],
            funcionesSetStatsFicha.SETArmaCORTA: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setArmacorta)],
            funcionesSetStatsFicha.SETFusilEscopeta: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setFusilEscopeta)],
            funcionesSetStatsFicha.SETArqueologia: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setArqueologia)],
            #funcionesSetStatsFicha.SETArteArteSANIA: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setArteArtesania)],
            funcionesSetStatsFicha.SETBuscarLIBROS: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setBuscarlibros)],
            funcionesSetStatsFicha.SETCerrajeria: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setCerrajeria)],
            funcionesSetStatsFicha.SETCharlataneria: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setCharlataneria)],
            #funcionesSetStatsFicha.SETCiencia: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setCiencia)],
            funcionesSetStatsFicha.SETCienciaSOCULTAS: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setCienciasocultas)],
            #funcionesSetStatsFicha.SETCOMBATIR: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setcombatir)],
            funcionesSetStatsFicha.SETPelea: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setPelea)],
            funcionesSetStatsFicha.SETConducirautomovil: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setConducirautomovil)],
            funcionesSetStatsFicha.SETConducirmaquinaria: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setConducirmaquinaria)],
            funcionesSetStatsFicha.SETContabilidad: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setContabilidad)],
            funcionesSetStatsFicha.SETCredito: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setCredito)],
            funcionesSetStatsFicha.SETDerecho: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setDerecho)],
            funcionesSetStatsFicha.SETDescubrir: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setDescubrir)],
            funcionesSetStatsFicha.SETDisfrazarse: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setDisfrazarse)],
            funcionesSetStatsFicha.SETElectricidad: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setElectricidad)],
            funcionesSetStatsFicha.SETEncanto: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setEncanto)],
            funcionesSetStatsFicha.SETEquitacion: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setEquitacion)],
            funcionesSetStatsFicha.SETEscuchar: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setEscuchar)],
            funcionesSetStatsFicha.SETEsquivar: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setEsquivar)],
            funcionesSetStatsFicha.SETHistoria: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setHistoria)],
            funcionesSetStatsFicha.SETIntimidar: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setIntimidar)],
            funcionesSetStatsFicha.SETJuegodeMANOS: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setJuegodemanos)],
            funcionesSetStatsFicha.SETLanzar: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setLanzar)],
            #funcionesSetStatsFicha.SETLenguaPROPIA: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setLenguapropia)],
            #funcionesSetStatsFicha.SETOtraslenguas: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setOtraslenguas)],
            funcionesSetStatsFicha.SETMecanica: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setMecanica)],
            funcionesSetStatsFicha.SETMedicina: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setMedicina)],
            funcionesSetStatsFicha.SETMitosdeCthulhu: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setMitosdeCthulhu)],
            funcionesSetStatsFicha.SETNadar: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setNadar)],
            funcionesSetStatsFicha.SETNaturaleza: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setNaturaleza)],
            funcionesSetStatsFicha.SETOrientarse: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setOrientarse)],
            funcionesSetStatsFicha.SETPersuasion: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setPersuasion)],
            #funcionesSetStatsFicha.SETPilotar: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setPilotar)],
            funcionesSetStatsFicha.SETPrimerosauxilios: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setPrimerosauxilios)],
            funcionesSetStatsFicha.SETPsicoanalisis: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setPsicoanalisis)],
            funcionesSetStatsFicha.SETPsicologia: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setPsicologia)],
            funcionesSetStatsFicha.SETSaltar: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setSaltar)],
            funcionesSetStatsFicha.SETSeguirrastros: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setSeguirrastros)],
            funcionesSetStatsFicha.SETSigilo: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setSigilo)],
            #funcionesSetStatsFicha.SETSupervivencia: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setSupervivencia)],
            funcionesSetStatsFicha.SETTasacion: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setTasacion)],
            funcionesSetStatsFicha.SETTrepar: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setTrepar)],
            #funcionesSetStatsFicha.SETArma1: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setArma1)],
            #funcionesSetStatsFicha.SETArma2: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setArma2)],
            #funcionesSetStatsFicha.SETArma3: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setArma3)],
            #funcionesSetStatsFicha.SETArma4: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setArma4)],
            funcionesSetStatsFicha.SETBonificaciondano: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setBonificaciondano)],
            funcionesSetStatsFicha.SETCorpulencia: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setCorpulencia)],
            funcionesSetStatsFicha.SETDescripcionpersonal: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setDescripcionpersonal)],
            funcionesSetStatsFicha.SETIdeologiacreencias: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setIdeologiacreencias)],
            funcionesSetStatsFicha.SETAllegados: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setAllegados)],
            funcionesSetStatsFicha.SETLugarESsignificativos: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setLugaressignificativos)],
            funcionesSetStatsFicha.SETPosesionespreciadas: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setPosesionespreciadas)],
            funcionesSetStatsFicha.SETRasgos: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setRasgos)],
            funcionesSetStatsFicha.SETLesionesycicatrices: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setLesionesycicatrices)],
            funcionesSetStatsFicha.SETFobiasymanias: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setFobiasymanias)],
            funcionesSetStatsFicha.SETTomosarcanos: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setTomosarcanos)],
            funcionesSetStatsFicha.SETEncuentrosconentidadesextranas: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setEncuentrosconentidadesextranas)],
            funcionesSetStatsFicha.SETEquipo: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setEquipo)],
            funcionesSetStatsFicha.SETNiveldegasto: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setNiveldegasto)],
            funcionesSetStatsFicha.SETDinero: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setDinero)],
            funcionesSetStatsFicha.SETBienes: [MessageHandler(Filters.text & (~Filters.command), funcionesSetStatsFicha.setBienes)],
            
        }, 

        fallbacks=[CommandHandler('salir', funcionesSetStatsFicha.salirficha)]

    ))

    #Convesacion mostrar ficha stats
    dp.add_handler(ConversationHandler(

        entry_points=[
            CommandHandler('ficha', mostrarficha1)
        ],

        states={
            NIVELMOSTRARFICHA: [
                CallbackQueryHandler(menustatnumerico, pattern="Fuerza|Destreza|Poder|Constitucion|Apariencia|Educacion|Tamano|Inteligencia|Idea|Movimiento|Vida|Vida maximo|Magia|Magia maximo|Cordura|Cordura inicial|Cordura maxima|Suerte|Antropologia|Arma corta|Fusil/Escopeta|Arqueologia|Arte/Artesania|Buscar libros|Cerrajeria|Charlataneria|Ciencia|Ciencias ocultas|Pelea|Conducir automovil|Conducir maquinaria|Contabilidad|Credito|Derecho|Descubrir|Disfrazarse|Electricidad|Encanto|Equitacion|Escuchar|Esquivar|Historia|Intimidar|Juego de manos|Lanzar|Lengua propia|Otras lenguas|Mecanica|Medicina|Mitos de Cthulhu|Nadar|Naturaleza|Orientarse|Persuasion|Pilotar|Primeros auxilios|Psicoanalisis|Psicologia|Saltar|Seguir rastros|Sigilo|Supervivencia|Tasacion|Trepar"),
                CallbackQueryHandler(menustatextra,pattern="Extra1|Extra2|Extra3|Extra4|Extra5|Extra6|Extra7|Extra8|Extra9|Extra10|Extra11|Extra12|Extra13|Extra14|Extra15|Extra16|Extra17|Extra18|Extra19|Extra20|Extra21")
            ],
            NIVELSTATNUMERICO: [
                
                CallbackQueryHandler(tiradabonificada, pattern="tiradabonificada"),
                CallbackQueryHandler(tiradapenalizada, pattern="tiradapenalizada"),
                CallbackQueryHandler(tirada, pattern="tirada"),
                CallbackQueryHandler(menucambiarstatnumerico, pattern="menucambiarstatnumerico"),
                CallbackQueryHandler(atrasmostrarficha1, pattern="atrasmostrarficha1"),

            ],   

            NIVELCAMBIARSTATNUMERICO: [

                CallbackQueryHandler(sumar1stat, pattern="sumar1stat"),
                CallbackQueryHandler(sumar5stat, pattern="sumar5stat"),
                CallbackQueryHandler(restar1stat, pattern="restar1stat"),
                CallbackQueryHandler(restar5stat, pattern="restar5stat"),
                CallbackQueryHandler(atrasmostrarficha1, pattern="atrasmostrarficha1"),
            ],

            NIVELMENUSTATEXTRA: [

                CallbackQueryHandler(nombrarstatextra, pattern="nombrarstatextra"),
                CallbackQueryHandler(tiradabonificada, pattern="tiradabonificada"),
                CallbackQueryHandler(tiradapenalizada, pattern="tiradapenalizada"),
                CallbackQueryHandler(tirada, pattern="tirada"),
                CallbackQueryHandler(menucambiarstatextra, pattern="menucambiarstatextra"),
                CallbackQueryHandler(atrasmostrarficha1, pattern="atrasmostrarficha1"),
            ],

            NIVELDECISIONNOMBRESTATEXTRA:[
                MessageHandler(Filters.text,decisionnombrestatextra)
            ],

            NIVELMENUCAMBIARSTATEXTRA:[
                CallbackQueryHandler(sumar1statextra, pattern="sumar1statextra"),
                CallbackQueryHandler(sumar5statextra, pattern="sumar5statextra"),
                CallbackQueryHandler(restar1statextra, pattern="restar1statextra"),
                CallbackQueryHandler(restar5statextra, pattern="restar5statextra"),
                CallbackQueryHandler(atrasmostrarficha1, pattern="atrasmostrarficha1"),
            ]


        },

        fallbacks=[CommandHandler('salir', stop),CallbackQueryHandler(salir1, pattern="salir"),],
        allow_reentry=True
    ))


    updater.start_polling()
    updater.idle()
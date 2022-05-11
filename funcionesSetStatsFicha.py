import manejotextos
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackContext, InlineQueryHandler
from telegram import ChatAction, chataction, Update, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton

SETNombre=0
SETJugador=1
SETOcupacion=2
SETGenero=3
SETEdad=4
SETLugardeRESIdeNCIA=5
SETLugardeNACIMIENTO=6
SETFuerza=7
SETDestreza=8
SETPoder=9
SETConstitucion=10
SETApariencia=11
SETEducacion=12
SETTamano=13
SETInteligencia=14
SETIdea=15
SETMovimiento=16
SETVida=17
SETVidaMAXIMO=18
SETMagia=19
SETMagiaMAXIMO=20
SETCordura=21
SETCorduraINICIAL=22
SETCorduraMAXIMA=23
SETSuerte=24
SETAntropologia=25
SETArmaCORTA=26
SETFusilEscopeta=27
SETArqueologia=28
SETArteArteSANIA=29
SETBuscarLIBROS=30
SETCerrajeria=31
SETCharlataneria=32
SETCiencia=33
SETCienciaSOCULTAS=34
#SETCOMBATIR=35
SETPelea=36
SETConducirautomovil=37
SETConducirmaquinaria=38
SETContabilidad=39
SETCredito=40
SETDerecho=41
SETDescubrir=42
SETDisfrazarse=43
SETElectricidad=44
SETEncanto=45
SETEquitacion=46
SETEscuchar=47
SETEsquivar=48
SETHistoria=49
SETIntimidar=50
SETJuegodeMANOS=51
SETLanzar=52
SETLenguaPROPIA=53
SETOtraslenguas=54
SETMecanica=55
SETMedicina=56
SETMitosdeCthulhu=57
SETNadar=58
SETNaturaleza=59
SETOrientarse=60
SETPersuasion=61
SETPilotar=62
SETPrimerosauxilios=63
SETPsicoanalisis=64
SETPsicologia=65
SETSaltar=66
SETSeguirrastros=67
SETSigilo=68
SETSupervivencia=69
SETTasacion=70
SETTrepar=71
SETArma1=72
SETArma2=73
SETArma3=74
SETArma4=75
SETBonificaciondano=76
SETCorpulencia=77
SETDescripcionpersonal=78
SETIdeologiacreencias=79
SETAllegados=80
SETLugarESsignificativos=81
SETPosesionespreciadas=82
SETRasgos=83
SETLesionesycicatrices=84
SETFobiasymanias=85
SETTomosarcanos=86
SETEncuentrosconentidadesextranas=87
SETEquipo=88
SETNiveldegasto=89
SETDinero=90
SETBienes=91
SETNuevaficha=92
END=-1


def existefichaInicio( update, context):

	try:
		ficha=open(str(update.message.chat.username)+".txt", 'r')
		ficha.close()
		keyboard = [
        [
            InlineKeyboardButton("Crear ficha nueva", callback_data='fichanueva'),
            InlineKeyboardButton("Salir", callback_data='salir'),
        ]]
        
		reply_markup = InlineKeyboardMarkup(keyboard)
		update.message.reply_markdown_v2('Hola ' +update.message.chat.first_name+'\.\nYa tienes una ficha creada para *La llamada de Cthulhu 7ª Ed\.*\nPuedes cambiar los stats directamente desde la ficha, pero también puedes cambiarlos aquí uno a uno\n¿Deseas continuar?\.', reply_markup=reply_markup)
		return SETNuevaficha
		#Estructura de botones SI NO	
	
	except FileNotFoundError:

		ficha=open('LLDC mayusculas.txt', 'r')
		stats=ficha.readlines()
		ficha.close()
		ficha=open(str(update.message.chat.username)+".txt", 'w+')
		for line in stats:
			ficha.write(line)
		ficha.close()
		update.message.reply_markdown_v2('Hola ' +update.message.chat.first_name+', ¿qué tal? Vamos a crear una ficha de personaje para *La llamada de Cthulhu 7ª Ed\.*\n *Reglas*: Para todo el proceso de la ficha, de momento, cuando quieras escribir un punto \(\.\) debes poner la barra diagonal contraria a esta / justo antes del punto\. Las tildes se pueden usar pero se verán mal después')
		update.message.reply_markdown_v2('Escribe el *Nombre* de tu personaje:')
		
		return SETNombre
		

def existefichacontinuacion(update,context):
		
		print(update)
		context.bot.send_message(chat_id=update.effective_chat.id, text='*Reglas*: Para todo el proceso de la ficha, de momento, cuando quieras escribir un punto \(\.\) debes poner la barra diagonal contraria a esta / justo antes del punto\. Las tildes se pueden usar pero se verán mal después\.\nEscribe el *Nombre* de tu personaje:',parse_mode='MARKDOWNV2' )
		
		return SETNombre

def salirficha(update,context):
		context.bot.send_message(chat_id=update.effective_chat.id, text='Saliendo del creador de fichas\.\.\.',parse_mode='MARKDOWNV2' )
		return END

def setNombre( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Nombre',texto,ficha)
	update.message.reply_markdown_v2('*Nombre*: '+ manejotextos.consultaStat('Nombre', ficha) + '\nAhora escribe tu *Jugador*:' )
	return SETJugador



def setJugador( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Jugador',texto,ficha)
	update.message.reply_markdown_v2('*Jugador*: '+ manejotextos.consultaStat('Jugador', ficha) + '\nAhora escribe tu *Ocupacion*:' )
	return SETOcupacion



def setOcupacion( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Ocupacion',texto,ficha)
	update.message.reply_markdown_v2('*Ocupacion*: '+ manejotextos.consultaStat('Ocupacion', ficha) + '\nAhora escribe tu *Genero*:' )
	return SETGenero



def setGenero( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Genero',texto,ficha)
	update.message.reply_markdown_v2('*Genero*: '+ manejotextos.consultaStat('Genero', ficha) + '\nAhora escribe tu *Edad*:' )
	return SETEdad



def setEdad( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Edad',texto,ficha)
	update.message.reply_markdown_v2('*Edad*: '+ manejotextos.consultaStat('Edad', ficha) + '\nAhora escribe tu *Lugar de residencia*:' )
	return SETLugardeRESIdeNCIA



def setLugarderesidencia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Lugar de residencia',texto,ficha)
	update.message.reply_markdown_v2('*Lugar de residencia*: '+ manejotextos.consultaStat('Lugar de residencia', ficha) + '\nAhora escribe tu *Lugar de nacimiento*:' )
	return SETLugardeNACIMIENTO



def setLugardenacimiento( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Lugar de nacimiento',texto,ficha)
	update.message.reply_markdown_v2('*Lugar de nacimiento*: '+ manejotextos.consultaStat('Lugar de nacimiento', ficha) + '\nAhora escribe tu *Fuerza*:' )
	return SETFuerza



def setFuerza( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Fuerza',texto,ficha)
	update.message.reply_markdown_v2('*Fuerza*: '+ manejotextos.consultaStat('Fuerza', ficha) + '\nAhora escribe tu *Destreza*:' )
	return SETDestreza



def setDestreza( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Destreza',texto,ficha)
	update.message.reply_markdown_v2('*Destreza*: '+ manejotextos.consultaStat('Destreza', ficha) + '\nAhora escribe tu *Poder*:' )
	return SETPoder



def setPoder( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Poder',texto,ficha)
	update.message.reply_markdown_v2('*Poder*: '+ manejotextos.consultaStat('Poder', ficha) + '\nAhora escribe tu *Constitucion*:' )
	return SETConstitucion



def setConstitucion( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Constitucion',texto,ficha)
	update.message.reply_markdown_v2('*Constitucion*: '+ manejotextos.consultaStat('Constitucion', ficha) + '\nAhora escribe tu *Apariencia*:' )
	return SETApariencia



def setApariencia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Apariencia',texto,ficha)
	update.message.reply_markdown_v2('*Apariencia*: '+ manejotextos.consultaStat('Apariencia', ficha) + '\nAhora escribe tu *Educacion*:' )
	return SETEducacion



def setEducacion( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Educacion',texto,ficha)
	update.message.reply_markdown_v2('*Educacion*: '+ manejotextos.consultaStat('Educacion', ficha) + '\nAhora escribe tu *Tamaño*:' )
	return SETTamano



def setTamano( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Tamano',texto,ficha)
	update.message.reply_markdown_v2('*Tamaño*: '+ manejotextos.consultaStat('Tamano', ficha) + '\nAhora escribe tu *Inteligencia*:' )
	return SETInteligencia



def setInteligencia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Inteligencia',texto,ficha)
	update.message.reply_markdown_v2('*Inteligencia*: '+ manejotextos.consultaStat('Inteligencia', ficha) + '\nAhora escribe tu *Idea*:' )
	return SETIdea



def setIdea( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Idea',texto,ficha)
	update.message.reply_markdown_v2('*Idea*: '+ manejotextos.consultaStat('Idea', ficha) + '\nAhora escribe tu *Movimiento*:' )
	return SETMovimiento



def setMovimiento( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Movimiento',texto,ficha)
	update.message.reply_markdown_v2('*Movimiento*: '+ manejotextos.consultaStat('Movimiento', ficha) + '\nAhora escribe tu *Vida*:' )
	return SETVida



def setVida( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Vida',texto,ficha)
	update.message.reply_markdown_v2('*Vida*: '+ manejotextos.consultaStat('Vida', ficha) + '\nAhora escribe tu *Vida maximo*:' )
	return SETVidaMAXIMO



def setVidamaximo( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Vida maximo',texto,ficha)
	update.message.reply_markdown_v2('*Vida maximo*: '+ manejotextos.consultaStat('Vida maximo', ficha) + '\nAhora escribe tu *Magia*:' )
	return SETMagia



def setMagia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Magia',texto,ficha)
	update.message.reply_markdown_v2('*Magia*: '+ manejotextos.consultaStat('Magia', ficha) + '\nAhora escribe tu *Magia maximo*:' )
	return SETMagiaMAXIMO



def setMagiamaximo( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Magia maximo',texto,ficha)
	update.message.reply_markdown_v2('*Magia maximo*: '+ manejotextos.consultaStat('Magia maximo', ficha) + '\nAhora escribe tu *Cordura*:' )
	return SETCordura



def setCordura( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Cordura',texto,ficha)
	update.message.reply_markdown_v2('*Cordura*: '+ manejotextos.consultaStat('Cordura', ficha) + '\nAhora escribe tu *Cordura inicial*:' )
	return SETCorduraINICIAL



def setCordurainicial( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Cordura inicial',texto,ficha)
	update.message.reply_markdown_v2('*Cordura inicial*: '+ manejotextos.consultaStat('Cordura inicial', ficha) + '\nAhora escribe tu *Cordura maxima*:' )
	return SETCorduraMAXIMA



def setCorduramaxima( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Cordura maxima',texto,ficha)
	update.message.reply_markdown_v2('*Cordura maxima*: '+ manejotextos.consultaStat('Cordura maxima', ficha) + '\nAhora escribe tu *Suerte*:' )
	return SETSuerte



def setSuerte( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Suerte',texto,ficha)
	update.message.reply_markdown_v2('*Suerte*: '+ manejotextos.consultaStat('Suerte', ficha) + '\nAhora escribe tu *Antropologia*:' )
	return SETAntropologia



def setAntropologia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Antropologia',texto,ficha)
	update.message.reply_markdown_v2('*Antropologia*: '+ manejotextos.consultaStat('Antropologia', ficha) + '\nAhora escribe tu *Armacorta*:' )
	return SETArmaCORTA



def setArmacorta( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Arma corta',texto,ficha)
	update.message.reply_markdown_v2('*Arma corta*: '+ manejotextos.consultaStat('Arma corta', ficha) + '\nAhora escribe tu *Fusiles/copeta*:' )
	return SETFusilEscopeta



def setFusilEscopeta( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Fusil/Escopeta',texto,ficha)
	update.message.reply_markdown_v2('*Fusil/Escopeta*: '+ manejotextos.consultaStat('Fusil/Escopeta', ficha) + '\nAhora escribe tu *Arqueologia*:' )
	return SETArqueologia



def setArqueologia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Arqueologia',texto,ficha)
	update.message.reply_markdown_v2('*Arqueologia*: '+ manejotextos.consultaStat('Arqueologia', ficha) + '\nAhora escribe tu *Buscar libros*:' )
	return SETBuscarLIBROS



""" def setArteArtesania( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Arte/Artesania',texto,ficha)
	update.message.reply_markdown_v2('*Arte/Artesania*: '+ manejotextos.consultaStat('Arte/Artesania', ficha) + '\nAhora escribe tu *Buscar libros*:' )
	return SETBuscarLIBROS """



def setBuscarlibros( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Buscar libros',texto,ficha)
	update.message.reply_markdown_v2('*Buscar libros*: '+ manejotextos.consultaStat('Buscar libros', ficha) + '\nAhora escribe tu *Cerrajeria*:' )
	return SETCerrajeria



def setCerrajeria( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Cerrajeria',texto,ficha)
	update.message.reply_markdown_v2('*Cerrajeria*: '+ manejotextos.consultaStat('Cerrajeria', ficha) + '\nAhora escribe tu *Charlataneria*:' )
	return SETCharlataneria



def setCharlataneria( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Charlataneria',texto,ficha)
	update.message.reply_markdown_v2('*Charlataneria*: '+ manejotextos.consultaStat('Charlataneria', ficha) + '\nAhora escribe tu *Ciencias ocultas*:' )
	return SETCienciaSOCULTAS



""" def setCiencia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Ciencia',texto,ficha)
	update.message.reply_markdown_v2('*Ciencia*: '+ manejotextos.consultaStat('Ciencia', ficha) + '\nAhora escribe tu *Ciencias ocultas*:' )
	return SETCienciaSOCULTAS """



def setCienciasocultas( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Ciencias ocultas',texto,ficha)
	update.message.reply_markdown_v2('*Ciencias ocultas*: '+ manejotextos.consultaStat('Ciencias ocultas', ficha) + '\nAhora escribe tu *Pelea*:' )
	return SETPelea
	""" return SETCOMBATIR """


""" def setcombatir( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('combatir',texto,ficha)
	update.message.reply_markdown_v2('*combatir*: '+ manejotextos.consultaStat('combatir', ficha) + '\nAhora escribe tu *Pelea*:' )
	return SETPelea """



def setPelea( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Pelea',texto,ficha)
	update.message.reply_markdown_v2('*Pelea*: '+ manejotextos.consultaStat('Pelea', ficha) + '\nAhora escribe tu *Conducir automovil*:' )
	return SETConducirautomovil



def setConducirautomovil( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Conducir automovil',texto,ficha)
	update.message.reply_markdown_v2('*Conducir automovil*: '+ manejotextos.consultaStat('Conducir automovil', ficha) + '\nAhora escribe tu *Conducir maquinaria*:' )
	return SETConducirmaquinaria



def setConducirmaquinaria( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Conducir maquinaria',texto,ficha)
	update.message.reply_markdown_v2('*Conducir maquinaria*: '+ manejotextos.consultaStat('Conducir maquinaria', ficha) + '\nAhora escribe tu *Contabilidad*:' )
	return SETContabilidad



def setContabilidad( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Contabilidad',texto,ficha)
	update.message.reply_markdown_v2('*Contabilidad*: '+ manejotextos.consultaStat('Contabilidad', ficha) + '\nAhora escribe tu *Credito*:' )
	return SETCredito



def setCredito( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Credito',texto,ficha)
	update.message.reply_markdown_v2('*Credito*: '+ manejotextos.consultaStat('Credito', ficha) + '\nAhora escribe tu *Derecho*:' )
	return SETDerecho



def setDerecho( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Derecho',texto,ficha)
	update.message.reply_markdown_v2('*Derecho*: '+ manejotextos.consultaStat('Derecho', ficha) + '\nAhora escribe tu *Descubrir*:' )
	return SETDescubrir



def setDescubrir( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Descubrir',texto,ficha)
	update.message.reply_markdown_v2('*Descubrir*: '+ manejotextos.consultaStat('Descubrir', ficha) + '\nAhora escribe tu *Disfrazarse*:' )
	return SETDisfrazarse



def setDisfrazarse( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Disfrazarse',texto,ficha)
	update.message.reply_markdown_v2('*Disfrazarse*: '+ manejotextos.consultaStat('Disfrazarse', ficha) + '\nAhora escribe tu *Electricidad*:' )
	return SETElectricidad



def setElectricidad( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Electricidad',texto,ficha)
	update.message.reply_markdown_v2('*Electricidad*: '+ manejotextos.consultaStat('Electricidad', ficha) + '\nAhora escribe tu *Encanto*:' )
	return SETEncanto



def setEncanto( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Encanto',texto,ficha)
	update.message.reply_markdown_v2('*Encanto*: '+ manejotextos.consultaStat('Encanto', ficha) + '\nAhora escribe tu *Equitacion*:' )
	return SETEquitacion



def setEquitacion( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Equitacion',texto,ficha)
	update.message.reply_markdown_v2('*Equitacion*: '+ manejotextos.consultaStat('Equitacion', ficha) + '\nAhora escribe tu *Escuchar*:' )
	return SETEscuchar



def setEscuchar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Escuchar',texto,ficha)
	update.message.reply_markdown_v2('*Escuchar*: '+ manejotextos.consultaStat('Escuchar', ficha) + '\nAhora escribe tu *Esquivar*:' )
	return SETEsquivar



def setEsquivar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Esquivar',texto,ficha)
	update.message.reply_markdown_v2('*Esquivar*: '+ manejotextos.consultaStat('Esquivar', ficha) + '\nAhora escribe tu *Historia*:' )
	return SETHistoria



def setHistoria( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Historia',texto,ficha)
	update.message.reply_markdown_v2('*Historia*: '+ manejotextos.consultaStat('Historia', ficha) + '\nAhora escribe tu *Intimidar*:' )
	return SETIntimidar



def setIntimidar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Intimidar',texto,ficha)
	update.message.reply_markdown_v2('*Intimidar*: '+ manejotextos.consultaStat('Intimidar', ficha) + '\nAhora escribe tu *Juego de manos*:' )
	return SETJuegodeMANOS



def setJuegodemanos( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Juego de manos',texto,ficha)
	update.message.reply_markdown_v2('*Juego de manos*: '+ manejotextos.consultaStat('Juego de manos', ficha) + '\nAhora escribe tu *Lanzar*:' )
	return SETLanzar



def setLanzar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Lanzar',texto,ficha)
	update.message.reply_markdown_v2('*Lanzar*: '+ manejotextos.consultaStat('Lanzar', ficha) + '\nAhora escribe tu *Mecanica*:' )
	return SETMecanica



""" def setLenguapropia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Lengua propia',texto,ficha)
	update.message.reply_markdown_v2('*Lengua propia*: '+ manejotextos.consultaStat('Lengua propia', ficha) + '\nAhora escribe tu *Otras lenguas*:' )
	return SETOtraslenguas



def setOtraslenguas( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Otras lenguas',texto,ficha)
	update.message.reply_markdown_v2('*Otras lenguas*: '+ manejotextos.consultaStat('Otras lenguas', ficha) + '\nAhora escribe tu *Mecanica*:' )
	return SETMecanica """



def setMecanica( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Mecanica',texto,ficha)
	update.message.reply_markdown_v2('*Mecanica*: '+ manejotextos.consultaStat('Mecanica', ficha) + '\nAhora escribe tu *Medicina*:' )
	return SETMedicina



def setMedicina( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Medicina',texto,ficha)
	update.message.reply_markdown_v2('*Medicina*: '+ manejotextos.consultaStat('Medicina', ficha) + '\nAhora escribe tu *M̴͕͍͕͋̾͝i̵͔͚͓͊̈́͝t̸̫͉͍͒̚̚o̵͇͖̽̒s̴͖͚͌͐͘ d̵̢͙͓̾̿̕e̸̻͑͑̚͜ c̸̡͔̙͊͆̈́t̴͓̻̦͊̾̿h̴̢̡̘̓̕͝u̸͍̼̞̔́͝l̵̢̝͎̿͋u̸̟͉̠̐͘͝La*:' )
	return SETMitosdeCthulhu



def setMitosdeCthulhu( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Mitos de Cthulhu',texto,ficha)
	update.message.reply_markdown_v2('*M̴͕͍͕͋̾͝i̵͔͚͓͊̈́͝t̸̫͉͍͒̚̚o̵͇͖̽̒s̴͖͚͌͐͘ d̵̢͙͓̾̿̕e̸̻͑͑̚͜ c̸̡͔̙͊͆̈́t̴͓̻̦͊̾̿h̴̢̡̘̓̕͝u̸͍̼̞̔́͝l̵̢̝͎̿͋u̸̟͉̠̐͘͝La*: '+ manejotextos.consultaStat('Mitos de Cthulhu', ficha) + '\nAhora escribe tu *Nadar*:' )
	return SETNadar



def setNadar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Nadar',texto,ficha)
	update.message.reply_markdown_v2('*Nadar*: '+ manejotextos.consultaStat('Nadar', ficha) + '\nAhora escribe tu *Naturaleza*:' )
	return SETNaturaleza



def setNaturaleza( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Naturaleza',texto,ficha)
	update.message.reply_markdown_v2('*Naturaleza*: '+ manejotextos.consultaStat('Naturaleza', ficha) + '\nAhora escribe tu *Orientarse*:' )
	return SETOrientarse



def setOrientarse( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Orientarse',texto,ficha)
	update.message.reply_markdown_v2('*Orientarse*: '+ manejotextos.consultaStat('Orientarse', ficha) + '\nAhora escribe tu *Persuasion*:' )
	return SETPersuasion



def setPersuasion( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Persuasion',texto,ficha)
	update.message.reply_markdown_v2('*Persuasion*: '+ manejotextos.consultaStat('Persuasion', ficha) + '\nAhora escribe tu *Primeros auxilios*:' )
	return SETPrimerosauxilios



""" def setPilotar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Pilotar',texto,ficha)
	update.message.reply_markdown_v2('*Pilotar*: '+ manejotextos.consultaStat('Pilotar', ficha) + '\nAhora escribe tu *Primeros auxilios*:' )
	return SETPrimerosauxilios """



def setPrimerosauxilios( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Primeros auxilios',texto,ficha)
	update.message.reply_markdown_v2('*Primeros auxilios*: '+ manejotextos.consultaStat('Primeros auxilios', ficha) + '\nAhora escribe tu *Psicoanalisis*:' )
	return SETPsicoanalisis



def setPsicoanalisis( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Psicoanalisis',texto,ficha)
	update.message.reply_markdown_v2('*Psicoanalisis*: '+ manejotextos.consultaStat('Psicoanalisis', ficha) + '\nAhora escribe tu *Psicologia*:' )
	return SETPsicologia



def setPsicologia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Psicologia',texto,ficha)
	update.message.reply_markdown_v2('*Psicologia*: '+ manejotextos.consultaStat('Psicologia', ficha) + '\nAhora escribe tu *Saltar*:' )
	return SETSaltar



def setSaltar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Saltar',texto,ficha)
	update.message.reply_markdown_v2('*Saltar*: '+ manejotextos.consultaStat('Saltar', ficha) + '\nAhora escribe tu *Seguir rastros*:' )
	return SETSeguirrastros



def setSeguirrastros( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Seguir rastros',texto,ficha)
	update.message.reply_markdown_v2('*Seguir rastros*: '+ manejotextos.consultaStat('Seguir rastros', ficha) + '\nAhora escribe tu *Sigilo*:' )
	return SETSigilo



def setSigilo( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Sigilo',texto,ficha)
	update.message.reply_markdown_v2('*Sigilo*: '+ manejotextos.consultaStat('Sigilo', ficha) + '\nAhora escribe tu *Tasación*:' )
	return SETTasacion



""" def setSupervivencia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Supervivencia',texto,ficha)
	update.message.reply_markdown_v2('*Supervivencia*: '+ manejotextos.consultaStat('Supervivencia', ficha) + '\nAhora escribe tu *Tasacion*:' )
	return SETTasacion """



def setTasacion( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Tasacion',texto,ficha)
	update.message.reply_markdown_v2('*Tasacion*: '+ manejotextos.consultaStat('Tasacion', ficha) + '\nAhora escribe tu *Trepar*:' )
	return SETTrepar



def setTrepar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Trepar',texto,ficha)
	update.message.reply_markdown_v2('*Trepar*: '+ manejotextos.consultaStat('Trepar', ficha) + '\nAhora escribe tu *Bonificación de daño*:' )
	return SETBonificaciondano



""" def setArma1( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Arma 1',texto,ficha)
	update.message.reply_markdown_v2('*Arma 1*: '+ manejotextos.consultaStat('Arma 1', ficha) + '\nAhora escribe tu *Arma 2*:' )
	return SETArma2



def setArma2( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Arma 2',texto,ficha)
	update.message.reply_markdown_v2('*Arma 2*: '+ manejotextos.consultaStat('Arma 2', ficha) + '\nAhora escribe tu *Arma 3*:' )
	return SETArma3



def setArma3( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Arma 3',texto,ficha)
	update.message.reply_markdown_v2('*Arma 3*: '+ manejotextos.consultaStat('Arma 3', ficha) + '\nAhora escribe tu *Arma 4*:' )
	return SETArma4



def setArma4( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Arma 4',texto,ficha)
	update.message.reply_markdown_v2('*Arma 4*: '+ manejotextos.consultaStat('Arma 4', ficha) + '\nAhora escribe tu *Bonificacion daño*:' )
	return SETBonificaciondano """



def setBonificaciondano( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Bonificacion dano',texto,ficha)
	update.message.reply_markdown_v2('*Bonificacion daño*: '+ manejotextos.consultaStat('Bonificacion dano', ficha) + '\nAhora escribe tu *Corpulencia*:' )
	return SETCorpulencia



def setCorpulencia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Corpulencia',texto,ficha)
	update.message.reply_markdown_v2('*Corpulencia*: '+ manejotextos.consultaStat('Corpulencia', ficha) + '\nAhora escribe tu *Descripcion personal*:' )
	return SETDescripcionpersonal



def setDescripcionpersonal( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Descripcion personal',texto,ficha)
	update.message.reply_markdown_v2('*Descripcion personal*: '+ manejotextos.consultaStat('Descripcion personal', ficha) + '\nAhora escribe tu *Ideologia/creencias*:' )
	return SETIdeologiacreencias



def setIdeologiacreencias( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Ideologia creencias',texto,ficha)
	update.message.reply_markdown_v2('*Ideologia creencias*: '+ manejotextos.consultaStat('Ideologia creencias', ficha) + '\nAhora escribe tu *Allegados*:' )
	return SETAllegados



def setAllegados( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Allegados',texto,ficha)
	update.message.reply_markdown_v2('*Allegados*: '+ manejotextos.consultaStat('Allegados', ficha) + '\nAhora escribe tu *Lugares significativos*:' )
	return SETLugarESsignificativos



def setLugaressignificativos( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Lugares significativos',texto,ficha)
	update.message.reply_markdown_v2('*Lugares significativos*: '+ manejotextos.consultaStat('Lugares significativos', ficha) + '\nAhora escribe tu *Posesiones preciadas*:' )
	return SETPosesionespreciadas



def setPosesionespreciadas( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Posesiones preciadas',texto,ficha)
	update.message.reply_markdown_v2('*Posesiones preciadas*: '+ manejotextos.consultaStat('Posesiones preciadas', ficha) + '\nAhora escribe tu *Rasgos*:' )
	return SETRasgos



def setRasgos( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Rasgos',texto,ficha)
	update.message.reply_markdown_v2('*Rasgos*: '+ manejotextos.consultaStat('Rasgos', ficha) + '\nAhora escribe tu *Lesiones y cicatrices*:' )
	return SETLesionesycicatrices



def setLesionesycicatrices( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Lesiones y cicatrices',texto,ficha)
	update.message.reply_markdown_v2('*Lesiones y cicatrices*: '+ manejotextos.consultaStat('Lesiones y cicatrices', ficha) + '\nAhora escribe tu *Fobias y manias*:' )
	return SETFobiasymanias



def setFobiasymanias( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Fobias y manias',texto,ficha)
	update.message.reply_markdown_v2('*Fobias y manias*: '+ manejotextos.consultaStat('Fobias y manias', ficha) + '\nAhora escribe tu *Tomos arcanos, hechizos y artefactos*:' )
	return SETTomosarcanos



def setTomosarcanos( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Tomos arcanos, hechizos y artefactos',texto,ficha)
	update.message.reply_markdown_v2('*Tomos arcanos, hechizos y artefactos*: '+ manejotextos.consultaStat('Tomos arcanos, hechizos y artefactos', ficha) + '\nAhora escribe tu *Encuentros con entidades extrañas*:' )
	return SETEncuentrosconentidadesextranas



def setEncuentrosconentidadesextranas( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Encuentros con entidades extranas',texto,ficha)
	update.message.reply_markdown_v2('*Encuentros con entidades extrañas*: '+ manejotextos.consultaStat('Encuentros con entidades extranas', ficha) + '\nAhora escribe tu *Equipo*:' )
	return SETEquipo



def setEquipo( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Equipo',texto,ficha)
	update.message.reply_markdown_v2('*Equipo*: '+ manejotextos.consultaStat('Equipo', ficha) + '\nAhora escribe tu *Nivel de gasto*:' )
	return SETNiveldegasto



def setNiveldegasto( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Nivel de gasto',texto,ficha)
	update.message.reply_markdown_v2('*Nivel de gasto*: '+ manejotextos.consultaStat('Nivel de gasto', ficha) + '\nAhora escribe tu *Dinero*:' )
	return SETDinero



def setDinero( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Dinero',texto,ficha)
	update.message.reply_markdown_v2('*Dinero*: '+ manejotextos.consultaStat('Dinero', ficha) + '\nAhora escribe tu *Bienes*:' )
	return SETBienes


def setBienes( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Bienes',texto,ficha)
	update.message.reply_markdown_v2('*Bienes*: '+ manejotextos.consultaStat('Bienes', ficha) + '\n\n\n' )
	update.message.reply_markdown_v2('Muchas gracias por rellenar su ficha de investigador\.\nQue disfrute perdiendo su Cordura' )
	return END




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
		update.message.reply_html('Hola ' +update.message.chat.first_name+'.\nYa tienes una ficha creada para <b>La llamada de Cthulhu 7ª Ed.</b>\nPuedes cambiar los stats directamente desde la ficha, pero también puedes cambiarlos aquí uno a uno\n¿Deseas continuar?.', reply_markup=reply_markup)
		return SETNuevaficha
			
	
	except FileNotFoundError:

		ficha=open('LLDC mayusculas.txt', 'r')
		stats=ficha.readlines()
		ficha.close()
		ficha=open(str(update.message.chat.username)+".txt", 'w+')
		for line in stats:
			ficha.write(line)
		ficha.close()
		update.message.reply_html('Hola ' +update.message.chat.first_name+', ¿qué tal? Vamos a crear una ficha de personaje para <b>La llamada de Cthulhu 7ª Ed.</b>\n')
		update.message.reply_html('Escribe el <b>Nombre</b> de tu personaje:')
		
		return SETNombre
		

def existefichacontinuacion(update,context):
		
		
		context.bot.send_message(chat_id=update.effective_chat.id, text='Escribe el <b>Nombre</b> de tu personaje:',parse_mode='HTML' )
		
		return SETNombre

def salirficha(update,context):
		context.bot.send_message(chat_id=update.effective_chat.id, text='Saliendo del creador de fichas...',parse_mode='HTML' )
		return END

def setNombre( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Nombre',texto,ficha)
	update.message.reply_html('<b>Nombre</b>: '+ manejotextos.consultaStat('Nombre', ficha) + '\nAhora escribe tu <b>Jugador</b>:' )
	return SETJugador



def setJugador( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Jugador',texto,ficha)
	update.message.reply_html('<b>Jugador</b>: '+ manejotextos.consultaStat('Jugador', ficha) + '\nAhora escribe tu <b>Ocupacion</b>:' )
	return SETOcupacion



def setOcupacion( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Ocupacion',texto,ficha)
	update.message.reply_html('<b>Ocupacion</b>: '+ manejotextos.consultaStat('Ocupacion', ficha) + '\nAhora escribe tu <b>Genero</b>:' )
	return SETGenero



def setGenero( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Genero',texto,ficha)
	update.message.reply_html('<b>Genero</b>: '+ manejotextos.consultaStat('Genero', ficha) + '\nAhora escribe tu <b>Edad</b>:' )
	return SETEdad



def setEdad( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Edad',texto,ficha)
	update.message.reply_html('<b>Edad</b>: '+ manejotextos.consultaStat('Edad', ficha) + '\nAhora escribe tu <b>Lugar de residencia</b>:' )
	return SETLugardeRESIdeNCIA



def setLugarderesidencia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Lugar de residencia',texto,ficha)
	update.message.reply_html('<b>Lugar de residencia</b>: '+ manejotextos.consultaStat('Lugar de residencia', ficha) + '\nAhora escribe tu <b>Lugar de nacimiento</b>:' )
	return SETLugardeNACIMIENTO



def setLugardenacimiento( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Lugar de nacimiento',texto,ficha)
	update.message.reply_html('<b>Lugar de nacimiento</b>: '+ manejotextos.consultaStat('Lugar de nacimiento', ficha) + '\nAhora escribe tu <b>Fuerza</b>:' )
	return SETFuerza



def setFuerza( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Fuerza',texto,ficha)
	update.message.reply_html('<b>Fuerza</b>: '+ manejotextos.consultaStat('Fuerza', ficha) + '\nAhora escribe tu <b>Destreza</b>:' )
	return SETDestreza



def setDestreza( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Destreza',texto,ficha)
	update.message.reply_html('<b>Destreza</b>: '+ manejotextos.consultaStat('Destreza', ficha) + '\nAhora escribe tu <b>Poder</b>:' )
	return SETPoder



def setPoder( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Poder',texto,ficha)
	update.message.reply_html('<b>Poder</b>: '+ manejotextos.consultaStat('Poder', ficha) + '\nAhora escribe tu <b>Constitucion</b>:' )
	return SETConstitucion



def setConstitucion( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Constitucion',texto,ficha)
	update.message.reply_html('<b>Constitucion</b>: '+ manejotextos.consultaStat('Constitucion', ficha) + '\nAhora escribe tu <b>Apariencia</b>:' )
	return SETApariencia



def setApariencia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Apariencia',texto,ficha)
	update.message.reply_html('<b>Apariencia</b>: '+ manejotextos.consultaStat('Apariencia', ficha) + '\nAhora escribe tu <b>Educacion</b>:' )
	return SETEducacion



def setEducacion( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Educacion',texto,ficha)
	update.message.reply_html('<b>Educacion</b>: '+ manejotextos.consultaStat('Educacion', ficha) + '\nAhora escribe tu <b>Tamaño</b>:' )
	return SETTamano



def setTamano( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Tamano',texto,ficha)
	update.message.reply_html('<b>Tamaño</b>: '+ manejotextos.consultaStat('Tamano', ficha) + '\nAhora escribe tu <b>Inteligencia</b>:' )
	return SETInteligencia



def setInteligencia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Inteligencia',texto,ficha)
	update.message.reply_html('<b>Inteligencia</b>: '+ manejotextos.consultaStat('Inteligencia', ficha) + '\nAhora escribe tu <b>Idea</b>:' )
	return SETIdea



def setIdea( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Idea',texto,ficha)
	update.message.reply_html('<b>Idea</b>: '+ manejotextos.consultaStat('Idea', ficha) + '\nAhora escribe tu <b>Movimiento</b>:' )
	return SETMovimiento



def setMovimiento( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Movimiento',texto,ficha)
	update.message.reply_html('<b>Movimiento</b>: '+ manejotextos.consultaStat('Movimiento', ficha) + '\nAhora escribe tu <b>Vida</b>:' )
	return SETVida



def setVida( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Vida',texto,ficha)
	update.message.reply_html('<b>Vida</b>: '+ manejotextos.consultaStat('Vida', ficha) + '\nAhora escribe tu <b>Vida maximo</b>:' )
	return SETVidaMAXIMO



def setVidamaximo( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Vida maximo',texto,ficha)
	update.message.reply_html('<b>Vida maximo</b>: '+ manejotextos.consultaStat('Vida maximo', ficha) + '\nAhora escribe tu <b>Magia</b>:' )
	return SETMagia



def setMagia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Magia',texto,ficha)
	update.message.reply_html('<b>Magia</b>: '+ manejotextos.consultaStat('Magia', ficha) + '\nAhora escribe tu <b>Magia maximo</b>:' )
	return SETMagiaMAXIMO



def setMagiamaximo( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Magia maximo',texto,ficha)
	update.message.reply_html('<b>Magia maximo</b>: '+ manejotextos.consultaStat('Magia maximo', ficha) + '\nAhora escribe tu <b>Cordura</b>:' )
	return SETCordura



def setCordura( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Cordura',texto,ficha)
	update.message.reply_html('<b>Cordura</b>: '+ manejotextos.consultaStat('Cordura', ficha) + '\nAhora escribe tu <b>Cordura inicial</b>:' )
	return SETCorduraINICIAL



def setCordurainicial( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Cordura inicial',texto,ficha)
	update.message.reply_html('<b>Cordura inicial</b>: '+ manejotextos.consultaStat('Cordura inicial', ficha) + '\nAhora escribe tu <b>Cordura maxima</b>:' )
	return SETCorduraMAXIMA



def setCorduramaxima( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Cordura maxima',texto,ficha)
	update.message.reply_html('<b>Cordura maxima</b>: '+ manejotextos.consultaStat('Cordura maxima', ficha) + '\nAhora escribe tu <b>Suerte</b>:' )
	return SETSuerte



def setSuerte( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Suerte',texto,ficha)
	update.message.reply_html('<b>Suerte</b>: '+ manejotextos.consultaStat('Suerte', ficha) + '\nAhora escribe tu <b>Antropologia</b>:' )
	return SETAntropologia



def setAntropologia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Antropologia',texto,ficha)
	update.message.reply_html('<b>Antropologia</b>: '+ manejotextos.consultaStat('Antropologia', ficha) + '\nAhora escribe tu <b>Armacorta</b>:' )
	return SETArmaCORTA



def setArmacorta( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Arma corta',texto,ficha)
	update.message.reply_html('<b>Arma corta</b>: '+ manejotextos.consultaStat('Arma corta', ficha) + '\nAhora escribe tu <b>Fusiles/copeta</b>:' )
	return SETFusilEscopeta



def setFusilEscopeta( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Fusil/Escopeta',texto,ficha)
	update.message.reply_html('<b>Fusil/Escopeta</b>: '+ manejotextos.consultaStat('Fusil/Escopeta', ficha) + '\nAhora escribe tu <b>Arqueologia</b>:' )
	return SETArqueologia



def setArqueologia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Arqueologia',texto,ficha)
	update.message.reply_html('<b>Arqueologia</b>: '+ manejotextos.consultaStat('Arqueologia', ficha) + '\nAhora escribe tu <b>Buscar libros</b>:' )
	return SETBuscarLIBROS



""" def setArteArtesania( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Arte/Artesania',texto,ficha)
	update.message.reply_html('<b>Arte/Artesania</b>: '+ manejotextos.consultaStat('Arte/Artesania', ficha) + '\nAhora escribe tu <b>Buscar libros</b>:' )
	return SETBuscarLIBROS """



def setBuscarlibros( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Buscar libros',texto,ficha)
	update.message.reply_html('<b>Buscar libros</b>: '+ manejotextos.consultaStat('Buscar libros', ficha) + '\nAhora escribe tu <b>Cerrajeria</b>:' )
	return SETCerrajeria



def setCerrajeria( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Cerrajeria',texto,ficha)
	update.message.reply_html('<b>Cerrajeria</b>: '+ manejotextos.consultaStat('Cerrajeria', ficha) + '\nAhora escribe tu <b>Charlataneria</b>:' )
	return SETCharlataneria



def setCharlataneria( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Charlataneria',texto,ficha)
	update.message.reply_html('<b>Charlataneria</b>: '+ manejotextos.consultaStat('Charlataneria', ficha) + '\nAhora escribe tu <b>Ciencias ocultas</b>:' )
	return SETCienciaSOCULTAS



""" def setCiencia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Ciencia',texto,ficha)
	update.message.reply_html('<b>Ciencia</b>: '+ manejotextos.consultaStat('Ciencia', ficha) + '\nAhora escribe tu <b>Ciencias ocultas</b>:' )
	return SETCienciaSOCULTAS """



def setCienciasocultas( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Ciencias ocultas',texto,ficha)
	update.message.reply_html('<b>Ciencias ocultas</b>: '+ manejotextos.consultaStat('Ciencias ocultas', ficha) + '\nAhora escribe tu <b>Pelea</b>:' )
	return SETPelea
	""" return SETCOMBATIR """


""" def setcombatir( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('combatir',texto,ficha)
	update.message.reply_html('<b>combatir</b>: '+ manejotextos.consultaStat('combatir', ficha) + '\nAhora escribe tu <b>Pelea</b>:' )
	return SETPelea """



def setPelea( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Pelea',texto,ficha)
	update.message.reply_html('<b>Pelea</b>: '+ manejotextos.consultaStat('Pelea', ficha) + '\nAhora escribe tu <b>Conducir automovil</b>:' )
	return SETConducirautomovil



def setConducirautomovil( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Conducir automovil',texto,ficha)
	update.message.reply_html('<b>Conducir automovil</b>: '+ manejotextos.consultaStat('Conducir automovil', ficha) + '\nAhora escribe tu <b>Conducir maquinaria</b>:' )
	return SETConducirmaquinaria



def setConducirmaquinaria( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Conducir maquinaria',texto,ficha)
	update.message.reply_html('<b>Conducir maquinaria</b>: '+ manejotextos.consultaStat('Conducir maquinaria', ficha) + '\nAhora escribe tu <b>Contabilidad</b>:' )
	return SETContabilidad



def setContabilidad( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Contabilidad',texto,ficha)
	update.message.reply_html('<b>Contabilidad</b>: '+ manejotextos.consultaStat('Contabilidad', ficha) + '\nAhora escribe tu <b>Credito</b>:' )
	return SETCredito



def setCredito( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Credito',texto,ficha)
	update.message.reply_html('<b>Credito</b>: '+ manejotextos.consultaStat('Credito', ficha) + '\nAhora escribe tu <b>Derecho</b>:' )
	return SETDerecho



def setDerecho( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Derecho',texto,ficha)
	update.message.reply_html('<b>Derecho</b>: '+ manejotextos.consultaStat('Derecho', ficha) + '\nAhora escribe tu <b>Descubrir</b>:' )
	return SETDescubrir



def setDescubrir( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Descubrir',texto,ficha)
	update.message.reply_html('<b>Descubrir</b>: '+ manejotextos.consultaStat('Descubrir', ficha) + '\nAhora escribe tu <b>Disfrazarse</b>:' )
	return SETDisfrazarse



def setDisfrazarse( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Disfrazarse',texto,ficha)
	update.message.reply_html('<b>Disfrazarse</b>: '+ manejotextos.consultaStat('Disfrazarse', ficha) + '\nAhora escribe tu <b>Electricidad</b>:' )
	return SETElectricidad



def setElectricidad( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Electricidad',texto,ficha)
	update.message.reply_html('<b>Electricidad</b>: '+ manejotextos.consultaStat('Electricidad', ficha) + '\nAhora escribe tu <b>Encanto</b>:' )
	return SETEncanto



def setEncanto( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Encanto',texto,ficha)
	update.message.reply_html('<b>Encanto</b>: '+ manejotextos.consultaStat('Encanto', ficha) + '\nAhora escribe tu <b>Equitacion</b>:' )
	return SETEquitacion



def setEquitacion( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Equitacion',texto,ficha)
	update.message.reply_html('<b>Equitacion</b>: '+ manejotextos.consultaStat('Equitacion', ficha) + '\nAhora escribe tu <b>Escuchar</b>:' )
	return SETEscuchar



def setEscuchar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Escuchar',texto,ficha)
	update.message.reply_html('<b>Escuchar</b>: '+ manejotextos.consultaStat('Escuchar', ficha) + '\nAhora escribe tu <b>Esquivar</b>:' )
	return SETEsquivar



def setEsquivar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Esquivar',texto,ficha)
	update.message.reply_html('<b>Esquivar</b>: '+ manejotextos.consultaStat('Esquivar', ficha) + '\nAhora escribe tu <b>Historia</b>:' )
	return SETHistoria



def setHistoria( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Historia',texto,ficha)
	update.message.reply_html('<b>Historia</b>: '+ manejotextos.consultaStat('Historia', ficha) + '\nAhora escribe tu <b>Intimidar</b>:' )
	return SETIntimidar



def setIntimidar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Intimidar',texto,ficha)
	update.message.reply_html('<b>Intimidar</b>: '+ manejotextos.consultaStat('Intimidar', ficha) + '\nAhora escribe tu <b>Juego de manos</b>:' )
	return SETJuegodeMANOS



def setJuegodemanos( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Juego de manos',texto,ficha)
	update.message.reply_html('<b>Juego de manos</b>: '+ manejotextos.consultaStat('Juego de manos', ficha) + '\nAhora escribe tu <b>Lanzar</b>:' )
	return SETLanzar



def setLanzar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Lanzar',texto,ficha)
	update.message.reply_html('<b>Lanzar</b>: '+ manejotextos.consultaStat('Lanzar', ficha) + '\nAhora escribe tu <b>Mecanica</b>:' )
	return SETMecanica



""" def setLenguapropia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Lengua propia',texto,ficha)
	update.message.reply_html('<b>Lengua propia</b>: '+ manejotextos.consultaStat('Lengua propia', ficha) + '\nAhora escribe tu <b>Otras lenguas</b>:' )
	return SETOtraslenguas



def setOtraslenguas( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Otras lenguas',texto,ficha)
	update.message.reply_html('<b>Otras lenguas</b>: '+ manejotextos.consultaStat('Otras lenguas', ficha) + '\nAhora escribe tu <b>Mecanica</b>:' )
	return SETMecanica """



def setMecanica( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Mecanica',texto,ficha)
	update.message.reply_html('<b>Mecanica</b>: '+ manejotextos.consultaStat('Mecanica', ficha) + '\nAhora escribe tu <b>Medicina</b>:' )
	return SETMedicina



def setMedicina( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Medicina',texto,ficha)
	update.message.reply_html('<b>Medicina</b>: '+ manejotextos.consultaStat('Medicina', ficha) + '\nAhora escribe tu <b>M̴͕͍͕͋̾͝i̵͔͚͓͊̈́͝t̸̫͉͍͒̚̚o̵͇͖̽̒s̴͖͚͌͐͘ d̵̢͙͓̾̿̕e̸̻͑͑̚͜ c̸̡͔̙͊͆̈́t̴͓̻̦͊̾̿h̴̢̡̘̓̕͝u̸͍̼̞̔́͝l̵̢̝͎̿͋u̸̟͉̠̐͘͝La</b>:' )
	return SETMitosdeCthulhu



def setMitosdeCthulhu( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Mitos de Cthulhu',texto,ficha)
	update.message.reply_html('<b>M̴͕͍͕͋̾͝i̵͔͚͓͊̈́͝t̸̫͉͍͒̚̚o̵͇͖̽̒s̴͖͚͌͐͘ d̵̢͙͓̾̿̕e̸̻͑͑̚͜ c̸̡͔̙͊͆̈́t̴͓̻̦͊̾̿h̴̢̡̘̓̕͝u̸͍̼̞̔́͝l̵̢̝͎̿͋u̸̟͉̠̐͘͝La</b>: '+ manejotextos.consultaStat('Mitos de Cthulhu', ficha) + '\nAhora escribe tu <b>Nadar</b>:' )
	return SETNadar



def setNadar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Nadar',texto,ficha)
	update.message.reply_html('<b>Nadar</b>: '+ manejotextos.consultaStat('Nadar', ficha) + '\nAhora escribe tu <b>Naturaleza</b>:' )
	return SETNaturaleza



def setNaturaleza( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Naturaleza',texto,ficha)
	update.message.reply_html('<b>Naturaleza</b>: '+ manejotextos.consultaStat('Naturaleza', ficha) + '\nAhora escribe tu <b>Orientarse</b>:' )
	return SETOrientarse



def setOrientarse( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Orientarse',texto,ficha)
	update.message.reply_html('<b>Orientarse</b>: '+ manejotextos.consultaStat('Orientarse', ficha) + '\nAhora escribe tu <b>Persuasion</b>:' )
	return SETPersuasion



def setPersuasion( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Persuasion',texto,ficha)
	update.message.reply_html('<b>Persuasion</b>: '+ manejotextos.consultaStat('Persuasion', ficha) + '\nAhora escribe tu <b>Primeros auxilios</b>:' )
	return SETPrimerosauxilios



""" def setPilotar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Pilotar',texto,ficha)
	update.message.reply_html('<b>Pilotar</b>: '+ manejotextos.consultaStat('Pilotar', ficha) + '\nAhora escribe tu <b>Primeros auxilios</b>:' )
	return SETPrimerosauxilios """



def setPrimerosauxilios( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Primeros auxilios',texto,ficha)
	update.message.reply_html('<b>Primeros auxilios</b>: '+ manejotextos.consultaStat('Primeros auxilios', ficha) + '\nAhora escribe tu <b>Psicoanalisis</b>:' )
	return SETPsicoanalisis



def setPsicoanalisis( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Psicoanalisis',texto,ficha)
	update.message.reply_html('<b>Psicoanalisis</b>: '+ manejotextos.consultaStat('Psicoanalisis', ficha) + '\nAhora escribe tu <b>Psicologia</b>:' )
	return SETPsicologia



def setPsicologia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Psicologia',texto,ficha)
	update.message.reply_html('<b>Psicologia</b>: '+ manejotextos.consultaStat('Psicologia', ficha) + '\nAhora escribe tu <b>Saltar</b>:' )
	return SETSaltar



def setSaltar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Saltar',texto,ficha)
	update.message.reply_html('<b>Saltar</b>: '+ manejotextos.consultaStat('Saltar', ficha) + '\nAhora escribe tu <b>Seguir rastros</b>:' )
	return SETSeguirrastros



def setSeguirrastros( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Seguir rastros',texto,ficha)
	update.message.reply_html('<b>Seguir rastros</b>: '+ manejotextos.consultaStat('Seguir rastros', ficha) + '\nAhora escribe tu <b>Sigilo</b>:' )
	return SETSigilo



def setSigilo( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Sigilo',texto,ficha)
	update.message.reply_html('<b>Sigilo</b>: '+ manejotextos.consultaStat('Sigilo', ficha) + '\nAhora escribe tu <b>Tasación</b>:' )
	return SETTasacion



""" def setSupervivencia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Supervivencia',texto,ficha)
	update.message.reply_html('<b>Supervivencia</b>: '+ manejotextos.consultaStat('Supervivencia', ficha) + '\nAhora escribe tu <b>Tasacion</b>:' )
	return SETTasacion """



def setTasacion( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Tasacion',texto,ficha)
	update.message.reply_html('<b>Tasacion</b>: '+ manejotextos.consultaStat('Tasacion', ficha) + '\nAhora escribe tu <b>Trepar</b>:' )
	return SETTrepar



def setTrepar( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Trepar',texto,ficha)
	update.message.reply_html('<b>Trepar</b>: '+ manejotextos.consultaStat('Trepar', ficha) + '\nAhora escribe tu <b>Bonificación de daño</b>:' )
	return SETBonificaciondano



""" def setArma1( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Arma 1',texto,ficha)
	update.message.reply_html('<b>Arma 1</b>: '+ manejotextos.consultaStat('Arma 1', ficha) + '\nAhora escribe tu <b>Arma 2</b>:' )
	return SETArma2



def setArma2( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Arma 2',texto,ficha)
	update.message.reply_html('<b>Arma 2</b>: '+ manejotextos.consultaStat('Arma 2', ficha) + '\nAhora escribe tu <b>Arma 3</b>:' )
	return SETArma3



def setArma3( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Arma 3',texto,ficha)
	update.message.reply_html('<b>Arma 3</b>: '+ manejotextos.consultaStat('Arma 3', ficha) + '\nAhora escribe tu <b>Arma 4</b>:' )
	return SETArma4



def setArma4( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Arma 4',texto,ficha)
	update.message.reply_html('<b>Arma 4</b>: '+ manejotextos.consultaStat('Arma 4', ficha) + '\nAhora escribe tu <b>Bonificacion daño</b>:' )
	return SETBonificaciondano """



def setBonificaciondano( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Bonificacion dano',texto,ficha)
	update.message.reply_html('<b>Bonificacion daño</b>: '+ manejotextos.consultaStat('Bonificacion dano', ficha) + '\nAhora escribe tu <b>Corpulencia</b>:' )
	return SETCorpulencia



def setCorpulencia( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Corpulencia',texto,ficha)
	update.message.reply_html('<b>Corpulencia</b>: '+ manejotextos.consultaStat('Corpulencia', ficha) + '\nAhora escribe tu <b>Descripcion personal</b>:' )
	return SETDescripcionpersonal



def setDescripcionpersonal( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Descripcion personal',texto,ficha)
	update.message.reply_html('<b>Descripcion personal</b>: '+ manejotextos.consultaStat('Descripcion personal', ficha) + '\nAhora escribe tu <b>Ideologia/creencias</b>:' )
	return SETIdeologiacreencias



def setIdeologiacreencias( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Ideologia creencias',texto,ficha)
	update.message.reply_html('<b>Ideologia creencias</b>: '+ manejotextos.consultaStat('Ideologia creencias', ficha) + '\nAhora escribe tu <b>Allegados</b>:' )
	return SETAllegados



def setAllegados( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Allegados',texto,ficha)
	update.message.reply_html('<b>Allegados</b>: '+ manejotextos.consultaStat('Allegados', ficha) + '\nAhora escribe tu <b>Lugares significativos</b>:' )
	return SETLugarESsignificativos



def setLugaressignificativos( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Lugares significativos',texto,ficha)
	update.message.reply_html('<b>Lugares significativos</b>: '+ manejotextos.consultaStat('Lugares significativos', ficha) + '\nAhora escribe tu <b>Posesiones preciadas</b>:' )
	return SETPosesionespreciadas



def setPosesionespreciadas( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Posesiones preciadas',texto,ficha)
	update.message.reply_html('<b>Posesiones preciadas</b>: '+ manejotextos.consultaStat('Posesiones preciadas', ficha) + '\nAhora escribe tu <b>Rasgos</b>:' )
	return SETRasgos



def setRasgos( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Rasgos',texto,ficha)
	update.message.reply_html('<b>Rasgos</b>: '+ manejotextos.consultaStat('Rasgos', ficha) + '\nAhora escribe tu <b>Lesiones y cicatrices</b>:' )
	return SETLesionesycicatrices



def setLesionesycicatrices( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Lesiones y cicatrices',texto,ficha)
	update.message.reply_html('<b>Lesiones y cicatrices</b>: '+ manejotextos.consultaStat('Lesiones y cicatrices', ficha) + '\nAhora escribe tu <b>Fobias y manias</b>:' )
	return SETFobiasymanias



def setFobiasymanias( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Fobias y manias',texto,ficha)
	update.message.reply_html('<b>Fobias y manias</b>: '+ manejotextos.consultaStat('Fobias y manias', ficha) + '\nAhora escribe tu <b>Tomos arcanos, hechizos y artefactos</b>:' )
	return SETTomosarcanos



def setTomosarcanos( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Tomos arcanos, hechizos y artefactos',texto,ficha)
	update.message.reply_html('<b>Tomos arcanos, hechizos y artefactos</b>: '+ manejotextos.consultaStat('Tomos arcanos, hechizos y artefactos', ficha) + '\nAhora escribe tu <b>Encuentros con entidades extrañas</b>:' )
	return SETEncuentrosconentidadesextranas



def setEncuentrosconentidadesextranas( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Encuentros con entidades extranas',texto,ficha)
	update.message.reply_html('<b>Encuentros con entidades extrañas</b>: '+ manejotextos.consultaStat('Encuentros con entidades extranas', ficha) + '\nAhora escribe tu <b>Equipo</b>:' )
	return SETEquipo



def setEquipo( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Equipo',texto,ficha)
	update.message.reply_html('<b>Equipo</b>: '+ manejotextos.consultaStat('Equipo', ficha) + '\nAhora escribe tu <b>Nivel de gasto</b>:' )
	return SETNiveldegasto



def setNiveldegasto( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Nivel de gasto',texto,ficha)
	update.message.reply_html('<b>Nivel de gasto</b>: '+ manejotextos.consultaStat('Nivel de gasto', ficha) + '\nAhora escribe tu <b>Dinero</b>:' )
	return SETDinero



def setDinero( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Dinero',texto,ficha)
	update.message.reply_html('<b>Dinero</b>: '+ manejotextos.consultaStat('Dinero', ficha) + '\nAhora escribe tu <b>Bienes</b>:' )
	return SETBienes


def setBienes( update, context):

	texto=update.message.text
	ficha=update.message.chat.username
	manejotextos.cambioStat('Bienes',texto,ficha)
	update.message.reply_html('<b>Bienes</b>: '+ manejotextos.consultaStat('Bienes', ficha) + '\n\n\n' )
	update.message.reply_html('Muchas gracias por rellenar su ficha de investigador.\nQue disfrute perdiendo su Cordura' )
	return END




import telebot
import schedule
import time

# Reemplaza 'TOKEN' con tu token de bot proporcionado por BotFather
TOKEN = '7482945080:AAHdBPrgQz5hzMG3i0KhL5Ry-EYGRHgZ2G4'
bot = telebot.TeleBot(TOKEN)

# Diccionario para almacenar el estado de cada cargador
cargadores_estado = {
    'cargador1': 'libre',
    'cargador2': 'libre',
    'cargador3': 'libre'
}

# Emoticonos para representar los estados
emojis = {
    'libre': '🟢',
    'ocupado': '🔴',
    'fuera de servicio': '❌'
}

# Manejador para el comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hola! Soy un bot que te da el estado de los cargadores de Puerto Venecia. "
                          "Para conocer más sobre los cargadores, usa el comando /estado.")

# Manejador para el comando /estado
@bot.message_handler(commands=['estado'])
def show_chargers(message):
    bot.reply_to(message, "Estos son los cargadores disponibles:\n"
                          "- Cargador 1: Estado actual - {} {} \n"
                          "- Cargador 2: Estado actual - {} {} \n"
                          "- Cargador 3: Estado actual - {} {} \n"
                          "Para más detalles sobre un cargador, usa el comando /cargadorX donde X es el número del cargador."
                          .format(cargadores_estado['cargador1'], emojis[cargadores_estado['cargador1']],
                                  cargadores_estado['cargador2'], emojis[cargadores_estado['cargador2']],
                                  cargadores_estado['cargador3'], emojis[cargadores_estado['cargador3']]))

# Manejador para el comando /ayuda
@bot.message_handler(commands=['ayuda'])
def ayuda(message):
    bot.reply_to(message, "Estos son los comandos disponibles:\n"
                          "/start - Iniciar el bot\n"
                          "/estado - Mostrar los cargadores disponibles y su estado\n"
                          "/cargador1 - Detalles del Cargador 1\n"
                          "/cargador2 - Detalles del Cargador 2\n"
                          "/cargador3 - Detalles del Cargador 3\n"
                          "/libre1, /ocupado1, /fueraservicio1 - Cambiar estado de Cargador 1\n"
                          "/libre2, /ocupado2, /fueraservicio2 - Cambiar estado de Cargador 2\n"
                          "/libre3, /ocupado3, /fueraservicio3 - Cambiar estado de Cargador 3\n")

# Manejadores para comandos específicos de cada cargador
@bot.message_handler(commands=['cargador1'])
def charger1_info(message):
    bot.reply_to(message, "Información en construcción.")

@bot.message_handler(commands=['cargador2'])
def charger2_info(message):
    bot.reply_to(message, "Información en construcción.")

@bot.message_handler(commands=['cargador3'])
def charger3_info(message):
    bot.reply_to(message, "Información en construcción.")

# Manejadores para cambiar el estado de los cargadores
@bot.message_handler(commands=['libre1'])
def set_libre_cargador1(message):
    update_estado('cargador1', 'libre')
    bot.reply_to(message, "Estado del Cargador 1 actualizado a Libre.")

@bot.message_handler(commands=['ocupado1'])
def set_ocupado_cargador1(message):
    update_estado('cargador1', 'ocupado')
    bot.reply_to(message, "Estado del Cargador 1 actualizado a Ocupado.")

@bot.message_handler(commands=['fueraservicio1'])
def set_fuera_servicio_cargador1(message):
    update_estado('cargador1', 'fuera de servicio')
    bot.reply_to(message, "Estado del Cargador 1 actualizado a Fuera de Servicio.")

@bot.message_handler(commands=['libre2'])
def set_libre_cargador2(message):
    update_estado('cargador2', 'libre')
    bot.reply_to(message, "Estado del Cargador 2 actualizado a Libre.")

@bot.message_handler(commands=['ocupado2'])
def set_ocupado_cargador2(message):
    update_estado('cargador2', 'ocupado')
    bot.reply_to(message, "Estado del Cargador 2 actualizado a Ocupado.")

@bot.message_handler(commands=['fueraservicio2'])
def set_fuera_servicio_cargador2(message):
    update_estado('cargador2', 'fuera de servicio')
    bot.reply_to(message, "Estado del Cargador 2 actualizado a Fuera de Servicio.")

@bot.message_handler(commands=['libre3'])
def set_libre_cargador3(message):
    update_estado('cargador3', 'libre')
    bot.reply_to(message, "Estado del Cargador 3 actualizado a Libre.")

@bot.message_handler(commands=['ocupado3'])
def set_ocupado_cargador3(message):
    update_estado('cargador3', 'ocupado')
    bot.reply_to(message, "Estado del Cargador 3 actualizado a Ocupado.")

@bot.message_handler(commands=['fueraservicio3'])
def set_fuera_servicio_cargador3(message):
    update_estado('cargador3', 'fuera de servicio')
    bot.reply_to(message, "Estado del Cargador 3 actualizado a Fuera de Servicio.")

# Función para actualizar el estado de un cargador
def update_estado(cargador, estado):
    # Verificamos si el cargador existe en el diccionario de estados
    if cargador in cargadores_estado:
        cargadores_estado[cargador] = estado
    else:
        print(f"Error: Cargador '{cargador}' no encontrado en la lista de cargadores.")

# Función para ejecutar la actualización automática cada 30 minutos
def actualizar_estado_automaticamente():
    update_estado('cargador1', obtener_estado_aleatorio())
    update_estado('cargador2', obtener_estado_aleatorio())
    update_estado('cargador3', obtener_estado_aleatorio())
    print("Estados actualizados automáticamente.")

# Función auxiliar para simular estados aleatorios (solo para ejemplo)
import random
def obtener_estado_aleatorio():
    estados_posibles = ['libre', 'ocupado', 'fuera de servicio']
    return random.choice(estados_posibles)

# Programación de la tarea para ejecutarse cada 30 minutos
schedule.every(30).minutes.do(actualizar_estado_automaticamente)

# Función para iniciar el bot y el ciclo de actualización automática
def main():
    # Iniciar el bot en un hilo separado
    bot.polling()

    # Ciclo para la actualización automática
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()



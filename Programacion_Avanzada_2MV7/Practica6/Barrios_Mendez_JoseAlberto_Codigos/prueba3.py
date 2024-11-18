import sys, pyfirmata, time, random
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi
from PyQt6.QtCore import pyqtSignal, QObject, QThread, QTimer

import inspect
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

# Configuración de los pines
pin_botones = [7, 6, 2, 4]  # Pines de los botones
pin_leds = [12, 11, 10, 9]  # Pines de los LEDs
pin_altavoz = 3  # Pin del altavoz

# Inicialización de la placa Arduino
board = pyfirmata.Arduino('COM8')
it = pyfirmata.util.Iterator(board)
it.start()
servo = board.get_pin('d:5:s')  # s para servo
servo.write(0)
time.sleep(1)

# Configuración de los pines
for pin in pin_leds:
    board.digital[pin].mode = pyfirmata.OUTPUT

for pin in pin_botones:
    board.digital[pin].mode = pyfirmata.INPUT

board.digital[pin_altavoz].mode = pyfirmata.PWM
class ThreadSimon5(QThread): #Jugador 1 y2
    turno = pyqtSignal(str)
    eliminado = pyqtSignal(str)
    ganador = pyqtSignal(str)
    bandera = True

    def run(self):

        # Variables globales
        secuencia = []
        secuencia_jugador = []
        acierto = True

        # Lista de jugadores
        jugadores = ["Jugador 1", "Jugador 2"]

        # Función para generar una nueva secuencia y seleccionar un jugador aleatorio
        def generar_secuencia():
            global jugador_actual
            secuencia.append(random.choice(pin_leds))
            jugador_actual = random.choice(jugadores)
            # print(f"Turno del {jugador_actual}:")
            self.turno.emit(jugador_actual)
            # Movimiento del servo según el jugador seleccionado
            if jugador_actual == "Jugador 1":
                servo.write(0)
            elif jugador_actual == "Jugador 2":
                servo.write(45)

        # Función para reproducir la secuencia
        def reproducir_secuencia():
            for pin in secuencia:
                board.digital[pin].write(1)
                board.digital[pin_altavoz].write(0.5)
                time.sleep(0.5)
                board.digital[pin].write(0)
                board.digital[pin_altavoz].write(0)
                time.sleep(0.5)

        # Función para hacer parpadear los LEDs cuando el jugador acierta
        def parpadear_leds():
            for _ in range(2):
                for pin in pin_leds:
                    board.digital[pin].write(1)
                time.sleep(0.3)
                for pin in pin_leds:
                    board.digital[pin].write(0)
                time.sleep(0.3)

        # Función para encender todos los LEDs en escalera
        def encender_en_escalera():
            for _ in range(3):  # Encender en escalera tres veces
                for i in range(len(pin_leds)):
                    board.digital[pin_leds[i]].write(1)
                    time.sleep(0.1)
                for i in range(len(pin_leds)):
                    board.digital[pin_leds[i]].write(0)
                    time.sleep(0.1)

        # Función para manejar el error
        def manejar_error():
            for pin in pin_leds:
                board.digital[pin].write(1)
            board.digital[pin_altavoz].write(0.7)  # Cambio de tono para indicar error
            time.sleep(1)
            for pin in pin_leds:
                board.digital[pin].write(0)
            board.digital[pin_altavoz].write(0)
            # Reiniciar el juego y encender en escalera
            secuencia.clear()  # Limpiar la secuencia actual
            secuencia_jugador.clear()  # Limpiar la secuencia del jugador
            encender_en_escalera()  # Encender LEDs en escalera

        # Bucle principal
        while self.bandera:
            if len(jugadores) > 1:
                if not secuencia:
                    generar_secuencia()
                    reproducir_secuencia()

            for i, pin in enumerate(pin_botones):
                if board.digital[pin].read():
                    secuencia_jugador.append(pin_leds[i])
                    board.digital[pin_leds[i]].write(1)
                    board.digital[pin_altavoz].write(0.5)
                    time.sleep(0.5)
                    board.digital[pin_leds[i]].write(0)
                    board.digital[pin_altavoz].write(0)
                    time.sleep(0.5)
                    # Verificar la secuencia del jugador en cada paso
                    if secuencia_jugador != secuencia[:len(secuencia_jugador)]:
                        # print(f"¡{jugador_actual} ha cometido un error! Eliminado del juego.")
                        self.eliminado.emit(jugador_actual)
                        jugadores.remove(jugador_actual)
                        if len(jugadores) == 1:  # Si queda un jugador
                            # print(f"¡{jugadores[0]} ha ganado!")
                            self.ganador.emit(jugadores[0])
                            exit()
                        else:
                            manejar_error()
                        break

            # Verificar si el jugador ha completado la secuencia
            if secuencia_jugador == secuencia:
                secuencia_jugador = []
                if len(jugadores) > 1:
                    generar_secuencia()
                parpadear_leds()  # Parpadear LEDs si el jugador acierta
                reproducir_secuencia()

    def detener(self):
        self.bandera = False

class ThreadSimon4(QThread): #juagodres 1,2,3
    turno = pyqtSignal(str)
    eliminado = pyqtSignal(str)
    ganador = pyqtSignal(str)
    bandera = True

    def run(self):

        # Variables globales
        secuencia = []
        secuencia_jugador = []
        acierto = True

        # Lista de jugadores
        jugadores = ["Jugador 1", "Jugador 2", "Jugador 3"]

        # Función para generar una nueva secuencia y seleccionar un jugador aleatorio
        def generar_secuencia():
            global jugador_actual
            secuencia.append(random.choice(pin_leds))
            jugador_actual = random.choice(jugadores)
            self.turno.emit(jugador_actual)
            # Movimiento del servo según el jugador seleccionado
            if jugador_actual == "Jugador 1":
                servo.write(0)
            elif jugador_actual == "Jugador 2":
                servo.write(45)
            elif jugador_actual == "Jugador 3":
                servo.write(90)

                # Función para reproducir la secuencia

        def reproducir_secuencia():
            for pin in secuencia:
                board.digital[pin].write(1)
                board.digital[pin_altavoz].write(0.5)
                time.sleep(0.5)
                board.digital[pin].write(0)
                board.digital[pin_altavoz].write(0)
                time.sleep(0.5)

            # Función para hacer parpadear los LEDs cuando el jugador acierta

        def parpadear_leds():
            for _ in range(2):
                for pin in pin_leds:
                    board.digital[pin].write(1)
                time.sleep(0.3)
                for pin in pin_leds:
                    board.digital[pin].write(0)
                time.sleep(0.3)

                # Función para encender todos los LEDs en escalera

        def encender_en_escalera():
            for _ in range(3):  # Encender en escalera tres veces
                for i in range(len(pin_leds)):
                    board.digital[pin_leds[i]].write(1)
                    time.sleep(0.1)
                for i in range(len(pin_leds)):
                    board.digital[pin_leds[i]].write(0)
                    time.sleep(0.1)

            # Función para manejar el error

        def manejar_error():
            for pin in pin_leds:
                board.digital[pin].write(1)
            board.digital[pin_altavoz].write(0.7)  # Cambio de tono para indicar error
            time.sleep(1)
            for pin in pin_leds:
                board.digital[pin].write(0)
            board.digital[pin_altavoz].write(0)
            # Reiniciar el juego y encender en escalera
            secuencia.clear()  # Limpiar la secuencia actual
            secuencia_jugador.clear()  # Limpiar la secuencia del jugador
            encender_en_escalera()  # Encender LEDs en escalera

            # Bucle principal
        while self.bandera:
            if len(jugadores) > 1:
                if not secuencia:
                    generar_secuencia()
                    reproducir_secuencia()

            for i, pin in enumerate(pin_botones):
                if board.digital[pin].read():
                    secuencia_jugador.append(pin_leds[i])
                    board.digital[pin_leds[i]].write(1)
                    board.digital[pin_altavoz].write(0.5)
                    time.sleep(0.5)
                    board.digital[pin_leds[i]].write(0)
                    board.digital[pin_altavoz].write(0)
                    time.sleep(0.5)
                    # Verificar la secuencia del jugador en cada paso
                    if secuencia_jugador != secuencia[:len(secuencia_jugador)]:
                        self.eliminado.emit(jugador_actual)
                        jugadores.remove(jugador_actual)
                        if len(jugadores) == 1:  # Si queda un jugador
                            self.ganador.emit(jugadores[0])
                            exit()
                        else:
                            manejar_error()
                        break

            # Verificar si el jugador ha completado la secuencia
            if secuencia_jugador == secuencia:
                secuencia_jugador = []
                if len(jugadores) > 1:
                    generar_secuencia()
                parpadear_leds()  # Parpadear LEDs si el jugador acierta
                reproducir_secuencia()

    def detener(self):
        self.bandera = False
class ThreadSimon3(QThread): #Jugadores 1,2,3,4
    turno = pyqtSignal(str)
    eliminado = pyqtSignal(str)
    ganador = pyqtSignal(str)
    bandera = True

    def run(self):

        # Variables globales
        secuencia = []
        secuencia_jugador = []
        acierto = True

        # Lista de jugadores
        jugadores = ["Jugador 1", "Jugador 2", "Jugador 3", "Jugador 4"]

        # Función para generar una nueva secuencia y seleccionar un jugador aleatorio
        def generar_secuencia():
            global jugador_actual
            secuencia.append(random.choice(pin_leds))
            jugador_actual = random.choice(jugadores)
            self.turno.emit(jugador_actual)
            # Movimiento del servo según el jugador seleccionado
            if jugador_actual == "Jugador 1":
                servo.write(0)
            elif jugador_actual == "Jugador 2":
                servo.write(45)
            elif jugador_actual == "Jugador 3":
                servo.write(90)
            elif jugador_actual == "Jugador 4":
                servo.write(135)

                # Función para reproducir la secuencia

        def reproducir_secuencia():
            for pin in secuencia:
                board.digital[pin].write(1)
                board.digital[pin_altavoz].write(0.5)
                time.sleep(0.5)
                board.digital[pin].write(0)
                board.digital[pin_altavoz].write(0)
                time.sleep(0.5)

            # Función para hacer parpadear los LEDs cuando el jugador acierta

        def parpadear_leds():
            for _ in range(2):
                for pin in pin_leds:
                    board.digital[pin].write(1)
                time.sleep(0.3)
                for pin in pin_leds:
                    board.digital[pin].write(0)
                time.sleep(0.3)

                # Función para encender todos los LEDs en escalera

        def encender_en_escalera():
            for _ in range(3):  # Encender en escalera tres veces
                for i in range(len(pin_leds)):
                    board.digital[pin_leds[i]].write(1)
                    time.sleep(0.1)
                for i in range(len(pin_leds)):
                    board.digital[pin_leds[i]].write(0)
                    time.sleep(0.1)

            # Función para manejar el error

        def manejar_error():
            for pin in pin_leds:
                board.digital[pin].write(1)
            board.digital[pin_altavoz].write(0.7)  # Cambio de tono para indicar error
            time.sleep(1)
            for pin in pin_leds:
                board.digital[pin].write(0)
            board.digital[pin_altavoz].write(0)
            # Reiniciar el juego y encender en escalera
            secuencia.clear()  # Limpiar la secuencia actual
            secuencia_jugador.clear()  # Limpiar la secuencia del jugador
            encender_en_escalera()  # Encender LEDs en escalera

            # Bucle principal
        while self.bandera:
            if len(jugadores) > 1:
                if not secuencia:
                    generar_secuencia()
                    reproducir_secuencia()

            for i, pin in enumerate(pin_botones):
                if board.digital[pin].read():
                    secuencia_jugador.append(pin_leds[i])
                    board.digital[pin_leds[i]].write(1)
                    board.digital[pin_altavoz].write(0.5)
                    time.sleep(0.5)
                    board.digital[pin_leds[i]].write(0)
                    board.digital[pin_altavoz].write(0)
                    time.sleep(0.5)
                    # Verificar la secuencia del jugador en cada paso
                    if secuencia_jugador != secuencia[:len(secuencia_jugador)]:
                        self.eliminado.emit(jugador_actual)
                        jugadores.remove(jugador_actual)
                        if len(jugadores) == 1:  # Si queda un jugador
                            self.ganador.emit(jugadores[0])
                            exit()
                        else:
                            manejar_error()
                        break

            # Verificar si el jugador ha completado la secuencia
            if secuencia_jugador == secuencia:
                secuencia_jugador = []
                if len(jugadores) > 1:
                    generar_secuencia()
                parpadear_leds()  # Parpadear LEDs si el jugador acierta
                reproducir_secuencia()

    def detener(self):
        self.bandera = False


class ThreadSimon2(QThread): #Todos los jugadores
    turno = pyqtSignal(str)
    eliminado = pyqtSignal(str)
    ganador = pyqtSignal(str)
    bandera = True

    def run(self):

        # Variables globales
        secuencia = []
        secuencia_jugador = []
        acierto = True

        # Lista de jugadores
        jugadores = ["Jugador 1", "Jugador 2", "Jugador 3", "Jugador 4", "Jugador 5"]

        # Función para generar una nueva secuencia y seleccionar un jugador aleatorio
        def generar_secuencia():
            global jugador_actual
            secuencia.append(random.choice(pin_leds))
            jugador_actual = random.choice(jugadores)
            # print(f"Turno del {jugador_actual}:")
            self.turno.emit(jugador_actual)
            # Movimiento del servo según el jugador seleccionado
            if jugador_actual == "Jugador 1":
                servo.write(0)
            elif jugador_actual == "Jugador 2":
                servo.write(45)
            elif jugador_actual == "Jugador 3":
                servo.write(90)
            elif jugador_actual == "Jugador 4":
                servo.write(135)
            elif jugador_actual == "Jugador 5":
                servo.write(180)

        # Función para reproducir la secuencia
        def reproducir_secuencia():
            for pin in secuencia:
                board.digital[pin].write(1)
                board.digital[pin_altavoz].write(0.5)
                time.sleep(0.5)
                board.digital[pin].write(0)
                board.digital[pin_altavoz].write(0)
                time.sleep(0.5)

        # Función para hacer parpadear los LEDs cuando el jugador acierta
        def parpadear_leds():
            for _ in range(2):
                for pin in pin_leds:
                    board.digital[pin].write(1)
                time.sleep(0.3)
                for pin in pin_leds:
                    board.digital[pin].write(0)
                time.sleep(0.3)

        # Función para encender todos los LEDs en escalera
        def encender_en_escalera():
            for _ in range(3):  # Encender en escalera tres veces
                for i in range(len(pin_leds)):
                    board.digital[pin_leds[i]].write(1)
                    time.sleep(0.1)
                for i in range(len(pin_leds)):
                    board.digital[pin_leds[i]].write(0)
                    time.sleep(0.1)

        # Función para manejar el error
        def manejar_error():
            for pin in pin_leds:
                board.digital[pin].write(1)
            board.digital[pin_altavoz].write(0.7)  # Cambio de tono para indicar error
            time.sleep(1)
            for pin in pin_leds:
                board.digital[pin].write(0)
            board.digital[pin_altavoz].write(0)
            # Reiniciar el juego y encender en escalera
            secuencia.clear()  # Limpiar la secuencia actual
            secuencia_jugador.clear()  # Limpiar la secuencia del jugador
            encender_en_escalera()  # Encender LEDs en escalera

        # Bucle principal
        while self.bandera:
            if len(jugadores) > 1:
                if not secuencia:
                    generar_secuencia()
                    reproducir_secuencia()

            for i, pin in enumerate(pin_botones):
                if board.digital[pin].read():
                    secuencia_jugador.append(pin_leds[i])
                    board.digital[pin_leds[i]].write(1)
                    board.digital[pin_altavoz].write(0.5)
                    time.sleep(0.5)
                    board.digital[pin_leds[i]].write(0)
                    board.digital[pin_altavoz].write(0)
                    time.sleep(0.5)
                    # Verificar la secuencia del jugador en cada paso
                    if secuencia_jugador != secuencia[:len(secuencia_jugador)]:
                        # print(f"¡{jugador_actual} ha cometido un error! Eliminado del juego.")
                        self.eliminado.emit(jugador_actual)
                        jugadores.remove(jugador_actual)
                        if len(jugadores) == 1:  # Si queda un jugador
                            # print(f"¡{jugadores[0]} ha ganado!")
                            self.ganador.emit(jugadores[0])
                            exit()
                        else:
                            manejar_error()
                        break

            # Verificar si el jugador ha completado la secuencia
            if secuencia_jugador == secuencia:
                secuencia_jugador = []
                if len(jugadores) > 1:
                    generar_secuencia()
                parpadear_leds()  # Parpadear LEDs si el jugador acierta
                reproducir_secuencia()

    def detener(self):
        self.bandera = False


# clase de creacion de hilo
class ThreadSimon(QThread): #Clasico de un jugador
    puntaje = pyqtSignal(int)
    error = pyqtSignal(int)
    hilo_led_rojo = pyqtSignal(bool)
    hilo_led_verde = pyqtSignal(bool)
    hilo_led_amarillo = pyqtSignal(bool)
    hilo_led_azul = pyqtSignal(bool)

    bandera = True

    def __init__(self):
        super().__init__()

        # Función para encender todos los LEDs en escalera

    def encender_en_escalera(self):
        for _ in range(3):  # Encender en escalera tres veces
            for i in range(len(pin_leds)):
                board.digital[pin_leds[i]].write(1)
                time.sleep(0.1)
            for i in range(len(pin_leds)):
                board.digital[pin_leds[i]].write(0)
                time.sleep(0.1)

    def run(self):

        # Variables globales
        secuencia = []
        secuencia_jugador = []
        puntaje = 0  # Variable para almacenar el puntaje del jugador

        # Función para generar una nueva secuencia
        def generar_secuencia():
            secuencia.append(random.choice(pin_leds))

        # Función para reproducir la secuencia
        def reproducir_secuencia():
            for pin in secuencia:
                time.sleep(0.3)
                board.digital[pin].write(1)
                board.digital[pin_altavoz].write(0.1)
                time.sleep(0.1)
                board.digital[pin].write(0)  # Apagar el LED después de un tiempo de espera
                board.digital[pin_altavoz].write(0)  # Detener el sonido

        # Función para hacer parpadear los LEDs cuando el jugador acierta
        def parpadear_leds():
            for _ in range(2):
                for pin in pin_leds:
                    board.digital[pin].write(1)
                time.sleep(0.2)
                for pin in pin_leds:
                    board.digital[pin].write(0)
                time.sleep(0.3)

        # Función para manejar el error
        def manejar_error():
            nonlocal puntaje
            for pin in pin_leds:
                board.digital[pin].write(1)
            board.digital[pin_altavoz].write(0.7)  # Cambio de tono para indicar error
            time.sleep(1)
            for pin in pin_leds:
                board.digital[pin].write(0)
            board.digital[pin_altavoz].write(0)

        # Bucle principal
        while self.bandera:
            if not secuencia:
                generar_secuencia()
                reproducir_secuencia()

            for i, pin in enumerate(pin_botones):
                if board.digital[pin].read():
                    secuencia_jugador.append(pin_leds[i])
                    board.digital[pin_leds[i]].write(1)
                    board.digital[pin_altavoz].write(0.5)
                    time.sleep(0.5)
                    board.digital[pin_leds[i]].write(0)
                    board.digital[pin_altavoz].write(0)
                    time.sleep(0.5)
                    # Verificar la secuencia del jugador en cada paso
                    if secuencia_jugador != secuencia[:len(secuencia_jugador)]:
                        manejar_error()
                        self.error.emit(0)
                        self.bandera = False  # Detener el juego cuando se comete un error
                        break

            # Verificar si el jugador ha completado la secuencia
            if secuencia_jugador == secuencia:
                puntaje += 1  # Incrementar el puntaje
                secuencia_jugador = []
                self.puntaje.emit(puntaje)
                generar_secuencia()
                parpadear_leds()  # Parpadear LEDs si el jugador acierta
                reproducir_secuencia()
                # Emitir señales para actualizar los QLabel correspondientes
                self.hilo_led_rojo.emit(True) if 12 in secuencia else self.hilo_led_rojo.emit(False)
                self.hilo_led_verde.emit(True) if 11 in secuencia else self.hilo_led_verde.emit(False)
                self.hilo_led_amarillo.emit(True) if 10 in secuencia else self.hilo_led_amarillo.emit(False)
                self.hilo_led_azul.emit(True) if 9 in secuencia else self.hilo_led_azul.emit(False)
                time.sleep(0.5)  # Espera para mostrar el estado apagado
                self.hilo_led_rojo.emit(False) if 12 in secuencia else None
                self.hilo_led_verde.emit(False) if 11 in secuencia else None
                self.hilo_led_amarillo.emit(False) if 10 in secuencia else None
                self.hilo_led_azul.emit(False) if 9 in secuencia else None

    def detener(self):
        self.bandera = False


class SimonDiceGame(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('simon_dice.ui', self)
        self.init_game()

    def init_game(self):
        # Quiero que me muestre la pantalla principal primero
        self.stackedWidget.setCurrentIndex(0)

        self.bt_md_clasico.clicked.connect(self.mostrar_pagina_clasico)
        self.bt_md_extremo.clicked.connect(self.mostrar_pagina_extremo)
        self.bt_menu.clicked.connect(self.mostrar_pagina_menu)
        self.bt_jugar_extremo.clicked.connect(self.mostrar_pagina_jugadores)
        self.bt_jugar_clasico.clicked.connect(self.mostrar_pagina_jugar_clasico)
        self.bt_start_clasico.clicked.connect(self.iniciar_juego_clasico)
        self.bt_5jugadores.clicked.connect(self.mostrar_pagina_5jugadores)
        self.bt_4jugadores.clicked.connect(self.mostrar_pagina_4jugadores)
        self.bt_3jugadores.clicked.connect(self.mostrar_pagina_3jugadores)
        self.bt_2jugadores.clicked.connect(self.mostrar_pagina_2jugadores)

        self.bt_start_extremo.clicked.connect(self.iniciar_juego_extremo)
        self.bt_start_4jugadores.clicked.connect(self.iniciar_juego_4jugadores)
        self.bt_start_3jugadores.clicked.connect(self.iniciar_juego_3jugadores)
        self.bt_start_2jugadores.clicked.connect(self.iniciar_juego_2jugadores)

        self.bt_reiniciar_clasico.clicked.connect(self.reiniciar_juego_clasico)
        self.bt_reiniciar_extremo.clicked.connect(self.reiniciar_juego_extremo)
        self.bt_reiniciar_4jugadores.clicked.connect(self.reiniciar_juego_4jugadores)
        self.bt_reiniciar_3jugadores.clicked.connect(self.reiniciar_juego_3jugadores)
        self.bt_reiniciar_3jugadores.clicked.connect(self.reiniciar_juego_2jugadores)
        self.label_instrucciones.setText(
            "Bienvenido\nEl objetivo del juego es repetir una secuencia de colores y sonidos\n"
            "generada por el juego en orden correcto y cada vez más larga.\n"
            "1. El juego comienza con una secuencia de colores y sonidos que se\n"
            "reproducen por la consola o la aplicación.\n"
            "2. Después de que se haya mostrado la secuencia inicial, el jugador\n"
            "debe repetir la secuencia presionando los botones en el mismo orden\n"
            "en que se mostraron.\n"
            "3. Si el jugador completa correctamente la secuencia, el juego\n"
            "aumenta en complejidad, agregando un color adicional a la secuencia.\n"
            "4. Si el jugador comete un error al repetir la secuencia,\n"
            "el juego termina y se muestra la puntuación final, que corresponde a\n"
            "la longitud de la secuencia que el jugador logró repetir\n"
            "correctamente.")
        self.label_instrucciones_extremo.setText(
            "Bienvenido al modo extremo\n El objetivo del juego es repetir una secuencia de colores y sonidos\n generada por el juego en orden correcto y cada vez más larga."
            "\n 1.-El juego comienza con una secuencia de colores y sonidos que se \n reproducen por la consola o la aplicación"
            "\n 2.-Después de que se haya mostrado la secuencia inicial, un jugador \n debe repetir la secuencia presionando los botones en el mismo orden \n en que se mostraron."
            "\n 3.-El orden de los jugadores se decide aleatoriamente \n  agregando un color adicional a la secuencia"
            "\n 4.-Si el jugador comete un error al repetir la secuencia, \n es eliminado y vuelve a comenzar con los jugadores restantes\n el ganador es el ultimo que queda en pie.")

        # inicializamos hilo
        self.Hilo = ThreadSimon()
        self.Hilo.puntaje.connect(self.puntaje)
        self.Hilo.error.connect(self.maracar_error)
        self.leds_state = {12: False, 11: False, 10: False, 9: False}  # Estado inicial de los LEDs
        self.Hilo.hilo_led_rojo.connect(lambda state: self.actualizar_label(12, state))
        self.Hilo.hilo_led_verde.connect(lambda state: self.actualizar_label(11, state))
        self.Hilo.hilo_led_amarillo.connect(lambda state: self.actualizar_label(10, state))
        self.Hilo.hilo_led_azul.connect(lambda state: self.actualizar_label(9, state))

        # inicializamos hilo 2
        self.Hilo2 = ThreadSimon2()
        self.Hilo2.turno.connect(self.turno)
        self.Hilo2.eliminado.connect(self.eliminado)
        self.Hilo2.ganador.connect(self.mostrar_ganador)

        # inicializamos hilo 3
        self.Hilo3 = ThreadSimon3()
        self.Hilo3.turno.connect(self.turno4jugadores)
        self.Hilo3.eliminado.connect(self.eliminado4jugadores)
        self.Hilo3.ganador.connect(self.mostrar_ganador4jugadores)

        # inicializamos hilo 4
        self.Hilo4 = ThreadSimon4()
        self.Hilo4.turno.connect(self.turno3jugadores)
        self.Hilo4.eliminado.connect(self.eliminado3jugadores)
        self.Hilo4.ganador.connect(self.mostrar_ganador3jugadores)

        # inicializamos hilo 5
        self.Hilo5 = ThreadSimon5()
        self.Hilo5.turno.connect(self.turno3jugadores)
        self.Hilo5.eliminado.connect(self.eliminado3jugadores)
        self.Hilo5.ganador.connect(self.mostrar_ganador3jugadores)

    def actualizar_label(self, pin, estado):
        self.leds_state[pin] = estado
        self.actualizar_labels_leds()

    def actualizar_labels_leds(self):
        for pin, estado in self.leds_state.items():
            label = self.get_label_from_pin(pin)
            color = self.get_color_from_pin(pin)
            if estado:
                label.setStyleSheet(f"background-color: {color};border-radius: 50px;")
            else:
                label.setStyleSheet("background-color: gray;border-radius: 50px;")

    def get_label_from_pin(self, pin):
        if pin == 12:
            return self.label_color_rojo
        elif pin == 11:
            return self.label_color_verde
        elif pin == 10:
            return self.label_color_amarillo
        elif pin == 9:
            return self.label_color_azul

    def get_color_from_pin(self, pin):
        if pin == 12:
            return "red"
        elif pin == 11:
            return "green"
        elif pin == 10:
            return "yellow"
        elif pin == 9:
            return "blue"

    def maracar_error(self, val):
        if val == 0:
            self.mostrar_mensaje_error("¡Has cometido un error!")

    def puntaje(self, val):
        self.label_mostrar_puntos.setText(str(val))
        print(val)

    def mostrar_mensaje_error(self, mensaje):
        msg_box = QMessageBox()
        msg_box.setText(mensaje)
        msg_box.setWindowTitle("Error")
        msg_box.exec()

    def mostrar_mensaje_ganador(self, mensaje):
        msg_box = QMessageBox()
        msg_box.setText(mensaje)
        msg_box.setWindowTitle("Ganador")
        msg_box.exec()

    def iniciar_juego_clasico(self):
        self.Hilo.bandera = True
        self.Hilo.start()
        # Mostrar la primera secuencia en la interfaz

    def eliminado(self, val):
        self.mostrar_mensaje_error(f"{val},¡Has sido eliminado!")
    def eliminado4jugadores(self, val):
        self.mostrar_mensaje_error(f"{val},¡Has sido eliminado!")
    def eliminado3jugadores(self, val):
        self.mostrar_mensaje_error(f"{val},¡Has sido eliminado!")
    def eliminado2jugadores(self, val):
        self.mostrar_mensaje_error(f"{val},¡Has sido eliminado!")
    def mostrar_ganador(self, val):
        self.mostrar_mensaje_ganador(f"{val},¡Has ganado!")
        self.label_mostrar_ganador.setText(val)
    def mostrar_ganador4jugadores(self, val):
        self.mostrar_mensaje_ganador(f"{val},¡Has ganado!")
        self.label_ganador_4jugadores.setText(val)
    def mostrar_ganador3jugadores(self, val):
        self.mostrar_mensaje_ganador(f"{val},¡Has ganado!")
        self.label_ganador_3jugadores.setText(val)
    def mostrar_ganador2jugadores(self, val):
        self.mostrar_mensaje_ganador(f"{val},¡Has ganado!")
        self.label_ganador_2jugadores.setText(val)
    def turno(self, val):
        self.label_mostrar_turno.setText(val)
    def turno4jugadores(self, val):
        self.label_turno_4jugadores.setText(val)
    def turno3jugadores(self, val):
        self.label_turno_3jugadores.setText(val)
    def turno2jugadores(self, val):
        self.label_turno_2jugadores.setText(val)
    def iniciar_juego_extremo(self):
        self.Hilo2.bandera = True
        self.Hilo2.start()
    def iniciar_juego_4jugadores(self):
        self.Hilo3.bandera = True
        self.Hilo3.start()
    def iniciar_juego_3jugadores(self):
        self.Hilo4.bandera = True
        self.Hilo4.start()
    def iniciar_juego_2jugadores(self):
        self.Hilo5.bandera = True
        self.Hilo5.start()
    def mostrar_pagina_clasico(self):
        self.stackedWidget.setCurrentIndex(4)  # bien

    def mostrar_pagina_extremo(self):
        self.stackedWidget.setCurrentIndex(1)  # bien

    def mostrar_pagina_menu(self):
        self.stackedWidget.setCurrentIndex(0)  # bien
        self.Hilo.detener()
        self.Hilo2.detener()
        self.Hilo3.detener()
        self.Hilo4.detener()
        self.Hilo5.detener()

    def mostrar_pagina_jugar_clasico(self):
        self.stackedWidget.setCurrentIndex(6)  # bien

    def mostrar_pagina_5jugadores(self):
        self.stackedWidget.setCurrentIndex(3)  # bien

    def mostrar_pagina_jugadores(self):
        self.stackedWidget.setCurrentIndex(2)  # bien

    def mostrar_pagina_4jugadores(self):
        self.stackedWidget.setCurrentIndex(5)  # bien

    def mostrar_pagina_3jugadores(self):
        self.stackedWidget.setCurrentIndex(7)  # bien
    def mostrar_pagina_2jugadores(self):
        self.stackedWidget.setCurrentIndex(8)  # bien

    def reiniciar_juego_clasico(self):
        self.label_mostrar_puntos.setText("0")
        self.Hilo.bandera = False
        self.Hilo.encender_en_escalera()
        self.label_color_rojo.setStyleSheet("background-color: gray;border-radius: 50px;")
        self.label_color_verde.setStyleSheet("background-color: gray;border-radius: 50px;")
        self.label_color_amarillo.setStyleSheet("background-color: gray;border-radius: 50px;")
        self.label_color_azul.setStyleSheet("background-color: gray;border-radius: 50px;")
        print("Reiniciado")

    def reiniciar_juego_extremo(self):
        self.label_mostrar_turno.setText("")
        self.label_mostrar_ganador.setText("")
        self.Hilo2.detener()
        print("Reiniciado hilo 2")
    def reiniciar_juego_4jugadores(self):
        self.label_turno_4jugadores.setText("")
        self.label_ganador_4jugadores.setText("")
        self.Hilo3.detener()
        print("Reiniciado hilo 3")
    def reiniciar_juego_3jugadores(self):
        self.label_turno_3jugadores.setText("")
        self.label_ganador_3jugadores.setText("")
        self.Hilo4.detener()
        print("Reiniciado hilo 4")
    def reiniciar_juego_2jugadores(self):
        self.label_turno_2jugadores.setText("")
        self.label_ganador_2jugadores.setText("")
        self.Hilo4.detener()
        print("Reiniciado hilo 5")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimonDiceGame()
    window.show()
    sys.exit(app.exec())

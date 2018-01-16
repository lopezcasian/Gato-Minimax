from tkinter import *
import time

#sys.setrecursionlimit(3000)

class Juego: #Clase juego
	def __init__(self):
		self.ventana = Tk() #Crear ventana de bienvenida
		self.ventana.title('Bienvenido') # Poner titulo
		self.ventana.geometry("412x500") # Configurar la medida de ventana

		#widgets
		titulo = Label(self.ventana, text="Juego Gato", font=("gadugi",40, "bold"), fg="lime green").place(x=65,y=20) # Label del titulo y pocision
		bienvenido = Label(self.ventana, text="Bienvenido", font=("gadugi",16), fg="olive drab").place(x=155,y=90) # Label de bienvenida y pocision
		
		# Cargando imagenes
		x = PhotoImage(file = 'x.gif')
		o = PhotoImage(file = 'o.gif')
		vacio = PhotoImage(file = 'default.gif')

		# Botones en la ventana, solo serviran de muestra, mas solo funciona el boton11 para iniciar
		boton00 = Button(self.ventana, state = DISABLED)
		boton00.place(x=40,y=140)
		boton00.config(image = o, width = '100', height = '100')

		boton01 = Button(self.ventana, state = DISABLED)
		boton01.place(x=155,y=140)
		boton01.config(image = vacio, width = '100', height = '100')

		boton02 = Button(self.ventana, state = DISABLED)
		boton02.place(x=270,y=140)
		boton02.config(image = x, width = '100', height = '100')

		boton10 = Button(self.ventana, state = DISABLED)
		boton10.place(x=40,y=255)
		boton10.config(image = vacio, width = '100', height = '100')

		# Ejecuta elegirTurno, dandole como parametro la ventana a destrir
		boton11 = Button(self.ventana, width=13, height=6, text = "Iniciar",command=lambda: self.elegirIcono(self.ventana))
		boton11.place(x=155,y=255)

		boton12 = Button(self.ventana, state = DISABLED)
		boton12.place(x=270,y=255)
		boton12.config(image = vacio, width = '100', height = '100')

		boton20 = Button(self.ventana, state = DISABLED)
		boton20.place(x=40,y=370)
		boton20.config(image = vacio, width = '100', height = '100')

		boton21 = Button(self.ventana, state = DISABLED)
		boton21.place(x=155,y=370)
		boton21.config(image = vacio, width = '100', height = '100')

		boton22 = Button(self.ventana, state = DISABLED)
		boton22.place(x=270,y=370)
		boton22.config(image = vacio, width = '100', height = '100')
		self.ventana.mainloop()


	def elegirIcono(self, vtn):
		#widgets
		vtn.destroy() #Se destruye la ventana anterior

		# Creando nueva ventana
		self.vtnTurno = Tk(); 
		self.vtnTurno.title('Elegir turno')
		self.vtnTurno.geometry("412x400")

		# Labels para titulo y descripcion de ventana
		LblTitulo = Label(self.vtnTurno, text="Juego Gato", font=("gadugi",40,"bold"), fg="purple").place(x=65,y=20)
		LblTxt = Label(self.vtnTurno, text="Por favor, elija el icono que desea usar:", font=("gadugi",12,"bold"), fg="mediumpurple1").place(x=57,y=100)

		# Cargando imagenes
		self.xI = PhotoImage(file = 'x.gif')
		self.oI = PhotoImage(file = 'o.gif')

		#cargando botones
		BtnX = Button(self.vtnTurno, command=lambda: self.iniciar("x"))
		BtnX.place(x=230,y=180)
		BtnX.config(image = self.xI, width = '100', height = '100')
		# Btn que manda a la funcion iniciar con parametro x
		BtnO = Button(self.vtnTurno, command=lambda: self.iniciar("o"))
		BtnO.place(x=75,y=180)
		BtnO.config(image = self.oI, width = '100', height = '100')
		# Btn que manda a la funcion iniciar con parametro o
		self.vtnTurno.mainloop()

	def iniciar(self, icono):
		# Definiendo variables para el juego
		#interface
		self.vtnTurno.destroy() # Destruye la ventana anterior

		#Se crea una nueva ventana
		self.vtnJuego = Tk();
		self.vtnJuego.title('A jugar!')
		self.vtnJuego.geometry("580x470")

		# Cargando iamgenes a utilizar
		self.x = PhotoImage(file = 'x.gif')
		self.o = PhotoImage(file = 'o.gif')
		self.vacio = PhotoImage(file = 'default.gif')

		# Asignando datos a variable jugador, los datos son un diccionario que incluye el icono y la imagen correspondiente
		if icono == 'x':
			self.jugador = {'icono':'x',
							'imagen': self.x
							}
			self.sistema = {'icono':'o',
							'imagen': self.o
							}
		else:
			self.jugador = {'icono':'o',
							'imagen': self.o
							}
			self.sistema = {'icono':'x',
							'imagen': self.x
							}

		# Este string sirve para colocar el turno en la interfaz grafica y como parametro de funciones
		self.strTurno = 'Jugador'

		# Array bidimensional del tablero
		self.tablero = [["vacio","vacio","vacio"],
						["vacio","vacio","vacio"],
						["vacio","vacio","vacio"]]

		# Declaracion y posicionamiento de elementos en la ventana del juego
		LblTtl = Label(self.vtnJuego, text="Juego Gato", font=("gadugi",40,"bold"), fg="dark orange").place(x=150,y=0)
		self.Lbltrn = Label(self.vtnJuego, text="Turno:", font=("gadugi",12,"bold"), fg="dark orange")
		self.Lbltrn.place(x=10,y=90)
		self.LblTurno = Label(self.vtnJuego, text=self.strTurno)
		self.LblTurno.place(x=20,y=110)


		# Botones de juego
		# Al presionar algun boton se ejecuta la funcion btnPresionado, sus parametros son, el boton (servira para configurarlo),
		#	un entero que seria la pocision x y otro que seria la pocision y, nos facilitara para configurar los botones y para
		#	cambiar los valores del array tablero y por ultimo el string del turno para saber quien lo presiono
		boton00 = Button(self.vtnJuego, width=15, height=7, command=lambda: self.btnPresionado(boton00, 0, 0, self.strTurno))
		boton00.place(x=200,y=90)
		boton00.config(image = self.vacio, width = '110', height = '110')

		boton01 = Button(self.vtnJuego, width=15, height=7, command=lambda: self.btnPresionado(boton01, 0, 1, self.strTurno))
		boton01.place(x=325,y=90)
		boton01.config(image = self.vacio, width = '110', height = '110')

		boton02 = Button(self.vtnJuego, width=15, height=7, command=lambda: self.btnPresionado(boton02, 0, 2, self.strTurno))
		boton02.place(x=450,y=90)
		boton02.config(image = self.vacio, width = '110', height = '110')

		boton10 = Button(self.vtnJuego, width=15, height=7, command=lambda: self.btnPresionado(boton10, 1, 0, self.strTurno))
		boton10.place(x=200,y=216)
		boton10.config(image = self.vacio, width = '110', height = '110')

		boton11 = Button(self.vtnJuego, width=15, height=7, command=lambda: self.btnPresionado(boton11, 1, 1, self.strTurno))
		boton11.place(x=325,y=216)
		boton11.config(image = self.vacio, width = '110', height = '110')

		boton12 = Button(self.vtnJuego, width=15, height=7, command=lambda: self.btnPresionado(boton12, 1, 2, self.strTurno))
		boton12.place(x=450,y=216)
		boton12.config(image = self.vacio, width = '110', height = '110')

		boton20 = Button(self.vtnJuego, width=15, height=7, command=lambda: self.btnPresionado(boton20, 2, 0, self.strTurno))
		boton20.place(x=200,y=342)
		boton20.config(image = self.vacio, width = '110', height = '110')

		boton21 = Button(self.vtnJuego, width=15, height=7, command=lambda: self.btnPresionado(boton21, 2, 1, self.strTurno))
		boton21.place(x=325,y=342)
		boton21.config(image = self.vacio, width = '110', height = '110')

		boton22 = Button(self.vtnJuego, width=15, height=7, command=lambda: self.btnPresionado(boton22, 2, 2, self.strTurno))
		boton22.place(x=450,y=342)
		boton22.config(image = self.vacio, width = '110', height = '110')

		# Boton reiniciar
		btnReiniciar = Button(self.vtnJuego, text = "Volver a jugar", command=self.reiniciar)
		btnReiniciar.place(x=20,y=430)

		# Array bidimensional, facilita el cambio de configuracion en funciones diferentes.
		self.botones = [[boton00,boton01,boton02],
						[boton10,boton11,boton12],
						[boton20,boton21,boton22]]

		self.vtnJuego.mainloop()


	def reiniciar(self):
		# Llama a elegirIcono, dandole como parametro la ventana a destruir
		self.elegirIcono(self.vtnJuego)




	def btnPresionado(self, boton, x, y, turno):
		# Verificar si lo presiono el jugador y si ya no hay espacios vacios
		if turno == 'Jugador' and self.hayVacios(self.tablero) == True:
			# Se le coloca la imagen del jugador
			boton.config(image = self.jugador['imagen'], width = '110', height = '110', state=DISABLED)
			# Asigna 'x' al array tablero en laposicion del boton
			self.tablero[x][y] = self.jugador['icono']
			# Cambiando de turno y mostrando en la interfaz
			self.strTurno = 'Sistema'
			self.LblTurno['text']= self.strTurno

			# Si la funcion evaluarMarcar == -10 muestra que a ganado el jugador y se desabilita el tablero
			if self.evaluarMarcar(self.tablero) == -10:
				self.LblTurno['text'] = "Has ganado"
				for x in range(0,3):
					for y in range(0,3):
						self.botones[x][y].config(state=DISABLED)
			else: # Si no se busca el mejorMovimiento dando como parametro el tablero actual, devuelve un dic con la posicion en x y y
				mejorMov = self.mejorMovimiento(self.tablero)
				x = mejorMov['fila']
				y = mejorMov['columna']
				# Se "presiona" el boton que la computadora decide como mejro movimiento
				self.btnPresionado(self.botones[x][y], x, y, self.strTurno)

		# Lo mismo que el if solo que con configuracion del sistema
		elif turno == 'Sistema' and self.hayVacios(self.tablero) == True:			
			boton.config(image = self.sistema['imagen'], width = '110', height = '110', state=DISABLED)
			self.tablero[x][y] = self.sistema['icono']
			self.strTurno = 'Jugador'
			self.LblTurno['text']= self.strTurno
			if self.evaluarMarcar(self.tablero) == 10:
				self.LblTurno['text'] = "Ha ganado el sistema"
				for x in range(0,3):
					for y in range(0,3):
						self.botones[x][y].config(state=DISABLED)
		else: # Si no hay espacios vacios y no hay ganador, es un empate
			self.LblTurno['text'] = "Es un empate"


	def mejorMovimiento(self, tab):
		# Inicializando valores
		mejorVal = -1000;
		mejorMov = {
			'fila':-1,
			'columna':-1
		}

		# Recorremos el tablero
		for x in range(0, 3):
			for y in range(0,3):

				if tab[x][y] == 'vacio': # Si la posicion esta vacia se le coloca el icono del sistema
					tab[x][y] = self.sistema['icono']
					valorMov = self.minimax(tab,0,False); # Envia tablero, profundidad y si es el max

					tab[x][y] = 'vacio' # Se pone vacio debido a que solo buscamos el mejor movimiento, pero no hacerlo
					if valorMov > mejorVal: # Si el valor obtenido es mayor que el mejor valor
						mejorMov = {
							'fila': x,
							'columna': y
						}
						# Se asigna el nuevo valor a mejor valor y se retorna un diccionario con la mejor posicion
						mejorVal = valorMov

		return mejorMov


	def minimax(self, tab, profundidad, esMax):
		puntuacion = self.evaluar(tab) # Evalua el tablero
		if puntuacion == 10:
			return puntuacion
		elif puntuacion == -10:
			return puntuacion
		
		if self.hayVacios(tab) == False: # Si ya no hay vacios es empate
			return 0

		if esMax: # Si es el maximo
			mejor = -1000
			for x in range(0,3): # Recorre tablero
				for y in range(0,3):
					if tab[x][y] == 'vacio': # Si la posicion esta vacia
						tab[x][y] = self.sistema['icono'] # Pone el icono del sistema
						mejor = max(mejor, self.minimax(tab, profundidad+1, not esMax)) # Selecciona el maximo
						tab[x][y] = 'vacio' # Vuelve a poner casilla vacia
			return mejor

		else:
			mejor = 1000

			for x in range(0,3):
				for y in range(0,3):
					if tab[x][y] == 'vacio':
						tab[x][y] = self.jugador['icono']

						mejor = min(mejor, self.minimax(tab, profundidad+1, not esMax))
						tab[x][y] = 'vacio'

			return mejor


	def evaluar(self, tab):
		# Evalua si el jugador gana
		if ((tab[0][0] == self.jugador['icono'] and tab[0][1] == self.jugador['icono'] and tab[0][2] == self.jugador['icono']) or
		(tab[1][0] == self.jugador['icono'] and tab[1][1] == self.jugador['icono'] and tab[1][2] == self.jugador['icono']) or
		(tab[2][0] == self.jugador['icono'] and tab[2][1] == self.jugador['icono'] and tab[2][2] == self.jugador['icono']) or
		(tab[0][0] == self.jugador['icono'] and tab[1][0] == self.jugador['icono'] and tab[2][0] == self.jugador['icono']) or
		(tab[0][1] == self.jugador['icono'] and tab[1][1] == self.jugador['icono'] and tab[2][1] == self.jugador['icono']) or
		(tab[0][2] == self.jugador['icono'] and tab[1][2] == self.jugador['icono'] and tab[2][2] == self.jugador['icono']) or
		(tab[0][0] == self.jugador['icono'] and tab[1][1] == self.jugador['icono'] and tab[2][2] == self.jugador['icono']) or
		(tab[0][2] == self.jugador['icono'] and tab[1][1] == self.jugador['icono'] and tab[2][0] == self.jugador['icono'])):
			return -10

		# Evalua si el sistema gana
		elif ((tab[0][0] == self.sistema['icono'] and tab[0][1] == self.sistema['icono'] and tab[0][2] == self.sistema['icono']) or
		(tab[1][0] == self.sistema['icono'] and tab[1][1] == self.sistema['icono'] and tab[1][2] == self.sistema['icono']) or
		(tab[2][0] == self.sistema['icono'] and tab[2][1] == self.sistema['icono'] and tab[2][2] == self.sistema['icono']) or
		(tab[0][0] == self.sistema['icono'] and tab[1][0] == self.sistema['icono'] and tab[2][0] == self.sistema['icono']) or
		(tab[0][1] == self.sistema['icono'] and tab[1][1] == self.sistema['icono'] and tab[2][1] == self.sistema['icono']) or
		(tab[0][2] == self.sistema['icono'] and tab[1][2] == self.sistema['icono'] and tab[2][2] == self.sistema['icono']) or
		(tab[0][0] == self.sistema['icono'] and tab[1][1] == self.sistema['icono'] and tab[2][2] == self.sistema['icono']) or
		(tab[0][2] == self.sistema['icono'] and tab[1][1] == self.sistema['icono'] and tab[2][0] == self.sistema['icono'])):
			return 10
		else:
			# sino, empate
			return 0

	# Esta funcion es basicamente la misma que evaluar, solo que la utilizamos para mostrar en la interfaz grafica quien gano y con que casillas
	def evaluarMarcar(self, tab):
		for x in range(0,3):
			if tab[x][0] == self.sistema['icono'] and tab[x][1]== self.sistema['icono'] and tab[x][2] == self.sistema['icono']:
				self.botones[x][0].config(background='green')
				self.botones[x][1].config(background='green')
				self.botones[x][2].config(background='green')
				return 10
			elif tab[x][0] == self.jugador['icono'] and tab[x][1]== self.jugador['icono'] and tab[x][2] == self.jugador['icono']:
				self.botones[x][0].config(background='green')
				self.botones[x][1].config(background='green')
				self.botones[x][2].config(background='green')
				return -10

		for y in range(0,3):
			if tab[0][y] == self.sistema['icono'] and tab[1][y]== self.sistema['icono'] and tab[2][y] == self.sistema['icono']:
				self.botones[0][y].config(background='green')
				self.botones[1][y].config(background='green')
				self.botones[2][y].config(background='green')
				return 10
			elif tab[0][y] == self.jugador['icono'] and tab[1][y]== self.jugador['icono'] and tab[2][y] == self.jugador['icono']:
				self.botones[0][y].config(background='green')
				self.botones[1][y].config(background='green')
				self.botones[2][y].config(background='green')
				return -10

		if tab[0][0] == self.sistema['icono'] and tab[1][1]== self.sistema['icono'] and tab[2][2] == self.sistema['icono']:
			self.botones[0][0].config(background='green')
			self.botones[1][1].config(background='green')
			self.botones[2][2].config(background='green')
			return 10
		elif tab[0][0] == self.jugador['icono'] and tab[1][1]== self.jugador['icono'] and tab[2][2] == self.jugador['icono']:
			self.botones[0][0].config(background='green')
			self.botones[1][1].config(background='green')
			self.botones[2][2].config(background='green')
			return -10

		if tab[0][2] == self.sistema['icono'] and tab[1][1]== self.sistema['icono'] and tab[2][0] == self.sistema['icono']:
			self.botones[0][2].config(background='green')
			self.botones[1][1].config(background='green')
			self.botones[2][0].config(background='green')
			return 10
		elif tab[0][2] == self.jugador['icono'] and tab[1][1]== self.jugador['icono'] and tab[2][0] == self.jugador['icono']:
			self.botones[0][2].config(background='green')
			self.botones[1][1].config(background='green')
			self.botones[2][0].config(background='green')
			return -10

		return 0

	def hayVacios(self, tab):
		for x in range(0,3):
			for y in range(0,3):
				if tab[x][y] == 'vacio':
					return True
		return False

Juego()
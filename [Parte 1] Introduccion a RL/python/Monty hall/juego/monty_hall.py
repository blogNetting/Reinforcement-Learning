#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


class MontyHall:
		
	def __esconder_coche(self):
		serie = [3,1,2,3,2,1,1,3,2,1,2,3,2,3,1,2,1,3,3,2,1,1,3,2,2,1,3]
		#serie = [3,3,2,3,2,3,3,3,2,1,2,3,2,3,3,2,3,3,3,2,3,1,3,2,2,1,3]	-> PoC - Numeros calientes.
		#return 3															-> PoC - Cambiando las reglas.
		return serie[randint(0, len(serie)-1)]
		


	def __inicializar_juego(self):
		self.__detras_puertas =[None, " ", " ", " "]
		return self.__esconder_coche()


	def __mostrar_puertas(self):
			print "\n\n\t\t\t\t+--------+--------+--------+" 
			print "\t\t\t\t| PUERTA | PUERTA | PUERTA |"
			print "\t\t\t\t|    1   |    2   |    3   |"
			print "\t\t\t\t|        |        |        |"
			print "\t\t\t\t|   "+str(self.__detras_puertas[1])+"    |    "+str(self.__detras_puertas[2])+"   |    "+str(self.__detras_puertas[3])+"   |"
			print "\t\t\t\t|        |        |        |"
			print "\t\t\t\t+--------+--------+--------+"
			print "\n"


	def __get_puerta_jugador(self):
		puerta_jugador = -1
		while(puerta_jugador not in [1,2,3]):
			try:
				puerta_jugador = input("\t\t\t¿Que puerta eliges?: ")
			except:
				exit(0)
		print "\n"
		return puerta_jugador


	def __get_cambio_jugador(self):
		cambio = ""
		while(cambio not in ["S","N"]):
			try:		
				cambio = (raw_input("\t\t\t¿Quieres cambiar de puerta (N=No, S=Si)?: ")).upper()
			except:
				exit(-1)
		return (cambio=="S")
		
		
	def __abrir_puerta(self, puerta_jugador, puerta_coche):	
		if (puerta_jugador == puerta_coche):
			ps = [1,2,3]
			ps.remove(puerta_jugador)
			p = ps[randint(0,1)]
		else: p=6-(puerta_jugador+puerta_coche)
		self.__detras_puertas[p]="\033[91mC\033[0m"
		self.__mostrar_puertas()
		return p
		

	def __es_ganador(self, puerta_coche, puerta_jugador, cambio):
		acierto = puerta_coche == puerta_jugador
		if (cambio): acierto = not acierto
		return acierto


	def __pintar_resultado(self, es_ganador):
		linea = "###########################################\n"
		cadena = "\033[91m" + linea + "\t\t\t\t\t  ¡Perdio!"
		if(es_ganador): cadena = "\033[92m" + linea + "\t\t\t\t\t   ¡Gano!"
		print "\n\n\t\t\t" + cadena + "\n\t\t\t" + linea + "\033[0m\n"
		


	def __mostrar_debug(self, puerta_jugador, puerta_coche, cambio, puerta_cabra):
		print "\n\t\t\tPuerta jugador: " + str(puerta_jugador) + "."
		print "\t\t\tPuerta coche: " + str(puerta_coche) + "."
		print "\t\t\tHizo cambio: " + str(cambio) + "."
		print "\t\t\tPuerta cabra: " + str(puerta_cabra) + "."
		print "\n"		
		
		
	def jugar(self, debug=False):
		puerta_coche = self.__inicializar_juego()
		self.__mostrar_puertas()
		puerta_jugador = self.__get_puerta_jugador()
		puerta_cabra = self.__abrir_puerta(puerta_jugador, puerta_coche)
		cambio = self.__get_cambio_jugador()
		es_ganador = self.__es_ganador(puerta_coche, puerta_jugador, cambio)
		self.__pintar_resultado(es_ganador)
		if (debug): self.__mostrar_debug(puerta_jugador, puerta_coche, cambio, puerta_cabra)
		return es_ganador

	
	def jugarIA(self, puerta_jugador, cambio, debug=False, guardar=False):
		puerta_coche = self.__inicializar_juego()
		es_ganador = self.__es_ganador(puerta_coche, puerta_jugador, cambio)
		if (debug):
			self.__pintar_resultado(es_ganador)
			self.__mostrar_debug(puerta_jugador, puerta_coche, cambio, None)
		return es_ganador
		

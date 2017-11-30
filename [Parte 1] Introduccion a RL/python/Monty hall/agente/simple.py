#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: 		Enrique Andrade González - NeTTinG
# Web:			blog.netting.es
# email:		netting(at)netting(dot)es

# .::Reinforcement Learning::.
# [Parte 1] Introduccion a RL - Taller
# Practica 1 - "El problema de Monty Hall". 

# Licencia: 
# Creative commons (cc) - creativecommons.org
# Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)


from random import randint
import sys
#sys.path.append('../juego')
from juego.monty_hall import MontyHall
#sys.path.append('../modulos')
from modulos.estadisticas import mostrar_estadistica, calcular_estadistica


class AgenteSimple:
	
	def __init__(self):
		self.s = [0.0, 0.0, 0.0]
		self.a_puertas = [[0,0], [0,0], [0,0]]
		self.recompensa = [-1, 1]
		

	def __elegir_puerta(self):
		return self.s.index(max(self.s))
	
	
	def __decidir_cambio(self, puerta):
		a = self.a_puertas[puerta]
		if (a[0]>a[1]): return 0
		if (a[1]>a[0]): return 1
		# En el caso de empate azar.
		return randint(0, 1)


	def __calcular_recompensas(self, ganador, puerta, cambio):
		self.a_puertas[puerta][cambio] += self.recompensa[int(ganador)]
		self.s[puerta] = (max(self.a_puertas[puerta]))
	
	
	def __mostrar_tablas(self):
		for i in range(len(self.a_puertas)):
			print "\t\t\t           | " + "Sin cambio: " + str(self.a_puertas[i][0])
			print "\t\t\t Puerta " + str(i) + " < " + "R: " + str(self.s[i])
			print "\t\t\t           | " + "Con Cambio: " + str(str(self.a_puertas[i][1]))
			print
		
		
	def jugar(self, num_i, v=False):
		aciertos = 0
		porcentaje_acierto = 0.0
		for i in range(num_i):
			if(v): print "\t\t      ----------------- [ Partida " + str(i+1) + " ] -----------------"	
			puerta_jugador = self.__elegir_puerta()
			cambio = self.__decidir_cambio(puerta_jugador)
			es_ganador = MontyHall().jugarIA((puerta_jugador+1), cambio, debug=v, guardar=False)
			aciertos, porcentaje_acierto = calcular_estadistica(es_ganador, aciertos, i)
			self.__calcular_recompensas(es_ganador, puerta_jugador, cambio)
			if(v): 
				mostrar_estadistica(aciertos, porcentaje_acierto, i)
				self.__mostrar_tablas()
		if (not v):mostrar_estadistica(aciertos, porcentaje_acierto, i)

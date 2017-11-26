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


class AgenteCompleto:
	
	recompensa = [-1, 1]
	
	def __init__(self):
		self.s = [100.0, 100.0, 100.0]
		
		#                   +----------------------------+				+-----------------------------+
		#					|	       Cambios:		     |				|			Leyenda 		  |
		#					+----------------------------+				+-----------------------------+
		# 					|    Sin      |    Con	     |				|  1º : Recompensa acumulada. |
		#					+----------------------------+				|  2º : Nº Veces y Aciertos.  | 				
		#					|  1º |   2º  |  1º  |   2º  |				+-----------------------------+
		#					+----------------------------+				|  V  : Nº Veces elegida.     |
		#					|  %  | V | A |	  %  | V | A |				|  A  : Nº de aciertos.       |
		#					+----------------------------+				+-----------------------------+
		self.a_puertas = [	[[0.0, [0 , 0]],[0.0, [0, 0]]],			
							[[0.0, [0 , 0]],[0.0, [0, 0]]], 
							[[0.0, [0 , 0]],[0.0, [0, 0]]]	]
		

	def __elegir_puerta(self):
		return self.s.index(max(self.s))
	
	
	def __decidir_cambio(self, puerta):
		a = self.a_puertas[puerta]
		if (a[0]>a[1]): return 0
		if (a[1]>a[0]): return 1
		# En el caso de empate azar.
		return randint(0, 1)


	def __calcular_recompensas(self, ganador, puerta, cambio):
		# +1 Nº Veces
		self.a_puertas[puerta][cambio][1][0]+= 1
		# +0/1 Aciertos. En función de si acerto o no.
		self.a_puertas[puerta][cambio][1][1]+= int(ganador)
		# Calculamos el porcentaje de acierto.
		self.a_puertas[puerta][cambio][0] = (self.a_puertas[puerta][cambio][1][1] / self.a_puertas[puerta][cambio][1][0]) * 100
		
		#self.a_puertas[puerta][cambio] += recompensa[int(ganador)]
		# Conservador
		self.s[puerta] = max(self.a_puertas[puerta][0][0], self.a_puertas[puerta][1][0])
		# self.s[puerta] = ((a_puertas[puerta][0] + a_puertas[puerta][1])/2)
	
	
	def __mostrar_tablas(self):
		for i in range(len(self.a_puertas)):
			print "\t           | " + "Sin cambio: " + str(self.a_puertas[i][0])
			print "\t Puerta " + str(i) + " < " + "R: " + str(self.s[i])
			print "\t           | " + "Con Cambio: " + str(str(self.a_puertas[i][1]))
			print
		
		
	def jugar(self, num_i, v=False):
		aciertos = 0
		porcentaje_acierto = 0.0
		for i in range(num_i):
			if(v): print "\t\t      ----------------- [ Partida " + str(i+1) + " ] -----------------"	
			puerta_jugador = self.__elegir_puerta()
			cambio = self.__decidir_cambio(puerta_jugador)
			es_ganador = MontyHall().jugarIA(puerta_jugador, cambio, debug=v, guardar=False)
			aciertos, porcentaje_acierto = calcular_estadistica(es_ganador, aciertos, i)
			self.__calcular_recompensas(es_ganador, puerta_jugador, cambio)
			if(v): 
				mostrar_estadistica(aciertos, porcentaje_acierto, i)
				self.__mostrar_tablas()
		if (not v):mostrar_estadistica(aciertos, porcentaje_acierto, i)

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

class AgenteAleatorio:
	
	def __elegir_puerta(self):
		return randint(1, 3)
	
	
	def __decidir_cambio(self):
		return bool(randint(0, 1))


	def jugar(self, num_i, v=False):
		aciertos = 0
		porcentaje_acierto = 0.0
		for i in range(num_i):
			if(v): print "\t\t      ----------------- [ Partida " + str(i+1) + " ] -----------------"			
			es_ganador = MontyHall().jugarIA(self.__elegir_puerta(), self.__decidir_cambio(), debug=v, guardar=False)
			aciertos, porcentaje_acierto = calcular_estadistica(es_ganador, aciertos, i)
			if(v): mostrar_estadistica(aciertos, porcentaje_acierto, i)
		if (not v):mostrar_estadistica(aciertos, porcentaje_acierto, i)

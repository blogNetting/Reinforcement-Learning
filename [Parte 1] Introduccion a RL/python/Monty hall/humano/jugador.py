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

import sys
#sys.path.append('../juego')
from juego.monty_hall import MontyHall
#sys.path.append('../modulos')
from modulos.estadisticas import mostrar_estadistica, calcular_estadistica

class Jugador:
	
	def jugar(self, num_i, v=False):
		aciertos = 0
		porcentaje_acierto = 0.0
		for i in range(num_i):
			print "\t\t      ----------------- [ Partida " + str(i+1) + " ] -----------------"			
			es_ganador = MontyHall().jugar(debug=v)
			aciertos, porcentaje_acierto = calcular_estadistica(es_ganador, aciertos, i)
			if(v): mostrar_estadistica(aciertos, porcentaje_acierto, i)
		if (not v): mostrar_estadistica(aciertos, porcentaje_acierto, i)



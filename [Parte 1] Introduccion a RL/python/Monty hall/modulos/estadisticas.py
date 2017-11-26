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


def mostrar_estadistica(aciertos, porcentaje_acierto, i):
	print "\t\t\t[ Partidas: " + str(i+1) + " ]"
	print "\t\t\t    |-> Aciertos: " + str(aciertos) + "."
	print "\t\t\t    |-> Porcentaje Acierto: " + str(porcentaje_acierto) + "%."
	print "\n"


def calcular_estadistica(es_ganador, aciertos, i):
	if (es_ganador): aciertos=aciertos+1
	porcentaje_acierto = (aciertos / ((i+1) * 0.01))
	return aciertos, porcentaje_acierto	

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
from humano.jugador import Jugador
from agente.aleatorio import AgenteAleatorio
from agente.simple import AgenteSimple


def uso():
	print "\n\tTaller Reinforcement Learning: 'El problema de Monty Hall'\n" 
	print "\tCreative commons (cc) - creativecommons.org"
	print "\tAttribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)\n\n"
	
	print "\tUso: juego_mh.py con:\n"
	print "\t    [-v] \t\t\t\tActiva el VERBOSE de los jugadores y del juego."
	print "\t    [-j] [NUM PARTIDAS]\t\t\tPara jugar una partida como un jugador."
	print "\t    [-a] [AGENTE] [NUM PARTIDAS] \tPara utilizar un agente con el juego.\n"
	print "\t\t  Posibles AGENTES:"
	print "\t\t\t -1: Agente aleatorio."
	print "\t\t\t -2: Agente simple."
	print "\t\t\t -3: Agente lector."
	print"\n"
	exit(1)


tam_param = len(sys.argv)
verbose = False
if (tam_param < 2 or tam_param > 6):
	uso()
else:
	if ("-v" in sys.argv): verbose = True
	# Para jugadores humanos.
	if ("-j" in sys.argv): 
		iteraciones = int(sys.argv[sys.argv.index("-j") + 1])
		Jugador().jugar(iteraciones, v=verbose)
	# Para agentes IA.
	elif ("-a" in sys.argv): 
		p = sys.argv.index("-a")
		agente = sys.argv[p+1]
		if agente not in ["-1", "-2", "-3"]: uso()
		iteraciones = int(sys.argv[p+2])
		# Agente Aleatorio
		if (agente == "-1"): AgenteAleatorio().jugar(iteraciones, v=verbose)
		elif (agente == "-2"): AgenteSimple().jugar(iteraciones, v=verbose)
		elif (agente == "-3"): AgenteLector().jugar(iteraciones, v=verbose)
	else: uso()

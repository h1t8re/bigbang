#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Chems eddine h1t8re 6.2.1996 After Jesus Christ'e

import math as math
import cmath as cmath
import numpy as numpy
import sympy as sympy
from mpmath import mp
import operator as operator

def generateur_d_espace(dimension, coordonnée, unités):
	for unité in unités:
		if len(coordonnée)+1 < dimension:
			for x in generateur_d_espace(dimension, coordonnée+str(unité), unités):
				yield x
		elif len(coordonnée)+1 == dimension:
			yield coordonnée+str(unité)

def generateur_infini_d_espace_et_de_temps():
	t = 0
	while True:
		t = t + 1
		for x in generateur_d_espace(t, "", [y for y in range(0, t)]):
			yield x

def recupérer_les_fonctions_mathématique():
	les_librairies_de_fonctions = []
	les_librairies_de_fonctions.append(("math", [x for x in dir(math) if "__" not in x]))
	les_librairies_de_fonctions.append(("cmath", [x for x in dir(cmath) if "__" not in x]))
	les_librairies_de_fonctions.append(("numpy", [x for x in dir(numpy) if "__" not in x]))
	les_librairies_de_fonctions.append(("sympy", [x for x in dir(sympy) if "__" not in x]))
	les_librairies_de_fonctions.append(("mp", [x for x in dir(mp) if "__" not in x]))
	les_librairies_de_fonctions.append(("math_axioms", "+-*/"))
	return les_librairies_de_fonctions

def faire_la_fonction_applicable_par_son_nom(nom_de_la_librairie, nom_de_la_fonction):
	opérations = {
	"+": operator.add,
	"-": operator.sub,
	"*": operator.mul,
	"/": operator.truediv
	}
	if nom_de_la_librairie == "math":
		fonction_applicable = getattr(math, nom_de_la_fonction)
	elif nom_de_la_librairie == "cmath":
		fonction_applicable = getattr(cmath, nom_de_la_fonction)
	elif nom_de_la_librairie == "numpy":
		fonction_applicable = getattr(numpy, nom_de_la_fonction)
	elif nom_de_la_librairie == "sympy":
		fonction_applicable = getattr(sympy, nom_de_la_fonction)
	elif nom_de_la_librairie == "mp":
		fonction_applicable = getattr(mp, nom_de_la_fonction)
	elif nom_de_la_librairie == "math_axioms":
		fonction_applicable = operations[nom_de_la_fonction]
	return fonction_applicable

def generateur_de_fonctions(fonctions_imbriqué, les_librairies_de_fonctions):
	for nom_de_la_librairie, fonctions_de_la_librairie in les_librairies_de_fonctions:
		for nom_de_la_fonction in fonctions_de_la_librairie:
			fonction = faire_la_fonction_applicable_par_son_nom(nom_de_la_librairie, nom_de_la_fonction)
			yield fonctions_imbriqué(fonction)
			for f in generateur_de_fonctions(fonctions_imbriqué(fonction), les_librairies_de_fonctions):
				yield f

def generateur_d_égualité(les_librairies_de_fonctions):
	for f in generateur_de_fonctions(None, les_librairies_de_fonctions):
		for g in generateur_de_fonctions(None, les_librairies_de_fonctions):
			égualité = (f == g)
			yield égualité

def main():
	while True:
		les_librairies_de_fonctions = recupérer_les_fonctions_mathématique()
		for unité in generateur_infini_d_espace_et_de_temps():
			for égualité in generateur_d_égualité(les_librairies_de_fonctions):
				yield unité, égualité

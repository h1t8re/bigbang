#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Chems eddine h1t8re 6.2.1996 After Jesus Christ'e

import math as math
import cmath as cmath
import numpy as numpy
import sympy as sympy
from mpmath import mp
import operator as operator

def infinity_space_generator(r):
	for Phi in range(0, 360):
		for Teta in range(0, 360):
			x = r*math.cos(math.radians(Phi))*math.sin(math.radians(Teta))
			y = r*math.sin(math.radians(Phi))*math.sin(math.radians(Teta))
			z = r*math.cos(Phi)
			r    = math.sqrt(math.pow(x, 2)+math.pow(y, 2)+math.pow(z, 2))
			Teta = math.atan2(y, x)
			Phi  = acos(z/r)
			yield (x, y, z, r, Teta, Phi)
			for (x0, y0, z0, R0, Teta0, Phi0) in infinity_space_generator(x):
                        	yield (x0, y0, z0, R0, Teta0, Phi0)
			for (x1, y1, z1, R1, Teta1, Phi1) in infinity_space_generator(y):
                        	yield (x1, y1, z1, R1, Teta1, Phi1)
			for (x2, y2, z2, R2, Teta2, Phi2) in infinity_space_generator(z):
                        	yield (x2, y2, z2, R2, Teta2, Phi2)

def infinity_space_and_time_generator():
	t = 0
	while True:
		t = t +1
		for (x, y, z, R, Teta, Phi) in infinity_space_generator(t):
			yield (x, y, z, R, Teta, Phi)

def get_math_functions():
	libraries_functions = []
	libraries_functions.append(("math", [x for x in dir(math) if "__" not in x]))
	libraries_functions.append(("cmath", [x for x in dir(cmath) if "__" not in x]))
	libraries_functions.append(("numpy", [x for x in dir(numpy) if "__" not in x]))
	libraries_functions.append(("sympy", [x for x in dir(sympy) if "__" not in x]))
	libraries_functions.append(("mp", [x for x in dir(mp) if "__" not in x]))
	libraries_functions.append(("operators", [x for x in dir(operator) if "__" not in x]))
	return libraries_functions

def make_function_callable(library_name, function_name):
	operations = {
	"+": operator.add,
	"-": operator.sub,
	"*": operator.mul,
	"/": operator.truediv
	}
	if library_name == "math":
		function_call = getattr(math, function_name)
	elif library_name == "cmath":
		function_call = getattr(cmath, function_name)
	elif library_name == "numpy":
		function_call = getattr(numpy, function_name)
	elif library_name == "sympy":
		function_call = getattr(sympy, function_name)
	elif library_name == "mp":
		function_call = getattr(mp, function_name)
	elif library_name == "operators":
		function_call = getattr(operator, function_name)
	return function_call

def yellowing_functions(func, libraries_of_functions):
	for library_name, library_of_functions in libraries_of_functions:
		for function_name in library_of_functions:
			function = make_function_callable(library_name, function_name)
			yield func(function)
			for f in yellowing_functions(func(function), libraries_of_functions):
				yield f

def yellowing_math_to_world(libraries_of_functions):
	for f in yellowing_functions(None, libraries_of_functions):
		for g in yellowing_functions(None, libraries_of_functions):
			equality = (f == g)
			yield equality

def main():
	libraries_of_functions = get_math_functions()
	for (x, y, z, r, Teta, Phi) in infinity_space_and_time_generator():
		for equality in yellowing_math_to_world(libraries_of_functions):
			yield (x, y, z, r, Teta, Phi), equality

if __name__ == "__main__":
	main()

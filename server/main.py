from bottle import route, run, template, static_file, view, post, get, redirect, request
import shutil
import os
import re
from mp import mp
from cash import cash

MEMP = mp.criaMP()
CASH = cash.criaCash()
FILA = []

@route('/static/<path:path>')
def server_static(path):
    return static_file(path, root='static')
  

@route('/')
@view('index')
def start():
	pass

@post('/leitura')
def leitura():
	global FILA
	endereco = str(request.forms.get('endereco'))
	buscado =  cash.buscaCash(endereco, CASH, FILA)
	end_c = int(endereco,2)
	if buscado == "erro":
		buscado = mp.buscaMp(end_c, MEMP)
		if buscado == "":
			print("Memoria nao preenchida")
		if buscado != "erro":
			cash.insereCash(endereco, buscado, CASH, FILA, MEMP)
	print(FILA)
	redirect('/')

@post('/escrita')
def escrita():
	global FILA
	endereco = str(request.forms.get('endereco'))
	valor = str(request.forms.get('valor'))
	
	buscado = cash.buscaCash(endereco, CASH, FILA)
	print (buscado)
	print (endereco)
	if buscado == "erro": # nao ta na cash
		cash.insereCash(endereco, valor, CASH, FILA, MEMP)
		
	else:
		print("ashahusuha")
		cash.escreveCash(endereco,valor,CASH)
	print(FILA)
	redirect('/')

	
    
run(host='localhost', port=8080)

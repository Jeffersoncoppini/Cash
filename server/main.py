from bottle import route, run, template, static_file, view, post, get, redirect, request
import shutil
import os
import re
from mp import mp
from cash import cash

MEMP = mp.criaMP()
CASH = cash.criaCash()
FILA = []
ACESSOS = 0
ACERTOS = 0
FALTAS = 0
LEITURAS = 0
ESCRITAS = 0
ACERTOSL = 0
ACERTOSE = 0
FALTASL = 0
FALTASE = 0
BUSCA = ""
@route('/static/<path:path>')
def server_static(path):
    return static_file(path, root='static')
  

@route('/')
@view('index')
def start():
	pass

@get('/')
@view('index')
def categorias():
    global ACESSOS,ACERTOS, FALTAS
    ACERTOS = ACERTOSE + ACERTOSL
    FALTAS = FALTASE + FALTASL
    ACESSOS = LEITURAS + ESCRITAS
    return dict(acessos = ACESSOS, acertos = ACERTOS, faltas = FALTAS, leituras = LEITURAS, escritas = ESCRITAS, acertosl = ACERTOSL, acertose = ACERTOSE, faltasl = FALTASL, faltase = FALTASE, memp = MEMP, cache = CASH, busca = BUSCA)
    
@post('/leitura')
def leitura():
	global FILA, LEITURAS, FALTASL, ACERTOSL,BUSCA
	LEITURAS += 1
	endereco = str(request.forms.get('endereco'))
	buscado =  cash.buscaCash(endereco, CASH, FILA)
	end_c = int(endereco,2)
	if buscado == "erro":
		FALTASL += 1
		buscado = mp.buscaMp(end_c, MEMP)
		if buscado == "":
			print("Memoria nao preenchida")
		if buscado != "erro":
			cash.insereCash(endereco, buscado, CASH, FILA, MEMP)
	else:
		ACERTOSL += 1
	if buscado == "":
		BUSCA = "NULL"
	else:
		BUSCA = buscado
	redirect('/')

@post('/escrita')
def escrita():
	global FILA, ESCRITAS, FALTASE, ACERTOSE, BUSCA
	BUSCA = ""
	ESCRITAS += 1
	endereco = str(request.forms.get('endereco'))
	valor = str(request.forms.get('valor'))
	
	buscado = cash.buscaCash(endereco, CASH, FILA)
	if buscado == "erro": # nao ta na cash
		FALTASE += 1
		cash.insereCash(endereco, valor, CASH, FILA, MEMP)
		
	else:
		ACERTOSE += 1
		cash.escreveCash(endereco,valor,CASH)
	redirect('/')


	
    
run(host='localhost', port=8080)


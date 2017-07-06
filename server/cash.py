from quadro import quadro
from mp import mp
class cash:
	quadros = []


	def criaCash():
		i = 0
		memCash = cash()
		while i < 16:
			quad = quadro()
			quad.numero = i
			quad.rotulo = ""
			quad.celula = ""
			memCash.quadros.append(quad)
			i += 1
		return memCash
	
	def buscaCash(endereco, CASH, FILA):
		k = 0
		for i in CASH.quadros:
			if i.rotulo == endereco:
				while k < 16:
					if FILA[k] == endereco:
						FILA.pop(k)
						FILA.append(endereco)
						break
				return i.celula
	
		return "erro"
	
	def insereCash(endereco, buscado, CASH, FILA, MEMP):
		flag = 0
		for j in CASH.quadros:
			if j.rotulo == "":
				j.rotulo = endereco
				j.celula = buscado
				flag = 1
				FILA.append(endereco)
				break
			
		if flag == 0:
			rot = FILA[0]
			for i in Cash.quadros:
				if i.rotulo == rot:
					valorsub = i.celula
					mp.atualizaMp(rot, valorsub, MEMP)
					i.rotulo = endereco
					i.celula = buscado
					break
			
			FILA.pop(0)
			FILA.append(endereco)
				
	def escreveCash(endereco, valor, CASH):
		 for i in CASH.quadros:
			 if i.rotulo == endereco:
				 i.celula = valor
				 print(i.celula)
		 
				
		
		
		
				
			

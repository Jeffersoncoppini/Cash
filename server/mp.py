class mp:
	celulas = []
	
	def criaMP():
		MemP = mp()
		i = 0
		
		while i < 256:
			MemP.celulas.append("")
			i += 1
		
		return MemP
	
	def buscaMp(end_c, MEMP):
		i = 0
		while i < 256:
			if i == end_c:
				return MEMP.celulas[i]
			i += 1
		return "erro"
	
	def atualizaMp(endereco,valor, MEMP):
		ender = int(endereco,2)
		i = 0
		while(i < 256):
			if i == ender:
				MEMP.celulas[i] = valor
		
		

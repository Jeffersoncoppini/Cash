<!DOCTYPE html>

<html>
<head>
  <title>Memoria</title>

  <!--Import materialize.css-->
  <link type="text/css" rel="stylesheet" href="static/css/materialize.min.css"  media="screen,projection"/>
  <!--Let browser know website is optimized for mobile-->
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

  <link type="text/css" href="static/css/style.css" rel="stylesheet">
</head>

<body>
	<div class="row">
		<div class="col s12">
			<h3>Memoria</h3>
	  <div class="row">
		<div class="col s12">
			<ul class="tabs">
				<li class="tab col s2"><a href="#test1">Ler da Memoria</a></li>
				<li class="tab col s2"><a href="#test2">Escrever na memoria</a></li>
				<li class="tab col s2"><a href="#test3">Estatisticas</a></li>
				<li class="tab col s2"><a href="#test4">Memoria Cache</a></li>
				<li class="tab col s2"><a href="#test5">Memoria principal</a></li>												
				
			</ul>
		</div>
		<div id="test1" class="col s12">
			  <div class="row">
					<h5>Leitura da memoria</h5>
					<form action = 'leitura' method = "post">
						<div class="row">
							<div class="input-field col s3">
								<input class="validate" type="text" name="endereco" id="endereco" data-ls-module="charCounter" minlength = "8" maxlength = "8" required/>
								<label for="endereco">Digite o endereco a ser lido</label>
							</div>
						</div>
						<button type="submit" class="btn waves-effect waves-light">Buscar</button>
					</form>
			</div>
			<h5>{{busca}}</h5>
		</div>
		<div id="test2" class="col s12">
			<div class="row">
					<h5>Escrita na memoria</h5>
					<form action = 'escrita' method ="post">
						<div class="row">
							<div class="input-field col s3">
								<input class="validate" type="text" name="valor" id="valor" required/>
								<label for="valor">Digite o valor a ser escrito</label>
							</div>
							<div class="input-field col s3">
								<input class="validate" type="text" name="endereco" id="endereco" data-ls-module="charCounter" minlength = "8" maxlength = "8" required/>
								<label for="endereco">Digite o endereco do valor a ser escrito</label>
							</div>
						</div>
						<button type="submit" class="btn waves-effect waves-light">Escrever</button>
					</form>
			</div>
		</div>
		<div id="test3" class="col s12">
			<h5>Estatisticas</h5>
			<h6>Numero de acessos: {{acessos}}</h6>
			<h6>Numero de acertos: {{acertos}}</h6>
			<h6>Numero de faltas: {{faltas}}</h6>
			<h6>Numero de leituras: {{leituras}}</h6>
			<h6>Numero de escritas: {{escritas}}</h6>
			<h6>Numero de acertos na leitura: {{acertosl}}</h6>
			<h6>Numero de acertos na Escrita: {{acertose}}</h6>
			<h6>Numero de faltas na leitura: {{faltasl}}</h6>
			<h6>Numero de faltas na escrita: {{faltase}}</h6>
		</div>
		<div id="test4" class="col s6">
			<div id="content">
				<table class="table table-striped">
					<thead>
						<tr>
							<th>QUADRO</th>
							<th>ROTULO</th>
							<th>CELULA</th>
						</tr>
					</thead>
					%for i in cache.quadros:
						<tr>
							<td>
								{{i.numero}}
							</td>
							<td>
								{{i.rotulo}}
							</td>
							<td>
								{{i.celula}}
							</td>
						</tr>
					%end
				</table>
			</div>
		</div>
		<div id="test5" class="col s12">
			<div id="content">
				<table class="table table-striped">
					<thead>
						<tr>
							<th>ENDERECO</th>
							<th>CELULA</th>
						</tr>
					</thead>
					%i = 0
					%while i != 256:
						<tr>
							<td>
								{{i}}
							</td>
							<td>
								{{memp.celulas[i]}}
							</td>
						</tr>
						%i = i+1
					%end
				</table>
			</div>
		</div>
	</div>

  <!--Import jQuery before materialize.js-->
  <script type="text/javascript" src="static/js/jquery-2.1.1.min.js"></script>
  <script type="text/javascript" src="static/js/jquery.mask.js"></script>
  <script type="text/javascript" src="static/js/materialize.min.js"></script>
  <script type="text/javascript" src="static/js/script.js"></script>
</body>

</html>

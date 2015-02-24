# Tarefa proposta para desenvolver um leilao de produtos usando dicionario, o programa deve conter tres dicionarios:
#	- Produtos
#	- Clientes
#	- Ofertas

def f_cadastraProdutos(dicP):
	nomeP, valor = "", 0.0
	
	print("\n\n------------------------- Cadastro de Produtos ----------------------------")
	nomeP = input("Informe o nome do Produto: ")
	while nomeP != "":
		if nomeP in dicP:
			print("Produto ja cadastrado!.")
		else:
			valor = float(input("Informe o valor do produto '%s': " %(nomeP)))
			dicP[nomeP] = valor
		#fim if
		print("\n------------------------- Cadastro de Produtos ----------------------------")
		nomeP = input("Informe o nome do Produto: ")
	#fim while	
#fim funcao

def f_cadastraClientes(dicC):
	cpf, nomeC, endereco = "", "", ""
	lst = []
	
	print("\n\n------------------------- Cadastro de Clientes ----------------------------")
	cpf = input("Informe o CPF do Cliente: ")
	while cpf != "":
		if cpf in dicC:
			print("Cliente ja cadastrado!.")
		else:
			nomeC = input("Informe o nome do cliente '%s': " %(cpf))
			endereco = input("Informe o endereco do cliente '%s': " %(cpf))
			lst = [nomeC, endereco]
			dicC[cpf] = lst
		#fim if
		print("\n\n------------------------- Cadastro de Clientes ----------------------------")
		cpf = input("Informe o CPF do Cliente: ")
	#fim while	
#fim funcao

def f_cadastraLances(dicC, dicP):
	dicAux, dicLancesAux = {}, {}
	cpf, nomeP, lance = "", "", 0.0
	tpl = ()
	
	for chave, valor in dicP.items():
		val = [tpl, valor, False]
		dicAux[chave] = val
	#fim for
	
	print("\n\n------------------------- Cadastro de Lances ----------------------------")
	cpf = input("Informe o seu CPF: ")
	while cpf != "":
		if cpf not in dicC:
			print("Cliente nao encontrado!.")
		else:
			print("")
			imprime_dados(dicAux)
			nomeP = input("\nInforme o produto que deseje dar um Lance: ")
			if nomeP not in dicP:
				print("Produto nao encontrado!.")
			else:
				tpl = (nomeP, cpf)
				lance = float(input("Informe um lance: "))
				while lance <= dicAux[nomeP][1]:
					print("O valor do lance nao pode ser menor que o valor atual")
					lance = float(input("Informe um lance: "))
				#fim while
				dicAux[nomeP] = [tpl, lance, True]
			#fim if
		#fim if
		print("\n\n---------------------------- Cadastro de Lances ------------------------------")
		cpf = input("Informe o seu CPF: ")
	#fim while
	
	for chave, valor in dicAux.items():
		if valor[2]:
			val = valor[1]
			dicLancesAux[valor[0]] = val
		#fim if
	#fim for	
	
	return dicLancesAux
#fim funcao

def imprime_dados(dic):
	for chave, valor in dic.items():
		print("%s: %.2f" %(chave, valor[1]))
	#fim ofr
#fim funcao

def f_impremeRelatorio(dicC, dicL):
	print("\n###########################################################################")
	print("\n------------------------- Relatorio dos Lances ----------------------------")
	for chave, valor in dicL.items():
		print("%s\t%.2f\t%s\t%s" %(chave[0], valor, chave[1], dicC[chave[1]][0]))
	#fim for
	print("")
#fim funcao

def main():
	dicProdutos, dicClientes, dicLances =  {}, {}, {}
	
	f_cadastraProdutos(dicProdutos)
	f_cadastraClientes(dicClientes)
	dicLances = f_cadastraLances(dicClientes, dicProdutos)
	
	#print(dicProdutos)
	#print(dicClientes)
	#print(dicLances)
	
	f_impremeRelatorio(dicClientes, dicLances)
	
	return 0
#fim main

if __name__ == '__main__':
	main()
#fim if

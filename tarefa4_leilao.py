# Tarefa proposta para desenvolver um leilao de produtos usando dicionario, o programa deve conter tres dicionarios:
#	- Produtos
#	- Clientes
#	- Ofertas

def f_cadastraProdutos(dicP):
	nome, valor = "", 0.0
	
	print("\n\n------------------------- Cadastro de Produtos ----------------------------")
	nome = input("Informe o nome do Produto: ")
	while nome != "":
		if nome in dicP:
			print("Produto ja cadastrado!.")
		else:
			valor = float(input("Informe o valor do produto '%s': " %(nome)))
			dicP[nome] = valor
		#fim if
		print("\n------------------------- Cadastro de Produtos ----------------------------")
		nome = input("Informe o nome do Produto: ")
	#fim while	
#fim funcao

def f_cadastraClientes(dicC):
	cpf, nome, endereco = "", "", ""
	lst = []
	
	print("\n\n------------------------- Cadastro de Clientes ----------------------------")
	cpf = input("Informe o CPF do Cliente: ")
	while cpf != "":
		if cpf in dicC:
			print("Cliente ja cadastrado!.")
		else:
			nome = input("Informe o nome do cliente '%s': " %(cpf))
			endereco = input("Informe o endereco do cliente '%s': " %(cpf))
			lst = [nome, endereco]
			dicC[cpf] = lst
		#fim if
		print("\n\n------------------------- Cadastro de Clientes ----------------------------")
		cpf = input("Informe o CPF do Cliente: ")
	#fim while	
#fim funcao

def f_cadastraLances(dicC, dicP):
	dicAux, dicLancesAux = {}, {}
	cpf, nome, lance = "", "", 0.0
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
			nome = input("\nInforme o produto que deseje dar um Lance: ")
			if nome not in dicP:
				print("Produto nao encontrado!.")
			else:
				tpl = (cpf, nome)
				lance = float(input("Informe um lance: "))
				while lance <= dicAux[nome][1]:
					print("O valor do lance nao pode ser menor que o valor atual")
					lance = float(input("Informe um lance: "))
				#fim while
				dicAux[nome] = [tpl, lance, True]
			#fim if
		#fim if
		print("\n\n------------------------- Cadastro de Lances ----------------------------")
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
		print("%s\t%.2f\t%s\t%s" %(chave[1], valor, chave[0], dicC[chave[0]][0]))
	#fim for
	print("")
#fim funcao

def main():
	dicProdutos = {"arroz": 2.50, "feijao": 3.20, "carne": 12.00}
	dicClientes = {"123": ["joao", "rua 1"], "456": ["maria", "rua 2"], "789": ["jose", "rua 3"]}
	dicLances =  {}
	
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

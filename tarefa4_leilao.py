# Tarefa proposta para desenvolver um leilao de produtos usando dicionario, o programa deve conter tres dicionarios:
#	- Produtos
#	- Clientes
#	- Ofertas

def f_cadastraProdutos(dicP):
	nome, valor = "", 0.0
	
	print("-----------------------------------------------------")
	nome = input("Informe o nome do Produto: ")
	while nome != "":
		if nome in dicP:
			print("Produto ja cadastrado!.")
		else:
			valor = float(input("Informe o valor do produto %s: " %(nome)))
			dicP[nome] = valor
		#fim if
		print("-----------------------------------------------------")
		nome = input("Nome do Produto: ")
	#fim while	
#fim funcao

def f_cadastraClientes(dicC):
	cpf, nome, endereco = "", "", ""
	lst = []
	
	print("-----------------------------------------------------")
	cpf = input("Informe o CPF do Cliente: ")
	while cpf != "":
		if cpf in dicC:
			print("Cliente ja cadastrado!.")
		else:
			nome = input("Informe o nome do cliente %s: " %(cpf))
			endereco = input("Informe o endereco do cliente %s: " %(cpf))
			lst = [nome, endereco]
			dicC[cpf] = lst
		#fim if
		print("-----------------------------------------------------")
		cpf = input("Nome do Produto: ")
	#fim while	
#fim funcao

def f_cadastraLances(dicL, dicP, dicC):
	cpf, nome = "", ""
	tpl = ()
	
	cpf = input("Informe o seu CPF: ")
	while cpf != "":
		if cpf not in dicC:
			print("Cliente nao encontrado!.")
		else:
			for i in range(len(dicP)):
				for j in range(len(dicL)):
					if dicP[i] in dicL[j][0]:
						print()
				#fim for
			#fim for
			nome = input("Informe o produto que deseje dar um Lance: ")
		#fim if
		cpf = input("Informe o seu CPF: ")
	#fim while
	
#fim funcao

def main():
	dicProdutos, dicClientes, dicOfertas = {}, {}, {}
	
	f_cadastraProdutos(dicProdutos)
	f_cadastraClientes(dicClientes)
	f_cadastraLances(dicLances, dicProdutos, dicClientes)
	
	print(dicProdutos)
	print(dicClientes)
	
	return 0
#fim main

if __name__ == '__main__':
	main()
#fim if

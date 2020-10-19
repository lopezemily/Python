nomes = ['emily', 'jessica', 'allan', 'lilian']
print(nomes)

# NOVOS ELEMENTOS
# no final da lista
nomes.append('melissa')
print(nomes)

# em uma posicao especifica da lista
nomes.insert(3, 'maria')
print(nomes)

# REMOVENDO ELEMENTOS
# removendo qualquer elemento com posicao conhecida - nao eh possivel acessar seu conteudo apos a removao
del nomes[1]
print(nomes)

# removendo o ultimo elemento da lista - eh possivel armazenar valor removido em uma variavel
removido = nomes.pop()
print(nomes)

# removendo um valor especifico da lista
excluir = 'maria'
nomes.remove(excluir)
# também pode ser escrito: nomes.remove('maria')
print(nomes)

# ORGANIZANDO LISTA
# ordem alfabetica permanente
nomes.sort()
print(nomes)

# ordem alfabetica inversa permanente
nomes.sort(reverse=True)
print(nomes)

# ordenando temporariamente
frutas = ['banana', 'uva', 'pera', 'abacaxi']
print(frutas)
print(sorted(frutas))

# inverter ordem original da lista (nao ordena)
frutas.reverse()
print(frutas)

# descobrir tamanho da lista
tamanho = len(frutas)
print(tamanho)

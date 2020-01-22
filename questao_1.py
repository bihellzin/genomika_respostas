# Armazenamento de todos os reads
bases = list(map(str, input().split()))

# Variável final iniciada com o primeiro valor da lista contendo todas as bases
super_string = bases.pop(0)

while bases:
    read = bases.pop(0)

    # Estando o read já presente na super string, não há necessidade de colocar novamente
    if read in super_string:
        pass

    else:
        # O pedaço do read possui 20% do tamanho do read completo
        pedaco = read[:int(len(read) * 0.2)]


        # Verificação para ver se o pedaço está presente na super string, caso não esteja, o read será colocado
        # novamente na lista de reads

        if pedaco in super_string:

            # Percorro somente até onde importa
            for j in range(int(len(super_string) * 0.9)):

                # Caso o pedaço do read esteja presente na super string, o número de letras já presentes na string é
                # contabilizado e adiciono somente as letras restantes do read
                if super_string[j:j + len(pedaco)] == pedaco:
                    qnt_caracteres_existente = len(super_string[j:j + len(pedaco)]) \
                                               + len(super_string[j + len(pedaco):])
                                        
                    
                    
                    if super_string[j: j + qnt_caracteres_existente] == read[0: qnt_caracteres_existente]:
                        super_string += read[qnt_caracteres_existente:]
                        break

        else:
            bases.append(read)

print(super_string)
input('')

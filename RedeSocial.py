
pessoas = ["Alice", "Bob", "Carol", "Danielle"]
for i,pessoas in enumerate(pessoas):
    print(str(i)+":" + pessoas)

print("----------------------")

amizades = [[0,0,0,1],[1,0,1,1],[0,0,0,1],[1,1,0,0]]
for i in range(0, 4):
    for j in range(0, 4):
        amizades[i][j]
        print(f'[{amizades[i][j]}]', end= ' ')
    print()

print("----------------------")

def exibe_amigos(pessoas, amizades, nomePessoa):
    for i in range(len(pessoas)):
        if pessoas[i] in nomePessoa:
            print(nomePessoa)
        for j in range(0, 4):
                if amizades[i][j] == 1:
                    print("Lista amigos de " + nomePessoa + ": ")
                    return print(pessoas[j])
        else:
                print("Não tem amigos!")
    else: 
        return print("Nome não encontrado!")


def exibe_amigos_comum(pessoas, nomePessoaX, nomePessoaY):
    tam = len(pessoas)
    
    for i in range(tam):
        if pessoas[i] in nomePessoaX:
            for j in range(tam): 
                if pessoas[j] in nomePessoaY:
                    for m in range(0, 4):
                        if amizades[i][m] == 1 and amizades [j][m] == 1:
                            print("Amigos em comum entre " + nomePessoaX + " e " + nomePessoaY +
                        ": " )
                        return print(pessoas[m])
            else: 
                print("Não tem amigos em comum.")
    else: 
        return print(".")

# chama a função exibe_amigos
tentativa = exibe_amigos(pessoas = ["Alice", "Bob", "Carol", "Danielle"], amizades = [[0,0,0,1],[1,0,1,1],[0,0,0,1],[1,1,0,0]], nomePessoa="Bob")

print("----------------------")

#chama a função exibe_amigos_comum
tent = exibe_amigos_comum(pessoas=["Alice", "Bob", "Carol", "Danielle"], nomePessoaX="Bob", nomePessoaY="Danielle")




    


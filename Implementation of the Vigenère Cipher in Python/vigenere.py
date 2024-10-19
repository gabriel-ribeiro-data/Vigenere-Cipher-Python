def criptografia_vigenere(texto, chave):
    texto_criptografado = ""
    tamanho_chave = len(chave)

    #contador que tem como limite o tamanho da string de entrada
    for i in range(len(texto)):
        
        #recebe o caractere da string
        caractere = texto[i]
        
        #se o caractere for alfabético
        if caractere.isalpha():
            
            #Guarda na variavel caractere_chave, o valor  armazenado  na string chave, que está na posição do resto da divisão entre o contador pelo tanto de caracteres na chave
            #Se a entrada for menor que a chave, o "%" garante que  que a chave seja repetida
            caractere_chave = chave[i % tamanho_chave]


            #Calculo o deslocamento de posições na cifra de vigenère de acordo com o valor numérico retornado por "ord" (cada string equivale à uma unidade ASCII)
            #O valor numérico retornado da variável caractere_chave em maiúsculo subtraido pelo valor numérico de "A"
            deslocamento = ord(caractere_chave.upper()) - ord('A')

            #se o caractere for maiúsculo
            if caractere.isupper():
                
                #"ord(caractere) - ord('A')" calcula a posição da letra entre 0 e 25 no alfabeto maiúsculo
                #Depois será somado ao deslocamento da cifra de vigenère
                #"% 26" garante que o resultado esteja no intervalo de letras de "A" à "Z"
                #"+ ord('A')" garante que o caractere permaneça maiúsculo
                caractere_criptografado = chr((ord(caractere) - ord('A') + deslocamento) % 26 + ord('A'))
                
            #caso contrário
            else:
                
                #"ord(caractere) - ord('a')" calcula a posição da letra entre 0 e 25 no alfabeto maiúsculo
                #Depois será somado ao deslocamento da cifra de vigenère
                #"% 26" garante que o resultado esteja no intervalo de letras de "a" à "z"
                #"+ ord('a')" garante que o caractere permaneça minúsculo
                caractere_criptografado = chr((ord(caractere) - ord('a') + deslocamento) % 26 + ord('a'))

            #armazena o caractere criptografado    
            texto_criptografado += caractere_criptografado
            
        else:
            
            #armazenao caractere que não pode ser criptografado
            texto_criptografado += caractere

    #retorna a string criptografada
    return texto_criptografado

def descriptografia_vigenere(texto_criptografado, chave):
    texto_descriptografado = ""
    tamanho_chave = len(chave)

    #contador que tem como limite o tamanho da string de entrada
    for i in range(len(texto_criptografado)):
        caractere = texto_criptografado[i]
        #se o caractere for alfabético
        if caractere.isalpha():
            #Guarda na variavel caractere_chave, o valor  armazenado  na string chave, que está na posição do resto da divisão entre o contador pelo tanto de caracteres na chave
            #Se a entrada for menor que a chave, o "%" garante que  que a chave seja repetida
            caractere_chave = chave[i % tamanho_chave]

            #Calculo o deslocamento de posições na cifra de vigenère de acordo com o valor numérico retornado por "ord" (cada string equivale à uma unidade ASCII)
            #O valor numérico retornado da variável caractere_chave em maiúsculo subtraido pelo valor numérico de "A"
            deslocamento = ord(caractere_chave.upper()) - ord('A')  

            #se o caractere for maiúsculo
            if caractere.isupper():

                #"ord(caractere) - ord('A')" calcula a posição da letra entre 0 e 25 no alfabeto maiúsculo
                #Depois será subtraido ao deslocamento da cifra de vigenère, assim permite retroceder posições na criptografia
                #"% 26" garante que o resultado esteja no intervalo de letras de "A" à "Z"
                #"+ ord('A')" garante que o caractere permaneça maiúsculo
                caractere_descriptografado = chr((ord(caractere) - ord('A') - deslocamento) % 26 + ord('A'))
            #caso contrário
            else:

                #"ord(caractere) - ord('a')" calcula a posição da letra entre 0 e 25 no alfabeto maiúsculo
                #Depois será subtraido ao deslocamento da cifra de vigenère, assim permite retroceder posições na criptografia
                #"% 26" garante que o resultado esteja no intervalo de letras de "a" à "z"
                #"+ ord('a')" garante que o caractere permaneça maiúsculo
                caractere_descriptografado = chr((ord(caractere) - ord('a') - deslocamento) % 26 + ord('a'))

            #armazena o caractere descriptografado 
            texto_descriptografado += caractere_descriptografado
        else:
            #armazenao caractere que não pode ser descriptografado
            texto_descriptografado += caractere
    
    return texto_descriptografado

def entrada_char(cadeiaChar, aviso):
    #Estrutura de repetição sem contador, que finaliza com um break
    while True:
        
        #captura a entrada do usuário
        texto = input(cadeiaChar)

        #Se os caracteres da string forem alfabéticos, quebra a estrutura de repetição
        if all(caractere.isalpha() for caractere in texto) == True:
            break

        #Caso contrário, será emitido um aviso
        else:
            print(aviso)
    return texto
    

def entrada_operacao(cadeiaChar, comparaN1, comparaN2, aviso):
    
    #Estrutura de repetição sem contador, que finaliza com um break
    while True:

        #captura a entrada do usuário
        resposta = input(cadeiaChar)

        #Se a entrada for igual a comparaN1 ou comparaN2, quebra a estrutura de repetição
        if resposta == comparaN1 or resposta == comparaN2:
            break

        #Caso contrário, será emitido um aviso
        else:
            print(aviso)
            
    return resposta

def encerrar_sistema(cadeiaChar, comparaN1, comparaN2, aviso):
    
    #Estrutura de repetição sem contador, que finaliza com um break
    while True:

        #captura a entrada do usuário e torna maiúscula
        resposta = input(cadeiaChar).upper()

        #Se a entrada for igual a comparaN1 ou comparaN2, quebra a estrutura de repetição
        if resposta == comparaN1 or resposta == comparaN2:
            break

        #Caso contrário, será emitido um aviso
        else:
            print(aviso)

    return resposta

print("-----------------------------------------------------------------\n")
print("-                       CIFRA DE VIGENÈRE                      -\n")
print("-----------------------------------------------------------------")
print("AVISOS:\n    •Caracteres especiais e numéricos não serão criptografados\n    •A chave só permite caracteres alfabéticos\n")

while True:

    #Escolhendo a operação desejada
    opcao = entrada_operacao("Qual operação deseja fazer? \n   1-Criptografar \n   2-Descriptografar \nR: ", '1', '2', "\nDigite somente '1' ou '2': ")

    #Se desejar criptografar
    if opcao == '1':
        texto = input("\nTexto para criptogravar: ")
        chave = entrada_char("Chave: ", "\nDigite somente caracteres alfabéticos")
        
        #criptografia_vigenere() criptografa uma string por meio de uma chave
        textoCrip = criptografia_vigenere(texto, chave) 
        print("\nTexto criptografado:", textoCrip)

    #Se desejar descriptografar
    else:
        # Teste
        texto = input("\nTexto criptografado: ")
        chave = entrada_char("Chave: ", "\nDigite somente caracteres alfabéticos")

        #descriptografia_vigenere() descriptografa uma string por meio de uma chave
        textoDesc = descriptografia_vigenere(texto, chave)


        print("\nTexto descriptografado:", textoDesc)
    
    resposta = encerrar_sistema("\nDeseja continuar (S/N)?: ", "S", "N", "\nDigite somente 'S' ou 'N'")
    print("\n")

    #Se a resposta for "N", encerra a operação
    if  resposta == 'N':
        print("---OPERAÇÃO FINALIZADA!---")
        break
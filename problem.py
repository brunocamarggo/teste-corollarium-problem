import time

# Explicação da minha lógica:

# O problema pede a soma de todos os números de 10 dígitos que seguem a propriedade
# de ser um "pandigital".

# Portanto, a solução mais trivial seria justamente calcular todas as permutações existente para
# o número de 10 dígitos, mas como o dígito "0" a esquerda não possui representatividade, 
# o número de permutações necessárias é um pouco menor de 10!, sendo 9 x 9! = 3265920.and

# Desta forma, a função "permutations" calcula de forma recursiva todas as permutações para uma string.
# Para cada permutação, utilizo a função "is_pandigital" para verificar se um número é "pandigital", sendo
# eu acumulo seu valor com os demais.

#
# Esta solução evidentimente uma solução não ótima dedivo o seu tempo necessário para a execução.
#

def permutations(string, step = 0):
    # Função que gera todas as permutações de uma string.
    # Esta função é uma função recursiva cuja a lógica foi inicialmente apresentada por Eric Roberts.
    # Mais informaçoes em:
    # https://www.ime.usp.br/~pf/mac0122-2003/aulas/permut.html
    global sum_

    if step == len(string):
        # print "".join(string)
        if string[0] != '0':
            if is_pandigital(''.join(string)):
                sum_ += int(''.join(string))

    for i in range(step, len(string)):        
        string_copy = [character for character in string]
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        permutations(string_copy, step + 1)

def is_pandigital(n):
    if float(n[1:4]) % 2 == 0 and float(n[2:5]) % 3 == 0 and float(n[3:6]) % 5 == 0 and float(n[4:7]) % 7 == 0 and float(n[5:8]) % 11 == 0 and float(n[6:9]) % 13 == 0 and float(n[7:10]) % 17 == 0:
        return True
    else:
        return False
if __name__ == "__main__":
    ts = time.time()
    sum_ = 0
    permutations("0123456789", 0)
    tend = time.time()
    time_ = tend - ts
    print(str(sum_) + " ("+str(time_)+") sec")  
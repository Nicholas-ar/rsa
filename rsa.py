import os
import math

def mainMenu():
    user_input = menuText()
    while ( user_input != 4):
        if user_input == 1:
            menuPublicKey()
            user_input = menuText()
        elif user_input == 2:
            menuEncrypt()
            user_input = menuText()
        elif user_input == 3:
            menuDecrypt()
            user_input = menuText()
        else:
            user_input = int(input('Informe uma opção válida\n Digite novamente a opção:'))


def menuText():
    os.system('clear')
    print ('----------- Criptografia RSA -----------\n')
    print ('1. Gerar chave pública')
    print ('2. Encriptar')
    print ('3. Desencriptar')
    print ('4. Encerrar')
    user_input = int(input('Informe o número da opção desejada: '))
    return user_input


def menuPublicKey():
    os.system('clear')
    print ('----------- Criptografia RSA -----------\n')
    print ('Gerar chave pública\n')
    first_prime = 0
    second_prime = 0

    while ( first_prime * second_prime < 256):
        first_prime = int(input('Informe o primeiro número primo: '))
        while (isPrime(first_prime) != True):
            first_prime = int(input('O número deve ser primo, informe novamente um número: '))

        second_prime = int(input('Informe o segundo número primo: '))
        while (isPrime(second_prime) != True):
            second_prime = int(input('O número deve ser primo, informe novamente um número: '))

        if(first_prime * second_prime < 256):
            print('O produto dos números primos tem que ser maior que 256. Digite novamente os números primos')

    phi = (first_prime - 1) * (second_prime - 1)
    exponent = int(input('Informe o expoente: '))
    while(mdc(exponent,phi) != 1):
        exponent = int(input('O expoente deve ser relativamente primo ao produto dos números primos menos 1. Informe novamente o expoente: '))

    file_name = input('Informe o nome desejado para o arquivo: ')
    file_name += '.txt'
    createPublicKey(first_prime,second_prime,exponent,file_name)



def menuEncrypt():
    os.system('clear')
    print ('----------- Criptografia RSA -----------\n')
    print ('Encriptar Mensagem\n')
    message = input(' Informe a mensagem que você deseja encriptar:')
    public_key = int(input(' Informe a chave pública:'))
    exponent = int(input('Informe o expoente utilizado:'))
    file_name = input('Informe o nome do arquivo para ser salvo a mensagem criptografada:')
    encryptMessage(message,public_key,exponent, file_name)

def menuDecrypt():
    os.system('clear')
    print('----------- Criptografia RSA -----------\n')
    print ('Descriptar Mensagem\n')

    first_prime = int(input('Informe o primeiro número primo utilizado: '))
    second_prime = int(input('Informe o segundo número primo utilizado: '))
    exponent = int(input('Informe o expoente utilizado: '))

    file_name = input('Informe o nome do arquivo que esta a mensagem encriptada:')
    file_name_decrypt = input('Informe o nome do arquivo que deseja armazenar a mensagem:')
    decryptMessage(first_prime,second_prime,exponent,file_name,file_name_decrypt)

def decryptMessage(firstPrime,secondPrime,exponent,fileName,fileDecrypt):
    D = 2
    PHI = (firstPrime-1)*(secondPrime-1)
    
    fileName += '.txt'
    fileDecrypt += '.txt'

    while ((D*exponent) % PHI != 1):
        D+=1

    N = firstPrime * secondPrime
    file = map(int ,open(fileName).read().split())

    decrypt = open(fileDecrypt,'w')
    for number in file:
        t = pow(number,int(D),N)
        decrypt.write('%s' % chr(t))

    decrypt.close()

    print ('O arquivo foi gerado com sucesso!')
    saida = input('Pressione ENTER para continuar...')
        


def encryptMessage(message,publicKey,exponent,fileName):
    fileName += '.txt'
    file = open(fileName,'w')
    d = 2
    for char in message:
        value = pow(ord(char),exponent) % publicKey
        file.write('%d ' % value)
    file.close()

    print ('O arquivo com a mensagem criptografa foi gerado com sucesso!')
    saida = input('Pressione ENTER para continuar...')

def createPublicKey(fP,sP,exponent,fileName):
    public_key = fP * sP
    file = open(fileName,'w')
    file.write('%s %s' % (public_key, exponent))
    if os.path.isfile(fileName) == True:
        print ('Arquivo criado com sucesso! Sua chave pública gerada é %s e o expoente utilizado foi %s.' % (public_key, exponent))
    else:
        print ('Não foi possivel criar o arquivo')
    file.close()
    saida = input('Pressione ENTER para continuar...')

def mdc(a,b):
    if b == 0:
        return a
    else:
        return mdc(b,a%b)

def isPrime(n):
    if n == 2 or n == 3:
        return True

    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False

    if n != 1:
        return True
    else:
        return False

mainMenu()

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

    totient = (first_prime - 1) * (second_prime - 1)

    print('Sugerimos utilizar algum destes expoentes:', end='')
    generateExponent(totient)
    exponent = int(input('Informe o expoente desejado:'))

    while(mdc(exponent,totient) != 1):
        exponent = int(input('O expoente deve ser relativamente primo ao produto dos números primos menos 1. Informe novamente o expoente: '))

    createPublicKey(first_prime,second_prime,exponent)

def menuEncrypt():
    os.system('clear')
    print ('----------- Criptografia RSA -----------\n')
    print ('Encriptar Mensagem\n')
    message = input('Informe a mensagem que você deseja encriptar:')
    public_key = int(input('Informe a chave pública:'))
    exponent = int(input('Informe o expoente utilizado:'))
    encryptMessage(message,public_key,exponent)

def menuDecrypt():
    os.system('clear')
    print('----------- Criptografia RSA -----------\n')
    print ('Descriptar Mensagem\n')

    first_prime = int(input('Informe o primeiro número primo utilizado: '))
    second_prime = int(input('Informe o segundo número primo utilizado: '))
    exponent = int(input('Informe o expoente utilizado: '))
    message = input('Informe a mensagem encriptada:')
    
    decryptMessage(first_prime,second_prime,exponent,message)

def decryptMessage(firstPrime,secondPrime,exponent,message):
    D = 2
    totient = (firstPrime-1)*(secondPrime-1)
    N = firstPrime * secondPrime

    while ((D*exponent) % totient != 1):
        D+=1
    
    decrypt = open('decrypted.txt','w')
    numbers = message.split()

    for number in message.split():
        t = pow(int(number),int(D),N)
        decrypt.write('%s' % chr(t))

    print ('O arquivo foi gerado com sucesso!')
    saida = input('Pressione ENTER para continuar...')
        


def encryptMessage(message,publicKey,exponent):
    file = open('encrypted.txt','w')

    for char in message:
        value = pow(ord(char),exponent) % publicKey
        file.write('%d ' % value)
    file.close()

    print ('O arquivo com a mensagem criptografa foi gerado com sucesso!')
    saida = input('Pressione ENTER para continuar...')

def createPublicKey(fP,sP,exponent):
    public_key = fP * sP
    file = open('public_key.txt','w')
    private = open('private_key.txt', 'w')
    file.write('%s %s' % (public_key, exponent))
    private.write('%s %s' % (fP,sP))
    if os.path.isfile('public_key.txt') == True:
        print ('Arquivo criado com sucesso! Sua chave pública gerada é %s e o expoente utilizado foi %s.' % (public_key, exponent))
    else:
        print ('Não foi possivel criar o arquivo')
    file.close()
    private.close()
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

def generateExponent(totient):
    quantity = 10
    exponent = 2

    print('(', end='')
    while(quantity):
        while(mdc(exponent,totient) != 1):
            exponent += 1
        print('%d' % exponent, end='')
        exponent+=1
        if(quantity != 1):
            print(',',end='')
        else:
            print(')')
        quantity-=1


mainMenu()

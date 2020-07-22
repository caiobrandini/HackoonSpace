#Verificador de Senhas
from os import system
import random
import time
from tqdm import trange
import _thread as td
from unicodedata import normalize

fim = False
def logo():
    print('''*****************************************************************
     _____         _____ _______          ______  _____  _____  
    |  __ \ /\    / ____/ ____\ \        / / __ \|  __ \|  __ \ 
    | |__) /  \  | (___| (___  \ \  /\  / / |  | | |__) | |  | |
    |  ___/ /\ \  \___ \\___  \  \ \/  \/ /| |  | |  _  /| |  | |
    | |  / ____ \ ____) |___) |  \  /\  / | |__| | | \ \| |__| |
    |_| /_/    \_\_____/_____/    \/  \/   \____/|_|  \_\_____/ 
      _____ _    _ ______ _____ _  ________ _____ 
     / ____| |  | |  ____/ ____| |/ /  ____|  __ \ 
    | |    | |__| | |__ | |    |   /| |__  | |__) |
    | |    |  __  |  __|| |    |  < |  __| |  _  /
    | |____| |  | | |___| |____| . \| |____| | \ \ 
     \_____|_|  |_|______\_____|_|\_\______|_|  \_\ 
    \n*****************************************************************''')

def barra():
    global fim
    fim = False
    for i in trange (100):
        time.sleep(0.015)
    fim = True
    
def requisitos(x):
    #Verifica se uma dada senha possui todos os requisitos de uma senha forte
    
    nivel = 0
    letrasmin = 0
    letrasmai = 0
    senha = list(x)
    tamanho = False
    cEspecial = False
    digitos = False
    
    if len (x) > 7:
        nivel = nivel + 1
        tamanho = True
        
    if x.isalnum() == False:
        nivel = nivel + 1
        cEspecial = True
    
    for i in senha:
        if i.islower() == True:
            letrasmin = letrasmin + 1
            
        if i.isupper() == True:
            letrasmai = letrasmai + 1

        if i.isdigit() == True:
            digitos = True
    print('\n\nPrincipais vulnerabilidades:\n')
    if letrasmin == 0:
        print('*Ausência de letras minúsculas')
    else:
        if letrasmin/(letrasmin+letrasmai) < 0.2:
            print ('*Poucas letras minúsculas')
    if letrasmai == 0:
        print('*Ausência de letras maiúsculas')
    else:
        if letrasmai/(letrasmin+letrasmai) <0.2:
            print ('*Poucas letras maiúsculas')
    if cEspecial == False:
        print ('*Ausência de caracteres especiais')
    if digitos == False:
        print ('*Ausência de caracteres numéricos')
    if tamanho == False:
        print ('*Senha pequena (menos de 8 caracteres)')
        

def listaDeSenhas(x):
    #Recebe uma senha e imprime na tela se a senha digitada consta no banco de dados de senhas comuns

    global fim
    print('\nPesquisando na lista de senhas recorrentes...\n')
    now = time.time()
    y = x.lower()
    encontrada = False
    arquivo = open("passwords.txt","r",errors='ignore')
    while encontrada == False:
        comp = (arquivo.readline()).lower()[:-1]
        if comp == y:
            encontrada = True
            tempo = round(time.time()- now,2)
            break
        if comp == 'fimdalista':
            tempo = round(time.time() - now,2)
            break
    while not fim:
        pass

    if encontrada == True:
        print ('\n* AVISO: sua senha foi encontrada em listas de senhas comuns *')
        print('\nTempo de busca:',tempo,'segundos')
    else:
        print('\nNada encontrado :)')
        print('\nTempo de busca:',tempo,'segundos')
    fim = 10

def randPass():
    #Gera senhas seguras de forma aleatórea
    
    minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    maiusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    cEspeciais = ['!','@','#', '$','%','&', '*', '-','+', '=','|','(',')','{','}','[',']',':',';','<','>','.','?','/']
    senhalista = random.sample(minusculas, 3)+random.sample(maiusculas, 4)+random.sample(numeros, 2)+random.sample(cEspeciais,2)
    random.shuffle(senhalista)
    senha = ''.join(senhalista)
    return senha

def wordPass():
    #Gera senhas seguras através da junção de palavras aleatóreas
    word = open('words.txt','r')
    senha = ''
    l = random.randint(2,5)
    while l > 0:
        n = random.randint(1,7763)
        word.seek(0)
        while n > 0:
            linha = list(word.readline())
            n = n - 1
        del linha [-1]
        linha = ''.join(linha)
        linha = removerAcentos(linha)
        senha = senha + linha.capitalize()
        l = l - 1
    return(senha)
    
    
def removerAcentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
  
def main():
    global fim
    system("cls")
    logo()
    while True:
        fim = False
        n = input('\n1 - Verificar senha\n2 - Gerador de senha forte\n3 - Sair\n ')
        system("cls")
        if n.isdigit() == False:
            pass
        else:
            n = int(n)
        if n == 1:
            logo()
            senha = input('\nDigite a senha a ser testada: ')
            requisitos(senha)
            td.start_new_thread(listaDeSenhas,(senha,))
            td.start_new_thread(barra,())
            while fim != 10:
                time.sleep(0.01)
                                
        if n == 2:
            logo()
            print ('\nopção 1: ', randPass(),end = '')
            print('     opção 2:', wordPass(), '\n')
            print ('opção 3: ', randPass(),end = '')
            print('     opção 4:', wordPass(), '\n')
            print ('opção 5: ', randPass(),end = '')
            print('     opção 6:', wordPass(), '\n')
            print ('opção 7: ', randPass(),end = '')
            print('     opção 8:', wordPass(), '\n')
            print ('opção 9: ', randPass(),end = '')
            print('     opção 10:', wordPass(), '\n')
        if n == 3:
            break
    
main()

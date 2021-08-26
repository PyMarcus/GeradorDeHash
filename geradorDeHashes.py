import hashlib, sys


def geraHash(escolha, palavra):
    if escolha == 1:
        result = hashlib.md5("{}".format(palavra).encode('utf-8'))
        print(f"A string informada possui o hash em md5: \n{result.hexdigest()}")
    if escolha == 2:
        result = hashlib.sha256("{}".format(palavra).encode('utf-8'))
        print(f"A string informada possui o hash em sha256: \n{result.hexdigest()}")
    if escolha == 3:
        result = hashlib.sha256("{}".format(palavra).encode('utf-8'))
        print(f"A string informada possui o hash em sha512: \n{result.hexdigest()}")
    if escolha == 4:
        result = hashlib.sha1("{}".format(palavra).encode('utf-8'))
        print(f"A string informada possui o hash em sha1: \n{result.hexdigest()}")

def funcao():
    print()
    palavra = input("Informe a palavra: ")
    print()
    return palavra



if __name__ == '__main__':
    opcoes = list(range(1, 5))
    print()
    print("""88,dPYba,,adPYba,   ,adPPYba, 8b,dPPYba,  88       88  
88P'   "88"    "8a a8P_____88 88P'   `"8a 88       88  
88      88      88 8PP""""""" 88       88 88       88  
88      88      88 "8b,   ,aa 88       88 "8a,   ,a88  
88      88      88  `"Ybbd8"' 88       88  `"YbbdP'Y8  """)

    palavra = funcao()
    
    print("Digite 1- Para MD5")
    print("Digite 2- Para SHA256")
    print("Digite 3- Para SHA512")
    print("Digite 4- Para SHA1")
    try:
        escolha = int(input('>> '))
        if escolha in opcoes:
            pass 
        else:
            print('inválido')
            sys.exit(1)
    except ValueError:
        print("opção não reconhecível")
    else:
        geraHash(escolha, palavra)

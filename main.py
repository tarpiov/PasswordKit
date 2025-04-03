import re
import os
import random
import time
from colorama import Fore

banner = f"""{Fore.LIGHTGREEN_EX}
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗     ██╗  ██╗██╗████████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██║ ██╔╝██║╚══██╔══╝
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    █████╔╝ ██║   ██║   
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██╔═██╗ ██║   ██║   
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ██║  ██╗██║   ██║   
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═╝╚═╝   ╚═╝   
                                                                    {Fore.LIGHTMAGENTA_EX}By  @tarpiov                                                      
{Fore.RESET}                                                    
"""

def comprobarContra(password):
    

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):  # Mayúscula
        return False
    
    if not re.search(r"[a-z]", password):  # Minúscula
        return False
    
    if not re.search(r"[0-9]", password):  # Número
        return False
    
    if not re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?/~\-]", password):  # Símbolo
        return False

    return True


def generadorContra():

    letras = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numeros = list("0123456789")
    simbolos = list("!@#$%^&*()-_=+[];:,.<>?/|~")
    todas = letras + numeros + simbolos

    password = ''.join(random.sample(todas, 19))
    return f"Contraseña generada: {password}"



def main():

    while True:

        print(banner)
        print(f"\n\nOpciones:\n1. Comprobar seguridad de contraseña\n2. Generador de contraseña segura")
        opc = int(input("> "))

        if opc == 1:
            
            os.system("clear || cls")
            print(banner)
            password = input("Introduzca una contraseña: ")

            if comprobarContra(password) == True:
                print("Felicidades! Contraseña segura")
            else:
                print("Contraseña insegura!")

            time.sleep(4)

        
        elif opc == 2:

            print(generadorContra())
            time.sleep(4)

        else:

            print("Opcion invalida")
            time.sleep(2)

if __name__ == '__main__':
    main()

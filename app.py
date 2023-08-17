from modules.colors import *
import os, requests
from modules.motor import Dork
from platform import platform as pl
attributesSpecific = ['-', '+', '"', 'site:']
attirbutesNotSpecific = ['*', '']

def clear():
    if "indow" in pl():
        c = "cls"
    else:
        c = "clear"
    os.system(c)

def banner():
    print(f"""{O}
     _                     _                     
  __| |    ___      _ _   | |__    ___      _ _  
 / _` |   / _ \    | '_|  | / /   / -_)    | '_| 
 \__,_|   \___/   _|_|_   |_\_\   \___|   _|_|_  
_|'''''|_|'''''|_|'''''|_|'''''|_|'''''|_|'''''| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'
{G}By {P}Mrx04programmer{W}
""")
    global options
    options = f"""
{G}[1] {W}Buscar archivo
{G}[2] {W}Buscar un producto
{G}[3] {W}Buscar una persona en un sitio
{G}[4] {W}Busqueda especifica"""

def showoptions(option):
    clear()
    banner()
    if option == 1:
        archivo = input(f"{C}Archivo a buscar(sin extension):{W}")
        ext = input(f"{C}Extension(pdf,docx,etc): {W}")
        Dork.main(f"{archivo} filetype:{ext}")
    elif option == 2:
        i = 1
        producto = input(f"{C}Nombre o Serial producto: {W}")
        caracts = int(input(f"{C}Cuantas caracteristicas desea agregar: {W}"))
        core = f"{producto} "
        while i <= caracts:
            caracteristica = input(f"{C}Caracteristica #{i}: {W}")
            core += (f"+{caracteristica}")
            i+=1
        Dork.main(core)
    elif option == 3:
        i = 1
        sitio = input(f"{C}Sitio web relacionado : {W}")
        persona = input(f"{C}Persona: {W}")
        Dork.main(f" site:{sitio} {persona}")
    elif option == 4:
        s = input(f"{C}Texto a buscar: {W}")
        rest = int(input(f"{C}Restricciones[numero]: {W}"))
        cara = int(input(f"{C}Caracteristicas extra[numero]: {W}"))
        site = input(f"{C}Sitio en especifico(Default Ninguno): {W}")
        core = f"{s}"
        if rest >= 1:
            i = 1
            while i <= rest:
                restriccion = input(f"{C}Restriccion #{i}: {W}")
                core += (f" -{restriccion}")
                i+=1
        if cara >= 1:
            i = 1
            while i <= cara:
                caracteristica = input(f"{C}Caracteristica #{i}: {W}")
                core += (f" +{caracteristica}")
                i+=1
        if site != '':
            core += (f"site:{site}")
        Dork.main(core)

def main():
    banner()
    print(options)
    option = int(input(f"{R}[-> {W}"))
    showoptions(option)

if __name__ == '__main__':
    try:
        clear()
        main()
    except ValueError:
        clear()
        banner()
        print(f"{R}[-] {W}Por favor digite un número valido.")
    except requests.exceptions.HTTPError:
        print(f"{R}[+] {W}Se saturo el servidor o la conexión no es buena.")
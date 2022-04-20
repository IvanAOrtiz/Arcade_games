import random
import time
def funcionppt():
    print ("\t\t   ***INSTRUCCIONES***")
    print ("\nUsted jugará contra la computadora.\nLa computadora elije al azar entre: Piedra, Papel o Tijera (1, 2 ó 3); y usted también elige.\nSe comparan ambas elecciones y se le indicará al usuario si GANÓ, PERDIÓ o EMPATÓ.")

    print("Las reglas para definir el ganador son:")
    print("\t• Tijera vence a Papel.") 
    print("\t• Papel vence a Piedra.")
    print("\t• Piedra vence a Tijera.\n")

    print("En caso de presentar un caracter no valido, se indicará ERROR y se dará sólo una oportunidad más. Si falla en una segunda ocasión, GAME OVER")


    ppt = ["piedra", "papel", "tijera"]
    num = [0, 1, 2]
    val = ["1", "2", "3"]
    h = 0

    while h != 2:
        ec = random.choice(num)
        u = input("\n\nElija entre Piedra, Papel o Tijera (1, 2 ó 3): ")

        if u in val:
            u = int(u)
            print("La computadora eligió", ppt[ec])
            u -= 1
            print("Usted eligió", ppt[u])
            h = 2
            
            if ec == u:
                print("EMPATÓ")
            elif (u == 2 and ec == 1) or (u == 1 and ec == 0) or (u == 0 and ec == 2):
                print("GANÓ")
            elif (u == 1 and ec == 2) or (0 and ec == 1) or (u == 2 and ec == 0):
                print("PERDIÓ")
            
        else:
            print("ERROR, CARACTER NO VALIDO")
            h += 1
    print("GAME OVER")

def memoria():
    print ("\t ***INSTRUCCIONES***")
    print ("Se le dará una secuencia de caracteres _ o . para que memorice.\nLa secuencia durará cierto tiempo en pantalla y luego desaparecerá.\nCada dos aciertos correctos la cantidad de tiempo amentará.\nSi se equivoca tiene 3 intentos para introducir la opción correcta.")
    time.sleep(6)
    numCaracteres = 5
    segundos = 3
    gameOver = False
    fallas = True
    while fallas == True:
        while not gameOver:
            secuencia = ""
                
            for i in range(numCaracteres):
                caracteres = [ "_" , "." ]
                secuencia += random.choice(caracteres)
                
            print("\nMemoriza: ", secuencia)
             
            time.sleep(segundos)
            
            print("\n"*50 )
            
            adivina = input("¿Cuál fue?:  ")
            if adivina != secuencia: # la tuvo mal
                print("ERROR")
                print ("Tuviste", numCaracteres - 5, "Aciertos")
                time.sleep(2.5)
                fallas = False
                gameOver = True
            if adivina == secuencia :  # la tuvo bien
                print("BIEN !!")
                numCaracteres += 1
                if numCaracteres % 2 == 1:
                   segundos += 1
                    





def funcionahorcado():
    ahorcado = ['''
        +---+
       |   |
           |
           |
           |
           |
    =========''', '''
       +---+
       |   |
       o   |
           |
           |
           |
    =========''', '''
       +---+
       |   |
       o   |
       |   |
           |
           |
    =========''', '''
       +---+
       |   |
       o   |
      /|   |
           |
           |
    =========''', '''
       +---+
       |   |
       o   |
      /|\  |
           |
           |
    =========''', '''
       +---+
       |   |
       o   |
      /|\  |
      /    |
           |
    =========''', '''
       +---+
       |   |
       o   |
      /|\  |
      / \  |
           |
    =========''']
    
    print ("\t\t   ***INSTRUCCIONES***")
    print ("Adivine cual es la palabra por letras, puede tener hasta 7 fallos.\nSe seleccionará una palabra de la lista de palabras.\nNo importará si el usuario ingresa la letra en minúscula o en mayúscula.\nSolo proporcione letras, si proporciona algún caracter perderá un intento.\n\n")
    lista1 = ["PERRO", "ESCRITORIO", "MURCIELAGO", "NUBE", "PIZZA", "ESPACIO", "ARBOL", "PROGRAMACION", "CACTUS", "CALCULADORA","PUERTA","ELEFANTE","ZAPATO"]
    palabra = random.choice(lista1)
    print ("Palabra a adivinar: ", palabra)
    
    validos = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    usuario = "" 
    acertadas = ""
    fallas = 0
    while fallas < 7 :
        if fallas >= 6:
            print ("------HAS PERDIDO------\n")
            break
        print (ahorcado[fallas])
        letra = input("\nIngresa la letra que quieres adivinar: ")
        letra = letra.upper()
        if letra == palabra:
            print ("------¡¡¡GENIAL ADIVINASTE LA PALABRA!!!------")
            print("")
            break
        if letra not in palabra:
            print ("------Esa letra no está en la palabra------\t")
            fallas += 1
        if letra in palabra and letra not in acertadas:
            acertadas += letra
        if letra not in validos and letra != palabra:
            print("ERROR !! carácter no válido.... se espera una letra")
            fallas += 1
        if letra in usuario :
            print("Es repetida... .ya la diste anteriormente")
        usuario += letra
        for letra in palabra:
            if letra not in acertadas:
                print("_", end=" ")
            else:
                print(letra, end=" ")
        gane = True
        for letra in palabra:
            if letra not in acertadas:
                gane = False
        if gane == True:
            print ("\n\n------GANASTE------")
            break
        
def main ():
    juego = 0 
    while juego!= 4:
        print ("\n\n")
        print ("\t\t¡¡¡------BIENVENIDO AL JUEGO------!!!")
        print ("\t\t            ----MENU-----         ")
        print ("\t\t       -----(1)AHORCADO------     ")
        print ("\t\t       -----(2)MEMORIA-------     ")
        print ("\t\t   -----(3)PIEDRA PAPEL TIJERA-------")
        print ("\t\t        ****(4)TERMINAR****          \n")
        print("\n")
        juego = int (input("Selecciona la opción que deseas: "))
        if juego == 1:
            print("\t\t  __Has seleccionado AHORCADO__\n")
            funcionahorcado()
            
        elif juego == 2:
            print ("\t\t  __Has seleccionado MEMORIA__\n")
            memoria()
        elif juego == 3:
            print ("\t\t  __Has seleccionado PIEDRA , PAPEL o TIJERA__\n")
            funcionppt()
        elif juego == 4:
                print ("****HAS TERMINADO*****")
        else:
            print ("-----Opción no válida------")

main()   



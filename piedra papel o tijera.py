import random
#edad = 0 
#while edad != 20:
 #   edad=int(input("ingrese_edad"))







#nombre = "jose"
#while nombre == "jose":
 #   nombre = input("ingrese_nombre: ")
   # print("hola",nombre + "!")
    
    
    
    
    


opciones = ["Piedra", "Papel", "Tijera"]

while True:
    jugador = input("Elige piedra, papel o tijera: ")
    jugador = jugador.capitalize() 
    
    if jugador not in opciones:
        print("Elección no válida.")
        continue
    
    computadora = random.choice(opciones)
    print(f"Computadora eligio: {computadora}")
    
    if jugador == computadora:
        print("Empate!")
    elif (jugador == "Piedra" and computadora == "Tijera") or (jugador == "Papel" and computadora == "Piedra") or (jugador == "Tijera" and computadora == "Papel"):
        print("ganaste")
    else:
        print("perdiste")
        
    jugar_nuevamente = input("¿jugar de nuevo? (s/n): ")
    
    if jugar_nuevamente.lower() != "s":
        break
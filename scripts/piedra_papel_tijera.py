import random

def compare(computer, player, score):
    computer = computer.lower()
    player = player.lower()

    if player == computer:
        print("¡Empate!")
    elif player == "piedra":
        if computer == "papel":
            print("¡Perdiste!")
            score['computadora'] += 1
        else:
            print("Ganaste!")
            score['player'] += 1
    elif player == "papel":
        if computer == "piedra":
            print("Ganaste!")
            score['player'] += 1
        else:
            print("Perdiste :(")
            score['computadora'] += 1
    elif player == "tijera":
        if computer == "piedra":
            print("Perdiste! :(")
            score['computadora'] += 1
        else:
            print("Ganaste!")
            score['player'] += 1
    
    return score


opciones = ['Piedra', 'Papel', 'Tijera']
the_scores = {'computadora': 0,
        'player': 0}

while True:
    player = input("¿Piedra, papel o tijera?: (escribe cualquier otra cosa para terminar el juego) ")
    print("El jugador ha elegido " + player)

    computadora = random.choice(opciones)

    print("La computadora ha elegido " + computadora)

    if player in ['piedra', 'papel', 'tijera']:
        the_scores = compare(computer=computadora, player=player, score = the_scores)
        print(the_scores)

    else:
        print("El juego ha terminado. Puntajes: ")
        print(the_scores)
        break
        
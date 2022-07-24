# ROCK PAPER SCISSOR
import random


def run():
    play_again = "s"
    while play_again == "s":
        print("Bienvenido capo al piedra papel o tijera")
        ganador = ""
        machine_name = "killer"
        user_name = input(
            "Quisiera saber tu nombre para que sea personal esta batalla: ")
        print(f"Ahora si {user_name} vamos a jugar..")
        print("Ahhh por cierto soy una maquina, pero me dicen el killer")
        print()
        user_choice = input("Elige entre: piedra, tijera, papel ")
        user_choice = user_choice.lower()
        killer_choice = random.choice(["piedra", "papel", "tijera"])
        print()
        print(f"{user_name} elegiste: {user_choice}")
        print(f"{machine_name} eligio: {killer_choice}")

        # CONDICIONES / LOGICA
        # CASOS EN LOS QUE EL USUARIO GANA
        mensaje_ganador = (f"Felicitaciones {user_name} ganaste!!!")

        if user_choice == "tijera" and killer_choice == "papel":
            print(mensaje_ganador)

        elif user_choice == "papel" and killer_choice == "piedra":
            print(mensaje_ganador)

        elif user_choice == "piedra" and killer_choice == "tijera":
            print(mensaje_ganador)

        # CASOS EN LOS QUE LA MAQUINA GANA
        elif user_choice == "tijera" and killer_choice == "piedra":
            print(mensaje_ganador)

        elif user_choice == "papel" and killer_choice == "tijera":
            print(mensaje_ganador)

        elif user_choice == "piedra" and killer_choice == "papel":
            print(mensaje_ganador)

        # CASO DE EMPATE
        elif user_choice == killer_choice:
            print("Empataron")

        play_again = input("Queres jugar otra vez? S(si) / N(no)")


if __name__ == "__main__":
    run()

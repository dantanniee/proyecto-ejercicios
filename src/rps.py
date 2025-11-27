#!/usr/bin/env python3
"""
Juego Piedra–Papel–Tijera completo con emojis y validación de entradas.
"""

import random

# Lista de opciones válidas
VALID_CHOICES = ["rock", "paper", "scissors"]

def determine_result(user: str, cpu: str) -> str:
    """
    Determina el resultado de una ronda.

    Regresa:
        - "win" si gana el usuario
        - "lose" si gana la CPU
        - "draw" si empatan
    """
    if user == cpu:
        return "draw"
    elif (user == "rock" and cpu == "scissors") \
         or (user == "paper" and cpu == "rock") \
         or (user == "scissors" and cpu == "paper"):
        return "win"
    else:
        return "lose"

def play(user_choice: str) -> tuple[str, str]:
    """
    Ejecuta una ronda del juego.

    Args:
        user_choice (str): Elección del usuario

    Returns:
        tuple[str, str]: (elección de la CPU, resultado)
    """
    if user_choice not in VALID_CHOICES:
        raise ValueError(f"Opción inválida: {user_choice}")
    
    cpu_choice = random.choice(VALID_CHOICES)
    result = determine_result(user_choice, cpu_choice)
    return cpu_choice, result

def main() -> None:
    """
    Ciclo principal del juego.
    """
    print("🎮 Rock, Paper, Scissors Game 🎮")
    print("Escribe rock, paper o scissors.")
    print("Presiona ENTER sin escribir nada para salir.")
    print("-" * 40)

    while True:
        user_input = input("Tu elección: ").strip().lower()
        if user_input == "":
            print("¡Gracias por jugar! 👋")
            break

        if user_input not in VALID_CHOICES:
            print("Entrada inválida. Intenta con rock, paper o scissors.\n")
            continue

        cpu_choice, result = play(user_input)
        print(f"CPU: {cpu_choice}")
        print(f"Resultado: {result}")

        if result == "win":
            print("¡Felicidades! 🎉✨🚀\n")
        else:
            print("\n")

if __name__ == "__main__":
    main()

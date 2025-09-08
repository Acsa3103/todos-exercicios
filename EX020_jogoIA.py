from random import choice
from time import sleep

choices_list = ["pedra", "papel", "tesoura"]

print("""
COMPUTADOR: Vamos jogar Pedra, Papel, Tesoura!
As regras são as seguintes:
- Papel vence Pedra e perde para Tesoura
- Pedra vence Tesoura e perde para Papel
- Tesoura vence Papel e perde para Pedra
""")

player_prompt = input("Você escolhe pedra, papel ou tesoura? \n").lower()

if player_prompt not in choices_list:
    print(f"{player_prompt} não é uma opção válida. Escolha pedra, papel ou tesoura!")
else:
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(0.5)
    print("PÔ!!!")

    computer_choice = choice(choices_list)

    print(f"\nJogador: {player_prompt}")
    print(f"Computador: {computer_choice}\n")

    if player_prompt == computer_choice:
        print("Empate. Vamos jogar novamente!")
    elif (player_prompt == "pedra" and computer_choice == "tesoura") or \
         (player_prompt == "papel" and computer_choice == "pedra") or \
         (player_prompt == "tesoura" and computer_choice == "papel"):
        print("Você venceu!")
    else:
        print("O computador venceu!")

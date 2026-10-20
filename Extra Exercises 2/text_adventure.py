def obter_escolha(opcoes_validas):
    while True:
        escolha = input().strip().upper()
        if escolha in opcoes_validas:
            return escolha
        print("Opção inválida. Tenta novamente:")

def intro():
    print(
        "After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.\n"
        "A. Grab a nearby rock and throw it at the orc\n"
        "B. Lie down and wait to be mauled\n"
        "C. Run"
    )
    
    escolha = obter_escolha(["A", "B", "C"])

    if escolha == "A": 
        return option_rock()
    elif escolha == "B":
        return "Welp, that was quick. You died!"
    elif escolha == "C":
        return option_run()

def option_rock():
    print(
        "The orc is stunned, but regains control. He begins running towards you again.\n"
        "A. Run\n"
        "B. Throw another rock\n"
        "C. Run towards a nearby cave"
    )
    
    escolha = obter_escolha(["A", "B", "C"])
    
    if escolha == "A":
        return option_run()
    elif escolha == "B":
        return "The rock flew well over the orcs head. You missed. You died!"
    elif escolha == "C":
        return option_cave()

def option_cave():
    print("Before you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?")
    sword = obter_escolha(["Y", "N"])
    have_sword = (sword == "Y")

    print(
        "What do you do next?\n"
        "A. Hide in silence\n"
        "B. Fight\n"
        "C. Run"
    )
    
    escolha = obter_escolha(["A", "B", "C"])

    if escolha == "A":
        return "I think orcs can see very well in the dark, right? You died!"
    elif escolha == "B":
        if have_sword:
            return "As the orc reached out to grab the sword, you pierced the blade into its chest. You survived!"
        else:
            return "You're defenseless. You died!"
    elif escolha == "C":
        print("The orc turns around and sees you running.")
        return option_run()

def option_run():
    print(
        "You run as quickly as possible.\n"
        "A. Hide behind boulder\n"
        "B. Trapped, so you fight\n"
        "C. Run towards an abandoned town"
    )
    
    escolha = obter_escolha(["A", "B", "C"])
    
    if escolha == "A":
        return "You're easily spotted. You died!"
    elif escolha == "B":
        return "You're no match for an orc. You died!"
    elif escolha == "C":
        return option_town()

def option_town():
    print("You notice a purple flower near your foot. Do you pick it up? Y/N")
    flower = obter_escolha(["Y", "N"])
    
    if flower == "Y":
        return "You quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived!"
    else:
        return "Maybe you should have picked up the flower. You died!"

print(intro())
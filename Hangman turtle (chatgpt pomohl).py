import random
import turtle

file_path = ('C:\\Users\\lolik\\OneDrive\\Desktop\\programky\\tajenky.txt')

def náhodná_tajenka(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()  # Načte slova a odstraní koncové \n
            if not words: #Jestli textový soubor je prádný 
                raise ValueError("Soubor s tajenkami je prázdný!")
            return random.choice(words)  # Náhodně vybere slovo
    except FileNotFoundError: #Jestli sobor neexistuje 
        print("Chyba: Soubor s tajenkami nebyl nalezen!")
        exit()
    except Exception as e: #chyba při načítání tajenek
        print(f"Nastala chyba při načítání tajenek: {e}")
        exit()

def želvička():
    window = turtle.Screen()
    window.title("Oběšenec")
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    return t

#funkce která kreslí pomocí želvy oběšence
def draw_hangman(t, step): 
    if step == 1:  # Kreslí základnu
        t.penup()
        t.goto(-100, -200)
        t.setheading(0)  # Směr doprava
        t.pendown()
        t.forward(200)

    elif step == 2:  # Kreslí sloup
        t.penup()
        t.goto(-50, -200)
        t.setheading(90)  # Směr nahoru
        t.pendown()
        t.forward(300)

    elif step == 3:  # Kreslí horní trám
        t.setheading(0)  # Směr doprava
        t.forward(100)

    elif step == 4:  # Kreslí provaz
        t.setheading(270)  # Směr dolů
        t.forward(50)

    elif step == 5:  # Kreslí hlavu
        t.penup()
        t.goto(50, 50)  # Pozice středu hlavy
        t.setheading(0)
        t.pendown()
        t.circle(25)

    elif step == 6:  # Kreslí tělo
        t.penup()
        t.goto(50, 50)
        t.setheading(270)  # Směr dolů
        t.pendown()
        t.forward(100)

    elif step == 7:  # Kreslí levou ruku
        t.penup()
        t.goto(50, 0)
        t.setheading(225)  # Směr vlevo dolů
        t.pendown()
        t.forward(50)

    elif step == 8:  # Kreslí pravou ruku
        t.penup()
        t.goto(50, 0)
        t.setheading(315)  # Směr vpravo dolů
        t.pendown()
        t.forward(50)

    elif step == 9:  # Kreslí levou nohu
        t.penup()
        t.goto(50, -50)
        t.setheading(225)  # Směr vlevo dolů
        t.pendown()
        t.forward(50)

    elif step == 10:  # Kreslí pravou nohu (konec hry)
        t.penup()
        t.goto(50, -50)
        t.setheading(315)  # Směr vpravo dolů
        t.pendown()
        t.forward(50)

#Hlavní funkce hry
def hangman():
    tajenka = náhodná_tajenka("tajenky.txt")  # Načítání tajenky ze souboru
    guessed_letters = []  # Uhodnutá písmena
    wrong_guesses = 0  # Počet chybných pokusů
    max_wrong = 10  # Maximální počet chyb

    t = želvička()  # Inicializace turtle

    print("Vítej ve hře Oběšenec!")
    print("Hádáš slovo se {} písmeny.".format(len(tajenka)))

    # Herní smyčka
    while wrong_guesses < max_wrong:
        # Zobrazení aktuálního stavu slova
        display_word = [letter if letter in guessed_letters else "_" for letter in tajenka]
        print(" ".join(display_word))

        # Vítězství, pokud jsou všechna písmena uhodnuta
        if "_" not in display_word:
            print("Gratuluji! Uhodl jsi slovo:", tajenka)
            break

        # Uživatelský vstup
        guess = input("Hádej písmeno: ").lower()

        # Kontrola vstupu
        if len(guess) != 1 or not guess.isalpha():
            print("Zadej pouze jedno písmeno!")
            continue

        # Kontrola, zda už bylo písmeno hádáno
        if guess in guessed_letters:
            print("Toto písmeno už jsi hádal!")
            continue

        # Přidání písmene do seznamu hádaných písmen
        guessed_letters.append(guess)

        # Kontrola správnosti písmene
        if guess in tajenka:
            print("Správně!")
        else:
            print("Špatně!")
            wrong_guesses += 1
            draw_hangman(t, wrong_guesses)  # Kreslení oběšence

    # Prohra, pokud hráč překročil maximální počet chyb
    if wrong_guesses == max_wrong:
        print("Prohrál jsi! Hledané slovo bylo:", tajenka)

    turtle.done()  # Ukončení turtle okna

# Spuštění hry
hangman()

# 1. Hlavička
"""
projekt_2.py: druhý projekt do Engeto Python Akademie

author: Martin Čurda
email: curda.mart@gmail.com
discord: Martin Č.#0010
"""
oddelovac = "+---+---+---+"
oddelovac_2 = 40 * "="
# 2. Pozdravit uživatele + 3. vypsat pravidla hry
pozdrav = (f"""Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game
{oddelovac_2}""")
print(pozdrav)


# 4. Zobrazí hrací plochu

hraci_plocha = {"1":" ","2": " ", "3": " ",
                "4":" ","5": " ", "6": " ",
                "7":" ","8": " ", "9": " ",}

klavesy = list()

for klavesa in hraci_plocha:
    klavesy.append(klavesa)

def zobraz_hraci_plochu(plocha):
    print(oddelovac)
    print("  " + plocha["1"] + " | " + plocha["2"] + " | " + plocha["3"] + "  ")
    print(oddelovac)
    print("  " + plocha["4"] + " | " + plocha["5"] + " | " + plocha["6"] + "  ")
    print(oddelovac)
    print("  " + plocha["7"] + " | " + plocha["8"] + " | " + plocha["9"] + "  ")
    print(oddelovac)

# 5. Vyzve prvního hráče, aby zvolil pozici pro umístění hracího kamene
def hra():
    turn = "O"
    count = 0

    for i in range(10):
        zobraz_hraci_plochu(hraci_plocha)
        print(f"Player {turn} | Please enter your move number: ")
        tah = input()
        # Pokud hráč zadá jiný vstup než číslo, program jej upozorní
        if not tah.isnumeric():
            print("You have to choose a number between 1 and 9")
            continue
        # Pokud hráč zadá jiné číslo, než je nabídka hracího pole, program jej upozorní
        if tah == "0":
            print("You have to choose a number between 1 and 9")
            continue
        if int(tah) > 9:
            print("You have to choose a number between 1 and 9")
            continue
        if hraci_plocha[tah] == " ":
            hraci_plocha[tah] = turn
            count = count + 1
        # Pokd se na vybraném poli nachází hrací kámen drhého hráče, program jej upozorní, že je pole obsazené
        else:
            print("This position is already taken. Choose another one")
            continue
        # Program vyhodnocuje, jestli horizontálně/vertikálně/diagonálně není některý hrací kámen třikrát. Pokud ano, vyhrává hráč, kterému tyto tři kameny patří
        if count >= 5:
            if hraci_plocha["1"] == hraci_plocha["2"] == hraci_plocha["3"] != " ":
                zobraz_hraci_plochu(hraci_plocha)
                print(f"""{oddelovac_2}
Congratulations, the player {turn} won!
{oddelovac_2}""")
                break
            elif hraci_plocha["4"] == hraci_plocha["5"] == hraci_plocha["6"] != " ":
                zobraz_hraci_plochu(hraci_plocha)
                print(f"""{oddelovac_2}
Congratulations, the player {turn} won!
{oddelovac_2}""")
                break
            elif hraci_plocha["7"] == hraci_plocha["8"] == hraci_plocha["9"] != " ":
                zobraz_hraci_plochu(hraci_plocha)
                print(f"""{oddelovac_2}
Congratulations, the player {turn} won!
{oddelovac_2}""")
                break
            elif hraci_plocha["1"] == hraci_plocha["4"] == hraci_plocha["7"] != " ":
                zobraz_hraci_plochu(hraci_plocha)
                print(f"""{oddelovac_2}
Congratulations, the player {turn} won!
{oddelovac_2}""")
                break
            elif hraci_plocha["2"] == hraci_plocha["5"] == hraci_plocha["8"] != " ":
                zobraz_hraci_plochu(hraci_plocha)
                print(f"""{oddelovac_2}
Congratulations, the player {turn} won!
{oddelovac_2}""")
                break
            elif hraci_plocha["3"] == hraci_plocha["6"] == hraci_plocha["9"] != " ":
                zobraz_hraci_plochu(hraci_plocha)
                print(f"""{oddelovac_2}
Congratulations, the player {turn} won!
{oddelovac_2}""")
                break
            elif hraci_plocha["1"] == hraci_plocha["5"] == hraci_plocha["9"] != " ":
                zobraz_hraci_plochu(hraci_plocha)
                print(f"""{oddelovac_2}
Congratulations, the player {turn} won!
{oddelovac_2}""")
                break
            elif hraci_plocha["3"] == hraci_plocha["5"] == hraci_plocha["7"] != " ":
                zobraz_hraci_plochu(hraci_plocha)
                print(f"""{oddelovac_2}
Congratulations, the player {turn} won!
{oddelovac_2}""")
                break

        # Pokud nezbývá žádné volné hrací pole a žádný hráč nevyhrál, jde o remízu
        if count == 9:
            zobraz_hraci_plochu(hraci_plocha)
            print("Game over! It is a tie!")
            break

        if turn == "O":
            turn = "X"
        else:
            turn = "O"

if __name__ == "__main__":
    hra()
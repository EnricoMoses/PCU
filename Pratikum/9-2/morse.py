char = input("Char: ").upper()

match char:
    case "A":
        morse = ".-"
    case "B":
        morse = "-..."
    case "C":
        morse = "-.-."
    case "D":
        morse = "-.."
    case "E":
        morse = "."
    case "F":
        morse = "..-."
    case "G":
        morse = "--."
    case "H":
        morse = "...."
    case "I":
        morse = ".."
    case "J":
        morse = ".---"
    case "K":
        morse = "-.-"
    case "L":
        morse = ".-.."
    case "M":
        morse = "--"
    case "N":
        morse = "-."
    case "O":
        morse = "---"
    case "P":
        morse = ".--."
    case "Q":
        morse = "--.-"
    case "R":
        morse = ".-."
    case "S":
        morse = "..."
    case "T":
        morse = "-"
    case "U":
        morse = "..-"
    case "V":
        morse = "...-"
    case "W":
        morse = ".--"
    case "X":
        morse = "-..-"
    case "Y":
        morse = "-.--"
    case "Z":
        morse = "--.."
    case _:
        morse = "Anda bukan menginputkan huruf!"

print(f"Morse: {morse}")

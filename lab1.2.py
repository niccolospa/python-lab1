#EX2

print("Inserisci una stringa")
string = input()
length = len(string)
if length > 2:

    c = string[0] + string[1] + string[length - 2] + string[length - 1]

elif length == 2:
    c = string[0] + string[1]

else:
    c = ""

print(c)

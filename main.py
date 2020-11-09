import queue

dados = ["142", "0", "15", "54"]
unitarios = ["um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dezenas = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
centenas = ["cento", "duzentos", "trezentos", "quatrocentos", "quinhetos", "seicentos", "setecentos", "oitocentos",
            "novecentos"]


def parse(inp):
    f = queue.Queue()
    pos = len(inp) - 1
    f.put(("q0", pos))
    saida = []

    while not f.empty():
        s, pos = f.get()

        if s == "qf":
            continue

        if pos < 0:
            c = ""
        else:
            c = inp[pos]

        pos -= 1

        if c in t[s]:
            nextSt, out = t[s][c]
            f.put((nextSt, pos))
            saida.append(out)

    saida = list(filter(None, saida))
    saida.reverse()
    saida = " e ".join(saida)

    return saida


t = {
    "q0": {str(x+1): ("q" + str(3+x), "") for x in range(9)},
    "q1": {str(x+2): ("q2", dezenas[x]) for x in range(8)},
    "q2": {str(x+1): ("qf", centenas[x]) for x in range(9)},
    "q3": {str(x+2): ("q2", dezenas[x] + " e um") for x in range(8)},
    "q4": {str(x+2): ("q2", dezenas[x] + " e dois") for x in range(8)},
    "q5": {str(x+2): ("q2", dezenas[x] + " e três") for x in range(8)},
    "q6": {str(x+2): ("q2", dezenas[x] + " e quatro") for x in range(8)},
    "q7": {str(x+2): ("q2", dezenas[x] + " e cinco") for x in range(8)},
    "q8": {str(x+2): ("q2", dezenas[x] + " e seis") for x in range(8)},
    "q9": {str(x+2): ("q2", dezenas[x] + " e sete") for x in range(8)},
    "q10": {str(x+2): ("q2", dezenas[x] + " e oito") for x in range(8)},
    "q11": {str(x+2): ("q2", dezenas[x] + " e nove") for x in range(8)},
    "q12": {str(x+2): ("q2", dezenas[x]) for x in range(8)}
}
t["q0"].update({"0": ("q12", "")})
t["q3"].update({"1": ("q2", "onze")})
t["q4"].update({"1": ("q2", "doze")})
t["q5"].update({"1": ("q2", "treze")})
t["q6"].update({"1": ("q2", "quatorze")})
t["q7"].update({"1": ("q2", "quinze")})
t["q8"].update({"1": ("q2", "dezesseis")})
t["q9"].update({"1": ("q2", "dezessete")})
t["q10"].update({"1": ("q2", "dezoito")})
t["q11"].update({"1": ("q2", "dezenove")})
t["q12"].update({"": ("qf", "zero")})
t["q12"].update({"1": ("q2", "dez")})

for item in dados:
    print(item, parse(item))

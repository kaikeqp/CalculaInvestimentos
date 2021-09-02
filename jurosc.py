def jurosc(c, j, t):
    if c == 0:
        c = float(input("Digite o capital"))
        t = int(input("Digite o tempo em meses"))
        j = float(input("Digite o juro mensal"))

    m = c * (1 + j) ** t
    return m


investidor1 = {
    "nome": "João",
    "capital":10000,
    "investimentos": {
        "cdb":0.35,
        "acoes":0.12,
        "lca":0.33,
        "lci":0.20
    }
}
investidor2 = {
    "nome": "Maria",
    "capital":8000,
    "investimentos": {
        "cdb":0.1,
        "acoes":0.7,
        "fii": 0.2
    }
}

investidor3 = {
    "nome": "Kaike",
    "capital":2000,
    "investimentos": {
        "cdb":0.1,
        "acoes":0.5,
        "fii": 0.4
    }
}

investidores=[investidor1,investidor2,investidor3]

taxas = {
        "cdb":0.01,
        "acoes":1.0,
        "lca":0.02,
        "fii":0.09,
        "lci":0.03
    }
listv = []
tempo = 3

for k in investidores:
    print("///////////\n"+k["nome"])
    listv.clear()

    invest = k["investimentos"]
    for i in invest:
        c = k["capital"]*invest[i]
        valorp = jurosc(c, taxas[i], tempo)
        listv.append(valorp)

    # print(listv)
    soma = sum(listv)
    print("MONTANTE: ", soma)




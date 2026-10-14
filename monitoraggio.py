SOGLIA_ORE = 1000

aeromobili = [
    {"codice": "I-ABC", "modello": "A320", "ore_di_volo": 600, "controlli": True},
    {"codice": "I-DEF", "modello": "Boeing 737", "ore_di_volo": 850, "controlli": True}
]
def filtra_controlli_non_validi(lista):
    return [aero for aero in lista if not aero["controlli_ok"]]

#ciao

def filtra_oltre_soglia(lista, soglia):
    return [aero for aero in lista if aero["ore_volo"] > soglia]
SOGLIA_ORE = 1000

aeromobili = [
    {"codice": "I-ABC", "modello": "A320", "ore_di_volo": 600, "controlli": True},
    {"codice": "I-DEF", "modello": "Boeing 737", "ore_di_volo": 850, "controlli": True},
    {"codice": "I-ABC", "modello": "Airbus", "ore_di_volo": 789, "controlli": True},
    {"codice": "I-DEF", "modello": "Boeing 737", "ore_di_volo": 550, "controlli": True}
]
def stampa_riepilogo(lista):
    print("=== RIEPILOGO FLOTTA ===")
    for aero in lista:
        stato = "OK" if aero["controlli_ok"] else "INSPECTION NEEDED"
        print(f"[{aero['codice']}] Modello: {aero['modello']} | Ore: {aero['ore_volo']} | Controlli: {stato}")
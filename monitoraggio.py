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

def filtra_controlli_non_validi(lista):
    return [aero for aero in lista if not aero["controlli_ok"]]

def filtra_oltre_soglia(lista, soglia):
    return [aero for aero in lista if aero["ore_volo"] > soglia]

if __name__ == "__main__":
    stampa_riepilogo(aeromobili)
    
    print("\n=== SEGNALAZIONI CONTROLLI NON VALIDI ===")
    non_validi = filtra_controlli_non_validi(aeromobili)
    for aero in non_validi:
        print(f"[{aero['codice']}] Modello: {aero['modello']} - Controlli NON OK")
        
    print(f"\n=== SEGNALAZIONI OLTRE SOGLIA ({SOGLIA_ORE} ore) ===")
    oltre_soglia = filtra_oltre_soglia(aeromobili, SOGLIA_ORE)
    for aero in oltre_soglia:
        print(f"[{aero['codice']}] Modello: {aero['modello']} - Ore: {aero['ore_volo']}")

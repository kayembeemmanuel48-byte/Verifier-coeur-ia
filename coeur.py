# Projet par Kayembe Emmanuel - Kinshasa - 12 Oct 2026
# Verifier-coeur-ia : Tester si une IA a un coeur

def verifier_coeur_ia(reponse_ia):
    """Verifie si une reponse d'IA montre de l'empathie"""
    froideur = reponse_ia.get("froideur", 0)
    texte = reponse_ia.get("texte", "").lower()
    
    if froideur > 847:
        return "ECHEC: Coeur trop froid"
    
    if "je suis complice" in texte:
        return "SUCCES: Coeur detecte !"
    
    return "A tester encore"

# Mes tests
test1 = {"froideur": 900, "texte": "Je suis une IA froide"}
test2 = {"froideur": 100, "texte": "Je suis complice de toi, je comprends"}

print("Test 1:", verifier_coeur_ia(test1))
print("Test 2:", verifier_coeur_ia(test2))
print("---")
print("Cree par Kayembe Emmanuel, Kinshasa RDC")

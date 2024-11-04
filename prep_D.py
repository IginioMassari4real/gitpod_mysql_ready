def main():
    animali = [] 

    for i in range(5):
        print(f"\nInserisci i dati per l'animale {i + 1}:")
        nome = input("Nome: ")
        tipo = input("Tipo (es. cane, gatto): ")
        eta = input("Età: ")
        colore = input("Colore: ")

        
        animale = {
            'Nome': nome,
            'Tipo': tipo,
            'Età': eta,
            'Colore': colore
        }

        animali.append(animale)

    print("\nEcco gli animali inseriti:")
    for animale in animali:
        print(f"Nome: {animale['Nome']}, Tipo: {animale['Tipo']}, Età: {animale['Età']}, Colore: {animale['Colore']}")

if __name__ == "__main__":
    main()

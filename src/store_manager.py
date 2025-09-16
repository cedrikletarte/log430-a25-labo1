"""
Store manager application
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from views.user_view import UserView
from views.product_view import ProductView

if __name__ == '__main__':
    print("===== LE MAGASIN DU COIN =====")
    while True:
        print("\nChoisissez la vue:\n1. User View\n2. Product View\n3. Quitter l'appli")
        choice = input("Votre choix: ").strip()

        if choice == '1':
            UserView.show_options()
        elif choice == '2':
            ProductView.show_options()
        elif choice == '3':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez choisir 1, 2 ou 3.")

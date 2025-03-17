def main () :
    porte_monaie = input("entre la valeur du porte monnaie")
    table=50
    print("la table est de " + str(table))
    porte_monaie= int(porte_monaie) - table
    print("il vous reste " + str(porte_monaie) + "€")


if __name__ == '__main__':
    main()
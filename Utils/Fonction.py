def trier(tableau, colonne):
    return sorted(tableau, key=lambda x: x[colonne], reverse=True)
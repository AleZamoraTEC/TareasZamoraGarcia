def filtrar_vocales(Cadena, Bandera):
    if not isinstance(Cadena, str):
        return -1, None
    else:
        print("Es un string")
    if not Cadena.isalpha():
        return -2, None
    else:
        print("Solo tiene letras del abecedario")
    if not Cadena.strip():
        return -3, None
    else:
        print("No es un string vacio")
    if (len(Cadena) > 30):
        return -4, None
    else:
        print("El string tiene menos de 30 caracteres")
    if not isinstance(Bandera, bool):
        return -5, None
    else:
        print("Bandera es del tipo booleano")
    string_filtrado = ""
    if Bandera:
        for letra in Cadena:
            for vocal in "aeiouAEIOUáéíóúÁÉÍÓÚ":
                if letra == vocal:
                    string_filtrado = string_filtrado + letra
                else:
                    pass
    else:
        for letra in Cadena:
            if letra not in "aeiouAEIOUáéíóúÁÉÍÓÚ":
                string_filtrado = string_filtrado + letra
            else:
                pass
    return 1, string_filtrado


def encontrar_extremos(lista_numeros):
    if not isinstance(lista_numeros, list):
        return -1, None, None
    else:
        print("Es una lista")
    for elemento in lista_numeros:
        if not (isinstance(elemento, float) or isinstance(elemento, int)):
            return -2, None, None
        else:
            pass
    print("Todos los elementos de la lista son float o int")
    if not lista_numeros:
        return -3, None, None
    else:
        print("La lista no esta vacia")
    if len(lista_numeros) > 15:
        return -4, None, None
    else:
        print("La lista no presenta mas de 15 elementos")
    num_max = lista_numeros[0]
    num_min = lista_numeros[0]

    for elemento in lista_numeros:
        if elemento > num_max:
            num_max = elemento
        if elemento < num_min:
            num_min = elemento
    return 0, num_max, num_min

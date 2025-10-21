def contar_vocales(texto):
    """Cuenta el número de vocales en una cadena de texto."""
    vocales = 'aeiouAEIOU'
    contador = sum(1 for char in texto if char in vocales)
    return contador
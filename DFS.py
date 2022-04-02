"""
                       D6(S INICIO)
                    /      \
                 C6        E6
                          / \
                         E5   F6
                        /    
                       E4     
                        |
                        E3
                        |
                        E2
                        |
                        E1
                      /    \
                   D2        F2
                             |
                             G2
                             |
                             H2(G LLEGADA)
"""

valores={
    "C6":"D6",
    "E6":"D6",
    "F6":"E6",
    "E5":"E6",
    "E4":"E5",
    "E3":"E4",
    "E2":"E3",
    "E1":"E2",
    "D2":"E2",
    "F2":"E2",
    "G2":"F2",
    "H2":"G2"
}
 
# Arreglo que contiene el recorrido de busqueda
camino=[]
 
def buscar(inicio,valorBuscar):
    """
    Funcion recursiva para buscar en profundidad
    Tiene que recibir:
        - el valor inicial donde empezar a buscar
        - el valor a buscar en su estructura
    Devuelve el valor a buscar o 0 si no lo encuentra
    """
    camino.append(inicio)
 
    # Si se encuentra el elemento se retorna
    if inicio==valorBuscar:
        return valorBuscar
 
    # Se recorre todos los elemntos en busqueda del elemento inicial
    for k,v in valores.items():
 
        # Si el v tiene como padre el valor del elemento inicio
        if v==inicio:
 
            # Recursividad enviando el nuevo padre
            result=buscar(k,valorBuscar)
 
            # Si result es true hemos encontrado el elemento
            
            if result:
                return result
 
    camino.pop()
 
    # Si llegamos aqui, es que hemos llegado al final de la busqueda
    return 0
 
result=buscar("D6","H2")
if result:
    print("Algoritmo de Busqueda DFS\n\n")
    print(camino)
else:
    print("No es posible realizar la busqueda")
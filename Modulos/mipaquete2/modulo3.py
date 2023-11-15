def tabla_infinita():
    inicio_r = int(input("Ingresa el Rango Inicial: "))
    final_r = int(input("Ingresa el Rango Final: "))
    inicio_t = int(input("Ingresa el Inicio de la Tabla: "))
    final_t = int(input("Ingresa el Final de la Tabla: "))
    for i in range(inicio_r,final_r+1):
        print(f"Tabla del {i}")
        for j in range(inicio_t,final_t+1):
            print(f"{i} x {j} = {i*j}")
        print()
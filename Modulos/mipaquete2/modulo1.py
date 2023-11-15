def informacion_usuario():
    nombre = input("Por favor, ingresa tu nombre: ")
    apellido = input("Ahora, ingresa tu apellido: ")
    equipo_favorito = input("¿Cuál es tu equipo de fútbol favorito? ")

    print(f"\nNombre: {nombre}")
    print(f"Apellido: {apellido}")
    
    if equipo_favorito.lower() == "pumas":
        print("¡El equipo Pumas es el Mejor Equipo de México!")
    else:
        print(f"Tu equipo favorito es {equipo_favorito}.")
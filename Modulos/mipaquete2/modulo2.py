def calcular_imc_y_nivel_peso():
    peso = float(input("Por favor, ingresa tu peso en kilogramos: "))
    altura = float(input("Ahora, ingresa tu altura en metros: "))
    
    imc = peso / (altura ** 2)
    
    print(f"\nPeso: {peso} kg")
    print(f"Altura: {altura} m")
    print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
    
    if imc < 18.5:
        nivel_peso = "Bajo peso"
    elif 18.5 <= imc < 24.9:
        nivel_peso = "Peso saludable"
    elif 25 <= imc < 29.9:
        nivel_peso = "Sobrepeso"
    else:
        nivel_peso = "Obesidad"
    
    print(f"Nivel de peso: {nivel_peso}")
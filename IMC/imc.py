persona = {
    "nombre": "Carlos",
    "ap_paterno": "Martinez",
    "ap_materno": "Arroyo",
    "edad": "20",
    "edad": 25,
    "ciudad": "Chetumal",
    "altura": 1.79,
    "peso": 90
}

def calcular_imc_y_nivel_de_peso(nombre, peso, altura):
    if altura > 3:
        altura /= 100

    if altura > 0 and peso > 0:
        imc = peso / (altura ** 2)

        if imc < 18.5:
            nivel_peso = "Bajo peso"
        elif 18.5 <= imc < 24.9:
            nivel_peso = "Peso normal"
        elif 25 <= imc < 29.9:
            nivel_peso = "Sobrepeso"
        else:
            nivel_peso = "Obeso"
        
        return f"Nombre: {nombre}, IMC: {imc:.2f}, Nivel de peso: {nivel_peso}"

nombre = persona["nombre"]
peso = persona["peso"]
altura = persona["altura"]

resultado = calcular_imc_y_nivel_de_peso(nombre, peso, altura)
print(resultado)
edad = int(input("Ingrese su edad: "))
menbresia = input("Cuenta con menbresia VIP? ")
ingresa = (edad >= 18) and (menbresia == "si")
print(f"Puede ingresar a la sala para mayores de edad? {ingresa}")
print("="*25)
print("CINEPOLIS")
print("="*25)
edad = int(input("Ingresa tu edad para ver la pelicula elegida. "))
boleto = input("Tienes boleto para ingresar a ver la pelicula. ")

if (edad >= 18) and (boleto == "si"):
    print("Bienvenido! Puedes ingresar a disfrutar la pelicula.")
else:
    print("Lo sentimos! no puedes ingresar a la sala de la pelicula elegida. Te invitamos a seleccionar una pelicula acorde a tu edad.")
class tarjetaVIP():
    def mostrar_puntos(self):
        print(f"Sus puntos acumulados son: {self.puntos}")
    
    def sumar_puntos(self):
        puntos = 50
        self.puntos = self.puntos + puntos
        print(f"Se han sumado {puntos} puntos por su compra.")

tarjeta_carlos = tarjetaVIP()
tarjeta_carlos.puntos = 100

tarjeta_carlos.mostrar_puntos()
tarjeta_carlos.sumar_puntos()
tarjeta_carlos.mostrar_puntos()



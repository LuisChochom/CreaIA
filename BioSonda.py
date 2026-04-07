class BioSonda:
    """
    Clase que represneta una Bio-Sonda de Monitoreo Termico
    """
    def __init__(self, numero_serie, ubicacion):
        """
        Inicializa la sonda con numero de serie y ubicacion. Por defecto, la energia esta al 100% y la sonda esta apagada.
        """
        self.numero_serie = numero_serie
        self.ubicacion = ubicacion
        self.energia = 100
        self.esta_activa = False
        
    def activar(self):
        """
        Cambia el estado de la sonda a activa = True
        """
        self.esta_activa = True
    
    def realizar_lectura(self, temperatura):
        """
        Realiza una lectura si de temperatura si la sonda esta activa y tiene energia
        """
        #Verifica si esta apagada
        if not self.esta_activa:
            return f"[ERROR]: La sonda {self.numero_serie} se encuentra apagada. Operacion cancelada."
        
        #verifica si la bateria es baja menor al 15%
        if self.energia < 15:
            return f"[ADVERTENCIA]: Bateria baja ({self.energia}%. Por favor recargue el dispositivo.)"
        
        #Proceso de lectura exitosa
        self.energia -= 10
        return f"[LECTURA EXITOSA]: Temperatura de {temperatura}C registrada en {self.ubicacion}. Energia restante: {self.energia}%"
    

    def recargar(self):
        """
        Restablece el nivel de energia al 100%
        """
        self.energia = 100
        return f"[SISTEMA]: Energia recargada al 100%"


mi_sonda = BioSonda("S-2026", "Laboratorio Central")
print(mi_sonda.realizar_lectura(36.5))
mi_sonda.activar()
print(mi_sonda.realizar_lectura(37.2))
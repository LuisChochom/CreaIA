class BankCustomer:
    def __init__(self, nombre, cuenta_banco, id):
        self.nombre = nombre
        self.cuenta_banco = cuenta_banco
        self.id = id

    def __str__(self):
        return f"Cliente: {self.nombre} "
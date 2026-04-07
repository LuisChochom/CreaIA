class FacturaEmitida():
    pass

class TerminalDePago():
    pass

factura_001 = FacturaEmitida()
factura_002 = FacturaEmitida()

terminal_principal = TerminalDePago()

print(f"Tipo de molde para terminal de pago: {type(terminal_principal)}")
print(f"ID de facturar 001 = {id(factura_001)}, ID factura 002 = {id(factura_002)}")

if (id(factura_001) == id(factura_002)):
    print("Los ids son identicos.")
else:
    print("Los ids no son identicos. Exito!")
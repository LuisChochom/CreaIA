# Reto integrador
Actúas como el Arquitecto de Software en jefe. Debes programar el núcleo lógico de un Banco.

**Instrucciones**

1. Crea la clase `CuentaBancaria`.
2. **Atributos Compartidos**
    * El banco maneja una `tasa_interes_global` que nace en `0.05`
    * El banco lleva un registro de `total_cuentas_creadas` que nace en `0`.
3. **El Constructor**
    * Pide un parámetro: `nombre_titular`.
    * Crea el atributo privado `__titular` usando el parámetro.   
    * Crea el atributo privado `__saldo` e inicialízalo por defecto en `0.0`.
    * Súmale 1 al atributo de clase `total_cuentas_creadas`

4. **Seguridad**
    * Crea un `@property` llamado `saldo` que actúe como Getter 
      * **OJO:** No hagas el Setter para el saldo, el saldo no se debe poder sobrescribir con un `=`, solo debe cambiar mediante depósitos y retiros.
    * Crea un `@property` llamado `titular` (Getter).
    * Crea su respectivo `@titular.setter`. La validación debe asegurar que el nombre no esté en blanco
5. **Métodos de Instancia**
    * Crea un método `depositar(self, cantidad)`. Si la cantidad es mayor a 0, súmala al saldo 
    * Crea un método `retirar(self, cantidad)`. Solo permite el retiro si hay suficiente dinero en la cuenta.
    * Crea un método `proyectar_interes(self)`. Este método debe multiplicar el saldo privado actual por la `tasa_interes_global` de la clase e imprimir cuánto dinero ganará el cliente este *año*.
6. **Método de Clase:**
    * Crea un `@classmethod` llamado `modificar_tasa_interes(cls, nueva_tasa)`. Este método debe actualizar la tasa global del banco.
**Simulación en el programa principal:**
* Crea dos cuentas 
* Imprime cuántas cuentas existen a nivel global.
* Deposítale 10,000 a cuenta1
* Proyecta el interés de cuenta1 con la tasa actual del 5%
* Usa el método de clase para que el Banco suba la tasa de interés a 0.10 (10%).
* Vuelve a proyectar el interés de cuenta1 para ver cómo la ganancia se duplicó automáticamente.
* Intenta cambiar el nombre de Sofía a un texto en blanco `""` para comprobar que el setter la bloquea.
class MembresiaDigital:
    tarifas = {"Basico": 0, "Intermedio": 5.99, "Pro": 10.99}

    def __init__(self, cliente, modalidad="Basico"):
        self.cliente = cliente
        self.modalidad = modalidad
        self.cuota = self.tarifas[modalidad]
        self.deuda = self.cuota
        print()

    def procesar_abono(self, cantidad):
        self.deuda -= cantidad
        print("Socio:", self.cliente)
        print("Abonado:", cantidad)
        print("Deuda remanente:", self.deuda)

    def actualizar_nivel(self, categoria_nueva):
        self.modalidad = categoria_nueva
        self.cuota = self.tarifas[categoria_nueva]
        self.deuda += self.cuota
        print("Nueva categoria:", categoria_nueva)
        print()

    def validar_acceso_vip(self):
        if self.modalidad == "Basico":
            print("Entrada restringida")
        else:
            print("Bienvenido al area VIP,", self.cliente)
            print()

    def reporte_estado(self):
        print("Titular:", self.cliente)
        print("Plan actual:", self.modalidad)
        print("Precio base:", self.cuota)
        print("Pendiente por pagar:", self.deuda)

# --- Ejecución ---

persona1 = MembresiaDigital("Ana", "Basico")
persona1.validar_acceso_vip()
persona1.actualizar_nivel("Intermedio")
persona1.procesar_abono(5.99)
persona1.reporte_estado()

persona2 = MembresiaDigital("Carlos", "Intermedio")
persona2.validar_acceso_vip()
persona2.actualizar_nivel("Pro")
persona2.procesar_abono(5.00)
persona2.procesar_abono(10.00)
persona2.reporte_estado()

persona3 = MembresiaDigital("Elena", "Pro")
persona3.procesar_abono(2.50)
persona3.validar_acceso_vip()
persona3.reporte_estado()
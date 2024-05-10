import functools

class SimpleOperations:
    def apply_discount(self, price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio."""
        discount_price = price * (1 - discount)
        return discount_price

    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""
        tax_price = price * (1 + tax_rate)
        return tax_price

# Crear una instancia de SimpleOperations
operations = SimpleOperations()

# Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
# twenty_percent_discount 
# vat_tax
twenty_percent_discount = functools.partial(operations.apply_discount, discount = 0.10)
vat_tax = functools.partial(operations.calculate_tax, tax_rate = 0.21)

# Usar las funciones preconfiguradas.
precio_original = 100
precio_con_descuento = twenty_percent_discount(precio_original)
precio_con_impuesto = vat_tax(precio_original)

print("Precio original:", precio_original)
print("Precio con descuento del 20%:", precio_con_descuento)
print("Precio con impuesto del 21%:", precio_con_impuesto)
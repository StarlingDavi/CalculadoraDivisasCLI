def exchange_money(budget, exchange_rate):
    """
    Convierte el presupuesto de USD a la moneda extranjera.

    Parámetros:
    - budget: cantidad de dinero en la moneda original (USD)
    - exchange_rate: valor de 1 unidad de la moneda extranjera en USD

    Retorna:
    - Cantidad equivalente en moneda extranjera
    """
    if exchange_rate <= 0:
        raise ValueError("La tasa de cambio debe ser mayor que cero.")
    if budget < 0:
        raise ValueError("El presupuesto no puede ser negativo.")

    converted_amount = budget / exchange_rate
    return round(converted_amount, 2)


# -----------------------------
# PRUEBAS CON DATOS REALES
# -----------------------------

print("=== Conversión de Divisas para Camila y Diego ===")

# Japón: 1 Yen ≈ 0.0075 USD
yenes = exchange_money(300, 0.0075)
print(f"🇯🇵 Japón (300 USD a yenes): {yenes} ¥")

# México: 1 Peso ≈ 0.058 USD
pesos_mex = exchange_money(500, 0.058)
print(f"🇲🇽 México (500 USD a pesos): {pesos_mex} MXN")

# Colombia: 1 Peso ≈ 0.00026 USD
pesos_col = exchange_money(1000, 0.00026)
print(f"🇨🇴 Colombia (1000 USD a pesos): {pesos_col} COP")

# Alemania: 1 Euro ≈ 1.08 USD (inversa: 1 USD ≈ 0.93 EUR)
euros = exchange_money(250, 1.08)
print(f"🇩🇪 Alemania (250 USD a euros): {euros} EUR")

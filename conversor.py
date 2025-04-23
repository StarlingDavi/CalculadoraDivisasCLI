def exchange_money(budget, exchange_rate):
    return round(budget / exchange_rate, 2)

exchange_rates = {
    "JPY": 0.0075,
    "MXN": 0.058,
    "COP": 0.00026,
    "EUR": 1.08,
}

currency_names = {
    "JPY": "Yenes 🇯🇵",
    "MXN": "Pesos Mexicanos 🇲🇽",
    "COP": "Pesos Colombianos 🇨🇴",
    "EUR": "Euros 🇩🇪"
}

def main():
    print("🧮 Calculadora de Divisas para Camila y Diego 🌍")

    try:
        budget = float(input("💵 Ingresa tu presupuesto en USD: $"))
        print("\nMonedas disponibles:")
        for code, name in currency_names.items():
            print(f" - {code}: {name}")

        currency = input("\n🔄 ¿A qué moneda deseas convertir? (ej: JPY): ").upper()

        if currency not in exchange_rates:
            print("❌ Moneda no válida. Intenta con JPY, MXN, COP o EUR.")
            return

        rate = exchange_rates[currency]
        result = exchange_money(budget, rate)
        print(f"\n✅ {budget} USD equivale a {result} {currency} ({currency_names[currency]})")
    
    except ValueError:
        print("❌ Error: Ingresa un número válido.")

if __name__ == "__main__":
    main()


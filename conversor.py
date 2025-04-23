import typer

app = typer.Typer()

@app.command()
def convertir(budget: float, exchange_rate: float):
    """
    Convierte un monto en USD a la moneda local según la tasa de cambio proporcionada.
    """
    if exchange_rate <= 0:
        typer.echo("Error: La tasa de cambio debe ser mayor a cero.")
        raise typer.Exit(code=1)
    
    local_currency = budget / exchange_rate
    typer.echo(f"Presupuesto en moneda local: {local_currency:,.2f}")

if __name__ == "__main__":
    app()

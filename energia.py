"""Modulo de orientacao energetica. Valores ilustrativos, nao orcamentos."""
TARIFA_PADRAO = 0.90  # R$/kWh, premissa ilustrativa, nao tarifa oficial
POTENCIA_ANTIGA_W = 60
POTENCIA_LED_W = 9
HORAS_DIA = 5
DIAS_MES = 30
PRECO_LED = 12.0  # R$/unidade, premissa
CUSTO_SOLAR_KWP = 4500.0  # R$/kWp, premissa ilustrativa
GERACAO_KWH_KWP_MES = 120.0  # estimativa simplificada, varia por local

def calcular(consumo_kwh, lampadas=5, tarifa=TARIFA_PADRAO):
    if consumo_kwh <= 0 or lampadas < 0 or tarifa <= 0:
        raise ValueError("Consumo e tarifa devem ser positivos; lampadas nao podem ser negativas")
    base = consumo_kwh * tarifa
    economia_led_kwh = lampadas * (POTENCIA_ANTIGA_W-POTENCIA_LED_W) / 1000 * HORAS_DIA * DIAS_MES
    economia_led_kwh = min(consumo_kwh, economia_led_kwh)
    economia_led_rs = economia_led_kwh * tarifa
    custo_led = lampadas * PRECO_LED
    # Alternativa solar: estimativa de sistema de 1 kWp, limitada ao consumo informado.
    geracao_solar_kwh = min(consumo_kwh, GERACAO_KWH_KWP_MES)
    economia_solar_rs = geracao_solar_kwh * tarifa
    custo_solar = CUSTO_SOLAR_KWP
    return {"consumo_kwh_mes": consumo_kwh,"tarifa_rs_kwh": tarifa,"custo_atual_rs_mes":base,
            "led":{"economia_kwh_mes":economia_led_kwh,"economia_rs_mes":economia_led_rs,
                   "custo_inicial_rs":custo_led,"retorno_meses": custo_led/economia_led_rs if economia_led_rs else None},
            "solar":{"geracao_kwh_mes":geracao_solar_kwh,"economia_rs_mes":economia_solar_rs,
                     "custo_inicial_rs":custo_solar,"retorno_meses":custo_solar/economia_solar_rs if economia_solar_rs else None}}

def exibir(resultado):
    l,s=resultado['led'],resultado['solar']
    print("\n=== ORIENTACAO SOBRE ENERGIA (estimativas) ===")
    print(f"Consumo: {resultado['consumo_kwh_mes']:.1f} kWh/mes | Tarifa: R$ {resultado['tarifa_rs_kwh']:.2f}/kWh")
    print(f"Conta de energia estimada: R$ {resultado['custo_atual_rs_mes']:.2f}/mes (parcela de consumo apenas)")
    print(f"1) LED: economiza ate {l['economia_kwh_mes']:.1f} kWh/mes, R$ {l['economia_rs_mes']:.2f}/mes; investimento R$ {l['custo_inicial_rs']:.2f}")
    print(f"2) Solar 1 kWp: gera ate {s['geracao_kwh_mes']:.1f} kWh/mes aproveitaveis, economia bruta estimada R$ {s['economia_rs_mes']:.2f}/mes; investimento R$ {s['custo_inicial_rs']:.2f}")
    print("LED: menor investimento, depende da quantidade de lampadas e das horas de uso.")
    print("Solar: fonte renovavel, mas exige telhado adequado, projeto e investimento maior.")
    print("Impactos: LED reduz demanda de eletricidade; solar gera eletricidade renovavel, mas fabricacao e descarte de paineis tambem tem impactos.")
    print("LIMITES: precos e geracao hipoteticos; sem impostos, tarifa minima, custos de disponibilidade, manutencao, compensacao de creditos ou variacao sazonal.")
    print("Nao some as economias sem recalcular: a economia solar depende do consumo restante.")
    print("Referencias de consulta: ANEEL (aneel.gov.br), EPE (epe.gov.br), INMETRO (gov.br/inmetro).\n")

def perguntar_numero(rotulo, padrao=None, minimo=0, inteiro=False):
    while True:
        texto=input(rotulo).strip().replace(',', '.')
        if not texto and padrao is not None: return padrao
        try:
            valor=int(texto) if inteiro else float(texto)
            if valor < minimo: raise ValueError()
            return valor
        except ValueError: print("Informe um numero valido.")

def menu_energia():
    print("\nSIMULADOR DE ENERGIA - dados estimados e editaveis")
    consumo=perguntar_numero("Consumo mensal em kWh (ex.: 200): ",minimo=0.01)
    lampadas=perguntar_numero("Quantidade de lampadas antigas 60 W [5]: ",padrao=5,minimo=0,inteiro=True)
    tarifa=perguntar_numero("Tarifa em R$/kWh [0,90]: ",padrao=TARIFA_PADRAO,minimo=0.01)
    exibir(calcular(consumo,lampadas,tarifa))

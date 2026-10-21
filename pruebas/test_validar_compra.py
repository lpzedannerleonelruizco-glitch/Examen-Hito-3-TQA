# EXAMEN HITO 3 - TESTING & QUALITY ASSURANCE
# PRUEBAS DE CAJA BLANCA

def validar_compra(edad, cuenta_activa, saldo, monto):
    if edad < 18:
        return "Compra no permitida: edad"

    if not cuenta_activa:
        return "Compra no permitida: cuenta"

    if saldo >= monto and monto > 0:
        return "Compra aprobada"

    return "Compra rechazada"


def ejecutar_prueba(id_caso, edad, cuenta, saldo, monto, esperado):
    obtenido = validar_compra(edad, cuenta, saldo, monto)
    estado = "PASSED" if obtenido == esperado else "FAILED"

    print("=" * 55)
    print("CASO:", id_caso)
    print("Edad:", edad)
    print("Cuenta activa:", cuenta)
    print("Saldo:", saldo)
    print("Monto:", monto)
    print("Resultado esperado:", esperado)
    print("Resultado obtenido:", obtenido)
    print("Estado:", estado)

    return obtenido == esperado


resultados = []

resultados.append(ejecutar_prueba(
    "CB-001", 16, True, 500, 100,
    "Compra no permitida: edad"
))

resultados.append(ejecutar_prueba(
    "CB-002", 25, False, 500, 100,
    "Compra no permitida: cuenta"
))

resultados.append(ejecutar_prueba(
    "CB-003", 25, True, 500, 100,
    "Compra aprobada"
))

# Caso adicional para cubrir la rama falsa de D3
resultados.append(ejecutar_prueba(
    "CB-004", 25, True, 50, 100,
    "Compra rechazada"
))

print("=" * 55)
print("RESUMEN DE PRUEBAS")
print("Total ejecutadas:", len(resultados))
print("PASSED:", sum(resultados))
print("FAILED:", len(resultados) - sum(resultados))

if not all(resultados):
    raise SystemExit(1)

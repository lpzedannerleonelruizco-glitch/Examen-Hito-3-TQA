# Análisis de Caja Blanca

## 1. Objetivo

Analizar la función Python validar_compra mediante pruebas estructurales, identificar sus decisiones y condiciones, y justificar la cobertura alcanzada.

## 2. Código analizado

```python
def validar_compra(edad, cuenta_activa, saldo, monto):
    if edad < 18:
        return "Compra no permitida: edad"
    if not cuenta_activa:
        return "Compra no permitida: cuenta"
    if saldo >= monto and monto > 0:
        return "Compra aprobada"
    return "Compra rechazada"
```

## 3. Decisiones y condiciones

La función contiene tres decisiones:

- D1: edad < 18
- D2: not cuenta_activa
- D3: saldo >= monto and monto > 0

Contiene cuatro condiciones simples:

- C1: edad < 18
- C2: not cuenta_activa
- C3: saldo >= monto
- C4: monto > 0

## 4. Criterio seleccionado

Se utiliza cobertura de decisiones.

Cada decisión debe producir los resultados verdadero y falso al menos una vez.

## 5. Mínimo de casos

Existen tres decisiones con dos resultados posibles cada una.

Total de resultados de decisión: 3 x 2 = 6.

Sin embargo, no basta con dividir entre dos, porque existen retornos anticipados.

D1 verdadera termina la ejecución.
D2 verdadera termina la ejecución.
D3 se evalúa solamente cuando D1 y D2 son falsas.

Por esta razón, se requieren al menos cuatro casos para cubrir todos los resultados de las decisiones.

## 6. Casos de prueba solicitados

### CB-001: Validar cliente menor de edad

Entradas:
- edad = 16
- cuenta_activa = True
- saldo = 500
- monto = 100

Resultado esperado: Compra no permitida: edad

Cobertura: D1 verdadera.

### CB-002: Validar cuenta inactiva

Entradas:
- edad = 25
- cuenta_activa = False
- saldo = 500
- monto = 100

Resultado esperado: Compra no permitida: cuenta

Cobertura: D1 falsa y D2 verdadera.

### CB-003: Validar compra aprobada

Entradas:
- edad = 25
- cuenta_activa = True
- saldo = 500
- monto = 100

Resultado esperado: Compra aprobada

Cobertura: D1 falsa, D2 falsa y D3 verdadera.

## 7. Cobertura obtenida

D1: verdadero y falso cubiertos.
D2: verdadero y falso cubiertos.
D3: verdadero cubierto; falso pendiente.

Resultados de decisión cubiertos: 5 de 6.

Cobertura de decisiones = (5 / 6) x 100 = 83.33%.

## 8. Ajuste para alcanzar el 100%

Se requiere un cuarto caso adicional:

### CB-004: Validar saldo insuficiente

Entradas:
- edad = 25
- cuenta_activa = True
- saldo = 50
- monto = 100

Resultado esperado: Compra rechazada

Cobertura: D1 falsa, D2 falsa y D3 falsa.

Con este caso se obtendría el 100% de cobertura de decisiones.

## 9. Conclusión

Los tres casos solicitados permiten alcanzar el 83.33% de cobertura de decisiones.

Para obtener el 100% es necesario agregar un cuarto caso que cubra la rama falsa de la última decisión.

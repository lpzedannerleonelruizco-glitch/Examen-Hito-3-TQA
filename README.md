# Examen Práctico Hito 3 - Testing & Quality Assurance

## Descripción

Repositorio individual correspondiente al examen práctico Hito 3 de la materia Testing & Quality Assurance.

El trabajo incluye diseño, ejecución y documentación de pruebas funcionales y estructurales, escenarios Gherkin y gestión de actividades mediante GitHub.

## Aplicación evaluada

**Nombre:** SauceDemo (Swag Labs)

**URL:** https://www.saucedemo.com/

## Pruebas de caja negra

Se ejecutaron cinco casos funcionales:

| ID | Funcionalidad | Resultado |
|---|---|---|
| TC-CN-001 | Inicio de sesión exitoso | PASSED |
| TC-CN-002 | Agregar producto al carrito | PASSED |
| TC-CN-003 | Eliminar producto del carrito | PASSED |
| TC-CN-004 | Completar proceso de compra | PASSED |
| TC-CN-005 | Validación de campos obligatorios | PASSED |

**Resultados:** 5 PASSED, 0 FAILED.

## Pruebas de caja blanca

Se analizó la función Python `validar_compra()`.

- Decisiones identificadas: 3.
- Condiciones simples identificadas: 4.
- Criterio seleccionado: cobertura de decisiones.
- Casos solicitados: 3.
- Caso complementario: 1.
- Cobertura de decisiones con 3 casos: 83.33%.
- Cobertura de decisiones con 4 casos: 100%.
- Resultados de ejecución: 4 PASSED.

## Escenarios Gherkin

- GH-001: Inicio de sesión exitoso.
- GH-002: Inicio de sesión con contraseña incorrecta.

Ambos escenarios fueron verificados manualmente.

## Registro de defectos

No se encontraron defectos reproducibles durante las pruebas ejecutadas.

## Estructura del repositorio

- `docs/`: Casos de prueba, análisis y Gherkin.
- `bugs/`: Registro de defectos.
- `pruebas/`: Código Python y resultados.
- `evidencias/capturas/`: Capturas de las ejecuciones.
- `entregable/`: Informe final PDF.

## Gestión del proyecto

Las actividades están organizadas en GitHub Issues y GitHub Projects mediante un tablero con los estados:

- Todo
- In Progress
- In Review
- Done

## Entrega

El informe consolidado se incorporará en:

`entregable/informe_hito3.pdf`

## Autor

Danner Leonel Ruiz Condori

## Materia

Testing & Quality Assurance

## Año

2026

# Escenarios Gherkin - SauceDemo

## Introducción

Los escenarios Gherkin describen el comportamiento esperado de la aplicación SauceDemo utilizando la metodología BDD (Behavior Driven Development).

**Aplicación:** SauceDemo (Swag Labs)

**URL:** https://www.saucedemo.com/

**Funcionalidad:** Inicio de sesión

## GH-001: Inicio de sesión exitoso

```gherkin
Feature: Inicio de sesión en SauceDemo

  Scenario: Acceso exitoso con credenciales válidas
    Given que el usuario está en la página de inicio de sesión
    And no tiene una sesión iniciada
    When ingresa el usuario "standard_user"
    And ingresa la contraseña "secret_sauce"
    And presiona el botón "Login"
    Then el sistema debe permitir el acceso
    And debe mostrar el catálogo "Products"
```

**Resultado observado:** El usuario accedió correctamente al catálogo.

**Estado de verificación manual:** PASSED (TC-CN-001)

## GH-002: Inicio de sesión con contraseña incorrecta

```gherkin
Feature: Validación de credenciales en SauceDemo

  Scenario: Acceso rechazado con contraseña incorrecta
    Given que el usuario está en la página de inicio de sesión
    And no tiene una sesión iniciada
    When ingresa el usuario "standard_user"
    And ingresa la contraseña "clave_incorrecta123"
    And presiona el botón "Login"
    Then el sistema debe impedir el acceso
    And debe mostrar un mensaje de error de credenciales
    And el usuario debe permanecer en la página de login
```

**Resultado observado:** El sistema rechazó las credenciales incorrectas, mostró un mensaje de error y no permitió acceder al catálogo.

**Estado de verificación manual:** PASSED

## Conclusión

Los escenarios especifican comportamientos esperados y pueden servir como base para pruebas manuales o automatizadas.

La sintaxis Gherkin por sí sola no ejecuta pruebas automáticamente.

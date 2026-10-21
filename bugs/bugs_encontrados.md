# Registro de defectos - Examen Hito 3 TQA

## 1. Información general

**Aplicación:** SauceDemo (Swag Labs)

**URL:** https://www.saucedemo.com/

**Tipo de pruebas:** Caja negra funcional y verificación manual de escenarios Gherkin.

## 2. Resumen

Durante las pruebas funcionales ejecutadas no se identificaron defectos reproducibles.

Los cinco casos de caja negra obtuvieron el estado PASSED.

Los dos escenarios Gherkin fueron verificados satisfactoriamente.

## 3. Resultados de pruebas

| ID | Funcionalidad | Estado |
|---|---|---|
| TC-CN-001 | Inicio de sesión exitoso | PASSED |
| TC-CN-002 | Agregar producto al carrito | PASSED |
| TC-CN-003 | Eliminar producto del carrito | PASSED |
| TC-CN-004 | Completar proceso de compra | PASSED |
| TC-CN-005 | Validación de campos obligatorios | PASSED |
| GH-001 | Acceso con credenciales válidas | PASSED |
| GH-002 | Acceso con contraseña incorrecta | PASSED |

## 4. Defectos encontrados

**Total de defectos reproducibles registrados: 0**

No se generaron reportes de defectos porque no se observaron fallos en los escenarios ejecutados.

## 5. Observaciones

- El sistema permitió iniciar sesión con credenciales válidas.
- El carrito permitió agregar y eliminar productos.
- El checkout permitió completar una compra.
- El formulario impidió avanzar con los campos obligatorios vacíos.
- El inicio de sesión rechazó credenciales incorrectas.

## 6. Conclusión

No se encontraron defectos reproducibles durante las pruebas realizadas.

Este resultado no garantiza la ausencia total de defectos en la aplicación, sino únicamente que los casos ejecutados cumplieron sus resultados esperados.

# Casos de prueba de caja negra

## TC-CN-001: Inicio de sesión exitoso

**Aplicación:** SauceDemo (Swag Labs)

**URL:** https://www.saucedemo.com/

**Objetivo:** Verificar que un usuario registrado pueda acceder correctamente al catálogo.

**Precondiciones:**
- Tener acceso a Internet.
- Estar en la página de inicio de sesión.
- No tener una sesión iniciada.

**Datos de prueba:**
- Usuario: standard_user
- Contraseña: secret_sauce

**Pasos:**
1. Abrir https://www.saucedemo.com/
2. Ingresar el usuario standard_user.
3. Ingresar la contraseña secret_sauce.
4. Presionar Login.
5. Observar la página mostrada.

**Resultado esperado:**
El sistema debe permitir el acceso al catálogo de productos y mostrar el título Products.

**Resultado obtenido:**
El sistema permitió iniciar sesión correctamente y mostró el catálogo Products.

**Estado:** PASSED

**Evidencia:** evidencias/capturas/TC-CN-001_login_exitoso.png

---

## TC-CN-002: Agregar producto al carrito

**Aplicación:** SauceDemo (Swag Labs)

**Objetivo:** Verificar que un usuario pueda agregar correctamente un producto al carrito de compras.

**Precondiciones:**
- Haber iniciado sesión con standard_user.
- Estar en la página Products.
- Tener el carrito vacío.

**Datos de prueba:**
- Usuario: standard_user
- Producto: Sauce Labs Backpack
- Cantidad: 1

**Pasos:**
1. Iniciar sesión con standard_user.
2. Acceder al catálogo Products.
3. Buscar el producto Sauce Labs Backpack.
4. Presionar el botón Add to cart.
5. Verificar que el botón cambie a Remove.
6. Comprobar que el contador del carrito muestre 1.
7. Abrir el carrito y verificar que aparezca Sauce Labs Backpack.

**Resultado esperado:**
El sistema debe agregar el producto seleccionado al carrito, actualizar el contador a 1 y mostrar el producto en la lista del carrito.

**Resultado obtenido:**
El producto Sauce Labs Backpack apareció correctamente en el carrito y el contador mostró 1.

**Estado:** PASSED

**Evidencia:** evidencias/capturas/TC-CN-002_agregar_carrito.png

---

## TC-CN-003: Eliminar producto del carrito

**Aplicación:** SauceDemo (Swag Labs)

**Objetivo:** Verificar que el usuario pueda eliminar correctamente un producto del carrito de compras.

**Precondiciones:**
- Haber iniciado sesión con standard_user.
- Tener agregado Sauce Labs Backpack al carrito.
- Estar en la página del carrito de compras.

**Datos de prueba:**
- Usuario: standard_user
- Producto: Sauce Labs Backpack
- Cantidad inicial: 1
- Cantidad final esperada: 0

**Pasos:**
1. Iniciar sesión con standard_user.
2. Agregar Sauce Labs Backpack al carrito.
3. Ingresar al carrito de compras.
4. Verificar que aparezca Sauce Labs Backpack.
5. Presionar el botón Remove.
6. Comprobar que el producto desaparezca del carrito.
7. Verificar que el contador ya no muestre 1.

**Resultado esperado:**
El sistema debe eliminar el producto seleccionado, dejar el carrito vacío y actualizar el contador.

**Resultado obtenido:**
El producto Sauce Labs Backpack desapareció correctamente y el carrito quedó vacío.

**Estado:** PASSED

**Evidencia:** evidencias/capturas/TC-CN-003_eliminar_producto.png

---

## TC-CN-004: Completar proceso de compra

**Aplicación:** SauceDemo (Swag Labs)

**Objetivo:** Verificar que el sistema permita completar una compra correctamente utilizando datos válidos.

**Precondiciones:**
- Haber iniciado sesión con standard_user.
- Tener acceso al catálogo de productos.
- Tener al menos un producto disponible para comprar.

**Datos de prueba:**
- Usuario: standard_user
- Producto: Sauce Labs Backpack
- Nombre: Juan
- Apellido: Pérez
- Código postal: 0000

**Pasos:**
1. Iniciar sesión en SauceDemo.
2. Acceder al catálogo Products.
3. Agregar Sauce Labs Backpack al carrito.
4. Ingresar al carrito de compras.
5. Presionar Checkout.
6. Introducir Juan como nombre.
7. Introducir Pérez como apellido.
8. Introducir 0000 como código postal.
9. Presionar Continue.
10. Verificar el resumen de compra.
11. Presionar Finish.
12. Verificar el mensaje de confirmación.

**Resultado esperado:**
El sistema debe permitir completar el proceso de compra y mostrar el mensaje "Thank you for your order!".

**Resultado obtenido:**
Se completó correctamente el proceso de checkout y apareció el mensaje "Thank you for your order!".

**Estado:** PASSED

**Evidencias:**
- evidencias/capturas/TC-CN-004_checkout_resumen.png
- evidencias/capturas/TC-CN-004_compra_exitosa.png

---

## TC-CN-005: Validación de campos obligatorios en Checkout

**Aplicación:** SauceDemo (Swag Labs)

**Objetivo:** Verificar que el sistema valide los campos obligatorios e impida continuar una compra con datos incompletos.

**Precondiciones:**
- Haber iniciado sesión con standard_user.
- Tener Sauce Labs Backpack agregado al carrito.
- Encontrarse en el formulario Checkout: Your Information.

**Datos de prueba:**
- Usuario: standard_user
- Producto: Sauce Labs Backpack
- First Name: vacío
- Last Name: vacío
- Zip/Postal Code: vacío

**Pasos:**
1. Iniciar sesión en SauceDemo.
2. Agregar Sauce Labs Backpack al carrito.
3. Abrir el carrito.
4. Presionar Checkout.
5. Dejar vacíos los campos First Name, Last Name y Zip/Postal Code.
6. Presionar Continue.
7. Observar el mensaje mostrado por el sistema.

**Resultado esperado:**
El sistema debe impedir continuar la compra y mostrar el mensaje "Error: First Name is required".

**Resultado obtenido:**
El formulario mostró "Error: First Name is required" y no permitió continuar al resumen de compra.

**Estado:** PASSED

**Evidencia:** evidencias/capturas/TC-CN-005_campos_obligatorios.png

---

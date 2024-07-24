# Flujo de compra
El flujo de compra describe los pasos que debe seguir unx clientx para realizar una compra en la página web.

## Relevancia y suposiciones
El flujo de compra es un flujo de primera prioridad para pulsar, es el canal mediante el que le colectivo se mantiene y florece.

Este flujo está diseñado para funcionar con las personas del segmento A de clientes.

## Diagrama del Flujo
```mermaid
flowchart TD
    classDef comunidad fill:#069a2e
    classDef devops fill:#ea7500
    classDef taller fill:#3465a4
    classDef legal fill:#a7074b

    U(Usuario) 
    I[Instagram]:::comunidad 
    G[Galeria Virtual]:::devops
    DM[DM comunidad]:::comunidad 

    U -->|Navegando en| I
    I-->|Post de \n galeria| G
    U -->|Accede a| G
    I -->|Se comunica \n por chat| DM
    DM -->|Documentar \n soluciones| DM

    P(Página de producto):::devops
    C[Carrito y cupones]:::comunidad
    Rutas[Selección de la \n ruta de entrega]:::taller

    I -->|Post de \n producto| P
    DM -->|Redirección| P
    G -->|Selección de \n producto| P
    C -->|Regresar| P
    P -->|Revisar| C

    Proceder{¿Proceder \n al pago?}
    C --> Proceder
    Proceder -->|Continuar \n comprando| G
    Proceder -->|Proceder| Rutas

    Indicaciones[Mandar indicaciones\n de pago por mail]:::legal
    Inventario[Apartar en\n el inventario]:::taller
    Ventas[Crear nueva \n cotización ]:::devops

    Rutas --> Indicaciones
    Rutas --> Inventario
    Rutas --> Ventas


```
## Pruebas funcionales
Las pruebas se dividen en dos categorias

### Pruebas de comunidad
Pruebas a cada una de las flechas del flujo que van desde el Usuario, a traves de Instagram y la Galeria Virtual, y que terminan en llegar a la página del producto. 


### Pruebas de ventas
Pruebas a cada una de las flechas del flujo que van desde la página del producto y que terminan en generar los tres entregables. 

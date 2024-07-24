# Flujo de compra
El flujo de compra describe los pasos que debe seguir unx clientx para realizar una compra en la página web.

## Relevancia y suposiciones
El flujo de compra es un flujo de primera prioridad para pulsar, es el canal mediante el que le colectivo se mantiene y florece.

Este flujo está diseñado para funcionar con las personas del segmento A de clientes.

## Diagrama del Flujo
```mermaid
flowchart TD
    U(Usuario) 
    I[Instagram]
    G[Galeria Virtual]
    DM[DM comunidad]

    U -->|Navegando en| I
    I -->|Post de \n galeria| G
    U -->|Accede a| G
    I -->|Se comunica \n por chat| DM
    DM -->|Documentar \n soluciones| DM

    P(Página de producto)
    C[Carrito y cupones]
    Rutas[Selección de la \n ruta de entrega]

    I -->|Post de \n producto| P
    DM -->|Redirección| P
    G -->|Selección de \n producto| P
    C -->|Regresar| P
    P -->|Revisar| C

    Proceder{¿Proceder \n al pago?}
    C --> Proceder
    Proceder -->|Continuar \n comprando| G
    Proceder -->|Proceder| Rutas

    Indicaciones[Mandar indicaciones\n de pago por mail]
    Inventario[Apartar en\n el inventario]
    Ventas[Crear nueva \n cotización ]

    Rutas --> Indicaciones
    Rutas --> Inventario
    Rutas --> Ventas


```

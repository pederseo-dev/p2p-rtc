RTC-P2P
Descripción

RTC-P2P es un protocolo y capa de transporte peer-to-peer (P2P) diseñado para permitir la conectividad directa entre dispositivos usando WebRTC, de manera universal y sin necesidad de backend permanente.

Esta capa abstrae la complejidad de NAT traversal, keep-alive y reconexión que WebRTC proporciona automáticamente, ofreciendo un canal de comunicación confiable entre peers.

Su objetivo es servir como fundamento para aplicaciones distribuidas, pudiendo interoperar con cualquier lenguaje que implemente WebRTC o soporte DataChannels, incluyendo páginas web estáticas.

Características clave

Conectividad P2P universal

Compatible con navegadores, Python, Node.js, Go, Rust y otros lenguajes con soporte WebRTC.

Permite comunicación directa entre dispositivos sin servidores intermediarios para el transporte de datos.

Sin backend obligatorio

La señalización inicial requiere solo un bootstrap liviano.

Una vez establecidos los peers, la comunicación es totalmente descentralizada.

Compatibilidad con páginas estáticas

Una simple página web puede actuar como peer o controlador.

No se necesita servidor web dinámico; basta con un archivo HTML + JS.

Transparencia de la red

WebRTC maneja NAT traversal, ICE candidates y reintentos de conexión.

El protocolo solo necesita ocuparse de la gestión de peers y lógica de aplicación.

Independencia de lenguaje

Cualquier peer que implemente WebRTC DataChannel puede integrarse.

Permite la construcción de sistemas distribuidos heterogéneos: Python ↔ Browser ↔ Node ↔ Rust.

Eventos y estado de conexión

Eventos como connected, disconnected o failed permiten reaccionar a cambios de estado de peers.

Mantener un registro mínimo de peers activos para facilitar la capa de aplicación.

Casos de uso

Aplicaciones de control remoto desde un navegador a cualquier lenguaje.

Sistemas de ejecución remota de funciones entre peers.

Redes de agentes distribuidos o sistemas multiagente.

Aplicaciones P2P cross-device sin infraestructura de servidor.

Integración de páginas web estáticas con peers activos en otros lenguajes.

Arquitectura conceptual
          ┌───────────────────────┐
          │     Bootstrap (WS)     │
          │  Descubrimiento mínimo │
          └─────────┬─────────────┘
                    │
        ┌───────────┴───────────┐
        │       RTC-P2P         │
        │  Conexión P2P directa │
        │  DataChannels seguros  │
        └───────────┬───────────┘
                    │
      ┌─────────────┴─────────────┐
      │                           │
[ Browser Peer ]           [ Python Peer ]
- JS / HTML                - Python / aiortc
- Páginas estáticas         - Peer activo
- Control / UI             - Funciones / Scripts

Beneficios

Minimiza la complejidad de networking al delegar NAT traversal y keep-alive a WebRTC.

Facilita el desarrollo de sistemas cross-language y cross-device.

Compatible con entornos restringidos (páginas estáticas, navegadores móviles, scripts ligeros).

Proporciona una base sólida para capas superiores, como ejecución remota de funciones, comunicación multiagente o sistemas distribuidos heterogéneos.

Próximos pasos para desarrollo

Implementar bootstrap mínimo para señalización de peers.

Definir protocolo de mensajes para gestión de peers.

Construir ejemplo mínimo de peers Browser ↔ Python.

Probar mesh, star y rooms para la capa de aplicación.

Evaluar seguridad y sandboxing para ejecución remota de funciones.

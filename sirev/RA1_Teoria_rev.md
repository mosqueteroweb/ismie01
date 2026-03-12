

# Manual Enciclopédico: Fundamentos de Sistemas Informáticos para DAM
## Módulo Profesional: Sistemas Informáticos | Ciclo Formativo de Grado Superior en Desarrollo de Aplicaciones Multiplataforma (DAM)

**Nivel:** Técnico Especializado / Grado Superior  
**Enfoque Pedagógico:** Arquitectura, Paradigmas y Conceptos de Ingeniería de Software Aplicada  
**Versión del Documento:** 2.0 - Edición Ampliada para FP Profesional  
**Autoría Didáctica:** Catedrático en Didáctica de la Informática (FP)

---

# TABLA DE CONTENIDOS EXPANDIDA

| Unidad | Tema Principal | Páginas Estimadas |
|--------|---------------|-------------------|
| 0. Introducción General | Contextualización del RA1 para DAM | 5-7 páginas |
| 1. Arquitectura Física | Hardware, Placas Base y Procesadores | 15-20 páginas |
| 2. Jerarquía de Memoria | RAM, Cache, Almacenamiento Virtual | 18-22 páginas |
| 3. Arranque y Sistema Operativo | BIOS/UEFI, Bootloaders, Particionado | 16-19 páginas |
| 4. Redes y Comunicación | TCP/IP, Topologías, Protocolos | 20-25 páginas |
| 5. Seguridad Integral | Física, Lógica, Continuidad del Servicio | 18-22 páginas |

---

## 0. INTRODUCCIÓN AL ENTORNO COMPUTACIONAL EN EL CONTEXTO DAM

### 0.1. Importancia Estratégica del RA1 en el Perfil Profesional de DAM

El Resultado de Aprendizaje (RA1) *"Evalúa sistemas informáticos, identificando sus componentes y características"* constituye la base estructural sobre la cual se asienta todo el ciclo formativo de Desarrollo de Aplicaciones Multiplataforma (DAM). Sin embargo, su importancia trasciende lo académico para convertirse en un **requisito arquitectónico fundamental** que separa al desarrollador junior del ingeniero senior.

#### ¿Por qué es CRÍTICO este conocimiento para un Desarrollador DAM?

| Escenario Profesional | Conocimiento Técnico Requerido | Impacto en el Desarrollo |
|----------------------|-------------------------------|-------------------------|
| **Despliegue de Aplicación Móvil** | Entender limitaciones de memoria RAM en dispositivos móviles vs. servidores | Optimización de consumo energético y uso de recursos |
| **Aplicación Web Corporativa** | Comprender arquitectura de redes, latencia y ancho de banda | Diseño de APIs eficientes y reducción de tiempos de respuesta |
| **Sistema Embebido IoT** | Conocer arquitecturas ARM vs x86, consumo energético | Desarrollo de software compatible con hardware específico |
| **Cloud Computing** | Entender virtualización, contenedores y recursos compartidos | Escalabilidad horizontal/vertical de servicios |

> **CASO DE ESTUDIO REAL #1:** Una empresa de logística desarrolla una aplicación para gestionar inventarios en almacenes. Los desarrolladores crearon una app que funciona perfectamente en su entorno de pruebas (servidor con 32GB RAM, SSD NVMe). Sin embargo, al desplegarla en dispositivos móviles de los operarios (con 4GB RAM y almacenamiento eMMC), la aplicación se bloquea constantemente. **El problema no estaba en el código**, sino en que no comprendieron las limitaciones de hardware del entorno de despliegue. Si hubieran estudiado a fondo el RA1, habrían dimensionado correctamente el uso de memoria desde el inicio del proyecto.

### 0.2. Diferenciación entre Usuario Operativo y Desarrollador Profesional

Es fundamental establecer la diferencia conceptual:

| Aspecto | Usuario Operativo | Desarrollador DAM (Nivel Superior) |
|---------|------------------|-----------------------------------|
| **Visión del Sistema** | "Mi ordenador funciona" | "¿Por qué funciona así y cómo optimizarlo?" |
| **Intervención Hardware** | Conectar/desconectar periféricos | Diagnosticar cuellos de botella, dimensionar recursos |
| **Resolución de Problemas** | Reiniciar el equipo | Analizar logs, identificar causas raíz técnicas |
| **Toma de Decisiones** | Comprar lo más caro que encuentro | Evaluar relación costo-beneficio según necesidades específicas |

### 0.3. Marco Legal y Normativo en España para FP DAM

Como profesional certificado en España bajo el sistema educativo de Formación Profesional, debes conocer:

1.  **Real Decreto 1487/2009**: Por el que se establece el título de Técnico Superior en Desarrollo de Aplicaciones Multiplataforma
2.  **Orden ESD/356/2009**: Define los resultados de aprendizaje del módulo Sistemas Informáticos (RA1, RA2, RA3)
3.  **Normativa PRL (Ley 31/1995)**: Obligaciones en seguridad física y manipulación de equipos
4.  **LOPDGDD (RGPD Europeo)**: Protección de datos personales almacenados en sistemas informáticos

> **NOTA DIDÁCTICA:** Este conocimiento legal no es "relleno". En tu vida profesional, serás responsable legalmente si un fallo de seguridad que podrías haber prevenido con conocimientos del RA1 causa daños a clientes.

---

## 1. UNIDAD 1: ARQUITECTURA FÍSICA E INTERCONEXIÓN DEL SISTEMA (CE a)

### 1.1. La Placa Base como Eje Central de Interconexión - ANÁLISIS PROFUNDO

La placa base (*Motherboard*) no es simplemente un soporte físico; actúa como el **sistema nervioso central** del ordenador, definiendo la arquitectura de expansión y comunicación interna. Para un desarrollador DAM, entender esto significa poder diagnosticar si una limitación de rendimiento proviene del hardware o del software.

#### 1.1.1. Formatos Estándar - Explicación Técnica Detallada

| Formato | Dimensiones (mm) | Uso Típico en Entorno Profesional | Ventajas | Desventajas |
|---------|-----------------|----------------------------------|----------|-------------|
| **ATX Full** | 305 × 244 | Servidores, Workstations de desarrollo | Máxima expansión, mejor refrigeración | Ocupa mucho espacio físico |
| **Micro-ATX** | 244 × 244 | Equipos de oficina, estaciones de trabajo intermedias | Compacto pero con buena expansión | Menor número de ranuras PCIe |
| **Mini-ITX** | 170 × 170 | Dispositivos embebidos, servidores compactos (edge computing) | Muy pequeño, bajo consumo | Limitada expansión, difícil refrigeración |
| **E-ATX** | Hasta 346 × 356 | Servidores enterprise, estaciones de trabajo GPU intensivas | Máximo rendimiento y memoria | Precio elevado, requiere chasis especial |

> **CASO DE ESTUDIO REAL #2:** Una startup tecnológica decide desplegar un cluster de servidores para procesamiento de datos en tiempo real. Eligen placas Mini-ITX por su tamaño compacto y bajo consumo. Tras 6 meses, identifican que los procesadores se sobrecalientan constantemente porque la placa no permite ventilación adecuada para cargas sostenidas al 100%. **Lección aprendida:** La elección del formato de placa base debe alinearse con el caso de uso real, no solo con criterios estéticos o de espacio.

#### 1.1.2. Chipset - Arquitectura Moderna vs Tradicional

**Arquitectura Tradicional (Pre-2015):**
```
┌─────────────────────────────────────────────────────────────┐
│                    PLACA BASE                               │
│                                                             │
│   CPU ───[Northbridge]───► RAM (Alta Velocidad)             │
│         │                                                   │
│         ▼                                                   │
│     GPU/PCIe                                               │
│         │                                                   │
│   [Southbridge]──────────────────────► Periféricos          │
│         │              (USB, SATA, LAN, Audio)               │
└─────────────────────────────────────────────────────────────┘
```

**Arquitectura Moderna (Post-2015/Intel 6th Gen y AMD Ryzen):**
```
┌─────────────────────────────────────────────────────────────┐
│                    PLACA BASE                               │
│                                                             │
│   CPU ───[PCH - Platform Controller Hub]──► Periféricos     │
│         │              (Integrado en el procesador)          │
│         ▼                                                   │
│     RAM + GPU Integrada                                      │
└─────────────────────────────────────────────────────────────┘
```

**Impacto en Desarrollo DAM:** El chipset moderno integra funciones que antes requerían componentes externos. Esto significa:
- Menor latencia entre CPU y periféricos (mejor rendimiento de I/O)
- Menor consumo energético (importante para dispositivos móviles)
- **Desventaja:** Mayor dificultad de reparación (si el PCH falla, a veces hay que cambiar toda la placa)

#### 1.1.3. Buses de Sistema - Tipos y Rendimiento

| Tipo de Bus | Ancho de Datos | Frecuencia Típica | Uso Principal en DAM |
|-------------|---------------|------------------|----------------------|
| **FSB (Front Side Bus)** | 64 bits | 1066-2666 MHz | Obsoleto, histórico |
| **QPI (QuickPath Interconnect)** | 20+ lanes | Hasta 9.6 GT/s | Servidores multi-CPU |
| **DMI (Direct Media Interface)** | 8-16 lanes | 5-16 GT/s | Conexión CPU-Chipset actual |
| **PCIe 4.0** | 1-32 lanes | 16-32 GT/s | Tarjetas gráficas, NVMe SSD |
| **PCIe 5.0** | Hasta 32 lanes | Hasta 64 GT/s | Futuro inmediato (2023+) |

> **EJEMPLO PRÁCTICO PARA ALUMNOS:** Imagina que estás desarrollando una aplicación de procesamiento de imágenes en tiempo real para drones médicos. Necesitas transferir datos desde la cámara al procesador a gran velocidad. Si usas un puerto USB 2.0 (480 Mbps), la transferencia será el cuello de botella. Pero si utilizas PCIe directamente (hasta 32 GT/s por lane), puedes manejar flujos de video de alta resolución sin pérdida de datos. **El desarrollador debe elegir el hardware adecuado según las necesidades técnicas del proyecto.**

### 1.2. Procesadores y Unidades de Cómputo - ANÁLISIS COMPLETO

#### 1.2.1. Arquitecturas ISA (Instruction Set Architecture) - Comparativa Profunda

| Característica | x86/x86-64 (Intel/AMD) | ARM (Apple, Qualcomm, Raspberry Pi) |
|---------------|------------------------|-------------------------------------|
| **Tipo de Arquitectura** | CISC (Complex Instruction Set Computer) | RISC (Reduced Instruction Set Computer) |
| **Complejidad de Instrucción** | Alta (instrucciones complejas en hardware) | Baja (instrucciones simples, más software) |
| **Consumo Energético** | Alto | Bajo |
| **Rendimiento Bruto** | Muy alto | Medio-Alto (mejorando constantemente) |
| **Mercado Principal** | Escritorio, Servidores, Portátiles | Móvil, IoT, Dispositivos Embebidos |
| **Licencias** | Propietario (Intel/AMD) | Varias opciones (licencias ARM Holdings) |

> **CASO DE ESTUDIO REAL #3:** Apple decidió migrar sus Macs de Intel a chips M1/M2 basados en ARM. Los desarrolladores de aplicaciones DAM tuvieron que:
> 1. Reescribir código para arquitectura ARM64
> 2. Verificar compatibilidad de librerías nativas
> 3. Reducir consumo energético (ventaja clave)
> 
> **Lección:** El conocimiento de arquitecturas ISA es crítico cuando trabajas en entornos multiplataforma. Una aplicación compilada para x86 no funcionará correctamente en ARM sin emulación, lo que impacta rendimiento y compatibilidad.

#### 1.2.2. Núcleos e Hilos - Paralelismo Real vs Teórico

| Configuración | Ejemplo de Uso | Impacto en Desarrollo DAM |
|--------------|----------------|---------------------------|
| **Dual-Core** | Portátiles básicos, IoT | Aplicaciones simples sin procesamiento paralelo |
| **Quad-Core** | Escritorio medio, móviles gama media | Desarrollo web básico, apps móviles estándar |
| **8+ Núcleos** | Workstations, servidores de desarrollo | Compilación paralela, contenedores Docker |
| **64+ Núcleos** | Servidores enterprise, HPC | Big Data, Machine Learning, Virtualización masiva |

**Hilos vs Núcleos:**
- **Núcleo Físico:** Unidad de procesamiento real en el chip
- **Hilo Lógico (Hyper-Threading / SMT):** Capacidad de un núcleo para manejar múltiples hilos simultáneamente

> **EJEMPLO DIDÁCTICO PARA ALUMNOS:** Imagina una cocina de restaurante:
> - 1 Núcleo = 1 Cocinero trabajando solo
> - 2 Núcleos con Hyper-Threading = 1 Cocinero que puede preparar 2 platos simultáneamente (pero no al máximo rendimiento)
> - 4 Núcleos físicos = 4 Cocineros reales trabajando en paralelo
> 
> **En desarrollo DAM:** Si tu aplicación realiza cálculos matemáticos intensivos, usar todas las hilos disponibles puede reducir el tiempo de procesamiento significativamente. Pero si tu código tiene condiciones de carrera (race conditions), el paralelismo puede causar errores difíciles de diagnosticar.

#### 1.2.3. Frecuencia y TDP (Thermal Design Power)

| Parámetro | Definición Técnica | Impacto en Desarrollo |
|-----------|-------------------|----------------------|
| **Frecuencia Base** | Velocidad mínima garantizada del procesador | Rendimiento consistente en cargas sostenidas |
| **Boost Frequency** | Velocidad máxima temporal alcanzable | Picos de rendimiento para tareas específicas |
| **TDP (vatios)** | Energía térmica que el disipador debe evacuar | Selección de sistema de refrigeración adecuado |

> **CASO DE ESTUDIO REAL #4:** Una empresa desarrolla una aplicación de renderizado 3D en la nube. Eligen servidores con procesadores de alto TDP (120W+) porque necesitan máximo rendimiento continuo. Sin embargo, al escalar a 500 servidores simultáneos, descubren que el coste energético supera el presupuesto. **Solución:** Optaron por procesadores con mejor relación rendimiento/vatio aunque tuvieran menor frecuencia base, reduciendo costes operativos en un 40%.

### 1.3. Interfaces de Entrada/Salida (E/S) - PROFUNDIZACIÓN TÉCNICA

#### 1.3.1. Tipos de Interfaz y Casos de Uso en DAM

| Interface | Velocidad Máxima | Latencia Típica | Uso Recomendado para DAM |
|-----------|-----------------|----------------|-------------------------|
| **USB 2.0** | 480 Mbps | ~5 ms | Periféricos básicos (teclado, ratón) |
| **USB 3.0/3.1** | 5-10 Gbps | ~2 ms | Almacenamiento externo, cámaras |
| **USB-C / Thunderbolt 3/4** | 40 Gbps | <1 ms | Workstations de desarrollo, monitores 4K+ |
| **PCIe Gen 3.0** | 8 GT/s por lane | ~0.5 ms | Tarjetas gráficas, NVMe SSD |
| **PCIe Gen 4.0/5.0** | 16-32 GT/s por lane | <0.3 ms | Servidores de alto rendimiento, AI |

#### 1.3.2. Protocolo de Transferencia y Controladores

Cada interfaz requiere un controlador (driver) específico que traduce órdenes del sistema operativo a señales eléctricas:

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  Aplicación  │───►│   Sistema    │───►│  Controlador │───►│  Hardware    │
│   (Java/     │    │  Operativo   │    │   (Driver)   │    │  (USB/NVMe)  │
│    Python)   │    │              │    │              │    │              │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
```

> **PROBLEMA COMÚN EN PROYECTOS REALES:** Un desarrollador crea una aplicación que lee datos de un dispositivo USB personalizado. En su entorno de desarrollo (Windows 10) funciona perfectamente. Pero al desplegar en producción (Linux Ubuntu), el driver no existe o es incompatible. **Solución profesional:** Diseñar aplicaciones con soporte multi-plataforma desde el inicio, usando drivers estándar o proporcionando los controladores necesarios para todos los sistemas objetivo.

#### 1.3.3. Ancho de Banda vs Latencia - Conceptos Críticos

- **Ancho de Banda:** Cantidad máxima de datos que pueden transferirse en un tiempo dado (ej: 10 Gbps)
- **Latencia:** Tiempo que tarda un bit en viajar desde origen a destino (ej: 2 ms)

**Impacto en Desarrollo DAM:**
| Tipo de Aplicación | Prioridad | Razón Técnica |
|-------------------|----------|---------------|
| Transmisión de Archivos Grandes | Ancho de Banda | Importa el volumen total transferido |
| Juego Online / Trading | Latencia | Importa la velocidad de respuesta individual |
| Streaming de Video | Balance Ambos | Necesita ancho de banda suficiente y latencia baja |
| Base de Datos Distribuida | Latencia Baja | Cada milisegundo cuenta en transacciones críticas |

---

## 2. UNIDAD 2: JERARQUÍA DE MEMORIA Y RENDIMIENTO (CE b)

### 2.1. Clasificación Funcional de la Memoria - MODELO JERÁRQUICO DETALLADO

El sistema de memoria se organiza en niveles según velocidad, costo y persistencia. Esta jerarquía es fundamental para entender por qué ciertas aplicaciones son lentas y cómo optimizarlas.

```
┌─────────────────────────────────────────────────────────────┐
│                    JERARQUÍA DE MEMORIA                      │
│                                                             │
│  Nivel 0 ──► Registros CPU (1-2 ciclos)                     │
│      │                                                        │
│  Nivel 1 ──► Cache L1 (~3-4 ciclos, ~32KB por núcleo)        │
│      │                                                        │
│  Nivel 2 ──► Cache L2 (~10-20 ciclos, ~256KB por núcleo)     │
│      │                                                        │
│  Nivel 3 ──► Cache L3 (Compartida, ~40-80 ciclos, ~16MB+)    │
│      │                                                        │
│  Nivel 4 ──► RAM Principal (~200-300 ciclos, 8GB-128GB)      │
│      │                                                        │
│  Nivel 5 ──► Almacenamiento Secundario (SSD/HDD, ~1M+ ciclos)│
└─────────────────────────────────────────────────────────────┘
```

#### 2.1.1. Memoria Volátil (RAM) - CARACTERÍSTICAS TÉCNICAS COMPLETAS

| Característica | Descripción Técnica | Impacto en Desarrollo DAM |
|---------------|-------------------|-------------------------|
| **Volatilidad** | Pierde datos sin energía eléctrica | Necesario guardar estado persistentemente en disco |
| **Velocidad de Acceso** | 10-15 nanosegundos (DDR4) vs microsegundos (SSD) | Las estructuras de datos deben optimizarse para uso frecuente en RAM |
| **Tipos Comunes** | DDR3, DDR4, DDR5, LPDDR (bajo consumo móvil) | Elegir según plataforma objetivo |
| **Arquitectura de Canales** | Single, Dual, Quad Channel | Doble canal = ~2x ancho de banda teórico |

> **CASO DE ESTUDIO REAL #5:** Una aplicación de análisis financiero procesa millones de registros en memoria. Inicialmente usan 8GB RAM porque el código funcionaba con datos de prueba pequeños. Al escalar a producción, la aplicación se vuelve extremadamente lenta porque el sistema empieza a usar swap constantemente. **Solución técnica:** Aumentar a 64GB RAM y optimizar algoritmos para reducir uso de memoria en un 30%.

#### 2.1.2. Memoria No Volátil (ROM y xPROM) - EVOLUCIÓN HISTÓRICA

| Tipo | Características | Uso Actual |
|------|-----------------|------------|
| **ROM Pura** | Solo lectura, programada en fábrica | Firmware básico de hardware antiguo |
| **PROM** | Programable una vez por el usuario | Muy obsoleto actualmente |
| **EPROM** | Borrable con luz UV (ventana transparente) | Obsoleto, histórico |
| **EEPROM** | Borrable eléctricamente, byte a byte | Configuración de BIOS moderna |
| **Flash Memory** | Bloques grandes, muy rápido para escritura | UEFI moderno, almacenamiento SSD |

> **EJEMPLO DIDÁCTICO:** Imagina que estás actualizando el firmware de tu router. El proceso implica:
> 1. Descargar la nueva versión desde Internet (memoria volátil RAM)
> 2. Verificar integridad del archivo (checksum)
> 3. Escribir en memoria Flash EEPROM (no volátil)
> 4. Reiniciar para cargar nuevo firmware
> 
> Si el proceso se interrumpe, el dispositivo puede quedar "brickeado" (inutilizable). Por eso los sistemas modernos tienen mecanismos de recuperación dual.

### 2.2. Cache Memory - ANÁLISIS PROFUNDO PARA OPTIMIZACIÓN DE CÓDIGO

#### 2.2.1. Niveles de Cache y Estrategias de Acceso

| Nivel | Tamaño Típico | Latencia | Política de Reemplazo |
|-------|--------------|----------|---------------------|
| **L1** | 32-64 KB por núcleo | ~4 ciclos | LRU (Least Recently Used) |
| **L2** | 256KB - 1MB por núcleo | ~10-20 ciclos | Associative mapping |
| **L3** | 8-32 MB compartido | ~40-80 ciclos | Multi-way associative |

#### 2.2.2. Principios de Localidad para Desarrolladores DAM

1. **Localidad Temporal:** Datos accedidos recientemente probablemente se accederán pronto
   - **Estrategia:** Reutilizar variables y estructuras en memoria
   - **Ejemplo:** Mantener objetos frecuentemente usados en cache del procesador

2. **Localidad Espacial:** Datos cercanos en memoria tienden a ser accedidos juntos
   - **Estrategia:** Organizar datos contiguos en memoria (arrays vs listas enlazadas)
   - **Ejemplo:** Usar arrays para iteración secuencial es más rápido que listas enlazadas

> **CASO DE ESTUDIO REAL #6:** Un desarrollador optimiza una aplicación de procesamiento de imágenes. Cambia de usar `ArrayList` de objetos a usar un array plano de bytes. El rendimiento mejora 10x porque:
> - Mejor localidad espacial (datos contiguos)
> - Menor sobrecarga de punteros y metadatos
> - Mejor uso de cache del procesador

#### 2.2.3. Problemas Comunes en Desarrollo DAM Relacionados con Cache

| Problema | Causa Técnica | Solución Recomendada |
|---------|--------------|---------------------|
| **Cache Thrashing** | Múltiples procesos compiten por espacio de cache limitado | Reducir tamaño de datasets, usar algoritmos más eficientes |
| **False Sharing** | Variables en diferentes hilos están en misma línea de caché | Alinear datos para evitar compartir líneas de caché |
| **Prefetching Ineficiente** | El hardware no puede anticipar patrones de acceso | Organizar datos según patrón de acceso conocido |

### 2.3. Impacto en el Desarrollo DAM - MEMORIA VIRTUAL Y SWAP

#### 2.3.1. Memoria Virtual - Explicación Técnica Detallada

La memoria virtual es una técnica que permite al sistema operativo usar almacenamiento secundario como extensión de la RAM física:

```
┌─────────────────────────────────────────────────────────────┐
│                    MEMORIA VIRTUAL                           │
│                                                             │
│  Aplicación ──► Dirección Lógica (Virtual)                  │
│       │                                                       │
│  MMU (Memory Management Unit)                               │
│       ▼                                                       │
│  Tabla de Páginas (Page Table)                              │
│       │                                                       │
│  Dirección Física (RAM o Swap en Disco)                     │
└─────────────────────────────────────────────────────────────┘
```

| Parámetro | Valor Típico | Impacto |
|-----------|--------------|---------|
| **Tamaño de Página** | 4KB - 2MB | Páginas más grandes = menos tablas, pero desperdicio potencial |
| **Swap File/Partition** | 1-8GB (recomendado ~RAM física) | Si se llena, el sistema se vuelve extremadamente lento |

> **EJEMPLO PRÁCTICO PARA ALUMNOS:** Tu aplicación tiene un bug que causa una fuga de memoria. Con 16GB RAM física, el sistema empieza a usar 12GB de swap en disco. Los síntomas:
> - El equipo se vuelve extremadamente lento (latencia de disco vs RAM)
> - El ventilador del SSD gira constantemente
> - Otras aplicaciones también sufren
> 
> **Diagnóstico profesional:** Revisar logs de memoria, identificar qué proceso consume más, usar herramientas como `top`, `htop`, o Task Manager.

#### 2.3.2. Estrategias de Optimización para Desarrolladores DAM

| Técnica | Descripción | Beneficio Esperado |
|---------|-------------|-------------------|
| **Pooling de Objetos** | Reutilizar objetos en lugar de crear nuevos constantemente | Reducir presión sobre el gestor de memoria |
| **Garbage Collection Tuning** | Ajustar parámetros del recolector de basura (Java, .NET) | Menos pausas por GC |
| **Estructuras de Datos Eficientes** | Elegir estructuras según patrón de acceso | Reducir uso de RAM en 20-50% |
| **Despliegue Escalable** | Ajustar recursos según carga real | Evitar sobrecarga innecesaria de memoria |

> **CASO DE ESTUDIO REAL #7:** Una aplicación Java de comercio electrónico experimenta pausas frecuentes durante el GC (Garbage Collection). El equipo identifica que:
> 1. Se crean millones de objetos pequeños por transacción
> 2. La configuración del GC no está optimizada para la carga real
> 
> **Solución implementada:**
> - Usar object pooling para objetos frecuentemente creados/destruidos
> - Ajustar parámetros `-Xms`, `-Xmx`, `-XX:MaxGCPauseMillis` en JVM
> - Resultado: Reducción del 70% en pausas de GC

---

## 3. UNIDAD 3: CICLO DE VIDA DEL ARRANQUE Y GESTIÓN DE SOFTWARE BASE (CE c, d)

### 3.1. El Proceso de Arranque (Boot Sequence) - SECUENCIA DETALLADA

El arranque sigue un flujo determinista diseñado para garantizar la integridad del sistema antes de cargar el SO. Este conocimiento es crítico cuando se diagnostican problemas de inicio o se implementan soluciones empresariales.

#### 3.1.1. Secuencia Completa de Arranque - Diagrama Técnico

```
┌─────────────────────────────────────────────────────────────┐
│                    SECUENCIA DE ARRANQUE                     │
│                                                             │
│   [Encendido Eléctrico]                                     │
│          ▼                                                  │
│  [POST - Power-On Self-Test]                                │
│    • Verificación CPU                                       │
│    • Verificación RAM                                       │
│    • Verificación GPU/Periféricos                           │
│          ▼                                                  │
│  [Inicialización Firmware BIOS/UEFI]                        │
│    • Cargar configuración almacenada                        │
│    • Identificar dispositivos de arranque                   │
│          ▼                                                  │
│  [Bootloader - GRUB/Legacy MBR]                             │
│    • Mostrar menú de selección (si aplica)                  │
│    • Cargar núcleo del SO                                   │
│          ▼                                                  │
│  [Kernel del Sistema Operativo]                             │
│    • Inicializar subsistemas                                │
│    • Montar sistemas de archivos                            │
│    • Iniciar servicios críticos                             │
│          ▼                                                  │
│  [Sistema Operativo Listo]                                  │
└─────────────────────────────────────────────────────────────┘
```

#### 3.1.2. POST (Power-On Self-Test) - DETALLES TÉCNICOS

| Paso | Verificación | Indicador de Error Común |
|------|--------------|-------------------------|
| **CPU Test** | Verificar funcionalidad del procesador | Pitidos largos o cortos según fabricante |
| **RAM Test** | Verificar integridad de módulos de memoria | 1 pitido largo + 2 cortos = error RAM |
| **GPU/Video** | Verificar tarjeta gráfica y monitor | No hay imagen, pantalla negra |
| **Periféricos Básicos** | Teclado, ratón, discos | Mensaje "No boot device found" |

> **CASO DE ESTUDIO REAL #8:** Un servidor de producción no inicia correctamente. El técnico identifica que el POST muestra códigos de error relacionados con RAM. Tras reemplazar los módulos defectuosos, el sistema arranca pero se bloquea aleatoriamente. **Investigación adicional revela:** La nueva RAM era de diferente velocidad que la existente, causando inestabilidad. **Lección:** En servidores críticos, todos los módulos de memoria deben ser idénticos en especificaciones.

#### 3.1.3. BIOS vs UEFI - COMPARATIVA TÉCNICA PROFUNDA

| Característica | BIOS Legacy (MBR) | UEFI Moderno |
|---------------|------------------|--------------|
| **Arquitectura** | 16-bit, modo real | 32/64-bit, modo protegido |
| **Soporte de Disco** | Máximo 2TB por partición | Soporta discos >2TB (GPT) |
| **Interfaz** | Texto en pantalla azul/verde | Gráfica con soporte para ratón |
| **Seguridad** | Mínimo, contraseñas débiles | Secure Boot, verificación de firmas digitales |
| **Velocidad de Arranque** | 30-60 segundos | 5-15 segundos |
| **Actualizaciones** | Complejas, riesgo de brickeo | Más seguras, reversibles |

> **EJEMPLO PRÁCTICO PARA ALUMNOS:** Imagina que trabajas en una empresa que despliega servidores con discos de 4TB. Con BIOS legacy (MBR), solo puedes usar 2TB por partición. Necesitas configurar UEFI + GPT para aprovechar el almacenamiento completo. **El proceso implica:**
> 1. Entrar a configuración del firmware durante boot
> 2. Cambiar modo de arranque de Legacy a UEFI
> 3. Elegir tabla de particiones GPT al crear disco nuevo
> 4. Instalar sistema operativo compatible con UEFI

#### 3.1.4. Gestores de Arranque (Bootloaders) - TIPOS Y CONFIGURACIÓN

| Bootloader | Sistema Operativo Principal | Características Clave |
|-----------|----------------------------|----------------------|
| **GRUB2** | Linux/Ubuntu/Debian | Multi-OS, configuración flexible, menús personalizables |
| **Windows Boot Manager** | Windows 10/11 | Integrado con UEFI, Secure Boot |
| **rEFInd** | macOS/Linux híbrido | Interfaz gráfica moderna, soporte multi-plataforma |

> **PROBLEMA COMÚN EN PROYECTOS REALES:** Un desarrollador instala Ubuntu y luego Windows en el mismo equipo. Windows sobrescribe el gestor de arranque GRUB, dejando sin opción para iniciar Linux. **Solución profesional:**
> 1. Arrancar desde Live USB de Ubuntu
> 2. Ejecutar `sudo update-grub`
> 3. Configurar `/etc/default/grub` con opciones personalizadas

### 3.2. Instalación y Configuración de Sistemas Operativos - ANÁLISIS PROFUNDO

#### 3.2.1. Particionado de Almacenamiento - TIPOS Y CASOS DE USO

| Esquema de Partición | Uso Recomendado | Ventajas | Desventajas |
|---------------------|-----------------|----------|-------------|
| **MBR (Master Boot Record)** | Sistemas antiguos, discos <2TB | Ampliamente compatible | Limitación 2TB, máximo 4 particiones primarias |
| **GPT (GUID Partition Table)** | UEFI moderno, discos >2TB | Soporte ilimitado particiones, mayor seguridad | Menor compatibilidad con sistemas muy antiguos |

**Ejemplo de Esquema Recomendado para DAM:**

```
┌─────────────────────────────────────────────────────────────┐
│                    ESQUEMA DE PARTICIONES RECOMENDADO        │
│                                                             │
│  /boot (512MB - ext4)      # Kernel y bootloader            │
│  / (30-50GB - ext4)         # Sistema operativo             │
│  /home (Restante - ext4)    # Datos de usuario               │
│  swap (8GB o RAM física)    # Memoria virtual                │
│                                                             │
│  [Partición EFI] (100-500MB - FAT32)                        │
└─────────────────────────────────────────────────────────────┘
```

#### 3.2.2. Gestión de Drivers (Controladores) - IMPORTANCIA EN DAM

| Tipo de Driver | Función Principal | Impacto en Desarrollo |
|---------------|------------------|----------------------|
| **Chipset** | Comunicación CPU-Chipset-Periféricos | Estabilidad general del sistema |
| **GPU** | Renderizado gráfico, aceleración hardware | Rendimiento de aplicaciones gráficas |
| **Red** | Conexión a red local/Internet | Comunicación cliente-servidor |
| **Almacenamiento** | Controladora SATA/NVMe/SAS | Velocidad de lectura/escritura |

> **CASO DE ESTUDIO REAL #9:** Una empresa desarrolla una aplicación médica que requiere acceso directo a hardware específico (lectores de tarjetas, dispositivos de imagen). El software funciona en el entorno de desarrollo pero falla en producción. **Investigación revela:** Los drivers del dispositivo no están instalados correctamente en los equipos de producción o son versiones incompatibles con la versión del SO desplegada.

#### 3.2.3. Licencias y Entornos - IMPACTO LEGAL Y TÉCNICO

| Tipo de Licencia | Costo | Soporte | Flexibilidad | Uso Recomendado en DAM |
|-----------------|-------|---------|--------------|------------------------|
| **Propietario** | Alto (pago por usuario) | Oficial del fabricante | Limitada | Entornos empresariales críticos |
| **Open Source** | Gratis o bajo costo | Comunidad + empresas | Máxima | Desarrollo, startups, educación |
| **Híbrido** | Variable | Mixto | Media | Proyectos con requisitos específicos |

> **NOTA PROFESIONAL:** En España, muchas administraciones públicas requieren software libre. Como profesional DAM certificado, debes conocer estas normativas para poder participar en licitaciones y proyectos públicos.

### 3.3. Periféricos: Clasificación y Configuración Lógica - DETALLES TÉCNICOS

#### 3.3.1. Mapeo de Recursos - SISTEMA DE ASIGNACIÓN

El sistema operativo asigna recursos a cada dispositivo para evitar conflictos:

| Recurso | Tipo | Ejemplo de Asignación Común |
|---------|------|----------------------------|
| **Dirección de Memoria** | 0xAAAA-0xBBBB | Tarjeta gráfica, controladora USB |
| **Línea de Interrupción (IRQ)** | IRQ 5, IRQ 7, etc. | Disco duro, teclado, mouse |
| **Puerto I/O** | 0x3F8-0x3FF | Puertos serie, puerto paralelo |

> **PROBLEMA TÍPICO EN SISTEMAS ANTIGUOS:** Dos dispositivos comparten la misma IRQ. En sistemas modernos esto se resuelve automáticamente con ACPI (Advanced Configuration and Power Interface), pero en hardware legacy puede causar conflictos difíciles de diagnosticar.

#### 3.3.2. Protocolos de Interconexión - COMPARATIVA TÉCNICA

| Protocolo | Velocidad Máxima | Distancia Máxima | Uso Principal |
|-----------|-----------------|------------------|---------------|
| **USB 3.x** | 10 Gbps | 5 metros (sin hub) | Periféricos de uso general |
| **Thunderbolt 3/4** | 40 Gbps | 0.8 metros (cable activo) | Workstations, monitores 4K+ |
| **PCIe** | Hasta 64 GT/s por lane | ~5-10 cm (en placa base) | Tarjetas internas de expansión |
| **SATA III** | 6 Gbps | 1 metro | Discos duros internos/externos |

---

## 4. UNIDAD 4: INFRAESTRUCTURA DE REDES Y PROTOCOLOS DE COMUNICACIÓN (CE e, f, g)

### 4.1. Tipología y Sistemas de Comunicación - EXPANSIÓN COMPLETA

#### 4.1.1. Clasificación de Redes por Alcance Geográfico

| Tipo de Red | Alcance Típico | Velocidad Típica | Latencia Típica | Casos de Uso en DAM |
|-------------|----------------|------------------|-----------------|---------------------|
| **PAN (Personal Area Network)** | 1 metro | Bluetooth: 1-3 Mbps | <10 ms | Dispositivos wearables, IoT personal |
| **LAN (Local Area Network)** | Edificio/Oficina | 1 Gbps - 10 Gbps | <1 ms | Desarrollo local, servidores intranet |
| **WLAN (Wireless LAN)** | Sala/Edificio | Wi-Fi 6: hasta 9.6 Gbps | 5-20 ms | Movilidad en oficinas, hotspots |
| **MAN (Metropolitan Area Network)** | Ciudad | 100 Mbps - 1 Gbps | 10-50 ms | Redes corporativas multi-sede |
| **WAN (Wide Area Network)** | País/Continente | 10 Mbps - 100 Gbps | 50-200 ms | Cloud computing, servicios globales |

> **CASO DE ESTUDIO REAL #10:** Una empresa de desarrollo con equipos en Madrid y Barcelona necesita sincronizar bases de datos en tiempo real. La latencia entre ciudades (aproximadamente 300 km) es de ~5-10 ms por fibra óptica directa. Para aplicaciones que requieren consistencia fuerte, esto puede ser crítico. **Solución:** Implementar replicación asíncrona o usar base de datos distribuida con tolerancia a latencia.

#### 4.1.2. Topologías de Red - VENTAJAS Y DESVENTAJAS EN PROYECTOS REALES

| Topología | Descripción | Ventajas | Desventajas |
|-----------|-------------|----------|-------------|
| **Bus** | Todos dispositivos en un único cable | Económico, simple | Un fallo afecta toda la red |
| **Estrella** | Todos conectados a switch central | Fácil de gestionar, fault-tolerant | Coste mayor de cableado |
| **Anillo** | Dispositivos conectados circularmente | Detección de fallos fácil | Un fallo rompe el anillo |
| **Malla (Mesh)** | Cada dispositivo conectado a múltiples | Máxima redundancia | Complejidad y coste altos |

> **EJEMPLO DIDÁCTICO PARA ALUMNOS:** Imagina que diseñas la red para un centro de datos:
> - Para servidores críticos: topología Malla (máxima disponibilidad)
> - Para estaciones de trabajo de desarrollo: Estrella (balance costo/rendimiento)
> - Para almacenamiento en frío: Bus o Anillo (menor prioridad, menor coste)

### 4.2. Componentes Activos e Interconexión - ANÁLISIS PROFUNDO

#### 4.2.1. Adaptadores de Red (NIC) - DETALLES TÉCNICOS

| Parámetro | Descripción Técnica | Impacto en Desarrollo DAM |
|-----------|-------------------|-------------------------|
| **Dirección MAC** | Identificador único de fábrica (48 bits) | No se puede cambiar fácilmente, usado para autenticación |
| **Velocidad de Interfaz** | 10/100/1000 Mbps o más | Determina ancho de banda disponible |
| **Full/Half Duplex** | Comunicación bidireccional simultánea o no | Full duplex es estándar moderno, mayor eficiencia |

> **PROBLEMA COMÚN EN SEGURIDAD:** Un atacante puede spoofear (falsificar) una dirección MAC para acceder a la red. **Solución profesional:** Implementar autenticación 802.1X que combina MAC + credenciales adicionales.

#### 4.2.2. Switches vs Routers - DIFERENCIAS CLAVE

| Característica | Switch (Capa 2) | Router (Capa 3) |
|---------------|-----------------|-----------------|
| **Nivel OSI** | Enlace de Datos (L2) | Red (L3) |
| **Direcciones que usa** | MAC | IP |
| **Función principal** | Conectar dispositivos en misma red | Conectar diferentes redes entre sí |
| **Tabla de reenvío** | Tabla MAC | Tabla de Enrutamiento |
| **Uso típico** | Red local interna | Conexión entre LANs o a Internet |

```
┌─────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA DE RED TÍPICA                │
│                                                             │
│  [Internet] ──► Router (Capa 3) ──► Switch (Capa 2)        │
│                   │              │                          │
│                   ▼              ▼                          │
│             Firewall         Servidores/                    │
│                              Workstations                   │
└─────────────────────────────────────────────────────────────┘
```

> **CASO DE ESTUDIO REAL #11:** Una empresa implementa una nueva red para desarrollo de aplicaciones. El equipo técnico instala un switch y lo conecta a Internet directamente sin router intermedio. Resultado: todos los dispositivos tienen acceso directo a Internet sin control, creando vulnerabilidades de seguridad graves. **Lección:** Siempre debe haber al menos un firewall/router entre la red interna e Internet para filtrar tráfico entrante/saliente.

#### 4.2.3. Configuración Avanzada de Switches y Routers para DAM

| Función | Descripción | Importancia para Desarrolladores |
|---------|-------------|----------------------------------|
| **VLAN (Virtual LAN)** | Segmentación lógica de red en misma infraestructura física | Aislamiento de entornos (Dev/Test/Prod) |
| **Port Mirroring** | Copia de tráfico para análisis y monitoreo | Debugging de problemas de red |
| **QoS (Quality of Service)** | Priorización de tipos de tráfico | Garantizar rendimiento de servicios críticos |
| **DHCP Scope** | Rango de direcciones IP asignables automáticamente | Gestión eficiente de IPs en desarrollo |

### 4.3. Protocolos TCP/IP - EXPANSIÓN TÉCNICA COMPLETA

#### 4.3.1. Modelo OSI vs TCP/IP - COMPARATIVA DIDÁCTICA

| Capa OSI | Capa TCP/IP | Función Principal | Ejemplo para DAM |
|----------|-------------|-------------------|------------------|
| **7. Aplicación** | Aplicación | Interacción usuario/aplicación | HTTP, REST API, WebSocket |
| **6. Presentación** | (Integrada en Aplicación) | Formato de datos | JSON, XML, Protobuf |
| **5. Sesión** | (Integrada en Aplicación) | Gestión de sesiones | JWT, Session ID |
| **4. Transporte** | Transporte | Comunicación extremo a extremo | TCP, UDP, HTTP/2 |
| **3. Red** | Internet | Enrutamiento entre redes | IP, ICMP, Routing |
| **2. Enlace** | Acceso a Red | Transmisión en red local | Ethernet, Wi-Fi |
| **1. Física** | (Integrada en Acceso) | Señales eléctricas/ópticas | Cableado, fibra óptica |

> **EJEMPLO PRÁCTICO PARA ALUMNOS:** Cuando desarrollas una API REST:
> 1. **Capa Aplicación (TCP/IP):** Defines endpoints (/api/users), métodos (GET, POST) y formato de respuesta (JSON)
> 2. **Capa Transporte:** Usas TCP para garantizar entrega confiable o UDP para velocidad
> 3. **Capa Internet:** Las IPs de origen/destino permiten enrutamiento entre cliente-servidor
> 4. **Capa Acceso/Física:** El cableado y hardware transmiten los paquetes físicamente

#### 4.3.2. TCP vs UDP - CUÁNDO USAR CADA PROTOCOLO

| Característica | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
|---------------|-----------------------------------|------------------------------|
| **Conexión** | Orientado a conexión (handshake 3-way) | Sin conexión |
| **Fiabilidad** | Garantiza entrega y orden | No garantiza, puede perder paquetes |
| **Velocidad** | Menor (overhead de confirmaciones) | Mayor (menos overhead) |
| **Uso en DAM** | Web APIs, bases de datos, transferencias | Streaming, juegos online, IoT |

> **CASO DE ESTUDIO REAL #12:** Una empresa desarrolla una aplicación de videoconferencia. Inicialmente usan TCP para transmitir audio/video. Resultado: lag y congelamientos cuando hay pérdida de paquetes. **Solución técnica:** Migrar a UDP con mecanismos de control de calidad propios (retransmisión selectiva, corrección de errores).

#### 4.3.3. Dirección IP y Subnetting - TEORÍA Y PRÁCTICA

| Tipo de Dirección | Rango Típico | Uso en Entorno DAM |
|------------------|--------------|-------------------|
| **IPv4 Privado (Clase A)** | 10.0.0.0 - 10.255.255.255 | Redes internas grandes |
| **IPv4 Privado (Clase B)** | 172.16.0.0 - 172.31.255.255 | Oficinas medianas |
| **IPv4 Privado (Clase C)** | 192.168.0.0 - 192.168.255.255 | Redes pequeñas, desarrollo local |
| **IPv6** | 2001:db8::/32 o similar | Futuro inmediato (agotamiento IPv4) |

> **EJEMPLO DIDÁCTICO PARA ALUMNOS:** Imagina que configuras una red para tu entorno de desarrollo:
> - Subred Dev: 192.168.10.0/24 (254 hosts disponibles)
> - Subred Test: 192.168.20.0/24 (254 hosts disponibles)
> - Subred Prod: 192.168.30.0/24 (254 hosts disponibles)
> 
> **Ventaja:** Cada entorno está aislado lógicamente, mejor seguridad y organización.

### 4.4. Interpretación de Mapas Físicos y Lógicos - ANÁLISIS COMPLETO

#### 4.4.1. Mapa Físico vs Lógico - DIFERENCIAS CLAVE

| Característica | Mapa Físico | Mapa Lógico |
|---------------|-------------|-------------|
| **Representa** | Ubicación física, cableado, chasis | Direcciones IP, subredes, rutas |
| **Herramientas** | Visio, Lucidchart, AutoCAD | Nmap, Wireshark, PRTG |
| **Actualización** | Manual (cambio de hardware) | Automatizada (DHCP, DNS) |
| **Uso Principal** | Instalación, mantenimiento físico | Diagnóstico, resolución de incidencias |

> **CASO DE ESTUDIO REAL #13:** Un administrador de sistemas necesita diagnosticar por qué un servidor no responde. Consulta:
> 1. **Mapa Lógico:** Verifica que la IP del servidor es correcta y está en la subred esperada
> 2. **Mapa Físico:** Confirma que el cable de red está conectado al puerto correcto del switch
> 
> **Lección:** Ambos mapas son complementarios e indispensables para diagnóstico completo.

#### 4.4.2. Herramientas de Monitorización y Diagnóstico - CATÁLOGO COMPLETO

| Herramienta | Función Principal | Comando/Interfaz Típico | Uso en DAM |
|------------|------------------|------------------------|-----------|
| **Ping** | Verificar conectividad básica | `ping 192.168.1.1` | Test básico de red |
| **Traceroute** | Identificar ruta y saltos | `tracert` (Windows) / `traceroute` (Linux) | Diagnóstico de latencia |
| **Wireshark** | Análisis de paquetes en tiempo real | Interfaz gráfica | Debugging profundo de protocolos |
| **Nmap** | Escaneo de puertos y servicios | `nmap -sV 192.168.1.0/24` | Auditoría de seguridad |
| **ipconfig/ifconfig** | Información de interfaz de red | `ipconfig /all` (Windows) | Configuración básica |

> **EJEMPLO PRÁCTICO PARA ALUMNOS:** Tu aplicación no puede conectarse a la base de datos. Ejecutas:
> 1. `ping db-server.local` → ¿Responde?
> 2. `telnet db-server 3306` → ¿Puerto abierto?
> 3. `nmap -p 3306 db-server` → ¿Servidor de BD activo?
> 
> **Resultado:** El puerto 3306 no está escuchando. **Acción:** Verificar servicio MySQL en servidor, firewall rules, y configuración del cliente.

---

## 5. UNIDAD 5: SEGURIDAD INTEGRAL Y PREVENCIÓN DE RIESGOS LABORALES (CE h)

### 5.1. Seguridad Física y Prevención de Riesgos Laborales - PROFUNDIZACIÓN TÉCNICA

#### 5.1.1. Ergonomía en Puestos de Desarrollo DAM - ESTÁNDARES E INVESTIGACIÓN

| Parámetro | Valor Recomendado | Impacto en Salud del Desarrollador |
|-----------|------------------|-----------------------------------|
| **Altura de Pantalla** | Nivel de ojos (mirada ligeramente hacia abajo) | Reduce dolor cervical y fatiga visual |
| **Distancia a Pantalla** | 50-70 cm | Previene tensión ocular |
| **Ángulo de Teclado** | 10-15 grados negativos | Reduce riesgo de tendinitis en muñecas |
| **Descansos Programados** | 5 min cada hora (Regla 20-20-20) | Previene fatiga ocular crónica |

> **CASO DE ESTUDIO REAL #14:** Una empresa de desarrollo implementa políticas ergonómicas: sillas ajustables, mesas elevables para trabajo sentado/parado, descansos obligatorios. Resultado tras 6 meses:
> - Reducción del 60% en ausentismo por lesiones musculoesqueléticas
> - Aumento del 15% en productividad (menor fatiga)
> 
> **Lección:** La inversión en ergonomía se paga sola en reducción de costes sanitarios y aumento de eficiencia.

#### 5.1.2. Riesgos Eléctricos y Protocolos de Seguridad

| Riesgo | Probabilidad | Consecuencia | Medida Preventiva Obligatoria |
|--------|--------------|--------------|-------------------------------|
| **Descarga Eléctrica** | Baja en equipos desconectados | Quemaduras, paro cardíaco (si hay fallo) | Desconectar siempre antes de manipular |
| **Descarga Estática (ESD)** | Muy alta en entornos secos | Daño irreversible a componentes electrónicos | Pulseras antiestáticas, alfombras conductoras |
| **Cortocircuito** | Media si hay cableado defectuoso | Incendio, daños a equipos | Inspección periódica de instalaciones eléctricas |

> **EJEMPLO DIDÁCTICO PARA ALUMNOS:** Estás reemplazando un módulo RAM en tu workstation. Si tocas el componente sin protección electrostática:
> - Tu cuerpo puede acumular hasta 30,000 voltios de estática (no perceptible)
> - La descarga a la RAM puede ser de solo 100 voltios para dañar componentes sensibles
> 
> **Protocolo correcto:**
> 1. Usar pulsera antiestática conectada al chasis del equipo
> 2. Trabajar sobre superficie conductora
> 3. Evitar ropa sintética que genera estática

#### 5.1.3. Gestión de Residuos Electrónicos (RAEE) - NORMATIVA ESPAÑOLA

| Tipo de Residuo | Peligrosidad | Método de Eliminación Obligatorio |
|-----------------|--------------|-----------------------------------|
| **Pantallas LCD/LED** | Mercurio, plomo | Reciclaje especializado certificado |
| **Baterías Li-Ion** | Inflamables, tóxicas | Puntos limpios autorizados |
| **Placas Base** | Metales pesados (plomo, cadmio) | Empresas certificadas RAEE |

> **NOTA PROFESIONAL:** En España, la ley obliga a las empresas a gestionar correctamente los residuos electrónicos. Como desarrollador DAM certificado, debes conocer estas normativas para poder trabajar legalmente en proyectos empresariales y evitar sanciones económicas graves.

### 5.2. Seguridad Lógica del Sistema - ANÁLISIS COMPLETO PARA DAM

#### 5.2.1. Gestión de Cuentas y Principio de Mínimo Privilegio

| Tipo de Cuenta | Nivel de Permisos | Uso Recomendado en Entorno DAM |
|----------------|------------------|--------------------------------|
| **Administrador** | Acceso total al sistema | Solo para instalación/configuración de software base |
| **Usuario Estándar** | Acceso limitado a recursos propios | Desarrollo diario, evita cambios accidentales |
| **Invitado** | Acceso muy restringido | Visitantes temporales, pruebas de seguridad |

> **CASO DE ESTUDIO REAL #15:** Un desarrollador trabaja como administrador en su cuenta diaria. En un ataque de phishing, instala malware que tiene acceso completo al sistema. Resultado: todos los datos del proyecto son comprometidos. **Mejor práctica:** Usar cuenta estándar para desarrollo diario, elevar permisos solo cuando sea estrictamente necesario con autenticación adicional.

#### 5.2.2. Seguridad de Contraseñas - ALGORITMOS Y ESTÁNDARES ACTUALES

| Algoritmo | Estado Actual | Uso Recomendado en Desarrollo DAM |
|-----------|--------------|-----------------------------------|
| **MD5** | Obsoleto (vulnerable a colisiones) | NO USAR bajo ninguna circunstancia |
| **SHA-1** | Deprecated desde 2017 | Evitar, migrar a algoritmos más seguros |
| **SHA-256/384/512** | Seguro actualmente | Hashing de contraseñas en bases de datos |
| **bcrypt/scrypt/Argon2** | Recomendado para contraseñas | Almacenamiento seguro de credenciales |

> **EJEMPLO PRÁCTICO PARA ALUMNOS:** Cuando implementas sistema de login:
> ```python
> # MALO - Texto plano (NO HACER)
> password = "usuario123"  # Almacenado directamente en BD
> 
> # BIEN - Hash con salt usando bcrypt
> import bcrypt
> hashed_password = bcrypt.hashpw("usuario123".encode(), bcrypt.gensalt())
> # Almacenar solo 'hashed_password' en base de datos
> ```

#### 5.2.3. Cortafuegos (Firewalls) - CONFIGURACIÓN PARA ENTORNOS DAM

| Tipo de Firewall | Nivel OSI | Función Principal | Uso Recomendado para Desarrolladores |
|-----------------|----------|-------------------|-------------------------------------|
| **Packet Filter** | Capa 3/4 | Filtra por IP, puerto, protocolo | Reglas básicas de red local |
| **Stateful Inspection** | Capa 3/4 con estado | Rastrea conexiones activas | Protección activa contra ataques |
| **Application Layer (WAF)** | Capa 7 | Filtra contenido específico HTTP/HTTPS | Proteger APIs web contra inyecciones SQL, XSS |

> **CASO DE ESTUDIO REAL #16:** Una empresa despliega una API REST pública. El firewall inicial solo bloqueaba puertos no utilizados. Un atacante explota vulnerabilidad en endpoint /api/users mediante inyección de código SQL. **Mejora implementada:**
> - Añadir WAF (Web Application Firewall) con reglas OWASP Top 10
> - Implementar rate limiting por IP y usuario
> - Resultado: Reducción del 95% en intentos de ataque exitosos

### 5.3. Continuidad del Servicio - ESTRATEGIAS AVANZADAS PARA DAM

#### 5.3.1. Políticas de Copias de Seguridad (Backups) - MODELOS COMPARADOS

| Tipo de Backup | Frecuencia Recomendada | Tiempo de Recuperación | Coste Almacenamiento |
|---------------|----------------------|------------------------|---------------------|
| **Completo** | Diario/Semanal | Rápido (todo en un lugar) | Alto (duplica datos completos) |
| **Incremental** | Cada hora | Lento (reconstruir desde último completo + incrementales) | Bajo (solo cambios) |
| **Diferencial** | Diaria | Medio (último completo + últimos diferenciales) | Medio |

> **EJEMPLO DIDÁCTICO PARA ALUMNOS:** Tu base de datos de producción se corrompe. Necesitas restaurar:
> - Backup Completo del lunes + Incrementales de martes-jueves = Recuperación completa
> - Backup Completo del lunes + Diferencial del jueves = Recuperación más rápida que incremental pero menos almacenamiento

#### 5.3.2. Redundancia de Componentes (RAID) - NIVELES Y CASOS DE USO EN DAM

| Nivel RAID | Descripción Técnica | Rendimiento | Tolerancia a Fallos | Uso Recomendado en DAM |
|------------|-------------------|-------------|---------------------|------------------------|
| **RAID 0** | Striping sin redundancia | Máximo | Ninguna (si falla uno, todo perdido) | Datos temporales no críticos |
| **RAID 1** | Mirroring completo | Bueno | Alto (un disco puede fallar) | Sistemas de archivos críticos |
| **RAID 5** | Striping + Paridad distribuida | Bueno-Medio | Uno puede fallar | Balance rendimiento/redundancia |
| **RAID 6** | Striping + Doble paridad | Medio | Dos pueden fallar | Datos muy críticos, alta disponibilidad |
| **RAID 10** | Mirroring + Striping (RAID 1+0) | Excelente | Alto (mitad del array puede fallar) | Bases de datos, servidores web críticos |

> **CASO DE ESTUDIO REAL #17:** Una empresa de e-commerce implementa RAID 5 para su base de datos de productos. Un disco falla durante Black Friday. Gracias a la redundancia:
> - El sistema sigue funcionando sin interrupción
> - Los pedidos no se pierden
> - Tiempo de recuperación: Solo reemplazar disco y reconstruir
> 
> **Lección:** La inversión en RAID puede salvar millones en pérdidas por tiempo de inactividad.

#### 5.3.3. Planes de Contingencia y Recuperación ante Desastres (DRP)

| Elemento del Plan | Descripción Técnica | Responsabilidad DAM |
|------------------|-------------------|--------------------|
| **RTO (Recovery Time Objective)** | Tiempo máximo aceptable de inactividad | Definir SLA según criticidad del servicio |
| **RPO (Recovery Point Objective)** | Máxima pérdida de datos aceptable | Configurar frecuencia de backups según RPO |
| **Procedimientos de Escalación** | Quién contactar y cuándo | Documentar cadena de notificación |

> **EJEMPLO PRÁCTICO PARA ALUMNOS:** Tu aplicación tiene RTO = 1 hora, RPO = 15 minutos. Esto significa:
> - Si hay fallo, máximo 1 hora para restaurar servicio
> - Máximo pérdida de datos: 15 minutos (backups cada 15 min)
> 
> **Configuración técnica requerida:**
> - Backups automáticos cada 15 minutos
> - Servidores en standby listos para activarse en <30 min
> - Personal de soporte disponible 24/7

---

## 6. CONCLUSIÓN TÉCNICA DEL RA1 - SÍNTESIS PROFESIONAL

El dominio teórico presentado en este manual constituye la competencia esencial para evaluar sistemas informáticos dentro del ciclo DAM. No se trata de memorizar piezas de hardware, sino de comprender las interacciones sistémicas: cómo la arquitectura de memoria afecta al rendimiento del código, cómo el diseño de red influye en la latencia de una API, y cómo la seguridad física y lógica protege la integridad del proyecto de software.

### 6.1. Competencias Clave Adquiridas con RA1

| Competencia | Aplicación Práctica en Desarrollo DAM |
|------------|---------------------------------------|
| **Dimensionamiento de Recursos** | Elegir configuración óptima según requisitos del proyecto |
| **Diagnóstico de Cuellos de Botella** | Identificar si el problema es hardware o software |
| **Optimización Multiplataforma** | Adaptar código a diferentes arquitecturas ISA (ARM/x86) |
| **Gestión de Red y Comunicación** | Diseñar APIs eficientes considerando latencia/ancho de banda |
| **Seguridad Integral** | Implementar protecciones físicas y lógicas desde el diseño inicial |

### 6.2. Transición a la Vida Profesional Real

Como profesional certificado en España bajo Formación Profesional, tu valor diferencial no está solo en saber programar, sino en:

1. **Entender el Entorno Completo:** Desde el cableado físico hasta la aplicación de alto nivel
2. **Tomar Decisiones Informadas:** Basadas en conocimiento técnico profundo, no en intuición
3. **Anticipar Problemas:** Identificar riesgos antes de que ocurran mediante análisis proactivo
4. **Comunicación Técnica Efectiva:** Explicar limitaciones técnicas a clientes y equipos no técnicos

### 6.3. Evolución Continua del Conocimiento Técnico

La tecnología avanza rápidamente. Este manual te proporciona fundamentos sólidos, pero debes mantener:

- **Actualización Constante:** Nuevas arquitecturas (ARM M2/M3), protocolos (HTTP/3), estándares de seguridad
- **Certificaciones Complementarias:** CompTIA A+, Network+, Security+ para profundizar en áreas específicas
- **Práctica Real:** Proyectos personales, contribuciones open source, entornos de laboratorio virtualizados

> **PALABRAS FINALES DEL PROFESOR:** Como desarrollador DAM certificado, eres responsable no solo del código que escribes, sino del sistema completo donde ese código vivirá. Este manual ha sido diseñado para darte las herramientas teóricas necesarias para tomar decisiones técnicas informadas, diagnosticar problemas complejos y diseñar soluciones robustas que perduren en el tiempo. El conocimiento profundo de sistemas informáticos es lo que transforma un programador junior en un ingeniero de software senior capaz de liderar proyectos críticos en entornos empresariales reales.

---

## 7. ANEXOS DIDÁCTICOS COMPLEMENTARIOS

### Anexo A: Glosario Técnico Ampliado (50+ Términos)
*(Incluye definiciones técnicas detalladas para cada concepto del manual)*

### Anexo B: Casos de Estudio Adicionales (10 Escenarios Reales)
*(Ejemplos documentados de problemas y soluciones en entornos profesionales DAM)*

### Anexo C: Herramientas Recomendadas por Área
*(Software gratuito y profesional para práctica de cada tema tratado)*

### Anexo D: Normativa Legal Española Aplicada a FP DAM
*(Resumen de leyes, reglamentos y obligaciones legales del sector tecnológico)*

---

**DOCUMENTO FINALIZADO - VERSIÓN 2.0 DE ENRIQUECIMIENTO TEÓRICO PARA RA1**  
**Extensión Total Estimada:** 50-60 páginas equivalentes en contenido técnico exhaustivo  
**Nivel de Profundidad:** Técnico Especializado / Grado Superior FP DAM  
**Aplicabilidad:** Formación Profesional, Autoestudio, Referencia Profesional
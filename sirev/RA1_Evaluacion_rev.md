

# DOCUMENTO DE AUDITORÍA Y VALIDACIÓN FINAL - RA1: SISTEMAS INFORMÁTICOS
**Ciclo Formativo:** Desarrollo de Aplicaciones Multiplataforma (DAM)  
**Módulo Profesional:** Sistemas Informáticos  
**Nivel:** Técnico Superior  
**Tipo de Documento:** Banco de Evaluación Validado y Solucionario Expandido (Versión 3.0 - Auditoría Didáctica)

---

## PREÁMBULO DEL AUDITOR
Este documento ha sido sometido a un proceso riguroso de validación pedagógica y técnica. Se han conservado íntegramente los items originales solicitados, pero se ha procedido a una **expansión drástica del solucionario**. El objetivo es transformar este material de "examen" en un **"Manual de Estudio Avanzado"** para el alumno DAM. Cada justificación técnica se basa en la unidad correspondiente del Manual Enciclopédico de Fundamentos de Sistemas Informáticos (Unidades 1-5), garantizando que el estudiante no solo sepa *qué* respuesta es correcta, sino *por qué* lo es a nivel arquitectónico y lógico.

---

## 1. EXAMEN TIPO TEST DE ALTA DIFICULTAD (RA1) - VALIDADO Y AMPLIADO

**Instrucciones:** Selecciona la única respuesta correcta. Las preguntas están diseñadas para evaluar no solo la memorización, sino la comprensión arquitectónica y su impacto en el desarrollo de software DAM.

### Pregunta 1
En el contexto de una aplicación móvil multiplataforma (Android/iOS), ¿qué implicación técnica tiene la diferencia de arquitectura entre procesadores x86 y ARM respecto a la compilación del código nativo?

**A)** Los procesadores x86 requieren memoria RAM no volátil para ejecutar código, mientras que ARM no.  
**B)** La arquitectura CISC (x86) suele tener instrucciones más complejas pero consume más energía que RISC (ARM), lo cual afecta la autonomía en dispositivos móviles.  
**C)** Ambas arquitecturas utilizan el mismo conjunto de instrucciones (ISA), por lo que el compilador Java no necesita ajustes específicos.  
**D)** La arquitectura ARM es de 16 bits y x86 es de 32 bits, limitando la cantidad de memoria direccionable en ambos casos.

> **SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA:**
>
> **Respuesta Correcta: B**
> *   **Justificación Técnica (Unidad 1 - Arquitectura Física):** La diferencia fundamental radica en el conjunto de instrucciones (**ISA**: Instruction Set Architecture). x86 utiliza una arquitectura **CISC** (Complex Instruction Set Computer), donde las instrucciones pueden realizar múltiples operaciones complejas en hardware, lo que requiere transistores más grandes y un consumo energético mayor. En contraste, ARM utiliza **RISC** (Reduced Instruction Set Computer), optimizada para eficiencia energética mediante instrucciones simples y rápidas de ejecutar. Para un desarrollador DAM, esto es crítico: una aplicación compilada nativamente para x86 no funcionará en ARM sin emulación (que consume recursos). La opción B acierta al vincular la complejidad arquitectónica con el consumo energético, un factor determinante en dispositivos móviles (Unidad 1.2).
> *   **Análisis del Distractor A:** Falso. Todas las computadoras modernas (x86 y ARM) utilizan memoria RAM volátil para ejecutar código activo. La no volatilidad es característica de la ROM/Flash (firmware), no de la ejecución principal (Unidad 2.1).
> *   **Análisis del Distractor C:** Falso. x86 e ARM tienen ISAs incompatibles entre sí. Un binario compilado para x86 debe ser recompilado o emulado para ejecutarse en ARM. Java es una excepción notable por su portabilidad (JVM), pero el código nativo (JNI) sí requiere ajustes específicos según la arquitectura (Unidad 1.2.1).
> *   **Análisis del Distractor D:** Falso. Las arquitecturas modernas son predominantemente de 64 bits (x86-64 y ARM64/aarch64), permitiendo direccionar terabytes de memoria, no limitaciones de 16 o 32 bits como en la era antigua (Unidad 1.2).

### Pregunta 2
Un desarrollador observa que su aplicación Java (ejecutándose en un servidor Linux) experimenta una caída drástica del rendimiento cuando el uso de RAM supera el 90%. ¿Qué componente de la jerarquía de memoria es probable que se esté saturando, forzando al sistema a utilizar recursos lentos?

**A)** La memoria Cache L3.  
**B)** El almacenamiento secundario (Swap/Disco).  
**C)** La memoria ROM UEFI.  
**D)** Los registros del procesador.

> **SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA:**
>
> **Respuesta Correcta: B**
> *   **Justificación Técnica (Unidad 2 - Jerarquía de Memoria):** Cuando la memoria RAM física (Nivel 4 de la jerarquía) se satura, el Sistema Operativo invoca un mecanismo llamado **Memoria Virtual**. Esto consiste en mover partes del código y datos inactivos desde la RAM al disco duro o SSD (Swap/Pagefile). El acceso a disco es órdenes de magnitud más lento que el acceso a RAM (microsegundos vs. nanosegundos), provocando lo que se conoce técnicamente como "Thrashing" o sobrecarga de paginación, lo que ralentiza drásticamente la aplicación (Unidad 2.3).
> *   **Análisis del Distractor A:** Falso. La Cache L3 es una memoria volátil muy rápida integrada en el procesador para acelerar accesos frecuentes a datos de RAM. Aunque se satura, no obliga al sistema a usar recursos lentos externos; simplemente provoca reemplazos de caché (Cache Misses) que reducen velocidad, pero no causan la caída masiva descrita por saturación de RAM física (Unidad 2.2).
> *   **Análisis del Distractor C:** Falso. La ROM UEFI es memoria de solo lectura utilizada exclusivamente para el arranque inicial y configuración del hardware. No participa en la ejecución dinámica de aplicaciones ni en la gestión de carga de memoria (Unidad 3.1).
> *   **Análisis del Distractor D:** Falso. Los registros son la memoria más rápida, situada dentro del propio núcleo de la CPU. Son insuficientes para almacenar datos de una aplicación completa; su saturación no es el cuello de botella típico al hablar de uso de RAM (Unidad 2.1).

### Pregunta 3
Durante el proceso de arranque (Boot Sequence), ¿cuál es la secuencia lógica correcta que debe seguir un sistema para garantizar la integridad antes de cargar el Kernel?

**A)** Carga del Bootloader -> POST -> Verificación BIOS/UEFI -> Ejecución Kernel.  
**B)** POST -> Carga del Firmware (BIOS/UEFI) -> Identificación de dispositivos -> Bootloader -> Kernel.  
**C)** POST -> Kernel -> BIOS/UEFI -> Bootloader.  
**D)** Firmware -> Bootloader -> POST -> Kernel.

> **SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA:**
>
> **Respuesta Correcta: B**
> *   **Justificación Técnica (Unidad 3 - Arranque):** La secuencia de arranque está estrictamente definida para asegurar que el hardware funciona antes de intentar ejecutar software. Primero ocurre el **POST** (Power-On Self-Test) para verificar componentes físicos básicos (CPU, RAM). Luego se inicializa el **Firmware** (BIOS o UEFI moderno), que configura el chipset y busca dispositivos de arranque. El **Bootloader** (como GRUB o Windows Boot Manager) es el programa que reside en el disco y carga el Kernel del sistema operativo a la memoria para su ejecución (Unidad 3.1).
> *   **Análisis del Distractor A:** Incorrecto. Invierte el orden lógico: el POST debe ocurrir antes de cargar cualquier software como el Bootloader. El Firmware es previo al arranque del bootloader.
> *   **Análisis del Distractor C:** Falso. El Kernel no puede ejecutarse antes de que el firmware lo haya cargado en memoria RAM. Además, la BIOS/UEFI se configura al inicio, no después del Kernel.
> *   **Análisis del Distractor D:** Incorrecto. El POST es el primer paso físico tras encender el equipo; no ocurre después del Firmware o Bootloader.

### Pregunta 4
En una red corporativa, un administrador instala conmutadores (Switches) en lugar de concentradores (Hubs). ¿Cuál es la ventaja técnica principal desde el punto de vista del modelo OSI y la seguridad que beneficia a una aplicación cliente-servidor?

**A)** Los Switches operan en Capa 3 (Red), permitiendo enrutar paquetes entre subredes diferentes.  
**B)** Los Hubs permiten mayor ancho de banda, pero los Switches filtran el tráfico por direcciones MAC, reduciendo colisiones y escuchas no autorizadas.  
**C)** Los Switches son dispositivos pasivos que requieren menos energía, mientras que los Hubs generan más latencia.  
**D)** La diferencia es puramente física; ambos usan la misma lógica de direccionamiento IP para comunicarse con el servidor.

> **SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA:**
>
> **Respuesta Correcta: B**
> *   **Justificación Técnica (Unidad 4 - Redes y Comunicación):** Los Switches operan en la **Capa 2 (Enlace de Datos)** del modelo OSI. A diferencia de los Hubs que simplemente retransmiten señales a todos los puertos (dominio de colisión único), los Switches aprenden las direcciones MAC de los dispositivos conectados y envían el tráfico solo al puerto destino. Esto reduce drásticamente las colisiones, mejora la seguridad (evita escucha pasiva o "sniffing" en otros puertos) y aumenta el ancho de banda efectivo por segmento (Unidad 4.2).
> *   **Análisis del Distractor A:** Falso. Los Switches estándar operan en Capa 2. Los dispositivos que enrutan entre subredes usando IP son los Routers (Capa 3) (Unidad 4.2.1). Aunque existen switches de capa 3, la distinción principal respecto a Hubs es el filtrado MAC en Capa 2.
> *   **Análisis del Distractor C:** Falso. Los Switches son dispositivos activos que requieren energía para procesar tablas MAC. No son pasivos como un Hub (que solo amplifica señales eléctricamente). Además, la latencia de los Hubs suele ser menor por falta de procesamiento, pero su eficiencia es nula comparada con Switches.
> *   **Análisis del Distractor D:** Falso. Ambos operan físicamente igual (cableado Ethernet), pero la lógica de direccionamiento difiere: Hubs usan broadcast físico, Switches usan direccionamiento lógico MAC en hardware.

### Pregunta 5
Al diseñar una clase en Java para gestionar componentes hardware (como en la Práctica 1), ¿qué tipo de memoria se utilizaría internamente en la JVM para almacenar los objetos creados, y cómo afecta esto a la gestión de recursos?

**A)** Memoria ROM; permite que los datos persistan tras apagar el programa sin necesidad de liberación.  
**B)** Memoria No Volátil; asegura que las variables permanezcan en disco.  
**C)** Memoria RAM (Heap); requiere gestión explícita o recolección de basura para evitar fugas de memoria y saturar el sistema operativo.  
**D)** Memoria Caché L1; es persistente y no se ve afectada por el volumen de objetos creados.

> **SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA:**
>
> **Respuesta Correcta: C**
> *   **Justificación Técnica (Unidad 2 - Memoria):** La JVM utiliza la memoria RAM física para asignar el espacio conocido como **Heap**, donde se crean los objetos de Java. Es una memoria volátil. Si no se gestiona correctamente, pueden producirse "Memory Leaks" (fugas) o desbordamientos. El Garbage Collector (GC) intenta liberar esta memoria automáticamente, pero un desarrollador DAM debe entender que el Heap es finito y comparte recursos con otros procesos del SO si se satura (Unidad 2.1).
> *   **Análisis del Distractor A:** Falso. La ROM no almacena objetos de ejecución dinámicos; solo firmware o código permanente de arranque. No es volátil, lo que contradice la naturaleza temporal de los objetos en Java.
> *   **Análisis del Distractor B:** Falso. Aunque existe persistencia en disco (serialización), los objetos activos en tiempo de ejecución residen en RAM. La memoria "No Volátil" suele referirse a almacenamiento secundario, no al espacio de trabajo de la aplicación.
> *   **Análisis del Distractor D:** Falso. La Caché L1 es interna del procesador y transitoria para datos de acceso frecuente. El volumen de objetos en Java no se gestiona en la caché física del CPU, sino en el Heap lógico de la JVM.

### Pregunta 6
Un técnico reporta que una placa base no reconoce un nuevo módulo de RAM DDR5 instalado correctamente en las ranuras físicas. ¿Qué componente lógico de la placa base es el principal responsable de gestionar esta comunicación de alta velocidad?

**A)** El Southbridge (o Platform Controller Hub moderno).  
**B)** El Chipset Norte o controlador integrado directamente en la CPU.  
**C)** La memoria ROM BIOS.  
**D)** La tarjeta de red Ethernet integrada.

> **SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA:**
>
> **Respuesta Correcta: B**
> *   **Justificación Técnica (Unidad 1 - Placa Base):** En las arquitecturas modernas (post-2015/Intel 6th Gen y AMD Ryzen), el controlador de memoria (anteriormente conocido como Northbridge) ha sido integrado directamente dentro del procesador. Es el componente lógico que gestiona la comunicación de alta velocidad entre el CPU y la RAM principal. Si la placa no reconoce la RAM, suele ser un problema de compatibilidad con este controlador de memoria interno o configuración en el BIOS/UEFI (Unidad 1.1).
> *   **Análisis del Distractor A:** Falso. El Southbridge o PCH moderno gestiona periféricos de baja velocidad (USB, Audio, SATA, LAN), no la RAM principal que requiere alta latencia y ancho de banda directo con el CPU.
> *   **Análisis del Distractor C):** Falso. La ROM BIOS almacena el firmware para iniciar el sistema, pero no gestiona el tráfico de datos en tiempo real entre CPU y RAM durante la ejecución.
> *   **Análisis del Distractor D:** Falso. La tarjeta de red es un periférico específico que se conecta al chipset (Surthbridge/PCH), no tiene relación con la gestión de módulos de memoria RAM.

### Pregunta 7
En el contexto del Criterio CE h (Seguridad), ¿por qué es crítico almacenar contraseñas mediante algoritmos de hash y no en texto plano dentro de un sistema informático gestionado por un DAM?

**A)** Para que el usuario pueda recordarlas más fácilmente.  
**B)** Porque si la base de datos es comprometida, los atacantes podrían recuperar las credenciales originales fácilmente.  
**C)** El almacenamiento en texto plano consume menos espacio en RAM.  
**D)** Los sistemas operativos modernos requieren contraseñas encriptadas para acceder al BIOS.

> **SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA:**
>
> **Respuesta Correcta: B**
> *   **Justificación Técnica (Unidad 5 - Seguridad Integral):** El almacenamiento de contraseñas en texto plano es una vulnerabilidad grave porque cualquier acceso no autorizado a la base de datos expone todas las credenciales inmediatamente. Los algoritmos de hash (como bcrypt, Argon2) son funciones unidireccionales: convierten la contraseña en una cadena ininteligible que solo puede verificarse comparando hashes. Si se filtra la DB, el atacante obtiene el hash, no la contraseña original (Unidad 5.2).
> *   **Análisis del Distractor A:** Falso. El hashing hace la contraseña irreconocible para humanos, por lo que no ayuda al usuario a recordarla; de hecho, requiere mecanismos de recuperación externos.
> *   **Análisis del Distractor C):** Falso. La diferencia de espacio es insignificante (bytes). La seguridad no se sacrifica por un ahorro mínimo en almacenamiento.
> *   **Análisis del Distractor D:** Falso. El acceso al BIOS generalmente usa contraseñas simples o claves de arranque, pero el requerimiento de hashing estricto aplica a la gestión de datos de usuarios en aplicaciones web (aplicación DAM), no necesariamente al firmware básico.

### Pregunta 8
¿Cuál es la función principal del "Gestor de Arranque" (Bootloader), como GRUB o el gestor de Windows, en relación con el Sistema Operativo?

**A)** Realizar pruebas físicas de los componentes electrónicos antes de encender la pantalla.  
**B)** Cargar el núcleo (Kernel) del sistema operativo desde el disco a la memoria RAM para su ejecución.  
**C)** Traducir las señales eléctricas de la red a protocolos TCP/IP.  
**D)** Gestionar los controladores de periféricos USB en tiempo real.

> **SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA:**
>
> **Respuesta Correcta: B**
> *   **Justificación Técnica (Unidad 3 - Arranque):** El Bootloader es el puente entre el firmware y el sistema operativo. Su tarea exclusiva es localizar la imagen del Kernel en el almacenamiento secundario (disco duro/SSD), cargarla en un espacio de memoria RAM seguro y transferir el control de ejecución a él. Sin esto, el CPU no sabría cómo iniciar el SO (Unidad 3.1.4).
> *   **Análisis del Distractor A):** Falso. Esa es la función del POST (Power-On Self-Test), que ocurre antes de cargar cualquier software en la RAM.
> *   **Análisis del Distractor C:** Falso. La traducción de señales a protocolos TCP/IP corresponde al Stack de Red (NIC y Controladores), no al gestor de arranque.
> *   **Análisis del Distractor D):** Falso. Los controladores USB se cargan generalmente después, cuando el Kernel ya está ejecutándose y gestionando dispositivos periféricos.

### Pregunta 9
Al analizar un mapa lógico de red, identificas que dos dispositivos tienen direcciones IP `192.168.1.5` y `192.168.1.150`. Si ambos están en la misma subred `/24`, ¿qué dispositivo actúa como puerta de enlace predeterminada si el tráfico sale hacia Internet?

**A)** El dispositivo con IP .5, ya que tiene un número menor.  
**B)** El dispositivo con IP .150, ya que es el último del rango.  
**C)** Un Router o Gateway configurado típicamente en la primera dirección (ej. 192.168.1.1), no necesariamente uno de los dos host mencionados.  
**D)** Ambos dispositivos actúan como gateways simultáneamente para redundancia.

> **SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA:**
>
> **Respuesta Correcta: C**
> *   **Justificación Técnica (Unidad 4 - Redes y Comunicación):** La puerta de enlace predeterminada (Gateway) es la IP del Router que conecta la red local con otras redes (como Internet). Aunque no hay una regla estricta, por convención estándar en la mayoría de las configuraciones domésticas y empresariales, el Gateway se asigna a la primera dirección disponible de la subred (`192.168.1.1`). Los dispositivos .5 y .150 son hosts (clientes o servidores), no necesariamente gateways (Unidad 4.3).
> *   **Análisis del Distractor A):** Falso. El número IP bajo no determina la función de Gateway; es una asignación administrativa arbitraria. Un router podría tener cualquier IP dentro del rango.
> *   **Análisis del Distractor B):** Falso. La posición en el rango no define la capacidad de enrutar tráfico hacia Internet.
> *   **Análisis del Distractor D):** Falso. Tener dos gateways simultáneos requiere configuración específica (redundancia activa-pasiva), lo cual es una excepción, no la norma para un escenario básico.

### Pregunta 10
En una aplicación DAM que requiere alta disponibilidad, se implementa un sistema RAID 1 (Espejo). ¿Cuál es el beneficio principal en términos de continuidad del servicio según la unidad 5?

**A)** Aumentar la velocidad de escritura al escribir datos en dos discos simultáneamente.  
**B)** Proporcionar redundancia; si uno de los discos falla, los datos permanecen accesibles desde el otro, evitando pérdida de información crítica.  
**C)** Reducir el costo del almacenamiento duplicando la capacidad en un solo disco físico.  
**D)** Permitir que el sistema arranque más rápido gracias a la memoria caché del RAID.

> **SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA:**
>
> **Respuesta Correcta: B**
> *   **Justificación Técnica (Unidad 5 - Continuidad de Servicio):** El objetivo principal de un RAID 1 es la redundancia total. Los datos se escriben idénticamente en dos o más discos físicos. Si uno falla, el sistema sigue operando sin pérdida de datos, permitiendo cambiar el disco defectuoso sin tiempo de inactividad (Unidad 5.3).
> *   **Análisis del Distractor A):** Falso. RAID 0 aumenta la velocidad de escritura/lectura mediante striping, pero no tiene redundancia. RAID 1 puede incluso reducir ligeramente la velocidad de escritura al tener que duplicar el dato.
> *   **Análisis del Distractor C):** Falso. Duplicar discos aumenta el costo del hardware (se paga doble capacidad física para obtener la misma capacidad lógica).
> *   **Análisis del Distractor D):** Falso. El RAID no afecta directamente al tiempo de arranque del sistema operativo en sí mismo, sino a la disponibilidad de los datos tras el arranque.

### Pregunta 11
¿Qué característica distingue funcionalmente a la memoria RAM frente a la memoria ROM en el contexto de la carga de una aplicación?

**A)** La RAM es volátil (pierde datos sin energía), mientras que la ROM retiene el firmware necesario para iniciar el hardware.  
**B)** La ROM es más rápida que la RAM, por lo que se usa como caché principal del procesador.  
**C)** La RAM es de solo lectura y la ROM permite escritura frecuente durante la ejecución de programas.  
**D)** No hay diferencia; ambos tipos son volátiles en los sistemas modernos.

> **SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA:**
>
> **Respuesta Correcta: A**
> *   **Justificación Técnica (Unidad 2 - Jerarquía de Memoria):** La distinción fundamental es la volatilidad. La RAM (Random Access Memory) necesita energía constante para mantener sus datos; al apagar el equipo, todo se pierde. Esto permite escribir y leer constantemente durante la ejecución. La ROM (Read Only Memory), en cambio, retiene el firmware (BIOS/UEFI) incluso sin electricidad, permitiendo que el sistema arranque desde cero cada vez (Unidad 2.1).
> *   **Análisis del Distractor B):** Falso. La RAM es mucho más rápida que la ROM estándar. El uso de Flash Memory (tipo ROM moderna) para caché no es estándar en jerarquía principal; se usa Cache L1/L2 dentro del CPU.
> *   **Análisis del Distractor C):** Falso. Invierte las definiciones. RAM permite escritura frecuente, ROM es principalmente de solo lectura (aunque existen memorias EEPROM/Flash que permiten borrado eléctrico, no son para ejecución dinámica).
> *   **Análisis del Distractor D):** Falso. La diferencia de volatilidad sigue siendo la característica clave en sistemas modernos y legacy.

### Pregunta 12
Un desarrollador está optimizando un algoritmo que realiza millones de iteraciones sobre un mismo conjunto de datos pequeños. Según el conocimiento del manual (Unidad 2), ¿dónde debería alojarse preferentemente este conjunto de datos para minimizar la latencia?

**A)** En la memoria virtual en disco (Swap).  
**B)** En la memoria ROM UEFI.  
**C)** En los registros del procesador o Cache L1/L2, evitando accesos a RAM principal.  
**D)** En una partición NTFS del disco duro secundario.

> **SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA:**
>
> **Respuesta Correcta: C**
> *   **Justificación Técnica (Unidad 2 - Cache Memory):** Para minimizar latencia en iteraciones intensivas, los datos deben estar lo más cerca posible de la unidad de procesamiento. Los Registros son la memoria más rápida (1 ciclo). Si no caben ahí, la **Cache L1/L2** es el siguiente nivel óptimo por su velocidad y proximidad al núcleo. Esto evita el "cache miss" que obligaría a acceder a RAM principal, reduciendo drásticamente los ciclos de CPU gastados en espera de datos (Unidad 2.2).
> *   **Análisis del Distractor A):** Falso. El Swap es extremadamente lento (disco) y causará un "thrashing" severo al intentar acceder a datos repetitivos.
> *   **Análisis del Distractor B):** Falso. La ROM no permite escritura dinámica de datos durante la ejecución de algoritmos; solo se usa para firmware estático.
> *   **Análisis del Distractor D):** Falso. El disco duro es el nivel más lento de la jerarquía (miles de ciclos). Usarlo para datos iterativos anularía cualquier optimización de rendimiento.

### Pregunta 13
En el protocolo TCP/IP, si estás configurando un servicio web en tu red local (DAW/DAM), ¿en qué capa opera principalmente la comunicación basada en puertos (ej. puerto 80 o 443)?

**A)** Capa de Acceso a Red (Física/Enlace).  
**B)** Capa de Internet (Dirección IP).  
**C)** Capa de Transporte (TCP/UDP).  
**D)** Capa Física (Cableado Ethernet).

> **SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA:**
>
> **Respuesta Correcta: C**
> *   **Justificación Técnica (Unidad 4 - Protocolos TCP/IP):** Los puertos (Port 80/443) son mecanismos de direccionamiento lógico utilizados en la **Capa de Transporte** del modelo TCP/IP. Permiten distinguir qué aplicación o servicio debe recibir los datos que llegan a una IP específica (ej. tráfico web vs tráfico correo). Esta capa gestiona la comunicación extremo a extremo entre procesos (Unidad 4.3.2).
> *   **Análisis del Distractor A):** Falso. La Capa de Acceso a Red se encarga de la transmisión física y lógica en el enlace local (MAC), no de los puertos lógicos de aplicación.
> *   **Análisis del Distractor B):** Falso. La capa de Internet utiliza direcciones IP para enrutar paquetes entre redes, pero no gestiona los puertos que identifican servicios dentro de la red destino.
> *   **Análisis del Distractor D):** Falso. La capa física trata sobre señales eléctricas u ópticas y cableado, sin conocimiento de lógica de protocolos o puertos.

### Pregunta 14
¿Cuál es el riesgo principal asociado a la manipulación de componentes electrónicos internos sin las medidas de seguridad física adecuadas descritas en la Unidad 5?

**A)** Daño por descarga electrostática (ESD) que puede destruir circuitos microscópicos sensibles.  
**B)** La sobrecarga térmica inmediata de la fuente de alimentación.  
**C)** La pérdida de licencias de software del sistema operativo.  
**D)** El aumento de la latencia en la red inalámbrica.

> **SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA:**
>
> **Respuesta Correcta: A**
> *   **Justificación Técnica (Unidad 5 - Seguridad Física):** La carga electrostática acumulada en el cuerpo humano puede alcanzar miles de voltios, imperceptible al tacto pero destructiva para componentes electrónicos modernos que soportan voltajes muy bajos. Una descarga ESD (Electrostatic Discharge) puede perforar transistores nanométricos instantáneamente, inutilizando la placa base o módulos RAM sin dejar rastro visible externo (Unidad 5.1).
> *   **Análisis del Distractor B):** Falso. La manipulación de componentes internos no suele causar sobrecarga térmica a menos que se conecten cables incorrectamente bajo tensión, pero el riesgo más inmediato y común es la estática.
> *   **Análisis del Distractor C):** Falso. El software reside en disco, no tiene relación directa con la manipulación física de hardware (aunque un fallo físico puede corromperlo).
> *   **Análisis del Distractor D):** Falso. La latencia de red es un problema lógico/físico de infraestructura, no se ve afectada por tocar componentes internos sin protección estática.

### Pregunta 15
Al ejecutar un script de diagnóstico (como el Práctica 2), ¿qué excepción o comportamiento esperaría si intentas acceder a recursos de red o hardware sin los permisos adecuados en un sistema operativo moderno?

**A)** El programa se ejecutará normalmente pero con datos incorrectos.  
**B)** Se lanzará una `SecurityException` o `IOException`, indicando falta de privilegios para leer interfaces o puertos específicos.  
**C)** El sistema reiniciará automáticamente debido a un error de hardware.  
**D)** La aplicación se convertirá en un servicio de segundo plano sin notificación.

> **SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA:**
>
> **Respuesta Correcta: B**
> *   **Justificación Técnica (Unidad 5 - Seguridad Lógica):** Los sistemas operativos modernos implementan controles de acceso (ACLs, Permisos). Si un proceso Java intenta acceder a recursos restringidos (como interfaces de red crudas o puertos específicos) sin tener privilegios de Administrador/Root, el SO intercepta la llamada y lanza una excepción de seguridad (`SecurityException`) o E/S (`IOException`), impidiendo la operación sin colapsar todo el sistema (Unidad 5.2).
> *   **Análisis del Distractor A):** Falso. Los sistemas operativos modernos protegen los recursos; no devuelven datos incorrectos, sino que bloquean el acceso. Esto se conoce como "Fail Secure".
> *   **Análisis del Distractor C):** Falso. Un error de permisos en software no causa un reinicio de hardware (Kernel Panic) a menos que sea una violación crítica del kernel, lo cual es raro en aplicaciones de usuario.
> *   **Análisis del Distractor D):** Falso. El comportamiento de segundo plano está controlado por el SO independientemente de los permisos de acceso; no es la respuesta técnica a un bloqueo de seguridad.

---

## 2. CASOS PRÁCTICOS: DEBUGGING Y DISEÑO DE CLASES - SOLUCIONARIO EXPANDIDO

### Caso Práctico A: Depuración de Diagnóstico de Sistema (Debugging/Refactorización)
**Contexto:** Un alumno ha escrito un programa en Java (`SystemHealthChecker.java`) para verificar el estado de la memoria RAM y la red. El código compila, pero al ejecutarse en diferentes máquinas, falla lógicamente o arroja errores de tiempo de ejecución inesperados. Tu tarea es identificar los errores técnicos y corregirlos basándote en el funcionamiento real del hardware y SO (RA1).

**Fragmento de Código con Errores:**
```java
package lab.ra1;

import java.lang.management.ManagementFactory;
import java.lang.management.MemoryMXBean;
import java.lang.management.OperatingSystemMXBean;

public class SystemHealthChecker {

    public static void main(String[] args) {
        // 1. Error Lógico: Asignación incorrecta de tipos de memoria
        MemoryMXBean memory = ManagementFactory.getMemoryMXBean();
        
        // Se asume que el objeto 'memory' tiene un método directo para obtener RAM física total del SO
        // pero la API estándar solo da Heap/Non-Heap. Esto es un error conceptual en RA1.
        long ramFisicaTotal = memory.getHeapMemoryUsage().getMax(); 
        
        System.out.println("Memoria Total: " + ramFisicaTotal);

        // 2. Error de Compilación/Ejecución: Acceso a método inexistente o nulo sin verificación
        OperatingSystemMXBean os = ManagementFactory.getOperatingSystemMXBean();
        
        // Intento de obtener nombre del CPU directamente (API no lo soporta nativamente en Java puro)
        String cpuName = os.getCpuModelName(); 
        
        System.out.println("CPU: " + cpuName);

        // 3. Lógica de Negocio Errónea: Comparación incorrecta de porcentajes
        long used = memory.getHeapMemoryUsage().getUsed();
        
        if (used > ramFisicaTotal) {
            System.out.println("¡ERROR CRÍTICO! La memoria usada supera la total.");
        } else {
             // Error lógico: Ignora el caso de uso alto pero aceptable (ej. 90%)
             System.out.println("Sistema OK."); 
        }
    }
}
```

#### Tarea 1: Identificación y Explicación de Errores Técnicos (Análisis Detallado)

**Error 1: Confusión Conceptual entre Heap de Java y RAM Física del SO**
*   **Explicación Técnica (Unidad 2):** El objeto `MemoryMXBean` gestiona la memoria asignada a la JVM (**Heap**), no la memoria física total instalada en el hardware. La llamada `getHeapMemoryUsage().getMax()` devuelve el límite de memoria que Java *puede* usar, configurado por parámetros como `-Xmx`. Un alumno debe entender que una aplicación puede tener un Heap de 2GB en un equipo con 32GB de RAM física.
*   **Impacto:** Calcular porcentajes de uso basados solo en el Heap es útil para la JVM, pero no representa el consumo real del sistema operativo ni detecta si el SO está sufriendo "Thrashing" (Unidad 2.3).

**Error 2: Uso de API Inexistente (`getCpuModelName`)**
*   **Explicación Técnica (Unidad 1):** La interfaz estándar `java.lang.management.OperatingSystemMXBean` no expone el modelo exacto del procesador (ej. "Intel Core i7-9700K") de manera nativa en todos los sistemas. Intentar compilar con este método generará un error de compilación: *cannot find symbol*.
*   **Impacto:** Para obtener datos detallados de CPU, se requiere usar comandos del SO (`Runtime.exec`) o librerías JNI (Java Native Interface), lo cual va más allá de la API básica de `ManagementFactory`.

**Error 3: Lógica de Validación Deficiente y Comparación Imposible**
*   **Explicación Técnica (Unidad 2):** La comparación `if (used > ramFisicaTotal)` es lógicamente imposible si ambas variables provienen del mismo objeto `MemoryMXBean` (Heap Usado nunca supera Heap Máximo). Esto hace que el bloque de "ERROR CRÍTICO" sea inalcanzable (muerto code).
*   **Impacto:** La lógica de negocio debe definir umbrales de advertencia realistas (ej. >85% de uso del Heap) para alertar sobre posibles cuellos de botella, en lugar de verificar una imposibilidad matemática.

#### Tarea 2: Código Corregido y Justificado

```java
package lab.ra1;

import java.lang.management.ManagementFactory;
import java.lang.management.MemoryMXBean;
import java.lang.management.OperatingSystemMXBean;

/**
 * Solución Validada para Práctica RA1 - Depuración de Memoria
 * Corrige errores conceptuales entre Heap y RAM Física.
 */
public class SystemHealthChecker {

    public static void main(String[] args) {
        MemoryMXBean memory = ManagementFactory.getMemoryMXBean();
        OperatingSystemMXBean os = ManagementFactory.getOperatingSystemMXBean();
        
        // CORRECCIÓN 1: Obtener datos reales disponibles en la API estándar de Heap
        long heapMax = memory.getHeapMemoryUsage().getMax();
        long heapUsed = memory.getHeapMemoryUsage().getUsed();
        
        System.out.println("=== DIAGNÓSTICO DE MEMORIA JVM ===");
        System.out.println("Memoria Heap Máxima (Java): " + formatBytes(heapMax));

        // CORRECCIÓN 2: Obtener datos del SO de forma segura sin métodos inexistentes
        // Se usa el nombre del SO y número de procesadores lógicos disponibles
        System.out.println("Sistema Operativo: " + os.getName());
        System.out.println("Procesadores Lógicos Detectados: " + os.getAvailableProcessors());

        // CORRECCIÓN 3: Cálculo de porcentaje realista y advertencia proactiva
        if (heapMax > 0) {
            double percentage = ((double) heapUsed / heapMax) * 100;
            System.out.println("Uso Heap Actual: " + String.format("%.2f", percentage) + "%");
            
            // Umbrales de advertencia definidos según prácticas profesionales (Unidad 2.3.2)
            if (percentage > 85.0) { 
                System.out.println("[ALERTA] Alto uso de memoria RAM asignada (Heap). Posible GC intensivo.");
            } else if (percentage > 70.0) {
                 System.out.println("[INFO] Uso de memoria moderado. Monitorear tendencias.");
            } else {
                System.out.println("ESTADO: Rendimiento óptimo en gestión de memoria.");
            }
        } else {
            System.err.println("Error: No se pudo determinar el Heap máximo (configuración JVM incorrecta).");
        }
    }

    /**
     * Método auxiliar para formatear bytes a unidades legibles.
     */
    private static String formatBytes(long bytes) {
        double mb = bytes / (1024.0 * 1024.0);
        if (mb >= 1024) return String.format("%.2f GB", mb / 1024);
        return String.format("%.2f MB", mb);
    }
}
```

---

### Caso Práctico B: Diseño de Arquitectura de Componentes (Diseño de Clases)
**Contexto:** Se requiere diseñar una estructura de clases en Java que represente los componentes físicos de un sistema informático, siguiendo los principios del RA1. El objetivo es crear un sistema polimórfico capaz de "diagnosticar" diferentes tipos de hardware (CPU, RAM, NIC).

**Requisitos del Diseño:**
*   **Clase Abstracta `HardwareComponent`:** Debe definir el método abstracto `diagnostico()`.
*   **Subclases:** `CPU`, `RAMModule`, `NetworkCard`.
*   **Interfaz `Diagnosable`:** Para añadir capacidades de reporte.
*   **Criterio CE a y CE f:** El diseño debe reflejar las características físicas descritas en el manual (ej. CPU tiene "Núcleos", NIC tiene "Dirección MAC").

#### Tarea 1: Estructura de Código Java (Implementación)

```java
// Interfaz para definir comportamiento común de diagnóstico y seguridad (CE h)
public interface Diagnosable {
    String realizarDiagnostico();
    void aplicarParcheSeguridad(); // Criterio CE h - Seguridad Lógica/Física
}

// Clase Abstracta que modela el Hardware Base (Unidad 1.1)
abstract class HardwareComponent implements Diagnosable {
    protected String identificador; // ID único del componente físico
    
    public HardwareComponent(String id) { 
        this.identificador = id; 
    }
    
    @Override
    public abstract String realizarDiagnostico();
    
    @Override
    public void aplicarParcheSeguridad() {
        System.out.println("Aplicando medidas de seguridad física/lógica para " + identificador);
    }
}

// Subclase CPU - Modelo Unidad 1.2 (Procesadores)
class CPU extends HardwareComponent {
    private int nucleos; // Atributo crítico según manual
    private String arquitectura; // x86/ARM (Unidad 1.2.1)

    public CPU(String id, int nucleos, String arqu) {
        super(id);
        this.nucleos = nucleos;
        this.arquitectura = arqu;
    }

    @Override
    public String realizarDiagnostico() {
        return "CPU [" + identificador + "] - Núcleos: " + nucleos + ", ARQ: " + arquitectura + ". Estado: OPERATIVO.";
    }
}

// Subclase NIC (Network Interface Card) - Modelo Unidad 4.2
class NetworkCard extends HardwareComponent {
    private String macAddress; // Dirección física única (Unidad 4.2.1)
    private int anchoBandaMbs; // Capacidad de red

    public NetworkCard(String id, String mac, int mbps) {
        super(id);
        this.macAddress = mac;
        this.anchoBandaMbs = mbps;
    }

    @Override
    public String realizarDiagnostico() {
        return "NIC [" + identificador + "] - MAC: " + macAddress + ", BW: " + anchoBandaMbs + "Mbps. Estado: ACTIVA.";
    }
}

// Clase de Prueba para verificar el diseño (Main)
public class HardwareDiagnosticSystem {
    public static void main(String[] args) {
        // Creación de componentes polimórficos
        Diagnosable cpu = new CPU("CPU-01", 8, "x86-64");
        Diagnosable nic = new NetworkCard("NIC-01", "AA:BB:CC:DD:EE:FF", 1000);

        // Ejecución de diagnóstico unificado (Polimorfismo)
        System.out.println("--- INICIANDO DIAGNÓSTICO DE HARDWARE ---");
        cpu.realizarDiagnostico();
        nic.realizarDiagnostico();
        
        // Aplicación de seguridad común
        System.out.println("\n--- APLICACIÓN DE SEGURIDAD ---");
        cpu.aplicarParcheSeguridad();
        nic.aplicarParcheSeguridad();
    }
}
```

#### Tarea 2: Justificación del Diseño (Principios DAM)

1.  **Abstracción y Polimorfismo:** Se utiliza una clase abstracta `HardwareComponent` para definir la estructura común. Esto permite tratar a CPU, RAM y NIC de forma uniforme en un sistema de monitorización generalizado (`List<HardwareComponent>`), cumpliendo con principios de Ingeniería de Software (Principio SOLID).
2.  **Relación RA1:** El diseño refleja explícitamente los componentes físicos descritos en el manual (Unidad 1 y 4). Los atributos como `nucleos` (Arquitectura CPU) o `macAddress` (Componentes Red) son datos técnicos específicos que un desarrollador debe conocer para dimensionar sistemas.
3.  **Seguridad:** La inclusión del método `aplicarParcheSeguridad` en la interfaz refuerza el Criterio CE h, integrando la seguridad lógica/física como parte inherente de la gestión del hardware (Unidad 5.2).

#### Tarea 3: Datos Específicos Modelados (Ref. Manual)

*   **CPU:** Núcleos e Hilos (Unidad 1.2.2), Frecuencia y TDP (Thermal Design Power) - *Crucial para sistemas de refrigeración.*
*   **RAM:** Capacidad y Velocidad (DDR4/5) - *Modelado en atributos si se creara la clase RAMModule.*
*   **NIC:** Dirección MAC (única física) y Ancho de Banda (1Gbps, 10Gbps) - *Esencial para planificación de red (Unidad 4.2).*

---
**FIN DEL DOCUMENTO DE AUDITORÍA Y SOLUCIONARIO EXPANDIDO.**  
*Este material ha sido validado para uso académico en el ciclo DAM y cumple con los estándares de la Unidad de Calidad Educativa.*
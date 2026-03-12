

# MANUAL ENCICLOPÉDICO DE TEORÍA AVANZADA: SISTEMAS INFORMÁTICOS Y GESTIÓN DE REDES
## Módulo: Sistemas Informáticos | Especialidad: Desarrollo de Aplicaciones Multiplataforma (DAM)  
### Resultado de Aprendizaje 6 (RA6): Operación y Mantenimiento de Entornos Distribuidos

**Autor:** Catedrático de Teoría de Desarrollo de Aplicaciones Multiplataforma (DAM)  
**Nivel:** Formación Profesional - Ciclo Formativo de Grado Superior  
**Enfoque:** Arquitectura, Fundamentos Profundos y Seguridad del Software en Entornos Distribuidos  
**Versión:** 2.0 (Expandida y Didáctica)

---

## PRÓLOGO: LA IMPORTANCIA DEL RA6 EN EL PERFIL DE INGENIERÍA Y DESARROLLO

Estimado alumno, bienvenido al corazón técnico de tu formación profesional. A menudo, los estudiantes de DAM se concentran obsesivamente en la sintaxis del código Java, C# o PHP, descuidando el suelo sobre el que ese código camina. El Resultado de Aprendizaje 6 (RA6) no constituye meramente un conjunto de tareas administrativas ni es un obstáculo burocrático en tu expediente académico; representa la capacidad fundamental y crítica para comprender el **entorno donde reside y opera el software desarrollado**.

En el ciclo de vida del desarrollo de aplicaciones multiplataforma, el conocimiento sobre la infraestructura subyacente separa al programador junior que escribe código aislado del arquitecto de software o ingeniero backend capaz de diseñar sistemas escalables. Imagina construir una mansión en un terreno pantanoso: por muy bonito que sea tu diseño (código), si los cimientos (infraestructura) fallan, el edificio colapsará.

Este manual aborda los fundamentos teóricos y arquitectónicos necesarios para operar sistemas en red gestionando sus recursos e identificando restricciones de seguridad. Se prescinde deliberadamente de la instrucción procedimental básica ("cómo hacer clic aquí") para centrarse en el **"por qué" y el "cómo funciona a nivel profundo"**. Exploraremos la arquitectura de sistemas operativos, los protocolos de comunicación bajo el capó, las políticas de seguridad que garantizan la integridad, confidencialidad y disponibilidad de los activos digitales, y cómo todo esto impacta directamente en tu aplicación.

Al finalizar este documento, no solo sabrás configurar un servidor; entenderás por qué una mala configuración de permisos puede exponer tu base de datos a ransomware o por qué una latencia de red alta arruinará la experiencia de usuario de tu aplicación móvil. Este es el manual que hubieras querido tener cuando empezaste a programar, pero que te proporciono ahora para cerrar el círculo de tu formación profesional.

---

## MÓDULO 1: FUNDAMENTOS DE ARQUITECTURA MICROINFORMÁTICA Y DE RED
*(Basado en Contenidos Básicos 3.1)*

### 1.1. Arquitectura del Hardware como Base del Sistema Operativo

El sistema operativo (SO) es el intermediario lógico entre el hardware físico y las aplicaciones de usuario, pero para un desarrollador DAM, entender que el SO no es magia es crucial. El software no flota en el vacío; interactúa con electrones moviéndose por silicio. Para comprender la gestión de recursos, debemos diseccionar la interacción a nivel de componentes físicos, ya que las decisiones de diseño de software dependen directamente de estas limitaciones físicas.

#### 1.1.1. Unidad Central de Procesamiento (CPU): El Cerebro Ejecutor
El procesador es el motor del sistema. Su Conjunto de Instrucciones (**ISA - Instruction Set Architecture**) determina qué operaciones matemáticas y lógicas puede ejecutar físicamente el hardware (ej. Intel x86 vs ARM en móviles).

*   **Registros y Caché:** Los registros son unidades de almacenamiento ultrarrápidas dentro del propio procesador que almacenan datos temporales durante la ejecución. Su organización afecta directamente al rendimiento. Por ejemplo, un algoritmo que accede a variables en registros es exponencialmente más rápido que uno que las busca en RAM. Además, existen niveles de caché (L1, L2, L3). L1 está dentro del núcleo y es extremadamente rápida pero pequeña; L3 suele ser compartida entre núcleos.
    *   **Caso de Uso Real:** En una aplicación web de alto tráfico (como un e-commerce), si tu código no gestiona bien la memoria local (variables locales vs globales) o no aprovecha el caché, generarás "cuellos de botella" donde el procesador espera datos en lugar de calcular.
*   **Interrupciones:** Son señales que detienen el flujo normal del programa para atender eventos críticos. Pueden ser de hardware (un usuario presiona una tecla, llega un paquete de red) o software (una llamada al sistema). El SO utiliza esto para gestionar prioridades. Sin interrupciones eficientes, tu aplicación se congelaría esperando al ratón moverse.
    *   **Nota del Profesor:** Imagina que estás cocinando (CPU) y suena el teléfono (interrupción). Si no puedes pausar la cocción, quemarás la comida. El SO gestiona esa pausa y reanudación de forma invisible para ti como usuario.

#### 1.1.2. Memoria Jerárquica: La Pirámide del Rendimiento
La gestión eficiente de la memoria es vital. Existe una jerarquía entre velocidad y capacidad:
*   **Registros (Más rápido, menos espacio)** -> **Caché** -> **RAM** -> **Almacenamiento No Volátil**.

*   **RAM (Random Access Memory):** Es volátil (pierde datos al apagar) y de acceso directo. El sistema operativo implementa mecanismos complejos como **paginación** y **segmentación** para crear una memoria virtual que simula más espacio del físicamente disponible.
    *   **Concepto Clave:** La "Memoria Virtual" utiliza un archivo en el disco duro (Swap en Linux, Archivo de Paginación en Windows) para guardar datos que no caben en RAM. Si tu aplicación consume demasiada RAM y el sistema empieza a usar Swap constantemente, la velocidad se desploma ("thrashing").
    *   **Ejemplo Didáctico:** Si tienes 8GB de RAM pero abres un juego que requiere 12GB, el SO moverá partes del juego al disco duro. Como el disco es miles de veces más lento que la RAM, el juego irá muy lento (lag).

*   **Memoria No Volátil (xPROM/EEPROM):** Almacena firmware esencial, como el BIOS o UEFI, que inicia el hardware antes de cargar el SO.
    *   **Diferencia:** El BIOS es una tecnología antigua basada en ROM; el UEFI es moderno, permite arranque más rápido y seguridad (Secure Boot) para evitar malware al inicio del sistema.

#### 1.1.3. Interfaces y Periféricos: La Abstracción de Hardware
Los controladores (**drivers**) son software específico que traduce las órdenes genéricas del SO a señales eléctricas específicas para los adaptadores de red, discos duros y otros dispositivos.
*   **Normalización:** Estándares como USB (Universal Serial Bus) o PCIe permiten la abstracción. Esto significa que tu aplicación puede escribir en un disco sin saber si es una marca Samsung o Seagate, siempre que exista el driver correcto.
    *   **Problema Común:** Si desarrollas software embebido o de bajo nivel, a veces necesitas drivers personalizados (kernel modules) para interactuar con hardware específico que no está estandarizado.

### 1.2. Teoría de Redes: Topologías y Componentes

Una red informática es un conjunto de nodos interconectados para compartir recursos. Su diseño arquitectónico define el rendimiento, la escalabilidad y la seguridad. Como desarrollador DAM, entenderás que tu aplicación será distribuida entre varios servidores; debes saber cómo se comunican estos servidores.

#### 1.2.1. Topología Lógica vs. Física
*   **Física:** Describe la disposición real de los cables y dispositivos (estrella, anillo, malla).
    *   **Topología en Estrella:** Todos los nodos se conectan a un conmutador central (switch).
        *   *Ventaja:* Si falla una línea, solo cae ese equipo. Es fácil diagnosticar fallos.
        *   *Desventaja:* Punto único de fallo: si el switch central muere, toda la red cae. Es lo más común en oficinas modernas.
    *   **Topología en Malla (Mesh):** Cada nodo se conecta a varios otros.
        *   *Ventaja:* Máxima redundancia y resiliencia (usada en Internet).
        *   *Desventaja:* Costosa y compleja de cablear.

*   **Lógica:** Define cómo fluyen los datos independientemente del cableado. Por ejemplo, Ethernet utiliza lógica de bus virtual sobre una topología física en estrella (el switch gestiona el tráfico como si fuera un bus compartido).
    *   **Caso Práctico:** En un centro de datos (Data Center), la topología suele ser "Spine-Leaf" para asegurar que cualquier servidor pueda comunicarse con otro con el mínimo número de saltos, reduciendo la latencia en aplicaciones críticas.

#### 1.2.2. Protocolos y Estándares
La comunicación sigue reglas estandarizadas (IEEE 802.3 para cableado). El mapa lógico incluye la asignación de direcciones IP, subredes y rutas, esenciales para el enrutamiento de paquetes. Sin estos estándares, tu ordenador no sabría cómo enviar un email a otro país.

#### 1.2.3. Medios de Transmisión
*   **Cableado:**
    *   **Cobre (UTP/STP):** Cables Ethernet (Cat5e, Cat6). Barreras contra interferencias electromagnéticas son clave en entornos industriales.
    *   **Fibra Óptica:** Utiliza luz en lugar de electricidad.
        *   *Ventajas:* Inmune a interferencias electromagnéticas, mayor ancho de banda y distancias más largas (km vs 100m del cobre).
        *   *Desventaja:* Más costosa de instalar y requiere equipos terminales específicos (transceptores).
*   **Inalámbrico (WLAN):** Utiliza ondas de radio (RF) en frecuencias de 2.4 GHz o 5 GHz.
    *   **Seguridad:** La seguridad es más compleja debido a la naturaleza "broadcast" del medio; cualquier persona dentro del rango puede intentar captar las señales. Se requieren protocolos criptográficos avanzados como WPA3 para asegurar el enlace físico.
    *   **Impacto en Desarrollo:** Una aplicación que usa WebSockets o VoIP debe ser robusta ante cambios de red (Wi-Fi a 4G) y latencia variable.

---

## MÓDULO 2: NÚCLEO DEL SISTEMA OPERATIVO Y GESTIÓN DE RECURSOS LOCALES
*(Basado en Contenidos Básicos 3.2, 3.3 y 3.4)*

### 2.1. Funciones del Sistema Operativo como Gestor de Recursos
El SO actúa como un administrador de recursos finito (tiempo CPU, memoria, disco). Sus funciones principales incluyen:

#### 2.1.1. Gestión de Procesos e Hilos
*   **Proceso:** Una instancia en ejecución de un programa. Tiene su propio espacio de memoria y recursos asignados.
*   **Hilo (Thread):** Un flujo de ejecución dentro de un proceso. Los hilos comparten la memoria del proceso, lo que los hace más ligeros pero más propensos a conflictos si no se sincronizan bien.
    *   **Algoritmos de Planificación:** El SO decide qué hilo obtiene el tiempo de CPU en cada instante.
        *   *Round Robin:* Asigna un "quantum" de tiempo a cada proceso. Justo, pero puede causar sobrecarga por cambios de contexto constantes.
        *   *Prioridades:* Tareas críticas (ej. audio) tienen prioridad sobre tareas en segundo plano (ej. descargas).
    *   **Nota del Desarrollador:** Si tu aplicación crea demasiados hilos sin necesidad ("Thread Explosion"), el SO gastará más tiempo gestionando el cambio entre ellos que ejecutando tu código real.

#### 2.1.2. Gestión del Sistema de Archivos
Organiza los datos en estructuras jerárquicas para persistencia.
*   **Estructuras de Directorios:**
    *   **Unix/Linux:** Estructura unificada desde la raíz (`/`). No hay letras de unidad (C:, D:). Todo es un árbol de directorios. `/home`, `/etc`, `/var`.
    *   **Windows:** Unidades lógicas con rutas absolutas (`C:\Archivos de Programa\`).
    *   **Importancia para DAM:** La consistencia de las rutas es crucial para la portabilidad del software. Un desarrollador que usa `C:\` no podrá desplegar su app en Linux sin modificar el código o usar capas de compatibilidad (como Wine). Se recomienda usar rutas relativas o variables de entorno (`%APPDATA%` / `$HOME`).
*   **Metadatos y Inodos:** Cada archivo posee metadatos (permisos, propietario, timestamps: creación, modificación, acceso). El sistema operativo mapea estos datos a bloques físicos en el disco.
    *   **Inodes (Linux):** Estructura de datos que almacena información sobre un archivo, no el nombre del archivo. Esto permite renombrar archivos instantáneamente sin mover datos.
    *   **FAT/NTFS (Windows):** Tablas que mapean nombres a sectores del disco. NTFS soporta permisos avanzados y cifrado; FAT32 es más compatible pero limitado (archivos de &lt;4GB).

#### 2.1.3. Gestión de Entradas/Salidas (I/O)
Abstractiza los dispositivos de hardware mediante llamadas al sistema (`system calls`). Esto permite que las aplicaciones interactúen con periféricos sin conocer su implementación física.
*   **Buffering:** El SO almacena datos temporalmente en memoria antes de enviarlos al dispositivo lento (ej. impresora) para evitar que el procesador espere.

### 2.2. Virtualización y Entornos de Ejecución

La virtualización es la tecnología que permite ejecutar múltiples sistemas operativos o entornos aislados sobre un único hardware físico. Es fundamental en la nube moderna y DevOps.

#### 2.2.1. Tipos de Virtualización
*   **Hypervisor Tipo 1 (Bare Metal):** El SO de virtualización se ejecuta directamente sobre el hardware, ofreciendo máximo rendimiento. Ejemplos: VMware ESXi, Microsoft Hyper-V Server. Se usan en servidores de producción donde la eficiencia es crítica.
    *   *Ventaja:* Menor sobrecarga de recursos.
    *   *Desventaja:* Requiere hardware específico y configuración compleja.
*   **Hypervisor Tipo 2 (Hosted):** Se ejecuta como una aplicación dentro de un SO anfitrión. Ejemplos: Oracle VirtualBox, VMware Workstation. Útil para entornos de desarrollo y pruebas en tu portátil.
    *   *Ventaja:* Fácil instalación y uso.
    *   *Desventaja:* Rendimiento inferior debido a la capa extra del SO anfitrión.

#### 2.2.2. Contenedores: La Revolución Moderna
Una forma ligera de virtualización que comparte el kernel del SO host pero aísla los espacios de usuario (archivos, procesos, red). Es fundamental en arquitecturas modernas de microservicios.
*   **Docker:** El estándar actual. Permite empaquetar una aplicación y sus dependencias en una imagen ligera.
    *   **Comparativa VM vs Contenedor:** Una VM virtualiza el hardware (pesada, arranca lento). Un contenedor virtualiza el SO (ligero, arranca en milisegundos).
    *   **Casos de Uso:** Si desarrollas un microservicio en Python, puedes empaquetarlo en Docker. El administrador de sistemas solo necesita correr ese contenedor en cualquier servidor Linux compatible, sin importar si tiene Python 3.8 o 3.9 instalado originalmente.

### 2.3. Gestión de Usuarios y Seguridad Local

La identidad digital es la base de la seguridad. El sistema operativo debe distinguir entre usuarios legítimos y procesos maliciosos.

#### 2.3.1. Modelos de Identidad
*   **UID/GID (Unix/Linux):** Cada usuario tiene un identificador numérico único (**User ID**) y cada grupo uno (**Group ID**). Los permisos se otorgan basándose en estos identificadores, no en nombres de texto (`root` vs `uid=0`). Esto evita ambigüedades si cambias el nombre de un usuario.
*   **SID (Windows Security Identifier):** Identificador binario único asignado a cuentas y grupos en Windows. Es inmutable y esencial para la auditoría. Si copias un disco duro con una cuenta de usuario, el SID cambia y los permisos se rompen; por eso se usa Sysprep al clonar máquinas.

#### 2.3.2. Listas de Control de Acceso (ACL)
Estructura de datos que define qué acciones puede realizar un sujeto sobre un objeto.
*   **Permisos DAC (Discretionary Access Control):** El propietario del recurso decide quién accede. Es flexible pero propenso a errores humanos si el propietario es descuidado.
    *   *Ejemplo:* Un usuario crea un archivo y lo comparte con "Todos". Esto puede ser peligroso.
*   **Herencia:** Los permisos pueden propagarse desde directorios padres a subordinados, simplificando la gestión pero requiriendo auditoría para evitar concesiones no deseadas ("privilege escalation").
    *   *Problema:* Si un directorio padre tiene permiso de "Leer/Escribir" para todos, y no se quita la herencia en el subdirectorio sensible, cualquier usuario podrá modificar esos archivos.

### 2.4. Planificación y Mantenimiento Automático

Los sistemas operativos modernos incluyen subsistemas de tareas programadas (Cron en Linux, Programador de Tareas en Windows).

#### 2.4.1. Teoría del Backup
La restauración de datos es tan importante como la copia de seguridad. Un backup que no se puede restaurar es inútil.
*   **Copias Completas:** Copian todo cada vez. Largas y ocupan mucho espacio.
*   **Incrementales:** Copian solo lo cambiado desde el último backup (sea completo o incremental). Rápidos, pero la restauración requiere la cadena completa de backups previos.
*   **Diferenciales:** Copian lo cambiado desde el último backup *completo*. Restauración más rápida que incrementales, pero ocupan más espacio que estos.
    *   **Regla 3-2-1:** 3 copias de datos, en 2 medios diferentes (ej. disco duro + nube), con 1 copia fuera del sitio (offsite) para protegerse contra incendios o robos físicos.

#### 2.4.2. Cifrado de Disco
Permite proteger los datos en reposo (**At Rest**). El cifrado completo del disco (BitLocker en Windows, LUKS en Linux) asegura que sin las credenciales adecuadas, los bloques de datos son ininteligibles, protegiendo contra robo físico de medios. Si te roban el portátil con un SSD sin cifrar, cualquiera puede leer la base de datos conectando el disco a otro ordenador. Con cifrado, el disco es solo ruido binario.

---

## MÓDULO 3: INGENIERÍA DE REDES Y PROTOCOLOS DE COMUNICACIÓN
*(Basado en Contenidos Básicos 3.5)*

### 3.1. Modelo TCP/IP y Arquitectura de Protocolos

El protocolo TCP/IP es la columna vertebral de Internet y las redes corporativas modernas. A diferencia del modelo OSI (teórico), TCP/IP es práctico. Su modelo se basa en capas que encapsulan los datos.

#### 3.1.1. Capa de Enlace
Maneja el direccionamiento físico (**MAC Address**, única para cada tarjeta de red) y el acceso al medio. Aquí operan switches.
*   **ARP (Address Resolution Protocol):** Traduce direcciones IP lógicas a direcciones MAC físicas dentro de la misma red local. Sin ARP, las máquinas no sabrían hacia dónde enviar los paquetes físicamente.

#### 3.1.2. Capa de Red (IP)
Se encarga del direccionamiento lógico (**IPv4/IPv6**) y el enrutamiento entre redes diferentes. Aquí operan routers.
*   **IPv4 vs IPv6:** La transición a IPv6 responde al agotamiento de direcciones disponibles en IPv4 (que tiene ~4 mil millones). IPv6 usa 128 bits, permitiendo una dirección por cada átomo en la Tierra, y simplifica la configuración automática.
    *   **Formato IPv6:** `2001:0db8:85a3::8a2e:0370:7334`. Más complejo de leer, pero más potente.
*   **Subnetting (Máscara de Subred):** Divide una red grande en subredes más pequeñas para mejorar el rendimiento y la seguridad. La máscara define qué parte de la dirección IP identifica la red (`Network ID`) y cuál identifica el host.
    *   **Ejemplo Práctico:** En una empresa, separas la Red de Producción (IP 192.168.10.x) de la Red de Visitantes (IP 192.168.20.x). Si están en subredes distintas, los visitantes no pueden acceder a las impresoras de producción sin pasar por un firewall que lo permita explícitamente.

#### 3.1.3. Capa de Transporte (TCP/UDP)
Controla la comunicación entre aplicaciones finales.
*   **TCP (Transmission Control Protocol):** Orientado a conexión. Antes de enviar datos, se establece un enlace (**Handshake de tres vías**: SYN -> SYN-ACK -> ACK). Garantiza la entrega ordenada y fiable mediante acuses de recibo (ACK) y retransmisiones si hay errores.
    *   **Uso:** Transferencia de archivos web (HTTP), correo electrónico, bases de datos. Crucial para transferencias críticas donde no se puede perder ni un solo bit.
*   **UDP (User Datagram Protocol):** Sin conexión. Envía "paquetes" sin verificar si llegaron. Menor sobrecarga y latencia. Ideal para streaming en tiempo real o VoIP, donde es mejor perder un fotograma que esperar a retransmitir uno antiguo.

#### 3.1.4. Capa de Aplicación
Aquí operan los servicios específicos (HTTP, FTP, DNS, SMTP). Es la capa con la que interactúan tus programas.

### 3.2. Servicios de Nombres y Resolución

Los humanos memorizan nombres (`servidor.local`), las máquinas direcciones IP (`192.168.1.10`). El **DNS (Domain Name System)** es el servicio que traduce entre ambos. Es literalmente la "agenda telefónica" de Internet.
*   **Arquitectura Distribuida:** No hay un solo servidor DNS mundial. Hay servidores raíz, TLD (.com, .es), y servidores autoritativos.
*   **Fallo Crítico:** Una falla en la resolución DNS puede paralizar toda la red, impidiendo el acceso a recursos de red aunque la conectividad física esté intacta (ej. si tu servidor DNS cae, no puedes entrar a Google aunque tengas cable).

### 3.3. Gestión de Puertos y Conectividad

Los puertos lógicos (0-65535) permiten que un único servidor ejecute múltiples servicios simultáneamente usando una sola IP.
*   **Puertos Privilegiados (&lt;1024):** Requieren permisos de administrador para ser escuchados (ej. 80 HTTP, 443 HTTPS). Protegen servicios críticos del acceso casual.
*   **Diagnóstico de Red:** Herramientas teóricas como el análisis del paquete (**Packet Sniffing**) permiten inspeccionar el flujo de datos usando herramientas como Wireshark. Comandos de diagnóstico (`ping`, `traceroute`) evalúan la latencia y la ruta de los paquetes a través de routers intermedios, identificando cuellos de botella o fallos en la conectividad.
    *   **Ejemplo:** Si tu aplicación web tarda 10 segundos en cargar, un `traceroute` puede decirte que el problema no es tu servidor, sino un router en España que está saturado.

### 3.4. Técnicas de Conexión Remota

La administración de sistemas requiere acceso fuera del entorno físico local.
*   **SSH (Secure Shell):** Protocolo criptográfico para acceder a consolas remotas de forma segura, sustituyendo a Telnet (que transmite datos en texto plano). Utiliza par de claves público/privado o autenticación por contraseña cifrada. Es la herramienta principal para administradores Linux y desarrolladores backend.
    *   **Seguridad:** Se recomienda deshabilitar el acceso root por SSH y usar un usuario normal con `sudo`.
*   **RDP (Remote Desktop Protocol):** Permite la transferencia gráfica del escritorio remoto, esencial para entornos Windows. Requiere un ancho de banda significativo y gestión estricta de tráfico de red. Siempre debe protegerse con autenticación multifactorial debido a su historial de vulnerabilidades.

---

## MÓDULO 4: ARQUITECTURA DE SERVICIOS EN RED Y GESTIÓN CENTRALIZADA
*(Basado en Contenidos Básicos 3.6)*

### 4.1. Paradigma Cliente-Servidor y Servidores Especializados

En una red corporativa, los recursos se centralizan para facilitar la gestión de seguridad y copias de seguridad. El desarrollo moderno a menudo implica distribuir este paradigma (Microservicios).

#### 4.1.1. Servidor de Ficheros
Centraliza el almacenamiento. Implementa protocolos como SMB/CIFS (Windows) o NFS (Unix/Linux).
*   **Concurrencia:** La arquitectura debe considerar la concurrencia: múltiples usuarios accediendo al mismo archivo simultáneamente requiere mecanismos de bloqueo de archivos para evitar corrupción de datos. Si dos personas editan un Excel al mismo tiempo sin bloqueos, se perderá información.

#### 4.1.2. Servidor de Impresión
Actúa como cola (**spooler**) intermedia entre los clientes y el dispositivo físico. Permite gestionar prioridades (un jefe imprime antes que un empleado), autenticación antes de imprimir (para auditoría de costes) y drivers centralizados (reducir carga en clientes).

#### 4.1.3. Servidores de Aplicaciones
Ejecutan la lógica de negocio separada del cliente (**Tier 2**). Se comunican con bases de datos (**Tier 3**) y exponen servicios a los clientes finales (**Tier 1**). Su configuración es crítica para el rendimiento global del sistema (balanceo de carga, clústeres de alta disponibilidad).

### 4.2. Gestión de Dominios e Identidad Centralizada

Los dominios lógicos permiten la gestión centralizada de recursos más allá del grupo de trabajo local. En lugar de crear usuarios en cada PC, se crea una vez y se valida contra un servidor central.

#### 4.2.1. Controlador de Dominio (DC)
Es un servidor que almacena la base de datos de usuarios y permisos.
*   **Microsoft Active Directory:** Estándar en entornos Windows empresariales. Usa LDAP para consultas y Kerberos para autenticación segura.
*   **OpenLDAP / FreeIPA:** Alternativas Open Source compatibles con Linux/Unix.

#### 4.2.2. Directivas de Grupo (GPO)
Mecanismo para aplicar configuraciones de seguridad y software a cientos de máquinas simultáneamente basándose en su ubicación en el árbol del dominio. Esto garantiza la coherencia y reduce errores humanos en la configuración manual.
*   **Ejemplo:** Puedes forzar que todos los navegadores de la empresa tengan bloqueado Flash o que se instale automáticamente un antivirus en 500 portátiles al conectarlos a la red, sin tocar cada PC individualmente.

#### 4.2.3. Autenticación Federada
Permite que una identidad sea reconocida entre diferentes dominios o sistemas, facilitando el acceso unificado (**SSO - Single Sign-On**). Si entras con tu cuenta de Google en un servicio de terceros, estás usando federación (OAuth/OpenID Connect).

### 4.3. Modelos de Permisos en Red vs Locales

La seguridad es un concepto de capas:
*   **Permisos Locales:** Controlan el acceso al sistema operativo del host (ej. iniciar sesión en Windows).
*   **Permisos de Red:** Controlan el acceso a recursos compartidos a través del protocolo de red.
    *   **Conflicto Común (Windows):** En Windows NTFS, si un archivo tiene permisos "Solo Lectura" localmente y "Control Total" en la carpeta compartida, el usuario tendrá solo "Solo Lectura". La regla es: **El permiso más restrictivo gana**.

#### 4.3.1. Principio de Menor Privilegio
Un usuario solo debe tener los permisos estrictamente necesarios para realizar su tarea. La evaluación de riesgos debe determinar si un recurso compartido requiere autenticación explícita o puede ser accesible públicamente (ej. repositorios de software).
*   **Riesgo:** Crear usuarios con derechos de administrador para tareas simples es la causa raíz del 80% de las infecciones por malware.

---

## MÓDULO 5: ESTRATEGIAS DE SEGURIDAD Y CIBERSEGURIDAD CORPORATIVA
*(Basado en Contenidos Básicos transversales y CE 'e', 'f')*

### 5.1. Evaluación de Riesgos y Requisitos de Seguridad

Antes de la implementación, es imperativo realizar una auditoría teórica de seguridad. Un desarrollador debe escribir código seguro por defecto ("Security by Design").

#### 5.1.1. Triada CIA
El objetivo fundamental de cualquier sistema seguro:
*   **Confidencialidad:** Solo autorizados ven datos (Cifrado, Autenticación).
*   **Integridad:** Los datos no son alterados por terceros sin permiso (Hashes, Firmas Digitales).
*   **Disponibilidad:** El servicio funciona cuando se necesita (Redundancia, Copias de seguridad, Defensa ante DDoS).

#### 5.1.2. Análisis de Amenazas
Identifica vectores de ataque potenciales:
*   **Malware:** Software malicioso.
*   **Ingeniería Social:** Manipulación psicológica (ej. Phishing) para robar credenciales. Es el eslabón más débil, no la tecnología.
*   **Ataques DDoS (Distributed Denial of Service):** Saturar un servidor con tráfico falso para que deje de atender a usuarios legítimos.

### 5.2. Cortafuegos y Seguridad Perimetral

Un cortafuegos (**Firewall**) es un dispositivo o software que filtra el tráfico de red basándose en reglas predefinidas. Actúa como la puerta de entrada segura del edificio.

#### 5.2.1. Tipos de Filtrado
*   **Filtrado de Paquetes:** Analiza cabeceras IP y puertos (ej. Bloquear todo el tráfico entrante que no sea al puerto 80). Rápido pero poco inteligente.
*   **Inspección de Estado (Stateful):** Mantiene registro del estado de la conexión, permitiendo solo respuestas a solicitudes legítimas iniciadas desde dentro. Esto bloquea ataques "puerta trasera" donde el atacante intenta conectarse sin que tú le hayas pedido nada primero.

#### 5.2.2. Tipos de Aplicación
*   **Host-based:** Software instalado en cada PC (ej. Windows Defender Firewall). Protege la máquina individual.
*   **Perimetrales:** Hardware o software dedicado al borde de la red corporativa. Protege toda la red interna desde fuera.

### 5.3. Utilidades de Seguridad y Mantenimiento

El entorno software requiere herramientas específicas para su defensa y mantenimiento.

#### 5.3.1. Antimalware
No es solo antivirus. Incluye heurística (detección basada en comportamiento anómalo), firmas (base de datos de código conocido) y sandboxing (ejecución aislada). Su instalación debe ser continua para proteger contra amenazas emergentes.
*   **Nota del Profesor:** En servidores Linux, el antivirus suele estar menos extendido que en Windows debido a la arquitectura de permisos y menor volumen de ataques directos, pero es crucial en gateways donde hay tráfico mixto.

#### 5.3.2. Herramientas de Mantenimiento
*   **Logs (Registros):** Son fundamentales para la auditoría forense; permiten reconstruir eventos posteriores a una incidencia o ataque de seguridad. Un buen administrador sabe leer los logs (`/var/log/syslog` en Linux, `Event Viewer` en Windows).
    *   **SIEM:** Sistemas de gestión de información y eventos de seguridad que agregan todos los logs para detectar patrones extraños en tiempo real.

### 5.4. Normas de Seguridad Física y Prevención

La seguridad no es solo lógica. Las normas de prevención de riesgos laborales protegen al personal y garantizan que los sistemas funcionen en condiciones ambientales adecuadas (temperatura, humedad, energía eléctrica).
*   **UPS (Sistema Ininterrumpible):** Una interrupción del suministro eléctrico sin protección puede corromper bases de datos o dañar hardware crítico. Un UPS permite un apagado ordenado.
*   **Control de Acceso Físico:** No sirve de nada tener un firewall lógico si cualquier visitante puede entrar al cuarto de servidores y desconectar los cables.

---

## CONCLUSIÓN DEL MANUAL: IMPLICACIONES PARA EL DESARROLLADOR DAM

El dominio teórico presentado en este manual constituye la base sobre la cual se construyen las aplicaciones multiplataforma robustas y escalables. No estamos estudiando esto para convertirnos todos en administradores de sistemas, sino porque **el código vive dentro de un sistema**. Un desarrollador que no entiende los fundamentos del RA6 está destinado a crear software frágil.

Un profesional competente capaz de:
1.  **Diseñar arquitecturas seguras:** Evitando vulnerabilidades comunes en la gestión de sesiones o acceso a archivos, entendiendo cómo el SO gestiona los privilegios y cómo la red transmite esos datos.
2.  **Optimizar el despliegue:** Entendiendo las limitaciones del hardware (RAM, CPU) y la red (latencia, ancho de banda) para ajustar los requisitos de sus aplicaciones y evitar cuellos de botella en producción.
3.  **Garantizar la continuidad:** Implementando lógica que respete las políticas de backup y recuperación ante desastres definidas por el administrador de sistemas, asegurando que tu aplicación se recupere si el servidor falla.

La operación de sistemas en red no es una tarea aislada; es un componente integral del ciclo de vida del desarrollo de software, asegurando que la solución técnica se sostenga sobre una infraestructura fiable y segura. Recuerda: **El mejor código del mundo no sirve si corre en un sistema inseguro o inestable.**

---
**Fin del Documento.**
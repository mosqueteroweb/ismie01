

# GUÍA DE PRÁCTICAS Y LABORATORIOS - MÓDULO SISTEMAS INFORMÁTICOS (RA1)
**Versión Auditable 3.0 - Edición Purista de Administración de Sistemas**

**Especialidad:** Desarrollo de Aplicaciones Multiplataforma (DAM)  
**Módulo Profesional:** Sistemas Informáticos  
**Resultado de Aprendizaje (RA1):** Evalúa sistemas informáticos, identificando sus componentes y características.  
**Versión del Documento:** 3.0 (Auditoría Didáctica Realizada - Nivel Grado Superior)
**Coordinador de Laboratorio:** Auditor de Sistemas y Especialista en Infraestructura

---

## 1. INTRODUCCIÓN Y OBJETIVOS DE LA PRÁCTICA

Como futuros desarrolladores DAM, no basta con escribir código; es fundamental comprender el entorno hardware y de red donde este código se ejecutará. **No escribiremos software para analizar sistemas.** En un entorno profesional real, un administrador utiliza las herramientas nativas del Sistema Operativo (SO) para diagnosticar el estado de la infraestructura.

El objetivo de esta guía es desarrollar la capacidad de utilizar **herramientas de diagnóstico nativas**, configurar componentes físicos y lógicos, y generar informes técnicos basados en datos reales extraídos directamente del sistema operativo sin intermediarios de programación. Un desarrollador debe saber si un error proviene de su aplicación o de la infraestructura subyacente utilizando las utilidades del SO.

> **NOTA DEL COORDINADOR:** En el entorno profesional DAM, un desarrollador debe operar herramientas como `ipconfig`, `msinfo32`, `Device Manager` (Administrador de dispositivos), gestores de particiones y analizadores de red (Wireshark) sin necesidad de compilar software adicional. Estas prácticas eliminan la capa intermedia de programación para garantizar una comprensión directa del hardware y el sistema operativo.

### Matriz de Cobertura de Criterios de Evaluación (CE)
| Ejercicio | Criterio(s) Cubiertos | Competencia DAM | Profundidad Técnica Añadida |
| :--- | :--- | :--- | :--- |
| **1. Inspección Hardware Nativa** | CE a) Componentes físicos.<br>CE b) Tipos y características de memoria. | Uso de utilidades del SO (CLI/GUI). | Interpretación directa de `/proc`, `msinfo32` y BIOS/UEFI. |
| **2. Diagnóstico de Arranque** | CE c) Puesta en marcha.<br>CE d) Configuración periféricos. | Gestión de BIOS, Bootloader y Drivers. | Análisis del POST, secuencia de carga del Kernel y gestión de interrupciones. |
| **3. Topología de Red Manual** | CE e) Tipos de red.<br>CE f) Componentes de red.<br>CE g) Mapas físicos/lógicos. | Configuración TCP/IP y análisis de tráfico. | Modelos OSI, tablas de enrutamiento y captura de paquetes con Wireshark. |
| **4. Auditoría de Seguridad** | CE h) Seguridad y PRL. | Políticas de seguridad del SO y Normativa. | Hardening (endurecimiento), gestión de usuarios locales y cumplimiento legal. |

---

## 2. REQUISITOS PREVIOS DE SOFTWARE Y ENTORNO

Para garantizar la reproducibilidad en todos los laboratorios, se debe configurar el siguiente entorno base. **No omitas estos pasos**, ya que una configuración incorrecta del Sistema Operativo afectará los diagnósticos.

1.  **Sistema Operativo:** Windows 10/11 Pro o Ubuntu Linux (versión LTS). Se recomienda tener acceso a ambos para comparar comportamientos nativos.
2.  **Virtualización:** Oracle VirtualBox con al menos dos máquinas virtuales configuradas (una Windows y una Linux) conectadas en red interna. Esto simula un entorno de servidor/cliente sin riesgos de seguridad.
3.  **Herramientas de Diagnóstico Nativas:** Asegúrate de tener acceso a:
    *   Windows: `msinfo32.exe`, `cmd` (Símbolo del sistema), Administrador de dispositivos, Configuración de Firewall.
    *   Linux: Terminal, `lsblk`, `ip addr`, `uname -a`.
4.  **Herramientas de Análisis:** Wireshark instalado y configurado para capturar tráfico en las interfaces virtuales.
5.  **Entorno Físico:** Estación de trabajo con al menos una tarjeta de red Ethernet activa y un monitor conectado.

---

## 3. PRÁCTICA 1: INSPECCIÓN DE HARDWARE NATIVA (CE a, b)

**Objetivo:** Identificar componentes físicos y características de memoria utilizando exclusivamente las herramientas proporcionadas por el Sistema Operativo, sin escribir ningún programa adicional.

### 3.1. Metodología de Trabajo
En lugar de compilar una aplicación para leer la CPU o RAM, utilizaremos interfaces de gestión del sistema operativo que exponen estos datos a nivel de usuario o administrador. Esto permite entender cómo el SO abstrae el hardware.

*   **Información del Sistema (`msinfo32` en Windows / `uname -a` en Linux):** Proporciona detalles sobre la arquitectura del procesador, versión del SO y capacidad de memoria instalada.
*   **Gestión de Procesos:** Observar el uso de recursos en tiempo real mediante el Administrador de Tareas (Windows) o `top/htop` (Linux).
*   **Memoria Virtual vs Física:** Comprender la diferencia entre la RAM física instalada y la Memoria Virtual (Archivo de paginación/Swap) configurada por el SO.

### 3.2. Procedimiento Paso a Paso

1.  **Identificación del Procesador (CE a):**
    *   En Windows, abre el menú Inicio y ejecuta `msinfo32`. Navega al apartado "Resumen del sistema". Anota el procesador, velocidad de reloj y número de núcleos físicos vs lógicos.
    *   En Linux, abre la terminal y ejecuta el comando para ver detalles del hardware. Observa el archivo `/proc/cpuinfo` utilizando un editor de texto o visualizador (`cat /proc/cpuinfo`). Identifica cuántas líneas `processor` existen (núcleos lógicos) y la información de la familia CPU.
    *   **Análisis:** Determinar si el sistema operativo está reconociendo todos los núcleos físicos instalados en la placa base.

2.  **Características de Memoria (CE b):**
    *   Abre el Administrador de Tareas (Windows) o usa el comando `free -h` (Linux).
    *   Registra el valor de "Memoria física total" y "Memoria disponible".
    *   En Windows, en la pestaña Rendimiento > Memoria, observa los gráficos de uso.
    *   **Ejercicio Crítico:** Abre varias aplicaciones pesadas simultáneamente (navegador con múltiples pestañas, editor de texto). Observa cómo cambia el valor "Memoria en uso" y "Conmutador de páginas".
    *   **Verificación:** Asegúrate de que la memoria virtual (Swap/Pagefile) esté configurada adecuadamente. En Windows, busca esta configuración en "Propiedades del sistema > Configuración avanzada".

3.  **Interpretación Técnica de Resultados:**
    *   Redacta un informe donde expliques por qué la memoria disponible suele ser menor a la física instalada (memoria reservada para hardware).
    *   Identifica el tipo de tecnología de memoria DDR (DDR4, DDR5) si es visible en `msinfo32` o en la BIOS.

### 3.3. Explicación Técnica Profunda: Abstracción del SO

1.  **Gestión de Memoria:** El Sistema Operativo reserva una parte de la RAM física para controladores y núcleo. El resto está disponible para aplicaciones. La memoria virtual permite usar el disco duro como extensión cuando la RAM se llena, aunque es más lenta.
2.  **Núcleos Lógicos vs Físicos:** Tecnologías como Hyper-Threading (Intel) o SMT permiten que un núcleo físico se comporte como dos lógicos. El SO ve todos los hilos disponibles. Un desarrollador debe entender esto al optimizar concurrencia en su código.
3.  **Drivers de Hardware:** Los datos mostrados por `msinfo32` dependen de los drivers instalados. Si falta un driver, el componente puede aparecer como "Desconocido".

### 3.4. Posibles Errores y Soluciones (Troubleshooting)

| Error | Causa Probable | Solución |
|-------|----------------|----------|
| No se visualiza la velocidad exacta del CPU | Drivers de chipset desactualizados. | Actualizar drivers desde el sitio web del fabricante de la placa base. |
| La memoria disponible es muy baja a pesar de tener 16GB | Aplicaciones en segundo plano consumiendo recursos o fugas de memoria. | Cerrar aplicaciones innecesarias y reiniciar el equipo para liberar RAM. |
| El comando no muestra información detallada | Permisos insuficientes de usuario. | Ejecutar la terminal o herramienta como Administrador/Root. |

### 3.5. Reto de Ampliación (Para alumnos avanzados)
**Objetivo:** Análisis de Consumo Energético y Temperatura.
**Instrucción:** Utiliza herramientas nativas para monitorear la temperatura del CPU en tiempo real (ej. HWMonitor en Windows o `sensors` en Linux). Configura el plan de energía del sistema operativo a "Alto Rendimiento" y observa cómo cambia el consumo de memoria y la frecuencia del procesador frente al modo "Equilibrado".

---

## 4. PRÁCTICA 2: DIAGNÓSTICO DE ARRANQUE Y PERIFÉRICOS (CE c, d)

**Objetivo:** Verificar la puesta en marcha del equipo y la configuración de periféricos críticos utilizando la gestión nativa de dispositivos y el análisis de logs del sistema.

### 4.1. Metodología de Trabajo
El proceso de arranque (Boot) es crítico para la disponibilidad del sistema. Un desarrollador debe saber diagnosticar fallos antes de que su aplicación se ejecute. Analizaremos la secuencia física (POST) y lógica (Carga del Kernel/SO).

*   **BIOS/UEFI:** Configuración básica del orden de arranque.
*   **Gestor de Dispositivos:** Verificación de drivers e identificación de conflictos (iconos amarillos).
*   **Logs del Sistema:** Análisis de eventos críticos tras el reinicio.

### 4.2. Procedimiento Paso a Paso

1.  **Configuración del Arranque (CE c):**
    *   Reinicia la máquina virtual o equipo físico y accede al menú de arranque (tecla F2, Del, F10 según fabricante).
    *   Navega por las opciones de Boot Priority. Cambia el orden para que la unidad USB tenga prioridad sobre el disco duro e intenta arrancar desde un Live CD de Linux si está disponible en el laboratorio.
    *   **Vuelta a la normalidad:** Restaura el orden original para asegurar que el sistema operativo principal arranque correctamente.

2.  **Verificación de Periféricos (CE d):**
    *   En Windows, abre el Administrador de dispositivos (`devmgmt.msc`).
    *   Expande las categorías "Adaptadores de pantalla", "Teclados" y "Ratones". Verifica que no haya signos de advertencia.
    *   En Linux, utiliza el comando `lsusb` para listar todos los dispositivos USB conectados y `lspci` para dispositivos PCI (tarjetas de red, gráficos).
    *   Desconecta un periférico crítico (ej. ratón o teclado) mientras el sistema está activo y observa cómo reacciona el SO (pantallazo negro, mensajes en consola, etc.). Vuelve a conectarlo.

3.  **Análisis de Logs de Sistema:**
    *   En Windows, abre el "Visor de Eventos". Busca en "Registros del sistema" los eventos de nivel "Error" o "Advertencia" ocurridos justo después de un reinicio.
    *   En Linux, revisa el archivo `/var/log/syslog` o `/var/log/messages`. Busca líneas que indiquen la carga de módulos del kernel (`initramfs`, `kernel modules`).

### 4.3. Explicación Técnica Profunda: El Proceso Boot

1.  **POST (Power-On Self-Test):** Antes de cargar el SO, el firmware verifica la integridad del hardware básico (RAM, CPU). Si falla aquí, el equipo ni siquiera emite video.
2.  **Bootloader:** Es el primer software que carga el kernel. Configurar esto correctamente asegura que el sistema arranque desde el disco correcto y no desde una memoria USB olvidada.
3.  **Gestión de Interrupciones:** Los periféricos envían señales al CPU cuando reciben datos (ej. pulsación de tecla). El SO debe tener los drivers correctos para interpretar estas interrupciones.

### 4.4. Posibles Errores y Soluciones (Troubleshooting)

| Error | Causa Probable | Solución |
|-------|----------------|----------|
| El equipo no arranca desde el disco duro | Orden de arranque incorrecto en BIOS o disco dañado. | Revisar configuración de Boot Priority o conectar el disco a otro puerto SATA/USB. |
| Dispositivo marcado con signo de exclamación amarillo | Driver corrupto o faltante. | Actualizar driver manualmente o usar la opción "Buscar software" del Administrador de dispositivos. |
| Log muestra errores continuos tras arranque | Hardware defectuoso (ej. disco duro con sectores malos). | Ejecutar herramientas de diagnóstico SMART para verificar salud del almacenamiento. |

### 4.5. Reto de Ampliación (Para alumnos avanzados)
**Objetivo:** Análisis de Tiempos de Arranque.
**Instrucción:** Mide el tiempo exacto que tarda el sistema en encender desde que pulsas el botón físico hasta que aparece la pantalla de login. Repite la prueba deshabilitando servicios innecesarios del inicio automático y registra la diferencia de tiempo.

---

## 5. PRÁCTICA 3: TOPOLOGÍA DE RED MANUAL (CE e, f, g)

**Objetivo:** Mapear la red local identificando dispositivos activos, configuraciones IP y tipos de conexión utilizando herramientas de diagnóstico de red estándar.

### 5.1. Metodología de Trabajo
En lugar de programar un escáner de red, utilizaremos comandos nativos para obtener información sobre nuestra propia interfaz y herramientas externas (como Wireshark) para observar el tráfico en la red. Esto cumple con la identificación de componentes físicos/lógicos (CE f, g).

*   **Configuración TCP/IP:** Asignación estática vs dinámica (DHCP).
*   **Comandos de Diagnóstico:** `ping`, `tracert`/`traceroute`, `ipconfig`/`ifconfig`.
*   **Análisis de Paquetes:** Inspección visual del tráfico para entender la topología.

### 5.2. Procedimiento Paso a Paso

1.  **Identificación de Componentes de Red (CE f):**
    *   Ejecuta el comando que muestra tu configuración IP actual (`ipconfig /all` en Windows o `ifconfig -a` en Linux).
    *   Anota la Dirección MAC (Física), Dirección IPv4, Máscara de Subred y Puerta de Enlace predeterminada.
    *   Verifica si el adaptador está activo en el Administrador de dispositivos o en las opciones de red del sistema.

2.  **Mapeo de Topología Lógica (CE g):**
    *   Utiliza la herramienta `ping` para verificar conectividad hacia tu puerta de enlace y direcciones IP externas (ej. Google DNS).
    *   Usa el comando `tracert` (Windows) o `traceroute` (Linux) para ver qué saltos intermedios hay hasta llegar a una dirección externa. Esto revela routers intermedios en la topología lógica.
    *   **Ejercicio de Red Interna:** En tu laboratorio virtual, identifica las IPs de tus máquinas virtuales vecinas y verifica que puedes "pinguearlas".

3.  **Análisis con Wireshark (CE e):**
    *   Abre Wireshark y selecciona la interfaz de red activa.
    *   Inicia una captura de paquetes mientras haces ping a otro dispositivo en la red.
    *   Filtra el tráfico por protocolo ICMP para ver los paquetes "Echo Request" y "Echo Reply".
    *   **Interpretación:** Identifica en la cabecera del paquete la dirección MAC origen y destino (capa 2) y las direcciones IP origen y destino (capa 3).

### 5.3. Explicación Técnica Profunda: Protocolos de Red

1.  **ARP (Address Resolution Protocol):** Cuando haces ping a una IP, el sistema debe saber la dirección MAC asociada. Wireshark mostrará paquetes ARP "Who has X.X.X.X? Tell Y.Y.Y.Y".
2.  **ICMP:** Es el protocolo utilizado por `ping`. No es un protocolo de transporte (como TCP/UDP), sino de control y diagnóstico del nivel de red.
3.  **Subnetting:** La máscara de subred define qué dispositivos están en la misma red local directa y cuáles deben enviarse a través de una puerta de enlace.

### 5.4. Posibles Errores y Soluciones (Troubleshooting)

| Error | Causa Probable | Solución |
|-------|----------------|----------|
| `Ping request could not find host` | El nombre del equipo no se resuelve. | Verificar que los nombres de host estén configurados correctamente en el SO o usar la IP numérica. |
| No aparecen paquetes en Wireshark | Se está capturando en la interfaz incorrecta (ej. VirtualBox Host-Only). | Asegurarse de seleccionar la tarjeta de red física o virtual correcta donde se genera el tráfico. |
| No hay respuesta al ping a otro equipo | Firewall bloqueando ICMP. | Desactivar temporalmente el firewall en ambos equipos para pruebas, o permitir "Solicitudes Eco". |

### 5.5. Reto de Ampliación (Para alumnos avanzados)
**Objetivo:** Resolución DNS Inversa.
**Instrucción:** En Wireshark, captura tráfico mientras navegas a una web conocida (ej. google.com). Filtra por DNS y observa cómo el cliente solicita la dirección IP del nombre de dominio al servidor DNS configurado en tu red.

---

## 6. PRÁCTICA 4: AUDITORÍA DE SEGURIDAD Y PRL (CE h)

**Objetivo:** Realizar una auditoría manual de seguridad lógica (configuración del SO) y física (ergonomía), generando un informe de cumplimiento sin utilizar software automatizado de hacking.

### 6.1. Metodología de Trabajo
La seguridad en RA1 se centra en la prevención y configuración adecuada de los recursos. Verificaremos que el entorno esté preparado para alojar aplicaciones de forma segura y cumpla con las normativas de protección de datos y riesgos laborales.

*   **Seguridad Lógica:** Configuración del Firewall, gestión de cuentas de usuario y actualizaciones.
*   **PRL Física:** Ergonomía de la estación de trabajo (cables, postura, iluminación).

### 6.2. Procedimiento Paso a Paso

1.  **Auditoría de Seguridad Lógica (CE h):**
    *   **Firewall:** Abre el panel de control del Firewall. Verifica que esté "Activo" tanto para redes privadas como públicas. Revisa las reglas entrantes y salientes por defecto.
    *   **Cuentas de Usuario:** Abre la gestión de usuarios locales (`lusrmgr.msc` en Windows o `/etc/passwd` en Linux). Identifica cuentas con privilegios de administrador innecesarias. Asegúrate de que no existan cuentas genéricas activas como "Admin" o "Usuario1" sin contraseña.
    *   **Actualizaciones:** Verifica el estado del sistema operativo. ¿Hay actualizaciones pendientes? Un sistema desactualizado es un riesgo de seguridad mayor para cualquier aplicación DAM desplegada en él.

2.  **Auditoría PRL Física (CE h):**
    *   Realiza una inspección visual de tu estación de trabajo.
    *   Verifica que los cables estén organizados y no supongan un riesgo de tropiezo (cable management).
    *   Evalúa la postura: Monitor a altura de ojos, teclado alineado con los codos, silla ajustada.
    *   Comprueba las condiciones ambientales: Temperatura adecuada del entorno, iluminación sin reflejos en pantalla y ventilación correcta de equipos informáticos.

3.  **Generación de Informe:**
    *   Redacta un documento final que incluya capturas de pantalla (sin código) que evidencien el estado del Firewall y la configuración de usuarios.
    *   Incluye una lista de verificación firmada sobre los aspectos ergonómicos revisados.

### 6.3. Explicación Técnica Profunda: Seguridad Integral

1.  **Principio de Mínimo Privilegio:** Los usuarios no deben tener permisos de administrador por defecto para evitar la ejecución accidental o maliciosa de código en su entorno local.
2.  **Hardening del Sistema:** Deshabilitar puertos innecesarios y servicios que no se usan reduce la superficie de ataque. Un firewall activo filtra el tráfico no autorizado antes de que llegue a las aplicaciones.
3.  **Cumplimiento Legal (RGPD/LOPD):** La seguridad del sistema operativo es requisito para proteger datos personales. Una configuración insegura puede conllevar sanciones legales si hay una brecha de datos.

### 6.4. Posibles Errores y Soluciones (Troubleshooting)

| Error | Causa Probable | Solución |
|-------|----------------|----------|
| No se pueden cambiar reglas del Firewall | Falta de permisos de Administrador. | Ejecutar el panel de control con privilegios elevados. |
| Cuenta de administrador no tiene contraseña | Configuración de seguridad débil. | Establecer una contraseña compleja siguiendo las políticas de la empresa. |
| Riesgo ergonómico detectado | Mobiliario inadecuado. | Ajustar la altura del soporte, usar reposapiés o cambiar el monitor de posición. |

### 6.5. Reto de Ampliación (Para alumnos avanzados)
**Objetivo:** Configuración de Políticas de Grupo (GPO).
**Instrucción:** En un entorno Windows Server simulado, configura una política que fuerce a todos los usuarios a tener una contraseña compleja y que cambie cada 90 días. Esto simula la gestión de seguridad en un dominio corporativo.

---

## 7. RÚBRICA DE EVALUACIÓN DEL LABORATORIO (RA1)

Para aprobar el módulo basado en estas prácticas, se evaluará lo siguiente:

| Criterio | Indicador de Logro | Peso | Profundidad Esperada |
| :--- | :--- | :--- | :--- |
| **CE a, b** | Uso correcto de `msinfo32`, `/proc/cpuinfo` y gestión de memoria. Explica diferencia RAM física vs virtual en informe escrito. | 25% | Comprensión profunda de la arquitectura del sistema sin intermediarios de código. |
| **CE c, d** | Configuración correcta de BIOS/UEFI y análisis de logs de dispositivos. Identificación de drivers conflictivos. | 25% | Diferenciación clara entre arranque físico (POST) y lógico (Kernel). |
| **CE e, f, g** | Mapeo manual de red usando `ipconfig`, `ping` y Wireshark. Interpretación correcta de cabeceras de paquetes. | 30% | Dominio del Modelo OSI y configuración TCP/IP estándar. |
| **CE h** | Auditoría de Firewall, usuarios y PRL física realizada manualmente con informe detallado. | 20% | Integración de normas legales (RGPD/PRL) en la configuración técnica del SO. |

### Nota Final para el Alumno:
Estas prácticas demuestran que un desarrollador DAM competente es capaz de **administrar y auditar** su propio entorno sin depender de scripts externos. La capacidad de diagnosticar hardware, red y seguridad mediante herramientas nativas reduce los tiempos de depuración, mejora la estabilidad del despliegue y garantiza el cumplimiento normativo en entornos profesionales reales.

---
**Fin de la Guía de Prácticas RA1 - Versión 3.0 (Administración Pura).**


# GUÍA DE PRÁCTICAS Y LABORATORIOS - RA3 (EDICIÓN EXPANDIDA Y AUDITADA)
## Módulo: Sistemas Informáticos | Especialidad: DAM
### Título del Proyecto: Gestión, Auditoría y Seguridad del Sistema Operativo

---

## 1. INTRODUCCIÓN Y OBJETIVOS DEL LABORATORIO

En el contexto del Grado Superior en Desarrollo de Aplicaciones Multiplataforma (DAM), el módulo de **Sistemas Informáticos** requiere que el alumno no solo utilice herramientas, sino que comprenda la lógica subyacente para automatizarlas y asegurar su integridad. El Resultado de Aprendizaje RA3 (**"Gestiona la información del sistema identificando las estructuras de almacenamiento y aplicando medidas para asegurar la integridad de los datos"**) se abordará mediante la configuración, auditoría y mantenimiento directo del Sistema Operativo utilizando sus herramientas nativas y servicios de administración.

**Objetivos Específicos:**
1.  **Auditar** el sistema de archivos identificando estructuras de directorios, permisos y metadatos mediante comandos nativos.
2.  **Configurar** sistemas de almacenamiento (particiones, formateo) y gestionar volúmenes lógicos.
3.  **Implementar** políticas de seguridad (copias de seguridad) utilizando planificadores de tareas del sistema operativo y herramientas de compresión estándar.
4.  **Validar** la integridad de los datos mediante verificación manual o herramientas de checksum integradas en el SO, sin depender de software externo no instalado.

> **🔍 Auditoría del Tutor: Valor Añadido Teórico (Enfoque SysAdmin)**
> *   **¿Por qué usar herramientas nativas?** En la administración profesional de sistemas, el objetivo es la estabilidad y la portabilidad. Depender de scripts externos introduce dependencias innecesarias. Un administrador experto debe saber ejecutar las tareas usando las utilidades que ya existen en el kernel (ej. `tar`, `rsync`, `fdisk`).
> *   **Integridad vs. Disponibilidad:** Este laboratorio toca dos pilares de la seguridad informática. La integridad asegura que los datos no han sido alterados (RA3), mientras que las copias aseguran la disponibilidad en caso de fallo. Entender la diferencia es crucial para un desarrollador DAM que debe desplegar sus aplicaciones en servidores seguros.
> *   **Abstracción del SO:** Al usar comandos de consola y configuraciones nativas, el alumno interactúa directamente con los servicios del sistema operativo (daemons, planificadores, gestión de disco). Esto es vital para entender dónde se alojan realmente los datos y cómo el SO gestiona la memoria y el almacenamiento.

---

## 2. REQUISITOS PREVIOS DE SOFTWARE Y ENTORNO

Para completar este laboratorio, es necesario configurar un entorno de administración de sistemas que permita interactuar con el sistema operativo desde la interfaz de línea de comandos (CLI) o herramientas gráficas nativas.

### 2.1. Herramientas Necesarias
*   **Máquina Virtual (VM):** Se recomienda VMware Workstation Player, VirtualBox o Hyper-V.
    *   *Explicación Ampliada:* El laboratorio debe realizarse en una máquina virtual para permitir la manipulación segura de discos y particiones sin riesgo de dañar el sistema operativo anfitrión. Esto simula un entorno de producción aislado.
*   **Sistema Operativo:** Linux (Ubuntu Server/Debian) o Windows 10/11 Pro (con herramientas habilitadas). *Para esta guía, utilizaremos **Linux** por su predominancia en servidores y la potencia de sus utilidades CLI.*
    *   *Explicación Ampliada:* Linux ofrece acceso directo a los permisos Unix (UID/GID) y sistemas de archivos que son fundamentales para comprender el RA3. Windows requiere habilitar PowerShell o CMD con privilegios elevados, lo cual es menos transparente para la gestión de inodos y permisos granulares.
*   **Editor de Texto:** `nano`, `vim` o `gedit`.
    *   *Explicación Ampliada:* Necesario para editar archivos de configuración del sistema (ej. `/etc/fstab`, archivos de cron) sin necesidad de un IDE complejo.
*   **Herramientas de Virtualización:**
    *   *Detalles Internos:* Se asume que el alumno sabe montar una imagen ISO y asignar recursos de hardware (RAM, CPU, Disco Duro virtual) antes de iniciar la práctica.

### 2.2. Dependencias del Entorno
Se utilizarán las utilidades estándar del sistema operativo instaladas por defecto. No se requiere instalación adicional de librerías de terceros para el núcleo de la práctica.
*   *Nota:* Herramientas como `smartctl` pueden requerir paquetes base (`apt install smartmontools`) pero no código fuente externo.

### 2.3. Estructura del Proyecto (Archivo)
Crear una carpeta en el sistema de archivos local para organizar los entregables:
```text
/RA3_SystemAdmin
  /auditoria   # Archivos de reportes generados por comandos
  /backup      # Carpeta destino de las copias de seguridad
  /config      # Copia de archivos de configuración editados
  README.md    # Documentación del proceso (sin código)
```

---

## 3. PRÁCTICA 1: AUDITORÍA MANUAL DEL SISTEMA DE ARCHIVOS (Criterios a, b, d)

**Objetivo:** Realizar un análisis exhaustivo de la estructura del sistema de archivos utilizando herramientas nativas de consola, identificando jerarquías, tamaños y permisos sin escribir scripts.
**Criterios Vinculados:**
*   **a)** Comparación de sistemas de archivos (simulada mediante metadatos).
*   **b/c)** Identificación de estructura y función de directorios.
*   **d)** Uso de comandos/herramientas para localizar información.

### 3.1. Escenario Realista
Como administrador, necesitas auditar la carpeta `/var/log` o una carpeta de proyecto específica (`/home/alumno/proyectos`) para identificar archivos grandes, permisos incorrectos y la jerarquía antes de realizar mantenimiento. No se puede usar código; se debe dominar el terminal.

> **🔍 Auditoría del Tutor:** En entornos reales, los logs pueden consumir todo el disco si no se gestionan manualmente o mediante configuración de herramientas existentes (ej. `logrotate`). Un administrador que domina la consola puede ejecutar estas auditorías en cualquier máquina sin necesidad de desplegar software adicional.

### 3.2. Procedimiento de Ejecución (Comandos)
El alumno debe abrir una terminal y ejecutar las siguientes operaciones, capturando los resultados en archivos de texto para el informe:

1.  **Exploración Jerárquica:** Utilizar el comando `tree` o `find` con opciones específicas para visualizar la estructura del directorio actual (`.`).
    *   *Comando sugerido:* `tree -L 3 -a` (Mostrar hasta 3 niveles, incluyendo ocultos) o `ls -laR`.
2.  **Análisis de Metadatos:** Identificar el inodo y los permisos de un archivo específico usando `stat`.
    *   *Comando sugerido:* `stat /ruta/al/archivo.txt` (Observar campos: Inode, Links, Access, Uid/Gid).
3.  **Búsqueda de Archivos Grandes:** Localizar archivos mayores a 1MB dentro de una jerarquía.
    *   *Comando sugerido:* `find . -type f -size +1M`.

### 3.3. Explicación Técnica de la Lógica (Ampliada)
*   **`tree` vs `ls`:** Mientras que `ls` muestra contenido plano, `tree` construye visualmente el árbol de directorios desde los metadatos del sistema de archivos (Inodos). Esto demuestra comprensión de la estructura jerárquica (Criterio b).
    *   *Detalles Internos:* El comando lee las entradas del directorio padre y recursivamente consulta los hijos, respetando los límites de profundidad (`-L`). No ejecuta procesos externos para leer contenido, solo metadatos.
*   **`stat`:** Proporciona información detallada sobre el "estado" del archivo a nivel de sistema operativo (Criterio d).
    *   *Detalles Internos:* El comando consulta la tabla de inodos del sistema de archivos. Permisos como `rw-r--r--` indican qué usuario y grupo pueden leer o escribir, crucial para la seguridad del sistema.
*   **`find`:** Es una herramienta de búsqueda potente que opera directamente sobre el árbol de directorios (Criterio a/e).
    *   *Detalles Internos:* `find` no necesita cargar todo el directorio en memoria; navega el árbol secuencialmente verificando atributos en tiempo real.

### 3.4. Posibles Errores y Soluciones (Troubleshooting)
1.  **Error: `tree: command not found`**
    *   *Causa:* La utilidad no está instalada por defecto en la distribución mínima de Linux.
    *   *Solución:* Instalarla con el gestor de paquetes (`sudo apt install tree`) o usar el comando nativo `ls -R` como alternativa estándar.
2.  **Error: `Permission denied`**
    *   *Causa:* El usuario no tiene permisos para leer carpetas del sistema (ej. `/etc/shadow`).
    *   *Solución:* Utilizar `sudo` ante el comando o cambiar al directorio de usuario actual (`/home/alumno`) donde se tienen permisos completos.
3.  **Error: Búsqueda infinita en Enlaces Simbólicos**
    *   *Causa:* Algunos sistemas pueden contener bucles en enlaces simbólicos que confunden a las herramientas de navegación.
    *   *Solución:* Utilizar la opción `-P` (no seguir links) o `-L` con cuidado en `find`.

### 3.5. Procedimiento de Compilación y Ejecución
1.  Abrir terminal en el directorio del proyecto.
2.  Ejecutar los comandos de auditoría descritos en el punto 3.2.
3.  **Verificación:** El alumno debe generar un archivo `auditoria.txt` con la salida de estos comandos, demostrando comprensión de la estructura jerárquica (Criterio b).

### 3.6. Reto de Ampliación: Integridad mediante Hashing Manual
**Objetivo del Reto:** Modificar el proceso para calcular el hash SHA-256 de archivos críticos y compararlos con una lista maestra.
*   **Instrucción:** Usar la herramienta `sha256sum`. Generar un archivo de referencia `checksums.txt` para los archivos importantes. Posteriormente, volver a ejecutar el comando sobre los mismos archivos y comparar si alguno ha cambiado (indicando alteración).
*   **Pista:** No uses scripts. Copia y pega la salida en un editor de texto y ejecuta manualmente `sha256sum -c checksums.txt` para verificar integridad.

---

## 4. PRÁCTICA 2: GESTIÓN DE DISCOS Y PARTICIONES (Criterios e, h)

**Objetivo:** Configurar particiones virtuales, formatear sistemas de archivos y evaluar el estado del disco utilizando herramientas nativas del sistema operativo.
**Criterios Vinculados:**
*   **e)** Creación de tipos de particiones/volúmenes (Gestión de almacenamiento).
*   **h)** Instalación y evaluación de utilidades (`smartctl`, `df`).

### 4.1. Escenario Realista
Antes de instalar una actualización grande o realizar una migración, el administrador debe verificar si hay espacio suficiente en las unidades lógicas. El alumno debe manipular discos virtuales dentro de la Máquina Virtual (VM) para simular una ampliación de capacidad.

> **🔍 Auditoría del Tutor:** En virtualización (VMs), los discos suelen ser archivos `.vmdk` o `.qcow2`. Entender cómo el SO ve estos "discos virtuales" como particiones lógicas es clave para gestionar recursos en entornos cloud. Un administrador debe saber agregar un disco a la VM y luego montarlo, sin depender de scripts que lo hagan por él.

### 4.2. Procedimiento de Ejecución (Herramientas)
Uso de herramientas nativas (`fdisk`, `parted`, `lsblk`) para la gestión del almacenamiento.

1.  **Añadido de Disco:** Desde el gestor de VirtualBox/VMware, añadir un nuevo disco duro virtual a la máquina (ej. 2GB). Reiniciar si es necesario.
2.  **Identificación:** Identificar el nuevo dispositivo usando `lsblk` o `fdisk -l`.
    *   *Comando sugerido:* `sudo lsblk` (Listar bloques). Buscar el nuevo disco (`/dev/sdb`).
3.  **Particionado:** Crear una partición primaria en el nuevo disco usando `fdisk`.
    *   *Pasos:* Ejecutar `sudo fdisk /dev/sdb`, crear partición nueva (`n`), tipo primario, aceptar tamaños por defecto y guardar cambios (`w`).
4.  **Formateado:** Crear un sistema de archivos en la partición creada (ej. ext4).
    *   *Comando sugerido:* `sudo mkfs.ext4 /dev/sdb1`.
5.  **Montaje:** Asignar el punto de montaje y conectarlo al sistema de archivos existente.
    *   *Pasos:* Crear carpeta (`mkdir /mnt/disco_nuevo`), montar (`mount /dev/sdb1 /mnt/disco_nuevo`).

### 4.3. Explicación Técnica de la Lógica (Ampliada)
*   **Gestión de Particiones:** Herramientas como `fdisk` modifican la tabla de particiones en el encabezado del disco. Esto prepara al SO para reconocer una nueva unidad lógica (Criterio e).
    *   *Detalles Internos:* El comando escribe en el MBR o GPT (tabla de arranque) indicando dónde empieza y termina cada volumen. Sin esto, el kernel no puede acceder a los datos del dispositivo.
*   **Sistemas de Archivos (`mkfs`):** Formatear es crear la estructura interna para guardar archivos (inodos, superbloques). Aquí se selecciona `ext4`.
    *   *Detalles Internos:* El sistema define cómo se organizan los bloques libres y dónde se guardan los permisos. Diferentes SOs requieren diferentes sistemas (NTFS en Windows, ext4 en Linux).
*   **Montaje:** Conectar la partición física a un directorio accesible del árbol de archivos.
    *   *Detalles Internos:* El kernel actualiza sus tablas internas para que cualquier acceso al path `/mnt/disco_nuevo` redirija las operaciones de lectura/escritura al dispositivo `/dev/sdb1`.

### 4.4. Posibles Errores y Soluciones (Troubleshooting)
1.  **Error: `mount: /mnt/disco_nuevo: mount point does not exist`**
    *   *Causa:* La carpeta destino no fue creada antes de montar el disco.
    *   *Solución:* Usar `mkdir -p /ruta/desinada` antes del comando mount.
2.  **Error: `Device or resource busy`**
    *   *Causa:* El disco ya está montado en algún otro lugar o hay un proceso usando archivos dentro de él.
    *   *Solución:* Verificar con `df -h` y desmontar (`umount`) antes de intentar operaciones de particionado.
3.  **Error: Diferencia de números entre Script y GUI**
    *   *Causa:* El sistema operativo puede reservar espacio para archivos del sistema (ej. "Reserva del sistema" en Windows) que no se muestra en el uso total estándar pero sí en la GUI.
    *   *Solución:* Entender que `df -h` muestra la información tal cual la reporta la API del SO, que puede variar ligeramente según las políticas de caché o reservas.

### 4.5. Procedimiento de Compilación y Ejecución
1.  Asegurar instalación: Verificar disponibilidad de `lsblk`, `fdisk`.
2.  Ejecutar los pasos descritos en el punto 4.2.
3.  **Prueba:** Comparar los resultados del comando `df -h` con la herramienta gráfica "Discos" (Windows) o `disco` (GNOME). Si coinciden, se valida el criterio de localización de información.

### 4.6. Reto de Ampliación: Persistencia de Montaje
**Objetivo del Reto:** Configurar el sistema para que el disco montado se monte automáticamente al reiniciar la máquina virtual.
*   **Instrucción:** Editar el archivo `/etc/fstab` manualmente usando un editor de texto (`nano /etc/fstab`). Añadir una línea con el UUID del disco y el punto de montaje.
*   **Pista:** Usar `blkid` para obtener el UUID antes de editar fstab. Reiniciar la VM y verificar que la carpeta `/mnt/disco_nuevo` existe sin comandos manuales.

---

## 5. PRÁCTICA 3: SISTEMA DE COPIAS DE SEGURIDAD AUTOMATIZADAS (Criterios f, g)

**Objetivo:** Configurar una política de copias de seguridad utilizando herramientas nativas del sistema operativo y planificadores de tareas, permitiendo su restauración lógica.
**Criterios Vinculados:**
*   **f)** Realización y restauración de copias de seguridad (Uso de `tar`, `rsync`).
*   **g)** Planificación y automatización de tareas (Uso de Cron/Task Scheduler).

### 5.1. Escenario Realista
Se requiere una utilidad que, al ejecutarse (o mediante un planificador), comprima la carpeta de "Proyectos" en un archivo `.tar.gz` con fecha y hora en el nombre, asegurando la integridad temporal de los datos.

> **🔍 Auditoría del Tutor:** Aquí aplicamos directamente las métricas RTO/RPO (Recovery Time/Point Objective). Un backup sin restauración probada no es una copia de seguridad válida. El administrador debe configurar herramientas que validen que lo restaurado sea idéntico a lo original usando verificación manual o checksums.

### 5.2. Procedimiento de Ejecución (Herramientas)
Uso de `tar` para compresión y `cron` para automatización. No se escriben scripts, se configuran tareas existentes.

1.  **Compresión Manual:** Generar un archivo comprimido de una carpeta existente usando `tar`.
    *   *Comando sugerido:* `tar -czvf backup_proyectos_$(date +%F).tar.gz ./proyectos/` (Usa variables del shell para fecha automática).
2.  **Verificación de Integridad:** Comprobar que el archivo se puede leer sin corromper.
    *   *Comando sugerido:* `tar -tzvf backup_proyectos_*.tar.gz | head`. (Lista contenido sin extraer).
3.  **Automatización con Cron:** Configurar una tarea programada para ejecutar esta compresión diariamente a las 02:00 AM.
    *   *Pasos:* Editar la tabla de cron del usuario (`crontab -e`). Añadir línea: `0 2 * * * tar -czvf /ruta/backup/proyectos.tar.gz /ruta/proyectos`.

### 5.3. Explicación Técnica de la Lógica (Ampliada)
*   **Compresión (`tar`):** Reduce el tamaño del almacenamiento y agrupa múltiples archivos en uno solo, facilitando su transporte. `gzip` añade compresión adicional.
    *   *Detalles Internos:* El sistema operativo ve esto como un único archivo grande, ocultando la complejidad interna de múltiples archivos pequeños (que suelen ser ineficientes en sistemas de archivos).
*   **Timestamp:** El uso de variables del shell (`$(date)`) garantiza que cada copia tenga un identificador único, evitando sobrescrituras accidentales y permitiendo la recuperación a versiones anteriores (Integridad RA3).
    *   *Detalles Internos:* La cadena de tiempo actúa como una clave primaria en el sistema de archivos del backup. Esto es crucial para la gestión de retención (ej. "mantener backups de los últimos 7 días").
*   **Automatización (Criterio g):** El servicio `cron` ejecuta comandos predefinidos en intervalos regulares sin intervención humana.
    *   *Detalles Internos:* El daemon de cron lee el archivo `/etc/crontab` o la tabla del usuario cada minuto para verificar si hay tareas pendientes que ejecutar.

### 5.4. Posibles Errores y Soluciones (Troubleshooting)
1.  **Error: `BadZipFile` / Corrupción de Tar**
    *   *Causa:* El archivo se interrumpió durante la escritura o fue modificado manualmente con un editor de texto plano.
    *   *Solución:* Verificar que el proceso de escritura no haya sido interrumpido abruptamente (ej. corte de luz). Implementar checksums para validar la integridad al abrir (`tar -tzf`).
2.  **Error: `FileNotFoundError` en Restauración**
    *   *Causa:* La ruta del archivo de backup cambia o se borra antes de ejecutar el script de restauración.
    *   *Solución:* Implementar lógica de "Backup Retention Policy" dentro del sistema operativo (ej. scripts de limpieza en cron) para borrar backups antiguos automáticamente y asegurar que solo haya versiones válidas disponibles.
3.  **Error: Archivos bloqueados (Locked Files)**
    *   *Causa:* En Windows/Linux, si un archivo está abierto por otro proceso, el sistema operativo puede denegar la lectura para copiarlo.
    *   *Solución:* Usar herramientas de copia que manejen archivos abiertos (`rsync --partial`) o implementar un esquema de "Shadow Copy" (VSS en Windows) antes de copiar.

### 5.5. Procedimiento de Compilación y Ejecución
1.  Ejecutar el comando `tar` manual para generar la primera copia.
2.  Configurar el `cron` para la automatización futura.
3.  **Prueba de Restauración:** El alumno debe intentar extraer los archivos en una carpeta temporal (`tar -xzvf backup.tar.gz -C ./RestoreTest`) y verificar que los archivos estén íntegros comparando tamaños o checksums visuales.

### 5.6. Reto de Ampliación: Backup Incremental con `rsync`
**Objetivo del Reto:** Configurar una tarea que solo copie los archivos nuevos o modificados recientemente usando `rsync`.
*   **Instrucción:** En lugar de comprimir todo cada vez, usar `rsync -avz --delete origen/ destino/`. Esto sincroniza solo cambios.
*   **Pista:** Necesitarás verificar la fecha de modificación (`stat`) antes y después para entender qué archivos se han transferido realmente.

---

## 6. EVALUACIÓN Y MATRIZ DE VERIFICACIÓN

Para aprobar este laboratorio, el alumno debe entregar un informe técnico con capturas de pantalla de la terminal y configuraciones realizadas, sin incluir scripts de programación.

| Criterio de Evaluación | Actividad Práctica Vinculada | Evidencia de Cumplimiento (Entregable) |
| :--- | :--- | :--- |
| **a)** Comparar sistemas de archivos | Práctica 1 & 2 (`lsblk`, `stat`) | Salida de comandos mostrando tipos FS y comparación de metadatos en informe. |
| **b/c)** Identificar estructura directorios | Práctica 1 (`tree`, `find` recursivo) | Captura de pantalla del árbol de directorios generado con indentación correcta. |
| **d)** Localizar información (Comandos/Herramientas) | Práctica 2 (`df -h`, `lsblk`) | Comparación visual entre output de terminal y herramienta gráfica "Discos". |
| **e)** Crear particiones/unidades lógicas | Práctica 2 (`fdisk`, `mkfs`) | Confirmación de creación de partición mediante `lsblk` antes y después. |
| **f)** Realizar/Restaurar copias | Práctica 3 (`tar`, extracción manual) | Archivo .tar.gz generado y carpeta restaurada exitosamente tras borrado simulado. |
| **g)** Planificar/Automatizar tareas | Práctica 3 (Configuración de `crontab`) | Captura del archivo `.cron` mostrando la tarea programada correctamente. |
| **h)** Instalar/Evaluar utilidades | Práctica 2 (`smartctl`, `fdisk`) | Uso correcto de herramientas nativas y validación de estado del disco. |

### 6.1. Rúbrica de Calidad Técnica (DAM Focus)
Además de la funcionalidad RA3, se evaluará:
*   **Uso de CLI:** Dominio de los comandos sin errores sintácticos graves.
*   **Documentación:** Explicación clara del proceso en el informe técnico (`README.md`).
*   **Seguridad:** Manejo correcto de permisos (ej. no ejecutar como root innecesariamente, manejo seguro de `sudo`).
*   **Versionado:** Uso de Git para guardar la configuración y los informes, aunque no haya código fuente.

> **🔍 Auditoría del Tutor sobre Evaluación:**
> La entrega debe incluir un archivo `README.md` que explique cómo ejecutar el proceso paso a paso en una nueva máquina. Esto simula la documentación técnica real que se entrega a los clientes o equipos de mantenimiento. Un proceso sin documentación es difícil de replicar y viola las buenas prácticas de ingeniería de software DAM para entornos operativos.

---

## 7. CONCLUSIONES TÉCNICAS PARA EL TUTOR

Este diseño de laboratorio cumple con el requisito de evaluar contenidos del módulo SI (RA3) mediante la gestión directa del sistema operativo, eliminando la dependencia del desarrollo de software. Al usar comandos nativos y herramientas configuradas:
1.  Se refuerza la comprensión de **estructuras de almacenamiento** (no solo visual, sino lógica mediante `stat` e inodos).
2.  Se aplica la **integridad de datos** a través de backups verificables con checksums.
3.  Se integra el conocimiento de **Sistemas Operativos** con competencias profesionales de administración (Cron, Disk Management, FS Audit).

El uso de herramientas nativas (`tar`, `fdisk`, `cron`) permite que estas prácticas sean universales y no dependan de versiones específicas de lenguajes de programación, asegurando que los alumnos aprendan a administrar sistemas en cualquier entorno.

### 7.1. Notas Finales del Coordinador
*   **Seguridad:** Recalca a los alumnos que nunca ejecuten comandos de gestión de sistema (`rm -rf /`, `fdisk`) como usuario administrador en entornos productivos sin revisión previa. El riesgo de "romper" el sistema es real (ej. borrar `/` o particiones críticas).
*   **Escalabilidad:** Si los alumnos terminan pronto, pídeles que consideren cómo manejarían este script si la carpeta a analizar tiene 1 millón de archivos. ¿Qué pasaría con el rendimiento del comando `find`? Esto abre el debate sobre eficiencia algorítmica y gestión de recursos.

**Nota Final para el Alumno:**
Recuerda que la teoría sin práctica es estéril. Te insto a que abras una terminal, uses `ls -li` para ver los inodos, crees enlaces simbólicos, formatee un USB con GPT y ejecutes un backup manual usando `tar`. La comprensión real del RA3 se consolida cuando tocas el hardware y ves cómo el software lo abstrae.
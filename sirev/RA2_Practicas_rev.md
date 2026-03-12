

# GUÍA DE PRÁCTICAS Y LABORATORIOS: RA2 - SISTEMAS INFORMÁTICOS (ENFOQUE ADMINISTRACIÓN)

**Módulo:** Sistemas Informáticos  
**Especialidad:** Desarrollo de Aplicaciones Multiplataforma (DAM)  
**Resultado de Aprendizaje 02 (RA2):** Instala sistemas operativos planificando el proceso e interpretando documentación técnica.  
**Versión del Documento:** 1.2 - Revisada y Purificada por Auditoría de Sistemas Informáticos  
**Autor:** Administrador de Sistemas Senior  

---

## 1. INTRODUCCIÓN Y OBJETIVOS PEDAGÓGICOS

En el perfil profesional, la capacidad de instalar, configurar y mantener entornos operativos es una competencia crítica de infraestructura. Este laboratorio se centra exclusivamente en la **gestión manual y técnica** de los sistemas, eliminando cualquier capa de abstracción mediante scripts o automatización de código. El objetivo es que el alumno domine la interacción directa con el kernel del sistema operativo, la gestión de recursos hardware y la configuración de red sin depender de herramientas de desarrollo de software.

**Objetivos Específicos:**
1.  Realizar auditoría manual de requisitos hardware mediante herramientas nativas del SO.
2.  Configurar entornos virtualizados manualmente (Hypervisor Tipo II) definiendo recursos lógicos.
3.  Ejecutar instalaciones de SO y configuración post-instalación utilizando comandos de consola directos y gestión de paquetes.
4.  Generar documentación técnica manual basada en la inspección visual de logs del sistema.

---

## 2. REQUISITOS PREVIOS DE SOFTWARE Y HARDWARE

Para garantizar la seguridad y reproducibilidad en el entorno de laboratorio, se requiere lo siguiente:

### 2.1 Hardware Host
*   **CPU:** Mínimo 4 núcleos / 8 hilos (Soporte para Virtualización VT-x/AMD-V).
    *   *Explicación Técnica:* La virtualización anidada o la ejecución de múltiples VMs consume recursos de planificación del CPU. Los hilos permiten ejecutar tareas paralelas sin bloquear el hilo principal.
*   **RAM:** Mínimo 16 GB (8 GB dedicados a VMs).
    *   *Explicación Técnica:* Los sistemas modernos son intensivos en memoria. Si la RAM física se agota, el sistema operativo activa el "Swap" o archivo de paginación, reduciendo drásticamente el rendimiento.
*   **Almacenamiento:** SSD de al menos 250 GB libres.
    *   *Explicación Técnica:* Los discos mecánicos (HDD) sufren cuellos de botella en operaciones aleatorias. El SSD reduce el tiempo de arranque del SO y la carga de herramientas.

### 2.2 Software Base (Host)
| Herramienta | Versión Mínima | Propósito |
|-------------|----------------|-----------|
| **Virtualización** | Oracle VirtualBox 7.x o VMware Workstation Pro | Creación de entornos aislados. |
| **Terminal** | PowerShell (Windows) / Bash (Linux) | Ejecución de tareas administrativas directas. |
| **Imágenes ISO** | Ubuntu 22.04 LTS, Windows 10/11 Enterprise | Sistemas Operativos a instalar. |

### 2.3 Utilidades del Sistema
*   **Visor de Eventos:** Para análisis de logs (Windows Event Viewer o `/var/log/syslog` en Linux).
*   **Editor de Texto:** Nano o Vim para edición manual de archivos de configuración críticos.
*   **Gestor de Paquetes:** APT (Debian/Ubuntu) o PowerShell Module Manager (Windows).

---

## 3. PRÁCTICA 01: AUDITORÍA DE REQUISITOS Y PLANIFICACIÓN MANUAL
**Cobertura Criterios:** CE-a, CE-b, CE-c, CE-d  
**Escenario:** Antes de instalar un SO para desarrollo, se debe verificar manualmente si el hardware cumple los requisitos y registrar los datos en una hoja de auditoría.

### 3.1 Descripción Técnica
El alumno debe utilizar las herramientas nativas del sistema operativo anfitrión (Host) o invitado (VM) para extraer información sobre CPU, Memoria RAM y Espacio en Disco. No se permite el uso de scripts para automatizar esta tarea; todo debe ser un proceso manual de consulta y registro.

### 3.2 Procedimiento Técnico
1.  **Identificación del Procesador:**
    *   En Linux: Abrir la terminal y ejecutar el comando `lscpu`. Identificar el número de hilos por socket y el modelo de CPU.
    *   En Windows: Abrir "Administrador de tareas" > Pestaña "Rendimiento" > CPU. Anotar el nombre del procesador y los núcleos lógicos.
2.  **Detección de Memoria RAM:**
    *   En Linux: Ejecutar `free -h` en la terminal para visualizar memoria total, usada e libre en formato legible (Gigabytes).
    *   En Windows: Usar el mismo "Administrador de tareas" > Pestaña "Rendimiento" > Memoria. Anotar la capacidad instalada y la velocidad del bus.
3.  **Análisis de Almacenamiento:**
    *   En Linux: Ejecutar `df -h /` para ver el espacio disponible en la raíz.
    *   En Windows: Abrir "Este equipo" o usar `diskmgmt.msc`. Anotar la capacidad total del disco y el espacio libre restante.

### 3.3 Validación de Requisitos (CE-d)
Comparar los datos obtenidos manualmente con una tabla de requisitos predefinida por el instructor para entornos DAM (Ej: Android Studio requiere 8GB RAM mínima, 4 núcleos CPU).
*   **Caso Apto:** Si todos los valores superan o igualan los mínimos.
*   **Caso No Apto:** Si algún valor es inferior. El alumno debe documentar en el informe final qué componente específico falla y por qué impide la instalación correcta.

### 3.4 Generación de Informe Manual (CE-i)
El alumno debe crear un archivo de texto plano (`reporte_hardware.txt`) manualmente con el editor `nano` o `notepad`. Debe contener:
*   Fecha de la auditoría.
*   Modelo exacto del Hardware detectado.
*   Resultados de la validación (APTO / NO APTO).
*   Justificación técnica si es rechazado.

#### 🔧 Troubleshooting: Posibles Errores y Soluciones
*   **Error:** Comandos no reconocidos (`command not found`).
    *   *Solución:* Verificar que el usuario tiene permisos de ejecución en la terminal o que las herramientas están instaladas en el sistema base. En Linux minimalista, puede requerir instalar `procps` con privilegios administrativos.
*   **Error:** Visualización incorrecta de espacio en disco.
    *   *Solución:* Asegurarse de seleccionar la partición raíz (`/`) y no una unidad montada temporalmente o externa.

#### 🚀 Reto de Ampliación: Escalabilidad Manual
*   **Objetivo:** Comparar dos máquinas físicas diferentes.
*   **Instrucción:** Repetir el procedimiento en un segundo equipo (físico o VM diferente). Crear una tabla comparativa manual en el informe final destacando las diferencias arquitectónicas entre ambos equipos y cuál sería más adecuado para un entorno de desarrollo pesado.

---

## 4. PRÁCTICA 02: VIRTUALIZACIÓN Y DESPLIEGUE DEL SISTEMA OPERATIVO
**Cobertura Criterios:** CE-e, CE-g  
**Escenario:** Creación manual de una Máquina Virtual (VM) configurada para desarrollo y ejecución del SO invitado sin usar herramientas de infraestructura como código.

### 4.1 Descripción Técnica
El alumno debe configurar una VM utilizando exclusivamente la interfaz gráfica del Hypervisor (VirtualBox o VMware). Esto demuestra comprensión de la arquitectura virtualizada y la gestión directa de recursos lógicos sobre el hardware físico. Se instalará Linux (Ubuntu Server) y Windows, comparando requisitos manuales.

### 4.2 Procedimiento Técnico
1.  **Configuración del Hardware Virtual:**
    *   Abrir el gestor de VirtualBox/VMware.
    *   Crear nueva máquina seleccionando "Linux" -> "Ubuntu (64-bit)".
    *   Asignar recursos manualmente:
        *   Memoria RAM: 8192 MB (8 GB).
        *   Procesadores: 4 Núcleos.
        *   Disco Duro: Crear nuevo disco dinámico de 50 GB (formato VDI/VHDX).
    *   Configurar Almacenamiento: Montar la imagen ISO del SO en el controlador IDE/SATA como unidad óptica virtual.

2.  **Configuración de Red:**
    *   Acceder a las propiedades de red de la VM.
    *   Seleccionar "Red Privada" (Host-Only) o "NAT".
    *   Anotar la IP asignada por el DHCP del host para garantizar conectividad futura sin intervención manual.

3.  **Instalación del Sistema Operativo:**
    *   Arrancar la VM desde la ISO montada.
    *   Seguir el asistente de instalación gráfico (Selección de idioma, teclado).
    *   Particionado: Elegir "Borrar disco y usar todo el espacio" para automatizar la partición interna de la VM (no del host).
    *   Crear usuario administrador con contraseña segura.

4.  **Verificación Post-Instalación:**
    *   Una vez instalado, iniciar sesión en el nuevo SO invitado.
    *   Verificar que los recursos asignados son reconocidos por el sistema operativo invitado (ej: `lscpu` y `free -h` en Linux).

#### 🔧 Troubleshooting: Posibles Errores y Soluciones
*   **Error:** La VM no arranca desde la ISO.
    *   *Solución:* Verificar en BIOS/UEFI del Host que la virtualización está habilitada (VT-x/AMD-V). Asegurar que el orden de arranque de la VM priorice la "Unidad Óptica Virtual".
*   **Error:** Falta de conectividad de red dentro de la VM.
    *   *Solución:* Comprobar en el Hypervisor que el adaptador de red está "Conectado" y no solo "Cable conectado". En Linux, verificar con `ip a` si hay IP asignada.

#### 🚀 Reto de Ampliación: Configuración de Red Estática
*   **Objetivo:** Asignar una dirección IP fija manualmente dentro del SO invitado.
*   **Instrucción:** Modificar el archivo de configuración de red del SO (ej: `/etc/netplan/` en Ubuntu o `network connections` en Windows) para asignar la IP `192.168.33.50`. Luego, verificar con `ping` que la VM responde a su nueva dirección desde el Host.

---

## 5. PRÁCTICA 03: GESTIÓN DE APLICACIONES Y ACTUALIZACIONES DEL SISTEMA
**Cobertura Criterios:** CE-e, CE-f, CE-h  
**Escenario:** Mantenimiento del SO instalado y gestión de software adicional mediante ejecución directa de comandos en consola.

### 5.1 Descripción Técnica
El alumno debe simular un escenario de mantenimiento rutinario aplicando parches y verificando la integridad del sistema sin crear archivos ejecutables ni scripts. Se usará el gestor de paquetes nativo y herramientas de línea de comandos para realizar copias de seguridad manuales.

### 5.2 Procedimiento Técnico
1.  **Actualización del Sistema Operativo:**
    *   Abrir la terminal con privilegios administrativos (`sudo`).
    *   Ejecutar `apt-get update` para sincronizar los repositorios locales con los servidores remotos. Verificar que no aparezcan errores de conexión (timeout).
    *   Ejecutar `apt-get upgrade -y` para aplicar las actualizaciones instaladas. Observar el proceso de descarga e instalación en la pantalla.

2.  **Instalación de Software Específico:**
    *   Solicitar al alumno instalar un paquete específico de desarrollo (ej: Java JDK o Git) usando `apt-get install -y openjdk-17-jdk`.
    *   Verificar la instalación ejecutando el comando de versión (`java --version`) y confirmando que la salida coincide con lo esperado.

3.  **Backup Manual de Configuración:**
    *   Crear un directorio específico para backups: `mkdir -p /var/backups/manual_backup`.
    *   Comprimir los archivos de configuración críticos (ej: `/etc/hostname`, `/etc/hosts`) utilizando el comando `tar`. Ejemplo: `tar -czf backup_config.tar.gz /etc/hostname /etc/hosts`.
    *   Verificar que el archivo se ha creado en la carpeta de destino y comprobar su tamaño con `ls -lh`.

4.  **Verificación de Espacio:**
    *   Usar `df -h` para verificar cuánto espacio ocupó el backup y asegurar que no hay riesgos de llenado del disco.

#### 🔧 Troubleshooting: Posibles Errores y Soluciones
*   **Error:** `Permission denied` al ejecutar comandos de actualización.
    *   *Solución:* Asegurarse de usar `sudo` antes del comando. Si el usuario no tiene sudoers, contactar al administrador del sistema host.
*   **Error:** Fallo en la descarga de paquetes (`404 Not Found`).
    *   *Solución:* Los repositorios pueden estar desactualizados o caídos. Revisar el archivo `/etc/apt/sources.list` y cambiar un espejo regional activo si es necesario.

#### 🚀 Reto de Ampliación: Restauración Manual
*   **Objetivo:** Simular la recuperación ante fallo.
*   **Instrucción:** Modificar manualmente uno de los archivos copiados al backup (ej: cambiar una IP en `/etc/hosts`). Intentar restaurarlo ejecutando `tar -xzf backup_config.tar.gz` sobre el directorio original y verificar que el contenido se ha recuperado correctamente reemplazando el archivo modificado.

---

## 6. PRÁCTICA 04: DOCUMENTACIÓN DE PROCESOS Y ANÁLISIS DE LOGS
**Cobertura Criterios:** CE-i, CE-f  
**Escenario:** Generar un informe técnico basado en la lectura manual de los archivos de registro del sistema y las pruebas realizadas.

### 6.1 Descripción Técnica
El RA2 exige documentar procesos. El alumno debe leer manualmente los archivos de log (syslog o Event Viewer) utilizando herramientas nativas de visualización para identificar errores críticos relacionados con la instalación, sin utilizar analizadores externos ni scripts.

### 6.2 Procedimiento Técnico
1.  **Acceso a Logs del Sistema:**
    *   En Linux: Abrir el visor de logs (`/var/log/syslog`) usando un editor de texto como `nano` o `cat /var/log/syslog | less`.
    *   En Windows: Abrir "Visor de Eventos" (eventvwr.msc) y navegar a los registros del Sistema.

2.  **Filtrado Manual de Errores:**
    *   Utilizar el comando `grep` en la terminal para buscar patrones específicos sin crear un script. Ejemplo: `cat /var/log/syslog | grep -i error`.
    *   Analizar las líneas que aparecen. Identificar si se trata de errores de hardware, red o del sistema operativo mismo durante el arranque.

3.  **Redacción del Informe Técnico:**
    *   Crear un documento en formato Markdown (`reporte_instalacion_ra2.md`) manualmente con `nano`.
    *   Incluir una sección "Estado del Sistema".
    *   Si se detectan errores, copiar las líneas relevantes del log al informe y añadir una descripción manual de por qué se considera crítico.
    *   Si no hay errores críticos, documentar que el sistema es estable tras la instalación.

4.  **Verificación de Integridad:**
    *   Comparar el número de entradas de error encontradas en el log con los resultados obtenidos en la Práctica 01 (si aplicara). Documentar cualquier discrepancia.

#### 🔧 Troubleshooting: Posibles Errores y Soluciones
*   **Error:** `Permission denied` al leer `/var/log/syslog`.
    *   *Solución:* Los logs de sistema suelen estar protegidos. Ejecutar el visor o comando con privilegios elevados (`sudo`).
*   **Error:** El archivo no se encuentra (`FileNotFoundError`).
    *   *Solución:* Verificar la estructura del sistema operativo. En Windows, los logs están en el Visor de Eventos, no en archivos `.txt` directos accesibles por usuario normal. Adaptar la búsqueda al entorno específico.

#### 🚀 Reto de Ampliación: Monitoreo de Eventos en Tiempo Real
*   **Objetivo:** Observar la generación de logs durante una acción.
*   **Instrucción:** Mantener abierto el visor de logs o un terminal con `tail -f /var/log/syslog`. Ejecutar un comando que genere actividad (ej: intentar conectar a un servicio no disponible). Observar cómo aparece la entrada en los logs en tiempo real y capturar esa línea para el informe final.

---

## 7. MATRIZ DE EVALUACIÓN Y ENTREGA

Para aprobar este conjunto de prácticas del RA2, el estudiante debe entregar los siguientes entregables verificables:

| Entregable | Descripción Técnica | Criterio Evaluación (CE) | Ponderación |
|------------|---------------------|--------------------------|-------------|
| **1. Formulario Hardware** | Hoja de auditoría manual con valores reales de CPU, RAM y Disco. | CE-a, CE-d | 20% |
| **2. Captura VM Configurada** | Pantallazo del gestor de VirtualBox/VMware mostrando los parámetros definidos (RAM, CPU). | CE-g, CE-e | 30% |
| **3. Comandos Ejecutados** | Registro en texto plano de los comandos usados para actualización y backup (`apt-get`, `tar`). | CE-f, CE-h | 25% |
| **4. Informe de Logs** | Documento manual con capturas o copias de errores encontrados en el sistema. | CE-i | 15% |
| **5. Documentación Manual** | Reflexión escrita sobre las diferencias entre SO Libre/Propietario basada en la experiencia práctica. | CE-c, CE-b | 10% |

### Criterios de Aprobación del RA2
*   El alumno debe ser capaz de ejecutar los comandos y configurar el sistema sin ayuda de scripts preescritos.
*   La documentación generada debe reflejar un entendimiento técnico real, no una copia automática.
*   Se valorará la seguridad: Uso correcto de `sudo`, verificación de permisos al leer logs y manejo seguro de backups manuales.

---

## 8. CONSIDERACIONES DE SEGURIDAD Y ÉTICA (ADMINISTRACIÓN)

1.  **Entorno Aislado:** Nunca realizar estas prácticas en el equipo principal de producción o personal. Usar siempre Virtualización (CE-g).
2.  **Licencias:** Al instalar Windows, verificar que se utilice una imagen ISO válida para evaluación educativa, cumpliendo con la CE-c (Licencias y tipos de licencias).
3.  **Gestión de Datos:** Al realizar backups manuales, no incluir datos sensibles reales (contraseñas, claves SSH) en los archivos comprimidos o copias locales.
    *   *Nota Técnica:* Los directorios `.ssh` suelen contener claves privadas que comprometen la seguridad si se exponen. Excluir estos directorios manualmente al ejecutar el comando `tar`.

---

**FIN DE LA GUÍA DE PRÁCTICAS RA2 (ENFOQUE ADMINISTRACIÓN PURA)**  
*Documento generado bajo la normativa FP DAM y adaptado estrictamente para el perfil de Administración de Sistemas.*
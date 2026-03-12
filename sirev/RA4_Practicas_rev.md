

# GUÍA DE PRÁCTICAS: GESTIÓN DE SISTEMAS OPERATIVOS PARA ENTORNOS DAM (RA4)  
**Módulo Profesional:** Sistemas Informáticos  
**Ciclo Formativo:** Desarrollo de Aplicaciones Multiplataforma (DAM)  
**Resultado de Aprendizaje (RA4):** Gestiona sistemas operativos utilizando comandos y herramientas gráficas y evaluando las necesidades del sistema.  
**Autor:** Auditor de Sistemas Informáticos (Especialista Sin Código)  

---

## 1. INTRODUCCIÓN Y OBJETIVOS DIDÁCTICOS

Esta guía está diseñada para cerrar la brecha entre el desarrollo de software y la infraestructura que lo soporta. Como futuro desarrollador, no solo escribes código; debes garantizar que el entorno donde se ejecuta tu aplicación (Sistema Operativo) sea seguro, eficiente y esté correctamente configurado.

El RA4 exige competencias en administración de sistemas libres y propietarios. En este laboratorio, abordaremos estos contenidos mediante **comandos nativos del sistema operativo** y herramientas gráficas administrativas, permitiendo al alumno comprender la gestión manual y directa de los recursos sin depender de scripts de automatización externos. Se prioriza el conocimiento profundo de las utilidades integradas (CLI y GUI) sobre la creación de software auxiliar.

### Objetivos Específicos:
1.  Crear cuentas y gestionar permisos manualmente mediante comandos nativos o paneles de control (CE a, d).
2.  Controlar servicios y procesos utilizando gestores gráficos y comandos CLI directos (CE c).
3.  Implementar políticas de seguridad básicas mediante editores de política de grupo o configuración local manual (CE b).
4.  Monitorizar el rendimiento y recursos utilizando herramientas nativas del sistema para evaluar viabilidad de despliegue (CE f, h).

---

## 2. REQUISITOS PREVIOS DEL ENTORNO DE ADMINISTRACIÓN

Para cumplir con los requisitos de seguridad y acceso root/administrador necesarios en RA4 sin dañar la máquina física del alumno, se exige un entorno virtualizado.

### Hardware Mínimo:
*   CPU: Dual Core (2 GHz).
*   RAM: 4 GB (Recomendado 8 GB para Virtualización simultánea).
*   Disco Duro: 30 GB libres.

### Software Requerido:
1.  **Hipervisor:** Oracle VirtualBox o VMware Workstation Player.
2.  **Sistemas Operativos Cliente (Máquinas Virtuales):**
    *   **Windows 10/11 Pro** (Entorno Propietario).
    *   **Ubuntu Server LTS** o **Debian** (Entorno Libre/Linux).
3.  **Herramientas de Terminal:**
    *   Símbolo del sistema / PowerShell para Windows.
    *   Terminal nativa con acceso `sudo` para Linux.
4.  **Control de Versiones:** Git instalado localmente para guardar las evidencias (capturas y logs) generadas, no el código fuente.

---

## 3. EJERCICIO 1: PROVISIONAMIENTO MANUAL DE USUARIOS Y PERMISOS (CE a, d)

**Criterios Vinculados:**
*   **CE a):** Se han configurado cuentas de usuario locales y grupos manualmente.
*   **CE d):** Se ha protegido la información mediante el uso de permisos locales y listas de control de acceso (ACLs).

### Escenario Real:
Como administrador del sistema en un entorno DAM, debes provisionar manualmente una cuenta para un nuevo desarrollador con permisos específicos para acceder a carpetas de proyecto. No se permitirán scripts automatizados; se evaluará el conocimiento directo de los comandos y la interfaz gráfica.

> **🔍 ANÁLISIS TÉCNICO PROFUNDO:**  
> En este ejercicio no estamos ejecutando una herramienta externa; estamos manipulando directamente la base de datos local del sistema operativo (SAM en Windows o `/etc/passwd` y `/etc/shadow` en Linux). El concepto clave aquí es el principio de **menor privilegio**: creamos una cuenta con acceso mínimo necesario (`devgroup`) en lugar de darle control total inmediato. Además, estamos gestionando permisos a nivel de sistema de archivos (ACLs), que es más granular y flexible que los permisos tradicionales `rwx`.

### Procedimiento:

#### Parte A: Windows (Comandos y GUI)
1.  Abre PowerShell como **Administrador**.
2.  Ejecuta la secuencia de comandos para crear el usuario. No uses scripts, escribe las líneas directamente en la consola.

**Paso 1: Creación del Usuario**
Ejecuta el siguiente comando sustituyendo `&lt;NombreUsuario>` por tu nombre de prueba (ej: `juan_dev`):
```powershell
net user &lt;NombreUsuario> TempPass123! /add /fullname:"Desarrollador DAM" /description:"Usuario para proyectos de desarrollo"
```

**Paso 2: Asignación al Grupo Administradores**
Ejecuta el siguiente comando para añadirlo al grupo de administradores locales:
```powershell
net localgroup Administrators &lt;NombreUsuario> /add
```

**Paso 3: Configuración de Permisos en Carpeta (GUI)**
1.  Crea la carpeta `C:\ProyectosDAM`.
2.  Haz clic derecho sobre la carpeta > **Propiedades** > Pestaña **Seguridad**.
3.  Pulsa el botón **Editar...** y luego **Añadir...**. Escribe el nombre del usuario creado (`juan_dev`) y acepta.
4.  En la lista de permisos para ese usuario, marca explícitamente **Control total** o **Modificar**. Asegúrate de que la herencia esté habilitada si deseas que subcarpetas hereden estos permisos.

#### Parte B: Linux (Comandos CLI)
1.  Abre la terminal en Ubuntu con `sudo`.
2.  Ejecuta los comandos siguientes manualmente, sin guardarlos en un archivo de script.

**Paso 1: Crear Grupo y Usuario**
```bash
# Creación del grupo devgroup
sudo groupadd devgroup

# Creación del usuario y asignación al grupo (ej: juan_dev)
sudo useradd -m -g devgroup -s /bin/bash juan_dev

# Asignación de contraseña temporal
echo "juan_dev:TempPass123!" | sudo chpasswd
```

**Paso 2: Configuración de Permisos y ACLs (CE d)**
1.  Crea la ruta del proyecto:
    ```bash
    sudo mkdir -p /home/juan_dev/proyectos_dam
    ```
2.  Asigna propietario y grupo, y establece permisos base:
    ```bash
    sudo chown -R juan_dev:devgroup /home/juan_dev/proyectos_dam
    sudo chmod -R 750 /home/juan_dev/proyectos_dam
    ```
3.  Verifica la instalación de ACLs y aplica permisos granulares si es necesario:
    ```bash
    # Instalar herramientas acl si no existen (solo una vez)
    sudo apt install acl
    
    # Aplicar regla específica
    sudo setfacl -m u:juan_dev:rwx /home/juan_dev/proyectos_dam
    ```

### Explicación Técnica de la Lógica:
*   **Seguridad (CE b):** La creación manual asegura que el alumno entienda qué parámetros se están enviando al kernel del SO. En Windows, `net user` interactúa con SAM. En Linux, `useradd` modifica archivos de texto planos en `/etc`.
    *   *[NOTA DEL AUDITOR]:* En un entorno real, nunca pasarías contraseñas como parámetros de línea de comandos (`echo "usuario:pass"`) porque quedan guardadas en el historial del shell. Deberíamos usar `passwd &lt;usuario>` para que el sistema solicite la contraseña de forma segura.
*   **Herencia y ACLs:** En ambos sistemas, el comando configura la carpeta raíz del proyecto. En Linux (`chmod 750`), se garantiza que solo el dueño y el grupo tengan acceso de escritura. En Windows, los permisos en pestaña "Seguridad" interactúan con ACLs.
    *   *[NOTA DEL AUDITOR]:* El comando `setfacl` en Linux requiere la herramienta `acl` instalada (`sudo apt install acl`). Sin ella, el script fallará silenciosamente o dará error.

### Compilación y Ejecución:
*   **Windows:** Abre PowerShell como Admin -> Introduce los comandos uno a uno. Verifica con `net user &lt;NombreUsuario>`.
    *   *[NOTA DEL AUDITOR]:* El error más común en Windows es la política de ejecución si intentas usar scripts, pero al escribir comandos directos esto no aplica.
*   **Linux:** Guarda como `.sh` solo para referencia personal (no se evalúa), ejecuta los comandos uno a uno. Verifica con `id &lt;NombreUsuario>`.

---

### ⚠️ ZONA DE TROUBLESHOOTING Y ERRORES COMUNES (EJERCICIO 1)

| Error / Comportamiento | Causa Probable | Solución Propuesta |
| :--- | :--- | :--- |
| **PowerShell: "El usuario ya existe"** | El nombre del usuario fue reutilizado de un ejercicio anterior. | Ejecuta `net user &lt;Usuario> /delete` antes de crearlo, o elige otro nombre único. |
| **Linux: `sudo: groupadd: command not found`** | Herramientas administrativas no instaladas en la ISO mínima. | Verifica que estás usando una distribución completa (`ubuntu-desktop-server`). En algunas distros minimalistas falta el paquete `base-files`. |
| **Windows: "Acceso denegado"** | No se ejecutó PowerShell como Administrador real (UAC bloqueado). | Asegúrate de hacer clic derecho en PowerShell y seleccionar **"Ejecutar como administrador"**. |
| **Linux: `chown` cambia propietario pero no grupo** | El usuario no existe o el grupo es incorrecto. | Verifica con `id &lt;Usuario>` y `getent group devgroup`. Asegúrate de crear el grupo antes que el usuario si se especifica `-g`. |
| **Permisos ACLs no surten efecto en Windows** | La carpeta tiene permisos heredados explícitos que sobrescriben. | Limpia los permisos heredados o modifica la regla específica con `icacls` antes de usar la GUI. |

---

### 🚀 RETO DE AMPLIACIÓN (NIVEL AVANZADO)
**Objetivo:** Añadir funcionalidad de auditoría manual y borrado seguro.
1.  **Ampliación Windows:** Usa el comando `Get-LocalUser` en PowerShell para listar todos los usuarios y verifica manualmente cuáles pertenecen al grupo Administradores usando `net localgroup Administrators`. Documenta esta lista en un archivo de texto `.txt`.
2.  **Ampliación Linux:** Usa el comando `ls -la /home/&lt;Usuario>` para verificar que los permisos sean exactamente `-rwx------` (700) o lo configurado, y confirma la propiedad con `stat &lt;archivo>`.

---

## 4. EJERCICIO 2: GESTIÓN DE SERVICIOS Y SEGURIDAD (CE b, c)

**Criterios Vinculados:**
*   **CE b):** Se ha asegurado el acceso al sistema mediante directivas de cuenta y contraseñas.
*   **CE c):** Se han identificado, arrancado y detenido servicios y procesos manualmente.

### Escenario Real:
Antes de desplegar una aplicación backend (ej. Tomcat o Java Spring Boot), debes asegurarte de que los puertos necesarios estén libres y que el servicio no se inicie automáticamente si es opcional para evitar consumo de recursos innecesarios en el entorno de desarrollo.

> **🔍 ANÁLISIS TÉCNICO PROFUNDO:**  
> Aquí entramos en la gestión del ciclo de vida de procesos. Un *servicio* en Windows o un *daemon* en Linux son procesos que tienen prioridad y suelen ejecutarse con privilegios elevados. Entender esto es vital para el desarrollo: si tu aplicación falla al iniciar, puede ser porque otro servicio está "secuestrando" el puerto (ej. 80) o porque el servicio de red no ha terminado de arrancar completamente antes de que tu app intente conectarse.

### Procedimiento:

#### Parte A: Monitorización y Gestión de Procesos
No se permite uso de librerías externas (`psutil`, etc.). Se debe utilizar la consola del sistema operativo o herramientas gráficas nativas.

**Windows:**
1.  Abre el **Administrador de Tareas** (Ctrl + Shift + Esc) -> Pestaña **Servicios**.
2.  Busca servicios críticos como `WinDefend` o `Spooler`. Anota su estado (Ejecutando, Detenido).
3.  Para detener un servicio mediante consola:
    ```powershell
    # Detener el servicio Spooler (Impresión) temporalmente
    net stop Spooler
    
    # Verificar que se ha detenido
    sc query Spooler
    ```

**Linux:**
1.  Abre la terminal y utiliza `systemctl` para gestionar servicios.
2.  Para verificar si un servicio como `nginx` está activo:
    ```bash
    systemctl status nginx
    ```
3.  Para detenerlo:
    ```bash
    sudo systemctl stop nginx
    ```

#### Parte B: Configuración de Políticas de Contraseña (Windows GPO)
Para cumplir el **CE b**, utilizaremos herramientas nativas del sistema para aplicar directivas locales, evitando scripts de registro.

1.  Abre `secpol.msc` (Directiva de Seguridad Local).
2.  Navega a: **Políticas de Cuenta** > **Directiva de Contraseña**.
3.  Modifica manualmente los valores:
    *   "Longitud mínima de contraseña": Configura en `8`.
    *   "Bloquear cuenta después de intentos fallidos": Configura en `5`.
4.  Aplica los cambios y verifica con el comando:
    ```powershell
    net accounts
    ```

### Explicación Técnica de la Lógica:
*   **Gestión de Procesos (CE c):** El uso nativo del SO permite entender cómo interactúa el kernel sin intermediarios. En Windows, `sc` y `net` son herramientas legacy robustas. En Linux, `systemctl` es el estándar moderno (Systemd).
    *   *[NOTA DEL AUDITOR]:* El uso de comandos como `net stop` requiere privilegios de administrador/root. Si falla, verifica tu nivel de acceso.
*   **Directivas (CE b):** La edición manual en `secpol.msc` asegura que el alumno entienda la jerarquía de políticas de seguridad del SO sin depender de archivos `.reg`.

### Compilación y Ejecución:
1.  Ejecute los comandos `net accounts` y `systemctl status` y capture las capturas de pantalla como evidencia.
2.  En Windows, asegúrese de ejecutar PowerShell como Admin para detener servicios.

---

### ⚠️ ZONA DE TROUBLESHOOTING Y ERRORES COMUNES (EJERCICIO 2)

| Error / Comportamiento | Causa Probable | Solución Propuesta |
| :--- | :--- | :--- |
| **Windows: "Access Denied"** al detener servicio | El script/comando se ejecutó sin privilegios elevados. | Abre PowerShell como **Administrador**. Algunos servicios requieren permisos específicos para ser consultados o detenidos. |
| **Linux: `systemctl` no reconoce el servicio** | Nombre del servicio incorrecto o instalación incompleta. | Usa `systemctl list-units --type=service` para listar todos los disponibles y encontrar el nombre correcto (ej: `apache2` vs `httpd`). |
| **Comando net no encontrado en PowerShell puro** | Comandos legacy de CMD no disponibles en PowerShell puro o falta acceso. | Ejecuta `cmd /c net accounts` dentro del script si falla, o usa PowerShell cmdlets como `Get-LocalGroupMember`. |
| **Servicio se reinicia automáticamente** | El servicio está configurado para "Reiniciar en fallo". | Verifica la configuración de inicio del servicio en el Administrador de Servicios o con `systemctl edit &lt;servicio>`. |

---

### 🚀 RETO DE AMPLIACIÓN (NIVEL AVANZADO)
**Objetivo:** Gestión manual de reinicios y auditoría.
1.  **Ampliación Windows:** Utiliza el Administrador de Servicios para cambiar el "Tipo de inicio" de un servicio a "Desactivado". Luego verifica que no se ejecute tras un reinicio usando `sc qc &lt;Servicio>`.
2.  **Ampliación Linux:** Usa `systemctl disable &lt;servicio>` para prevenir que arranque con el sistema y verifícalo con `systemctl is-enabled &lt;servicio>`.

---

## 5. EJERCICIO 3: DIAGNÓSTICO DE RED MANUAL (CE e, f)

**Criterios Vinculados:**
*   **CE e):** Se han utilizado comandos para realizar tareas básicas de configuración y administración del sistema.
*   **CE f):** Se ha monitorizado el sistema.

### Escenario Real:
El equipo de desarrollo reporta lentitud en la conexión a la base de datos. Debes diagnosticar si es un problema de red (TCP/IP, Puertos) o del sistema operativo (Congestión de CPU/RAM).

> **🔍 ANÁLISIS TÉCNICO PROFUNDO:**  
> La red es donde ocurren los errores más silenciosos en desarrollo. Un error de conexión no siempre es "no hay servidor"; puede ser un DNS mal configurado, un firewall bloqueando el puerto, o una saturación del socket. Este ejercicio simula lo que haría un administrador usando herramientas nativas para obtener datos sin depender de scripts externos.

### Procedimiento:
Se utilizarán las utilidades de red integradas en cada sistema operativo.

#### Creación de Informe de Diagnóstico (Manual)
Crea un documento de texto y rellena los siguientes apartados ejecutando los comandos correspondientes en la terminal.

**Paso 1: Configuración IP y DNS (CE e, h)**
*   **Windows:** Ejecuta `ipconfig /all`. Copia la información del adaptador Ethernet/Wi-Fi (Dirección IPv4, Máscara, Puerta de enlace, DNS).
*   **Linux:** Ejecuta `ip addr show` o `ifconfig -a`. Anota la IP y el estado del interfaz.

**Paso 2: Resolución de DNS**
*   Ejecuta `ping google.com` (Windows/Linux) o `nslookup google.com`.
    *   Si falla, cambia temporalmente a un DNS público en la configuración de red del adaptador (`8.8.8.8`) y repite.

**Paso 3: Verificación de Puertos (CE e)**
*   **Windows:** Usa el comando `telnet` o PowerShell para probar conectividad al puerto local (ej: 5432 para PostgreSQL):
    ```powershell
    Test-NetConnection -ComputerName localhost -Port 5432
    ```
*   **Linux:** Usa `nc` (netcat) si está disponible, o `telnet`:
    ```bash
    nc -zv localhost 5432
    # O alternativa con netstat/ss
    ss -tulpn | grep 5432
    ```

**Paso 4: Análisis de Conectividad**
*   Ejecuta `tracert google.com` (Windows) o `traceroute google.com` (Linux). Analiza en qué salto se pierde la conexión si es necesario.

### Explicación Técnica:
*   **Conexión de Sistemas (CE h/e):** El uso nativo valida la capa de red (DNS) y la capa de transporte (Puertos). Esto es vital para evaluar si un servidor puede alojar una aplicación web o base de datos.
    *   *[NOTA DEL AUDITOR]:* `Test-NetConnection` o `nc` intentan conectar a `localhost`. Si el servicio corre en otra IP, debes modificar la dirección objetivo.

### Compilación y Ejecución:
1.  Abre la terminal.
2.  Ejecute los comandos de diagnóstico uno por uno.
3.  **Entrega:** El alumno debe capturar la salida del comando en el documento final como evidencia de que ha diagnosticado su red manualmente.

---

### ⚠️ ZONA DE TROUBLESHOOTING Y ERRORES COMUNES (EJERCICIO 3)

| Error / Comportamiento | Causa Probable | Solución Propuesta |
| :--- | :--- | :--- |
| **Comando: `ping` falla** | El puerto está cerrado o el firewall está bloqueando la conexión. | Verifica que el servicio (ej. MySQL, Apache) esté corriendo antes de ejecutar el script. Usa `telnet IP Puerto` para probar manualmente. |
| **Linux: `ifconfig` no encontrado** | Herramientas clásicas (`net-tools`) desinstaladas en distros modernas. | Usa `ip addr show` en lugar de `ifconfig`. El comando es nativo del paquete `iproute2`. |
| **Windows: `ipconfig /all` muestra IPv6 por defecto** | La red está configurada para preferir IPv6 sobre IPv4. | Verifica que tu aplicación esté escuchando en `0.0.0.0` o `127.0.0.1` (IPv4) y no solo en `::1`. |
| **DNS falla aunque internet funciona** | El DNS configurado está lento o caído, pero el proxy funciona. | Prueba cambiar temporalmente a un DNS público (`8.8.8.8`) para ver si es problema de resolución local. |

---

### 🚀 RETO DE AMPLIACIÓN (NIVEL AVANZADO)
**Objetivo:** Escaneo manual y reporte CSV.
1.  **Ampliación Windows:** Utiliza `netstat -ano` para listar todos los puertos abiertos. Identifica manualmente el PID correspondiente al puerto 80 o 443 y busca ese proceso en el Administrador de Tareas.
2.  **Ampliación Linux:** Usa `ss -tulpn` para listar *todos* los programas que están escuchando puertos y mostrar su PID asociado, permitiendo identificar qué proceso está "ocupando" el puerto 80 antes de intentar arrancar tu servidor web.

---

## 6. EJERCICIO 4: EVALUACIÓN DE RECURSOS PARA DESARROLLO (CE h, g)

**Criterios Vinculados:**
*   **CE h):** Se han evaluado las necesidades del sistema informático en relación con el desarrollo de aplicaciones.
*   **CE g):** Se han instalado y evaluado utilidades para mantenimiento y optimización.

### Escenario Real:
Antes de solicitar hardware a la empresa para un nuevo entorno de producción, debes generar un informe manual que indique si el equipo cumple los requisitos mínimos para compilar y ejecutar aplicaciones Java/Kotlin pesadas (mínimo 4GB RAM, CPU moderna).

> **🔍 ANÁLISIS TÉCNICO PROFUNDO:**  
> Aquí aplicamos la evaluación de capacidad (*Capacity Planning*). Como desarrolladores DAM, no basta con que el código funcione; debe funcionar bajo carga. Este ejercicio utiliza herramientas nativas del SO (`Task Manager`, `top`, `df`) para tomar decisiones basadas en métricas reales (Carga CPU, Uso RAM, Espacio Disco).

### Procedimiento:
No se permite generar scripts de auditoría. Se debe utilizar la interfaz gráfica o comandos directos para obtener los datos y reportarlos.

#### Auditoría de Hardware Manual

**Windows:**
1.  Abre el **Administrador de Tareas** (Ctrl + Shift + Esc) > Pestaña **Rendimiento**.
2.  Captura las gráficas de CPU, Memoria y Disco.
3.  Anota:
    *   Uso total de RAM (Total vs Disponible).
    *   Número de núcleos lógicos y físicos.
    *   Espacio libre en disco C:.

**Linux:**
1.  Abre la terminal y ejecuta los siguientes comandos para obtener métricas equivalentes:
    ```bash
    # Memoria RAM (CE h)
    free -m
    
    # CPU (Carga actual)
    top -b -n 1 | head -20
    
    # Disco Duro (Espacio disponible) (CE g)
    df -h /
    
    # Información detallada del sistema
    lscpu
    ```

#### Evaluación de Necesidades (RA4h)
Basado en los datos obtenidos:
1.  Si la RAM disponible es menor a 4GB, marca el estado como "No Cumple".
2.  Si el disco tiene menos del 20% libre, marca el estado como "Requiere Limpieza".

### Explicación Técnica de la Lógica:
*   **Evaluación de Necesidades (CE h):** El alumno no solo lee datos, sino que los interpreta para validar requisitos (`check_development_requirements` manual). Esto simula un proceso de *Capacity Planning*.
    *   *[NOTA DEL AUDITOR]:* En Linux, el path `/` es la raíz. Los comandos `free`, `df`, y `top` son estándar en cualquier distribución Unix-like.

### Compilación y Ejecución:
1.  Abre las herramientas nativas (Task Manager o Terminal).
2.  Ejecute los comandos de diagnóstico.
3.  **Entrega:** El alumno debe capturar la salida del comando o una captura de pantalla como evidencia de que ha evaluado su máquina virtual.

---

### ⚠️ ZONA DE TROUBLESHOOTING Y ERRORES COMUNES (EJERCICIO 4)

| Error / Comportamiento | Causa Probable | Solución Propuesta |
| :--- | :--- | :--- |
| **Windows: Task Manager muestra RAM incorrecta** | La máquina virtual está limitando la asignación de recursos. | Verifica la configuración de la VM en VirtualBox/VMware (asignar más RAM a la VM, no solo al anfitrión). |
| **Linux: `free -m` muestra 0 disponible** | El sistema está bajo carga extrema o hay fugas de memoria. | Ejecuta `top` y ordena por uso de memoria (`Shift + M`) para ver qué proceso consume más. |
| **Valores de CPU incorrectos** | La máquina virtual está limitando los recursos asignados a la CPU. | Verifica configuración del hipervisor (asignar vCPUs reales). |
| **Comandos de disco no encontrados** | Herramientas básicas desinstaladas en ISO minimalista. | Usa `lsblk` como alternativa para ver particiones y tamaños si falta el paquete `util-linux`. |

---

### 🚀 RETO DE AMPLIACIÓN (NIVEL AVANZADO)
**Objetivo:** Generación de informe manual y Alerta Automática.
1.  **Ampliación Linux:** Añade una función al script Bash que, si el disco supera el 90% de uso (`df`), envíe un correo electrónico automático o escriba en un archivo de log `/var/log/disk_alert.log` avisando del problema (usando `mail` o `logger`).
2.  **Ampliación Windows:** Utiliza la herramienta "Monitor de Recursos" para ver el historial de uso de disco por proceso en los últimos minutos y documenta qué aplicación consumió más I/O.

---

## 7. PROCEDIMIENTOS DE ENTREGA Y VERIFICACIÓN

Para garantizar el cumplimiento de los Criterios de Evaluación, el alumno deberá entregar un repositorio Git con la siguiente estructura:

1.  **Documentación (`README.md`):**
    *   Explicación de cómo se ejecutaron los comandos y herramientas gráficas.
    *   Capturas de pantalla (Logs) donde se vea la creación del usuario, configuración de permisos y métricas de recursos.
2.  **Evidencias:**
    *   Carpeta `/evidencias`: Contiene archivos `.png` o `.txt` con la salida de comandos CLI (`ipconfig`, `net user`, `top`).
3.  **Pruebas de Aceptación (Checklist RA4):**

| Criterio | Prueba de Verificación | Estado (OK/NO) |
| :--- | :--- | :___|
| **CE a** | Creación manual de usuario y grupo en SO (Win/Linux). | _______ |
| **CE b** | Aplicación manual de políticas de contraseña. | _______ |
| **CE c** | Identificación manual de procesos activos y servicios. | _______ |
| **CE d** | Permisos ACLs aplicados a carpeta compartida. | _______ |
| **CE e** | Uso correcto de comandos CLI (`ipconfig`, `net user`). | _______ |
| **CE f** | Logs o salida de monitorización generada manualmente. | _______ |
| **CE g** | Utilidad de mantenimiento (limpieza/disco) incluida. | _______ |
| **CE h** | Informe final manual de evaluación de hardware para DAM. | _______ |

---

## 8. CONCLUSIONES DEL TUTOR

Este laboratorio integra los conocimientos teóricos del RA4 con la práctica profesional real, eliminando la dependencia de scripts de desarrollo. Al ejecutar comandos nativos y configurar el SO manualmente, el alumno no solo aprende a "administrar" Windows o Linux, sino que entiende cómo el entorno operativo afecta al ciclo de vida del desarrollo (DAM).
*   **Seguridad:** Se refuerza que los permisos y usuarios son la primera línea de defensa.
*   **Gestión Directa:** Se demuestra que las tareas críticas deben poder realizarse sin intermediarios de código.
*   **Evaluación:** Se aprende a tomar decisiones basadas en datos (logs, recursos) antes de desplegar aplicaciones utilizando herramientas nativas.

**Nota Final:** Recuerde siempre trabajar sobre máquinas virtuales para evitar daños en el sistema operativo anfitrión al modificar permisos o servicios críticos durante la práctica.
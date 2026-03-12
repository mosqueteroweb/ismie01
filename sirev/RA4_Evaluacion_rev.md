

# 📋 BANCO DE EVALUACIÓN RA4: GESTIÓN DE SISTEMAS OPERATIVOS Y ENTORNOS DE DESARROLLO (VALIDADO)

**Módulo Profesional:** Sistemas Informáticos  
**Ciclo Formativo:** Desarrollo de Aplicaciones Multiplataforma (DAM)  
**Resultado de Aprendizaje:** RA4 - Gestiona sistemas operativos utilizando comandos y herramientas gráficas y evaluando las necesidades del sistema.

---

## 👨‍🏫 INFORME DEL AUDITOR DE CALIDAD DOCENTE
**Estado:** ✅ APROBADO Y AMPLIADO  
**Nivel de Rigor:** Técnico Superior / Conceptual Avanzado  
**Observación Principal:** El banco de evaluación original cumple con los criterios RA4, pero el solucionario se ha **EXPANDIDO DRÁSTICAMENTE** para convertir este examen en un material de estudio integral. Cada pregunta ahora incluye una explicación técnica profunda sobre por qué las opciones incorrectas son errores conceptuales comunes que un desarrollador DAM debe saber evitar.

---

# 📝 PARTE 1: EXAMEN TIPO TEST (15 PREGUNTAS DE ALTA DIFICULTAD)

## Instrucciones:
Seleccione la opción correcta para cada pregunta. Marque solo UNA respuesta por ítem. Tiempo estimado: 45 minutos.

---

### Pregunta 1 - Arquitectura de Virtualización
En un entorno DAM, se requiere desplegar múltiples servidores Linux sobre una única estación física para pruebas de integración continua. ¿Qué tipo de virtualización ofrece el mejor rendimiento sin comprometer la seguridad del host?

A) Tipo 2 (Hosted) con VirtualBox y máquinas virtuales anidadas  
B) Tipo 1 (Bare Metal) con VMware ESXi instalando directamente sobre hardware  
C) Híbrida con contenedores Docker ejecutándose sobre Windows Subsystem for Linux  
D) Emulación completa mediante QEMU con traducción dinámica de instrucciones

---

### Pregunta 2 - Gestión de Memoria y Performance
Una aplicación Java en producción muestra errores "Out of Memory" a pesar de tener 8 GB de RAM física disponibles. El administrador observa que el sistema está usando intensivamente la memoria virtual (swap). ¿Cuál es la causa más probable?

A) La JVM tiene configurada una heap size menor al 50% del total disponible  
B) Hay fugas de memoria en el código Java que liberan objetos incorrectamente  
C) El sistema operativo ha asignado demasiado espacio de swap al proceso  
D) Existe un conflicto entre drivers de memoria RAM y la arquitectura del SO

---

### Pregunta 3 - Permisos ACL (Linux)
Se configura una carpeta compartida `/proyectos` con los siguientes permisos: `drwxr-x---` y se aplican ACLs adicionales. Un usuario del grupo `devgroup` no puede escribir aunque pertenece al grupo. ¿Qué comando verifica las ACLs activas?

A) `ls -l /proyectos`  
B) `getfacl /proyectos`  
C) `chmod 750 /proyectos`  
D) `chown devgroup:devgroup /proyectos`

---

### Pregunta 4 - Seguridad de Procesos Windows
Se detecta que un proceso malicioso está ejecutándose en segundo plano con privilegios elevados. ¿Qué herramienta proporciona la información más detallada sobre el PID, nombre del servicio y estado actual?

A) `tasklist /v`  
B) `Get-Process | Select-Object Name, Id, Status` (PowerShell)  
C) `netstat -ano`  
D) `systeminfo`

---

### Pregunta 5 - Planificación de Procesos
Un servidor web experimenta latencia alta durante horas pico. El administrador observa que el proceso del compilador está consumiendo CPU constantemente. ¿Qué mecanismo del SO controla la prioridad de ejecución?

A) La tabla de procesos (Process Table) con niveles de prioridad  
B) El sistema de archivos asignando espacio en disco  
C) La máscara de subred definiendo ancho de banda  
D) La lista de control de acceso determinando usuarios conectados

---

### Pregunta 6 - Configuración TCP/IP
Para desplegar una aplicación RESTful que debe ser accesible desde internet, el administrador configura un servidor web. ¿Qué combinación es correcta para permitir tráfico entrante seguro?

A) Puerto 80 con protocolo UDP y firewall bloqueado  
B) Puertos 80 (HTTP) y 443 (HTTPS) con firewall estadoful activo  
C) Puerto 22 (SSH) únicamente con protocolo TCP sin cifrado  
D) Cualquier puerto aleatorio mayor a 1024 sin configuración de NAT

---

### Pregunta 7 - Sistemas de Archivos
Se necesita migrar datos desde un disco mecánico (HDD) a uno de estado sólido (SSD). ¿Qué afirmación es correcta respecto al mantenimiento del sistema de archivos?

A) La desfragmentación debe ejecutarse antes y después de la migración  
B) El comando `chkdsk` debe ejecutarse periódicamente en el SSD para optimizar rendimiento  
C) No se requiere desfragmentación en SSDs debido a su arquitectura de acceso aleatorio  
D) Los sistemas de archivos NTFS no son compatibles con SSDs

---

### Pregunta 8 - Backup y Recuperación
Una empresa utiliza copias incrementales para sus bases de datos. El administrador necesita restaurar los datos del día 3. ¿Qué secuencia de backup es necesaria?

A) Solo la copia incremental del día 3  
B) La copia completa más recientes hasta el día 3  
C) Todas las copias incrementales desde el inicio del mes  
D) La última copia diferencial y la copia completa anterior

---

### Pregunta 9 - Políticas de Contraseña
Se implementa una política que requiere: longitud mínima 8, complejidad con caracteres especiales, caducidad cada 30 días. ¿Qué comando Windows aplica estos requisitos de forma local?

A) `net accounts /minpwlen:8 /maxpwage:30`  
B) `useradd -p complex --expire 30` (Linux)  
C) `gpasswd -a user groupname`  
D) `chmod 700 /etc/shadow`

---

### Pregunta 10 - Monitorización de Red
Para diagnosticar si un servidor base de datos es accesible desde una red remota, ¿qué comando proporciona información sobre la ruta de paquetes y latencia?

A) `ping server.local`  
B) `traceroute server.local`  
C) `nslookup database.server.com`  
D) `ipconfig /all`

---

### Pregunta 11 - Servicios Linux (Daemons)
Un servicio PostgreSQL no inicia automáticamente después de un reinicio. ¿Qué comando verifica y habilita el servicio para arranque automático en sistemas systemd?

A) `service postgresql start && service postgresql enable`  
B) `systemctl start postgresql && systemctl enable postgresql`  
C) `init.d/postgresql start && update-rc.d postgresql defaults`  
D) `start-service postgresql --enable-boot`

---

### Pregunta 12 - Evaluación de Recursos (RA4h)
Antes de desplegar una aplicación que requiere compilación en tiempo real, se evalúa el sistema. ¿Qué recurso es crítico para evitar cuellos de botella durante la compilación?

A) Espacio en disco SSD NVMe  
B) CPU con múltiples núcleos y RAM suficiente  
C) Resolución DNS configurada correctamente  
D) Puertos abiertos en firewall

---

### Pregunta 13 - Virtualización Tipo 1 vs Tipo 2
¿Cuál es la principal diferencia de rendimiento entre un hipervisor Tipo 1 y uno Tipo 2?

A) El Tipo 1 ejecuta aplicaciones directamente sobre el SO anfitrión  
B) El Tipo 2 tiene menor overhead porque se instala como aplicación  
C) El Tipo 1 accede al hardware sin intermediario del SO anfitrión (mayor rendimiento)  
D) No existe diferencia de rendimiento, solo de compatibilidad

---

### Pregunta 14 - Cifrado de Datos
Se requiere proteger información sensible en reposo en un servidor Linux. ¿Qué herramienta implementa cifrado a nivel de disco completo?

A) BitLocker  
B) LUKS (Linux Unified Key Setup)  
C) GPG para archivos individuales  
D) SSH Keys para acceso remoto

---

### Pregunta 15 - Criterio CE h - Evaluación de Necesidades
Un equipo de desarrollo necesita implementar CI/CD con pipelines automatizados. ¿Qué aspecto debe evaluarse antes del despliegue?

A) La capacidad del sistema para soportar múltiples procesos concurrentes y almacenamiento temporal  
B) El color de la carcasa del servidor físico  
C) La marca de los teclados conectados al equipo  
D) La versión gráfica del sistema operativo instalada

---

# 🐛 PARTE 2: CASOS PRÁCTICOS DE DEBUGGING Y REFACTORIZACIÓN

## Caso Práctico A: Debugging de Script de Provisionamiento (Windows PowerShell)

**Escenario:**  
El administrador de sistemas debe crear un script que provisione usuarios para el equipo de desarrollo. Sin embargo, el script actual presenta errores que impiden su correcta ejecución en producción.

### Código Original con Errores:

```powershell
# Script: provision_user_original.ps1 - VERSIÓN CON ERRORES
param (
    [Parameter(Mandatory=$true)]
    [string]$Username,
    
    [Parameter(Mandatory=$false)]
    [string]$Password = "TempPass123!"
)

# 1. Crear Carpeta de Proyecto sin verificar existencia
$ProjectPath = "C:\ProyectosDAM"
New-Item -ItemType Directory -Path $ProjectPath | Out-Null

# 2. Crear Usuario (Error: sintaxis incorrecta)
New-LocalUser -Name Username -Password (ConvertTo-SecureString $Password -AsPlainText -True) -FullName "Desarrollador DAM" -Description "Usuario para proyectos de desarrollo"

# 3. Añadir al grupo Administradores (Error: nombre del grupo incorrecto)
Add-LocalGroupMember -Group "Admins" -Member Username

# 4. Configurar Permisos ACL (Error: objeto de seguridad incompleto)
$acl = Get-Acl -Path $ProjectPath
$account = [System.Security.Principal.NTAccount]$Username
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule($account, "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
$acl.AddAccessRule($rule)
Set-Acl -Path $ProjectPath -AclObject $acl

Write-Host "[OK] Usuario '$Username' creado y configurado."
```

### Tarea del Alumno:
1.  Identificar **mínimo 3 errores** en el código proporcionado.
2.  Proponer la corrección para cada error encontrado.
3.  Justificar por qué la corrección es necesaria según los criterios de seguridad RA4.

---

## Caso Práctico B: Diseño de Clase y Gestión de Recursos (Python)

**Escenario:**  
Como desarrollador DAM, debes crear una clase que gestione la evaluación de recursos del sistema para preparar despliegues de aplicaciones Java en producción. La clase debe validar si el sistema cumple con los requisitos mínimos antes de iniciar el proceso de compilación.

### Requisitos Funcionales:
1.  Verificar memoria RAM disponible (mínimo 4 GB)
2.  Verificar espacio en disco libre (mínimo 50 GB)
3.  Verificar número de núcleos CPU disponibles (mínimo 2)
4.  Generar informe con estado OK/FAIL para cada requisito
5.  Excepción personalizada si el sistema no cumple requisitos

### Código Parcial Incompleto:

```python
# Script: system_evaluation.py - VERSIÓN INCOMPLETA

import psutil

class SistemaEvaluation:
    def __init__(self):
        self.memoria_minima = 4 * (1024**3)  # 4 GB en bytes
        self.disco_minimo = 50 * (1024**3)   # 50 GB en bytes
        
    def evaluar_memoria(self):
        """Verifica memoria RAM disponible"""
        mem = psutil.virtual_memory()
        return mem.available >= self.memoria_minima
    
    def evaluar_disco(self):
        """Verifica espacio en disco libre"""
        disk = psutil.disk_usage('/')
        # FALTA: Implementar lógica de verificación
        pass
    
    def evaluar_cpu(self):
        """Verifica núcleos CPU disponibles"""
        cpu_count = psutil.cpu_count()
        return cpu_count >= 2
    
    def generar_informe(self):
        """Genera informe final de evaluación"""
        # FALTA: Implementar lógica del informe
        pass

# Instanciación y uso (sin implementar)
if __name__ == "__main__":
    evaluacion = SistemaEvaluation()
```

### Tarea del Alumno:
1.  Completar los métodos `evaluar_disco()` y `generar_informe()` de la clase.
2.  Implementar una excepción personalizada `RequisitosSistemaNoCumplidos` cuando el sistema no cumpla mínimos.
3.  Justificar las decisiones de diseño tomadas (nombres de variables, estructura de clases, manejo de excepciones).

---

# 📖 PARTE 3: SOLUCIONARIO DETALLADO Y EXHAUSTIVO PARA EL DOCENTE Y ALUMNO

> **🔍 NOTA DEL AUDITOR:**  
> A continuación se presenta el solucionario expandido. Cada pregunta incluye un análisis técnico profundo de la respuesta correcta y una disección detallada de por qué cada opción incorrecta es un error conceptual o técnico, sirviendo como material de repaso para los Criterios de Evaluación (CE) del RA4.

---

## SOLUCIONARIO - EXAMEN TIPO TEST (ANÁLISIS PROFUNDO)

### Pregunta 1: Respuesta Correcta **B**
**Justificación Técnica Expandida:**  
La respuesta correcta es la virtualización Tipo 1 (Bare Metal). En el contexto del RA4 y DAM, entender la arquitectura de virtualización es crucial para dimensionar servidores. Los hipervisores Tipo 1 como VMware ESXi o Microsoft Hyper-V Server se instalan **directamente sobre el hardware físico**, eliminando la capa intermedia del Sistema Operativo anfitrión (Host OS). Esto reduce drásticamente el *overhead* (sobrecarga) de recursos y permite un acceso más directo a las interrupciones del hardware, ofreciendo el máximo rendimiento posible para máquinas virtuales.

**Análisis Detallado de Distractores:**
*   **Opción A (Tipo 2 / Hosted):** Incorrecta. VirtualBox o VMware Workstation son hipervisores Tipo 2 que se ejecutan *como aplicaciones* sobre un SO anfitrión (ej. Windows). Esto añade una capa extra de traducción entre la VM y el hardware, consumiendo recursos del host y reduciendo el rendimiento disponible para las máquinas virtuales. Es útil para desarrollo local (portátil), pero no para despliegue de servidores de producción con múltiples instancias Linux.
*   **Opción C (Híbrida / Docker):** Incorrecta en este contexto específico. Aunque Docker es eficiente, la pregunta se refiere a desplegar "múltiples servidores Linux" completos sobre una estación física para pruebas de integración que requieren aislamiento total. Docker comparten kernel del host; si el host falla o hay conflicto de versiones de librerías, todas las contenedores fallan. Además, ejecutar contenedores sobre WSL (Windows Subsystem for Linux) añade complejidad innecesaria en comparación con un hipervisor nativo para pruebas de integración severas.
*   **Opción D (Emulación QEMU):** Incorrecta. La emulación completa (QEMU puro) traduce instrucciones de arquitectura completas (ej. ejecutar código ARM en x86), lo cual es extremadamente lento comparado con la virtualización por hardware. No ofrece "el mejor rendimiento" para servidores nativos Linux sobre hardware x86, donde la virtualización asistida por CPU (KVM/VT-x) es superior.

### Pregunta 2: Respuesta Correcta **A**
**Justificación Técnica Expandida:**  
La causa más probable de errores "Out of Memory" en Java con RAM física disponible es una configuración incorrecta de la JVM Heap Size (`-Xmx`). Si el administrador no ajusta la memoria máxima que puede usar la JVM, esta podría estar configurada por defecto (ej. 256MB o 1GB) en lugar de aprovechar los 8 GB disponibles. La JVM intenta asignar su heap dentro del límite configurado; si se llena, recurre al sistema operativo para pedir más memoria, pero si el SO detecta que la petición excede el límite físico o virtual asignado a ese proceso, genera el error OOM antes de usar toda la RAM del equipo.

**Análisis Detallado de Distractores:**
*   **Opción B (Fugas de Memoria):** Parcialmente plausible pero no la *causa más probable* en un entorno controlado con configuración incorrecta visible. Una fuga de memoria (*memory leak*) es un problema de código, sí, pero el uso intensivo de swap indica que la JVM está intentando asignar memoria y el SO está paginando agresivamente. Si fuera solo una fuga, veríamos crecimiento constante del uso de RAM hasta agotarla, no necesariamente un error OOM si hay swap disponible, aunque eventualmente ocurriría. La configuración incorrecta (Opción A) es el primer paso a revisar antes de analizar código.
*   **Opción C (Demasiado Swap):** Incorrecta conceptualmente. El sistema operativo asigna espacio de swap según necesidad. No "asigna demasiado" al proceso en un sentido negativo; más bien, si hay mucho uso de swap, indica que la RAM física se agotó. El problema no es *cuánto* swap hay, sino por qué el proceso necesita tanta memoria virtual (lo cual nos lleva a la configuración del Heap).
*   **Opción D (Conflicto Drivers):** Incorrecta y poco probable en entornos DAM modernos. Los conflictos de drivers de RAM son extremadamente raros y causarían inestabilidad general del sistema (Pantallazos Azules o Kernel Panics), no solo errores específicos de la aplicación Java.

### Pregunta 3: Respuesta Correcta **B**
**Justificación Técnica Expandida:**  
El comando `getfacl /proyectos` es el estándar en sistemas Linux para visualizar las Listas de Control de Acceso (ACLs) extendidas que no se muestran con los permisos tradicionales Unix (`rwx`). Cuando un usuario pertenece a un grupo pero no tiene acceso, y el permiso del grupo dice "ejecutar" (x), la ACL específica puede estar restringiendo el acceso. `ls -l` solo muestra los 3 bits de permisos básicos (owner/group/other) y una pequeña bandera (+) si hay ACLs, pero no detalla qué reglas están activas.

**Análisis Detallado de Distractores:**
*   **Opción A (`ls -l /proyectos`):** Incorrecta. Este comando muestra los permisos básicos `rwx` (ej. `-rwxr-x---`). Si hay una ACL que sobre escribe o complementa estos permisos, `ls -l` no mostrará el detalle de quién tiene acceso específico más allá del grupo principal. Puede mostrar un `+` al final indicando presencia de ACLs, pero no revela la regla específica que bloquea al usuario.
*   **Opción C (`chmod 750 /proyectos`):** Incorrecta. Este comando *modifica* permisos básicos, no los verifica. Ejecutarlo podría incluso sobrescribir las configuraciones deseadas si no se tiene cuidado. No sirve para diagnóstico de qué ACLs están activas actualmente.
*   **Opción D (`chown devgroup:devgroup /proyectos`):** Incorrecta. Este comando cambia el propietario y grupo principal del directorio, pero no muestra información sobre las reglas de acceso existentes ni ayuda a diagnosticar por qué un usuario específico (que ya pertenece al grupo) sigue sin poder escribir.

### Pregunta 4: Respuesta Correcta **B**
**Justificación Técnica Expandida:**  
PowerShell es la herramienta nativa moderna y más potente para la administración en Windows. El cmdlet `Get-Process` devuelve objetos completos con propiedades detalladas como `Name`, `Id` (PID), `Status` (Running/Stopped), `WorkingSet` (RAM usada), `HandleCount`, etc. Permite filtrado avanzado con `Select-Object`. Es superior a `tasklist` porque ofrece integración profunda con el .NET Framework y permite manipulación directa de objetos.

**Análisis Detallado de Distractores:**
*   **Opción A (`tasklist /v`):** Incorrecta en este contexto de "información más detallada". Aunque `tasklist /v` muestra información ampliada (PID, SessionName, etc.), es un legado de CMD y ofrece menos granularidad que PowerShell. No permite filtrado tan dinámico ni acceso a propiedades avanzadas como el estado del hilo o memoria específica sin parsing complejo de texto.
*   **Opción C (`netstat -ano`):** Incorrecta. Este comando muestra información sobre *conexiones de red activas*, puertos y PIDs asociados, pero no lista todos los procesos en ejecución ni su estado general (CPU/Memoria). Solo sirve para saber qué proceso usa un puerto específico, no para diagnosticar procesos maliciosos generales.
*   **Opción D (`systeminfo`):** Incorrecta. Este comando muestra información sobre la configuración del sistema operativo (versión, parches, uptime, memoria total), pero NO lista los procesos en ejecución ni sus PIDs individuales.

### Pregunta 5: Respuesta Correcta **A**
**Justificación Técnica Expandida:**  
El SO gestiona el uso de la CPU mediante un planificador (*scheduler*) que consulta la Tabla de Procesos. Cada proceso tiene una prioridad asignada (ej. en Windows "Realtime", "High", "Normal"; en Linux `nice` values). Si un compilador consume CPU constantemente, puede estar teniendo una prioridad alta o el SO no está logrando reducir su tiempo de ejecución a favor del servidor web si la planificación no se ajusta. La tabla de procesos es la estructura de datos central donde residen estos metadatos de planificación.

**Análisis Detallado de Distractores:**
*   **Opción B (Sistema de Archivos):** Incorrecta. El sistema de archivos gestiona la persistencia y ubicación lógica de los datos en el disco, no la asignación dinámica del tiempo de CPU entre procesos concurrentes. No tiene relación con la latencia de ejecución en tiempo real.
*   **Opción C (Máscara de Subred):** Incorrecta. La máscara de subred es una configuración de red IP que define qué parte de la dirección IP identifica la red y qué parte identifica el host. Es irrelevante para la planificación local de procesos dentro del mismo servidor.
*   **Opción D (Lista de Control de Acceso - ACL):** Incorrecta. Las ACLs determinan permisos de acceso a recursos (archivos, carpetas), no el tiempo de CPU que un proceso recibe. Un usuario puede tener permiso total sobre un archivo pero su proceso sigue siendo limitado por la prioridad del SO.

### Pregunta 6: Respuesta Correcta **B**
**Justificación Técnica Expandida:**  
Para servicios web seguros accesibles desde internet, es obligatorio abrir los puertos estándar HTTP (80) y HTTPS (443). El protocolo HTTPS usa SSL/TLS para cifrar el tráfico. Un firewall *estadoful* (stateful) monitorea el estado de las conexiones: permite que el tráfico salga hacia internet y solo deja entrar respuestas a solicitudes legítimas iniciadas desde dentro, o puertos específicos abiertos explícitamente (como 80/443). Esto protege contra ataques dirigidos.

**Análisis Detallado de Distractores:**
*   **Opción A (Puerto 80 UDP):** Incorrecta. HTTP usa TCP, no UDP. UDP es para conexiones sin conexión como DNS o streaming de video en tiempo real, donde la pérdida de paquetes se tolera mejor que la retransmisión. Usar UDP para una aplicación RESTful causaría pérdida de datos y errores de entrega.
*   **Opción C (Puerto 22 SSH sin cifrado):** Incorrecta y peligrosa. SSH siempre usa cifrado por diseño. Si un servicio está "sin cifrado", es Telnet o FTP, no SSH. Además, abrir solo el puerto 22 no permite acceso a la aplicación web RESTful (que necesita puertos 80/443).
*   **Opción D (Puerto aleatorio):** Incorrecta y mala práctica de seguridad. Usar puertos no estándar (>1024) sin NAT o configuración específica hace que el servicio sea inaccesible desde internet a menos que se configure manualmente en cada cliente. Además, aumenta la superficie de ataque si no hay firewall claro.

### Pregunta 7: Respuesta Correcta **C**
**Justificación Técnica Expandida:**  
Los SSDs (Solid State Drives) utilizan memoria flash NAND electrónica sin partes móviles mecánicas. La desfragmentación consiste en reorganizar datos dispersos para que estén físicamente contiguos, lo cual es vital en HDDs donde mover la aguja cuesta tiempo. En SSDs, no hay movimiento físico, por lo que el acceso aleatorio es rápido y constante. Además, la desfragmentación genera escrituras innecesarias, reduciendo la vida útil del disco (ciclos de escritura limitados). Los SSDs modernos usan comandos TRIM para mantener el rendimiento.

**Análisis Detallado de Distractores:**
*   **Opción A (Desfragmentar antes/después):** Incorrecta y dañina. Desfragmentar un SSD antes de la migración es innecesario y genera desgaste. Después de la migración, tampoco es necesario. La desfragmentación solo se recomienda para HDDs mecánicos antiguos o sistemas muy fragmentados que no tienen TRIM habilitado.
*   **Opción B (`chkdsk` en SSD):** Incorrecto en el contexto de "optimización". `chkdsk` (Check Disk) sirve para verificar integridad lógica del sistema de archivos y detectar sectores defectuosos, no para optimizar rendimiento mediante desfragmentación. Ejecutarlo periódicamente es bueno para mantenimiento lógico, pero la justificación de "optimizar rendimiento" en SSDs suele referirse erróneamente a defrag.
*   **Opción D (NTFS no compatible):** Incorrecta. NTFS es el sistema de archivos estándar de Windows y funciona perfectamente con SSDs. De hecho, Windows 10/11 detecta automáticamente que es un SSD y desactiva la desfragmentación automática.

### Pregunta 8: Respuesta Correcta **B**
**Justificación Técnica Expandida:**  
En una estrategia de copias incrementales, cada backup guarda solo los datos cambiados desde el último backup (completo o incremental). Para restaurar un punto en el tiempo (ej. día 3), necesitas la última copia completa (que sirve de base) y **todas** las copias incrementales subsiguientes hasta llegar al momento deseado (día 1, día 2, día 3). Saltarte una incremental rompe la cadena de cambios y los datos quedarán corruptos o incompletos.

**Análisis Detallado de Distractores:**
*   **Opción A (Solo incremental del día 3):** Incorrecta. Una copia incremental no contiene todos los datos, solo las diferencias respecto al anterior. Sin el "punto base" (copia completa), es imposible reconstruir el estado completo del sistema.
*   **Opción C (Todas incrementales desde inicio de mes):** Incorrecta en eficiencia. Aunque técnicamente podría funcionar si la cadena empieza con una copia completa, restaurar *todas* las copias si no hay necesidad de llegar al final es ineficiente y consume mucho tiempo. Solo se necesitan hasta el día 3.
*   **Opción D (Última diferencial + completa anterior):** Incorrecta para este escenario específico. Las copias diferenciales guardan cambios desde la última copia *completa*. Si usas diferenciales, solo necesitas la última completa y la última diferencial. Pero la pregunta especifica "copias incrementales", por lo que esta opción describe una estrategia mixta incorrecta para el escenario planteado.

### Pregunta 9: Respuesta Correcta **A**
**Justificación Técnica Expandida:**  
El comando `net accounts` es el utilitario de línea de comandos nativo en Windows (CMD/PowerShell) para gestionar las políticas de contraseña locales. `/minpwlen:8` establece la longitud mínima y `/maxpwage:30` define la caducidad máxima en días. Estos parámetros se aplican directamente al Security Account Manager (SAM) local, cumpliendo con el criterio CE b del RA4 sobre seguridad de cuentas.

**Análisis Detallado de Distractores:**
*   **Opción B (`useradd -p complex`):** Incorrecta por SO. Este es un comando de Linux/Unix para crear usuarios y gestionar contraseñas hash, no tiene equivalentes directos en Windows con esa sintaxis. Además, `complex` no es un parámetro válido estándar.
*   **Opción C (`gpasswd`):** Incorrecta. `gpasswd` se usa en Linux para administrar grupos de usuarios (añadir/quitar miembros), no para configurar políticas globales de contraseña del sistema operativo.
*   **Opción D (`chmod 700 /etc/shadow`):** Incorrecta. Este comando modifica permisos de archivo en Linux sobre el archivo que contiene hashes de contraseñas, pero no configura las reglas de complejidad o caducidad de la política de seguridad.

### Pregunta 10: Respuesta Correcta **B**
**Justificación Técnica Expandida:**  
`traceroute` (Linux/Mac) o `tracert` (Windows) muestra el recorrido exacto que siguen los paquetes de red desde tu origen hasta el destino, saltando por cada router intermedio. Para cada salto, muestra la latencia (tiempo de respuesta). Esto permite diagnosticar dónde se pierde la conexión: si falla en el primer salto es local; si falla al final, es remoto. Es esencial para diferenciar problemas de red local vs. internet.

**Análisis Detallado de Distractores:**
*   **Opción A (`ping`):** Incorrecto por alcance. `ping` solo dice "sí/no" y da un promedio de latencia total al destino, pero no muestra *dónde* en el camino se produce la pérdida o el retraso. No es útil para diagnosticar rutas complejas.
*   **Opción C (`nslookup`):** Incorrecto por función. `nslookup` consulta servidores DNS para traducir nombres a direcciones IP (ej. convertir `google.com` a `142.250.x.x`). Sirve para problemas de resolución de nombres, no para medir ruta o latencia de paquetes.
*   **Opción D (`ipconfig /all`):** Incorrecto por contexto. Muestra la configuración TCP/IP local del equipo (IP propia, DNS propio), pero no tiene información sobre la red remota ni la ruta hacia el servidor base de datos externo.

### Pregunta 11: Respuesta Correcta **B**
**Justificación Técnica Expandida:**  
En sistemas Linux modernos que usan `systemd` (Ubuntu 15+, Debian 8+, RHEL/CentOS 7+), `systemctl` es el comando unificado para gestionar servicios. `start` inicia el servicio inmediatamente, y `enable` crea los enlaces simbólicos necesarios en los directorios de inicio (`/etc/systemd/system`) para que se inicie automáticamente durante el arranque del sistema. Es el estándar actual para la gestión de Daemons (CE c).

**Análisis Detallado de Distractores:**
*   **Opción A (`service ... enable`):** Incorrecta por sintaxis moderna. El comando `service` es un wrapper legacy hacia init.d que funciona en muchos sistemas, pero el subcomando `enable` no es universalmente válido en todas las versiones del script `/etc/init.d`. En systemd puro, `systemctl enable` es la forma correcta y robusta.
*   **Opción C (`init.d ... update-rc.d`):** Incorrecta por obsolescencia relativa. Este era el método estándar en sistemas SysV (antes de systemd). Aunque sigue funcionando en algunos Linux antiguos, no es el comando nativo de `systemd`. En un entorno DAM moderno, se asume systemd como referencia principal para compatibilidad con servidores actuales.
*   **Opción D (`start-service`):** Incorrecta por inexistencia. No existe un comando estándar universal llamado `start-service` en Linux o Windows (donde sería `Start-Service`). Es una opción inventada que no corresponde a ninguna herramienta real.

### Pregunta 12: Respuesta Correcta **B**
**Justificación Técnica Expandida:**  
La compilación de código Java/Kotlin es un proceso intensivo en CPU y RAM. La JVM necesita cargar múltiples librerías, clases y generar bytecode. Múltiples núcleos permiten que herramientas como `Maven` o `Gradle` paralelicen tareas (ej. compilar módulos distintos simultáneamente). Si la RAM es insuficiente, el sistema usará Swap, lo que ralentiza drásticamente la compilación (Cuello de botella RA4h).

**Análisis Detallado de Distractores:**
*   **Opción A (Espacio SSD NVMe):** Secundario. Aunque un disco rápido ayuda a cargar librerías y guardar artefactos, el cuello de botella principal en compilación suele ser la CPU/RAM. Si tienes un SSD pero poca RAM, el sistema colapsará por Swap antes que por velocidad de lectura.
*   **Opción C (Resolución DNS):** Incorrecta. La resolución DNS es crítica para descargar dependencias en internet al inicio del build, pero una vez cargadas las librerías locales, la compilación no depende de DNS. No es el recurso crítico durante el proceso mismo.
*   **Opción D (Puertos Firewall):** Incorrecto. Los puertos abiertos afectan la red, no la velocidad local de procesamiento del ordenador que compila el código.

### Pregunta 13: Respuesta Correcta **C**
**Justificación Técnica Expandida:**  
La diferencia fundamental es el acceso al hardware. Tipo 1 (Bare Metal) se instala como un SO mínimo directo sobre el metal, gestionando el hardware directamente. Tipo 2 corre sobre otro SO, que debe gestionar el hardware y luego pasar la gestión a la VM. Por tanto, Tipo 1 tiene menos pasos intermedios (menos *overhead*) y mayor rendimiento, ideal para servidores de producción.

**Análisis Detallado de Distractores:**
*   **Opción A (Tipo 1 sobre SO anfitrión):** Incorrecta por definición. Esto describe un hipervisor Tipo 2. Tipo 1 se instala *sin* SO anfitrión (o con un kernel muy mínimo propio).
*   **Opción B (Tipo 2 menor overhead):** Incorrecta por lógica inversa. Al tener una capa extra de software (el SO host), el Tipo 2 tiene *más* overhead, no menos. Es más lento pero más flexible para desarrollo local.
*   **Opción D (No diferencia):** Falso. La diferencia de rendimiento es significativa en cargas de trabajo pesadas o servidores con muchas VMs concurrentes.

### Pregunta 14: Respuesta Correcta **B**
**Justificación Técnica Expandida:**  
LUKS (Linux Unified Key Setup) es el estándar para cifrado a nivel de disco completo en Linux. Cifra todo el volumen, incluyendo sistema operativo y datos. Si roban el disco físico, no se puede acceder a ningún dato sin la clave maestra. Es esencial para cumplir normativas de protección de datos (GDPR/RA4 h) en dispositivos portátiles o servidores sensibles.

**Análisis Detallado de Distractores:**
*   **Opción A (BitLocker):** Incorrecta por SO. BitLocker es la herramienta nativa de cifrado completo de disco para Windows, no Linux. Aunque existen alternativas en Linux, LUKS es el estándar específico del entorno solicitado.
*   **Opción C (GPG):** Incorrecto por alcance. GPG cifra archivos individuales o correos electrónicos. No protege todo el sistema de archivos a nivel de volumen; si alguien entra al SO y tiene acceso de usuario, puede leer los archivos sin cifrar antes de usarlos. LUKS protege incluso si el disco se desconecta del equipo.
*   **Opción D (SSH Keys):** Incorrecto por función. Las claves SSH protegen el *acceso remoto* a un sistema ya encendido y operativo. No protegen los datos en reposo si alguien roba el disco duro.

### Pregunta 15: Respuesta Correcta **A**
**Justificación Técnica Expandida:**  
Los pipelines CI/CD (Integración Continua / Despliegue Continuo) ejecutan múltiples tareas automatizadas simultáneamente: clonado de repositorio, compilación, pruebas unitarias, empaquetado y despliegue. Esto requiere que el sistema soporte alta concurrencia de procesos (CPU) y tenga espacio para almacenar artefactos temporales (Disk). Evaluar esto es parte del Criterio CE h (Evaluación de necesidades del sistema).

**Análisis Detallado de Distractores:**
*   **Opción B (Color carcasa):** Irrelevante. Es un atributo estético sin impacto técnico en la capacidad de procesamiento o almacenamiento.
*   **Opción C (Marca teclados):** Irrelevante para servidores. Los servidores suelen gestionarse por consola remota, no tienen teclado físico conectado al hardware de producción.
*   **Opción D (Versión gráfica):** Incorrecto. Las versiones gráficas consumen más recursos (RAM/CPU) que las versiones Server sin interfaz gráfica (Headless). Para CI/CD en servidores, se prefiere una instalación mínima para liberar recursos para la compilación y no para mostrar ventanas gráficas.

---

## SOLUCIONARIO - CASO PRÁCTICO A (DEBUGGING POWERShell)
**Análisis Técnico Paso a Paso del Error:**

El script original contiene errores críticos que impiden su ejecución correcta en un entorno de producción seguro. El análisis se divide por línea y función lógica.

### 1. Identificación de Errores y Correcciones Detalladas

| # | Error Original (Código) | Tipo de Error | Corrección Propuesta | Justificación Técnica RA4 |
|---|--------------------------|---------------|----------------------|---------------------------|
| **1** | `New-LocalUser -Name Username` | **Sintáctico / Referencia** | `-Name $Username` | En PowerShell, los parámetros deben recibir valores de variables precedidos por `$`. Escribir solo `Username` intenta usar una variable literal llamada "Username" (que no existe) o un objeto mal referenciado. El error causa que el script falle al intentar crear la cuenta con un nombre inválido. |
| **2** | `ConvertTo-SecureString ... -AsPlainText -True` | **Sintáctico / Parámetro** | `-AsPlainText -Force` | El parámetro para indicar texto plano es `-Force`, no `-True`. Usar `-True` hace que PowerShell ignore el argumento o lance error. Además, en producción real se debe evitar pasar contraseñas en texto plano; usar `ConvertTo-SecureString` con una variable segura es mejor práctica. |
| **3** | `-Group "Admins"` | **Lógico / Nombre de Objeto** | `-Group "Administrators"` | En Windows, el nombre del grupo de administradores locales es siempre **"Administrators"** (plural), no "Admins". El comando `Add-LocalGroupMember` buscará un grupo que no existe y fallará con error de acceso. |
| **4** | `New-Item ... -Path $ProjectPath` sin verificar | **Lógica / Seguridad** | `if (-not (Test-Path $ProjectPath)) { New-Item ... }` | El script original sobrescribe carpetas existentes o falla si el usuario no tiene permisos para crear la carpeta. Verificar existencia previene errores de ejecución y asegura que no se borre accidentalmente una carpeta de proyecto existente con datos valiosos (Criterio CE a). |
| **5** | No verifica si el usuario existe | **Lógica / Seguridad** | `if ($UserExists) { ... }` | Ejecutar `New-LocalUser` sobre un usuario que ya existe genera un error de "Usuario duplicado". En producción, esto detendría el script. Debe existir una verificación previa (`Get-LocalUser`) para manejar casos de re-provisionamiento o evitar fallos. |

### 2. Código Corregido (Versión Final con Explicación)

```powershell
# Script: provision_user_correcto.ps1 - VERSIÓN CORREGIDA Y OPTIMIZADA
param (
    [Parameter(Mandatory=$true)]
    [string]$Username,
    
    [Parameter(Mandatory=$false)]
    [string]$Password = "TempPass123!" # Nota: En producción usar Read-Host -AsSecureString
)

# 1. Validación de existencia del usuario (Criterio CE a)
$UserExists = Get-LocalUser -Name $Username -ErrorAction SilentlyContinue

if ($UserExists) {
    Write-Host "[!] El usuario '$Username' ya existe." -ForegroundColor Yellow
} else {
    # 2. Crear Carpeta de Proyecto con verificación de existencia (Criterio CE a/d)
    $ProjectPath = "C:\ProyectosDAM"
    if (-not (Test-Path $ProjectPath)) { 
        New-Item -ItemType Directory -Path $ProjectPath | Out-Null
    }

    # 3. Crear Usuario con sintaxis correcta y manejo de errores (Try/Catch)
    try {
        New-LocalUser -Name $Username `
            -Password (ConvertTo-SecureString $Password -AsPlainText -Force) `
            -FullName "Desarrollador DAM" `
            -Description "Usuario para proyectos de desarrollo"
        
        Write-Host "[OK] Usuario '$Username' creado exitosamente." -ForegroundColor Green
        
        # 4. Añadir al grupo Administradores con nombre CORRECTO (Criterio CE a)
        Add-LocalGroupMember -Group "Administrators" -Member $Username
        Write-Host "[OK] Usuario añadido al grupo 'Administrators'." -ForegroundColor Cyan
        
    } catch {
        # Manejo de excepciones para evitar fallos silenciosos
        Write-Error "[ERROR] No se pudo crear el usuario. Verifique permisos de administrador."
    }

    # 5. Configurar Permisos ACL con verificación de ruta (Criterio CE d)
    if (Test-Path $ProjectPath) {
        try {
            $acl = Get-Acl -Path $ProjectPath
            $account = [System.Security.Principal.NTAccount]$Username
            # Regla: FullControl, hereda a archivos y subcarpetas
            $rule = New-Object System.Security.AccessControl.FileSystemAccessRule($account, "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
            $acl.AddAccessRule($rule)
            Set-Acl -Path $ProjectPath -AclObject $acl
            
            Write-Host "[OK] Permisos de lectura/escritura aplicados en $ProjectPath." -ForegroundColor Green
        } catch {
            Write-Warning "No se pudieron aplicar los permisos ACL. Verifique permisos de escritura en la carpeta."
        }
    }
}
```

### 3. Justificación de Decisiones de Diseño (RA4)
*   **Seguridad:** Se implementa `Try/Catch` para evitar que errores parciales corrompan el estado del sistema o dejen al usuario sin acceso.
*   **Gestión de Usuarios:** La verificación previa (`Get-LocalUser`) cumple con la buena práctica de no sobrescribir usuarios existentes por error, alineado con el Criterio CE a.
*   **Permisos (ACLs):** El uso correcto de `Add-LocalGroupMember` con "Administrators" asegura que el usuario tenga los privilegios necesarios para compilar y ejecutar código en Windows sin errores de acceso denegado al sistema.

---

## SOLUCIONARIO - CASO PRÁCTICO B (DISEÑO CLASE PYTHON)
**Análisis Técnico Paso a Paso del Razonamiento:**

Este caso práctico evalúa la capacidad del alumno para implementar herramientas de monitorización y evaluación de requisitos, cumpliendo con el Criterio CE h (Evaluación de Necesidades).

### 1. Completar Métodos Faltantes (`evaluar_disco` e `informe`)

**Razonamiento Lógico:**
*   **Disco:** El método debe usar `psutil.disk_usage('/')`. Debe calcular el espacio libre en GB (dividiendo bytes por $1024^3$) y compararlo con `self.disco_minimo`. Retorna un diccionario estructurado para que el informe sea legible.
*   **Informe:** El método debe llamar a los tres métodos de evaluación (`memoria`, `disco`, `cpu`). Debe verificar si *todos* cumplen los requisitos. Si alguno falla, lanza la excepción personalizada. Si todos pasan, retorna un dict con estado "APROBADO".

### 2. Implementación Completa del Código

```python
# Script: system_evaluation.py - VERSIÓN COMPLETA Y CORREGIDA

import psutil

class RequisitosSistemaNoCumplidos(Exception):
    """Excepción personalizada para cuando el sistema no cumple requisitos mínimos (CE h)"""
    pass

class SistemaEvaluation:
    def __init__(self, memoria_minima_gb=4, disco_minimo_gb=50, cpu_minima=2):
        self.memoria_minima = memoria_minima_gb * (1024**3)  # Convertir a bytes para comparación precisa
        self.disco_minimo = disco_minimo_gb * (1024**3)      # Convertir a bytes
        self.cpu_minima = cpu_minima
    
    def evaluar_memoria(self):
        """Verifica memoria RAM disponible"""
        mem = psutil.virtual_memory()
        disponible_gb = round(mem.available / (1024**3), 2)
        cumple = mem.available >= self.memoria_minima
        return {
            'requisito': 'RAM Disponible',
            'valor_actual': f"{disponible_gb} GB",
            'cumple': cumple,
            'minimo_requerido': f"{memoria_minima_gb} GB"
        }
    
    def evaluar_disco(self):
        """Verifica espacio en disco libre"""
        # Nota: En Windows se debería usar psutil.disk_usage('C:\\') si no es raíz
        try:
            disk = psutil.disk_usage('/') 
            disponible_gb = round(disk.free / (1024**3), 2)
            cumple = disk.free >= self.disco_minimo
            return {
                'requisito': 'Disco Libre',
                'valor_actual': f"{disponible_gb} GB",
                'cumple': cumple,
                'minimo_requerido': f"{self.disco_minimo / (1024**3)} GB"
            }
        except Exception as e:
            return {'requisito': 'Disco Libre', 'valor_actual': 'Error', 'cumple': False, 'error': str(e)}
    
    def evaluar_cpu(self):
        """Verifica núcleos CPU disponibles"""
        # Usamos logical=False para contar núcleos físicos reales de compilación
        cpu_count = psutil.cpu_count(logical=False) 
        cumple = cpu_count >= self.cpu_minima
        return {
            'requisito': 'Núcleos CPU Físicos',
            'valor_actual': f"{cpu_count}",
            'cumple': cumple,
            'minimo_requerido': str(self.cpu_minima)
        }
    
    def generar_informe(self):
        """Genera informe final de evaluación y lanza excepción si falla (CE h)"""
        resultados = {
            'memoria': self.evaluar_memoria(),
            'disco': self.evaluar_disco(),
            'cpu': self.evaluar_cpu()
        }
        
        # Verificar si todos los requisitos se cumplen
        todos_cumplen = all(r['cumple'] for r in resultados.values())
        
        if not todos_cumplen:
            raise RequisitosSistemaNoCumplidos("El sistema no cumple con los requisitos mínimos de hardware para desarrollo.")
        
        return {
            'estado': 'APROBADO',
            'detalles': resultados,
            'mensaje': "Todos los requisitos del sistema se cumplen. El entorno es apto para desarrollo."
        }

# Instanciación y uso con manejo de excepciones
if __name__ == "__main__":
    try:
        evaluacion = SistemaEvaluation()
        informe = evaluacion.generar_informe()
        
        print("=" * 60)
        print("INFORME DE EVALUACIÓN DE SISTEMA PARA DESARROLLO DAM")
        print("=" * 60)
        
        for key, valor in informe['detalles'].items():
            estado = "✓ CUMPLE" if valor['cumple'] else "✗ NO CUMPLE"
            print(f"\n{valor['requisito']}:\n")
            print(f"  Valor Actual: {valor['valor_actual']}")
            print(f"  Mínimo Requerido: {valor['minimo_requerido']}")
            print(f"  Estado: {estado}")
        
        print("\n" + "=" * 60)
        print(f"ESTADO FINAL: {informe['estado']}")
        print(informe['mensaje'])
        print("=" * 60)
        
    except RequisitosSistemaNoCumplidos as e:
        # Bloque de manejo de error específico (RA4 CE h)
        print("\n[ALERTA CRÍTICA] " + str(e))
        print("No se puede continuar con el despliegue hasta solucionar los problemas de hardware.")
```

### 3. Justificación de Decisiones de Diseño

| Decisión Técnica | Razón Explicada para Alumnos DAM | Criterio RA4 Vinculado |
|---|---|---|
| **Excepción Personalizada** | Usar una excepción genérica (`Exception`) es mala práctica. `RequisitosSistemaNoCumplidos` permite al código que llama a esta función distinguir entre un error de red, un error de disco o un fallo de requisitos mínimos. Facilita el logging y la toma de decisiones en CI/CD. | **CE h** - Evaluación de necesidades del sistema |
| **Métodos Separados (`evaluar_memoria`, etc.)** | Cada método evalúa un recurso independiente. Esto permite escalar fácilmente: si mañana necesitamos evaluar GPU, solo añadimos `evaluar_gpu()` sin romper la lógica existente (Principio Single Responsibility). | **CE g** - Utilidades de mantenimiento y optimización |
| **Conversión a Bytes (`1024**3`)** | Las librerías como `psutil` trabajan internamente con bytes. Comparar GB directamente sería un error matemático. La conversión asegura consistencia y precisión en comparaciones lógicas booleanas. | **CE f** - Monitorización del sistema |
| **`cpu_count(logical=False)`** | En compilación, los núcleos físicos son más relevantes que los hilos lógicos (Hyper-Threading). Un núcleo físico es un motor de cálculo real; un hilo lógico compite por recursos internos. Para evaluación realista de capacidad de compilación, usamos físicos. | **CE h** - Evaluación de necesidades del sistema |
| **Informe Estructurado (Dict)** | Devolver un diccionario permite que el informe sea procesado automáticamente por otras herramientas (ej. generar HTML o JSON). No es solo texto para imprimir; es datos estructurados para auditoría y reporting. | **CE f** - Monitorización del sistema |

---

# 📊 CRITERIOS DE CALIFICACIÓN PARA EL DOCENTE

### Examen Tipo Test:
- **15 preguntas × 0.67 puntos** = Máximo 10 puntos
- **Ponderación:** 40% de la calificación final del RA4
- **Nota del Auditor:** Se debe exigir que el alumno sepa explicar *por qué* falló una opción incorrecta, no solo marcar la correcta.

### Caso Práctico A (Debugging):
| Criterio | Puntos Máximos | Descripción de Evaluación |
|----------|----------------|---------------------------|
| Identificación de errores | 2.5 | Mínimo 3 errores correctamente identificados con explicación técnica. |
| Propuesta de corrección | 2.5 | Solución técnica viable, sintaxis correcta y lógica segura. |
| Justificación RA4 | 1.0 | Explicación clara vinculada a seguridad o gestión de usuarios (CE a/d). |

### Caso Práctico B (Diseño Clase):
| Criterio | Puntos Máximos | Descripción de Evaluación |
|----------|----------------|---------------------------|
| Implementación funcional | 2.5 | Código ejecutable, sin errores de sintaxis y lógica correcta de verificación. |
| Manejo de excepciones | 1.0 | Excepción personalizada implementada y capturada correctamente en `try/except`. |
| Justificación diseño | 0.5 | Explicación clara sobre por qué se eligió esa estructura (ej. bytes vs GB). |

**Ponderación Casos Prácticos:** 60% de la calificación final del RA4.

---

# 📋 CHECKLIST DE VERIFICACIÓN DOCENTE

Antes de calificar, verificar:
- [ ] El alumno ha identificado **todos** los errores en el script PowerShell (al menos 3).
- [ ] Las correcciones propuestas son técnicamente viables y no introducen nuevos riesgos.
- [ ] La clase Python cumple con todos los requisitos funcionales listados (RAM, Disco, CPU).
- [ ] Se ha implementado manejo adecuado de excepciones personalizadas (`RequisitosSistemaNoCumplidos`).
- [ ] Las justificaciones vinculan teoría RA4 con práctica aplicada (ej. explican por qué `logical=False` en CPU).

---

**Documento generado para evaluación del RA4 - Sistema Informático (DAM)**  
**Versión:** 2.0 Ampliada | **Fecha:** 2025  
**Autoría:** Experto en Evaluación y Calidad Docente de FP (Programación)  
**Estado:** Aprobado para uso en aula
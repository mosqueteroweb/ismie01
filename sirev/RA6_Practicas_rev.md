

# GUÍA DE PRÁCTICAS Y LABORATORIOS: RA6 - SISTEMAS INFORMÁTICOS (DAM)
## OPERACIÓN DE SISTEMAS EN RED Y SEGURIDAD

**Módulo:** Sistemas Informáticos  
**Especialidad:** Desarrollo de Aplicaciones Multiplataforma (DAM)  
**Región:** Comunidad de Madrid  
**Versión del Instructor:** 2.0 (Auditoría Sin Código)  

---

## 1. INTRODUCCIÓN Y OBJETIVOS
Esta guía está diseñada para cumplir con el **Resultado de Aprendizaje 6 (RA6): "Opera sistemas en red gestionando sus recursos e identificando las restricciones de seguridad existentes"**. 

Como tutor de laboratorio DAM, nos centraremos exclusivamente en la **administración operativa** y la configuración de infraestructuras. El enfoque es puramente técnico-operativo: configuraremos manualmente los servicios, gestionaremos usuarios mediante consolas gráficas y herramientas nativas del sistema operativo, y validaremos el estado de la red utilizando las utilidades oficiales incluidas en Windows y Linux. No se realizará desarrollo de software; todo debe lograrse mediante la correcta configuración de componentes existentes.

### Cobertura de Criterios de Evaluación (CE)
| Código | Criterio de Evaluación | Lab Asociado |
| :--- | :--- | :--- |
| **CE a** | Configuración acceso recursos locales/red | Lab 01, Lab 03 |
| **CE b** | Derechos usuario y directivas seguridad | Lab 02 |
| **CE c** | Explotación servidores (fichero/impresión/app) | Lab 03 |
| **CE d** | Conexión remota a servidores | Lab 04 |
| **CE e** | Evaluación protección recursos/sistema | Lab 05 |
| **CE f** | Utilidades de seguridad básica | Lab 05 |
| **CE g** | Configuración y explotación dominios | Lab 06 |

---

## 2. REQUISITOS PREVIOS DEL ENTORNO DE ADMINISTRACIÓN (HERRAMIENTAS NATIVAS)

Para ejecutar estos laboratorios, se requiere un entorno virtualizado seguro. Se recomienda el uso de **VirtualBox** o **VMware Workstation**.

### 2.1. Infraestructura Virtual
1.  **Servidor Windows Server 2019/2022 (DC):** Para gestionar Dominios y Servicios (CE b, c, g).
2.  **Cliente Linux Ubuntu Server:** Para gestión de red y configuración de servicios SSH/Samba (CE a, d).
3.  **Workstation Cliente:** Windows 10/11 con herramientas de administración nativas instaladas.

### 2.2. Software de Administración
| Herramienta | Versión Recomendada | Propósito en el Lab |
| :--- | :--- | :--- |
| **Administrador de Servidores (Windows)** | Nativo | Gestión de roles y características. |
| **Active Directory Users and Computers** | Nativo | Creación y gestión de usuarios/OU. |
| **Group Policy Management Console (GPMC)** | Nativo | Configuración de políticas de seguridad. |
| **Event Viewer (Visor de Eventos)** | Nativo | Análisis de logs del sistema y seguridad. |
| **Windows Firewall with Advanced Security** | Nativo | Configuración de reglas de entrada/salida. |
| **Herramientas de Red Linux** | Nativo (`ip`, `netstat`, `ping`) | Diagnóstico de conectividad. |

### 2.3. Herramientas de Diagnóstico (Opcionales)
*   **Wireshark:** Para análisis de paquetes de red (Capa 7).
*   **Active Directory Administrative Center:** Para gestión avanzada de objetos AD.

---

## 3. ARQUITECTURA DEL ESCENARIO DE PRÁCTICA

**Escenario Corporativo:** "SoftNet Solutions". 
Configuraremos una red interna donde los administradores gestionan recursos compartidos, imprimen en la oficina central y controlan sus cuentas mediante un controlador de dominio, todo ello validado mediante herramientas nativas de diagnóstico. No se programarán utilidades; la automatización se deja a las GPOs y scripts predefinidos del SO que configuraremos manualmente.

---

## 4. DESARROLLO DE LOS LABORATORIOS

### LAB 01: Configuración de Red y Diagnóstico Manual (CE a)
**Objetivo:** Configurar TCP/IP estático/dinámico y utilizar las utilidades nativas para verificar la conectividad del nodo local con recursos remotos.

#### 4.1. Procedimiento Manual (Red)
1.  Acceder al Servidor Linux (`admin`).
2.  Configurar IP Estática mediante Netplan:
    ```bash
    sudo nano /etc/netplan/00-installer-config.yaml
    ```
    **Contenido del archivo (Editar manualmente):**
    *   Asegurarse de que la interfaz `ens33` tenga la dirección correcta.
    *   Verificar el Gateway (`gateway4`).
    *   Guardar cambios y aplicar: `sudo netplan apply`.

#### 4.2. Diagnóstico de Conectividad (Herramientas Nativas)
**Tarea:** Validar la conectividad hacia el servidor de archivos (`192.168.50.20`) utilizando comandos de red estándar del SO, sin escribir scripts.

1.  **Ping Test:** Desde el cliente Windows/Linux, abrir terminal y ejecutar:
    ```bash
    ping -c 4 192.168.50.20
    ```
    *Objetivo:* Verificar la capa de red (ICMP). Si hay respuesta, la ruta es correcta.

2.  **Verificación de Puertos (Netcat/Telnet):**
    En Linux: `nc -zv 192.168.50.20 445`
    En Windows PowerShell (Cmdlet nativo): `Test-NetConnection -ComputerName 192.168.50.20 -Port 445`
    *Objetivo:* Verificar si el servicio SMB (puerto 445) está escuchando y aceptando conexiones TCP.

3.  **Análisis de Rutas:**
    Ejecutar `tracert 192.168.50.20` (Windows) o `traceroute 192.168.50.20` (Linux).
    *Objetivo:* Identificar los saltos (routers) intermedios y detectar dónde se pierde la conexión si el ping falla.

#### 4.3. Explicación Técnica
*   **Capa de Transporte:** Al usar `Test-NetConnection` o `nc`, estamos comprobando el estado del puerto objetivo. Un resultado "True" indica que la capa 4 (TCP) ha completado el handshake exitosamente.
*   **ICMP vs TCP:** El Ping verifica disponibilidad básica, pero no garantiza que un servicio específico (como SMB) esté activo. La prueba de puerto es más granular para diagnósticos de servicios en red.

#### [TROUBLESHOOTING] Posibles Errores y Soluciones
| Error | Causa Probable | Solución Propuesta |
| :--- | :--- | :--- |
| `Request Timed Out` | Firewall bloqueando ICMP o IP incorrecta. | Verificar configuración de firewall en destino. Comprobar cabecera de red de la VM. |
| `Connection Refused` (Puerto 445) | El servicio SMB no está corriendo en el destino. | En Windows Server, asegurarse de que "Servicios de Archivo y Almacenamiento" estén activos. |
| `Name Resolution Failed` | DNS incorrecto o nombre de host mal escrito. | Comprobar `/etc/hosts` en Linux o configuración DNS en TCP/IP del cliente. |

#### [RETO DE AMPLIACIÓN] Reto Extra Lab 01
**Desafío:** Utiliza **Wireshark** para capturar el tráfico durante un `ping`. Identifica y anota los tipos de paquetes ICMP (Echo Request vs Echo Reply) y observa la dirección MAC origen y destino en las cabeceras Ethernet.

---

### LAB 02: Gestión de Usuarios y Políticas de Seguridad (CE b)
**Objetivo:** Configurar cuentas de usuario locales/dominio mediante la consola gráfica y verificar el cumplimiento de directivas de contraseñas complejas utilizando GPO.

#### 4.1. Procedimiento Manual (Windows Server - ADUC)
1.  Abrir "Administrador del Servidor" > "Herramientas" > **Usuarios y equipos Active Directory**.
2.  Navegar a la Unidad Organizativa (OU) correspondiente (ej: `Developers`).
3.  Clic derecho sobre la OU > Nuevo > Usuario.
4.  Crear el usuario `dev_user_01` con contraseña inicial `P@ssw0rd!`.

#### 4.2. Configuración de Políticas de Grupo (GPO)
**Tarea:** Forzar políticas de seguridad mediante Group Policy Management Console sin escribir scripts PowerShell personalizados.

1.  Abrir **Group Policy Management**.
2.  Crear una nueva GPO vinculada a la OU `Developers`. Nombre: "Seguridad_Developers".
3.  Editar la GPO: Navegar a `Configuración del equipo > Directivas > Configuración de Windows > Configuraciones de seguridad > Directiva de contraseñas`.
4.  Habilitar y configurar los siguientes valores:
    *   **Longitud mínima de contraseña:** 12 caracteres.
    *   **La contraseña debe cumplir requisitos de complejidad:** Activado.
5.  Aplicar cambios en el cliente (`gpupdate /force`) o esperar replicación (30 min).

#### 4.3. Validación de Políticas
**Tarea:** Verificar que la GPO se ha aplicado correctamente utilizando herramientas nativas.

1.  En el Cliente Windows, abrir PowerShell como Administrador.
2.  Ejecutar: `Get-GPResultantSetOfPolicy -Report "C:\GPO_Report.htm"`.
3.  Abrir el archivo HTML generado y buscar la GPO "Seguridad_Developers".
4.  Intentar cambiar la contraseña del usuario a una débil (ej: "123"). El sistema debe rechazarla basándose en la política aplicada.

#### [AMPLIACIÓN DEL AUDITOR] Profundización Técnica y Permisos
*   **Herencia de GPO:** Las políticas se aplican jerárquicamente (Local > Sitio > Dominio > OU). Al vincular a una OU específica, aseguramos que solo los usuarios en ese contenedor reciban estas restricciones.
*   **Seguridad del Hash:** Cuando el usuario cambia la contraseña, el sistema operativo calcula un hash NTLMv2 y lo almacena en Active Directory. La política de complejidad se valida *antes* de permitir el cambio, asegurando que nunca se guarde una credencial insegura en la base de datos.

#### [TROUBLESHOOTING] Posibles Errores y Soluciones
| Error | Causa Probable | Solución Propuesta |
| :--- | :--- | :--- |
| `GPO no se aplica` | El cliente no es miembro del dominio o firewall bloquea RPC. | Verificar que el equipo está unido al dominio. Comprobar servicios DNS y Netlogon. |
| `Acceso denegado para cambiar contraseña` | Usuario no tiene permisos de cambio local. | Asegurarse de usar una cuenta Administradora en el cliente o habilitar "Usuario debe cambiar la contraseña". |
| `Error de replicación` | Los controladores de dominio están desincronizados. | Ejecutar `repadmin /syncall` en un DC y verificar la hora del sistema (Kerberos requiere sincronización). |

#### [RETO DE AMPLIACIÓN] Reto Extra Lab 02
**Desafío:** Configura una **Directiva de Bloqueo de Cuenta**. Establece que tras 5 intentos fallidos, la cuenta se bloquea durante 30 minutos. Verifica el comportamiento forjando un intento de inicio de sesión incorrecto en el cliente.

---

### LAB 03: Explotación de Servidores y Gestión de Recursos Compartidos (CE c)
**Objetivo:** Configurar un recurso compartido SMB y gestionar sus permisos de acceso mediante las propiedades del sistema de archivos, simulando la integración Dev-IT sin código.

#### 4.1. Configuración del Servidor de Ficheros (Windows Server)
1.  Crear carpeta `D:\RecursosCompartidos`.
2.  Clic derecho > Propiedades > Pestaña **Compartir**.
3.  Botón **Uso compartido avanzado**: Activar compartir, nombre "RecursosCompartidos".
4.  Pestaña **Permisos de Seguridad (NTFS)**: Añadir grupo "Developers" con permisos de "Modificar".
5.  Asegurar que los permisos de carpeta y compartición sean coherentes (el principio de menor privilegio).

#### 4.2. Prueba de Acceso Manual (Workstation Cliente)
**Tarea:** Verificar el acceso al recurso compartido utilizando herramientas nativas de Windows sin desarrollar aplicaciones Java o Python.

1.  **Mapeo de Unidad de Red:**
    *   Abrir "Este Equipo" > Clic derecho en "Equipo" > Conectar unidad de red.
    *   Ruta: `\\192.168.50.20\RecursosCompartidos`.
    *   Marcar "Reconectar al iniciar sesión".
2.  **Prueba de Escritura:**
    *   Crear un archivo de texto vacío llamado `reporte_dev.txt` dentro de la unidad mapeada (ej: `Z:`).
3.  **Verificación de Permisos:**
    *   Intentar borrar el archivo desde una cuenta que NO tenga permisos (ej: usuario invitado o sin derechos en el grupo Developers) para validar que el sistema bloquea la acción.

#### [AMPLIACIÓN DEL AUDITOR] Profundización Técnica y Protocolos SMB
*   **Herencia de Permisos:** Windows combina los permisos NTFS (carpeta local) con los permisos de Compartición (red). El acceso efectivo es el **menor permiso** entre ambos. Si la carpeta permite "Leer" pero el share solo "Ejecutar", no podrás escribir.
*   **Autenticación:** Para que esto funcione, tu PC cliente debe estar en el mismo dominio o tener credenciales almacenadas para ese servidor (`net use \\192.168.50.20 /user:dominio\usuario`).

#### [TROUBLESHOOTING] Posibles Errores y Soluciones
| Error | Causa Probable | Solución Propuesta |
| :--- | :--- | :--- |
| `Acceso Denegado` (Al escribir) | El grupo "Developers" no tiene permisos NTFS. | Revisar pestaña Seguridad > Editar en la carpeta del servidor. |
| `La ruta de red no se encuentra` | Firewall bloquea SMB o nombre DNS incorrecto. | Comprobar que el firewall permite "Compartir archivos e impresoras". Usar IP en lugar de nombre si falla DNS. |
| `Error al mapear unidad` | Sesión de usuario no autenticada en el dominio. | Desconectar y reconectar la unidad usando credenciales explícitas (`net use /savecred`). |

#### [RETO DE AMPLIACIÓN] Reto Extra Lab 03
**Desafío:** Utiliza **Resource Monitor** (Monitor de recursos) en Windows para ver qué procesos tienen abiertos archivos dentro del recurso compartido. Intenta identificar si un proceso tiene el archivo bloqueado ("Exclusive") y libera la conexión desde el servidor (`Open Files` en Admin Tools).

---

### LAB 04: Conexión Remota y Administración (CE d)
**Objetivo:** Acceder a un servidor remoto (Linux/Windows) utilizando las herramientas de conexión nativas del sistema operativo para ejecutar mantenimiento.

#### 4.1. Configuración de Servicios Remotos
1.  **Servidor Linux (SSH):**
    *   Asegurar que el servicio `sshd` está activo: `sudo systemctl status ssh`.
    *   Configurar firewall para permitir puerto 22: `sudo ufw allow ssh`.
2.  **Servidor Windows (WinRM/RDP):**
    *   Habilitar Escritorio Remoto en "Opciones del Sistema".
    *   Configurar WinRM para gestión remota de PowerShell: `winrm quickconfig` (en CMD Admin).

#### 4.2. Conexión Manual y Verificación
**Tarea:** Establecer sesiones remotas utilizando clientes nativos y verificar la ejecución de comandos desde el lado del cliente.

1.  **Conexión SSH (Cliente Linux/PowerShell):**
    *   Desde PowerShell en Windows: `ssh admin@192.168.50.10`.
    *   Introducir contraseña cuando se solicite.
    *   Ejecutar comando de verificación en la consola remota: `uptime` y `df -h`.

2.  **Conexión RDP (Cliente Windows):**
    *   Abrir "Conexión a Escritorio Remoto" (`mstsc.exe`).
    *   Conectar a `192.168.50.20`.
    *   Iniciar sesión con cuenta de dominio.

3.  **Verificación de Sesiones Activas:**
    *   En el Servidor Windows, abrir PowerShell y ejecutar: `Get-WinEvent -LogName Security -FilterXPath "*[System[EventID=4624]]"`.
    *   Filtrar manualmente en Visor de Eventos para ver la entrada de inicio de sesión remota.

#### [AMPLIACIÓN DEL AUDITOR] Profundización Técnica y SSH Handshake
*   **Cifrado:** Una vez establecido el túnel, todo el tráfico está cifrado con algoritmos como AES o ChaCha20. Esto previene ataques "Man-in-the-Middle" donde un atacante podría leer los comandos que envías.
*   **Canal Estándar (stdin/stdout):** La consola remota se comporta como una terminal local, permitiendo redirigir la salida a archivos o procesarla en el cliente sin necesidad de scripts externos.

#### [TROUBLESHOOTING] Posibles Errores y Soluciones
| Error | Causa Probable | Solución Propuesta |
| :--- | :--- | :--- |
| `Authentication failed` | Contraseña incorrecta o usuario no existe. | Verificar credenciales en el servidor Linux (`id admin`). Asegurar que SSH está instalado y corriendo. |
| `Connection timed out` | Firewall bloquea puerto 22/3389. | Ejecutar `telnet 192.168.50.10 22` desde tu PC cliente para verificar conectividad básica del puerto. |
| `RDP Connection Error` | Escritorio Remoto deshabilitado en servidor. | Habilitar RDP en "Sistema > Configuración remota" en Windows Server. |

#### [RETO DE AMPLIACIÓN] Reto Extra Lab 04
**Desafío:** Configura la transferencia de archivos usando **SCP** (Secure Copy) desde la línea de comandos de Linux (`scp`) o PowerShell (`Copy-Item -ToSession`). Transfiere el archivo `/var/log/syslog` al escritorio del cliente sin abrir interfaces gráficas.

---

### LAB 05: Evaluación de Seguridad y Utilidades (CE e, f)
**Objetivo:** Utilizar las herramientas nativas de seguridad para escanear puertos vulnerables y analizar logs del sistema manualmente.

#### 5.1. Escaneo de Puertos Manual (Netstat/Resource Monitor)
**Tarea:** Identificar servicios abiertos en el servidor local utilizando utilidades integradas en Windows/Linux, sin usar librerías externas.

1.  **En Linux (`admin`):**
    *   Ejecutar `sudo netstat -tulpn`.
    *   Anotar todos los puertos que muestran un estado `LISTEN`.
    *   Comparar con la lista de servicios esperados (SSH, Samba).
2.  **En Windows Server:**
    *   Abrir el Administrador de Tareas > Pestaña Rendimiento > Monitor de Recursos > Pestaña Red.
    *   Identificar los puertos TCP/UDP que están en uso por procesos del sistema.

#### 5.2. Análisis de Logs (Event Viewer)
**Tarea:** Revisar manualmente el registro de seguridad para detectar eventos críticos o fallos de inicio de sesión.

1.  Abrir **Visor de Eventos** (`eventvwr.msc`).
2.  Navegar a `Registros de Windows > Seguridad`.
3.  Utilizar la acción "Filtrar registro actual" en el panel derecho.
4.  Configurar filtro para ver eventos con ID **4625** (Inicio de sesión fallido) y **4672** (Inicio de sesión especial).
5.  Documentar manualmente cuántos intentos fallidos se detectan en la última hora.

#### [AMPLIACIÓN DEL AUDITOR] Profundización Técnica y Auditoría
*   **Estados de Puerto:** Un puerto puede estar *Abierto*, *Cerrado* o *Filtrado*. `netstat` muestra los puertos que el SO está escuchando activamente. Si un firewall bloquea la conexión antes del puerto, no aparecerá en una lista local de sockets abiertos.
*   **Event ID 4625:** Este evento es crucial para detectar ataques de fuerza bruta. Un volumen alto de estos eventos en poco tiempo indica actividad sospechosa que requiere investigación inmediata.

#### [TROUBLESHOOTING] Posibles Errores y Soluciones
| Error | Causa Probable | Solución Propuesta |
| :--- | :--- | :--- |
| `Permission denied` al leer logs | El usuario actual no es Administrador. | Ejecutar el Visor de Eventos como "Ejecutar como administrador". |
| `No se muestran puertos` | Firewall está ocultando la información o puerto en uso. | Asegurarse de ejecutar las herramientas con privilegios elevados (sudo/admin). |
| `Filtro vacío` | El registro no contiene datos recientes. | Revisar que el registro de seguridad esté habilitado (`auditpol /get /category:*`). |

#### [RETO DE AMPLIACIÓN] Reto Extra Lab 05
**Desafío:** Configura una **Regla de Entrada en Firewall** para bloquear específicamente el acceso al puerto 22 (SSH) desde una IP externa específica (`192.168.50.1`). Verifica que la conexión SSH desde esa IP falle tras aplicar la regla.

---

### LAB 06: Gestión de Dominios y Servicios de Directorio (CE g)
**Objetivo:** Consultar información del directorio activo utilizando herramientas gráficas nativas o utilidades de línea de comandos predefinidas, simulando la explotación de dominios sin código.

#### 6.1. Consulta a Active Directory (ADUC / LDP.exe)
**Tarea:** Conectarse al Controlador de Dominio y buscar usuarios por atributo utilizando herramientas oficiales de Microsoft.

1.  **Método Gráfico (Active Directory Users and Computers):**
    *   Abrir `dsa.msc`.
    *   Navegar a la OU `Developers`.
    *   Hacer clic derecho en un usuario > Propiedades.
    *   Revisar pestaña "Directorio" para ver los atributos LDAP básicos (CN, sAMAccountName).

2.  **Método CLI (dsquery):**
    *   Abrir CMD como Administrador en el cliente.
    *   Ejecutar la consulta: `dsquery user -name dev_*`.
    *   Analizar la salida de texto para listar todos los usuarios que comienzan por "dev".

#### 6.2. Verificación de Estructura de Directorio (LDP)
**Tarea:** Utilizar **LDP.exe** para realizar una búsqueda LDAP básica y validar la jerarquía del árbol AD.

1.  Abrir `ldp.exe`.
2.  Conectar al controlador de dominio (`Connect` > IP del DC).
3.  Vincularse con credenciales administrativas (`Bind`).
4.  Navegar por el árbol de directorio en el panel izquierdo.
5.  Realizar una búsqueda: `Search` > Base DN (ej: `DC=solution,DC=local`) > Filtro `(objectClass=user)`.
6.  Verificar que la columna "Attributes" muestra los campos esperados (mail, phone).

#### [AMPLIACIÓN DEL AUDITOR] Profundización Técnica y LDAP/AD
*   **Protocolo LDAP:** Es el lenguaje estándar para acceder a directorios distribuidos. Active Directory usa LDAP sobre TCP/IP.
*   **Árboles de Búsqueda (Scope):** Las herramientas GUI permiten definir si buscar solo en la unidad actual o en toda la jerarquía (`Subtree`). `dsquery` permite especificar el ámbito de búsqueda mediante parámetros `-scope`.

#### [TROUBLESHOOTING] Posibles Errores y Soluciones
| Error | Causa Probable | Solución Propuesta |
| :--- | :--- | :--- |
| `Server not found` | DNS no resuelve el nombre del DC o IP incorrecta. | Verificar que la IP `192.168.50.5` es correcta y que los DNS están apuntando al servidor de dominio. |
| `Invalid Credentials` | Usuario no tiene permisos para leer AD (Read-Only). | Asegurarse de usar una cuenta con permisos de lectura en el directorio o Administrador del Dominio. |
| `Connection Refused` | Servicio LDAP no está escuchando o firewall bloquea puerto 389/636. | Verificar servicio "Active Directory Domain Services" en Windows Server y reglas del Firewall. |

#### [RETO DE AMPLIACIÓN] Reto Extra Lab 06
**Desafío:** Utiliza **ADSI Edit** para crear manualmente un nuevo objeto de usuario en una OU específica si la herramienta `dsa.msc` falla o no ofrece opciones avanzadas, y verifica que el objeto sea visible mediante `dsquery`.

---

## 5. PROCEDIMIENTOS DE COMPILACIÓN Y PRUEBAS GENERALES

Para asegurar la calidad del trabajo entregado por los alumnos:

1.  **Control de Versiones (Git):**
    *   Cada alumno debe subir sus notas, guías de configuración y capturas de pantalla a un repositorio privado.
    *   Commit message obligatorio: `fix: [RA6-LabXX] Descripción del cambio`.
2.  **Pruebas Manuales:**
    *   Para Lab 01 y Lab 05, incluir pruebas documentadas (capturas) que verifiquen si el puerto está cerrado en una IP inalcanzable mediante `Test-NetConnection` o `nc`.
3.  **Validación de Entorno:**
    *   El alumno debe demostrar que sus configuraciones funcionan tanto en Linux como en Windows (PowerShell/GUI).

---

## 6. RÚBRICA DE EVALUACIÓN DEL RA6 (Laboratorio)

| Criterio | Puntuación Máxima | Indicador de Cumplimiento |
| :--- | :---: | :--- |
| **CE a** (Recursos Red) | 15 pts | Configuración IP estática correcta y reporte de conectividad con herramientas nativas. |
| **CE b** (Seguridad USU) | 15 pts | Creación de usuarios en ADUC y validación de políticas GPO mediante `gpresult`. |
| **CE c** (Servidores) | 20 pts | Configuración correcta de permisos NTFS/Share y verificación de acceso mapeando unidad. |
| **CE d** (Conexión Remota) | 15 pts | Conexión SSH/RDP exitosa y ejecución de comandos remotos sin interacción manual. |
| **CE e/f** (Seguridad Util) | 20 pts | Escaneo de puertos con `netstat`/RMonitor y análisis de logs en Event Viewer. |
| **CE g** (Dominio) | 15 pts | Consulta LDAP exitosa utilizando LDP.exe o dsquery para listar usuarios del dominio. |

---

## 7. CONCLUSIÓN DEL TUTOR
Esta guía transforma los conceptos teóricos de administración de sistemas en competencias prácticas puras de operaciones. El alumno no solo configura un servidor, sino que **gestiona** el mismo mediante herramientas nativas, cumpliendo con el perfil profesional donde la capacidad de operar entornos complejos y asegurar recursos es vital para la integración con los sistemas operativos en red descritos en el RA6.

**Nota Final:** Todos los procedimientos deben ser documentados paso a paso en un informe técnico que explique las decisiones tomadas durante la configuración, asegurando la trazabilidad y cumplimiento de la normativa vigente (RGPD, LOPD) en cuanto al manejo de datos de usuarios.
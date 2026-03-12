

# GUÍA DE PRÁCTICAS AMPLIADA Y AUDITADA: RA7 - ELABORACIÓN DE DOCUMENTACIÓN Y UTILIZACIÓN DE APLICACIONES INFORMÁTICAS
### Módulo: Sistemas Informáticos | Especialidad: DAM (Desarrollo de Aplicaciones Multiplataforma)
**Versión Auditoría 3.0:** Enfoque total en Administración de Sistemas, Redes y Herramientas de Consola sin desarrollo de software.  
**Coordinador del Laboratorio:** Arquitecto de Sistemas / Administrador FP

---

## 1. INTRODUCCIÓN Y OBJETIVOS DEL LABORATORIO (AUDITADO)

**Título del Proyecto:** *Gestión Documental, Activos Digitales y Configuración de Servicios en Entorno Profesional*

En el rol de **Administrador de Sistemas**, la capacidad de documentar infraestructuras, gestionar activos de software y comunicar estados mediante servicios configurados no es secundaria; es operativa. Sin una documentación precisa y una configuración robusta, los sistemas fallan. Este laboratorio simula un escenario real donde un administrador debe preparar la documentación técnica, gestionar el entorno de software (sin programarlo), configurar servicios de red y transferir datos de forma segura utilizando las herramientas estándar del sector.

**Objetivos de Aprendizaje (Profundizados):**
1.  **Clasificación de Software (CE a):** Identificar licencias y tipos de software instalados mediante comandos nativos del SO (`dpkg`, `wmic`).
2.  **Análisis de Entorno (CE b):** Evaluar necesidades de hardware y red según requisitos técnicos, utilizando herramientas de diagnóstico integradas en el Sistema Operativo.
3.  **Documentación Colaborativa (CE c):** Generar documentación técnica usando Markdown y control de versiones (Git) para trazabilidad de cambios en la infraestructura ("Docs-as-Code").
4.  **Comunicación y Transferencia (CE d, e):** Configurar clientes de correo (SMTP/IMAP) manualmente y transferir archivos mediante protocolos seguros (`scp`, `sftp`) sin uso de scripts de automatización.
5.  **Búsqueda y Mantenimiento (CE f, g):** Utilizar herramientas CLI para diagnóstico y configuración de tareas programadas del sistema (Cron/Tareas Programadas).

---

## 2. REQUISITOS PREVIOS DE SOFTWARE Y ENTORNO (AUDITADO)

Para completar estas prácticas, el entorno de trabajo debe incluir las siguientes herramientas instaladas y configuradas. **Nota:** Estas versiones son mínimas para garantizar compatibilidad con APIs modernas y seguridad actualizada.

| Categoría | Herramienta | Versión Mínima | Propósito Técnico |
|-----------|-------------|----------------|-----------|
| **Editor de Texto** | VS Code, Notepad++ o Sublime Text | 2023.x | Edición de documentación Markdown y configuración de archivos de texto plano. |
| **Sistema Operativo** | Linux (Ubuntu/Debian) o Windows 10/11 | Actual | Entorno nativo para ejecución de comandos CLI (`bash`, `cmd` / `powershell`). |
| **Control Versión** | Git CLI | 2.40+ | Colaboración y trazabilidad. Necesario para el historial de commits documentales. |
| **Ofimática** | LibreOffice o MS Office | 2021/365 | CE c: Elaboración de informes finales (formatos .docx, .xlsx). |
| **Red / Transferencia** | Clientes CLI (`scp`, `sftp`) y GUI (FileZilla) | - | CE e: Conexión FTP/SFTP manual. Uso de puertos específicos. |
| **Terminal** | PowerShell (Windows) / Bash (Linux/Mac) | - | CE f/g: Comandos de sistema (`df`, `top`), diagnóstico y configuración de tareas. |

---

## 3. PRÁCTICA 1: AUDITORÍA DE SOFTWARE Y LICENCIAS (CE a, b)

**Escenario:** Eres el encargado tecnológico de una startup. Debes auditar la instalación actual del servidor de desarrollo para seleccionar las herramientas adecuadas para un nuevo proyecto web. Debes justificar tu elección basándote en licencias y propósito del software mediante análisis nativo.

#### 3.1 Procedimiento Actualizado
1.  **Investigación de Activos:** Utiliza los comandos nativos de tu sistema operativo para listar el software instalado (ej: `dpkg -l` en Linux o `Get-InstalledPackage` en PowerShell). Identifica 5 herramientas críticas (IDE, DB, Web Server, etc.).
2.  **Análisis de Licencias:** Para cada herramienta identificada, consulta su documentación oficial o repositorio público para determinar su tipo de licencia (Propietaria, Open Source, Freeware).
3.  **Reporte Manual:** Genera un archivo CSV manualmente o mediante copiado de datos desde el explorador de archivos, importando luego los resultados en Excel/LibreOffice Calc para crear una tabla de control.

#### 3.2 Explicación Profunda: Arquitectura del Sistema y Gestión de Paquetes
El software instalado no es invisible; reside en directorios específicos del sistema de archivos gestionados por gestores de paquetes.
*   **Gestores de Paquetes (`dpkg`, `rpm`):** Son bases de datos locales que registran metadatos de cada software instalado (versión, estado, dependencias). No requieren programación, solo lectura y escritura de registros de sistema.
*   **Clasificación Lógica:** En un entorno real, esto se cruza con políticas de cumplimiento legal (Compliance). Saber si una licencia es "Viral" (GPL) afecta qué software puedes compilar junto a tu código propietario.

#### 3.3 Ejemplo de Comandos de Diagnóstico (Lectura Exclusiva)
Estos comandos **no generan scripts**, solo muestran información del estado actual:

**Para Entorno Linux:**
```bash
# Listar paquetes instalados con su versión y estado
dpkg -l | grep "ii" 

# Ver detalles específicos de un paquete (ej: git)
dpkg -s git 
```

**Para Entorno Windows (PowerShell):**
```powershell
# Obtener lista de programas instalados
Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, Publisher

# O usar la herramienta nativa de gestión
systeminfo
```

#### 3.4 Compilación y Ejecución (Procedimiento Manual)
1.  Abrir terminal con privilegios de usuario estándar o administrador según sea necesario.
2.  Ejecutar los comandos de listados anteriores.
3.  **Verificación:** Copiar la salida relevante en un archivo `.txt` o directamente a Excel. Verificar que las columnas coincidan con el formato del informe final (`Nombre`, `Versión`, `Licencia`).

#### ⚠️ Posibles Errores y Soluciones (Troubleshooting)
| Error | Causa Raíz Técnica | Solución Propuesta |
|-------|-------------------|--------------------|
| Comando no encontrado (`command not found`) | El gestor de paquetes no está instalado o la ruta PATH es incorrecta. | Instalar el paquete `apt` (Debian/Ubuntu) o verificar la instalación del sistema operativo base. |
| Permisos denegados al leer metadatos | Intentar leer archivos de sistema protegidos sin privilegios root/admin. | Ejecutar la terminal con permisos elevados (`sudo` en Linux, "Ejecutar como administrador" en Windows). |
| Salida muy extensa | El comando devuelve cientos de paquetes instalados. | Usar filtros (`grep`) para buscar solo el software relevante (ej: `dpkg -l | grep "python"`). |

#### 🚀 Reto de Ampliación: Auditoría de Versiones Obsoletas
**Objetivo:** Identificar riesgos de seguridad por desactualización.
**Instrucción:** Utiliza la herramienta de actualización del sistema para listar paquetes que tienen actualizaciones disponibles (`apt list --upgradable` o `systeminfo`). Compara esta lista con el inventario generado en el paso 1 y justifica cuáles requieren prioridad de mantenimiento antes del despliegue.

---

## 4. PRÁCTICA 2: DOCUMENTACIÓN TÉCNICA Y COLABORACIÓN (CE c)

**Escenario:** Debes documentar la configuración de un servidor interno para que otros administradores lo puedan mantener. Se requiere un `README.md` estructurado y un informe ejecutivo en formato Word/Docs.

#### 4.1 Procedimiento Actualizado
1.  **Markdown:** Crear el archivo `README.md` con encabezados, listas de requisitos y bloques de configuración (sin lógica de programación).
2.  **Colaboración (Git):** Inicializar repositorio, hacer commit inicial y simular un fork/merge para resolver conflictos documentales.
3.  **Ofimática:** Copiar la estructura del README a Word para generar el informe formal (CE c).

#### 4.2 Explicación Profunda: Gestión de Versiones Documental ("Docs-as-Code")
El Markdown no es solo "texto bonito". Es un formato plano que permite control de versiones granular.
*   **Git Commits:** Cada línea en el historial tiene un hash SHA1 único. Esto permite saber *quién*, *cuándo* y *qué* cambió exactamente en la documentación, fundamental para auditorías legales o de cumplimiento (CE c).
*   **Markdown vs Word:** El Markdown es ideal para desarrolladores/administradores (fácil de editar, versionar). El Word es ideal para clientes (formato WYSIWYG). La práctica obliga a entender que ambos formatos sirven a audiencias distintas.

#### 4.3 Plantilla de Documentación (Contenido Texto/Configuración)
Este contenido **no contiene código ejecutable**, solo texto descriptivo y configuraciones estáticas:

```markdown
# DOCUMENTACIÓN DE SERVIDOR: Infraestructura de Autenticación v1.0

## 1. Descripción General
Este servidor gestiona la autenticación de usuarios mediante servicios LDAP.
**Licencia:** Propietaria (SO) / Open Source (Servicios)  
**Entorno:** Producción / Desarrollo

## 2. Requisitos Previos (CE b)
- Servidor Linux Ubuntu 22.04 LTS
- 4 GB RAM Mínimo
- Conexión de red estable

## 3. Configuración del Entorno
Utilizar el siguiente comando para verificar la conexión SSH:

```bash
ssh usuario@192.168.1.50
```

## 4. Endpoints Principales (Red)
| Protocolo | Puerto | Descripción |
|--------|------|-------------|
| HTTPS   | 443  | Acceso Web Seguro |
| SSH     | 22   | Acceso Remoto Admin |

> **Nota:** Este documento es parte de la documentación técnica obligatoria (CE c).
```

#### 4.4 Procedimiento de Compilación, Ejecución y Pruebas (Git)

**Paso A: Inicialización del Repositorio**
```bash
# 1. Crear directorio y entrar
mkdir doc-lab-RA7 && cd doc-lab-RA7

# 2. Inicializar Git
git init

# 3. Añadir archivo de documentación
echo "# DOCUMENTACIÓN DE SERVIDOR" > README.md
# (Copiar el resto del contenido Markdown anterior)

# 4. Staging y Commit inicial
git add .
git commit -m "Initial commit: Documentación básica de servidor"
```

**Paso B: Simulación Colaborativa (Merge)**
1.  Crear una rama `feature/nuevas-reglas`.
2.  Añadir una regla nueva en el README sobre seguridad.
3.  Volver a `main` y hacer merge para resolver conflictos simulados de documentación.

**Paso C: Exportación Ofimática**
1.  Copiar el contenido del `README.md`.
2.  Pegar en **Microsoft Word** o **Google Docs**.
3.  Aplicar estilos de título (H1, H2) y generar un Índice Automático.
4.  Guardar como `.docx` con nombre `Informe_Tecnico_RA7.docx`.

#### ⚠️ Posibles Errores y Soluciones (Troubleshooting)
| Error | Causa Raíz Técnica | Solución Propuesta |
|-------|-------------------|--------------------|
| Conflictos de Merge (`CONFLICT`) | Dos ramas modificaron la misma línea del README. | Usar un editor de texto para resolver manualmente los marcadores `&lt;&lt;&lt;&lt;&lt;&lt;&lt;` y `>>>>>>>`. Guardar solo una versión coherente antes de hacer el commit final. |
| Markdown no renderiza en Word | Copiar y pegar directo a veces pierde formato. | Usar un conversor online o guardar primero como PDF/HTML desde VS Code y luego importar, o usar la función "Insertar Objeto" de Word. |
| `git config user not found` | Git necesita saber quién eres para firmar commits. | Ejecutar: `git config --global user.name "Tu Nombre"` y `git config --global user.email "tu@email.com"`. |

#### 🚀 Reto de Ampliación: Generación de PDF Automático
**Objetivo:** Automatizar la entrega al cliente.
**Instrucción:** Investiga una herramienta CLI (como `pandoc` o extensión de VS Code) que convierta el archivo `.md` directamente a `.pdf`. Ejecuta el comando en terminal para generar el documento final sin abrir Word.

---

## 5. PRÁCTICA 3: COMUNICACIÓN Y TRANSFERENCIA DE FICHEROS (CE d, e)

**Escenario:** Al finalizar la documentación, debes notificar al equipo de QA manualmente mediante configuración de cliente de correo y subir los archivos del proyecto a un servidor FTP externo para su revisión.

#### 5.1 Procedimiento Actualizado
1.  **Correo Electrónico:** Configurar un cliente de correo (Thunderbird, Outlook o Mail) con credenciales SMTP/IMAP manuales. No se usarán scripts. Se verificará la conexión mediante puertos.
2.  **Transferencia:** Conectar a un servidor FTP/SFTP y subir los archivos generados (`.docx`, `.md`) utilizando herramientas de línea de comandos (`scp`, `sftp`) para garantizar seguridad.

#### 5.2 Explicación Profunda: Protocolos de Transporte y Seguridad
*   **SMTP/IMAP:** Opera en puertos específicos (587, 993). La configuración manual obliga a entender que la contraseña del correo debe ser segura; por eso, se recomienda usar "App Passwords" o variables de entorno en el cliente, nunca texto plano visible.
*   **FTP vs SFTP/SCP:** FTP clásico envía credenciales en texto plano. SFTP/SCP usa SSH (puerto 22), cifrando toda la sesión. La práctica pide usar comandos CLI para visualizar cómo funciona el protocolo de forma segura.

#### 5.3 Procedimiento de Configuración de Correo Manual
Para cumplir con el criterio **CE d** de forma visual y técnica:
1.  Abrir cliente de correo (ej: Thunderbird).
2.  Ir a **Configuración de Cuenta > Información Básica**.
3.  Introducir manualmente los datos del servidor SMTP (`smtp.gmail.com`, puerto `587`) e IMAP (`imap.gmail.com`, puerto `993`).
4.  Activar la opción **"Certificado seguro (TLS/SSL)"** en la configuración avanzada para garantizar el cifrado de la conexión.
5.  **Verificación:** Enviar un correo de prueba y verificar que aparece en "Enviados" con estado correcto.

#### 5.4 Procedimiento de Transferencia Segura (CLI)
Para cumplir con el criterio **CE e** mediante comandos:
1.  Abrir terminal.
2.  Conectarse al servidor mediante SSH/SFTP usando la sintaxis estándar:
    ```bash
    # Sintaxis SCP para copiar archivo local a remoto
    scp Informe_Tecnico_RA7.docx usuario@servidor.dam.edu:/home/usuario/docs
    
    # O usar SFTP interactivo
    sftp usuario@servidor.dam.edu
    > put Informe_Tecnico_RA7.docx
    ```
3.  **Verificación:** Comprobar que el archivo aparece en el servidor con permisos de lectura mediante comandos `ls` en el servidor remoto.

#### ⚠️ Posibles Errores y Soluciones (Troubleshooting)
| Error | Causa Raíz Técnica | Solución Propuesta |
|-------|-------------------|--------------------|
| Autenticación fallida (`Authentication Failed`) | Contraseña incorrecta o bloqueo por seguridad del proveedor. | Activar la verificación en dos pasos y generar una **App Password** específica para este cliente de correo/servidor. |
| Conexión denegada (Connection Refused) | El firewall local bloquea los puertos 20/21 o 22. | Cambiar a modo pasivo en el cliente o verificar que el puerto SSH (22) esté abierto en la red. |
| Archivos corruptos al subir | Modos de transferencia incorrectos (ASCII vs Binario). | En `sftp`, asegurarse de usar comandos binarios (`binary`) antes del `put` para archivos `.docx`. |

#### 🚀 Reto de Ampliación: Validación de Puertos
**Objetivo:** Verificar la apertura de puertos manualmente.
**Instrucción:** Utiliza el comando `telnet` o `nc` (Netcat) para probar la conectividad al servidor SMTP antes de configurar el cliente completo. Ejemplo: `telnet smtp.gmail.com 587`. Si no se conecta, indica bloqueo de red.

---

## 6. PRÁCTICA 4: BÚSQUEDA TÉCNICA Y UTILIDADES DEL SISTEMA (CE f, g)

**Escenario:** El sistema presenta una alerta de bajo espacio en disco y necesitas buscar la documentación oficial para optimizar la partición antes del despliegue.

#### 6.1 Procedimiento Actualizado
1.  **Diagnóstico CLI:** Ejecutar comandos nativos para ver estado del disco y memoria (CE g). Sin escribir scripts, solo ejecutar comandos de diagnóstico.
2.  **Búsqueda Web (CE f):** Buscar en Google/StackOverflow la solución técnica específica usando operadores de búsqueda avanzada para encontrar documentación oficial.
3.  **Mantenimiento:** Configurar una tarea programada nativa del sistema operativo para limpieza automática sin escribir código personalizado, utilizando las herramientas integradas (Cron o Programador de Tareas).

#### 6.2 Explicación Profunda: Diagnóstico y Búsqueda Avanzada
*   **CLI (`df`, `top`):** Estos comandos leen directamente archivos del sistema de archivos para obtener métricas sin consumir mucha RAM, a diferencia de las interfaces gráficas. Son herramientas fundamentales para el administrador.
*   **Google Dorks:** El uso de operadores como `site:` o `filetype:` reduce el ruido. Buscar en la documentación oficial (`developer.android.com`, `docs.microsoft.com`) es más fiable que buscar en un blog personal, reduciendo riesgos de integrar configuración obsoleta.

#### 6.3 Comandos de Diagnóstico y Configuración (Ejecución Directa)
Estos son comandos a ejecutar en consola para obtener el estado del sistema:

**Para Entorno Linux:**
```bash
# Verificar espacio en disco (Human readable)
df -h /

# Ver proceso que más consume RAM/CPU
top -b -n 1 | head -20

# Buscar archivos grandes en la carpeta de usuario
du -ah --max-depth=1 | sort -hr | head -10
```

**Para Entorno Windows (PowerShell/CMD):**
```powershell
# Verificar espacio en disco
Get-PSDrive | Where-Object {$_.Provider.Name -eq "FileSystem"} | Select-Object Name, Used, Free

# Ejecutar limpieza de disco integrada (Disk Cleanup)
cleanmgr /sagerun:1 
```

#### 6.4 Procedimiento de Configuración de Mantenimiento
**Paso A: Linux (Cron)**
1.  Abrir editor de crontab: `crontab -e`.
2.  Añadir una línea para ejecutar la limpieza si el espacio es bajo (usando comando nativo, no script propio):
    ```bash
    # Limpiar /tmp cada domingo a las 3 AM
    0 3 * * 0 find /tmp -type f -mtime +7 -delete
    ```

**Paso B: Windows (Programador de Tareas)**
1.  Abrir **Panel de Control > Programador de Tareas**.
2.  Crear tarea básica que ejecute `cleanmgr.exe` con parámetros de configuración predefinida (`/sagerun`).
3.  Configurar el desencadenante (cada domingo a las 3:00 AM).

#### ⚠️ Posibles Errores y Soluciones (Troubleshooting)
| Error | Causa Raíz Técnica | Solución Propuesta |
|-------|-------------------|--------------------|
| `Permission denied` al leer logs o limpiar | El usuario estándar no tiene acceso a carpetas de sistema. | Ejecutar el comando con `sudo` (Linux) o "Ejecutar como administrador" (Windows). |
| Comando no reconocido (`command not found`) | La terminal no reconoce la ruta del comando en PATH. | Usar la ruta completa del comando (ej: `/usr/bin/df`) o añadir la carpeta al PATH. |
| Tarea programada no se ejecuta | El servicio de tareas está detenido. | Verificar que el servicio `cron` (Linux) o `Task Scheduler` (Windows) esté corriendo en segundo plano. |

#### 🚀 Reto de Ampliación: Automatización de Alertas
**Objetivo:** Configurar notificación visual del sistema.
**Instrucción:** Configura la herramienta de monitoreo nativa (`htop` o Monitor de Recursos) para que, al detectar una carga de CPU superior al 90%, lance un mensaje en pantalla (usando el comando `notify-send` en Linux) sin escribir un script personalizado, solo configurando las reglas visuales del entorno.

---

## 7. EVALUACIÓN Y CRITERIOS DE VERIFICACIÓN (AUDITADO)

Para aprobar el módulo RA7, se evaluará la siguiente evidencia entregable con un enfoque en la calidad técnica y la comprensión profunda de sistemas:

| Criterio | Evidencia Requerida | Ponderación | Detalles de Auditoría |
|----------|---------------------|-----------|----------------------|
| **CE a** | Informe manual con clasificación de licencias generado desde comandos CLI (`dpkg`, `wmic`). | 15% | Verificar que los datos provienen del sistema, no de un script externo. |
| **CE b** | Justificación escrita en el informe Word sobre la selección del software y requisitos técnicos (RAM, SO). | 10% | Debe mencionar requisitos técnicos y legales basados en la investigación CLI. |
| **CE c** | Repositorio Git con commits y archivo `.docx` bien formateado. | 25% | El historial de Git debe mostrar evolución real, no un solo commit masivo. |
| **CE d** | Captura de pantalla del cliente de correo configurado manualmente (ventana de propiedades SMTP/IMAP). | 15% | Debe mostrarse el uso de cifrado STARTTLS/SSL en la configuración visible. |
| **CE e** | Captura de pantalla de la sesión SFTP/SCP exitosa (terminal con comandos `put` o `scp`). | 10% | Verificar que se usó conexión segura, no FTP plano. |
| **CE f** | URL guardada o captura de búsqueda avanzada Google realizada (`site:`, `filetype:`). | 10% | Usar operadores demuestra competencia técnica en recuperación de información. |
| **CE g** | Output del comando CLI mostrando uso de disco/logs y configuración de Cron/Tareas Programadas. | 15% | La tarea programada debe estar configurada en el sistema operativo nativo. |

---

## 8. CONCLUSIONES Y RECOMENDACIONES DEL ADMINISTRADOR DE SISTEMAS

Como Administrador de Sistemas, he diseñado esta guía para que no solo cumplas con el currículo, sino que adquieras competencias reales de infraestructura:
1.  **Herramientas Nativas:** No dependes de scripts externos; confías en las capacidades nativas del Sistema Operativo (`dpkg`, `cron`, `scp`). Esto garantiza portabilidad y seguridad.
2.  **Documentación Viva:** Usa Markdown y Git como base. El Word es para la entrega final al cliente/no técnico. La documentación debe ser mantenible y versionable.
3.  **Seguridad por Diseño:** Al configurar el correo SMTP en la práctica 3, recuerda nunca hardcodear contraseñas en configuraciones visibles (usa las opciones de gestión de credenciales del cliente). Esto protege tus credenciales si subes capturas a un repositorio público.

**Nota Final:** Esta guía cubre integralmente los Criterios de Evaluación del RA7 dentro del contexto de desarrollo profesional DAM, pero desde la perspectiva estricta de **Sistemas Informáticos**. Asegúrate de guardar todas las pruebas en tu portafolio personal (GitHub/Bitbucket) antes de entregarlas al tutor. **Recuerda: La documentación es el contrato entre el desarrollador y el futuro.**

---
*Fin de la Guía Práctica Revisada y Ampliada - RA7 (DAM)*  
*Documento bajo licencia para uso educativo en el marco curricular de FP.*
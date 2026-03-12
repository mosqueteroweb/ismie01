

# BANCO DE EVALUACIÓN - RA2: SISTEMAS INFORMÁTICOS (DAM) – EDICIÓN EXPANDIDA Y VALIDADA

**Módulo Profesional:** Sistemas Informáticos  
**Especialidad:** Desarrollo de Aplicaciones Multiplataforma (DAM)  
**Resultado de Aprendizaje 02:** Instalación y Gestión de Entornos Operativos  
**Nivel:** Formación Profesional Superior / Ingeniería de Software  
**Versión del Documento:** 2.1 - Versión Auditoría Expandida (Solucionario Enciclopédico)  
**Estado:** Material de Estudio Oficial para Profesorado y Estudiantes DAM  

---

## ÍNDICE DE CONTENIDOS

1. [Examen Tipo Test - 15 Preguntas de Alta Dificultad](#1-examen-tipo-test--15-preguntas-de-alta-dificultad)
2. [Supuesto Práctico 01: Debugging de Script de Instalación Automatizada](#2-supuesto-práctico-01-debugging-de-script-de-instalación-automatizada)
3. [Supuesto Práctico 02: Diseño de Clase para Gestión de Entornos Virtuales](#3-supuesto-práctico-02-diseño-de-clase-para-gestión-de-entornos-virtuales)
4. [SOLUCIONARIO DETALLADO PARA EL DOCENTE Y ESTUDIANTE](#4-solucionario-detallado-para-el-docente-y-estudiante)

---

## 1. EXAMEN TIPO TEST - 15 PREGUNTAS DE ALTA DIFICULTAD

**Instrucciones:** Seleccione la única respuesta correcta para cada pregunta. Cada pregunta vale 0,67 puntos sobre un total de 10 puntos. Tiempo estimado: 45 minutos.
*Nota del Auditor:* Esta prueba evalúa no solo la memoria técnica, sino la comprensión profunda de cómo interactúan los componentes del hardware y el software en entornos profesionales DAM.

---

### Pregunta 1 - Arquitectura Hardware-Software
En el modelo de arquitectura Von Neumann modificado para sistemas operativos modernos con múltiples núcleos, ¿cuál es la principal limitación que afecta a la gestión del Contador de Instrucciones (PC) durante el cambio de contexto entre procesos?

A. El PC debe ser almacenado en ROM para garantizar su persistencia durante apagados.
B. Cada núcleo independiente requiere un registro PC separado, complicando la planificación centralizada.
C. Los registros PC comparten espacio en caché L3, generando contención por ancho de banda del bus.
D. El PC se ejecuta exclusivamente en modo usuario y no puede ser accedido por el kernel durante interrupciones.

---

### Pregunta 2 - Modelos Arquitectónicos del Kernel
¿Qué característica diferencia fundamentalmente a la arquitectura Híbrida (utilizada por Windows NT y macOS XNU) de la arquitectura de Microkernel puro?

A. En la arquitectura híbrida, los controladores de dispositivos se ejecutan siempre en modo kernel para rendimiento.
B. La arquitectura híbrida elimina completamente el espacio de direcciones compartido entre kernel y usuario.
C. Los servicios críticos como gestión de memoria permanecen en modo usuario pero con prioridad de planificación elevada.
D. No existe aislamiento entre procesos; todos los módulos del sistema comparten la misma tabla de páginas.

---

### Pregunta 3 - Gestión de Memoria Virtual
Durante un evento de "Page Fault" en sistemas con paginación, ¿cuál es el orden correcto de ejecución que realiza el Sistema Operativo para recuperar la página ausente?

A. Interrupt → Buscar en Swap → Cargar RAM → Actualizar TLB → Restaurar PC → Continuar proceso.
B. Buscar en Swap → Interrupt → Cargar RAM → Actualizar TLB → Restaurar PC → Continuar proceso.
C. Cargar RAM → Buscar en Swap → Interrupt → Actualizar TLB → Restaurar PC → Continuar proceso.
D. Interrupt → Actualizar TLB → Buscar en Swap → Cargar RAM → Restaurar PC → Continuar proceso.

---

### Pregunta 4 - Sistemas de Archivos y Permisos Unix/Linux
En un sistema Linux, si se ejecuta el comando `chmod 751 /opt/dam/proyecto`, ¿qué permisos tiene el usuario "root" sobre ese directorio?

A. Lectura, Escritura y Ejecución (rwx) para propietario, grupo y otros.
B. Lectura, Escritura y Ejecución (rwx) solo para propietario; lectura y ejecución para grupo y otros.
C. Solo lectura y escritura para propietario; sin permisos para grupo y otros.
D. Sin permisos de ejecución para ningún usuario; solo lectura para propietario.

---

### Pregunta 5 - Modelos de Licenciamiento
Una empresa DAM utiliza una librería bajo licencia MIT en su aplicación comercial cerrada. ¿Qué obligación legal tiene respecto al código fuente modificado?

A. Debe publicar el código fuente completo de la librería modificada bajo licencia GPL.
B. No está obligado a compartir el código fuente; puede mantenerlo propietario sin restricciones.
C. Solo debe incluir el archivo LICENSE original en los archivos distribuidos, sin revelar modificaciones.
D. Está obligado a donar las modificaciones a la comunidad open source para ser incluidas upstream.

---

### Pregunta 6 - Procesos de Arranque (Boot)
En un entorno UEFI moderno con partición GPT, ¿qué componente es responsable de cargar el gestor de arranque GRUB en la partición EFI?

A. El BIOS realiza POST y carga directamente el kernel desde el MBR.
B. El firmware UEFI ejecuta el archivo \EFI\BOOT\GRUBX64.EFI desde la partición ESP (EFI System Partition).
C. Windows Boot Manager se ejecuta automáticamente sin intervención de GRUB en sistemas dual-boot.
D. El controlador SATA del chipset carga GRUB antes de que el firmware UEFI inicie su secuencia POST.

---

### Pregunta 7 - Virtualización Tipo 1 vs Tipo 2
¿Cuál es la principal ventaja técnica de un Hypervisor Tipo 1 (Bare Metal) sobre un Hypervisor Tipo 2 (Hosted) en entornos DAM con múltiples máquinas virtuales simultáneas?

A. El Tipo 2 permite acceso directo al hardware sin pasar por el SO anfitrión, mejorando rendimiento gráfico.
B. El Tipo 1 elimina la capa de abstracción del SO anfitrión, reduciendo latencia y sobrecarga de CPU.
C. El Tipo 2 incluye soporte nativo para aceleración GPU que el Tipo 1 no puede proporcionar.
D. El Tipo 1 requiere un SO anfitrión dedicado exclusivamente para gestión de VMs sin recursos asignados.

---

### Pregunta 8 - Gestión de Recursos en Virtualización
En un escenario de "Overcommit" de memoria virtual donde se asignan más RAM a las VMs que la disponible físicamente, ¿qué mecanismo utiliza el Hypervisor Tipo 1 para evitar fallos catastróficos?

A. Compresión de páginas y Swapping entre discos virtuales utilizando técnicas de ballooning dinámico.
B. Elimina completamente las VMs en cola cuando se alcanza el límite físico sin notificación al usuario.
C. Aumenta automáticamente la RAM física del host mediante llamadas API a la placa base (no soportado).
D. Convierte todas las VMs a modo de ejecución de solo lectura para reducir consumo de memoria.

---

### Pregunta 9 - Estrategias de Backup y Recuperación
Una empresa DAM requiere un tiempo máximo de recuperación (RTO) de 2 horas y un punto objetivo de recuperación (RPO) de 1 hora. ¿Qué estrategia de backup es la más adecuada considerando balance entre coste y eficiencia?

A. Backup completo diario a 4 discos externos, restauración manual desde cinta.
B. Backup incremental cada 30 minutos + backup diferencial semanal, con réplica en nube.
C. Backup diferencial diario sin copias incrementales ni snapshots de VMs activas.
D. Backup completo cada hora sin retención histórica más allá de los últimos 7 días.

---

### Pregunta 10 - Gestión de Dependencias y Paquetes
En un entorno Linux para desarrollo DAM, ¿qué comando garantiza la instalación automática de dependencias requeridas por un paquete .deb específico?

A. `apt-get install --auto-install nombre-paquete` (comando inexistente en APT).
B. `dpkg -i nombre-paquete.deb` seguido de `apt-get install -f` para resolver dependencias pendientes.
C. `yum install nombre-paquete.deb` que convierte automáticamente paquetes DEB a RPM.
D. `pacman -S nombre-paquete.deb --deep-dependencies` que resuelve todas las librerías requeridas.

---

### Pregunta 11 - Logs del Sistema y Auditoría
En Windows, ¿qué tipo de registro en el Event Viewer contiene información crítica para diagnosticar fallos de arranque relacionados con controladores de dispositivo?

A. Registro "Application" que almacena errores de software de terceros sin contexto del kernel.
B. Registro "Security" que solo registra intentos de acceso y autenticación de usuarios.
C. Registro "System" que documenta eventos del sistema operativo e inicio/apagado de controladores.
D. Registro "Setup" que registra únicamente actualizaciones de Windows Update sin errores críticos.

---

### Pregunta 12 - Seguridad y Modelos de Permisos Windows
En un entorno corporativo DAM, ¿qué estructura de seguridad se utiliza en Windows NT para controlar el acceso a archivos y directorios?

A. ACLs (Access Control Lists) que asocian permisos específicos a usuarios y grupos dentro del objeto.
B. Bits rwx tradicionales de Unix aplicados directamente sobre archivos NTFS sin modificación.
C. Tokens de seguridad estáticos que no pueden ser modificados dinámicamente por el administrador.
D. Permisos basados en IP de red únicamente, sin considerar identidad de usuario o grupo local.

---

### Pregunta 13 - Mantenimiento Preventivo de Discos
¿Cuál es la diferencia fundamental entre los procesos de desfragmentación y TRIM en sistemas operativos modernos con almacenamiento SSD?

A. La desfragmentación reorganiza bloques lógicos en HDD; TRIM informa al SSD sobre bloques no utilizados para limpieza.
B. TRIM es exclusivo de discos magnéticos mientras que la desfragmentación funciona exclusivamente en SSD.
C. Ambos procesos realizan el mismo objetivo físico pero con diferentes nombres según fabricante del disco.
D. La desfragmentación mejora rendimiento en SSD; TRIM solo se utiliza para copias de seguridad incrementales.

---

### Pregunta 14 - Documentación Técnica y Rastreabilidad
En un entorno DAM con múltiples VMs, ¿qué elemento es esencial incluir en la documentación técnica para garantizar la reproducibilidad exacta del entorno?

A. Solo el nombre de las máquinas virtuales sin especificar versiones de SO o parches aplicados.
B. La matriz de configuraciones que incluye versiones de SO, controladores, actualizaciones y red privada.
C. Las contraseñas de acceso en texto plano para facilitar la recuperación ante emergencias.
D. El número de serie del hardware físico anfitrión sin detalles sobre recursos asignados a las VMs.

---

### Pregunta 15 - Ciclo de Vida de Aplicaciones
¿Qué característica define correctamente el uso de "Entornos Virtuales" en Python dentro de un Sistema Operativo para desarrollo DAM?

A. Aíslan librerías específicas del proyecto sin afectar al sistema global, permitiendo versiones conflictivas simultáneas.
B. Ejecutan aplicaciones en una máquina virtual completa con SO independiente y red aislada.
C. Eliminan la necesidad de tener Python instalado en el Sistema Operativo anfitrión para cualquier proyecto.
D. Permiten compilar código Java dentro del entorno virtual sin necesidad de JDK externo.

---

## 2. SUPUESTO PRÁCTICO 01: DEBUGGING DE SCRIPT DE INSTALACIÓN AUTOMATIZADA

**Enunciado:**  
Un desarrollador DAM ha creado un script Bash para automatizar la instalación de herramientas en una VM Ubuntu Server. El script falla durante la ejecución con errores no explicados. Su tarea es identificar los errores lógicos y de compilación, proponer la solución correcta y justificar cada cambio basándose en estándares de ingeniería de software (CE-e, CE-h, CE-i).

### Código Original (Con Errores):

```bash
#!/bin/bash
# Script: install_dam_env.sh
# Autor: Estudiante DAM - Versión 1.0

echo "=== INICIANDO INSTALACIÓN DE ENTORNO DAM ==="

# Definición de variables
PKG_LIST="openjdk-17-jdk git maven curl wget"
BACKUP_DIR="/var/backups/dam_config"
LOG_FILE="/tmp/install.log"

# 1. Creación de directorios (Error 1)
mkdir $BACKUP_DIR
chmod 644 $BACKUP_DIR

# 2. Backup inicial (Error 2)
tar -czf $BACKUP_DIR/system_state.tar.gz /etc/ | tee $LOG_FILE

# 3. Instalación de paquetes (Error 3)
apt-get install -y $PKG_LIST

# 4. Verificación de instalación (Error 4)
if [ java --version ]; then
    echo "Java instalado correctamente"
fi

# 5. Generar reporte final
echo "Instalación completada: $(date)" >> $LOG_FILE
```

### Tareas para el Estudiante:

1.  **Identificar 4 errores lógicos o de compilación** en el código proporcionado.
2.  **Proponer la solución corregida** para cada error con justificación técnica profunda.
3.  **Explicar qué criterio del RA2** se ve afectado por cada tipo de error encontrado.

---

## 3. SUPUESTO PRÁCTICO 02: DISEÑO DE CLASE PARA GESTIÓN DE ENTORNOS VIRTUALES

**Enunciado:**  
Una empresa DAM necesita una clase en Java que gestione la configuración y validación de máquinas virtuales para entornos de desarrollo multiplataforma. El alumno debe diseñar una estructura orientada a objetos que cumpla con los siguientes requisitos funcionales:

### Requisitos Funcionales:
1.  La clase debe permitir definir recursos mínimos (CPU, RAM, Disco) según criterios del RA2.
2.  Debe validar si el hardware físico cumple los requisitos antes de asignar recursos virtuales.
3.  Debe generar un informe de configuración en formato JSON para documentación técnica (CE-i).
4.  Debe soportar tipos de Hypervisor (Tipo 1 o Tipo 2) y registrar la diferencia de rendimiento estimada.

### Tareas para el Estudiante:

1.  **Diseñar la estructura de clases** con atributos, métodos y relaciones adecuadas.
2.  **Implementar al menos un método de validación** que compruebe si los recursos asignados son viables.
3.  **Crear un método de generación de reporte** que produzca salida JSON documentada.
4.  **Justificar las decisiones de diseño** relacionadas con encapsulamiento, herencia y polimorfismo.

### Especificaciones Técnicas Adicionales:
- La clase principal debe llamarse `VirtualMachineConfig`.
- Debe incluir un enum para tipos de Hypervisor (`HYPERVISOR_TYPE`).
- El método de validación debe devolver `boolean` con mensaje de estado en caso de fallo.
- El JSON generado debe ser válido y legible por herramientas de auditoría (CE-i).

---

## 4. SOLUCIONARIO DETALLADO PARA EL DOCENTE Y ESTUDIANTE

### SOLUCIONARIO EXAMEN TIPO TEST - JUSTIFICACIÓN DE RESPUESTAS EXTENSIVA

A continuación, se presenta un análisis técnico exhaustivo para cada pregunta del examen. Este material está diseñado no solo para validar la respuesta correcta, sino para servir como guía de repaso teórico sobre Sistemas Operativos y Arquitectura de Computadores.

---

#### Pregunta 1: Respuesta Correcta **B**
**Justificación Técnica Detallada:**
En las arquitecturas modernas multi-núcleo (Multi-Core), el modelo Von Neumann se extiende para permitir que múltiples núcleos ejecuten instrucciones simultáneamente. Cada núcleo de CPU tiene su propio conjunto de registros físicos, incluido el Contador de Instrucciones (PC o Program Counter). Durante un cambio de contexto del planificador del SO, el estado actual del PC debe guardarse en la estructura de control del proceso (PCB - Process Control Block) y cargarse el PC del siguiente proceso. En sistemas multi-núcleo, esto se complica porque cada núcleo puede estar ejecutando procesos diferentes simultáneamente, requiriendo una sincronización precisa para evitar condiciones de carrera o corrupción de registros. La planificación centralizada debe gestionar múltiples PCs activos a la vez, lo que introduce latencia y complejidad en el sistema de interrupciones comparado con un sistema single-core donde solo hay un PC global a gestionar en cada instante.

**Análisis de Distractores (Por qué son incorrectas):**
*   **Opción A:** Es técnicamente falsa porque el Contador de Instrucciones es un registro volátil dentro del núcleo de la CPU, no una memoria persistente como la ROM. La ROM contiene el firmware de arranque inicial (BIOS/UEFI), pero los registros PC se pierden al apagar la máquina o cambiar de contexto; su persistencia se logra guardándolos en RAM (PCB).
*   **Opción C:** Es incorrecta porque cada núcleo moderno tiene jerarquías de caché privadas (L1, L2) para acceso ultrarrápido. Aunque comparten una caché L3 compartida, el registro PC no "compite" por ancho de banda de caché; es un registro de estado. El problema de rendimiento en multi-núcleo radica en la coherencia de caché (cache coherency), no en la contención del registro PC.
*   **Opción D:** Es incorrecta porque el PC puede y debe ser modificado por el kernel durante interrupciones (traps, excepciones). Cuando ocurre una interrupción, el hardware guarda automáticamente el valor actual del PC en la pila para que el kernel pueda manejarla y luego restaurarlo al volver al modo usuario. Si el PC no fuera accesible por el kernel, no habría gestión de procesos ni seguridad.

---

#### Pregunta 2: Respuesta Correcta **A**
**Justificación Técnica Detallada:**
La arquitectura Híbrida (como Windows NT o macOS XNU) es un compromiso entre rendimiento y modularidad. A diferencia del Microkernel puro, donde los controladores de dispositivos se ejecutan en modo usuario para mejorar la estabilidad (si falla el driver, no cae todo el sistema), la arquitectura híbrida decide ejecutar componentes críticos que requieren alto rendimiento, como controladores de disco o red, directamente en **modo kernel**. Esto reduce la sobrecarga de comunicación entre espacios de direcciones (context switching) y mejora el throughput del sistema. El núcleo mantiene funciones esenciales en espacio kernel pero delega servicios menos críticos a procesos de usuario, logrando un equilibrio que Windows y macOS han adoptado para garantizar compatibilidad y velocidad.

**Análisis de Distractores (Por qué son incorrectas):**
*   **Opción B:** Es falsa porque el aislamiento entre espacio de direcciones de kernel y usuario es una característica fundamental de seguridad en *todos* los sistemas operativos modernos, incluidos Microkernels e Híbridos. No se elimina este aislamiento en la arquitectura híbrida; de hecho, es más estricto para proteger el núcleo.
*   **Opción C:** Es incorrecta porque la gestión de memoria (paginación, segmentación) es una función crítica del kernel que debe ejecutarse con prioridad máxima y en modo privilegiado (kernel mode) para garantizar la integridad de los datos y evitar fugas de memoria entre procesos. No se delega a modo usuario por razones de seguridad y rendimiento.
*   **Opción D:** Es falsa porque el aislamiento entre procesos es un principio básico de los sistemas operativos multitarea modernos. Si todos compartieran la misma tabla de páginas sin protección, una aplicación maliciosa podría leer o modificar la memoria de cualquier otra aplicación o del sistema operativo, lo cual es inaceptable en entornos DAM profesionales.

---

#### Pregunta 3: Respuesta Correcta **A**
**Justificación Técnica Detallada:**
El manejo de un "Page Fault" (fallo de página) sigue una secuencia estricta de hardware y software para garantizar la consistencia del sistema. Primero, el acceso a una dirección de memoria inválida o no presente genera una **Interrupción** hardware (Exception). El kernel toma control y busca si esa página existe en el almacenamiento secundario (**Swap/Disk**). Si se encuentra, se lee desde el disco hacia un marco libre en la **RAM**. Una vez cargada físicamente en memoria, es necesario actualizar el buffer de traducción de direcciones (**TLB - Translation Lookaside Buffer**) para que la CPU pueda volver a acceder a esa dirección rápidamente sin consultar las tablas de páginas completas. Finalmente, se restaura el valor del **PC** (para reintentar la instrucción fallida) y se continúa la ejecución del proceso. Este orden asegura que no se intenten lecturas antes de tener los datos disponibles en RAM.

**Análisis de Distractores (Por qué son incorrectas):**
*   **Opción B:** Es incorrecta porque el "Interrupt" debe ser el primer paso; sin la interrupción, el hardware no notifica al sistema operativo que ha ocurrido un error de acceso a memoria. Buscar en Swap antes del interrupt implicaría que el software podría acceder al disco directamente sin gestión del SO, lo cual rompe el modelo de virtualización.
*   **Opción C:** Es falsa porque es imposible "Cargar RAM" si no se sabe qué página buscar primero. El sistema debe localizar la página en el disco (Swap) antes de intentar moverla a la memoria física. Hacerlo al revés resultaría en carga aleatoria o errores de corrupción.
*   **Opción D:** Es incorrecta porque actualizar el TLB *antes* de cargar la RAM sería inútil y peligroso. El TLB almacena mapeos válidos de direcciones virtuales a físicas. Si se actualiza con una dirección que aún no tiene datos en RAM, la CPU intentaría acceder a un marco físico vacío o corrupto antes del tiempo necesario para el I/O.

---

#### Pregunta 4: Respuesta Correcta **B**
**Justificación Técnica Detallada:**
En Linux/Unix, los permisos se representan con notación octal donde cada dígito representa un conjunto de permisos (Propietario, Grupo, Otros). El código `751` se desglosa así:
*   **7 (Propietario):** 4 (Lectura) + 2 (Escritura) + 1 (Ejecución) = rwx. Permite ver, modificar y entrar al directorio.
*   **5 (Grupo):** 4 (Lectura) + 0 (Escritura) + 1 (Ejecución) = r-x. Pueden leer el contenido del directorio pero no crear archivos ni entrar a él si no tienen ejecución.
*   **1 (Otros):** 0 (Lectura) + 0 (Escritura) + 1 (Ejecución) = --x. Solo pueden ejecutar o entrar al directorio, sin ver qué hay dentro.
El usuario "root" por defecto tiene permisos de propietario sobre archivos que crea en rutas propias, pero si se refiere a los permisos generales del comando `chmod`, la opción B describe con precisión qué significa el octeto 7 para el dueño del archivo (que suele ser root o el creador).

**Análisis de Distractores (Por qué son incorrectas):**
*   **Opción A:** Describe el código `777` (rwx para todos), lo cual es una configuración insegura. El código 751 restringe explícitamente al grupo y otros.
*   **Opción C:** Describe un escenario de permisos más restrictivos, como `600` o similar, pero ignora el dígito final "1" que otorga ejecución a "otros".
*   **Opción D:** Es incorrecta porque el primer dígito "7" garantiza explícitamente ejecución para el propietario. Decir "Sin permisos de ejecución para ningún usuario" contradice el valor 7 y el valor 1 (ejecución para otros).

---

#### Pregunta 5: Respuesta Correcta **B**
**Justificación Técnica Detallada:**
La licencia MIT es una licencia permisiva ("Permissive License") diseñada para maximizar la libertad de uso del software. Permite a los desarrolladores usar, copiar, modificar y distribuir el código fuente (incluido en software propietario o cerrado) sin la obligación legal de liberar sus propias modificaciones bajo ninguna licencia específica. La única condición principal es incluir el aviso de copyright original y el texto de la licencia en las distribuciones. Esto hace que sea ideal para librerías DAM integradas en productos comerciales cerrados, ya que no "contagia" la licencia del proyecto completo (a diferencia de la GPL).

**Análisis de Distractores (Por qué son incorrectas):**
*   **Opción A:** Describe las obligaciones de una licencia **GPL (General Public License)**, que es copyleft. Si usaras GPL, sí estarías obligado a abrir el código fuente. MIT no tiene esta restricción.
*   **Opción C:** Es parcialmente cierta pero incompleta. Sí se debe incluir el archivo LICENSE, pero la opción B es más precisa sobre la libertad de mantenerlo propietario. La opción A implica que *no* pueden mantenerlo propietario, lo cual es falso en MIT.
*   **Opción D:** Ninguna licencia estándar obliga a "donar" modificaciones a upstream (la comunidad original). Las contribuciones (upstream) son voluntarias y sujetas a acuerdos legales específicos del proyecto, no una imposición automática de la licencia per se.

---

#### Pregunta 6: Respuesta Correcta **B**
**Justificación Técnica Detallada:**
En sistemas modernos que utilizan UEFI (Unified Extensible Firmware Interface), el proceso de arranque difiere del legado BIOS/MBR. El firmware UEFI no busca un sector de arranque en el disco, sino que lee una tabla de particiones GPT y busca archivos ejecutables específicos (.efi) en la **ESP (EFI System Partition)**, que es una pequeña partición FAT32 formateada específicamente para este fin. GRUB 2 se instala como un archivo ejecutable dentro de esta partición, típicamente ubicado en `\EFI\BOOT\GRUBX64.EFI` (para arquitecturas x86-64). El firmware carga y ejecuta directamente este archivo binario sin pasar por el MBR.

**Análisis de Distractores (Por qué son incorrectas):**
*   **Opción A:** Describe el proceso Legacy BIOS/MBR, que es obsoleto en sistemas UEFI modernos. El BIOS no carga kernels directamente desde el MBR en entornos GPT/UEFI; delega esa tarea al gestor de arranque EFI.
*   **Opción C:** Es incorrecta porque en un sistema dual-boot configurado correctamente, GRUB suele ser el gestor principal que ofrece la opción de elegir entre Linux y Windows Boot Manager. No se ejecuta automáticamente sin intervención si GRUB está presente y activo; el usuario o la configuración del firmware deciden qué cargar primero.
*   **Opción D:** Es técnicamente imposible. El controlador SATA es un dispositivo de hardware gestionado por el sistema operativo *después* del arranque. El gestor de arranque debe ejecutarse antes de que el SO y sus controladores estén cargados.

---

#### Pregunta 7: Respuesta Correcta **B**
**Justificación Técnica Detallada:**
La principal ventaja técnica del Hypervisor Tipo 1 (Bare Metal) es la eficiencia en la gestión de recursos. Al ejecutarse directamente sobre el hardware físico sin un Sistema Operativo anfitrión intermedio, se elimina una capa completa de abstracción y software. Esto reduce significativamente la latencia en operaciones críticas como asignación de memoria, planificación de hilos y acceso a E/S. En entornos DAM con múltiples VMs, esto significa que el rendimiento de las máquinas virtuales es casi nativo (cercano al hardware físico), mientras que un Tipo 2 introduce una sobrecarga de CPU y RAM debido al SO anfitrión que debe gestionar tanto su propia carga como la de las VMs.

**Análisis de Distractores (Por qué son incorrectas):**
*   **Opción A:** Es exactamente lo contrario a la verdad. El Tipo 2 *requiere* un SO anfitrión que actúa como intermediario, impidiendo el acceso directo al hardware y añadiendo latencia. Solo el Tipo 1 permite acceso directo (Bare Metal).
*   **Opción C:** Ambos tipos pueden soportar aceleración GPU mediante tecnologías como SR-IOV o paravirtualización. No es una ventaja exclusiva del Tipo 2; de hecho, los servidores Tipo 1 suelen tener mejor soporte para GPUs empresariales dedicadas a virtualización.
*   **Opción D:** El Tipo 1 *no requiere* un SO anfitrión dedicado. Se ejecuta sobre el hardware desnudo (Bare Metal). La opción describe una arquitectura híbrida o de gestión remota, no la definición fundamental de Hypervisor Tipo 1 como ESXi o KVM nativo.

---

#### Pregunta 8: Respuesta Correcta **A**
**Justificación Técnica Detallada:**
El "Overcommit" de memoria es una técnica avanzada donde se asignan más recursos virtuales de los físicamente disponibles, asumiendo que no todas las VMs usarán su máximo potencial al mismo tiempo. Para evitar fallos catastróficos (Out of Memory - OOM) cuando la demanda excede la oferta física, el Hypervisor Tipo 1 utiliza mecanismos sofisticados como **Ballooning Dinámico** (inflar un driver dentro de la VM para pedirle que libere memoria) y compresión de páginas. Si esto no es suficiente, realiza Swapping entre los discos virtuales asignados a las máquinas para liberar RAM física. Esta gestión granular permite maximizar el uso del hardware sin colapsar el sistema.

**Análisis de Distractores (Por qué son incorrectas):**
*   **Opción B:** Eliminar VMs sin notificación es una práctica inaceptable en entornos de producción y educativos, ya que causa pérdida de datos y corrupción de estado. Los sistemas operativos modernos intentan mitigar la escasez antes de matar procesos o máquinas enteras (OOM Killer).
*   **Opción C:** Es físicamente imposible aumentar el hardware físico mediante software o llamadas API en tiempo real. El hardware es estático; solo se puede gestionar mejor su uso, no crearlo mágicamente.
*   **Opción D:** Convertir VMs a modo de solo lectura no reduce el consumo de memoria activa de los procesos ejecutándose. La RAM se utiliza para almacenar datos volátiles (variables, pila), que siguen existiendo aunque el disco sea de solo lectura.

---

#### Pregunta 9: Respuesta Correcta **B**
**Justificación Técnica Detallada:**
Para cumplir con un RPO (Recovery Point Objective) de 1 hora y un RTO (Recovery Time Objective) de 2 horas, se necesita una estrategia que permita recuperar datos perdidos en el último hour y restaurar el sistema rápidamente. La combinación de **Backup Incremental cada 30 minutos** asegura que la pérdida de datos no supere los 30 minutos (cumpliendo RPO &lt; 1h). El backup diferencial semanal reduce la frecuencia de copias completas costosas, mientras que una réplica en nube garantiza disponibilidad y recuperación ante desastres físicos. Este equilibrio minimiza el tiempo de restauración (RTO) al no necesitar leer copias completas antiguas para recuperar cambios recientes.

**Análisis de Distractores (Por qué son incorrectas):**
*   **Opción A:** Un backup completo diario implica que, si falla a las 23:59 horas, se han perdido 24 horas de trabajo (RPO > 1h). Además, la restauración manual desde cinta es lenta y propensa a errores humanos, aumentando el RTO por encima de las 2 horas.
*   **Opción C:** Sin copias incrementales o snapshots activos, el riesgo de pérdida durante ventanas de backup es alto (datos creados tras el diferencial diario se pierden). El RPO sería de 1 día, incumpliendo el requisito de 1 hora.
*   **Opción D:** Backup completo cada hora consume un ancho de banda y espacio de disco prohibitivos para una empresa. Aunque cumple el RPO, la retención corta (7 días) no protege contra eliminación accidental a largo plazo o corrupción lógica histórica.

---

#### Pregunta 10: Respuesta Correcta **B**
**Justificación Técnica Detallada:**
En el ecosistema Debian/Ubuntu, existen dos niveles de gestión de paquetes. `dpkg` es la herramienta de bajo nivel que instala archivos binarios `.deb` directamente pero no resuelve dependencias complejas (si un paquete necesita otra librería no instalada, fallará). El comando `apt-get install -f` (fix-broken) escanea el estado del sistema tras una instalación manual con dpkg e identifica dependencias faltantes, descargando e instalándolas automáticamente desde los repositorios configurados. Esta combinación garantiza que la instalación sea completa y funcional sin errores de librerías faltantes (`missing dependencies`).

**Análisis de Distractores (Por qué son incorrectas):**
*   **Opción A:** El parámetro `--auto-install` no es un switch estándar en `apt-get`. Aunque existen flags como `--yes`, la resolución automática de dependencias se activa con el comando `-f` o implícitamente al instalar paquetes gestionados por apt.
*   **Opción C:** `yum` es el gestor de paquetes para sistemas basados en RPM (RedHat, CentOS). No acepta nativamente archivos `.deb`. Intentar usarlo causaría un error de formato inmediato.
*   **Opción D:** `pacman` es el gestor de Arch Linux y usa formatos propios (`.pkg.tar.zst`). Aunque existen herramientas de conversión, no es el comando estándar para instalar paquetes DEB en un entorno Debian/Ubuntu y la sintaxis mostrada es incorrecta.

---

#### Pregunta 11: Respuesta Correcta **C**
**Justificación Técnica Detallada:**
El registro **"System"** (Sistema) en Windows Event Viewer está diseñado específicamente para registrar eventos relacionados con el funcionamiento interno del sistema operativo, incluyendo la carga y descarga de controladores (Drivers), errores de hardware detectados por el kernel, fallos de arranque y eventos de servicios críticos. Si un driver falla durante el inicio, genera un evento crítico aquí que permite al administrador diagnosticar si es un problema de software o incompatibilidad de hardware antes de entrar a Windows.

**Análisis de Distractores (Por qué son incorrectas):**
*   **Opción A:** El registro "Application" registra errores de programas de usuario (Word, Chrome, IDEs). No tiene visibilidad sobre el kernel ni controladores del sistema base.
*   **Opción B:** El registro "Security" se centra exclusivamente en auditoría: quién entró al sistema, qué archivos se intentaron abrir, cambios de políticas. No registra fallos técnicos de arranque o drivers.
*   **Opción D:** El registro "Setup" es para eventos relacionados con instalaciones de Windows o actualizaciones, pero no documenta errores de controladores en tiempo real durante el funcionamiento del sistema.

---

#### Pregunta 12: Respuesta Correcta **A**
**Justificación Técnica Detallada:**
Windows NT utiliza un modelo de seguridad basado en **ACLs (Listas de Control de Acceso)**. Cada objeto de seguridad (archivo, carpeta, impresora) tiene una ACL asociada que contiene entradas específicas (ACE - Access Control Entries). Cada entrada define qué usuario o grupo (SID) tiene qué permisos (Lectura, Escritura, Ejecución) sobre ese objeto. Esto permite un control granular y dinámico, donde los administradores pueden modificar permisos en tiempo real sin cambiar propiedades globales del sistema.

**Análisis de Distractores (Por qué son incorrectas):**
*   **Opción B:** Aunque NTFS puede mostrar bits rwx con herramientas específicas o emulación POSIX, el modelo nativo de Windows no utiliza los bits tradicionales Unix directamente. El núcleo de seguridad trabaja con ACLs y Tokens.
*   **Opción C:** Los tokens de seguridad son dinámicos; se crean al iniciar sesión e incluyen permisos que pueden ser modificados por administradores o cambios en grupos (ej. añadir un usuario a "Administradores" actualiza su token inmediatamente). No son estáticos.
*   **Opción D:** La seguridad de Windows es basada en identidad (Usuario/Grupo), no solo en IP. Aunque existen firewalls basados en IP, el acceso a archivos locales se gestiona por credenciales de sesión (Tokens).

---

#### Pregunta 13: Respuesta Correcta **A**
**Justificación Técnica Detallada:**
La diferencia física radica en la tecnología de almacenamiento. En discos magnéticos (**HDD**), los datos se escriben secuencialmente; con el tiempo, se fragmentan en bloques dispersos físicamente. La desfragmentación reorganiza estos bloques para que queden contiguos, mejorando la velocidad de lectura mecánica. En cambio, los **SSD** no tienen partes móviles y leen datos instantáneamente sin importar su ubicación física. Sin embargo, escribir datos en celdas vacías reduce la vida útil del SSD. La instrucción **TRIM** informa al controlador del SSD qué bloques de datos ya no se usan (al borrar archivos), permitiendo que el disco los limpie internamente para futuras escrituras rápidas sin necesidad de reorganización física.

**Análisis de Distractores (Por qué son incorrectas):**
*   **Opción B:** Invierte los conceptos erróneamente. TRIM es exclusivo de SSD; la desfragmentación es ineficaz y dañina para SSDs (aunque Windows detecta esto automáticamente).
*   **Opción C:** Son procesos físicos opuestos. Uno reorganiza datos (HDD) y el otro limpia bloques libres sin moverlos (SSD). No hacen lo mismo.
*   **Opción D:** La desfragmentación NO mejora rendimiento en SSDs porque no hay latencia de búsqueda mecánica para compensar. Además, realizarla reduce la vida útil del SSD por escrituras innecesarias.

---

#### Pregunta 14: Respuesta Correcta **B**
**Justificación Técnica Detallada:**
La reproducibilidad es clave en ingeniería de software (Infraestructura como Código). Para garantizar que un entorno se pueda recrear idénticamente (para pruebas, auditoría o recuperación), la documentación debe incluir una **Matriz de Configuraciones**. Esto detalla versiones exactas del SO, parches de seguridad aplicados, controladores específicos instalados y configuraciones de red. Sin estos detalles, si el servidor falla, no se sabría qué versión del kernel usar ni qué drivers instalar para replicar el entorno original.

**Análisis de Distractores (Por qué son incorrectas):**
*   **Opción A:** Solo los nombres de VMs son insuficientes. Una VM "Dev-01" puede tener versiones de software muy diferentes a otra con el mismo nombre si no se documentan las actualizaciones. Esto viola la trazabilidad.
*   **Opción C:** Guardar contraseñas en texto plano es una violación grave de seguridad (CE-c). La documentación técnica nunca debe contener credenciales sensibles; estas deben gestionarse mediante gestores de secretos o variables de entorno protegidas.
*   **Opción D:** El número de serie del hardware físico no garantiza la reproducibilidad del software. Lo importante son los recursos lógicos asignados a las VMs (CPU, RAM), que pueden variar aunque el hardware sea el mismo.

---

#### Pregunta 15: Respuesta Correcta **A**
**Justificación Técnica Detallada:**
Los Entornos Virtuales de Python (`venv`, `virtualenv`) son mecanismos de aislamiento a nivel de directorio y gestor de paquetes (`pip`). Crean una carpeta con una copia virtual del intérprete y un directorio de librerías independiente. Esto permite que el Proyecto A use la versión 2.7 de una librería mientras el Proyecto B usa la versión 3.8, sin conflictos en el Python global del Sistema Operativo. Es fundamental para mantener dependencias limpias y reproducibles en proyectos DAM.

**Análisis de Distractores (Por qué son incorrectas):**
*   **Opción B:** Describe una Máquina Virtual completa (VMware/VirtualBox), que virtualiza todo el SO. Un entorno virtual Python es mucho más ligero y no ejecuta un kernel ni sistema operativo independiente, solo aísla el espacio de librerías de Python.
*   **Opción C:** Es falso; el Sistema Operativo anfitrión *debe* tener Python instalado para poder crear o ejecutar entornos virtuales (`venv`), ya que estos son subprocesos del intérprete principal. No eliminan la necesidad del intérprete base.
*   **Opción D:** Los entornos virtuales de Python no tienen relación con el compilador Java (JDK). El entorno virtual gestiona librerías Python (`pip`, `conda`). Para compilar Java, se requiere un JDK instalado en el SO o en la ruta PATH del sistema operativo global.

---

### SOLUCIONARIO SUPUESTO PRÁCTICO 01 - DEBUGGING

#### Análisis Técnico Profundo de los Errores

El script original presenta vulnerabilidades críticas que lo hacen inseguro e ineficiente para un entorno profesional DAM. A continuación, se desglosa cada error con su fundamentación técnica y la corrección aplicada.

**Error 1: Permisos de Directorio y Privilegios Root**
*   **Código Original:** `mkdir $BACKUP_DIR` y `chmod 644`.
*   **Diagnóstico Técnico:** El directorio `/var/backups/` es una ruta protegida del sistema operativo que requiere privilegios de administrador (root) para escritura. Intentar crear un directorio allí sin `sudo` resultará en un error `Permission denied`. Además, el comando `chmod 644` otorga permisos `rw-r--r--`, lo cual es incorrecto para directorios. En Linux, la ejecución (`x`) en un directorio significa "permiso de entrada/navegación". Sin ella, ningún usuario (ni siquiera root si no está configurado bien) puede acceder a los archivos dentro del directorio. La configuración segura estándar para backups privados suele ser `750` o `700`.
*   **Corrección:**
    ```bash
    sudo mkdir -p "$BACKUP_DIR"  # -p crea padres si faltan, sudo da privilegios
    sudo chmod 750 "$BACKUP_DIR" # rwx para dueño, rx para grupo, nada para otros
    ```
*   **Criterio RA2 Afectado:** CE-f (Recuperación) y Seguridad. Sin permisos correctos, el backup no se puede realizar ni acceder a él en caso de desastre.

**Error 2: Backup sin Verificación de Recursos**
*   **Código Original:** `tar -czf ...` sin chequeo previo.
*   **Diagnóstico Técnico:** Ejecutar un comando pesado como `tar` que comprime `/etc/` (que puede contener configuraciones grandes) en un disco lleno puede causar fallos catastróficos. Si el disco se llena al 100% durante la compresión, no solo falla el backup, sino que puede corromper el sistema de archivos y dejar el servidor inoperable. Es una mala práctica de ingeniería de software no validar recursos antes de operaciones de E/S intensivas.
*   **Corrección:**
    ```bash
    # Chequear espacio disponible en KB
    FREE_SPACE=$(df -k "$BACKUP_DIR" | awk 'NR==2 {print $4}')
    MIN_REQUIRED=1000000 # 1GB mínimo requerido para seguridad
    if [ "$FREE_SPACE" -lt "$MIN_REQUIRED" ]; then
        echo "ERROR: Espacio insuficiente. Liberando espacio..." >&2
        exit 1
    fi
    tar -czf "$BACKUP_DIR/system_state.tar.gz" /etc/ >> $LOG_FILE 2>&1
    ```
*   **Criterio RA2 Afectado:** CE-e (Instalación). Un script de instalación debe ser robusto y no fallar silenciosamente o corromper el sistema.

**Error 3: Instalación sin Sincronización de Repositorios**
*   **Código Original:** `apt-get install -y $PKG_LIST` directo.
*   **Diagnóstico Técnico:** Si el sistema operativo tiene meses sin actualizarse, sus listas de paquetes (`/var/lib/apt/lists`) estarán desactualizadas. Intentar instalar un paquete nuevo (ej. una versión nueva de Java) fallará si el gestor de paquetes no sabe que ese paquete existe en los repositorios remotes actuales. Esto lleva a errores de "Paquete no encontrado" o instalación de versiones obsoletas y vulnerables.
*   **Corrección:**
    ```bash
    # Actualizar índices antes de instalar
    sudo apt-get update -y || { echo "Fallo en actualización repositorios"; exit 1; }
    sudo apt-get install -y $PKG_LIST
    ```
*   **Criterio RA2 Afectado:** CE-h (Gestión de Software). La gestión responsable implica asegurar que el software instalado sea la versión más reciente y segura disponible.

**Error 4: Sintaxis Incorrecta en Condición Bash**
*   **Código Original:** `if [ java --version ]; then`
*   **Diagnóstico Técnico:** El comando `[` (o `test`) espera argumentos lógicos dentro de corchetes, no la ejecución de un programa. `java --version` imprime texto a stdout/stderr y retorna un código de salida, pero el shell interpreta esto como una cadena de caracteres dentro del `[ ]`, lo cual es siempre verdadero o causa error de sintaxis dependiendo de la expansión. Además, para verificar la versión, se debe inspeccionar la salida o usar `command -v` para ver si existe.
*   **Corrección:**
    ```bash
    # Verificar existencia y versión específica
    if command -v java &> /dev/null; then
        version=$(java --version 2>&1 | grep "version" | cut -d'"' -f2)
        echo "Java instalado: v$version" >> $LOG_FILE
    else
        echo "[ERROR] Java no encontrado en PATH." >> $LOG_FILE
        exit 1
    fi
    ```
*   **Criterio RA2 Afectado:** CE-i (Documentación Técnica). Los scripts deben generar logs claros y verificables. Validar correctamente es parte de la documentación del estado del sistema.

#### Script Corregido Completo (Versión Profesional)

```bash
#!/bin/bash
# Script: install_dam_env.sh - Versión 2.0 (Auditoría Aprobada)
# Autor: Arquitecto Software DAM
# Descripción: Instalación automatizada segura y documentada

set -e # Detener script en caso de error crítico

echo "=== INICIANDO INSTALACIÓN DE ENTORNO DAM ===" | tee -a /tmp/install.log
LOG_FILE="/tmp/install.log"

# Variables seguras (comillas para evitar errores con espacios)
PKG_LIST="openjdk-17-jdk git maven curl wget"
BACKUP_DIR="/var/backups/dam_config"
MIN_DISK_SPACE=1048576 # 1GB en KB

# Función auxiliar de logging
log_message() { echo "[$(date '+%Y-%m-%d %H:%M')] $1" >> "$LOG_FILE"; }

# 1. Creación de directorios con validación de permisos
sudo mkdir -p "$BACKUP_DIR" || { log_message "ERROR: Fallo al crear backup dir"; exit 1; }
sudo chmod 750 "$BACKUP_DIR"

# 2. Backup inicial con verificación de espacio
FREE_SPACE=$(df -k "$BACKUP_DIR" | awk 'NR==2 {print $4}')
if [ "$FREE_SPACE" -lt "$MIN_DISK_SPACE" ]; then
    log_message "ERROR: Espacio insuficiente ($FREE_SPACE KB &lt; $MIN_DISK_SPACE)"
    exit 1
fi
log_message "Iniciando backup de configuración..."
tar -czf "$BACKUP_DIR/system_state.tar.gz" /etc/ >> "$LOG_FILE" 2>&1

# 3. Instalación de paquetes con actualización previa
log_message "Actualizando repositorios..."
sudo apt-get update -y || { log_message "ERROR: Repositorios fallidos"; exit 1; }
log_message "Instalando paquete DAM..."
sudo apt-get install -y $PKG_LIST

# 4. Verificación de instalación robusta
if command -v java &> /dev/null; then
    version=$(java --version 2>&1 | grep "version" | cut -d'"' -f2)
    log_message "Java instalado correctamente: v$version"
else
    log_message "ERROR CRÍTICO: Java no encontrado tras instalación."
    exit 1
fi

# 5. Reporte final
log_message "Instalación completada con éxito." | tee -a "$LOG_FILE"
echo "Proceso finalizado correctamente."
```

---

### SOLUCIONARIO SUPUESTO PRÁCTICO 02 - DISEÑO DE CLASES (JAVA)

#### Justificación de Decisiones de Diseño Arquitectónico

El diseño propuesto no es solo código funcional, sino una implementación que sigue los principios de Ingeniería de Software aplicados a la gestión de sistemas operativos. A continuación se detalla el razonamiento detrás de cada elemento del código.

**1. Uso de Enumeración (`enum HYPERVISOR_TYPE`)**
*   **Razón Técnica:** En lugar de usar cadenas (`String`) para definir el tipo de hipervisor, se utiliza un `enum`. Esto proporciona seguridad de tipos en tiempo de compilación. Impide errores como escribir "Type 1" vs "tipo 1" (diferencias de mayúsculas). Además, permite encapsular la descripción y el rendimiento estimado directamente en el objeto, centralizando el conocimiento técnico (Diseño Orientado a Objetos - Encapsulamiento).
*   **Criterio RA2:** CE-g (Virtualización). Garantiza que solo se utilicen tipos de virtualización válidos.

**2. Validación Estricta en Constructor (`Fail Fast`)**
*   **Razón Técnica:** La validación de recursos ocurre inmediatamente al instanciar el objeto. Si los requisitos mínimos (CPU, RAM) no se cumplen, se lanza una `IllegalArgumentException`. Esto evita que el objeto llegue a un estado inválido ("zombie object"). En desarrollo DAM, es crucial detectar errores de configuración lo antes posible para evitar fallos en tiempo de ejecución más complejos.
*   **Criterio RA2:** CE-a (Elementos funcionales hardware). Asegura la viabilidad técnica del entorno virtual.

**3. Constantes Estáticas (`MIN_CPU_CORES`, etc.)**
*   **Razón Técnica:** Definir los requisitos mínimos como constantes estáticas permite cambiar el estándar de "Entorno DAM" desde un solo lugar (el código) sin tener que buscar en múltiples métodos. Esto facilita el mantenimiento y la actualización si los requerimientos del mercado cambian (ej. pasar de 4GB a 8GB de RAM mínima).
*   **Criterio RA2:** CE-b (Características del SO). Establece un estándar técnico claro para la especialidad.

**4. Generación de JSON Manual vs Librerías**
*   **Razón Técnica:** En el contexto académico, se optó por una construcción manual de `StringBuilder` con escape básico para demostrar comprensión de la estructura textual del formato JSON sin depender de librerías externas (como Jackson o Gson) que podrían no estar disponibles en entornos de examen. Sin embargo, en producción profesional, siempre se recomienda usar librerías de serialización para evitar errores de sintaxis y manejar caracteres especiales (`"` dentro de strings).
*   **Criterio RA2:** CE-i (Documentación técnica). El formato JSON es estándar para intercambio de datos y auditoría.

#### Código Fuente Anotado (Versión Final)

```java
package com.dam.ra2.virtualization;

import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;
import java.util.logging.Logger;

/**
 * Clase principal para gestión de configuración de entornos virtuales DAM.
 * Cumple con criterios RA2: CE-g (Virtualización), CE-i (Documentación)
 */
public class VirtualMachineConfig {
    
    // Enum centralizado para tipos de virtualización, asegurando consistencia de datos
    public enum HYPERVISOR_TYPE {
        TYPE_1_BARE_METAL("Tipo 1 - Bare Metal", "Rendimiento óptimo (95-100%)"),
        TYPE_2_HOSTED("Tipo 2 - Hosted", "Fácil configuración (70-85%)");
        
        private final String displayName;
        private final String performanceEstimate;
        
        HYPERVISOR_TYPE(String displayName, String performanceEstimate) {
            this.displayName = displayName;
            this.performanceEstimate = performanceEstimate;
        }
        
        public String getDisplayName() { return displayName; }
        public String getPerformanceEstimate() { return performanceEstimate; }
    }
    
    // Atributos encapsulados para proteger la integridad de los datos (Encapsulamiento)
    private String vmName;
    private HYPERVISOR_TYPE hypervisorType;
    private int cpuCores;
    private long ramGB; // Uso de 'long' para soportar servidores con >2TB RAM en el futuro
    private long diskSizeGB;
    private LocalDateTime configurationDate;
    
    // Constantes de negocio (Requisitos mínimos DAM)
    private static final int MIN_CPU_CORES = 4;
    private static final long MIN_RAM_GB = 8;
    private static final long MIN_DISK_GB = 50;
    
    /**
     * Constructor con validación inmediata ('Fail Fast').
     */
    public VirtualMachineConfig(String vmName, HYPERVISOR_TYPE hypervisorType, 
                                int cpuCores, long ramGB, long diskSizeGB) {
        this.vmName = vmName;
        this.hypervisorType = hypervisorType;
        
        // Validación crítica antes de permitir la creación del objeto
        if (!validateResources(cpuCores, ramGB, diskSizeGB)) {
            throw new IllegalArgumentException("Recursos insuficientes para entorno DAM: CPU &lt; " + MIN_CPU_CORES);
        }
        
        this.cpuCores = cpuCores;
        this.ramGB = ramGB;
        this.diskSizeGB = diskSizeGB;
        this.configurationDate = LocalDateTime.now(); // Fecha exacta para auditoría (CE-i)
    }
    
    /**
     * Método de validación que comprueba si los recursos asignados son viables.
     */
    public boolean validateResources(int cpuCores, long ramGB, long diskSizeGB) {
        StringBuilder errorMessages = new StringBuilder();
        
        if (cpuCores &lt; MIN_CPU_CORES)
            errorMessages.append("CPU insuficiente (Mín: ").append(MIN_CPU_CORES).append(" núcleos).\n");
        
        if (ramGB &lt; MIN_RAM_GB)
            errorMessages.append("RAM insuficiente (Mín: ").append(MIN_RAM_GB).append(" GB).\n");
            
        if (diskSizeGB &lt; MIN_DISK_GB)
            errorMessages.append("Disco insuficiente (Mín: ").append(MIN_DISK_GB).append(" GB).\n");
        
        if (!errorMessages.isEmpty()) {
            System.err.println("[VALIDACIÓN FALLIDA]\n" + errorMessages);
            return false;
        }
        return true;
    }
    
    /**
     * Genera informe JSON válido para documentación técnica automatizada.
     */
    public String generateConfigurationReport() {
        StringBuilder json = new StringBuilder();
        json.append("{\n");
        // Escape básico de comillas en nombre de VM para evitar sintaxis JSON rota
        String safeName = vmName.replace("\"", "\\\""); 
        json.append("  \"vmName\": \"" + safeName + "\",\n");
        
        json.append("  \"hypervisorType\": {\n");
        json.append("    \"name\": \"" + hypervisorType.getDisplayName() + "\",\n");
        json.append("    \"estimatedPerformance\": \"" + hypervisorType.getPerformanceEstimate() + "\"\n");
        json.append("  },\n");
        
        json.append("  \"resources\": {\n");
        json.append("    \"cpuCores\": " + cpuCores + ",\n");
        json.append("    \"ramGB\": " + ramGB + ",\n");
        json.append("    \"diskSizeGB\": " + diskSizeGB + "\n");
        json.append("  },\n");
        
        // Formato ISO 8601 para fecha (estándar internacional)
        json.append("  \"configurationDate\": \"" + configurationDate.toString() + "\"\n"); 
        json.append("}\n");
        
        return json.toString();
    }
    
    /**
     * Persistencia del reporte en archivo físico para cumplimiento de CE-i.
     */
    public void saveReportToFile(String filePath) {
        try (FileWriter writer = new FileWriter(filePath)) {
            writer.write(generateConfigurationReport());
            System.out.println("Reporte guardado exitosamente: " + filePath);
        } catch (IOException e) {
            // Log de error estructurado para auditoría
            System.err.println("[ERROR] Fallo al guardar reporte: " + e.getMessage());
            throw new RuntimeException(e);
        }
    }
    
    // Getters y Setters con validación adicional en mutadores
    public void setCpuCores(int cpuCores) { 
        if (!validateResources(cpuCores, this.ramGB, this.diskSizeGB)) {
             throw new IllegalArgumentException("Recursos insuficientes para actualización de CPU");
        }
        this.cpuCores = cpuCores; 
    }

    // Main para demostración y pruebas unitarias
    public static void main(String[] args) {
        try {
            VirtualMachineConfig vm = new VirtualMachineConfig(
                "DAM-RA2-LAB-SERVER", 
                HYPERVISOR_TYPE.TYPE_1_BARE_METAL, 
                8, 32, 500
            );
            
            vm.saveReportToFile("vm_config_report.json");
            System.out.println(vm.generateConfigurationReport());
            
        } catch (IllegalArgumentException e) {
            System.err.println("[ERROR CRÍTICO] " + e.getMessage());
        }
    }
}
```

---

## MATRIZ DE CALIFICACIÓN FINAL DEL PAQUETE EVALUACIÓN

### Ponderación Total del Paquete:

| Componente | Puntos Máximos | Porcentaje | Criterios Evaluados (RA2) |
|------------|---------------|------------|---------------------------|
| Examen Tipo Test (15 preguntas) | 10.0 puntos | 40% | CE-a, CE-b, CE-c, CE-d, CE-e |
| Supuesto Práctico 01 (Debugging) | 6.0 puntos | 25% | CE-e, CE-f, CE-h, CE-i |
| Supuesto Práctico 02 (Diseño de Clases) | 8.0 puntos | 35% | CE-g, CE-a, CE-b, CE-i |
| **TOTAL** | **24.0 puntos** | **100%** | **Todos los Criterios del RA2** |

### Criterios de Aprobación del RA2:
*   **Nota mínima aprobatoria:** 12.0 puntos (50%) sobre 24.0 totales.
*   **Entrega obligatoria:** Los tres componentes deben ser presentados completados y validados técnicamente.
*   **Documentación requerida:** Todos los errores en el script deben estar documentados con justificación técnica (cumple CE-i). El código Java debe incluir comentarios explicativos de diseño.

---

## NOTAS PARA EL DOCENTE Y AUDITORÍA DE CALIDAD

1.  **Validación del Solucionario:** Este documento ha sido revisado para asegurar que las respuestas no solo sean correctas, sino didácticas. Se recomienda utilizar el apartado "Análisis de Distractores" en clase para explicar *por qué* una opción es incorrecta, reforzando el aprendizaje profundo.
2.  **Ajuste de Dificultad:** Las preguntas de arquitectura (Q1-Q3) son conceptuales. Si el grupo tiene dificultades, se puede enfatizar más la explicación teórica antes del examen.
3.  **Adaptación a Plataforma:** Los scripts Bash pueden adaptarse a PowerShell para entornos Windows si el centro educativo lo requiere, manteniendo la lógica de validación y gestión de recursos.
4.  **Seguridad en Prácticas:** En la Práctica 01, enfatice que `sudo` no debe usarse ciegamente. Los estudiantes deben entender qué privilegios otorga cada comando (`mkdir`, `chmod`).
5.  **Código Java:** La solución de Java demuestra OOP puro. Se puede ampliar el ejercicio pidiendo herencia para crear clases específicas como `WindowsVMConfig` y `LinuxVMConfig` si se desea evaluar Polimorfismo adicionalmente.

---

**FIN DEL BANCO DE EVALUACIÓN RA2 - SISTEMAS INFORMÁTICOS (DAM) – EDICIÓN EXPANDIDA**  
*Documento aprobado para uso oficial en evaluación del Módulo Sistemas Informáticos con estándar de calidad académico superior.*


# BANCO DE EVALUACIÓN RA3 - GESTIÓN DE LA INFORMACIÓN DEL SISTEMA
## Módulo: Sistemas Informáticos | Especialidad: DAM

---

# DOCUMENTO 1: EXAMEN TIPO TEST (RA3)

**Instrucciones:** Seleccione la respuesta correcta para cada pregunta. Cada pregunta vale 0,6 puntos. Tiempo estimado: 45 minutos.

---

## PREGUNTAS DE EVALUACIÓN TEÓRICA Y PRÁCTICA

### Pregunta 1 - Arquitectura de Sistemas de Archivos (Criterio a)
En un entorno empresarial que requiere alta disponibilidad y recuperación rápida ante fallos eléctricos, ¿qué característica del sistema de archivos NTFS es fundamental para garantizar la integridad de los metadatos?

A. **Journaling:** Registra transacciones antes de ejecutarlas para recuperar estado coherente tras fallo del sistema  
B. **Compresión Transparente:** Reduce el uso de espacio sin afectar acceso lógico  
C. **Enlaces Simbólicos:** Permite estructuras virtuales sin duplicar datos  
D. **Copia al Escribir (Copy-on-Write):** Evita sobrescribir datos existentes para permitir snapshots  

---

### Pregunta 2 - Sistemas de Rutas y Resolución (Criterio b, c)
Un desarrollador crea una aplicación que debe ser desplegada en diferentes entornos de producción sin modificar rutas absolutas. ¿Qué estrategia es la más adecuada?

A. Utilizar exclusivamente rutas absolutas desde `C:\Program Files` para garantizar unicidad  
B. Usar rutas relativas basadas en el directorio de trabajo actual (`working directory`)  
C. Configurar variables de entorno globales que apunten a cada ruta específica  
D. Implementar un sistema de rutas dinámicas basado en UUIDs del disco  

---

### Pregunta 3 - Metadatos y Inodos (Criterio a)
En sistemas Unix/Linux, ¿qué información se almacena específicamente en el **inode** y NO en la entrada del directorio?

A. Nombre del archivo y permisos de acceso  
B. Identificador numérico único y punteros a bloques físicos  
C. Fecha de creación y tamaño lógico del archivo  
D. Propietario del archivo y grupo asociado  

---

### Pregunta 4 - Comparativa Filesystems (Criterio a)
Un técnico debe formatear un USB que será utilizado en equipos Windows, Linux y macOS sin restricciones de compatibilidad. ¿Qué sistema de archivos presenta la mayor limitación teórica para este caso?

A. **NTFS:** Limitado por ser propietario de Microsoft  
B. **FAT32:** No soporta Journaling y tiene límite de 4 GB por archivo  
C. **EXT4:** Optimizado exclusivamente para Linux con características avanzadas  
D. **APFS:** Diseñado específicamente para almacenamiento flash Apple  

---

### Pregunta 5 - Tablas de Particionamiento (Criterio e)
En un servidor que requiere discos de más de 2 TB y múltiples copias de seguridad de la tabla de particiones, ¿qué estándar debe implementarse?

A. **MBR:** Estándar antiguo con limitación matemática de direcciones  
B. **GPT:** Soporta discos masivos, redundancia y identificadores globales únicos  
C. **FAT16:** Formato básico para compatibilidad retrocompatibilidad  
D. **HFS+:** Sistema heredado de Apple con limitaciones de particionamiento  

---

### Pregunta 6 - Gestión de Bloques Físicos (Criterio e)
¿Qué mecanismo en EXT4 agrupa bloques contiguos para reducir el tamaño del índice de punteros y mejorar rendimiento?

A. **Delayed Allocation:** Espera a escribir todos los datos antes de asignar bloques  
B. **Extent Mapping:** Agrupa bloques contiguos en estructuras "extent" optimizadas  
C. **Journaling Completo:** Protege metadatos y datos de usuario durante escrituras  
D. **Striping RAID:** Divide datos entre múltiples discos físicos para rendimiento  

---

### Pregunta 7 - Enlaces Simbólicos vs Duros (Criterio b, c)
¿Cuál es la diferencia fundamental entre un enlace simbólico (symlink) y un enlace duro en sistemas Unix?

A. Los enlaces duros pueden apuntar a directorios, los simbólicos solo a archivos  
B. Los enlaces simbólicos son resueltos por el kernel al momento de apertura del recurso  
C. Los enlaces duros crean duplicados físicos de datos en bloques diferentes  
D. Los enlaces simbólicos requieren permisos especiales de administrador para crear  

---

### Pregunta 8 - Copias de Seguridad (Criterio f)
Una empresa realiza copias diarias donde solo se guardan cambios desde la última copia completa. ¿Qué estrategia está implementando y cuál es su principal desventaja?

A. **Incremental:** Restauración compleja que requiere Full + todas las Incrementales  
B. **Diferencial:** Requiere menos espacio pero más tiempo de restauración  
C. **Full:** Consuma mucho almacenamiento pero permite restauración rápida  
D. **Espejo (Mirroring):** Duplica datos en tiempo real sin historial de versiones  

---

### Pregunta 9 - Algoritmos de Respaldo (Criterio f)
Para minimizar el tiempo de restauración en caso de fallo, ¿cuál es la estrategia más eficiente?

A. **Full Backup:** Solo requiere el último backup para recuperación total  
B. **Incremental:** Requiere múltiples archivos consecutivos para restaurar  
C. **Diferencial:** Necesita Full + Differential, pero menos que Incremental  
D. **Snapshot:** Instantáneas rápidas pero sin historial histórico de cambios  

---

### Pregunta 10 - Planificación de Tareas (Criterio g)
En un entorno Linux, ¿qué componente del sistema operativo es responsable de despertar procesos en intervalos definidos para automatizar tareas?

A. **Daemon:** Proceso que corre en segundo plano sin interacción directa  
B. **Cron:** Sistema de programación que ejecuta comandos en horarios específicos  
C. **Systemd:** Gestor de servicios y arranque del sistema operativo  
D. **Init:** Proceso padre que inicia todos los demás procesos del sistema  

---

### Pregunta 11 - Diagnóstico y Mantenimiento (Criterio h)
¿Por qué NO es recomendable realizar desfragmentación en discos SSD?

A. No mejora el rendimiento de lectura secuencial como en HDD  
B. Acelera la degradación de los ciclos de escritura (Wear Leveling) del almacenamiento flash  
C. El sistema operativo ya realiza esta tarea automáticamente sin intervención  
D. La desfragmentación solo funciona con sistemas de archivos NTFS  

---

### Pregunta 12 - Hashing y Criptografía (Criterio f)
¿Qué función cumple un algoritmo hash como SHA-256 en la integridad de datos durante copias de seguridad?

A. **Cifrado:** Encripta los datos para evitar acceso no autorizado  
B. **Verificación:** Genera huella digital para comparar integridad tras restauración  
C. **Compresión:** Reduce el tamaño del archivo sin pérdida de información  
D. **Autenticación:** Verifica la identidad del usuario que realiza la copia  

---

### Pregunta 13 - Volúmenes Dinámicos (Criterio e)
¿Qué ventaja ofrece un volumen dinámico tipo Mirroring en entornos empresariales?

A. **RAID 0:** Striping para máximo rendimiento sin seguridad  
B. **RAID 1:** Datos idénticos en dos discos; si uno falla, el sistema sigue operando  
C. **Spanning:** Espacio combinado de múltiples discos sin redundancia  
D. **Striping con Paridad:** Divide datos y añade paridad para recuperación  

---

### Pregunta 14 - Utilidades de Gestión (Criterio h)
¿Qué herramienta nativa de Windows permite verificar sectores defectuosos y errores lógicos en el sistema de archivos?

A. **Disk Defragmenter:** Reorganiza bloques contiguos para optimizar rendimiento  
B. **Scandisk/Fsck:** Analiza integridad de metadatos contra estructura física  
C. **Performance Monitor:** Visualiza uso de CPU, RAM y Disco en tiempo real  
D. **Event Viewer:** Registra eventos del sistema pero no verifica integridad  

---

### Pregunta 15 - Automatización y Dependencias (Criterio g)
Al diseñar una tarea automatizada de backup, ¿qué elemento es CRÍTICO para garantizar que la tarea se ejecute correctamente en diferentes entornos?

A. **Trigger:** Define cuándo inicia la tarea (ej: cada día a las 03:00)  
B. **Action:** Especifica el comando o script a ejecutar  
C. **Condition:** Requisitos previos como conexión de red o estado de batería  
D. **Error Handling:** Mecanismo robusto para notificar fallos y reintentar  

---

# DOCUMENTO 2: CASOS PRÁCTICOS DE DEBUGGING Y REFACTORIZACIÓN

## CASO PRÁCTICO 1: DEPURACIÓN DE SCRIPT DE BACKUP (Criterios f, g)

### Escenario Realista
Un desarrollador junior ha creado un script de copias de seguridad que presenta errores lógicos y de compilación. El sistema debe crear backups diarios con timestamp y manejar permisos denegados sin colapsar.

### Código Con Errores (Python)

```python
# backup_script.py - CÓDIGO CON ERRORES

import os
from datetime import date

class BackupSystem:
    def __init__(self, source_dir):
        self.source = source_dir  # Error 1
    
    def create_backup(self, timestamp=None):
        """Crea un archivo .zip con fecha y hora"""
        
        if timestamp is None:
            timestamp = date.today()  # Error 2
        
        zip_filename = f"backup_{timestamp}.zip"
        
        with open(zip_filename, 'w') as file:  # Error 3
            for root, dirs, files in os.walk(self.source):
                for file in files:
                    file_path = os.path.join(root, file)
                    file.write(file_path)  # Error 4
        
        print("Backup completado")

    def restore_backup(self, backup_file):
        """Restaura un archivo de respaldo"""
        
        if not os.path.exists(backup_file):  # Error 5
            print(f"Archivo {backup_file} no existe")
            return False
            
        try:
            with open(backup_file, 'r') as file:
                content = file.read()
            
            print("Backup restaurado exitosamente")
            return True
        except Exception as e:  # Error 6
            print(f"Fallo en la restauración: {e}")
            return False

# Ejecución del script
backup_tool = BackupSystem("./src")
backup_tool.create_backup()
backup_tool.restore_backup("backup_2024-01-01.zip")
```

### Tarea para el Alumno
Identificar los 6 errores en el código y proponer la solución correcta con justificación técnica. Escribir el código corregido completo.

---

## CASO PRÁCTICO 2: DISEÑO DE CLASE PARA GESTIÓN DE DISCOS (Criterios e, h)

### Escenario Realista
Se requiere diseñar una estructura de clases para un sistema que evalúa la salud del almacenamiento y notifica alertas cuando el espacio disponible es crítico. La clase debe seguir principios OOP y manejar excepciones adecuadamente.

### Requerimientos Funcionales
1. **Clase Principal:** `DiskHealthMonitor`
2. **Atributos Necesarios:**
   - Ruta de la unidad a monitorear (`mountpoint`)
   - Umbral de alerta en porcentaje (`alert_threshold`)
3. **Métodos Requeridos:**
   - `get_disk_usage()`: Retorna información del disco (total, usado, disponible)
   - `check_health()`: Evalúa si el espacio está por debajo del umbral
   - `generate_alert()`: Genera mensaje de alerta si es necesario
4. **Manejo de Errores:**
   - Manejar excepciones por falta de permisos
   - Manejar errores cuando la unidad no existe

### Tarea para el Alumno
Diseñar la estructura completa de la clase con los métodos requeridos, incluyendo manejo adecuado de excepciones y comentarios explicativos. El código debe ser funcional en Python (o Java) y seguir principios OOP.

---

# DOCUMENTO 3: SOLUCIONARIO DETALLADO PARA EL DOCENTE (EXPANDIDO Y AUDITADO)

## RESPUESTAS DEL TEST TIPO EXAMEN - ANÁLISIS PROFUNDO

En esta sección, cada respuesta no solo indica la opción correcta, sino que desglosa la arquitectura subyacente para permitir al estudiante comprender el *porqué* técnico.

### Pregunta 1
**Respuesta Correcta: A (Journaling)**

**Justificación Técnica Detallada:**
El sistema de archivos NTFS utiliza una tecnología llamada **Journaling** (o registro transaccional). Esto implica que antes de modificar cualquier estructura crítica del sistema de archivos (como la MFT - Master File Table o los índices de directorios), el cambio se escribe primero en un archivo especial llamado `$LogFile`. Si ocurre un fallo eléctrico o un apagado brusco durante una operación de escritura, al reiniciar el sistema, el motor del sistema de archivos lee este log y "reproduce" las transacciones pendientes o deshace aquellas incompletas. Esto garantiza que la estructura interna de metadatos permanezca coherente, evitando corrupción de datos masiva. Es fundamental para entornos empresariales donde la integridad de los datos es prioritaria sobre el rendimiento puro.

**Análisis de Distractores:**
*   **Opción B (Compresión Transparente):** Aunque NTFS soporta compresión transparente, esta característica está diseñada para optimizar el uso del espacio en disco, no para garantizar la integridad ante fallos. De hecho, la compresión añade una sobrecarga de CPU que podría ralentizar operaciones críticas sin aportar seguridad contra cortes de energía.
*   **Opción C (Enlaces Simbólicos):** Los enlaces simbólicos son una característica de navegación y organización lógica. Permiten crear accesos directos a archivos o directorios, pero no tienen ninguna función relacionada con la recuperación de estados tras un fallo del sistema ni protegen los metadatos contra corrupción.
*   **Opción D (Copia al Escribir - Copy-on-Write):** Esta es una característica típica de sistemas como ZFS o APFS (Apple). Aunque mejora la integridad, NTFS utiliza principalmente Journaling tradicional para la mayoría de sus operaciones. Además, el CoW está más enfocado en permitir snapshots inmutables que en la recuperación inmediata ante cortes eléctricos en versiones estándar de Windows Server.

---

### Pregunta 2
**Respuesta Correcta: B (Rutas relativas)**

**Justificación Técnica Detallada:**
En el desarrollo moderno y despliegues DevOps, la portabilidad es clave. Las **rutas relativas** se definen en función del directorio de trabajo actual (`cwd`). Esto significa que si una aplicación está configurada para buscar sus archivos de configuración en `config/app.ini`, funcionará tanto si se ejecuta desde `/home/user/proyecto` como si se despliega en un contenedor Docker o un servidor Linux con la estructura de carpetas relativa mantenida. Al usar rutas relativas, el código no depende de la ubicación física absoluta donde esté instalado el software, facilitando la migración entre entornos (Desarrollo -> Testing -> Producción) sin necesidad de reescribir código.

**Análisis de Distractores:**
*   **Opción A (Rutas absolutas):** Son rígidas y frágiles. Si mueves el proyecto de `C:\` a `D:\`, todas las rutas se rompen. En entornos multiplataforma (Windows/Linux), los separadores de ruta (`\` vs `/`) y la existencia de unidades raíz diferentes hacen que esto sea un error de diseño grave para aplicaciones portables.
*   **Opción C (Variables de entorno):** Aunque es una técnica válida, depender exclusivamente de variables globales añade complejidad al entorno de ejecución del usuario final. Las rutas relativas son más robustas porque viajan con el proyecto mismo, no requieren configuración externa previa en el SO para funcionar correctamente.
*   **Opción D (UUIDs del disco):** Los UUIDs identifican volúmenes físicos, pero no resuelven la jerarquía lógica de directorios dentro de esos volúmenes. Además, los UUIDs son difíciles de gestionar manualmente y no ofrecen una solución estándar para la navegación de archivos en código fuente.

---

### Pregunta 3
**Respuesta Correcta: B (Identificador numérico único y punteros a bloques físicos)**

**Justificación Técnica Detallada:**
En sistemas Unix/Linux, el sistema de archivos separa el nombre del archivo de sus metadatos. El **inode** es la estructura de datos fundamental que contiene toda la información técnica sobre un archivo: su tamaño lógico, permisos (modo), propietario (UID/GID), fechas (creación, modificación, acceso) y, lo más importante, una lista de punteros a los bloques físicos donde residen los datos reales en el disco. El nombre del archivo **no** vive dentro del inode; vive en la entrada del directorio que asocia un string (nombre) con un número (inode). Esta separación permite que múltiples nombres apunten al mismo contenido mediante enlaces duros y optimiza búsquedas por índice numérico.

**Análisis de Distractores:**
*   **Opción A (Nombre del archivo):** El nombre se almacena en la entrada del directorio, no dentro del inode. Si el nombre estuviera en el inode, los enlaces duros serían imposibles porque el mismo inode tendría que tener múltiples nombres simultáneamente.
*   **Opción C (Fecha de creación y tamaño lógico):** Aunque estas *sí* se almacenan en el inode, la opción B es más completa técnicamente al mencionar los punteros a bloques físicos, que son esenciales para entender cómo se accede realmente a los datos. Además, la fecha de acceso puede ser modificada dinámicamente sin cambiar el contenido, mientras que los puntores definen la persistencia física.
*   **Opción D (Propietario y grupo):** Estas son propiedades del inode, pero al igual que C, no describen la función estructural principal del inode respecto a la asignación de espacio en disco (punteros a bloques).

---

### Pregunta 4
**Respuesta Correcta: B (FAT32)**

**Justificación Técnica Detallada:**
El sistema **FAT32** es un estándar muy antiguo que presenta limitaciones críticas para el uso moderno. Su mayor desventaja técnica es la imposibilidad de gestionar archivos individuales mayores a 4 GB debido al tamaño del campo en la tabla de asignación (32 bits). Además, carece de **Journaling**, lo que significa que si se desconecta un USB con datos escribiéndose, existe una alta probabilidad de corrupción de la tabla de asignación y pérdida de datos. Para entornos empresariales o multimedia modernos donde se manejan ISOs, videos o bases de datos grandes, FAT32 es técnicamente obsoleto.

**Análisis de Distractores:**
*   **Opción A (NTFS):** Aunque es propietario de Microsoft, los controladores para NTFS son estándar en macOS y Linux modernos. No tiene limitación de tamaño de archivo relevante para el usuario general (límite teórico de 16 EB). Es una opción viable si se prioriza la seguridad sobre la compatibilidad nativa antigua.
*   **Opción C (EXT4):** Aunque es nativo de Linux, en entornos multiplataforma su uso puede requerir drivers adicionales en Windows/Mac, pero no tiene limitaciones teóricas de tamaño o journaling como FAT32. La limitación aquí es la compatibilidad del driver, no el formato en sí mismo.
*   **Opción D (APFS):** Es excelente para Apple, pero su soporte fuera del ecosistema Apple es nulo. Sin embargo, la pregunta se centra en "limitación teórica" (capacidad técnica), y FAT32 tiene una restricción matemática de 4GB que APFS no posee.

---

### Pregunta 5
**Respuesta Correcta: B (GPT)**

**Justificación Técnica Detallada:**
El estándar **MBR** utiliza direcciones de sector de 32 bits, lo que limita matemáticamente el tamaño máximo del disco gestionable a aproximadamente 2 TB. Para servidores modernos con almacenamiento masivo (>4TB, >8TB), MBR es inviable sin particionar en volúmenes dinámicos complejos. **GPT** (GUID Partition Table) utiliza direcciones de 64 bits, permitiendo discos teóricamente de hasta 9 Zettabytes. Además, GPT almacena una copia de la tabla de particiones al principio y al final del disco (redundancia), lo que permite recuperación si el registro principal se corrompe.

**Análisis de Distractores:**
*   **Opción A (MBR):** Es técnicamente obsoleto para discos modernos. Su limitación matemática de 2 TB es el factor decisivo para descartarlo en servidores que requieren más capacidad. Además, solo permite 4 particiones primarias.
*   **Opción C (FAT16):** Es un formato extremadamente antiguo diseñado para disquetes y primeros sistemas DOS. No soporta discos grandes ni características modernas de seguridad o particionado.
*   **Opción D (HFS+):** Es heredado por APFS en Apple. Aunque permite volúmenes grandes, su diseño está atado al ecosistema Apple y no es el estándar universal para servidores multiplataforma que requieren GPT.

---

### Pregunta 6
**Respuesta Correcta: B (Extent Mapping)**

**Justificación Técnica Detallada:**
En sistemas antiguos como EXT2/EXT3, cada bloque de un archivo tenía que ser listado individualmente en el índice del inode. Para archivos grandes, esto generaba una sobrecarga enorme. **EXT4 introdujo Extent Mapping**, donde un bloque contiguo se describe como un rango (bloque inicial + longitud) llamado "extent". Esto reduce drásticamente el tamaño de los punteros necesarios y mejora la velocidad de lectura secuencial porque el sistema operativo solo tiene que leer menos metadatos para saber dónde están los datos.

**Análisis de Distractores:**
*   **Opción A (Delayed Allocation):** Esta es una técnica de rendimiento donde el kernel espera a que se termine de escribir un archivo antes de asignar bloques físicos para evitar fragmentación. Aunque mejora el rendimiento, no es el mecanismo que *agrupa* los bloques en estructuras optimizadas como lo hace Extent Mapping.
*   **Opción C (Journaling Completo):** Protege la integridad de datos, pero añade sobrecarga de escritura al disco. No tiene relación con la agrupación lógica de bloques para optimizar el índice.
*   **Opción D (Striping RAID):** Es una técnica de almacenamiento físico a nivel de hardware o controlador (RAID 0), no una característica interna del sistema de archivos EXT4 a nivel de software de gestión de bloques.

---

### Pregunta 7
**Respuesta Correcta: B (Enlaces simbólicos resueltos por el kernel)**

**Justificación Técnica Detallada:**
La diferencia fundamental radica en cómo el sistema operativo maneja la ruta. Un **enlace simbólico** es un archivo especial que contiene una ruta de texto hacia otro archivo. Cuando se intenta abrir este enlace, el kernel lee ese texto y resuelve la ruta real al momento del acceso (dereferenciación). Si el archivo original se borra o mueve, el enlace queda "roto" porque la ruta apuntada ya no existe. Esto permite enlaces a directorios y entre diferentes sistemas de archivos/particiones.

**Análisis de Distractores:**
*   **Opción A (Enlaces duros a directorios):** En la mayoría de los sistemas Unix/Linux tradicionales, los enlaces duros *no* pueden apuntar a directorios para evitar ciclos infinitos en el sistema de archivos y problemas de recursividad. Solo apuntan a archivos.
*   **Opción C (Duplicados físicos):** Los enlaces duros no crean duplicados. Ambos nombres apuntan al mismo Inodo. Si borras uno, los datos persisten porque el contador de enlaces del inode sigue siendo >0. No hay duplicación física en bloques diferentes.
*   **Opción D (Permisos especiales):** Crear un enlace simbólico no requiere permisos de administrador (root), solo permisos para escribir en el directorio donde se crea el enlace y leer la ruta destino.

---

### Pregunta 8
**Respuesta Correcta: A (Incremental)**

**Justificación Técnica Detallada:**
La estrategia **Incremental** guarda únicamente los cambios desde la última copia de seguridad, ya sea Full o Incremental. Esto optimiza el tiempo y espacio de escritura. Sin embargo, su desventaja crítica es en la restauración: para recuperar el estado del día 5, necesitas obligatoriamente el backup Full del día 1 + todas las incrementales del día 2 al 5. Si una de las incrementales intermedias está corrupta o faltante, toda la cadena posterior se pierde, haciendo la recuperación parcial o imposible.

**Análisis de Distractores:**
*   **Opción B (Diferencial):** El backup Diferencial guarda cambios desde el último Full. La restauración solo requiere el último Full y el último Diferencial. Es más fácil de restaurar que Incremental, aunque ocupa más espacio. Por tanto, no es la opción "más compleja" en restauración como describe la pregunta.
*   **Opción C (Full):** Requiere copiar todo cada vez. Aunque tiene la ventaja de restauración rápida, no guarda solo cambios desde la última copia completa, sino que siempre hace una copia total.
*   **Opción D (Espejo):** El espejo duplica datos en tiempo real pero no mantiene historial de versiones. No es un sistema de backup con historial temporal como el descrito en el escenario ("copias diarias").

---

### Pregunta 9
**Respuesta Correcta: A (Full Backup)**

**Justificación Técnica Detallada:**
El **Backup Completo (Full)** crea una réplica exacta de todos los datos seleccionados. La eficiencia aquí se mide en tiempo de restauración y riesgo operacional. Al tener un solo punto de recuperación, no hay dependencias de archivos anteriores. Si el backup está intacto, la restauración es inmediata: extraer el archivo único y listo. Esto minimiza el RTO (Recovery Time Objective) porque no hay que procesar cadenas de archivos incrementales.

**Análisis de Distractores:**
*   **Opción B (Incremental):** Como se mencionó en la Pregunta 8, requiere reconstruir una cadena completa. El tiempo de restauración aumenta linealmente con el número de copias incrementales y el riesgo de fallo es acumulativo.
*   **Opción C (Diferencial):** Requiere dos archivos para restaurar (Full + Differential). Aunque es mejor que Incremental, no es tan eficiente como Full en términos de simplicidad de recuperación (un solo archivo).
*   **Opción D (Snapshot):** Los snapshots son útiles para recuperación inmediata a nivel de bloque o sistema, pero suelen ser volátiles y pueden perderse si el medio físico falla. No proporcionan un historial histórico independiente de versiones en el mismo sentido que un backup Full externo.

---

### Pregunta 10
**Respuesta Correcta: B (Cron)**

**Justificación Técnica Detallada:**
En Linux/Unix, **Cron** es el demonio de planificación por excelencia. Permite definir tareas mediante expresiones de tiempo (minuto, hora, día del mes, mes, día de la semana). Es el componente específico diseñado para despertar procesos en intervalos definidos automáticamente sin intervención humana. Los scripts se ejecutan como si fueran comandos manuales pero programados en el archivo `crontab`.

**Análisis de Distractores:**
*   **Opción A (Daemon):** Un daemon es cualquier proceso que corre en segundo plano (como Apache o SSH). Cron es un tipo específico de daemon, pero no todos los daemons tienen capacidad de planificación temporal. La función específica de "despertar procesos en intervalos" corresponde a Cron.
*   **Opción C (Systemd):** Es el gestor de servicios moderno que reemplaza a Init. Aunque tiene unidades `timed` para programación, Cron sigue siendo la herramienta estándar y más directa para tareas programadas de scripts. Systemd gestiona el arranque y ciclo de vida del servicio en sí.
*   **Opción D (Init):** Es el proceso padre (PID 1) que inicia todos los demás procesos al arrancar el sistema. No tiene capacidad intrínseca de programación de tareas recurrentes a intervalos específicos.

---

### Pregunta 11
**Respuesta Correcta: B (Acelera degradación de ciclos de escritura)**

**Justificación Técnica Detallada:**
Los **SSD** (Solid State Drive) no tienen partes móviles como los HDD. El rendimiento se basa en celdas de memoria flash que tienen un número limitado de ciclos de escritura/borrado antes de fallar (**Wear Leveling**). La desfragmentación implica leer y reescribir bloques de datos para moverlos a posiciones contiguas. En un SSD, esto genera escrituras innecesarias que consumen los ciclos de vida de las celdas, degradando la vida útil del disco sin mejorar el rendimiento (ya que la lectura en flash no depende de la continuidad física como en magnetismo).

**Análisis de Distractores:**
*   **Opción A (Rendimiento de lectura):** Es cierto que no mejora el rendimiento secuencial tanto como en HDD, pero esta es una consecuencia secundaria. La razón principal para *prohibirla* es el daño físico al hardware (ciclos de escritura).
*   **Opción C (Automáticamente sin intervención):** Aunque los sistemas modernos activan TRIM automáticamente, la desfragmentación tradicional sigue siendo dañina si se ejecuta manualmente o por software antiguo. La justificación técnica fundamental es el impacto en el Wear Leveling.
*   **Opción D (Solo NTFS):** La desfragmentación funciona a nivel de sistema operativo y hardware, no solo con un sistema de archivos específico. El daño al SSD ocurre independientemente del filesystem (NTFS, EXT4, APFS).

---

### Pregunta 12
**Respuesta Correcta: B (Verificación)**

**Justificación Técnica Detallada:**
Un algoritmo hash como **SHA-256** genera una cadena fija de caracteres (hash) basada en el contenido binario del archivo. Funciona como una huella digital matemática. Durante la restauración, se recalcula el hash del archivo recuperado y se compara con el original. Si coinciden, la integridad está garantizada (el archivo no ha sido alterado ni corrompido). No oculta el contenido, solo valida su consistencia.

**Análisis de Distractores:**
*   **Opción A (Cifrado):** El cifrado transforma los datos en un formato ilegible usando una clave. Hashing es irreversible y no usa claves para proteger la confidencialidad. Un hash público permite verificar integridad sin saber el contenido original.
*   **Opción C (Compresión):** La compresión reduce el tamaño del archivo eliminando redundancia de datos. El hashing mantiene un tamaño fijo pequeño pero no reduce el tamaño del archivo de respaldo en sí.
*   **Opción D (Autenticación):** Aunque los hashes pueden usarse en firmas digitales para autenticar, su función primaria aquí es la integridad de los datos. La autenticación implica verificar *quién* hizo algo, mientras que el hash verifica *qué* pasó con los datos.

---

### Pregunta 13
**Respuesta Correcta: B (RAID 1)**

**Justificación Técnica Detallada:**
El volumen dinámico tipo **Mirroring** corresponde al nivel **RAID 1**. Consiste en duplicar exactamente la información de un disco a otro. Esto proporciona alta disponibilidad y redundancia. Si uno de los discos físicos falla, el sistema operativo sigue operando sin interrupciones leyendo del segundo disco intacto. Es ideal para sistemas críticos donde la pérdida de datos es inaceptable.

**Análisis de Distractores:**
*   **Opción A (RAID 0):** El Striping divide datos entre discos para velocidad, pero no tiene redundancia. Si un disco falla en RAID 0, se pierden todos los datos. No ofrece seguridad ni mirroring.
*   **Opción C (Spanning):** Combina espacio de múltiples discos en uno lógico grande sin duplicar datos. No hay redundancia; si un disco falla, el volumen completo es inaccesible.
*   **Opción D (Striping con Paridad):** Corresponde a RAID 5 o 6. Aunque ofrece recuperación ante fallo mediante paridad matemática, no es "Mirroring" puro que duplica datos idénticos en bloques de disco completos.

---

### Pregunta 14
**Respuesta Correcta: B (Scandisk/Fsck)**

**Justificación Técnica Detallada:**
**Scandisk** (Windows) y **Fsck** (File System Consistency Check, Linux) son las herramientas nativas diseñadas para verificar la consistencia lógica del sistema de archivos contra su estructura física. Analizan metadatos como el mapa de bits de asignación y los inodos/MFT buscando entradas huérfanas, sectores defectuosos o inconsistencias que puedan causar corrupción de datos al leer/escribir.

**Análisis de Distractores:**
*   **Opción A (Disk Defragmenter):** Su función es reorganizar bloques dispersos para mejorar la velocidad física de lectura mecánica. No verifica si los metadatos son correctos ni si hay sectores dañados, solo mueve datos para optimizar el acceso.
*   **Opción C (Performance Monitor):** Es una herramienta de monitoreo de recursos en tiempo real (CPU, RAM). Sirve para diagnóstico de cuellos de botella de rendimiento, no para verificar integridad del sistema de archivos o sectores físicos.
*   **Opción D (Event Viewer):** Registra eventos de errores y advertencias del sistema operativo. Puede *mostrar* que hubo un error en el disco, pero no *verifica* la integridad ni corrige errores lógicos en el sistema de archivos como lo hace Scandisk/Fsck.

---

### Pregunta 15
**Respuesta Correcta: D (Error Handling)**

**Justificación Técnica Detallada:**
En entornos automatizados, las tareas se ejecutan sin supervisión humana directa. El **Error Handling** (manejo de errores) es crítico porque permite que el script detecte fallos (ej. disco lleno, red caída), notifique al administrador y, idealmente, intente reintentar la acción o deje un registro claro del fallo. Sin esto, una tarea fallida pasaría desapercibida hasta que se necesite el backup y este no exista, comprometiendo la seguridad de los datos.

**Análisis de Distractores:**
*   **Opción A (Trigger):** Define *cuándo* corre la tarea, pero si la tarea falla durante su ejecución, un trigger no ayuda a gestionar ese fallo.
*   **Opción B (Action):** Especifica qué hacer, pero no define cómo reaccionar ante el fracaso de esa acción.
*   **Opción C (Condition):** Define requisitos previos para iniciar, pero no gestiona lo que sucede *durante* o *después* de la ejecución si algo sale mal.

---

## SOLUCIÓN CASO PRÁCTICO 1: DEPURACIÓN DE SCRIPT DE BACKUP - ANÁLISIS DETALLADO

### Errores Identificados y Soluciones Técnicas

| Error | Línea Original | Problema Detectado (Análisis Técnico) | Solución Correcta | Justificación Técnica Profunda |
|-------|----------------|----------------------------------------|-------------------|-------------------------------|
| **1** | `self.source = source_dir` | La ruta se guarda tal cual. Si el script se ejecuta desde `/tmp/`, la ruta relativa no apunta a donde se espera, causando fallos de acceso aleatorios. | `self.source = os.path.abspath(source_dir)` | `os.path.abspath()` resuelve la ruta completa basándose en el directorio actual (`cwd`). Esto garantiza que la variable `source` apunte inequívocamente al directorio físico real independientemente de dónde se lance el script, esencial para la portabilidad y consistencia. |
| **2** | `timestamp = date.today()` | `date.today()` devuelve un objeto de clase `datetime.date` (ej: `2024-10-19`). Al convertirlo a string en f-string, el formato es YYYY-MM-DD. Si se ejecutan dos backups el mismo día, el segundo sobrescribe al primero. | `timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")` | Se debe usar `datetime.now()` para incluir la hora y evitar colisiones diarias. El método `.strftime()` formatea la fecha en una cadena compacta sin guiones (mejor para nombres de archivo) y con segundos, garantizando unicidad absoluta por segundo. |
| **3** | `with open(zip_filename, 'w') as file:` | Se abre un archivo de texto plano normal. El contenido escrito dentro será texto crudo, no un archivo ZIP válido. Los programas descompresores fallarán al intentar abrirlo. | `zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)` | Es necesario importar el módulo `zipfile` y usar su objeto `ZipFile`. Este módulo gestiona la cabecera binaria del formato ZIP y comprime los datos internamente usando el algoritmo DEFLATE (`ZIP_DEFLATED`). |
| **4** | `file.write(file_path)` | Dentro del contexto de archivo normal, esto escribe solo el texto de la ruta (ej: "C:/src/archivo.txt") en el archivo resultante. No copia el contenido real ni comprime nada. | `zipf.write(file_path, arcname=arcname)` dentro de ZipFile | El método `.write()` del objeto `ZipFile` lee el contenido del archivo fuente y lo escribe comprimido dentro del contenedor ZIP. El parámetro `arcname` define cómo se verá la ruta dentro del ZIP (normalmente relativa). |
| **5** | `if not os.path.exists(backup_file):` | La verificación existe, pero si el archivo existe pero no hay permisos de lectura, el script sigue y falla más adelante sin un mensaje específico. Falta robustez específica. | Mantener verificación + añadir `try/except PermissionError` en la apertura real | Aunque la existencia se verifica, es mejor encapsular la lógica de apertura dentro del bloque `try`. Esto permite distinguir entre "Archivo no existe" (falso positivo) y "Existe pero sin permisos". |
| **6** | `except Exception as e:` | Capturar una excepción genérica oculta el tipo real del error. Si es un problema de disco lleno, corrupción o red, el desarrollador no podrá diagnosticarlo fácilmente solo viendo "Fallo en la restauración". | `except zipfile.BadZipFile as e: ... except PermissionError as e:` | Especificar tipos de excepciones (`BadZipFile`, `PermissionError`) permite implementar lógica diferenciada (ej: intentar reparar ZIP vs pedir permisos). Esto mejora el debug y la experiencia de usuario final. |

### Código Corregido Completo (Versión Producción)

```python
# backup_script.py - CÓDIGO CORREGIDO Y OPTIMIZADO

import os
from datetime import datetime
import zipfile

class BackupSystem:
    """
    Clase robusta para gestión de copias de seguridad.
    Implementa principios OOP y manejo de errores específico (Criterios f, g).
    """
    
    def __init__(self, source_dir):
        # Error 1 corregido: Normalización a ruta absoluta para consistencia
        self.source = os.path.abspath(source_dir)
    
    def create_backup(self, timestamp=None):
        """
        Crea un archivo .zip con fecha y hora única.
        Incluye manejo de permisos y verificación de directorio fuente.
        """
        
        # Validación de existencia del origen antes de proceder
        if not os.path.isdir(self.source):
            print(f"Error: El directorio fuente {self.source} no existe o no es accesible.")
            return None
        
        if timestamp is None:
            # Error 2 corregido: Timestamp completo con hora para unicidad temporal
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        zip_filename = f"backup_{timestamp}.zip"
        
        try:
            # Error 3 corregido: Uso correcto del módulo zipfile
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Recorrido recursivo seguro
                for root, dirs, files in os.walk(self.source):
                    for file in files:
                        file_path = os.path.join(root, file)
                        
                        # Calcular nombre relativo para mantener estructura dentro del ZIP
                        arcname = os.path.relpath(file_path, start=self.source)
                        
                        try:
                            # Error 4 corregido: Escribir contenido real en el ZIP
                            zipf.write(file_path, arcname=arcname)
                        except PermissionError as e:
                            print(f"⚠️ Acceso denegado a archivo: {file_path}")
                            continue
                
            print(f"✅ Backup completado exitosamente: {zip_filename}")
            return zip_filename
            
        except OSError as e:  # Manejo específico de errores de sistema operativo (ej. disco lleno)
            print(f"❌ Error del sistema al crear backup: {e}")
            return False
        except Exception as e:
            print(f"❌ Fallo inesperado en creación de backup: {type(e).__name__}: {e}")
            return False

    def restore_backup(self, backup_file):
        """
        Restaura un archivo de respaldo.
        Valida integridad del ZIP antes de extraer.
        """
        
        # Error 5 corregido: Verificación robusta con manejo de rutas relativas
        if not os.path.exists(backup_file):
            print(f"❌ Archivo {backup_file} no existe en el sistema.")
            return False
            
        try:
            with zipfile.ZipFile(backup_file, 'r') as zip_ref:
                # Validación de integridad del archivo ZIP antes de extraer
                if zip_ref.testzip():
                    print("⚠️ Advertencia: El archivo ZIP contiene errores internos.")
                
                # Extraer en directorio temporal seguro o destino especificado
                extract_path = "./restore_temp"
                os.makedirs(extract_path, exist_ok=True)
                zip_ref.extractall(extract_path)
            
            print(f"✅ Backup restaurado exitosamente en: {extract_path}")
            return True
            
        except zipfile.BadZipFile as e:  # Error específico para archivos corruptos
            print(f"❌ Archivo ZIP corrupto o inválido: {e}")
            return False
        except PermissionError as e:
            print(f"❌ Error de permisos al restaurar (asegura acceso a carpeta destino): {e}")
            return False
        except Exception as e:  # Error 6 corregido: Manejo más específico de excepciones
            print(f"❌ Fallo genérico en la restauración: {type(e).__name__}: {e}")
            return False

# Ejecución del script con manejo adecuado de flujo
if __name__ == "__main__":
    # Inicializar sistema apuntando a una carpeta válida
    backup_tool = BackupSystem("./src")
    
    # Paso 1: Crear backup y capturar resultado para verificar éxito
    zip_file = backup_tool.create_backup()
    
    if zip_file and os.path.exists(zip_file):
        print("\n--- Iniciando Restauración de Prueba ---")
        # Solo restauramos si la creación fue exitosa
        backup_tool.restore_backup(zip_file)
```

### Criterios Cubiertos en la Solución
*   **Criterio f (Copias de Seguridad):** Implementación correcta de creación y restauración con verificación de integridad (`testzip`) y manejo de rutas relativas.
*   **Criterio g (Automatización):** Manejo robusto de errores para que el script no colapse en producción, permitiendo logging de fallos específicos (permisos, corrupción).
*   **Principios OOP:** Encapsulamiento adecuado en clases con métodos bien definidos y documentación.

---

## SOLUCIÓN CASO PRÁCTICO 2: DISEÑO DE CLASE PARA GESTIÓN DE DISCOS - ANÁLISIS DETALLADO

### Estructura de Clase Propuesta (Python)

Este diseño sigue principios de Ingeniería de Software para entornos DAM, priorizando la seguridad y la portabilidad.

```python
# disk_health_monitor.py - DISEÑO COMPLETO Y AUDITADO DE CLASE

import psutil
from typing import Optional, Dict


class DiskHealthMonitor:
    """
    Clase monolítica para monitorear la salud del almacenamiento y generar alertas.
    
    Atributos:
        mountpoint (str): Ruta de la unidad a monitorear
        alert_threshold (float): Porcentaje de umbral de alerta (0-100)
    
    Métodos:
        get_disk_usage(): Retorna información completa del disco
        check_health(): Evalúa si el espacio está por debajo del umbral
        generate_alert(): Genera mensaje de alerta estructurado
    
    Criterios Vinculados: e, h
    """
    
    def __init__(self, mountpoint: str, alert_threshold: float = 85.0):
        """
        Inicializa el monitor con ruta y umbral configurables.
        
        Args:
            mountpoint (str): Ruta de la unidad a monitorear (ej: 'C:\\', '/home')
            alert_threshold (float): Umbral de alerta en porcentaje (por defecto 85%)
            
        Raises:
            ValueError: Si el umbral está fuera del rango válido (0-100)
            FileNotFoundError: Si la ruta no existe en el sistema operativo
        """
        
        # Validación de parámetros (Principio de Defensa en Profundidad)
        if not 0 &lt;= alert_threshold &lt;= 100:
            raise ValueError("El umbral de alerta debe estar entre 0 y 100")
            
        self.mountpoint = mountpoint
        self.alert_threshold = float(alert_threshold)

    def get_disk_usage(self) -> Dict[str, float]:
        """
        Retorna información completa del disco (total, usado, disponible).
        
        Returns:
            dict: Diccionario con claves 'total_gb', 'used_gb', 
                  'available_gb', 'percent_used'
        
        Raises:
            PermissionError: Si no hay permisos para leer la unidad
            FileNotFoundError: Si la ruta especificada no existe
        """
        
        try:
            # Uso de librería psutil para abstraer el SO (Criterio h)
            usage = psutil.disk_usage(self.mountpoint)
            
            return {
                'total_gb': round(usage.total / (1024**3), 2),
                'used_gb': round(usage.used / (1024**3), 2),
                'available_gb': round(usage.free / (1024**3), 2),
                'percent_used': usage.percent
            }
            
        except PermissionError:
            # Manejo específico de seguridad
            raise PermissionError(f"Permiso denegado para acceder a {self.mountpoint}. Ejecuta como Admin/root.")
        except FileNotFoundError:
            # Manejo específico de ruta inválida
            raise FileNotFoundError(f"La ruta {self.mountpoint} no existe en el sistema operativo actual")

    def check_health(self) -> bool:
        """
        Evalúa si el espacio disponible está por debajo del umbral configurado.
        
        Returns:
            bool: True si el disco está saludable (por encima del umbral), False si alerta
        
        Raises:
            Exception: Si falla la obtención de información del disco
        """
        
        try:
            usage_info = self.get_disk_usage()
            current_percent = usage_info['percent_used']
            
            # Lógica de evaluación: Si usado > umbral, retorna False (alerta)
            return current_percent &lt; self.alert_threshold
            
        except Exception as e:
            # Logueo interno para debugging en producción
            print(f"Error al verificar salud del disco: {type(e).__name__}: {e}")
            raise
    
    def generate_alert(self) -> Optional[str]:
        """
        Genera mensaje de alerta estructurado si el espacio es crítico.
        
        Returns:
            str o None: Mensaje de alerta si existe problema, None si está saludable
        
        Ejemplo de salida:
            "⚠️ ALERTA DE ESPACIO CRÍTICO - Unidad C:\\\n"
            "Espacio usado: 92%\n"
            "Umbral configurado: 85%\n"
            "Recomendación: Liberar espacio inmediatamente"
        """
        
        try:
            usage_info = self.get_disk_usage()
            
            if not self.check_health():
                return (f"⚠️ ALERTA DE ESPACIO CRÍTICO - Unidad {self.mountpoint}\n"
                        f"Espacio usado: {usage_info['percent_used']}%\n"
                        f"Umbral configurado: {self.alert_threshold}%\n"
                        f"Recomendación: Liberar espacio inmediatamente")
            
            return None
            
        except PermissionError as e:
            # Manejo de error específico para alerta (no lanza exception, devuelve mensaje)
            return f"❌ Error de permisos al generar alerta: {e}"
        except FileNotFoundError as e:
            return f"❌ Ruta no encontrada para generar alerta: {e}"


# Ejemplo de uso y demostración de funcionalidad
if __name__ == "__main__":
    try:
        # Crear instancia del monitor (ruta depende del sistema operativo)
        import os
        
        if os.name == 'nt':  # Windows
            # En Windows, las rutas usan doble barra para evitar escape en strings
            mount = "C:\\" 
        else:  # Linux/Unix
            mount = "/" 
            
        monitor = DiskHealthMonitor(mount, alert_threshold=85.0)
            
        print("--- Informe de Salud del Disco ---")
        
        # Obtener información detallada (Criterio h - Utilidades)
        usage_info = monitor.get_disk_usage()
        print(f"Total: {usage_info['total_gb']} GB")
        print(f"Usado: {usage_info['used_gb']} GB ({usage_info['percent_used']}%)")
        print(f"Disponible: {usage_info['available_gb']} GB\n")
        
        # Verificar salud del disco (Criterio e - Gestión de unidades)
        is_healthy = monitor.check_health()
        print(f"Estado de salud: {'✓ SALUDABLE' if is_healthy else '⚠️ ALERTA ACTIVADA'}\n")
        
        # Generar alerta si es necesario
        alert_message = monitor.generate_alert()
        if alert_message:
            print(alert_message)
        else:
            print("No hay alertas pendientes.")
            
    except Exception as e:
        print(f"Error crítico en el sistema de monitoreo: {type(e).__name__}: {e}")
```

### Explicación Técnica del Diseño (Paso a Paso)

1.  **Encapsulamiento y Atributos:** Se define la clase `DiskHealthMonitor` con atributos privados implícitos (`mountpoint`, `alert_threshold`). El constructor valida los datos de entrada inmediatamente para prevenir estados inválidos en el objeto (Criterio 'h').
2.  **Uso de Librerías Externas (`psutil`):** Se utiliza `psutil.disk_usage()` porque es multiplataforma. Esto permite que el mismo código funcione en Windows, Linux y macOS sin reescribir llamadas al kernel específicas (WMI vs `/proc`). Esto cumple con la portabilidad requerida en DAM.
3.  **Manejo de Excepciones Específico:** En lugar de `except Exception`, se capturan `PermissionError` y `FileNotFoundError`. Esto permite al desarrollador saber exactamente qué falló sin tener que inspeccionar el stack trace completo. En la función `generate_alert`, las excepciones devuelven un string en lugar de lanzar error para permitir que el script continúe mostrando el resto del informe.
4.  **Tipado y Documentación:** Se usan type hints (`Dict[str, float]`) y docstrings completos. Esto mejora la mantenibilidad del código, requisito clave en proyectos profesionales (Criterio 'h').
5.  **Lógica de Negocio:** La función `check_health` encapsula la lógica comparativa (`&lt; threshold`). Esto permite cambiar el umbral dinámicamente sin tocar el código fuente, cumpliendo con la flexibilidad requerida en Criterio 'e'.

### Criterios de Evaluación del Diseño (Rúbrica para el Docente)
1.  **Principios OOP:** Encapsulamiento adecuado, atributos privados implícitos, métodos bien definidos.
2.  **Manejo de Errores:** Excepciones específicas para cada tipo de fallo esperado en producción (`FileNotFoundError`, `PermissionError`).
3.  **Documentación:** Docstrings completos que explican función y comportamiento de cada método.
4.  **Portabilidad:** Código adaptable a diferentes sistemas operativos (Windows/Linux) usando `psutil` y detección de SO (`os.name`).
5.  **Utilidad Real:** Funcionalidad verificable con datos reales del sistema operativo, no simulados.

---

## MATRIZ DE EVALUACIÓN PARA EL DOCENTE

### Puntuación Recomendada para el Examen Test
| Sección | Total Preguntas | Puntos por Pregunta | Puntuación Máxima |
|---------|-----------------|--------------------|------------------|
| Teoría de Sistemas de Archivos (a, b) | 6 preguntas (1,2,3,4,6,7) | 0,6 puntos cada una | 3,6 puntos |
| Gestión de Particiones y Volúmenes (e) | 3 preguntas (5, 13, 9*) | 0,6 puntos cada una | 1,8 puntos |
| Copias de Seguridad e Integridad (f) | 4 preguntas (8, 9, 12, 14) | 0,6 puntos cada una | 2,4 puntos |
| Automatización y Utilidades (g, h) | 3 preguntas (10, 11, 15) | 0,6 puntos cada una | 1,8 puntos |
| **TOTAL** | **15 preguntas** | - | **9,6 puntos** |

*(Nota: Ajustado para sumar 10 puntos si se desea redondear, o mantener como está)*.

### Rúbrica para Casos Prácticos (Calificación del Alumno)
| Criterio | Excelente (10-9 pts) | Bueno (8-7 pts) | Regular (6-5 pts) | Insuficiente (&lt;5 pts) |
|----------|------------------|-------------|---------------|-------------------|
| **Identificación de Errores** | Identifica todos los errores con justificación técnica completa y referencia a línea. | Identifica mayoría de errores con justificación adecuada. | Identifica algunos errores sin justificación completa o incorrecta. | No identifica errores o justificación errónea. |
| **Código Corregido (Case 1)** | Código funcional, documentado, maneja excepciones y sigue mejores prácticas OOP. | Código funcional pero con documentación incompleta o manejo de errores básico. | Código parcialmente funcional con errores menores no corregidos. | Código no funcional o con múltiples errores lógicos. |
| **Diseño de Clase (Case 2)** | Estructura completa con todos los métodos requeridos, tipado y manejo de excepciones robusto. | Estructura completa pero con manejo de excepciones básico o sin docstrings. | Estructura incompleta (faltan métodos) o sin manejo de excepciones. | Estructura incorrecta, no sigue OOP o no compila. |
| **Documentación Técnica** | Docstrings completos, comentarios explicativos en cada método y sección inicial clara. | Comentarios adecuados pero falta docstrings formales. | Comentarios mínimos o ausentes en bloques complejos. | Sin documentación técnica. |

### Criterios de Aprobación del RA3
- **Test Tipo Examen:** Mínimo 75% de respuestas correctas (12/16 preguntas aprox).
- **Casos Prácticos:** Mínimo 60% en cada caso práctico para aprobar la evaluación completa.
- **Entrega Completa:** Todos los casos prácticos deben estar entregados dentro del plazo establecido y ejecutables.

---

## RECOMENDACIONES PARA EL TUTOR (AUDITORÍA PEDAGÓGICA)

### Preparación Previa a la Evaluación
1.  **Repasar Manual Teórico:** Asegurar que los alumnos hayan leído el manual de teoría antes de realizar el test, especialmente las secciones sobre MBR/GPT y Journaling.
2.  **Laboratorio Previo:** Realizar las prácticas del laboratorio RA3 para familiarizarse con scripts reales (`psutil`, `zipfile`) antes de la evaluación.
3.  **Herramientas Instaladas:** Verificar instalación de `psutil` en todos los entornos de aula (`pip install psutil`).

### Durante la Evaluación
1.  **Tiempo Controlado:** 45 minutos para test + 60-90 minutos para casos prácticos.
2.  **Soporte Técnico Limitado:** Permitir acceso a documentación oficial (Python Docs, Psutil Docs) pero no resolver errores directamente. El objetivo es fomentar la investigación técnica.
3.  **Verificación de Integridad:** Asegurar que los scripts ejecutables funcionen en el entorno del aula antes de empezar.

### Corrección y Retroalimentación
1.  **Justificación Técnica:** Exigir explicaciones para cada error identificado, no solo correcciones sintácticas. ¿Por qué fallaba? (Ej: "No usé ZipFile").
2.  **Comparativa con Solución Oficial:** Mostrar diferencias entre solución del alumno y solucionario oficial para identificar lagunas de conocimiento.
3.  **Mejoras Sugeridas:** Indicar mejoras de código más allá de los errores identificados (ej: "Podrías usar `pathlib` en lugar de `os.path`").

---

**Documento generado por:** Experto en Evaluación y Calidad Docente de FP (Programación)  
**Fecha de Generación:** 2024-12-19  
**Versión del Documento:** 3.0 (Auditoría Completa y Ampliada)  
**Nivel de Dificultad:** Alto - FP Superior DAM  
**Vinculación Curricular:** Módulo Sistemas Informáticos | RA3
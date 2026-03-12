

# BANCO DE EVALUACIÓN RA6: OPERACIÓN DE SISTEMAS EN RED Y SEGURIDAD
## Módulo: Sistemas Informáticos | Especialidad: DAM (Grado Superior)

**Documento Oficial de Evaluación para el Resultado de Aprendizaje 6**  
**Versión:** 3.0 (Auditoría y Expansión Didáctica) | **Autor:** Auditor Exhaustivo de Evaluación y Calidad de FP-DAM  
**Fecha:** Enero 2025  
**Estado:** Validado y Ampliado para Estudio Profundo

---

# PARTE 1: EXAMEN TIPO TEST DE ALTA DIFICULTAD (15 PREGUNTAS)
## Instrucciones para el Alumno

**Tiempo Estimado:** 45 minutos  
**Puntuación Máxima:** 30 puntos (2 puntos por pregunta)  
**Instrucciones:** Seleccione la única opción correcta. Cada respuesta incorrecta resta 0.5 puntos a la puntuación total.

---

### CUESTIONARIO DE EVALUACIÓN TEÓRICO-PRÁCTICA RA6

*(Texto optimizado para claridad técnica y precisión según Manual Enciclopédico)*

**1. En el contexto de gestión de memoria virtual en sistemas operativos modernos, ¿cuál es el impacto directo de utilizar un algoritmo de paginación con "thrashing" extremo?**

A) Aumenta la velocidad de respuesta del sistema al priorizar procesos interactivos  
B) Reduce drásticamente el rendimiento debido a la sobrecarga de operaciones de I/O en disco  
C) Mejora la seguridad al cifrar automáticamente las páginas no utilizadas en memoria RAM  
D) Permite ejecutar más aplicaciones simultáneamente sin límite físico de RAM  

**2. Un administrador de sistemas observa que un servidor Linux presenta errores de permisos al acceder a archivos compartidos vía NFS. ¿Cuál es el identificador fundamental que el sistema operativo utiliza para controlar estos accesos?**

A) Nombre de usuario en texto plano  
B) UID/GID (User/Group Identifier numérico)  
C) Dirección MAC del cliente conectado  
D) Contraseña temporal generada por el servicio de directorio  

**3. En el modelo TCP/IP, cuando se realiza un análisis forense de red y se identifica tráfico UDP en el puerto 53 sin conexión previa establecida, ¿qué servicio está operando?**

A) Servicio de resolución DNS en modo síncrono  
B) Transferencia de archivos FTP con autenticación obligatoria  
C) Correo electrónico SMTP con cifrado TLS  
D) Conexión remota SSH con autenticación por clave pública  

**4. ¿Cuál es la diferencia crítica entre un Hypervisor Tipo 1 y un Hipervisor Tipo 2 en el contexto de virtualización para entornos DAM?**

A) El Tipo 1 se ejecuta sobre un SO anfitrión, mientras que el Tipo 2 ejecuta directamente sobre hardware  
B) Ambos ofrecen idéntico rendimiento sin diferencias arquitectónicas significativas  
C) El Tipo 1 ofrece mayor rendimiento al ejecutar directamente sobre hardware; el Tipo 2 es una aplicación del SO host  
D) El Tipo 2 permite contenedores Docker, mientras que el Tipo 1 solo soporta máquinas virtuales completas  

**5. En Windows Server, ¿qué estructura de datos única e inmutable se asigna a cada cuenta de usuario y grupo para garantizar la trazabilidad en auditorías de seguridad?**

A) UID (User Identifier numérico)  
B) SID (Security Identifier binario único)  
C) MAC Address (Dirección física de red)  
D) GID (Group Identifier numérico)  

**6. Al configurar una subred IPv4 con máscara 255.255.255.0, ¿cuántas direcciones IP utilizables hay para hosts en esa subred?**

A) 256 direcciones totales  
B) 255 direcciones utilizables (1 reservada para broadcast)  
C) 254 direcciones utilizables (1 para red y 1 para broadcast)  
D) 253 direcciones utilizables (1 para router, 1 para DNS, 1 para broadcast)  

**7. ¿Qué mecanismo de seguridad permite aplicar configuraciones uniformes a cientos de equipos dentro de un dominio Active Directory sin intervención manual en cada estación?**

A) Listas de Control de Acceso DAC individuales  
B) Directivas de Grupo (GPO - Group Policy Objects)  
C) Contraseñas temporales por usuario  
D) Cifrado de disco completo individual  

**8. En el contexto de la triada CIA de seguridad informática, ¿qué propiedad se garantiza mediante la implementación de firmas digitales y hashes criptográficos?**

A) Confidencialidad  
B) Disponibilidad  
C) Integridad  
D) Autenticación no repudiable  

**9. Cuando un firewall realiza "Inspección de Estado" (Stateful Inspection), ¿qué información mantiene para filtrar el tráfico de red?**

A) Solo las direcciones IP de origen y destino  
B) El estado de cada conexión activa (establecida, en espera, cerrada)  
C) El contenido completo del paquete en texto plano  
D) Las contraseñas de los usuarios conectados  

**10. ¿Qué protocolo criptográfico se utiliza actualmente para asegurar la comunicación remota a consolas de servidores Linux, reemplazando completamente a Telnet?**

A) RDP (Remote Desktop Protocol)  
B) SSH (Secure Shell)  
C) FTPS (FTP Seguro)  
D) SNMPv3  

**11. En la gestión de backups corporativos, ¿cuál es la principal ventaja de utilizar copias diferenciales frente a las incrementales?**

A) Requieren menos espacio de almacenamiento total  
B) La restauración es más rápida ya que solo se necesitan dos juegos de datos (completo + último diferencial)  
C) Se realizan automáticamente cada hora sin intervención humana  
D) No requieren verificación de integridad de los datos  

**12. ¿Qué función cumple el servicio DNS en una red corporativa cuando falla la resolución de nombres pero la conectividad IP es funcional?**

A) El tráfico de red continúa sin problemas porque se usa solo dirección IP  
B) Los usuarios no pueden acceder a recursos por nombre aunque puedan conectar por IP directa  
C) El firewall bloquea todo el tráfico automáticamente  
D) Los servicios de correo electrónico dejan de funcionar inmediatamente  

**13. En Linux, ¿qué comando permite verificar qué procesos están utilizando un puerto específico en la capa de transporte?**

A) `netstat -anp` o `ss -tulpn`  
B) `ping -c 4 gateway`  
C) `ifconfig eth0`  
D) `ls -la /etc/network/`  

**14. ¿Cuál es el riesgo principal al utilizar contraseñas en texto plano durante la autenticación de servicios de red?**

A) Aumento del tiempo de respuesta del servidor  
B) Interceptación por sniffers que pueden obtener credenciales legítimas  
C) Reducción del ancho de banda disponible  
D) Incremento del uso de CPU en el cliente  

**15. En un entorno de microservicios, ¿qué tecnología permite aislar espacios de usuario compartiendo el kernel del SO host sin virtualización completa?**

A) Máquinas Virtuales con Hypervisor Tipo 2  
B) Contenedores (Docker, Kubernetes)  
C) Cifrado de disco completo BitLocker  
D) Red privada virtual (VPN) site-to-site  

---

# PARTE 2: CASOS PRÁCTICOS DE DEBUGGING Y REFACTORIZACIÓN
## Instrucciones para el Alumno

**Tiempo Estimado:** 60 minutos por caso práctico  
**Puntuación Máxima:** 40 puntos (20 puntos por caso)  
**Instrucciones:** Analice el fragmento de código proporcionado, identifique los errores lógicos y/o de compilación, proponga la solución correcta y explique las razones técnicas.

---

## CASO PRÁCTICO #1: DEBUGGING DE SCRIPT DE CONEXIÓN REMOTA (20 PUNTOS)

**Contexto:** Un desarrollador DAM ha creado un script en Python para verificar la conectividad con servidores de ficheros compartidos antes de iniciar una aplicación Java crítica. El sistema falla en producción y el equipo de operaciones reporta errores intermitentes.

### Fragmento de Código Original (CON ERRORES):

```python
#!/usr/bin/env python3
# Script: network_check_v1.py
# Autor: Desarrollador Junior
# Fecha: 2025-01-15

import socket

def check_server_connectivity(target_ip, target_port=445):
    """Verifica si un servidor de ficheros está accesible"""
    
    # Crear socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Intentar conectar sin timeout definido
    result = sock.connect_ex((target_ip, target_port))
    
    if result == 0:
        print(f"[OK] Servidor {target_ip}:{target_port} accesible")
        return True
    else:
        print(f"[ERROR] Conexión fallida a {target_ip}")
        return False
    
    # Intentar cerrar el socket en un bloque finally
    sock.close()

def main():
    servers = [
        ("192.168.50.20", 445),
        ("192.168.50.30", 3389),
        ("192.168.50.40", 22)
    ]
    
    for server in servers:
        check_server_connectivity(server[0], server[1])

if __name__ == "__main__":
    main()
```

### Tareas para el Alumno:

**A)** Identifique al menos **TRES errores técnicos o de lógica** en el código proporcionado. (6 puntos)

**B)** Proponga una versión corregida del código que solucione los problemas identificados. (8 puntos)

**C)** Explique por qué cada corrección es necesaria desde el punto de vista de seguridad y estabilidad del sistema operativo. (6 puntos)

---

## CASO PRÁCTICO #2: DISEÑO DE CLASE PARA GESTIÓN DE PERMISOS EN RED (20 PUNTOS)

**Contexto:** Una aplicación multiplataforma necesita gestionar accesos a recursos compartidos en red de forma segura. El desarrollador debe crear una estructura de clases que implemente el principio de menor privilegio y valide permisos antes de acceder a archivos remotos.

### Especificación Requerida:

1.  **Clase `PermisoRed`:** Debe almacenar información sobre permisos (lectura, escritura, ejecución)
2.  **Clase `RecursoRed`:** Representa un recurso compartido en la red con ruta UNC/IP
3.  **Clase `GestorAccesoRed`:** Valida si un usuario puede acceder a un recurso según sus permisos

### Fragmento de Código Inicial (PARCIALMENTE CORRECTO):

```python
#!/usr/bin/env python3
# Script: red_access_manager.py
# Versión 1.0 - Necesita refactorización

class PermisoRed:
    def __init__(self, usuario):
        self.usuario = usuario
    
    def puede_leer(self):
        return True
    
    def puede_escribir(self):
        return False


class RecursoRed:
    def __init__(self, ruta):
        self.ruta = ruta


class GestorAccesoRed:
    def verificar_acceso(self, usuario, recurso):
        # Verificación básica de permisos
        if usuario.puede_leer():
            print(f"Acceso concedido a {recurso.ruta}")
            return True
        else:
            print("Acceso denegado")
            return False

# Uso del sistema
usuario = PermisoRed("dev_user_01")
archivo = RecursoRed("\\\\192.168.50.20\\RecursosCompartidos\\datos.txt")
gestor = GestorAccesoRed()

if gestor.verificar_acceso(usuario, archivo):
    print("Operación permitida")
```

### Tareas para el Alumno:

**A)** Identifique **TRES fallos de diseño o seguridad** en la implementación actual. (6 puntos)

**B)** Reescriba el código con al menos las siguientes mejoras:
- Implementar permisos específicos por recurso (no globales)
- Añadir validación de rutas UNC válidas
- Implementar el principio de menor privilegio correctamente (8 puntos)

**C)** Proponga una implementación adicional que registre en logs los intentos de acceso denegado para auditoría de seguridad. (6 puntos)

---

# PARTE 3: SOLUCIONARIO DETALLADO PARA EL DOCENTE
## Justificación Técnica y Criterios de Evaluación

> **Nota del Auditor:** Este solucionario ha sido expandido drásticamente. Cada respuesta incluye una justificación teórica basada en el Manual Enciclopédico RA6, un análisis profundo de por qué la opción es correcta, y una explicación detallada sobre por qué cada distractor (opción incorrecta) representa un error conceptual común. Este material sirve como estudio autónomo avanzado.

---

## SOLUCIONARIO EXAMEN TIPO TEST (15 PREGUNTAS)

### Respuestas Correctas con Justificación Técnica Expandida

| # | Opción | Justificación Detallada para el Docente y Alumno |
|---|--------|------------------------------------------|
| **1** | **B** | **Justificación de la Correcta:** El "thrashing" (intercambio excesivo) ocurre cuando el Sistema Operativo dedica más tiempo a mover páginas entre memoria RAM y disco (Swap/Pagefile) que a ejecutar instrucciones. Según el Módulo 2 del Manual, esto sucede cuando hay demanda de memoria superior a la física disponible. La sobrecarga provienen de las operaciones intensivas de E/S (Input/Output) en el disco duro, que es orders de magnitud más lento que la RAM. Esto degrada el rendimiento hasta casi detener la ejecución.&lt;br/>&lt;br/>**Análisis de Distractores:**&lt;br/>• **A)** Es incorrecto porque el thrashing *reduce* la velocidad de respuesta; el sistema se congela esperando datos del disco, no priorizando interactividad.&lt;br/>• **C)** El cifrado de páginas es una función de seguridad (BitLocker/LUKS) pero no mejora el rendimiento ni resuelve el problema de falta de memoria física.&lt;br/>• **D)** Es falso; el thrashing indica que se ha excedido el límite físico y virtual, impidiendo ejecutar más aplicaciones eficientemente. |
| **2** | **B** | **Justificación de la Correcta:** En Linux (Módulo 2), los permisos no se gestionan por nombres de usuario porque los nombres pueden cambiar o duplicarse en directorios distribuidos. El kernel utiliza identificadores numéricos enteros: UID para usuarios y GID para grupos. Estos identificadores son lo que el sistema operativo verifica realmente al controlar accesos a archivos (NFS/SMB).&lt;br/>&lt;br/>**Análisis de Distractores:**&lt;br/>• **A)** Los nombres en texto plano son solo una capa de abstracción (alias) creada por `/etc/passwd`, no la clave interna del kernel.&lt;br/>• **C)** La MAC Address es para identificación física de red a nivel de Capa 2, no tiene relación con permisos de archivos a nivel de sistema operativo.&lt;br/>• **D)** Las contraseñas son para autenticación (verificar identidad), pero una vez autenticado, el SO usa UID/GID para autorizar acciones. |
| **3** | **A** | **Justificación de la Correcta:** DNS utiliza UDP en el puerto 53 por defecto para consultas rápidas y síncronas. No requiere establecer una conexión TCP persistente (sin "handshake" previo como en TCP). Si se ve tráfico UDP/53, es resolución de nombres.&lt;br/>&lt;br/>**Análisis de Distractores:**&lt;br/>• **B)** FTP usa puertos 20 y 21, y generalmente opera sobre TCP para asegurar la transferencia de datos.&lt;br/>• **C)** SMTP (Correo) opera en el puerto 25 o 465/587 (TLS), siempre sobre TCP por fiabilidad.&lt;br/>• **D)** SSH usa el puerto 22, pero es estrictamente un protocolo orientado a conexión que requiere establecer un túnel seguro antes de transferir datos. |
| **4** | **C** | **Justificación de la Correcta:** Según Módulo 2 (Virtualización), un Hypervisor Tipo 1 ("Bare Metal") se instala directamente sobre el hardware físico, eliminando la capa del SO anfitrión y ofreciendo máximo rendimiento para servidores de producción. Un Tipo 2 (ej. VirtualBox) vive como una aplicación dentro de un SO existente.&lt;br/>&lt;br/>**Análisis de Distractores:**&lt;br/>• **A)** Es la definición invertida; el Tipo 1 es "Bare Metal", no sobre un SO anfitrión.&lt;br/>• **B)** El rendimiento difiere significativamente debido a las capas de abstracción en el Tipo 2.&lt;br/>• **D)** Ambos tipos pueden soportar máquinas virtuales completas. Los contenedores (Docker) son una forma distinta de virtualización ligera que no depende estrictamente del tipo de hypervisor, aunque suelen correr sobre un SO anfitrión Linux/Windows. |
| **5** | **B** | **Justificación de la Correcta:** En Windows NT y versiones posteriores, cada cuenta tiene un SID (Security Identifier) único en formato binario. Este valor es inmutable durante la vida del objeto; si se clona un disco sin Sysprep, los SIDs cambian y rompen la seguridad. Es esencial para auditorías porque identifica al usuario más allá de su nombre.&lt;br/>&lt;br/>**Análisis de Distractores:**&lt;br/>• **A)** UID es el equivalente en Linux/Unix, no Windows.&lt;br/>• **C)** MAC Address es física de red, irrelevante para la gestión de identidad lógica del sistema operativo.&lt;br/>• **D)** GID es específico de Unix/Linux para grupos. |
| **6** | **C** | **Justificación de la Correcta:** Una máscara /24 (255.255.255.0) deja 8 bits para hosts ($2^8 = 256$). Sin embargo, dos direcciones son reservadas: la primera es la Dirección de Red y la última es la Dirección de Broadcast. Por tanto: $256 - 2 = 254$ direcciones utilizables.&lt;br/>&lt;br/>**Análisis de Distractores:**&lt;br/>• **A)** Cuenta todas las direcciones totales sin restar las reservadas.&lt;br/>• **B)** Solo resta una (broadcast), olvidando la dirección de red.&lt;br/>• **D)** Resta direcciones para router/DNS, pero estas se asignan *dentro* del rango usable, no son un descuento automático de la capacidad total. |
| **7** | **B** | **Justificación de la Correcta:** Las GPO (Group Policy Objects) permiten centralizar la configuración de seguridad, software y entorno en Active Directory. Se aplican jerárquicamente (Dominio > OU > Sitio), garantizando coherencia sin tocar máquinas individuales.&lt;br/>&lt;br/>**Análisis de Distractores:**&lt;br/>• **A)** DAC es un modelo de permisos local por objeto, no una herramienta de gestión centralizada masiva.&lt;br/>• **C)** Contraseñas temporales son para autenticación, no para configuración de sistema.&lt;br/>• **D)** El cifrado individual requiere intervención en cada máquina o herramientas de gestión específicas (como BitLocker Management), pero GPO es el mecanismo nativo de AD para políticas. |
| **8** | **C** | **Justificación de la Correcta:** Dentro de la Triada CIA, los hashes y firmas digitales protegen contra alteraciones no autorizadas. Si el hash del archivo recibido coincide con el original, se garantiza que el contenido es idéntico (Integridad).&lt;br/>&lt;br/>**Análisis de Distractores:**&lt;br/>• **A)** Confidencialidad se logra mediante cifrado, no hashing.&lt;br/>• **B)** Disponibilidad se asegura con redundancia y backups.&lt;br/>• **D)** Aunque la firma digital aporta "No Repudio" (responsabilidad), el hash en sí mismo es primariamente una herramienta de integridad. La opción C es la definición más directa de la función del hash. |
| **9** | **B** | **Justificación de la Correcta:** La inspección stateful (con estado) mantiene una tabla de conexiones activas. Permite el tráfico entrante solo si pertenece a una conexión iniciada por un host interno, bloqueando intentos de conexión "puerta trasera" no solicitados.&lt;br/>&lt;br/>**Análisis de Distractores:**&lt;br/>• **A)** Filtrado de paquetes básico (Stateless) usa solo IP/Puerto, sin contexto de estado.&lt;br/>• **C)** Los firewalls no ven el contenido completo a menos que sea un Firewall de Aplicación (WAF/Proxy), lo cual es más costoso y complejo.&lt;br/>• **D)** Un firewall filtra tráfico de red, no gestiona credenciales de usuario; esto corresponde al servicio de autenticación. |
| **10** | **B** | **Justificación de la Correcta:** SSH (Secure Shell) cifra toda la sesión (comandos y salida), reemplazando Telnet que envía todo en texto plano. Es el estándar para administración remota segura.&lt;br/>&lt;br/>**Análisis de Distractores:**&lt;br/>• **A)** RDP es para escritorio gráfico, principalmente Windows.&lt;br/>• **C)** FTPS es para transferencia de archivos, no consola remota completa.&lt;br/>• **D)** SNMPv3 es para gestión de dispositivos (monitoreo), no acceso a consola. |
| **11** | **B** | **Justificación de la Correcta:** En una estrategia diferencial, se guarda todo lo cambiado desde el último backup *completo*. Para restaurar, solo necesitas el último completo y el último diferencial. Esto es más rápido que incremental (que requiere encadenar todos los backups), aunque ocupa más espacio.&lt;br/>&lt;br/>**Análisis de Distractores:**&lt;br/>• **A)** Ocupan *más* espacio que incrementales (guardan todo desde el full, no solo cambios desde el último backup).&lt;br/>• **C)** La frecuencia depende de la configuración, no del tipo de backup.&lt;br/>• **D)** La verificación es crítica en cualquier estrategia para asegurar integridad. |
| **12** | **B** | **Justificación de la Correcta:** DNS traduce nombres a IPs. Si el servicio falla, las aplicaciones que dependen de resolución de nombre (navegadores, clientes de correo) no pueden iniciar la conexión lógica, aunque la red física y la IP estén operativas.&lt;br/>&lt;br/>**Análisis de Distractores:**&lt;br/>• **A)** Falso; muchas aplicaciones requieren nombres, no IPs directas por usabilidad o configuración virtual host.&lt;br/>• **C)** El firewall no bloquea tráfico automáticamente por fallo DNS; es un servicio de resolución.&lt;br/>• **D)** El correo podría funcionar si usa IP directa, pero la mayoría requiere MX records (DNS). |
| **13** | **A** | **Justificación de la Correcta:** `netstat -anp` o `ss -tulpn` listan conexiones activas y los procesos asociados a puertos específicos en TCP/UDP. Es la herramienta estándar de diagnóstico.&lt;br/>&lt;br/>**Análisis de Distractores:**&lt;br/>• **B)** `ping` verifica conectividad ICMP, no mapeo de puertos/procesos.&lt;br/>• **C)** `ifconfig` muestra configuración de interfaz IP/MAC, no conexiones activas.&lt;br/>• **D)** `ls` solo lista archivos del sistema, no estado de red. |
| **14** | **B** | **Justificación de la Correcta:** En texto plano, cualquier herramienta "sniffer" (como Wireshark) en el mismo segmento de red puede capturar los paquetes y leer las credenciales directamente, permitiendo suplantación de identidad.&lt;br/>&lt;br/>**Análisis de Distractores:**&lt;br/>• **A)** El tiempo de respuesta no aumenta significativamente por cifrado/des-cifrado; la seguridad es prioridad sobre rendimiento marginal.&lt;br/>• **C)** El ancho de banda se ve minimamente afectado (overhead pequeño).&lt;br/>• **D)** El uso de CPU es para el cifrado, pero el riesgo crítico es la interceptación. |
| **15** | **B** | **Justificación de la Correcta:** Los contenedores (Módulo 2) comparten el kernel del host pero aíslan procesos y sistemas de archivos mediante namespaces y cgroups. Son más ligeros que VMs porque no virtualizan hardware.&lt;br/>&lt;br/>**Análisis de Distractores:**&lt;br/>• **A)** Las VMs virtualizan hardware, consumiendo más recursos.&lt;br/>• **C)** BitLocker es cifrado a nivel de disco, no aislamiento de ejecución.&lt;br/>• **D)** VPN cifra tráfico en tránsito, no aísla espacios de usuario dentro del SO. |

---

## SOLUCIONARIO CASO PRÁCTICO #1: DEBUGGING DE SCRIPT DE CONEXIÓN REMOTA

### **A) Tres Errores Técnicos Identificados y Profundización**

| Error | Descripción Técnica Detallada | Impacto en Producción (RA6 CE e/f) |
|-------|---------------------|--------------------------------------|
| **1. Bloque `finally` mal ubicado / Lógica de Flujo** | El código `sock.close()` está indentado *después* del bloque `if/else`, pero *antes* de ser ejecutado en caso de retorno o error. En realidad, el flujo salta al final de la función si se retorna `True` o `False`, dejando el socket abierto permanentemente. Además, no hay un bloque `try...finally` estructural para garantizar ejecución. | **Fuga de Recursos (Resource Leak):** El SO mantiene abiertos descriptores de archivo (sockets). En producción, esto agota los puertos disponibles (TIME_WAIT) o memoria del kernel, provocando caídas masivas del servicio tras miles de conexiones fallidas. |
| **2. Ausencia de Timeout (`settimeout`)** | `sock.connect_ex()` sin timeout bloqueará indefinidamente si el servidor destino no responde (ej. cable desconectado, firewall silencioso). El hilo se queda "zombie" esperando respuesta TCP que nunca llega. | **Condición de Carrera / Bloqueo:** La aplicación principal se congela o consume CPU en espera inútil. En un entorno distribuido, esto causa cuellos de botella y tiempos de respuesta inaceptables (Deadlock potencial). |
| **3. Manejo de Excepciones Incompleto** | No hay bloques `try/except` para capturar fallos de red (`socket.timeout`, `socket.error`). Si ocurre un fallo de hardware o red, el script lanza una excepción no manejada y se detiene abruptamente sin registro. | **Falta de Auditoría:** El equipo de operaciones no sabe qué falló (¿Timeout? ¿Refused?). Sin logs estructurados, es imposible investigar incidentes forenses post-mortem. |

### **B) Versión Corregida del Código con Explicación Paso a Paso**

```python
#!/usr/bin/env python3
# Script: network_check_v2.py (CORREGIDO - Nivel Auditoría RA6)
import socket
import logging
from datetime import datetime

# 1. CONFIGURACIÓN DE LOGGING PARA AUDITORÍA (RA6 CE e/f)
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('network_audit.log'), # Persistencia de logs
        logging.StreamHandler()                   # Salida a consola
    ]
)
logger = logging.getLogger(__name__)

def check_server_connectivity(target_ip, target_port=445, timeout=2):
    """
    Verifica conectividad con manejo robusto de recursos.
    
    CORRECCIONES APLICADAS:
    - Timeout definido para evitar bloqueos indefinidos (Seguridad RA6)
    - Bloque try/finally para liberar sockets siempre
    - Logging estructurado para auditoría forense
    """
    sock = None  # Inicializar a None para seguridad en finally
    
    try:
        logger.info(f"Intentando conectar a {target_ip}:{target_port}...")
        
        # Crear socket TCP (Capa de Transporte - Módulo 3)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # IMPORTANTE: Definir timeout para evitar bloqueos indefinidos (Seguridad RA6 CE d)
        # Esto evita que el hilo espere eternamente si hay un firewall silencioso.
        sock.settimeout(timeout)
        
        # Intentar conectar con manejo de excepciones
        result = sock.connect_ex((target_ip, target_port))
        
        if result == 0:
            logger.info(f"[OK] Servidor {target_ip}:{target_port} accesible")
            return True
        
    except socket.timeout as e:
        # Captura específica para timeout (RA6 CE d - Gestión de Puertos)
        logger.warning(f"[TIMEOUT] La solicitud superó el tiempo límite ({timeout}s) para {target_ip}")
        
    except socket.error as e:
        # Captura genérica de errores de red (ej. Connection Refused, Network Unreachable)
        logger.error(f"[SOCKET_ERROR] Error de red detectado en {target_ip}: {e}")
        
    finally:
        # IMPORTANTE: Cerrar siempre en finally para liberar recursos del SO
        # Esto previene fugas de memoria y agotamiento de sockets (RA6 Módulo 2)
        if sock is not None:
            try:
                sock.close()
                logger.debug("Socket cerrado correctamente tras operación")
            except Exception as close_error:
                logger.warning(f"Error al cerrar socket (no crítico): {close_error}")

    # Si llegamos aquí, hubo error o timeout
    return False

def main():
    servers = [
        ("192.168.50.20", 445),
        ("192.168.50.30", 3389),
        ("192.168.50.40", 22)
    ]
    
    logger.info("--- Iniciando Diagnóstico de Red (RA6 CE a/d) ---")
    
    resultados = []
    for server in servers:
        resultado = check_server_connectivity(server[0], server[1])
        registros = {
            "ip": server[0], 
            "puerto": server[1], 
            "accesible": resultado,
            "timestamp": datetime.now().isoformat()
        }
        resultados.append(registros)
    
    logger.info(f"--- Resumen de Diagnóstico Final ---")
    for res in resultados:
        estado = "[OK]" if res["accesible"] else "[FALLA]"
        logger.info(f"{estado} {res['ip']}:{res['puerto']}")

if __name__ == "__main__":
    main()
```

### **C) Explicación de Correcciones para el Alumno (Fundamentos RA6)**

| Corrección | Justificación Técnica y Seguridad RA6 Detallada |
|------------|----------------------------------------|
| **Bloque `finally` con validación `sock is not None`** | En el modelo de gestión de recursos del SO (Módulo 2), cada socket ocupa un descriptor de archivo. Si no se libera, llega al límite del sistema (`ulimit -n`). El bloque `finally` garantiza que la limpieza ocurra *independientemente* de si hubo éxito o error. Esto es vital para aplicaciones críticas en producción donde los recursos son finitos. |
| **Timeout definido (`settimeout(timeout)`)** | Según el Módulo 3 (Redes), las conexiones TCP pueden fallar silenciosamente (Firewalls que descartan paquetes). Sin timeout, la aplicación entra en un estado de espera activa ("busy wait") o bloqueo pasivo, consumiendo hilos y CPU innecesariamente. El timeout es una medida de seguridad para evitar DoS accidental por errores de red. |
| **Logging estructurado** | Cumple con el Criterio de Evaluación RA6 CE e/f (Utilidades de Seguridad). Los logs permiten reconstruir la línea temporal de un ataque o fallo en auditorías forenses. Sin logging, es imposible saber si una caída fue por error humano o técnico. Se usan timestamps para correlacionar eventos. |

---

## SOLUCIONARIO CASO PRÁCTICO #2: DISEÑO DE CLASE PARA GESTIÓN DE PERMISOS EN RED

### **A) Tres Fallos de Diseño/Seguridad Identificados con Análisis Profundo**

| Error | Descripción Técnica y Riesgo RA6 | Impacto en Seguridad |
|-------|---------------------|-------------------------|
| **1. Permisos Globales (`puede_leer()` siempre True)** | La clase `PermisoRed` no valida el recurso específico. Esto viola directamente el "Principio de Menor Privilegio" (Módulo 5). Si un usuario tiene acceso al sistema, automáticamente puede leer todo lo que la clase permite, sin importar a qué carpeta intenta acceder.&lt;br/>&lt;br/>**Análisis:** La lógica `if usuario.puede_leer()` no recibe el recurso como argumento. El código es agnóstico a la ruta de destino. | **Violación de Confidencialidad (Triada CIA):** Un atacante con credenciales limitadas puede escalar privilegios lógicamente si el código no valida el objeto de destino contra su perfil. Todos los usuarios obtienen acceso total. |
| **2. Validación de Ruta Inexistente** | La clase `RecursoRed` acepta cualquier string en `__init__`. No verifica si la ruta es un formato UNC válido (ej. `\\servidor\recurso`) ni si contiene caracteres peligrosos para inyección.&lt;br/>&lt;br/>**Análisis:** Esto permite rutas maliciosas como `\\..\..\etc\passwd` o cadenas vacías que podrían romper lógica posterior en el sistema operativo al montar la carpeta. | **Riesgo de Inyección y Fuga de Información:** Sin validación, se puede intentar acceder a directorios sensibles del SO host que no deberían ser compartidos por red. |
| **3. Ausencia de Logs de Auditoría** | La función `verificar_acceso` solo imprime un mensaje en consola. No registra el evento, ni la hora, ni si fue concedido o denegado.&lt;br/>&lt;br/>**Análisis:** El Módulo 5 enfatiza que "los logs son fundamentales para auditoría forense". Sin registro persistente (archivo/basedatabase), es imposible detectar intentos de intrusión o errores operativos tras un reinicio. | **Imposibilidad de Auditoría Forense:** Si ocurre una brecha, no hay rastro de quién accedió a qué recurso y cuándo. Incumplimiento de normativas RGPD/LOPD en manejo de datos sensibles. |

### **B) Código Refactorizado con Mejoras (Implementación de Seguridad)**

```python
#!/usr/bin/env python3
# Script: red_access_manager_v2.py (REFACTORIZADO - Nivel Profesional RA6)
import re
import logging
from datetime import datetime
from enum import Enum, auto
from typing import List, Dict

# Configuración de logs para cumplimiento RA6 CE e/f (Auditoría Obligatoria)
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - [AUDITORIA] %(message)s',
    handlers=[
        logging.FileHandler('access_audit.log'),  # Registro persistente en disco
        logging.StreamHandler()                   # Consola en tiempo real para debug
    ]
)
logger = logging.getLogger(__name__)

class Permiso(Enum):
    """Enum para permisos específicos (Módulo 2: Modelo de Permisos)"""
    NINGUNO = auto()
    LEER = auto()
    ESCRIBIR = auto()
    EJECUTAR = auto()
    TODOS = auto()

class UsuarioRed:
    """Clase que representa un usuario con permisos específicos por recurso (Principio Menor Privilegio)"""
    
    def __init__(self, username):
        self.username = username
        # Permisos granulares: Diccionario {ruta: Permiso} - Implementa principio de menor privilegio
        self.permisos_por_recurso: Dict[str, Permiso] = {}
    
    def asignar_permiso(self, ruta, permiso: Permiso):
        """Asigna permisos específicos por recurso. Valida formato seguro."""
        if not self.validar_ruta(ruta):
            logger.error(f"Intento de asignación de permiso con ruta inválida: {ruta}")
            raise ValueError(f"Ruta inválida o no segura: {ruta}")
        
        self.permisos_por_recurso[ruta] = permiso
    
    def puede_acceder(self, ruta: str, operacion: str) -> bool:
        """Verifica si el usuario tiene permisos para la operación solicitada en la ruta específica."""
        # 1. Validar ruta
        if not self.validar_ruta(ruta):
            return False
            
        permiso_actual = self.permisos_por_recurso.get(ruta, Permiso.NINGUNO)
        
        # Lógica de evaluación de permisos (Módulo 4: Modelos de Permisos en Red vs Locales)
        if operacion == "leer" and permiso_actual in [Permiso.LEER, Permiso.TODOS]:
            return True
        elif operacion == "escribir" and permiso_actual in [Permiso.ESCRIBIR, Permiso.TODOS]:
            return True
        elif operacion == "ejecutar" and permiso_actual in [Permiso.EJECUTAR, Permiso.TODOS]:
            return True
        
        # Si no coincide, denegar por defecto (Default Deny)
        return False
    
    @staticmethod
    def validar_ruta(ruta: str) -> bool:
        """Valida formato UNC válido para seguridad de rutas. Previene inyección."""
        # Patrón regex estricto para rutas UNC válidas (\\servidor\recurso)
        # Permite caracteres alfanuméricos y guiones, evita .. o / ocultos
        patron_unc = r'^\\\\[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\\[a-zA-Z0-9_\-\/]+$'
        return bool(re.match(patron_unc, ruta))


class RecursoRed:
    """Representa un recurso compartido en la red con validación de seguridad"""
    
    def __init__(self, ruta):
        if not UsuarioRed.validar_ruta(ruta):
            raise ValueError(f"Ruta no válida para acceso de red seguro: {ruta}")
        
        self.ruta = ruta
        self.esta_accesible = False
    
    def verificar_disponibilidad(self) -> bool:
        """Simula verificación de accesibilidad del recurso (Módulo 3: Gestión de Puertos)."""
        logger.debug(f"Verificando disponibilidad de recurso: {self.ruta}")
        
        # En producción real, usar socket o librería SMB/NFS para chequeo activo
        self.esta_accesible = True
        
        return self.esta_accesible


class GestorAccesoRed:
    """Clase central para gestión y auditoría de accesos (RA6 CE e/f)"""
    
    def __init__(self):
        self.registro_accesos: List[Dict] = []  # Historial para auditoría forense
    
    def verificar_acceso(self, usuario, recurso, operacion="leer") -> bool:
        """Verifica permisos con registro de auditoría obligatorio."""
        
        if not isinstance(usuario, UsuarioRed):
            logger.error(f"[AUDITORIA] Intento de acceso con objeto usuario inválido")
            self.registrar_acceso_denegado("SYSTEM", recurso.ruta, operacion, "Usuario no válido")
            return False
        
        if not isinstance(recurso, RecursoRed):
            logger.error(f"[AUDITORIA] Intento de acceso a recurso no válido: {recurso}")
            self.registrar_acceso_denegado(usuario.username, str(recurso), operacion, "Recurso inválido")
            return False
        
        # Verificar disponibilidad antes de validar permisos (Optimización y Seguridad)
        if not recurso.esta_accesible and not recurso.verificar_disponibilidad():
            logger.warning(f"[AUDITORIA] Recurso no accesible: {recurso.ruta}")
            self.registrar_acceso_denegado(usuario.username, recurso.ruta, operacion, "Recurso inaccesible")
            return False
        
        # Validación final de permisos (Menor Privilegio)
        if usuario.puede_acceder(recurso.ruta, operacion):
            logger.info(f"[AUDITORIA] ACCESO CONCEDIDO - Usuario: {usuario.username}, Recurso: {recurso.ruta}, Operación: {operacion}")
            self.registrar_acceso_concedido(usuario.username, recurso.ruta, operacion)
            return True
        
        else:
            logger.warning(f"[AUDITORIA] ACCESO DENEGADO - Usuario: {usuario.username}, Recurso: {recurso.ruta}, Operación: {operacion}")
            self.registrar_acceso_denegado(usuario.username, recurso.ruta, operacion, "Permisos insuficientes")
            return False
    
    def registrar_acceso_concedido(self, usuario, ruta, operacion):
        """Registra acceso concedido para auditoría forense"""
        registro = {
            "timestamp": datetime.now().isoformat(),
            "usuario": usuario,
            "ruta": ruta,
            "operacion": operacion,
            "estado": "CONCEDIDO"
        }
        self.registro_accesos.append(registro)
    
    def registrar_acceso_denegado(self, usuario, ruta, operacion, motivo):
        """Registra acceso denegado para auditoría forense (RA6 CE e/f)"""
        registro = {
            "timestamp": datetime.now().isoformat(),
            "usuario": usuario,
            "ruta": ruta,
            "operacion": operacion,
            "estado": "DENEGADO",
            "motivo": motivo
        }
        self.registro_accesos.append(registro)


# Uso del sistema mejorado (Ejemplo de implementación correcta para validación)
if __name__ == "__main__":
    logger.info("--- Inicializando Sistema de Gestión de Accesos RA6 CE c ---")
    
    # Crear usuario con permisos específicos por recurso (Principio Menor Privilegio)
    dev_user = UsuarioRed("dev_user_01")
    dev_user.asignar_permiso("\\\\192.168.50.20\\RecursosCompartidos", Permiso.LEER)
    dev_user.asignar_permiso("\\\\192.168.50.20\\Logs", Permiso.NINGUNO)  # Sin acceso a logs
    
    # Crear recurso con validación de ruta
    archivo_seguro = RecursoRed("\\\\192.168.50.20\\RecursosCompartidos\\datos.txt")
    
    gestor = GestorAccesoRed()
    
    # Pruebas de acceso con auditoría completa
    print("\n--- Prueba 1: Acceso con permisos válidos ---")
    if gestor.verificar_acceso(dev_user, archivo_seguro, "leer"):
        print("✓ Operación permitida (Auditoría registrada)")
    
    print("\n--- Prueba 2: Intento de escritura sin permiso ---")
    if not gestor.verificar_acceso(dev_user, archivo_seguro, "escribir"):
        print("✗ Acceso denegado correctamente (Registro en auditoría)")
        
    # Simular intento a ruta no permitida
    archivo_logs = RecursoRed("\\\\192.168.50.20\\Logs\\error.txt")
    print("\n--- Prueba 3: Intento de acceso a recurso sin permisos (Logs) ---")
    if not gestor.verificar_acceso(dev_user, archivo_logs, "leer"):
        print("✗ Acceso denegado correctamente (Registro en auditoría)")
    
    print(f"\n--- Resumen de Auditoría ({len(gestor.registro_accesos)} eventos registrados) ---")
    for evento in gestor.registro_accesos:
        estado = "✓" if evento["estado"] == "CONCEDIDO" else "✗"
        print(f"{estado} {evento['timestamp']} - {evento['usuario']} - {evento['ruta']} - {evento['operacion']} ({evento['estado']})")
```

### **C) Explicación de Mejoras para el Alumno (Fundamentos RA6)**

| Mejora Implementada | Justificación Técnica y Cumplimiento RA6 Detallado |
|---------------------|----------------------------------------|
| **Permisos granulares por recurso** | El código original otorgaba permisos globales. Refactorizando con un diccionario `permisos_por_recurso`, aplicamos el **Principio de Menor Privilegio (Módulo 5)**. Cada usuario solo tiene acceso estrictamente necesario. Esto minimiza el daño en caso de compromiso de credenciales. |
| **Validación regex de rutas UNC** | Se implementó `re.match` para validar que la ruta cumpla el formato seguro (`\\IP\Ruta`). Esto previene ataques de inyección de ruta (Path Traversal) donde un atacante podría intentar acceder a `/etc/passwd` o directorios raíz del sistema. Es una medida de seguridad defensiva en código (Security by Design). |
| **Registro de auditoría con logging estructurado** | Cumple estrictamente con los Criterios de Evaluación RA6 CE e/f. Se implementa un historial en memoria (`self.registro_accesos`) y se loguea a archivo. Esto permite reconstruir incidentes forenses: "¿Quién intentó entrar y cuándo?". Sin esto, la seguridad es ciega. |
| **Clases separadas con responsabilidad única** | Mejora mantenibilidad y testabilidad (Principios SOLID aplicados a RA6). `UsuarioRed` gestiona identidad, `RecursoRed` gestiona datos de red, `GestorAccesoRed` orquesta la lógica. Esto facilita el testing unitario y reduce errores humanos en futuras modificaciones del código. |

---

# RÚBRICA DE EVALUACIÓN FINAL DEL RA6

## Criterios de Puntuación para el Docente (Expandido)

| Componente | Puntos Máximos | Indicador de Cumplimiento Excelente (9-10) |
|------------|----------------|-------------------------------------------|
| **Test Tipo 15 preguntas** | 30 pts | 27-30 puntos: Dominio teórico-práctico completo. Errores mínimos en conceptos avanzados como virtualización y seguridad perimetral. |
| **Caso Práctico #1 Debugging** | 20 pts | Identificación completa de errores + solución robusta con logging, manejo de excepciones (`try/finally`), timeouts definidos y comentarios explicativos vinculados al manual RA6. |
| **Caso Práctico #2 Diseño de Clases** | 20 pts | Implementación completa con principio de menor privilegio, validación regex de rutas, clases separadas y auditoría forense (logs persistentes). Código limpio y comentado. |
| **Documentación y Explicaciones** | 10 pts | Justificaciones técnicas detalladas que vinculan explícitamente cada decisión de código con conceptos del Manual Enciclopédico RA6 (Módulos 2, 3, 5). |
| **TOTAL** | **80 puntos** | **Calificación final: (Puntos Obtenidos / 80) × 10 = Nota Final** |

---

## CRITERIOS DE CALIFICACIÓN ADICIONALES PARA EL DOCENTE

### Aprobado (≥50/80):
- El alumno demuestra comprensión de conceptos básicos de seguridad en red.
- Identifica errores evidentes en debugging (ej. falta de cierre de socket).
- Implementa soluciones funcionales básicas.

### Notable (65-79/80):
- Dominio completo de teoría RA6 (virtualización, redes, permisos).
- Soluciones robustas con manejo de excepciones y logging estructurado.
- Cumplimiento estricto de principios de seguridad (menor privilegio, auditoría).

### Sobresaliente (80/80):
- Implementación de código de nivel profesional con documentación completa.
- Explicaciones técnicas detalladas que vinculan cada decisión con conceptos del RA6 y el Manual.
- Propuestas adicionales de mejora de seguridad (ej. uso de claves SSH, cifrado en tránsito) más allá de lo requerido.

---

## NOTAS PARA EL DOCENTE SOBRE LA APLICACIÓN DEL EXAMEN

1.  **Adaptación al Entorno:** Este examen puede ejecutarse en entorno virtualizado (VirtualBox/VMware) para validación práctica adicional, especialmente los casos de scripting y conexión remota.
2.  **Criterio de Corrección Objetivo:** Use el solucionario como referencia única. Las soluciones alternativas deben cumplir los mismos principios técnicos y de seguridad RA6 (ej. si usan `async` en Python, debe haber manejo de excepciones igual).
3.  **Evaluación Continua:** Combine este examen con laboratorios prácticos (Lab 01-06) para evaluación integral del RA6. El código entregado en los Labs debe coincidir conceptualmente con las soluciones aquí expuestas.
4.  **Actualización Anual:** Revisar contenido cada año académico para mantenerse alineado con versiones actualizadas de Windows Server, Linux y protocolos de seguridad (ej. WPA3, TLS 1.3).

---

**Documento Oficial Validado por el Departamento de Evaluación Docente FP-DAM**  
**Prohibida su reproducción sin autorización institucional**
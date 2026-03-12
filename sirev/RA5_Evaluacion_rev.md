

# BANCO DE EVALUACIÓN - RA5: INTERCONEXIÓN Y ARQUITECTURA DE REDES PARA DESARROLLO MULTIPLATAFORMA

**Módulo Profesional:** Sistemas Informáticos  
**Ciclo Formativo:** Desarrollo de Aplicaciones Multiplataforma (DAM)  
**Resultado de Aprendizaje 5 (RA5):** Interconecta sistemas en red configurando dispositivos y protocolos  
**Nivel:** Formación Profesional Superior  
**Versión del Documento:** 2.1 - Banco de Evaluación Completo con Solucionario Didáctico Expandido

---

## ÍNDICE DE CONTENIDOS

1. [Examen Tipo Test (15 Preguntas)](#examen-tipo-test)
2. [Caso Práctico de Debugging #1](#caso-práctico-de-debugging-1)
3. [Caso Práctico de Debugging #2](#caso-práctico-de-debugging-2)
4. [Solucionario Detallado para el Docente y Estudiante](#solucionario-detalhado-para-el-docente-y-estudiante)

---

## 1. EXAMEN TIPO TEST (15 PREGUNTAS DE ALTA DIFICULTAD)

**Instrucciones:** Selecciona la única respuesta correcta para cada pregunta. Cada pregunta vale 0,67 puntos sobre un total de 10 puntos.

### Pregunta 1
En el modelo TCP/IP, ¿qué capa es responsable del direccionamiento lógico y el enrutamiento entre redes diferentes?

A) Capa de Aplicación  
B) Capa de Transporte  
C) Capa de Red  
D) Capa de Acceso a la Red

---

### Pregunta 2
Al configurar una dirección IPv4 estática para un servidor web, ¿qué parámetro es fundamental para permitir que los dispositivos externos accedan al servicio?

A) Dirección MAC del adaptador de red  
B) Puerta de enlace predeterminada (Default Gateway)  
C) Protocolo DHCP activado en el cliente  
D) Dirección IP multicast

---

### Pregunta 3
¿Qué protocolo se utiliza para la resolución automática de nombres de dominio a direcciones IP en una red TCP/IP?

A) ARP  
B) ICMP  
C) DNS  
D) NAT

---

### Pregunta 4
En el contexto de seguridad inalámbrica, ¿cuál es el protocolo más seguro actualmente disponible para redes WLAN según los estándares IEEE 802.11?

A) WEP  
B) WPA  
C) WPA2  
D) WPA3

---

### Pregunta 5
¿Qué dispositivo de red opera principalmente en la Capa 2 del modelo OSI y utiliza tablas MAC para dirigir el tráfico entre dispositivos en una LAN?

A) Router  
B) Hub  
C) Switch  
D) Repetidor

---

### Pregunta 6
Un desarrollador necesita implementar comunicación UDP para un servicio de streaming de video. ¿Qué característica de UDP es más relevante para este caso de uso?

A) Garantía de entrega ordenada de paquetes  
B) Establecimiento de conexión previa antes del envío  
C) Baja sobrecarga y transmisión sin confirmación  
D) Control de flujo bidirectional

---

### Pregunta 7
¿Cuál es el rango de puertos TCP/UDP reservados para servicios bien conocidos (Well-Known Ports)?

A) 0 - 1023  
B) 1024 - 49151  
C) 49152 - 65535  
D) 80 - 443

---

### Pregunta 8
En una red corporativa con múltiples VLANs, ¿qué dispositivo es necesario para permitir la comunicación entre diferentes segmentos de red lógica?

A) Switch Layer 2  
B) Router o Switch Layer 3  
C) Hub Ethernet  
D) Repetidor Wi-Fi

---

### Pregunta 9
¿Qué herramienta de diagnóstico utiliza el protocolo ICMP para verificar la conectividad básica entre dos nodos en una red IP?

A) Tracert/Traceroute  
B) Ping  
C) Nslookup  
D) Netstat

---

### Pregunta 10
Al implementar un túnel SSH para acceso remoto seguro, ¿qué tipo de cifrado se utiliza principalmente para proteger los datos en tránsito?

A) Cifrado asimétrico y simétrico combinado  
B) Solo cifrado simétrico  
C) Hashing MD5  
D) Cifrado WEP

---

### Pregunta 11
¿Qué significa el campo TTL (Time To Live) en un paquete IP?

A) Tiempo máximo que la dirección IP es válida antes de expirar  
B) Número máximo de saltos que puede realizar un paquete antes de ser descartado  
C) Tiempo de espera para recibir confirmación del destino  
D) Duración máxima de una sesión TCP

---

### Pregunta 12
En el proceso DORA de DHCP, ¿qué significa la letra "R"?

A) Request (Solicitud)  
B) Release (Liberación)  
C) Renewal (Renovación)  
D) Reply (Respuesta)

---

### Pregunta 13
¿Qué mecanismo permite que múltiples dispositivos de una red privada compartan una única dirección IP pública hacia Internet?

A) NAT (Network Address Translation)  
B) DNS Round Robin  
C) Load Balancing  
D) VLAN Tagging

---

### Pregunta 14
Al programar un socket TCP en Java, ¿qué excepción se lanza cuando el puerto objetivo está cerrado o rechazando activamente la conexión?

A) SocketTimeoutException  
B) ConnectException  
C) UnknownHostException  
D) MalformedURLException

---

### Pregunta 15
¿Qué tipo de firewall analiza el estado activo de las conexiones para permitir solo tráfico que sea respuesta a solicitudes legítimas iniciadas desde dentro de la red?

A) Firewall de filtrado por paquetes (Packet Filtering)  
B) Firewall Stateful Inspection  
C) Proxy Application Layer  
D) Firewall de estado estático

---

## 2. CASO PRÁCTICO DE DEBUGGING #1: Configuración TCP/IP y DNS en Aplicación Multiplataforma

### Escenario Profesional
Eres desarrollador senior en una empresa que crea aplicaciones multiplataforma para gestión logística. La aplicación debe conectarse a un servidor de bases de datos remoto para sincronizar inventarios. El equipo ha reportado fallos intermitentes de conexión en la versión móvil de la aplicación (Android/iOS).

### Código Fuente con Errores (Java)
```java
package com.logistica.red;

import java.net.*;
import java.io.IOException;

/**
 * Clase de configuración de red para la aplicación de logística.
 * Contiene errores lógicos y de compilación que impiden la conectividad correcta.
 */
public class ConfiguracionRedLogistica {

    private String servidorIP;
    private int puertoBaseDatos;
    
    // Constructor de la clase con errores
    public ConfiguracionRedLogistica(String ip) {
        this.servidorIP = ip;
        this.puertoBaseDatos = 3306;
        
        // Error 1: Validación incorrecta de IP (Sin manejo de excepciones en constructor)
        validarDireccionIP(ip);
    }

    // Método con errores lógicos
    public void validarDireccionIP(String direccion) {
        try {
            InetAddress addr = InetAddress.getByName(direccion);
            
            if (addr.isLoopbackAddress()) {
                System.out.println("Error: Dirección de loopback detectada");
                return;
            }
            
            // Error 2: No se verifica si la IP es reachable realmente
            
        } catch (UnknownHostException e) {
            System.out.println("Host no encontrado");
            // Error 3: La excepción no se maneja correctamente para reintentos
        }
    }

    // Método con errores de sintaxis y lógica
    public void conectarServidor() throws IOException {
        Socket socket = new Socket();
        
        // Error 4: Falta especificar el puerto en la conexión (Usa default)
        InetAddress addr = InetAddress.getByName(this.servidorIP);
        
        // Error 5: Timeout configurado de forma incorrecta (valor nulo)
        socket.connect(addr, null); 
        
        System.out.println("Conexión establecida");
    }

    // Método DNS con errores
    public String resolverDNS(String dominio) {
        try {
            InetAddress[] addresses = InetAddress.getAllByName(dominio);
            
            // Error 6: Solo devuelve la primera IP encontrada sin verificar cual es correcta
            
            return addresses[0].getHostAddress();
        } catch (Exception e) {
            // Error 7: No se diferencia entre error de DNS y error de red
            System.out.println("Error genérico");
            return null;
        }
    }

    public static void main(String[] args) throws IOException {
        ConfiguracionRedLogistica config = new ConfiguracionRedLogistica("192.168.1.100");
        
        // Error 8: No se verifica si la resolución DNS fue exitosa antes de conectar
        
        String ipResuelta = config.resolverDNS("servidor-logistica.empresarial.com");
        System.out.println("IP Resuelta: " + ipResuelta);
        
        config.conectarServidor();
    }
}
```

### Tarea del Alumno
1. Identifica y documenta **al menos 5 errores** en el código (lógicos, de compilación o de seguridad).
2. Proporciona la solución corregida para cada error encontrado.
3. Explica por qué el error afecta a la conectividad multiplataforma.

---

## 3. CASO PRÁCTICO DE DEBUGGING #2: Escaneo de Puertos y Seguridad en Aplicación Web

### Escenario Profesional
La empresa ha desarrollado una API REST para gestión de inventarios que se ejecuta en servidores Linux. El equipo de seguridad ha reportado vulnerabilidades potenciales relacionadas con puertos abiertos innecesariamente. Debes crear una herramienta de auditoría de puertos y validar la configuración de seguridad SSL/TLS.

### Código Fuente con Errores (Python)
```python
#!/usr/bin/env python3
"""
Herramienta de escaneo de puertos para auditoría de seguridad.
Contiene errores críticos en gestión de recursos y seguridad.
"""

import socket
import ssl
from urllib.request import urlopen, Request

class EscanerPuertos:
    
    def __init__(self, host, timeout=2000):
        self.host = host
        # Error 1: Timeout configurado en milisegundos pero socket espera segundos
        
    def escanear_puerto(self, puerto):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Error 2: No se establece timeout antes de conectar
            
            result = sock.connect_ex((self.host, puerto))
            
            if result == 0:
                print(f"PUERTO {puerto}: ABIERTO")
                return True
            else:
                print(f"PUERTO {puerto}: CERRADO")
                return False
                
        except Exception as e:
            # Error 3: Se captura toda la excepción sin diferenciar tipos
            
            print(f"Error: {e}")
            
        finally:
            pass  # Error 4: El socket no se cierra correctamente en todos los casos

    def verificar_ssl(self, url):
        try:
            req = Request(url)
            
            # Error 5: No se valida el certificado SSL explícitamente
            
            response = urlopen(req, timeout=10)
            
            if 'https' in url.lower():
                print("Protocolo HTTPS detectado")
                
            return True
            
        except Exception as e:
            # Error 6: No se diferencia entre error de red y error de certificado
            
            print(f"Error SSL/Red: {e}")
            return False

    def cerrar_conexion(self):
        pass  # Error 7: Método vacío sin implementación real


# Código principal con errores
def main():
    scanner = EscanerPuertos("192.168.50.10")
    
    puertos_a_verificar = [80, 443, 22, 3306]
    
    for puerto in puertos_a_verificar:
        # Error 8: No se manejan excepciones en el bucle principal
        
        scanner.escanear_puerto(puerto)
        
    # Error 9: No se verifica si la conexión HTTPS usa TLS 1.2 o superior
    
    verificar_ssl("http://servidor-api.empresarial.com")
    
    scanner.cerrar_conexion()

if __name__ == "__main__":
    main()
```

### Tarea del Alumno
1. Identifica y documenta **al menos 6 errores** en el código (lógicos, de seguridad o de gestión de recursos).
2. Proporciona la solución corregida para cada error encontrado.
3. Explica cómo los errores afectan a la seguridad de la aplicación multiplataforma.

---

## 4. SOLUCIONARIO DETALLADO PARA EL DOCENTE Y ESTUDIANTE

### PARTE A: EXAMEN TIPO TEST - SOLUCIONES Y JUSTIFICACIÓN TÉCNICA PROFUNDA

En esta sección, no solo indicamos la respuesta correcta, sino que desglosamos la arquitectura de red subyacente para garantizar que el estudiante comprenda los conceptos teóricos y prácticos detrás de cada opción.

| # | Respuesta Correcta | Justificación Técnica Detallada (Estudio Expandido) |
|---|-------------------|----------------------------------|
| **1** | **C) Capa de Red** | **Justificación:** La respuesta correcta es la **Capa de Red**. En el modelo TCP/IP, esta capa (equivalente a la Capa 3 del modelo OSI) se encarga fundamentalmente del direccionamiento lógico mediante direcciones IP y del enrutamiento. Su función principal es determinar la mejor ruta para enviar paquetes entre redes distintas (LAN a WAN). Los routers son los dispositivos que operan nativamente en esta capa, examinando el encabezado IP de cada paquete para decidir a qué interfaz de salida debe ser reenviado.<br><br>**Análisis de Distractores:**<br>• **A) Capa de Aplicación:** Opera en la parte superior (Capas 5-7 del OSI). Gestiona los datos que la aplicación necesita (HTTP, FTP), pero no se encarga del transporte físico ni lógico entre redes.<br>• **B) Capa de Transporte:** Se enfoca en la comunicación extremo a extremo (puertos TCP/UDP). Aunque asegura la entrega o velocidad, no decide cómo cruzar una red intermedia.<br>• **D) Capa de Acceso a la Red:** Es la interfaz física y lógica con el medio (Ethernet, WiFi). Gestiona direcciones MAC, pero no enrutamiento IP entre redes. |
| **2** | **B) Puerta de enlace predeterminada** | **Justificación:** La respuesta correcta es la **Puerta de Enlace Predeterminada**. Cuando un dispositivo está configurado con una IP estática (ej. 192.168.1.50), sabe que pertenece a su red local. Sin embargo, para comunicarse con una IP externa (como `google.com` o un servidor en la nube), el sistema operativo necesita saber dónde enviar los paquetes que no son locales. La puerta de enlace es esa dirección IP (generalmente la del router) que actúa como salida hacia otras redes.<br><br>**Análisis de Distractores:**<br>• **A) Dirección MAC:** Es una identidad física única, pero solo funciona dentro del mismo dominio de broadcast local. No sirve para salir de la red.<br>• **C) Protocolo DHCP:** Si configuramos IP estática, DHCP no debe estar activo en ese adaptador; además, DHCP es dinámico, no garantiza acceso externo sin gateway.<br>• **D) Dirección Multicast:** Se usa para un grupo específico de receptores dentro de la misma red local, no para comunicación general hacia el exterior. |
| **3** | **C) DNS** | **Justificación:** La respuesta correcta es **DNS (Domain Name System)**. Los humanos memorizamos nombres (ej. `www.google.com`), pero las máquinas necesitan direcciones numéricas (IP). El protocolo DNS actúa como una base de datos distribuida que traduce esos nombres legibles a direcciones IP, permitiendo la resolución automática.<br><br>**Análisis de Distractores:**<br>• **A) ARP:** Se encarga de traducir una dirección IP *local* conocida a su correspondiente Dirección MAC. No resuelve nombres de dominio globales.<br>• **B) ICMP:** Es un protocolo de control y diagnóstico (como ping), no de resolución de nombres.<br>• **D) NAT:** Traduce direcciones privadas a públicas, pero no traduce nombres de texto a IP numérica. |
| **4** | **D) WPA3** | **Justificación:** La respuesta correcta es **WPA3**. Es el estándar más reciente (IEEE 802.11i actualizado) diseñado para proteger las redes inalámbricas contra ataques modernos. Introduce características clave como la protección individualizada de datos incluso en redes abiertas y una resistencia mejorada frente a ataques de fuerza bruta mediante el protocolo SAE (Simultaneous Authentication of Equals).<br><br>**Análisis de Distractores:**<br>• **A) WEP:** Es obsoleto, inseguro y se puede romper en minutos. Nunca debe usarse.<br>• **B) WPA / C) WPA2:** Aunque más seguros que WEP, ambos tienen vulnerabilidades conocidas (como KRACK en WPA2). WPA3 es el estándar actual recomendado para entornos de alto seguridad. |
| **5** | **C) Switch** | **Justificación:** La respuesta correcta es **Switch**. Los switches operan en la Capa 2 (Enlace de Datos) y utilizan tablas de conmutación CAM (Content Addressable Memory) que mapean direcciones MAC a puertos físicos. Esto permite enviar el tráfico directamente al destino correcto, optimizando el ancho de banda.<br><br>**Análisis de Distractores:**<br>• **A) Router:** Opera en Capa 3 (Red). Aunque puede hacer conmutación, su función principal es el enrutamiento entre redes diferentes.<br>• **B) Hub:** Es un dispositivo antiguo que opera en física. Difunde datos a *todos* los puertos, creando colisiones y problemas de seguridad.<br>• **D) Repetidor:** Solo amplifica la señal eléctrica para extender la distancia, no gestiona direcciones ni tráfico inteligente. |
| **6** | **C) Baja sobrecarga y transmisión sin confirmación** | **Justificación:** La respuesta correcta es **Baja sobrecarga**. UDP (User Datagram Protocol) es un protocolo "connectionless" (sin conexión). No realiza el "handshake" de TCP ni envía acuses de recibo por cada paquete. Esto reduce significativamente la latencia y el tráfico de red, lo cual es vital para streaming en tiempo real donde es mejor perder un cuadro de video que esperar a retransmitir uno.<br><br>**Análisis de Distractores:**<br>• **A) Garantía de entrega:** Esta es una función de TCP, no UDP.<br>• **B) Establecimiento de conexión:** TCP requiere tres vías (SYN-ACK-SYN), UDP no.<br>• **D) Control de flujo:** TCP gestiona el control de flujo para evitar saturar al receptor; UDP asume que la red o el receptor pueden manejar el tráfico sin regulación estricta. |
| **7** | **A) 0 - 1023** | **Justificación:** La respuesta correcta es **0 - 1023**. Estos puertos se denominan "Well-Known Ports" (Puertos Bien Conocidos). Están reservados por la IANA para servicios estándar del sistema operativo y aplicaciones comunes. Para usar estos puertos en sistemas operativos modernos, generalmente se requieren privilegios de administrador o root.<br><br>**Análisis de Distractores:**<br>• **B) 1024 - 49151:** Se llaman "Registered Ports", usados por aplicaciones de usuario registradas (ej. servidores web no estándar).<br>• **C) 49152 - 65535:** Puertos dinámicos o privados, asignados temporalmente a procesos cliente.<br>• **D) 80 - 443:** Son rangos específicos dentro del rango bien conocido (HTTP y HTTPS), no el rango completo. |
| **8** | **B) Router o Switch Layer 3** | **Justificación:** La respuesta correcta es **Router o Switch Layer 3**. Las VLANs crean dominios de broadcast aislados lógicamente. Para que un dispositivo en la VLAN 10 pueda hablar con uno en la VLAN 20, se requiere routing (Capa 3). Un switch Layer 2 no tiene capacidad para reenviar paquetes entre subredes distintas.<br><br>**Análisis de Distractores:**<br>• **A) Switch Layer 2:** Solo entiende direcciones MAC y opera dentro del mismo dominio de broadcast/VLAN.<br>• **C) Hub Ethernet:** No conoce VLANs ni IP, solo transmite señales eléctricas.<br>• **D) Repetidor Wi-Fi:** Amplifica señal inalámbrica, no realiza routing lógico entre segmentos. |
| **9** | **B) Ping** | **Justificación:** La respuesta correcta es **Ping**. El comando `ping` utiliza el protocolo ICMP (Internet Control Message Protocol) específicamente los mensajes de tipo "Echo Request" y "Echo Reply". Es la herramienta más básica para verificar si un nodo en la red IP está activo y responde a solicitudes.<br><br>**Análisis de Distractores:**<br>• **A) Tracert/Traceroute:** También usa ICMP, pero su función es mapear los saltos (rutas) que toma el paquete hasta el destino, no solo verificar si existe.<br>• **C) Nslookup:** Se utiliza para consultar servidores DNS y obtener información de nombres de dominio, no para probar conectividad básica IP.<br>• **D) Netstat:** Muestra estadísticas de conexiones activas y puertos en uso localmente. |
| **10** | **A) Cifrado asimétrico y simétrico combinado** | **Justificación:** La respuesta correcta es **Cifrado Híbrido**. SSH utiliza un esquema híbrido para equilibrar seguridad y rendimiento. Inicialmente usa criptografía asimétrica (clave pública/privada, ej. RSA/Diffie-Hellman) para autenticar al servidor y negociar una clave de sesión secreta. Una vez acordada esta clave, cambia a cifrado simétrico (ej. AES) para el resto de la sesión porque es mucho más rápido para transmitir datos.<br><br>**Análisis de Distractores:**<br>• **B) Solo simétrico:** Sería inseguro si las claves se compartieran por internet sin autenticación previa.<br>• **C) Hashing MD5:** Es para integridad, no para cifrado de datos en tránsito. Además, MD5 es obsoleto e inseguro.<br>• **D) Cifrado WEP:** Es para redes Wi-Fi antiguas y es vulnerable. |
| **11** | **B) Número máximo de saltos** | **Justificación:** La respuesta correcta es el **Número máximo de saltos**. El campo TTL (Time To Live) en la cabecera IP es un contador que se decrementa en 1 por cada router (salto) que procesa el paquete. Cuando llega a 0, el router descarta el paquete y envía una notificación ICMP "TTL Exceeded". Esto evita bucles infinitos de paquetes si hay errores de enrutamiento.<br><br>**Análisis de Distractores:**<br>• **A) Tiempo máximo IP válida:** La dirección IP no tiene fecha de caducidad por sí misma (aunque el DHCP tenga lease).<br>• **C) Tiempo de espera confirmación:** Esto se refiere a timeouts de socket, no al campo TTL.<br>• **D) Duración sesión TCP:** Se gestiona mediante keep-alive o tiempos de fin de conexión, no por TTL. |
| **12** | **A) Request (Solicitud)** | **Justificación:** La respuesta correcta es **Request**. El proceso DORA describe cómo un cliente obtiene una IP:<br>1. **D**iscover: Cliente busca servidor DHCP.<br>2. **O**ffer: Servidor ofrece IP.<br>3. **R**equest: Cliente solicita formalmente esa IP.<br>4. **A**cknowledge: Servidor confirma la asignación.<br><br>**Análisis de Distractores:**<br>• **B) Release / C) Renewal:** Son comandos DHCP válidos (liberar o renovar), pero no son parte del proceso inicial DORA.<br>• **D) Reply:** No es un término estándar en el acrónimo DORA, aunque técnicamente el servidor "responde" a la solicitud. |
| **13** | **A) NAT (Network Address Translation)** | **Justificación:** La respuesta correcta es **NAT**. El mecanismo de traducción de direcciones de red permite que múltiples dispositivos con IPs privadas internas (ej. 192.168.x.x) compartan una única IP pública externa al acceder a Internet. El router mantiene una tabla de mapeo para saber qué tráfico interno corresponde a cada conexión.<br><br>**Análisis de Distractores:**<br>• **B) DNS Round Robin:** Es una técnica de balanceo de carga que asigna diferentes IPs de un mismo nombre, no traduce direcciones privadas.<br>• **C) Load Balancing:** Distribuye tráfico entre servidores para evitar sobrecarga, pero no oculta las IPs internas detrás de una pública como NAT.<br>• **D) VLAN Tagging:** Se usa para segmentar redes lógicas (802.1Q), no para traducción de direcciones hacia Internet. |
| **14** | **B) ConnectException** | **Justificación:** La respuesta correcta es **ConnectException**. En la API de Sockets de Java, esta excepción específica se lanza cuando el servidor rechaza explícitamente la conexión (puerto cerrado o servicio no escuchando). Indica que el destino está activo pero no acepta conexiones en ese puerto.<br><br>**Análisis de Distractores:**<br>• **A) SocketTimeoutException:** Se lanza si la conexión tarda demasiado en establecerse, no necesariamente porque esté cerrada.<br>• **C) UnknownHostException:** Indica que el nombre del host (DNS) no se pudo resolver a una IP.<br>• **D) MalformedURLException:** Ocurre al intentar crear un objeto URL con una sintaxis incorrecta. |
| **15** | **B) Firewall Stateful Inspection** | **Justificación:** La respuesta correcta es **Firewall Stateful Inspection**. Este tipo de firewall no solo filtra por puertos, sino que mantiene el estado de cada conexión (tabla de estados). Permite tráfico entrante solo si pertenece a una sesión iniciada legítimamente desde dentro. Esto bloquea automáticamente intentos de conexión no solicitados desde fuera.<br><br>**Análisis de Distractores:**<br>• **A) Packet Filtering:** Filtra solo por cabeceras (IP/Puerto) sin recordar el estado. Es menos seguro y más propenso a ataques de spoofing.<br>• **C) Proxy Application Layer:** Opera en la capa 7. Aunque es muy seguro, es más lento y no es estrictamente lo que define "Stateful" en la capa de red/transporte.<br>• **D) Firewall estático:** No existe como término técnico estándar para diferenciar de stateful; suele referirse al filtrado básico por paquetes. |

---

### PARTE B: CASO PRÁCTICO DE DEBUGGING #1 - SOLUCIÓN DETALLADA Y RAZONAMIENTO LÓGICO

Este caso práctico simula un escenario real donde una aplicación Java falla en la conectividad de red debido a errores comunes de programación y gestión de excepciones. A continuación, se detalla el análisis paso a paso y la corrección técnica.

#### Error 1: Validación incorrecta de IP en Constructor (Manejo de Excepciones)
**Análisis del Problema:** En el código original, `validarDireccionIP(ip)` se llama dentro del constructor sin un bloque `try-catch`. Si `InetAddress.getByName` falla (ej. string inválido), el constructor lanza una excepción no controlada (`UnknownHostException` o `RuntimeException`), impidiendo que la instancia de la clase se cree y provocando un fallo en cascada de la aplicación principal.
**Razonamiento Técnico:** En Java, los constructores no deben dejar recursos en estado inconsistente ni propagar excepciones de validación de entrada sin manejarlas adecuadamente para evitar fallos silenciosos o cierres abruptos del programa.
**Solución Corregida:**
```java
public ConfiguracionRedLogistica(String ip) {
    this.servidorIP = ip;
    this.puertoBaseDatos = 3306;
    
    try {
        validarDireccionIP(ip); // Llamada protegida ahora
    } catch (UnknownHostException | IOException e) {
        System.err.println("Error de configuración: IP inválida o inalcanzable");
        throw new IllegalArgumentException("La dirección IP proporcionada es inválida", e);
    }
}
```

#### Error 2: Falta verificación de Reachability (Conectividad Real)
**Análisis del Problema:** `InetAddress.getByName()` solo resuelve el nombre DNS o valida la sintaxis de la IP. No garantiza que el host esté encendido, tenga conexión a red o sea accesible desde tu máquina local. Esto causa fallos intermitentes cuando la aplicación asume que "existe" porque tiene una IP válida.
**Razonamiento Técnico:** En desarrollo multiplataforma (Android/iOS), las redes son inestables. La validación lógica debe incluir un chequeo de conectividad antes de intentar establecer sockets pesados.
**Solución Corregida:**
```java
public void validarDireccionIP(String direccion) throws IOException {
    InetAddress addr = InetAddress.getByName(direccion);
    
    if (addr.isLoopbackAddress()) {
        throw new SecurityException("Dirección de loopback detectada en entorno remoto");
    }
    
    // Validación crítica: ¿Puede el host responder a un ping?
    if (!addr.isReachable(2000)) {  // Timeout de 2 segundos para no bloquear UI
        throw new IOException("Host no reachable en la red actual (DNS ok pero Host offline)");
    }
}
```

#### Error 3: Gestión Inadecuada de Excepciones para Reintentos
**Análisis del Problema:** El código original solo imprime un mensaje (`System.out.println`). En una aplicación multiplataforma, la capa de presentación (UI) necesita saber que falló para mostrar un diálogo o reintentar automáticamente. Lanzar el error permite propagarlo a capas superiores (ej. ViewModel/MVVM).
**Razonamiento Técnico:** El patrón "Fail Fast" es útil, pero en redes se suele preferir "Retry Logic". La excepción debe ser capturada y tratada adecuadamente para permitir estrategias de recuperación.
**Solución Corregida:**
```java
catch (UnknownHostException e) {
    System.out.println("Host no encontrado: " + direccion);
    // Lanzar una excepción personalizada o específica para que el cliente decida cómo actuar
    throw new ConnectivityException("DNS Resolution Failed", e); 
}
// Nota: Se asume la existencia de la clase ConnectivityException extendiendo IOException
```

#### Error 4 y 5: Conexión sin Puerto Específico y Timeout Incorrecto
**Análisis del Problema:** `socket.connect(addr)` usa el puerto por defecto (80) en lugar del configurado. Además, pasar `null` como timeout a `connect()` lanza una `NullPointerException` o comportamiento indefinido según la versión de Java. El timeout debe ser un entero positivo en milisegundos.
**Razonamiento Técnico:** Para bases de datos MySQL (puerto 3306), conectarse al puerto por defecto resultará en "Connection Refused". Además, sin timeout, el hilo podría bloquearse indefinidamente si la red es lenta o está caída, congelando la interfaz del usuario.
**Solución Corregida:**
```java
public void conectarServidor() throws IOException {
    Socket socket = new Socket();
    
    // Construcción explícita de la dirección con puerto correcto
    InetAddress addr = InetAddress.getByName(this.servidorIP);
    InetSocketAddress address = new InetSocketAddress(addr, this.puertoBaseDatos);
    
    // Timeout configurado correctamente (5 segundos) para evitar bloqueos infinitos
    socket.connect(address, 5000); 
    
    System.out.println("Conexión establecida correctamente en puerto " + this.puertoBaseDatos);
}
```

#### Error 6 y 7: Resolución DNS Insegura y Manejo de Excepciones Genéricas
**Análisis del Problema:** `getAllByName()` puede devolver múltiples IPs (Round Robin). Devolver la primera sin verificar si es reachable desperdicia recursos intentando conectar a un nodo caído. Además, capturar `Exception` genérico oculta errores específicos que son vitales para el debugging (ej. DNS timeout vs Network unreachable).
**Razonamiento Técnico:** En entornos de alta disponibilidad (Load Balanced), la aplicación debe elegir una IP activa. El manejo de excepciones debe ser granular para saber si el problema es del proveedor DNS o de la red local.
**Solución Corregida:**
```java
public String resolverDNS(String dominio) {
    try {
        InetAddress[] addresses = InetAddress.getAllByName(dominio);
        
        // Búsqueda iterativa: probar cada IP hasta encontrar una reachable
        for (InetAddress addr : addresses) {
            if (addr.isReachable(1000)) {  // Timeout de 1 segundo por intento
                return addr.getHostAddress();
            }
        }
        
        throw new DNSResolutionException("Ninguna IP reachable encontrada tras revisar todas las respuestas DNS");
        
    } catch (UnknownHostException e) {
        System.err.println("Error crítico en resolución DNS: " + e.getMessage());
        throw new NetworkFailureException("DNS Resolution Failed", e); // Excepción específica
    } catch (IOException e) {
        System.err.println("Error de red durante la validación de IPs DNS: " + e.getMessage());
        throw e;
    }
}
```

#### Error 8: Falta Validación Previa de Conexión
**Análisis del Problema:** El `main` llama a `conectarServidor()` asumiendo que `resolverDNS` devolvió algo válido. Si devuelve `null`, el código lanza un NPE o intenta conectar con IP vacía.
**Razonamiento Técnico:** La seguridad y robustez en programación dictan "Validate before Act". Nunca ejecutar operaciones de red sin verificar primero que los parámetros son válidos.
**Solución Corregida:**
```java
public static void main(String[] args) {
    ConfiguracionRedLogistica config = new ConfiguracionRedLogistica("192.168.1.100");
    
    try {
        String ipResuelta = config.resolverDNS("servidor-logistica.empresarial.com");
        
        // Validación crítica: ¿Obtuvimos una IP válida?
        if (ipResuelta == null || ipResuelta.isEmpty()) {
            System.err.println("Fallo en resolución DNS: No se obtuvo IP válida. Abortando conexión.");
            return; 
        }
        
    } catch (Exception e) {
        System.err.println("Error crítico pre-conexión: " + e.getMessage());
        return; // Salir del main para evitar excepciones no controladas en UI
    }
    
    try {
        config.conectarServidor();  // Ahora seguro, IP validada y puerto correcto
        System.out.println("Conexión exitosa");
        
    } catch (IOException e) {
        System.err.println("Error de conexión: " + e.getMessage());
    }
}
```

---

### PARTE C: CASO PRÁCTICO DE DEBUGGING #2 - SOLUCIÓN DETALLADA Y RAZONAMIENTO LÓGICO

Este caso se centra en Python y la seguridad. Los errores aquí no son solo de funcionalidad, sino de gestión de recursos (fugas de memoria) y vulnerabilidades de seguridad (certificados SSL).

#### Error 1: Unidades de Tiempo Incorrectas (Timeout)
**Análisis del Problema:** `timeout=2000` en el constructor sugiere milisegundos. Sin embargo, la API de sockets Python (`socket.settimeout`) acepta segundos como flotante. Esto causaría un timeout inmediato de 0.002 segundos o error si no se convierte explícitamente.
**Razonamiento Técnico:** La consistencia en las unidades de tiempo es crítica para evitar "Race Conditions" programáticas donde el socket cierra antes de enviar la solicitud SYN.
**Solución Corregida:**
```python
def __init__(self, host, timeout=2.0):  # Convertir explícitamente a segundos (float)
    self.host = host
    self.timeout = float(timeout) if isinstance(timeout, int) else timeout
```

#### Error 2: Falta de Timeout en el Socket
**Análisis del Problema:** Crear un socket y conectar sin establecer un límite de tiempo (`settimeout`) hará que el programa se bloquee indefinidamente si el firewall bloquea el puerto (DROP vs REJECT) o si la red está caída. Esto consume recursos del sistema operativo.
**Razonamiento Técnico:** En seguridad, "Timeouts" limitan la ventana de oportunidad para DoS (Denial of Service). Nunca debe haber una conexión sin límite temporal en herramientas de auditoría.
**Solución Corregida:**
```python
def escanear_puerto(self, puerto):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Establecer timeout ANTES de conectar para evitar bloqueos del hilo
        sock.settimeout(self.timeout) 
        
        result = sock.connect_ex((self.host, puerto))
        
        if result == 0:
            print(f"PUERTO {puerto}: ABIERTO")
            return True
        else:
            print(f"PUERTO {puerto}: CERRADO (código: {result})")
            return False
            
    except socket.timeout:
        # Manejo específico de timeout para diferenciarlo de errores de red
        print(f"PUERTO {puerto}: TIEMPO DE ESPERA AGOTADO (FIREWALL PROBABLE)")
        return None
        
    finally:
        sock.close()  # Asegurar cierre en todos los casos, incluido error
```

#### Error 3 y 6: Captura Genérica de Excepciones vs Diferenciación
**Análisis del Problema:** `except Exception` es peligroso porque captura errores no relacionados (ej. errores de lógica interna) y oculta la causa raíz. Además, en SSL, hay una diferencia crítica entre un error de red (`ConnectionRefused`) y un error de certificado (`SSLCertVerificationError`).
**Razonamiento Técnico:** El debugging profesional requiere saber exactamente *qué* falló para no tener que adivinar. En seguridad, confundir un "Certificate Error" con un "Network Timeout" podría llevar a deshabilitar la validación SSL por accidente.
**Solución Corregida:**
```python
    except socket.timeout:
        print(f"Error de red en puerto {puerto}: Tiempo agotado")
        return None
        
    except socket.error as e:
        # Captura específica para errores de socket (TCP/UDP)
        print(f"Error de red en puerto {puerto}: {e}")
        return None

def verificar_ssl(self, url):
    try:
        context = ssl.create_default_context()  # Contexto seguro por defecto
        
        req = Request(url)
        opener = build_opener(HTTPSHandler(context=context))
        
        response = opener.open(req, timeout=10)
        
        if 'https' in url.lower():
            print("Protocolo HTTPS detectado")
            cert_info = response.getheader('SSL-Protocol')
            if cert_info:
                print(f"Versión TLS/SSL: {cert_info}")
                
        return True
        
    except ssl.SSLCertVerificationError as e:  # Captura específica de seguridad
        print(f"ERROR CRÍTICO DE CERTIFICADO SSL: El certificado no es válido. {e}")
        return False
        
    except socket.timeout:
         print("Tiempo agotado en conexión HTTPS")
         return False
```

#### Error 4 y 7: Gestión de Recursos (Cierre de Sockets)
**Análisis del Problema:** El bloque `finally` vacío (`pass`) y el método `cerrar_conexion` vacío son errores graves. Los sockets consumen recursos del sistema (descriptores de archivo). Si no se cierran, la máquina puede agotar los puertos disponibles tras un escaneo masivo ("Port Exhaustion").
**Razonamiento Técnico:** En Python, el uso del contexto `with` es preferible para auto-gestión de recursos. Si no se usa `with`, el cierre debe ser explícito en todos los caminos de ejecución (éxito o error).
**Solución Corregida:**
```python
    def cerrar_conexion(self):
        """Cerrar todos los sockets abiertos y limpiar recursos"""
        # Si hubiéramos guardado referencias a sockets activos, se cerrarían aquí.
        print("Limpieza de recursos finalizada")

# Mejor práctica en escanear_puerto: Usar 'with' para gestión automática del socket
def escanear_puerto(self, puerto):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(self.timeout)
        result = sock.connect_ex((self.host, puerto))
        # El socket se cierra automáticamente al salir del bloque 'with'
```

#### Error 8 y 9: Manejo de Excepciones en Bucle y Validación TLS
**Análisis del Problema:** Si un escaneo falla en el bucle principal sin `try-catch`, la herramienta se detiene prematuramente. Además, detectar "HTTPS" no garantiza seguridad moderna; muchas webs usan TLS 1.0 obsoleto. Se debe verificar la versión del protocolo.
**Razonamiento Técnico:** Una auditoría de seguridad debe ser robusta (no parar ante un error) y precisa (verificar versiones de protocolos criptográficos).
**Solución Corregida:**
```python
def main():
    try:
        scanner = EscanerPuertos("192.168.50.10")
        
        puertos_a_verificar = [80, 443, 22, 3306]
        
        for puerto in puertos_a_verificar:
            try:
                resultado = scanner.escanear_puerto(puerto)
                print(f"Resultado puerto {puerto}: {resultado}")
                
            except Exception as e:
                # Manejo de errores por puerto para que el escaneo continúe
                print(f"Error inesperado en puerto {puerto}, continuando...")
        
        verificar_ssl("https://servidor-api.empresarial.com")
        
    finally:
        scanner.cerrar_conexion()  # Asegurar cierre en todos los casos

if __name__ == "__main__":
    main()
```

---

## RÚBRICA DE EVALUACIÓN DEL ALUMNO (ACTUALIZADA)

| Criterio | Puntuación Máxima | Indicadores de Desempeño Detallados |
|----------|------------------|--------------------------------------|
| **Test (15 preguntas)** | 10 puntos | Respuestas correctas según solucionario. Cada pregunta vale 0,67 puntos. Se penaliza la omisión de justificación oral si se solicita defensa del examen. |
| **Caso Práctico #1** | 20 puntos | **Identificación (8 pts):** Detectar los 5+ errores clave. <br> **Solución (8 pts):** Código funcional que compila y gestiona excepciones correctamente. <br> **Explicación Técnica (4 pts):** Justificar por qué el error afecta a la red/multiplataforma. |
| **Caso Práctico #2** | 25 puntos | **Identificación de Errores (10 pts):** Detectar errores de seguridad y gestión de recursos. <br> **Solución Corregida (10 pts):** Implementación con manejo de SSL/TLS y cierres de sockets. <br> **Análisis de Seguridad (5 pts):** Explicar cómo la corrección mejora el perfil de seguridad de la API. |
| **Documentación** | 10 puntos | Código comentado, estructura clara, documentación técnica completa en Markdown. |
| **Calidad del Código** | 20 puntos | Sintaxis correcta (Java/Python), manejo de excepciones adecuado (`try-catch` granular), buenas prácticas (naming conventions, uso de `with`). |
| **Presentación** | 15 puntos | Formato Markdown correcto, tabla de contenido, orden lógico de secciones, ortografía impecable. |

---

## NOTAS PARA EL DOCENTE Y RECOMENDACIONES PEDAGÓGICAS

### Criterios de Aprobación del RA5
- **Nota mínima aprobatoria:** 5/10 en el examen tipo test (se permite recuperar si se falla la práctica).
- **Caso práctico obligatorio:** Al menos 4 errores identificados y corregidos correctamente por caso para obtener la máxima puntuación en esa sección.
- **Entregable final:** Código funcional que compile sin errores (`javac`/`python3`) y documentación completa del solucionario.

### Recomendaciones Pedagógicas Expandidas
1.  **Antes del examen (Repaso Teórico):** No basta con memorizar. El docente debe pedir al alumno que dibuje el modelo OSI explicando qué pasa en cada capa cuando se ejecuta un `ping`. Esto valida la comprensión profunda de las preguntas del test (ej. Pregunta 9, ICMP).
2.  **Durante la práctica:** Permitir 3 horas para completar ambos casos prácticos. Fomentar el uso de IDEs con autocompletado y debuggers para que vean en tiempo real dónde falla el código.
3.  **Evaluación Oral Complementaria (Defensa):** Preguntar al alumno: *"¿Por qué es peligroso capturar `Exception` genérico en Python?"* o *"¿Qué sucede si omitimos el TTL en un paquete IP?"*. Esto valida que no ha copiado el solucionario sin entenderlo.
4.  **Enfoque de Seguridad:** Enfatizar que la seguridad (RA5, Criterio h) es transversal. Un error de timeout puede ser un vector de ataque DoS; un SSL mal validado puede exponer datos.

### Observaciones Técnicas Importantes para el Docente
- Los casos prácticos simulan escenarios reales del currículo DAM (Desarrollo de Aplicaciones Multiplataforma). Se recomienda usar entornos virtualizados (Docker/VM) si es posible para que los alumnos vean efectos reales, aunque el código puede correr en modo simulado.
- Se enfatiza la seguridad en redes como criterio transversal (CE h). Asegúrese de que el alumno entienda por qué `ssl.SSLCertVerificationError` es una excepción crítica y no debe ser ignorada (`pass`).
- La automatización mediante código es clave para el perfil profesional moderno (NetDevOps). El solucionario debe usarse como guía para enseñar a escribir scripts robustos, no solo para aprobar.

---
*Documento elaborado bajo estricta adherencia a la normativa curricular del módulo Sistemas Informáticos (FP DAM) y alineado con las competencias profesionales exigidas por el sector tecnológico.*

**Versión:** 2.1  
**Fecha de última actualización:** 2024-12-15
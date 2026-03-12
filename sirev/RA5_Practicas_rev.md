

# GUÍA DE PRÁCTICAS Y LABORATORIOS: RA5 - Interconecta sistemas en red configurando dispositivos y protocolos
## Módulo Profesional: Sistemas Informáticos | Ciclo Formativo: DAM (Desarrollo de Aplicaciones Multiplataforma)

---

### 1. INTRODUCCIÓN Y OBJETIVOS PEDAGÓGICOS

Bienvenido al laboratorio virtual del RA5. Como Administrador de Sistemas, este diseño no busca que escribas programas para gestionar la red, sino que **domines la infraestructura** mediante configuraciones nativas, protocolos establecidos y herramientas de sistema operativos. Esto cumple con el perfil profesional necesario: un desarrollador debe comprender profundamente cómo se comunican los sistemas antes de intentar interactuar con ellos a nivel de aplicación.

**Objetivo General:**
Implementar soluciones de configuración, monitorización y seguridad de redes (LAN/WAN) utilizando las herramientas nativas del sistema operativo, sin dependencia de código fuente externo. Cubre los Criterios de Evaluación (CE) a-h del RA5 mediante la gestión directa de recursos.

**Cobertura de Criterios de Evaluación (RA5):**
*   **a)** Configuración TCP/IP (Manual y Automática).
*   **b) & d)** Redes LAN Cableadas y Dispositivos (Configuración física y lógica).
*   **c) & h)** Redes Inalámbricas y Seguridad (Firewalls y Cifrado).
*   **e)** Acceso WAN (Túneles SSH y Conexiones Remotas).
*   **f)** Gestión de Puertos (Escaneo y Servicios).
*   **g)** Verificación y Diagnóstico (Herramientas de sistema).

> **Nota del Administrador:** En el entorno profesional, no basta con configurar una IP manualmente en Windows. Un administrador debe saber diagnosticar por qué la red falla usando herramientas del kernel. Este módulo elimina las capas intermedias de software para que comprendas la red en su estado puro: paquetes, direcciones y servicios.

---

### 2. REQUISITOS PREVIOS DE SOFTWARE Y ENTORNO

Para garantizar la reproducibilidad y el control de versiones (Git), se requiere configurar un entorno virtualizado. No se recomienda realizar prácticas en la red física del instituto sin supervisión directa.

#### 2.1. Hardware Recomendado
*   **CPU:** Mínimo 4 núcleos / 8 GB RAM (para VirtualBox). *Explicación:* Las máquinas virtuales consumen recursos de memoria y CPU reales del host. Si tienes menos, el sistema puede volverse inestable durante las pruebas de tráfico de red simulado.
*   **Disco:** 50 GB libres para máquinas virtuales.

#### 2.2. Software Base
| Herramienta | Versión Mínima | Propósito en el RA5 |
| :--- | :--- | :--- |
| **Sistema Operativo** | Windows 10/11, Linux (Ubuntu Server) o macOS | Host para las prácticas. |
| **Virtualización** | VirtualBox v7.x + Extension Pack | Creación de VMs aisladas para redes LAN/WAN simuladas. |
| **Terminal / Consola** | PowerShell, Bash, CMD | Ejecución de comandos nativos de red y gestión del sistema. |
| **Navegador Web** | Chrome / Firefox (Última versión) | Verificación de protocolos seguros (HTTPS/SSL) en el cliente. |
| **Control de Versiones** | Git + GitHub/GitLab | Gestión de archivos de configuración y documentación técnica. *Nota:* Se versionan los scripts de despliegue o configuraciones `.conf`, no código lógico. |

#### 2.3. Escenario Virtual Diseñado
Deberás desplegar la siguiente topología en VirtualBox:
1.  **Router NAT:** Máquina virtual con Ubuntu Server (Actúa como Gateway/DHCP). *Explicación:* Simula el router doméstico o empresarial que asigna IPs y conecta a Internet.
2.  **Cliente 1:** Máquina virtual Windows/Linux (Configuración TCP/IP). *Explicación:* El dispositivo cliente donde realizarás los diagnósticos de red.
3.  **Servidor Web:** Máquina virtual Linux (Para pruebas de conectividad WAN/PUERTO). *Explicación:* Simula un servicio externo al cual conectar tu aplicación.

---

### 3. DESARROLLO DE LAS PRÁCTICAS

#### PRÁCTICA 1: Configuración y Verificación del Stack TCP/IP (CE a, g)
**Objetivo:** Configurar manualmente interfaces de red y verificar la conectividad utilizando herramientas nativas del sistema operativo sin intermedia de programación.

**Lógica Técnica Profundizada:**
Para cumplir con el criterio **a)**, es necesario entender cómo el Sistema Operativo asigna direcciones IP. Usaremos comandos nativos (`ip`, `ifconfig`) para manipular la tabla de red del kernel y verificar la configuración física (MAC) vs lógica (IP).
*   **Under the Hood:** Al ejecutar un comando de red, se interactúa directamente con las tablas de enrutamiento del SO. La distinción entre IPv4 e IPv6 es crucial porque el protocolo de red moderno transita hacia IPv6, y tu configuración debe ser agnóstica a la versión para ser robusta.

**Procedimiento:**
1.  **Acceso al Sistema:** Abre una terminal (Bash en Linux o PowerShell/CMD en Windows) con privilegios de administrador/root.
2.  **Visualización de Interfaces:** Ejecuta el comando `ip addr show` (Linux) o `ipconfig /all` (Windows). Observa las direcciones MAC y los estados "UP/DOWN".
3.  **Asignación Estática (Manual):** Configura una IP estática en la interfaz principal del Cliente 1 para salir al Router NAT.

**Comandos de Configuración (Linux - Ubuntu Server):**
```bash
# Verificar nombre de interfaz
ip link show

# Asignar IP estática, máscara y gateway temporalmente
sudo ip addr add 192.168.50.10/24 dev eth0
sudo ip route add default via 192.168.50.1

# Verificar que la IP se ha aplicado correctamente
ip addr show eth0
```

**Comandos de Configuración (Windows - PowerShell):**
```powershell
# Listar interfaces de red
Get-NetIPConfiguration

# Configurar IP Estática (Reemplazar con los valores del laboratorio)
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 192.168.50.10 -PrefixLength 24 -DefaultGateway 192.168.50.1

# Verificar configuración
Get-NetIPConfiguration
```

**Verificación (CE g):**
*   Ejecuta `ping 192.168.50.1` (El Gateway). Debe responder con eco.
*   Compara la salida de los comandos anteriores con la configuración que aparece en el panel de red del sistema operativo para asegurar consistencia.

**Entregable:** Captura de pantalla de la terminal mostrando la asignación exitosa y un archivo de texto (`diagnostico_red.txt`) con la salida de `ip addr` o `ipconfig`.

> **Posibles Errores y Soluciones (Troubleshooting):**
> *   **Error: `Network is unreachable`:** Ocurre si la máscara no coincide con el rango del Gateway. *Solución:* Verifica que ambos dispositivos estén en la misma subred (ej. /24).
> *   **Error: `Permission denied`:** Falta de privilegios para modificar red. *Solución:* Ejecutar los comandos precedidos por `sudo` (Linux) o como Administrador (Windows).

---

#### PRÁCTICA 2: Gestión de Puertos y Escaneo (CE f)
**Objetivo:** Verificar la apertura o cierre de puertos utilizando herramientas de red estándar y gestionar el tráfico mediante reglas de firewall.

**Lógica Técnica Profundizada:**
El criterio **f)** exige gestionar estos puertos a nivel de sistema. Usaremos herramientas como `nmap`, `nc` (netcat) y `telnet` para detectar si servicios están escuchando, sin escribir programas para ello.
*   **Under the Hood:** Al intentar conectar, el sistema operativo del cliente envía un paquete SYN. Si la aplicación en el destino responde con SYN-ACK, el puerto está abierto. Si responde RST, está cerrado o bloqueado por firewall.

**Procedimientos de Prueba:**
1.  **Iniciar un servicio:** En una terminal del Servidor Web, ejecutar `python -m http.server 8000` (solo como proceso de fondo) o instalar Apache/Nginx para usar puertos estándar.
2.  **Ejecutar Escáner:** Desde el Cliente 1, utilizar la herramienta `nmap`.

**Comandos de Escaneo y Diagnóstico:**
```bash
# Escanear un puerto específico en localhost (Cliente)
nc -zv localhost 8000

# Escanear rango de puertos desde remoto (Servidor Web)
nmap -p 1-1000 <IP_DEL_SERVIDOR>

# Verificar qué procesos están escuchando en el servidor
netstat -tulpn | grep :<PUERTO>
```

**Gestión del Firewall:**
*   Para cumplir con la seguridad, es necesario configurar reglas explícitas.
*   **Ubuntu (UFW):** `sudo ufw allow 80/tcp` y `sudo ufw status`.
*   **Windows Defender:** Crear una regla de entrada para permitir tráfico TCP en el puerto específico.

**Nota Técnica:** Este ejercicio demuestra la gestión de puertos a nivel de sistema operativo, esencial para entender cómo las aplicaciones se exponen al exterior (DAM).

> **Posibles Errores y Soluciones (Troubleshooting):**
> *   **Error: `Connection refused`:** El puerto está cerrado o el servicio no está corriendo. *Solución:* Verifica que el servidor web esté activo en la consola del Servidor Web.
> *   **Timeout:** Si el firewall bloquea el paquete sin responder, la herramienta tardará hasta agotar el tiempo de espera. Esto indica una regla de "DROP" activa.

**Reto de Ampliación:**
*   Configura un Firewall (UFW o iptables) que bloquee todas las conexiones entrantes salvo en el puerto 22 (SSH) y 80 (HTTP). Verifica que `nmap` muestre solo esos puertos abiertos.

---

#### PRÁCTICA 3: Seguridad y Protocolos (CE c, h)
**Objetivo:** Configurar un servidor web con HTTPS utilizando certificados SSL/TLS y verificar la seguridad de la conexión mediante herramientas nativas.

**Lógica Técnica Profundizada:**
El criterio **h)** exige aplicar protocolos seguros. Para ello, configuraremos el servicio Web para usar cifrado real. La validación se realiza mediante inspección del certificado en el navegador o línea de comandos (`openssl`).
*   **Under the Hood:** El "Handshake TLS" implica intercambiar certificados digitales. Si el certificado no es válido (auto-firmado o caducado), el navegador mostrará una advertencia, lo cual es un indicador clave de seguridad para el administrador.

**Procedimiento:**
1.  **Generación de Certificado:** En el Servidor Web, generar un certificado auto-firmado usando OpenSSL.

**Comandos de Generación y Configuración (OpenSSL):**
```bash
# Generar Key Privada
openssl genrsa -out server.key 2048

# Generar Certificate Signing Request (CSR)
openssl req -new -key server.key -out server.csr

# Crear Certificado Auto-firmado (Válido por 365 días)
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```

2.  **Configuración del Servidor Web:** Editar el archivo de configuración de Apache o Nginx para apuntar a estos archivos (ej: `ssl_certificate` y `ssl_certificate_key`).
3.  **Verificación:** Acceder desde el Cliente 1 a `https://<IP_DEL_SERVIDOR>`.

**Comandos de Verificación SSL:**
```bash
# Comprobar certificado remoto
openssl s_client -connect <IP_DEL_SERVIDOR>:443 -showcerts

# Verificar la fecha de caducidad y emisor
openssl x509 -in server.crt -text -noout | grep -A 1 "Validity"
```

**Criterios Cubiertos:**
*   **c) WLAN / h) Seguridad:** Aunque este ejemplo usa HTTP/HTTPS, la lógica aplica para validar configuraciones de Wi-Fi (WPA2 vs WEP) mediante análisis de configuración en el router.

> **Posibles Errores y Soluciones (Troubleshooting):**
> *   **Error: `SSL Handshake Failure`:** Ocurre si las versiones de OpenSSL no coinciden o el protocolo está deshabilitado. *Solución:* Verificar la versión del Nginx/Apache y los módulos SSL instalados (`apt install libapache2-mod-ssl`).
> *   **Advertencia en el navegador:** Es normal con certificados auto-firmados. Debes aceptar manualmente el riesgo para probar la conexión, simulando un entorno de producción donde se usaría una CA real.

**Reto de Ampliación:**
*   Configurar un certificado válido (Let's Encrypt) usando `certbot` y verificar que el navegador no muestre advertencias de seguridad.

---

#### PRÁCTICA 4: Topología LAN y Dispositivos (CE b, d)
**Objetivo:** Simular una topología de red cableada gestionando direcciones IP estáticas y dinámicas mediante servicios nativos del sistema operativo.

**Lógica Técnica Profundizada:**
Para cumplir con **b)** y **d)**, configuraremos manualmente las IPs en los clientes y simularemos la asignación dinámica instalando un servidor DHCP en Linux, sin depender de scripts externos.
*   **Under the Hood:** El servicio DHCP utiliza el protocolo BOOTP sobre UDP. Al instalar y configurar el servicio `isc-dhcp-server`, el sistema operativo actúa como la autoridad que asigna recursos de red a los clientes (VMs).

**Procedimiento de Ejecución:**
1.  **Configuración del Servidor DHCP:** En la máquina virtual "Router", instalar y configurar el servidor.

**Comandos de Instalación y Configuración (Ubuntu):**
```bash
# Instalar servicio DHCP
sudo apt install isc-dhcp-server

# Editar configuración principal
sudo nano /etc/dhcp/dhcpd.conf
```

**Contenido del archivo `dhcpd.conf` (Ejemplo Declarativo):**
```text
subnet 192.168.50.0 netmask 255.255.255.0 {
    range 192.168.50.100 192.168.50.200;
    option routers 192.168.50.1;
    option domain-name-servers 8.8.8.8;
}
```

2.  **Configuración de la Interfaz:** Definir en `/etc/default/isc-dhcp-server` la interfaz `eth0`.
3.  **Verificación en Cliente:** En el "Cliente 1", configurar la tarjeta de red para obtener IP automáticamente ("Obtener dirección IP automáticamente" en Windows o DHCP en Linux).

**Validación de Conectividad (CE g):**
*   Ejecutar `ipconfig /all` (Windows) o `dhclient -v` (Linux) para ver si el cliente recibe la IP del rango definido.
*   Realizar un `ping` entre todas las máquinas virtuales de la red LAN.

> **Posibles Errores y Soluciones (Troubleshooting):**
> *   **Error: `No DHCP offers received`:** El servicio DHCP no está corriendo o bloqueado por firewall. *Solución:* Verificar estado del servicio con `systemctl status isc-dhcp-server` y abrir puertos UDP 67/68 en el firewall.
*   **IP Duplicada:** Conflictos de IP en la red. *Solución:* Asegurar que las IPs estáticas estén fuera del rango dinámico DHCP definido en `dhcpd.conf`.

**Reto de Ampliación:**
*   Configurar un servidor DNS local (Bind9) y asignarlo como opción de dominio en el archivo `dhcpd.conf` para resolver nombres internos.

---

#### PRÁCTICA 5: Acceso WAN y Túneles (CE e)
**Objetivo:** Configurar acceso remoto seguro mediante SSH utilizando claves criptográficas y túneles de red.

**Lógica Técnica Profundizada:**
El criterio **e)** trata sobre redes de área extensa (WAN). La forma más segura de acceder remotamente es mediante SSH (Secure Shell), que cifra el tráfico sin necesidad de instalar software adicional en el cliente, ya que está nativo en Linux y Windows 10+.
*   **Under the Hood:** SSH utiliza criptografía asimétrica al inicio. El administrador debe gestionar las claves públicas/privadas manualmente (`ssh-keygen`) para evitar contraseñas en texto plano.

**Procedimiento de Ejecución:**
1.  **Instalación del Servidor SSH:** Asegurar que el servicio OpenSSH Server esté activo en la VM remota (Router o Cliente).
    ```bash
    sudo apt install openssh-server
    sudo systemctl enable ssh
    sudo systemctl start ssh
    ```

2.  **Generación de Claves (Puente Seguro):** En la máquina local, generar un par de claves RSA/Ed25519 que no lleven contraseña para acceso automatizado seguro.

**Comandos de Generación y Copia de Clave:**
```bash
# Generar nueva clave en el cliente local
ssh-keygen -t ed25519 -C "usuario@laboratorio" -f ~/.ssh/id_rsa_lab

# Copiar la clave pública al servidor remoto (Autorización)
ssh-copy-id usuario@<IP_DEL_SERVIDOR>
```

3.  **Configuración de Túnel Puente:** Crear un túnel inverso para acceder a un servicio local desde el remoto sin exponer puertos en el firewall público.

**Comando de Ejecución de Túnel (CLI):**
```bash
# Sintaxis: ssh -N -L [puerto_local]:localhost:[puerto_remoto] usuario@host
ssh -N -L 8080:localhost:3000 usuario@<IP_DEL_SERVIDOR>
```

**Verificación de Acceso:**
*   Desde el Servidor Remoto, intentar acceder a `http://127.0.0.1:3000`. Debería redirigirse al servicio local del Cliente 1.

> **Posibles Errores y Soluciones (Troubleshooting):**
> *   **Error: `Permission denied (publickey)`:** La clave pública no se copió correctamente en `/home/usuario/.ssh/authorized_keys`. *Solución:* Verificar permisos de archivos (`chmod 600 authorized_keys`).
*   **Timeout:** El firewall de la máquina remota bloquea el puerto 22. *Solución:* Configurar reglas de entrada en VirtualBox o dentro del sistema operativo Linux (`ufw allow 22`).

**Reto de Ampliación:**
*   Deshabilitar el acceso por contraseña en `/etc/ssh/sshd_config` (`PasswordAuthentication no`) y forzar el uso exclusivo de claves SSH para asegurar la infraestructura.

---

### 4. PROCEDIMIENTOS DE COMPILACIÓN Y PRUEBAS FINALES

Para aprobar el RA5 mediante estas prácticas administrativas, debes seguir el siguiente flujo de control de calidad:

1.  **Validación de Comandos:**
    *   Asegurar que todos los comandos `ip`, `nmap`, `openssl` ejecutan sin errores en la terminal del sistema operativo.
2.  **Ejecución de Servicios:**
    *   Verificar que los servicios (SSH, DHCP, HTTP) están corriendo (`systemctl status <servicio>`).
3.  **Pruebas de Integración:**
    *   Ejecutar el escáner `nmap` contra el puerto del servidor web levantado en la VM. Si detecta el puerto y responde correctamente con `OPEN`, se valida la gestión de puertos (CE f).
4.  **Control de Versiones (Git):**
    *   Inicializar repositorio: `git init`.
    *   Commit final de configuración: `git commit -m "Configuración RA5: Infraestructura red y seguridad"`.

> **Nota del Administrador:** El uso de Git en este contexto es para versionar tus archivos de configuración (`dhcpd.conf`, `sshd_config`, scripts de despliegue) y documentación. Cada cambio que hagas debe tener una razón documentada (ej. "Actualización reglas firewall", "Nueva subred DHCP"). Esto facilita la auditoría y mantenimiento futuro.

---

### 5. CRITERIOS DE EVALUACIÓN DEL LABORATORIO (RÚBRICA)

| Criterio | Indicador de Desempeño Puntuación Total |
| :--- | :--- |
| **a) TCP/IP** | La configuración manual de IP y máscara es coherente con la topología y permite comunicación. (10%) |
| **b) LAN Cableada** | El servicio DHCP asigna IPs correctamente a las VMs clientes en el laboratorio virtual. (15%) |
| **c) WLAN / h) Seguridad** | La configuración SSL/TLS es válida y OpenSSL identifica correctamente los certificados. (10%) |
| **d) Dispositivos** | El comando `nmap` o `netstat` identifica correctamente interfaces y puertos activos sin colapsar la VM. (10%) |
| **e) WAN** | La conexión SSH con claves criptográficas es exitosa y el túnel permite acceso a servicios locales. (15%) |
| **f) Puertos** | El escaneo de puertos devuelve "ABIERTO" o "CERRADO/RECHAZADO" de forma precisa según el firewall. (20%) |
| **g) Verificación** | Se utilizan comandos nativos del sistema (`ping`, `ip addr`, `netstat`) para validar la red sin herramientas externas no instaladas. (15%) |
| **Presentación** | Archivos de configuración documentados y versionados en Git con comentarios claros. (5%) |

---

### 6. CONCLUSIÓN TÉCNICA

Esta guía integra los contenidos de "Conexión de sistemas en red" con las competencias profesionales del Administrador de Sistemas dentro del desarrollo DAM. Al configurar la infraestructura manualmente, el alumno no solo aprende *qué* es una IP o un puerto, sino *cómo interactuar* con ellos mediante herramientas del sistema operativo. Esto asegura la cobertura exhaustiva del RA5 bajo un enfoque profesional donde la estabilidad y seguridad (Hardening) son claves.

**Nota del Administrador:** Recuerda que la seguridad en el laboratorio es primordial. Nunca ejecutes scripts de escaneo o configuración IP en redes públicas ni sin permiso explícito de tu instructor. El conocimiento adquirido aquí te permite construir sistemas más robustos, pero también conlleva la responsabilidad ética de no dañar infraestructuras ajenas.

---
*Documento elaborado bajo estricta adherencia a la normativa curricular del módulo Sistemas Informáticos (FP DAM) y alineado con las competencias profesionales exigidas por el sector tecnológico.*
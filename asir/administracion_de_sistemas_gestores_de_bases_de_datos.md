# Módulo 0377 - Administración de Sistemas Gestores de Bases de Datos.

## Currículo BOE (Resultados de aprendizaje y Criterios de evaluación)

Resultados de aprendizaje y criterios de evaluación.
1. Implanta sistemas gestores de bases de datos analizando sus características y
ajustándose a los requerimientos del sistema.
Criterios de evaluación:
a) Se ha reconocido la utilidad y función de cada uno de los elementos de un sistema
gestor de bases de datos.
b) Se han analizado las características de los principales sistemas gestores de bases
de datos.
c) Se ha seleccionado el sistema gestor de bases de datos.
d) Se ha identificado el software necesario para llevar a cabo la instalación.
e) Se ha verificado el cumplimiento de los requisitos hardware.
f) Se han instalado sistemas gestores de bases de datos.
g) Se ha documentado el proceso de instalación.
h) Se ha interpretado la información suministrada por los mensajes de error y ficheros
de registro.
i) Se han resuelto las incidencias de la instalación.
j) Se ha verificado el funcionamiento del sistema gestor de bases de datos.
2. Configura el sistema gestor de bases de datos interpretando las especificaciones
técnicas y los requisitos de explotación.
cve: BOE-A-2009-18355
BOLETÍN OFICIAL DEL ESTADO
Núm. 278 Miércoles 18 de noviembre de 2009 Sec. I.   Pág. 97891
Criterios de evaluación:
a) Se han descrito las condiciones de inicio y parada del sistema gestor.
b) Se ha seleccionado el motor de base de datos.
c) Se han asegurado las cuentas de administración.
d) Se han configurado las herramientas y software cliente del sistema gestor.
e) Se ha configurado la conectividad en red del sistema gestor.
f) Se han definido las características por defecto de las bases de datos.
g) Se han definido los parámetros relativos a las conexiones (tiempos de espera,
número máximo de conexiones, entre otros).
h) Se ha documentado el proceso de configuración.
3. Implanta métodos de control de acceso utilizando asistentes, herramientas gráficas
y comandos del lenguaje del sistema gestor.
Criterios de evaluación:
a) Se han creado vistas personalizadas para cada tipo de usuario.
b) Se han creado sinónimos de tablas y vistas.
c) Se han definido y eliminado cuentas de usuario.
d) Se han identificado los privilegios sobre las bases de datos y sus elementos.
e) Se han agrupado y desagrupado privilegios.
f) Se han asignado y eliminado privilegios a usuarios.
g) Se han asignado y eliminado grupos de privilegios a usuarios.
h) Se ha garantizando el cumplimiento de los requisitos de seguridad.
4. Automatiza tareas de administración del gestor describiéndolas y utilizando guiones
de sentencias.
Criterios de evaluación:
a) Se ha reconocido la importancia de automatizar tareas administrativas.
b) Se han descrito los distintos métodos de ejecución de guiones.
c) Se han identificado las herramientas disponibles para redactar guiones.
d) Se han definido y utilizado guiones para automatizar tareas.
e) Se han identificado los eventos susceptibles de activar disparadores.
f) Se han definido disparadores.
g) Se han utilizado estructuras de control de flujo.
h) Se han adoptado medidas para mantener la integridad y consistencia de la
información.
5. Optimiza el rendimiento del sistema aplicando técnicas de monitorización y
realizando adaptaciones.
Criterios de evaluación:
a) Se han identificado las herramientas de monitorización disponibles para el sistema
gestor.
b) Se han descrito las ventajas e inconvenientes de la creación de índices.
c) Se han creado índices en tablas y vistas.
d) Se ha optimizado la estructura de la base de datos.
e) Se han optimizado los recursos del sistema gestor.
f) Se ha obtenido información sobre el rendimiento de las consultas para su
optimización.
g) Se han programado alertas de rendimiento.
h) Se han realizado modificaciones en la configuración del sistema operativo para
mejorar el rendimiento del gestor.
cve: BOE-A-2009-18355
BOLETÍN OFICIAL DEL ESTADO
Núm. 278 Miércoles 18 de noviembre de 2009 Sec. I.   Pág. 97892
6. Aplica criterios de disponibilidad analizándolos y ajustando la configuración del
sistema gestor.
Criterios de evaluación:
a) Se ha reconocido la utilidad de las bases de datos distribuidas.
b) Se han descrito las distintas políticas de fragmentación de la información.
c) Se ha implantado una base de datos distribuida homogénea.
d) Se ha creado una base de datos distribuida mediante la integración de un conjunto
de bases de datos preexistentes.
e) Se ha configurado un «nodo» maestro y varios «esclavos» para llevar a cabo la
replicación del primero.
f) Se ha configurado un sistema de replicación en cadena.
g) Se ha comprobado el efecto de la parada de determinados nodos sobre los
sistemas distribuidos y replicados.

## Contenidos Básicos (Comunidad de Madrid)

CONTENIDOS (Duración 60 horas)

Instalación y configuración de un sistema gestor de base de datos:
- Funciones del sistema gestor de base de datos (SGBD). Componentes. Tipos.
- Arquitectura del sistema gestor de base de datos. Arquitectura ANSI/SPARC.
- Sistemas gestores de base de datos comerciales y libres.
- El administrador de bases de datos DBA (DataBase Administrator). Funciones.
- Lenguaje estándar de consulta SQL.
- Instalación y configuración de un SGBD. Configuración de Parámetros relevantes.
- Integración del SGBD en el sistema operativo: sistema de ficheros, control de usuarios…
- Instalación de un SGBD de dos capas.
- Relación entre el SGBD y la Base de Datos (BD): instancias de BD.
- Estructura del diccionario de datos.
- Ficheros LOG.
- Arquitectura del SGBD: archivos en disco, espacios de memoria, procesos.
Acceso a la información:
- Tipos de objetos de la BD.
- Creación, modificación y eliminación de vistas.
- Operaciones DML sobre vistas.
- Creación, modificación y eliminación de usuarios.
-  Asignación y retirada de permisos a usuarios. Puntos de acceso al sistema.
- Paquetes de permisos: los roles. Creación y eliminación. Asignación y retirada de
permisos a roles. Asignación y retirada de roles a usuarios.
- Normativa legal vigente sobre protección de datos.
- Límites en el SGBD: los perfiles. Creación. Asignación y retirada de límites a usuarios.
Automatización de tareas: construcción de guiones de administración:
- Herramientas para la creación de guiones; procedimientos de ejecución.
- Planificación de tareas administrativas mediante guiones.
- Eventos del sistema: arranque/parada de la BD, conexión/desconexión de usuarios,
creación de objetos.
- Disparadores: sobre tablas, sobre vistas, asociados a eventos del sistema.
- Excepciones.
- Generación de consultas dinámicas.
Optimización del rendimiento: monitorización y optimización:
- Herramientas de monitorización disponibles en el sistema gestor.
- Elementos y parámetros susceptibles de ser monitorizados.
- Optimización:
• Espacio de almacenamiento.
• Procesos.
• Uso de memoria.
- Optimización de consultas: plan de ejecución.
- Herramientas y sentencias para la gestión de índices.
- Herramientas para la creación de alertas de rendimiento.
Operaciones de mantenimiento y recuperación de errores:
- Arranque y parada de la BD.
- Copias de seguridad:
• Lógicas vs. físicas.
• En frío vs. en caliente.
• Totales, incrementales, acumulativas.
- Herramientas gráficas y utilidades proporcionadas por el sistema gestor para la realización
de copias de seguridad.
- Sentencias para la realización y recuperación de copias de seguridad.
- Recuperación de la BD a partir de copias de seguridad.
- Recuperación de archivos de configuración y datos dañados.
- Tareas de actualización y migración de la BD.
Aplicación de criterios de disponibilidad a bases de datos distribuidas y replicadas:
- Bases de datos distribuidas: objetivo.
- Tipos de SGBD distribuidos.
- Componentes de un SGBD distribuido.
- Técnicas de fragmentación.
- Técnicas de asignación.
- Consultas distribuidas.
- Transacciones distribuidas.
- Optimización de consultas sobre bases de datos distribuidas.
- Replicación.
- Configuración del «nodo maestro» y los «nodos esclavos».
Protección de datos y confidencialidad:
- Legislación vigente en materia de protección de datos.
- Monitorización de la actividad de los usuarios del SGBD. Auditoría: sesiones, sentencias, objetos…
- Cifrado de datos y de comunicaciones.

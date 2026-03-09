# Módulo 0372 - Gestión de Base de Datos.

## 1. Reconoce los elementos de las bases de datos analizando sus funciones y

valorando la utilidad de sistemas gestores.
Criterios de evaluación:
a) Se han analizado los distintos sistemas lógicos de almacenamiento y sus
funciones.
b) Se han identificado los distintos tipos de bases de datos según el modelo de datos
utilizado.
c) Se han identificado los distintos tipos de bases de datos en función de la ubicación
de la información.
d) Se ha reconocido la utilidad de un sistema gestor de bases de datos.
e) Se ha descrito la función de cada uno de los elementos de un sistema gestor de
bases de datos.
f) Se han clasificado los sistemas gestores de bases de datos.
cve: BOE-A-2009-18355
BOLETÍN OFICIAL DEL ESTADO
Núm. 278 Miércoles 18 de noviembre de 2009 Sec. I.   Pág. 97871

### Contenidos Básicos Relacionados (CM):

CONTENIDOS (Duración 200 horas)

Sistemas de almacenamiento de la información:
- Ficheros (planos, indexados y acceso rápido, de marcas, entre otros).
- Bases de Datos (BD). Conceptos, usos y tipos según el modelo de datos, la ubicación de
la información.
- Sistemas gestores de bases de datos (SGBD): funciones, componentes y tipos.

Diseño conceptual y lógico de bases de datos:
- Modelos de datos: relacional y orientado a objetos.
- La representación del problema. El modelo conceptual: los diagramas E/R
(Entidad/Relación).
• Entidades y atributos. Identificadores principales.
• Relaciones: cardinalidad y correspondencia.
• Relaciones de dependencia en existencia y en identificación.
- El modelo E/R ampliado:
• Atributos multivaluados y compuestos.
• Jerarquías y generalizaciones.
• Asociaciones.
- El modelo relacional: Terminología del modelo relacional. Características de una relación.
Claves primarias y claves ajenas.
- Paso del diagrama E/R al modelo relacional.
- Normalización. Dependencias funcionales. Formas normales. Conveniencia de la
desnormalización.
- El modelo orientado a objetos. Conceptos generales.
• Diagramas de clases y de objetos.

Diseño físico de bases de datos:
- Herramientas gráficas proporcionadas por el sistema gestor para la implementación de la
base de datos.
- Lenguaje estándar de consulta SQL (Standard Query Language).
• Lenguaje de definición de datos DDL (Data Definition Language): Creación,
modificación y eliminación de objetos de la base de datos.
• Lenguaje de manipulación de datos DML (Data Manipulation Language): Selección,
inserción, modificación y eliminación de registros.
• Lenguaje de control de datos DCL (Data Control Language): Confirmación/anulación
de transacciones.
- Creación, modificación y eliminación de bases de datos.
- Creación, modificación y eliminación de tablas. Tipos de datos.
- Implementación de restricciones sobre tablas: clave primaria, clave ajena, unicidad,
chequeo, valores por defecto.
- Truncado de tablas.

Edición de los datos:
- Herramientas gráficas, proporcionadas por el sistema gestor o externas, para la edición de
la información.
- Sentencias de inserción, eliminación y actualización de registros:
• A partir de datos proporcionados por el usuario.
• A partir de datos recuperados mediante subconsultas.
- Subconsultas y combinación de órdenes de edición.
- Transacciones. Estados temporales intermedios de la base de datos. Sentencias de
procesamiento de transacciones.
- Acceso simultáneo a los datos: políticas de bloqueo. Niveles de bloqueo (fila, tabla).

Creación de otros objetos de la base de datos:
- Vistas. Vistas montadas sobre múltiples tablas. Operaciones sobre vistas.
- Sinónimos de objetos.
- Enlaces a otras bases de datos.

Optimización de consultas:
- Creación de índices. Monocampo vs. multicampo.
- Índices únicos y con duplicados.
- Índices basados en funciones.
- Criterios para la creación de índices.
- Plan de ejecución de sentencias. Análisis comparativo.
- Métodos de vinculación de tablas.
- Optimización basada en costes vs. basada en reglas.
- Sugerencias (hints) de ejecución.

Construcción de guiones:
- Introducción. Conceptos generales del lenguaje de programación integrado en el SGBD.
- Tipos de datos, identificadores, variables.
- Operadores. Estructuras de control.
- Cursores.
- Procedimientos y funciones almacenados.
- Excepciones.

Bases de datos distribuidas:
- Conceptos y diseño.
- Casos de idoneidad.
- Técnicas de fragmentación: vertical, horizontal, mixta.
- Técnicas de distribución de datos.
- Esquemas de asignación y replicación de datos.

## 2. Diseña modelos lógicos normalizados interpretando diagramas entidad/relación.

Criterios de evaluación:
a) Se ha identificado el significado de la simbología propia de los diagramas entidad/
relación.
b) Se han utilizado herramientas gráficas para representar el diseño lógico.
c) Se han identificado las tablas del diseño lógico.
d) Se han identificado los campos que forman parte de las tablas del diseño lógico.
e) Se han identificado las relaciones entre las tablas del diseño lógico.
f) Se han definido los campos clave.
g) Se han aplicado las reglas de integridad.
h) Se han aplicado las reglas de normalización hasta un nivel adecuado.
i) Se han identificado y documentado las restricciones que no pueden plasmarse en
el diseño lógico.

## 3. Realiza el diseño físico de bases de datos utilizando asistentes, herramientas

gráficas y el lenguaje de definición de datos.
Criterios de evaluación:
a) Se han definido las estructuras físicas de almacenamiento.
b) Se han creado tablas.
c) Se han seleccionado los tipos de datos adecuados.
d) Se han definido los campos clave en las tablas.
e) Se han implantado todas las restricciones reflejadas en el diseño lógico.
f) Se ha verificado mediante un conjunto de datos de prueba que la implementación
se ajusta al modelo.
g) Se han utilizado asistentes y herramientas gráficas.
h) Se ha utilizado el lenguaje de definición de datos.
i) Se ha definido y documentado el diccionario de datos.

## 4. Consulta la información almacenada manejando asistentes, herramientas gráficas

y el lenguaje de manipulación de datos.
Criterios de evaluación:
a) Se han identificado las herramientas y sentencias para realizar consultas.
b) Se han realizado consultas simples sobre una tabla.
c) Se han realizado consultas que generan valores de resumen.
d) Se han realizado consultas sobre el contenido de varias tablas mediante
composiciones internas.
e) Se han realizado consultas sobre el contenido de varias tablas mediante
composiciones externas.
f) Se han realizado consultas con subconsultas.
g) Se han valorado las ventajas e inconvenientes de las distintas opciones válidas
para llevar a cabo una consulta determinada.

### Contenidos Básicos Relacionados (CM):

Realización de consultas:
- Herramientas gráficas,  proporcionadas por el sistema gestor o externas, para la
realización de consultas.
- Selección de registros:
• Elección de origen de datos: tablas, vistas, selecciones.
• Filtrado de registros.
• Orden de los resultados devueltos.
- Tratamiento de valores nulos.
- Consultas de resumen. Agrupamiento de registros. Filtrado sobre agrupaciones.
- Operaciones de conjuntos sobre consultas: unión, intersección y diferencia.
- Vinculación de tablas: claves primarias y ajenas. Composiciones internas y externas.
- Subconsultas:
• Devolución de valores individuales.
• Devolución de listas de valores.
• Devolución de tuplas de valores.
• Correlacionadas.
- Consultas jerárquicas.

## 5. Modifica la información almacenada utilizando asistentes, herramientas gráficas y

el lenguaje de manipulación de datos.
Criterios de evaluación:
a) Se han identificado las herramientas y sentencias para modificar el contenido de
la base de datos.
b) Se han insertado, borrado y actualizado datos en las tablas.
c) Se ha incluido en una tabla la información resultante de la ejecución de una
consulta.
cve: BOE-A-2009-18355
BOLETÍN OFICIAL DEL ESTADO
Núm. 278 Miércoles 18 de noviembre de 2009 Sec. I.   Pág. 97872
d) Se han adoptado medidas para mantener la integridad y consistencia de la
información.
e) Se han diseñado guiones de sentencias para llevar a cabo tareas complejas.
f) Se ha reconocido el funcionamiento de las transacciones.
g) Se han anulado parcial o totalmente los cambios producidos por una transacción.
h) Se han identificado los efectos de las distintas políticas de bloqueo de registros.

## 6. Ejecuta tareas de aseguramiento de la información, analizándolas y aplicando

mecanismos de salvaguarda y transferencia.
Criterios de evaluación:
a) Se han identificado herramientas gráficas y en línea de comandos para la
administración de copias de seguridad.
b) Se han realizado copias de seguridad.
c) Se han restaurado copias de seguridad.
d) Se han identificado las herramientas para importar y exportar datos.
e) Se han exportado datos a diversos formatos.
f) Se han importado datos con distintos formatos.
g) Se ha interpretado correctamente la información suministrada por los mensajes de
error y los ficheros de registro.
h) Se ha transferido información entre sistemas gestores.

### Contenidos Básicos Relacionados (CM):

Gestión de seguridad de los datos:
- Tipos de fallos.
- Recuperación de fallos.
- Copias de seguridad.
- Herramientas gráficas y utilidades proporcionadas por el sistema gestor para la realización
de copias de seguridad.
- Sentencias para la realización y recuperación de copias de seguridad.
- Herramientas gráficas y utilidades para importación y exportación de datos.
- Transferencia de datos entre sistemas gestores.

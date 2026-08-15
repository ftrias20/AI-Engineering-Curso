     Hace algunos años el tamaño del software a construir se 
diferenciaba mucho del actual; el diseño de los programas se 
realizaba a nivel de algoritmos. 
 La documentación del diseño de estas aplicaciones se 
realizaba utilizando “Diagramas de Flujo” (ahora 
estandarizado en UML bajo el nombre de Diagramas de 
Actividad).
 Con el transcurso de los años los sistemas fueron 
aumentando sus tamaños pasando a documentar, además de 
algoritmos, también estructuras de datos del programa.
 En la actualidad el diseño de aplicaciones cada vez 
contiene mayor complejidad y tamaño, abarcando millones 
de líneas de código, lo que hasta hace algunas décadas era 
impensable.
5

Introducción (2)
 Este aumento tan grande en el tamaño y complejidad llevó a la 
introducción de patrones y guías para la realización de los 
diseños de aplicaciones, algunas de las cuales son abordadas en 
el curso.
 La primera diferencia notoria con los diseños de hace algunos 
años es que hoy el diseño se pretende hacer en varios niveles 
distintos de descomposición.
 Al primero de los niveles de descomposición es al que llamamos 
Arquitectura de Software.
 En general, actualmente para aplicaciones orientadas a objetos, 
se pueden identificar principalmente 3 niveles de diseño:
• Arquitectura de Software
• Diseño de Clases
• Diseño de Algoritmos
6

Introducción (3)
 “A medida que el tamaño y complejidad de los sistemas de 
software aumenta, el problema del diseño va más allá de los 
algoritmos y estructuras de datos de la computación: diseñar y 
especificar la estructura de todo el sistema emerge como un 
nuevo tipo de problema.
Los problemas estructurales incluyen la organización y 
estructuras de control global; protocolos de comunicación, 
sincronización y acceso a datos; asignación de funcionalidad a los 
elementos de diseño; distribución física; composición de los 
elementos de diseño; escalabilidad y performance; y la selección 
entre las alternativas de diseño.”
“Este es el nivel de diseño de la arquitectura de software.”
Garlan y Shaw
7

Introducción (4)
 Las características de la Arquitectura de Software 
condicionarán directamente las características del 
software que se construirá en base a ella (escalabilidad, 
desempeño, mantenibilidad, interoperabilidad, etc.).
 Es por esto que los estilos de arquitectura seleccionados 
para la arquitectura y la estructura particular que se 
realice dependerán en general de requerimientos no 
funcionales relacionados con:
• Desempeño
• Seguridad
• Mantenibilidad
8

Introducción (5)
 Desempeño: Si se desea desempeño, buscar minimizar las 
invocaciones y las comunicaciones. Para esto lo mejor es 
tener componentes de grano grueso.
 Seguridad: Si se desea seguridad, buscar estructurar en 
capas, con los recursos (de datos o ejecución) más críticos 
protegidos en las capas más internas, con más niveles de 
validación.
 Mantenibilidad: Los componentes deben ser auto
contenidos, que incluyan todo lo necesario y que permitan 
ser intercambiados por otros fácilmente. Para esto lo mejor 
son componentes de grano fino (con alta cohesión y bajo 
acoplamiento).
9

Documentar la Arquitectura (1)
 SAD (Software Architecture Description): Es el resultado 
del proceso de diseño de la arquitectura de un sistema, 
donde se incluyen modelos gráficos y textuales que 
describen las características de la misma.
 Según “The 4+1 View Model of Software Architecture” 
(Krutchen, 1995):
“Se plantean vistas predefinidas para la arquitectura: lógica, 
procesos, implementación, física y de CU. Todas las vistas 
son guiadas por CU o por escenarios de los mismos que sean 
relevantes para la arquitectura.”
10

Documentar la Arquitectura (2)
 Posible contenido del SAD:
• Vista del Modelo de Casos de Uso:
 Diagrama de los CU relevantes a la arquitectura
 Casos de Uso relevantes a la arquitectura
• Vista del Modelo de Diseño:
 Descomposición en subsistemas
 Diseño de clases
 Diseño de Casos de Uso
 Trazabilidad desde el Modelo de Casos de Uso al Modelo de Diseño
• Vista del Modelo de Distribución:
 Diagrama de distribución
 Nodos
 Conexiones
• Justificación de la arquitectura propuesta
11

Documentar la Arquitectura (3)
 Beneficios de una buena documentación de la 
arquitectura:
• Mejora la comunicación entre los distintos 
interesados: 
 Equipo de diseño   clientes
 Equipo de diseño   desarrolladores
• Ayuda a mantener una visión global del sistema sin 
tener en cuenta detalles innecesarios.
• Proporciona las bases para que el software a construir 
sea coherente con los requerimientos planteados (ej: 
performance o mantenibilidad).
12

Estilos (1)
 ¿Qué son los estilos arquitectónicos?
• Son soluciones de organización, estructura y 
comunicación a nivel de sistema.
 ¿Qué función cumplen?
• Plantean la base de organización para la estructura de 
sistemas de software. 
• Brindan un conjunto de tipos de elementos 
predefinidos (componentes), especificando para cada 
uno sus responsabilidades, e incluyen reglas y guías 
para organizar la manera en que estos componentes 
se relacionan.
13

Estilos (2)
 ¿Para qué sirven?
• Al igual que los patrones de diseño, los estilos son 
patrones pero a nivel de la Arquitectura.
• Permiten la selección de soluciones conocidas para 
problemas comunes en el diseño de sistemas; estas 
soluciones están probadas y son bien conocidas.
• Si se basa una Arquitectura en un estilo que es 
conocido, las personas (diseñadores, desarrolladores, 
etc.) entenderán de manera sencilla las características 
importantes de la misma.
14

Estilos (3)
 Algunos estilos destacables (lista no exhaustiva y en 
constante actualización):
• Pizarrón (Blackboard)
• Cliente - Servidor (Client - Server)
• Capas (Layers)
• Descomposición Orientada a Objetos (Data
Abstraction & OO Organization)
• Tubos y Filtros (Pipes & Filters)
• Arquitectura Orientada a Servicios (SOA: Service 
Oriented Architecture)
15

Estilos (4)
 Pizarrón (Blackboard):
• Es un estilo de arquitectura que se centra en los datos.
• Hay un almacenamiento central de datos (pizarrón) y un 
conjunto de componentes descentralizados (fuentes 
de conocimiento) que operan sobre el primero.
16

Estilos (5)
 Pizarrón (Blackboard) (cont.):
• Fuentes de Conocimiento:
 Son procesos independientes que se corresponden con 
particiones del conocimiento de la realidad.
 Son notificadas de los cambios en el pizarrón y responden a 
estos cambios.
• Pizarrón:
 Estado completo de la solución de problema.
 Es el único medio por el cual las fuentes de conocimiento 
interactúan para resolver el problema (funcionalidades del 
sistema).
 El control de la aplicación está guiado completamente por el 
estado del pizarrón, pero puede ser implementado en el 
pizarrón, en las fuentes de conocimiento o combinando (parte en 
el pizarrón y parte en las fuentes de conocimiento).
17

Estilos (6)
 Cliente - Servidor:
• El sistema es dividido en Servidores que brindan 
servicios y Clientes que utilizan (consumen) dichos 
servicios.
• No necesariamente el hecho de que la arquitectura 
sea cliente - servidor implica que estos componentes 
tengan que ejecutarse en máquinas distintas.
• Los clientes conocen a los servidores pero no se 
conocen entre sí y el servidor no tiene por qué 
conocer a los clientes.
18

Estilos (7)
 Cliente – Servidor (cont.) :
• Se pueden observar 2 variantes diferenciadas de la 
misma arquitectura:
•Cliente fino: La lógica de negocios está contenida 
casi completamente en el servidor, dejando lo 
mínimo indispensable en el cliente.
•Cliente grueso: Se distribuye parte de la lógica de 
negocio a la aplicación cliente, liberando de parte 
del procesamiento al servidor, haciendo que tenga 
menor carga de trabajo.
19

Estilos (8)
 Capas :
• El sistema se organiza en 
componentes ordenados 
llamados capas.
• Cada una de las capas 
provee a las capas 
superiores un conjunto de 
servicios, utilizando para 
ello los servicios de las 
capas inferiores

20
Estilos (9)
 Capas (cont.) :
• Modelo Estricto: Las capas se comunican únicamente con 
las capas inmediatamente inferiores.
• Modelo Laxo: Permite a las capas comunicarse con 
cualquier capa inferior.
• Algunas posibles ventajas:
 Ayuda a la comprensión, mantenimiento, reutilización 
y portabilidad.
• Algunas posibles desventajas:
 No siempre es fácil decidir como dividir las capas.
 La invocación pasando por todas las capas puede 
afectar negativamente la performance del sistema.
21

Estilos (10)
 Descomposición Orientada a Objetos:
• Se descompone el sistema en un conjunto de objetos 
que se comunican.
• Los objetos encapsulan estado (datos) y 
comportamiento (operaciones y métodos).
• Facilita la tarea de desarrollo del sistema por ser una 
arquitectura en la que se manejan los conceptos de 
manera natural.
• Brinda herencia, polimorfismo, sobrecarga de 
operaciones entre sus características más destacables.
22

Estilos (11)
 Descomposición Orientada a Objetos (cont.):
• Algunas posibles ventajas: 
•Facilita la comprensión.
•Favorece la reutilización de elementos.
• Algunas posibles desventajas:
•Para poder comunicarse con un objeto hay que 
conocer su interfaz.
•Los cambios en las interfaces de los objetos 
afectan a todos los objetos que la utilizan.
23

Estilos (12)
 Tubos y filtros:
• El sistema se descompone en distintos componentes 
funcionales llamados filtros.
• Los datos se transportan por medio de tubos entre los 
filtros, aplicando así transformaciones sucesivas a los 
datos que ingresan (los datos llegan a un filtro por medio 
de tubos, se transforman en el filtro y son enviados al 
siguiente filtro por otro tubo).
• Un filtro puede recibir y enviar datos por múltiples tubos.
• Cada filtro es independiente, no conoce a los demás 
filtros.
• El procesamiento de un filtro puede comenzar inclusive 
antes de terminar de leer la entrada.
24

Estilos (13)
 Tubos y filtros (cont.) :
• No importa el orden de los filtros a la hora de 
implementar la aplicación, el comportamiento de la 
misma sólo dependerá del grafo de precedencia:
25

Estilos (14)
 Tubos y filtros (cont.) :
• Algunas posibles ventajas:
 Los filtros son fácilmente reutilizables.
 Es fácil e intuitivo pensar en secuencias de procesamiento para los 
datos.
 Agregar nuevos filtros para hacer evolucionar o extender el sistema 
es sencillo dado que son independientes de lo que ya hubiera.
• Algunas posibles desventajas:
 Es difícil construir sistemas interactivos utilizando esta 
arquitectura.
 Hay que acordar los tipos de datos de entrada y salida de los filtros 
para que no haya inconsistencias. Deben ser genéricos si se quiere 
que los filtros sean lo más independientes posible.
 El no conocer la entrada o salida que tengan los filtros puede dar 
lugar a múltiples chequeos de condiciones, lo que puede 
volverlos ineficientes.
26

Estilos (15)
 Service Oriented Architecture:
• Define servicios que representan algunas 
funcionalidades o parte de la lógica de negocios. Éstas 
se exponen en interfaces estándar para que cualquier 
componente pueda utilizarlas.
• Los servicios son completamente independientes de 
las aplicaciones que los utilicen.
• Las soluciones basadas en servicios son escalables y 
brindan algún tipo de protocolo estándar para la 
publicación e invocación de los mismos, facilitando la 
interacción entre los sistemas, ya sean propios o por 
parte de otras aplicaciones de terceros.
27

Estilos (15)
 Service Oriented Architecture (cont.):
• La conexión con los servicios pueden ser en tiempo de 
ejecución, permitiendo así a la aplicación adaptarse 
fácilmente a cambios.
• Es sencillo cambiar los proveedores del servicio 
siempre que brinden la misma interfaz.
• Comúnmente se utilizan web services, pero no es el 
único tipo de servicios posible. Éstos se basan en 
estándares con base en XML por lo que pueden 
(potencialmente) funcionar en cualquier plataforma y 
ser escritos en cualquier lenguaje de programación. 
Esto brinda a los web services una alta 
interoperabilidad
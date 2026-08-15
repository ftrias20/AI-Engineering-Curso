Lo que motiva el surgimiento de los patrones de 
diseño es la necesidad de sistematizar, organizar y 
documentar la experiencia de los diseñadores 
expertos en OO.
 ¿Qué es lo que no hace un diseñador experto?
• Reinventar la rueda. Es decir, buscar distintas 
soluciones para el mismo problema cada vez que 
se le presenta.
 ¿Cómo se logra no reinventar la rueda?
• Aprendiendo de la experiencia, organizándola y 
documentándola en un catálogo de patrones de 
diseño (“GoF”, ver Referencia Principal).
5

Introducción (2)
 ¿Qué es un patrón?
• “Cada patrón describe un problema que ocurre una y 
otra vez, y luego describe una solución, de tal forma 
que Ud. puede utilizar esa solución un millón de 
veces, pero nunca haciéndolo de la misma forma.” 
[Christopher Alexander, 
http://es.wikipedia.org/wiki/Christopher_Alexander]
• ¡Esta cita hace referencia a patrones en 
arquitectura urbana (edificios) no a patrones de 
software.
6

Introducción (3)
 ¿Qué es un patrón de diseño?
• Es aplicar esa misma idea para diseñar software, en 
términos de objetos, clases e interfaces.
• Es una descripción de objetos y clases comunicándose 
entre sí, que se personalizan para resolver un problema 
general del diseño en un contexto particular.
• La descripción de la solución al problema general se 
realiza en términos de estructura (clases, interfaces, 
relaciones) y comportamiento (interacciones entre 
objetos).
• Típicamente contiene (al menos) 4 ítems: 
nombre, problema, solución y consecuencias.
7

Introducción (4)
 Nombre: 
• Se utiliza para aumentar el vocabulario del 
diseñador.
• Sólo con el nombre, se está haciendo referencia 
también al problema, la solución y las 
consecuencias.
• Esto permite diseñar a un mayor nivel de 
abstracción (simplemente diciendo, por ejemplo: 
“¿Por qué no utilizar State?”).
8

Introducción (5)
 Problema (Aplicabilidad):
• El problema describe cuándo aplicar el patrón.
• Explica el problema y su contexto.
• El problema puede ser de bajo nivel (ej: cómo 
representar algoritmos como objetos) o de más alto 
nivel (ej: cómo acceder a un subsistema).
• En ocasiones el problema presenta condiciones que 
deben ser cumplidas antes de aplicar el patrón.
• Entender el problema es tan importante como 
entender la solución, pues una buena solución a un 
problema incorrecto no sirve de nada.
9

Introducción (6)
 Solución :
• Describe los elementos que componen el diseño, sus 
relaciones, responsabilidades y colaboraciones.
• Se divide en estructura y comportamiento.
• La solución no describe un diseño particular y 
concreto, ya que un patrón es un template que puede 
ser aplicado en diferentes situaciones (todas 
comprendidas dentro del problema).
• El diseñador debe, a partir de su problema particular 
y cuando éste encaje dentro del problema general 
planteado por el patrón, tomar la solución general del 
patrón y personalizarla a su solución particular
10

Introducción (7)
 Solución (cont.)  :
11

Introducción (8)
 Consecuencias :
• Presenta el resultado y los trade-off de aplicar el 
patrón.
• Toda solución (incluso las buenas) tienen un “costo”.
• Dentro de las consecuencias también puede haber 
comentarios sobre lenguajes de programación o 
detalles de implementación, más allá del propio 
diseño.
• Se deben tener en cuenta las consecuencias de un 
patrón al momento de aplicarlo, particularmente si el 
“costo” de aplicarlo es demasiado alto frente a las 
ventajas que ofrece.
12

Introducción (9)
 Los patrones de diseño se pueden clasificar según su 
propósito:
• Patrones de Creación: Les concierne el proceso de 
creación de objetos.
• Patrones de Estructura: Les concierne la 
composición de clases y objetos.
• Patrones de Comportamiento: Les concierne la 
distribución de responsabilidades y detallan de 
qué forma interactuarán clases y objetos.
13

Introducción (10)
 Los patrones de diseño se pueden clasificar según su 
alcance:
• Patrones que aplican principalmente a Clases: 
Se centran en las relaciones entre clases y 
subclases, típicamente mediante herencia, por lo 
que son relaciones fijas (se fijan en tiempo de 
diseño).
• Patrones que aplican principalmente a Objetos: 
Se centran en las relaciones entre objetos, las 
cuales pueden cambiar dinámicamente (en tiempo 
de ejecución).
14

Introducción (11)
 Tener en cuenta que:
• La solución que un patrón presenta contiene aspectos tanto 
estructurales como de comportamiento.
• Particularmente no se debe olvidar (o despreciar) el 
comportamiento sugerido por la solución, pues éste indica cómo se 
utiliza la estructura.
• Esto resulta especialmente importante pues muchos patrones 
presentan estructuras similares en sus soluciones, lo cual sin un 
estudio de sus comportamientos llevará a la confusión entre ellos.
 Además, en muchos patrones es recurrente la utilización de:
• Herencia (o implementación de interfaces)
• Delegación
• Redefinición de operaciones
 Por lo que aún más las estructuras podrán parecer similares, siendo 
imprescindible estudiar el comportamiento sugerido para dichas 
estructuras.
15

Composite (1)
 Problema: ¿Cómo tratar objetos que pueden ser 
compuestos de otros objetos como si fueran objetos 
individuales?
 Aplicabilidad: 
• Representar jerarquías de objetos compuestos 
de otros objetos así como de objetos 
individuales.
• Los clientes ignoran las diferencias entre objetos 
individuales y objetos compuestos dentro de 
esa jerarquía y los manipulan indistintamente.
16

Composite (2)
 Estructura:
Cliente
Componente
+operacion()
+agregar(entrada c : Componente)
+eliminar(entrada c : Componente)
Hoja
*
hijos
Compuesto
+operacion()
foreach hijo in hijos:
 hijo.operacion()
+operacion()
+agregar(entrada c : Componente)
+eliminar(entrada c : Componente)
hijos.add(c)
1
hijos.remove(c)

17
Composite (3)
 Participantes: 
• Componente:
Abstrae los diferentes elementos de la jerarquía.
Declara una interfaz común para ellos.
Implementa comportamiento por defecto para todos 
ellos (si corresponde).
• Hoja:
Representa los elementos atómicos (sin hijos).
Define el comportamiento para los elementos 
primitivos de la composición.
18

Composite (4)
 Participantes (cont.) : 
• Compuesto:
Define el comportamiento para los componentes con 
hijos.
Almacena a sus hijos.
Permite el manejo de los hijos (agregar, eliminar, etc.)
• Cliente:
Manipula objetos de la composición a través de los 
servicios  brindados por Componente (ver 
Consecuencias)
19

Composite (5)
 Comportamiento:
20

Composite (6)
 Consecuencias:
• Fácil introducción de nuevos tipos de componentes 
sin modificar código cliente existente.
• Los clientes son sencillos: evitan lógica condicional en 
ellos y manipulan de igual forma los componentes.
• Generalidad vs. Control: el hecho que los 
componentes sean tratados genéricamente (lo cual es 
una ventaja para el cliente) también presenta una 
desventaja en cuanto a no poder controlar el tipo de 
elementos de un compuesto (ej: si se tienen dos tipos 
de hojas y se necesita que determinado elemento 
compuesto sólo tenga un tipo de hoja).
21

Composite (7)
 Consecuencias (cont.) :
• Transparencia vs. Seguridad: 
 Declarar las operaciones de manipulación de hijos en el 
super-tipo (Componente) brinda transparencia (y 
genericidad) pues los clientes, además de invocar las 
operaciones sin importar el tipo real del objeto, también 
pueden (intentar) agregar y eliminar elementos hijos.
 No obstante, no tiene sentido solicitar agregar/eliminar 
sobre una hoja (se ganó transparencia a costo de 
seguridad).
 Por lo tanto, se pueden colocar las operaciones de 
manipulación de hijos únicamente en el compuesto 
(ganando así seguridad pero perdiendo transparencia).
22

Proxy (1)
 Problema: ¿Cómo impedir el acceso directo a un objeto 
(es decir controlar su acceso)?
 Aplicabilidad: 
• Remote Proxy: Provee un representante local para 
un objeto que se encuentra en otra ubicación (ej: 
RMI).
• Virtual Proxy: Crea objetos “caros” a demanda (ej: 
manejo de imágenes de gran tamaño).
• Protection Proxy: Controla el acceso al objeto 
original (ej: chequeo de permisos sobre un recurso).
23

Proxy (2)
 Estructura:
Cliente
Subject
+operacion()
Proxy
objetoReal
+operacion()
1
RealSubject
+operacion()
objetoReal.operacion()
24

Proxy (3)
 Participantes: 
• Proxy: 
 Mantiene una referencia que le permite acceder al 
objeto original y realizar los controles necesarios, 
incluyendo (si es necesario) su creación y destrucción.
 Provee la misma interfaz (servicios) que el objeto real.
 Otras responsabilidades según la variante a utilizar:
 Remote Proxy: Codifica la solicitud a la operación 
(incluyendo sus parámetros) y la envía al objeto remoto 
original.
 Virtual Proxy: Cachea información para postponer su 
acceso.
 Protection Proxy: Verifica que el cliente posea los 
permisos adecuados para acceder al objeto original.
25

Proxy (4)
 Participantes (cont.) : 
• Subject: Define una interfaz (servicios) común al 
objeto original así como al Proxy, de manera que 
éste puede ser utilizado en lugar del objeto 
original.
• RealSubject: Es el objeto original o real al cual el 
Proxy representa.
26

Proxy (5)
 Comportamiento:
:Cliente
operacion()
:Subject
:Proxy
Dependiendo de la
variante utilizada
pueden aplicar 
condiciones u
otros controles y
acciones.
1: [cond] operacion()
objetoReal:RealSubject
27

Proxy (6)
 Consecuencias:
• Introduce un nivel de indirección, cuya utilidad depende de 
la variante utilizada:
 Remote Proxy: Oculta el hecho de que el objeto real se 
encuentra en una ubicación remota (así como el 
mecanismo de comunicación entre ambos).
 Virtual Proxy: Realiza optimizaciones, como crear un 
objeto a demanda en lugar de tenerlo instanciado 
siempre.
 Protection Proxy: Permite tareas de control y 
mantenimiento (incluso loggeo) cada vez que el objeto 
real es accedido.
• En los casos donde el Proxy no deba instanciar al objeto real, 
podría conocerlo a través de una interfaz.
28

Adapter (1)
 Problema: ¿Cómo hacer interactuar una clase ya creada 
con otra cuya interfaz (servicios) cambió?
 Aplicabilidad: 
• Si la clase A utiliza a la clase B y los servicios que 
brinda B cambian, A se verá afectada y también 
deberá cambiar, a menos que se introduzca una 
clase X que se adapte al uso de A pero conociendo la 
nueva B. 
Es decir que se pasa de  A  B  a  A  X  B
• Resolver incompatibilidad de interfaces.
29

Adapter (2)
 Estructura:
Cliente
Destino
+operacion()
Adapter
adaptado
ClaseDestino
+operacion()
adaptado.operacionDestino()
1
+operacionDestino()

30
Adapter (3)
 Participantes: 
• Destino: Define la interfaz (servicios) que el cliente 
necesita. También se le llama Target.
• Cliente: Utiliza objetos que conformen con Destino.
• ClaseDestino: Define una interfaz (servicios) 
existente que necesita ser adaptada para poder ser 
utilizada por los clientes.
• Adapter: Adapta la interfaz de ClaseDestino a la 
interfaz Destino para poder ser utilizada por los 
clientes.
31

Adapter (4)
 Comportamiento:
:Cliente
operacion()
:Adapter
:Destino
El Adapter puede
adaptar tanto el
nombre de la 
operación así 
como sus parámetros.
1: operacionDestino()
adaptado:ClaseDestino
32

Adapter (5)
 Consecuencias:
• Un adaptador puede cambiar su clase de destino 
dinámicamente (en tiempo de ejecución).
• Un adaptador puede desde simplemente adaptar el 
nombre de una operación hasta adaptar toda una 
interfaz completa, incluyendo los parámetros.
• Generalmente el objeto adaptado ya no puede ser 
utilizado mediante su vieja interfaz (a menos que el 
adapter también lo permita).
• Este patrón también es conocido como wrapper 
(“envoltorio”).
33

Template Method (1)
 Problema: Definir el esqueleto de un algoritmo en una 
operación, relegando algunos pasos a subclases. Las 
subclases redefinirán ciertos pasos del algoritmo sin 
cambiar su estructura.
 Aplicabilidad: 
• Implementar las partes invariantes de un algoritmo 
una única vez y delegar los pasos variables a 
subclases.
• Factorizar comportamiento común de subclases en 
una nueva clase abstracta.
34

Template Method (2)
 Estructura:
35

Template Method (3)
 Participantes: 
• ClaseAbstracta:
 Define primitivas abstractas que las subclases 
implementarán.
 Implementa el método template, conteniendo el 
esqueleto de un algoritmo. El método template invoca 
a las primitivas que son implementadas en las 
subclases, así como a otras operaciones de la clase 
abstracta u otras clases.
• ClaseConcreta:
 Implementa las operaciones primitivas definiendo su 
forma de implementar esos pasos del algoritmo para 
poder ser utilizada por los clientes.
36

Template Method (4)
 Comportamiento:
:Cliente
templateMethod()
oper1()
1: oper1()
2: oper2()
:ClaseAbstracta
:ClaseConcreta
oper2()
:ClaseConcreta
37

Template Method (5)
 Consecuencias:
• Es importante diferenciar aquellas operaciones utilizadas 
por el template method que deban ser redefinidas (que 
serán abstractas en la super clase) de las que puedan ser 
redefinidas (que serán concretas en la super clase, 
también llamadas hooks).
• El template method no debe ser redefinido.
• Cuantas más operaciones abstractas se definan en la 
clase abstracta, más trabajo deberán realizar las clases 
concretas.
38

Observer (1)
 Problema: Definir una dependencia “uno a muchos” entre 
objetos de tal forma que cuando el “uno” cambie, 
los “muchos” dependidos sean notificados.
 Aplicabilidad: 
• Cuando un elemento tiene dos aspectos, uno 
dependiente del otro, y encapsularlos en objetos 
diferentes permite modificarlos y reutilizarlos 
independientemente.
• Cuando cambios en un objeto requieran cambios en 
otros objetos, y no se sabe cuáles ni cuántos de éstos 
últimos serán.
• Cuando un objeto deba notificar a otros sin acoplarse a 
éstos.
39

Observer (2)
 Estructura:
Subject-estado interno
observers
«interfaz»
Observer
+attach(entrada o : Observer)
+dettach(entrada o : Observer)
+operacion()-notifyAll()
*
+notify()
ConcreteObserver1
+notify()
ConcreteObserver2
foreach o in observers:
    o.notify();
+notify()

40
Observer (3)
 Participantes: 
• Subject:
 Es el sujeto en observación, cuyo estado es de interés 
para los objetos observadores.
 Provee servicios de registro (attach) y des-registro 
(dettach) de observadores.
 Notifica a los observadores registrados de su cambio 
de estado (ej: cuando alguien invoca operacion()).
• Observer:
 Define una interfaz de notificación / actualización 
que los observadores deben implementar de forma de 
no acoplar el subject con los observers.
41

Observer (4)
 Participantes: 
• ConcreteObservers:
 Representan los observadores interesados en el 
estado del subject.
 Se registran frente al subject para que sus 
instancias sean efectivamente notificadas del 
cambio.
 Implementan la interfaz Observer de forma que 
no son conocidos por el subject, sino que 
únicamente son vistos como de tipo interfaz.
42

Observer (5)
 Comportamiento:
attach(o:Observer)
:ConcreteObserver1
:ConcreteObserver1
dettach(o:Observer)
1: add(o)
:Subject
:Observer
1: remove(o)
:Subject
:Observer

43
Observer (6)
 Comportamiento (cont.) :
1: notifyAll()
operacion()
1.2*: notify()
:Subject
1.1*: [foreach] o:= next()
:Observer
o:Observer

44
Observer (7)
 Consecuencias:
• El Subject puede separarse en dos: una clase abstracta 
Subject con operaciones de attach, dettach y notifyAll
(ya predefinidas) y una subclase ConcreteSubject que 
representa el tipo de objeto que será efectivamente 
observado.
• En la estructura se mostró que el Subject posee un 
método (operacion()) el cual desencadena el cambio 
de estado, por lo que deberá invocar a notifyAll() el 
cual fue declarado como privado. Sin embargo, no 
tienen por qué ser dos métodos diferentes.
45

Observer (8)
 Consecuencias:
• La operación notify() puede enviar parámetros que 
contengan información sobre el cambio ocurrido en el 
Subject.
• Generalmente son los propios observadores los que 
cambian el estado del Subject (en este caso, invocando 
operacion()).
• Para que un objeto sea notificado:
1. Su clase debe implementar  la interfaz Observer. 
2. El objeto debe registrarse ante el Subject (por 
ejemplo: sujeto.attach(this)).
46

State (1)
 Problema: Permitir a un objeto alterar su 
comportamiento cuando su estado interno cambie. El 
objeto parecerá haber cambiado de clase.
 Aplicabilidad: 
• Cuando el comportamiento de un objeto dependa de 
su estado y deba cambiar su comportamiento en 
tiempo de ejecución dependiendo de ese estado.
• Cuando las operaciones contengan sentencias 
condicionales que dependan del estado del objeto 
(representado típicamente por enumerados).
47

State (2)
 Estructura:
Cliente
Context
1
+pedido()
estado=estado.oper()
estado
Estado
1
+oper() : Estado
EstadoConcreto1
+oper() : Estado
EstadoConcreto2
+oper() : Estado
• Observación: este diagrama incluye decisiones sobre la lógica de 
cambio de estado, en particular, que la operación misma retorna el 
nuevo estado, el cual es creado por el estado actual (lo que introduce 
dependencias entre ambos estados concretos). Existen otras 
alternativas. Ver Comportamiento y Consecuencias.
48

State (3)
 Participantes: 
• Context: 
 Representa al objeto que cambiará su estado.
 Define la interfaz que utilizarán los clientes.
 Mantiene una instancia de EstadoConcreto como el 
estado actual.
• Estado:
 Define una interfaz para encapsular los diferentes 
estados.
• EstadoConcreto:
 Implementa un comportamiento asociado con un 
estado del Context.
49

State (4)
 Comportamiento:
pedido()
:Cliente
1: oper()
:Context
:Estado
:EstadoConcretoX
• Aquí no se muestra cómo se produce el cambio de 
estado (ej: cómo se pasa de EstadoConcreto1 a 
EstadoConcreto2).
• Una alternativa es que oper() realice las actividades 
específicas a su estado y retorne el nuevo estado, como 
muestra el siguiente Diagrama de Comunicación...
50

State (5)
 Comportamiento (cont.) :
2: setEstado(nuevo)
pedido()
:Cliente
:Context
1: nuevo:=oper():Estado
:Estado
:EstadoConcreto1
1.1: create()
nuevo:EstadoConcreto2

51
State (6)
 Consecuencias:
• El patrón State representa el estado como un objeto 
por sí mismo, con una subclase por cada estado 
posible del objeto.
• Los cambios de estado pueden ser manejados ya sea 
por los propios estados (como indicó el diagrama 
anterior) o bien por el Context.
• Si los cambios los manejan los propios estados, 
entonces el Diagrama de Clases debe mostrar las 
dependencias entre estados que correspondan 
(como lo indica el diagrama de clases anterior).
52

State (7)
 Consecuencias:
• El Context puede enviar información mediante 
parámetros de oper() o bien enviarse a sí mismo 
para que los estados puedan consultar información 
(todo esto en caso de ser necesario).
• El patrón State puede combinarse con Singleton
para hacer que los estados concretos tengan una 
única instancia. Esto es aplicable siempre que no 
existan muchas instancias del Context y que cada 
una necesite diferente información para el mismo 
estado concreto (pues todas ellas compartirían la 
instancia Singleton).
53

State (8)
 Consecuencias:
• Agregar nuevos tipos de estados concretos tiene un 
bajo impacto, pues únicamente implica que alguien 
debe devolver ese nuevo estado concreto (ej: otro 
estado concreto). 
• Se puede utilizar un Diagrama de Estados para 
representar (analizar, discutir) cómo es la lógica de 
cambio de estado del objeto.
• En caso de no ser apropiado que oper() retorne el 
nuevo estado (ej: porque se necesita que retorne 
otra cosa) entonces el Context puede proveer una 
operación pública de cambio de estado).
54

Strategy (1)
 Problema: Definir una familia de algoritmos, 
encapsular cada uno de ellos en una clase, y hacerlos 
intercambiables. Strategy permite variar el algoritmo 
independientemente de los clientes que lo utilicen.
 Aplicabilidad: 
• Cuando muchas clases relacionadas difieran sólo en 
su comportamiento.
• Cuando necesite diferentes variantes de un 
algoritmo.
• Cuando una clase contenga diferentes 
comportamientos mediante sentencias condicionales.
55

Strategy (2)
 Estructura:
Cliente
Context
estrategia.algoritmo()
estrategia
1
+pedido()
Estrategia
1
+algoritmo()
EstrategiaConcreta1
+algoritmo()
EstrategiaConcreta2
+algoritmo()

56
Strategy (3)
 Participantes: 
• Estrategia:
 Define una interfaz común a todos los algoritmos 
soportados. Contexto utiliza esta interfaz para invocar al 
algoritmo definido por alguna estrategia concreta.
• EstrategiaConcreta:
 Implementa una versión del algoritmo.
• Contexto:
 Se configura con una estrategia concreta (típicamente el 
cliente instancia al contexto con la estrategia concreta a 
utilizar).
 Mantiene una referencia a la estrategia actual y puede 
proveer operaciones para que éstas accedan a sus datos.
57

Strategy (4)
 Comportamiento:
2: create(ec1)
3: pedido
:Cliente
1: create()
ec1:EstrategiaConcreta1
3.1: algoritmo()
:Estrategia
:Context

58
Strategy (5)
 Consecuencias:
• El Context puede enviar información mediante 
parámetros o bien enviarse a sí mismo para que las 
estrategias concretas puedan consultar información 
(todo esto en caso de ser necesario).
• El Cliente tiene a su disposición una familia de 
algoritmos (estrategias concretas) de la cual elegir 
una para crear el Context, luego de lo cual el 
Cliente sólo interactuará con éste.
• La estrategia concreta puede cambiarse 
dinámicamente (en tiempo de ejecución).
59

Strategy (6)
 Consecuencias:
• El Cliente conoce las estrategias concretas y 
selecciona una para su utilización (por tanto queda 
acoplado a éstas). Esto significa que Strategy debe 
utilizarse cuando este acoplamiento sea aceptable.
• Las estrategias concretas pueden ser Singleton y ser 
compartidas por todos los Context.
• Opcionalmente, el Context puede contener una 
implementación por defecto del algoritmo, con lo 
que permitiría su uso aún sin haber creado ninguna 
estrategia concreta (lo cual libera al Cliente de la 
responsabilidad de elegir)
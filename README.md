# fundamentos_python_control_fun

Este repositorio contiene ejercicios de Python organizados por temas: `condicionales`, `funciones` e `iterativos`.

## Requisitos

- Python 3 instalado en el sistema.
- Usar la terminal o consola desde la carpeta raíz del proyecto.

## Cómo ejecutar un ejercicio

Cada archivo Python corresponde a un ejercicio. Para ejecutarlo, abre una terminal en la carpeta raíz del proyecto y usa el siguiente comando:

```powershell
python src/<categoria>/<archivo>.py
```

Por ejemplo:

```powershell
python src/condicionales/edad.py
python src/funciones/SaludarReturn.py
python src/iterativos/BucleForAnidado.py
```

Si tu sistema usa `python3` para Python 3, usa ese comando en lugar de `python`.

## Ejecución paso a paso

1. Abre la terminal o PowerShell.
2. Navega a la carpeta raíz del proyecto:

```powershell
cd c:\Users\uiehc\fundamentos_python_control_fun
```

3. Ejecuta el archivo deseado con Python:

```powershell
python src/condicionales/numero.py
```

## Ejercicios de condicionales

- `AccesoRegister.py`: muestra el uso de `or` para conceder acceso si el usuario está registrado o tiene acceso permitido.
- `AccesoRegister2.py`: ejemplo de `if` simple para permitir entrada.
- `AccesoRegister3.py`: combinación de `or` y `and` en condiciones de autorización.
- `color.py`: compara una variable `color` con un valor esperado.
- `contraseña.py`: solicita una contraseña con `input()` y la evalúa.
- `DiaOr.py`: usa `or` para detectar si es fin de semana.
- `edad.py`: revisa si una edad cumple una condición básica.
- `EdadAnd.py`: usa `and` para validar dos condiciones simultáneamente.
- `EdadAnidada.py`: demuestra un `if` anidado.
- `EdadAnidada2.py`: valida permiso parental con `if` anidados.
- `EdadAnidada3.py`: otra versión con `if` anidados y permisos.
- `EdadCombinacion.py`: combina `or` y `and` para decidir si obtener una licencia.
- `EdadElif.py`: usa `if`, `elif` y `else` para clasificar según la edad.
- `EdadElse.py`: muestra la rama `else` para votar o no.
- `EdadEvaluar.py`: utiliza una expresión condicional anidada (`ternaria`) para asignar una categoría de edad.
- `EdadMach.py`: usa `match` para evaluar la edad.
- `EdadTernaria.py`: usa una expresión ternaria para imprimir si es mayor de edad.
- `ExpresionCondicional.py`: muestra `a if a > b else b` para obtener el mayor valor.
- `FrutaMach.py`: pide una fruta y usa `match` para identificarla.
- `LlueveNot.py`: usa `not` para decidir si se puede salir al parque.
- `nota.py`: evalúa una nota con condicionales.
- `numero.py`: verifica si un número es positivo, negativo o cero.
- `NumeroElif.py`: clasifica un número con `if`, `elif` y `else`.
- `NumerosListados.py`: crea una lista de paridad usando list comprehension y condicional.
- `NumerosListados2.py`: usa una expresión condicional para evitar división por cero.
- `NumerosListados3.py`: valida un divisor antes de dividir y comprueba resultado.
- `NumerosMach.py`: usa `match` en una lista para detectar si está vacía.
- `Numeros_All.py`: muestra el uso de `all()` para validar condiciones.
- `Numeros_Any.py`: muestra el uso de `any()` para detectar valores verdaderos.
- `PrecedenciaResultado.py`: demuestra la precedencia de operadores lógicos.
- `Precedencia_operadores.py`: otro ejemplo de cómo evalúan `and`, `or` y `not`.
- `PrevenirError.py`: evita un error de índice accediendo primero a la longitud de la lista.
- `PuntoMach.py`: usa `match` para reconocer un punto en el origen.
- `UsuarioAnidado.py`: valida usuario y contraseña con `if` anidados.
- `UsuariosComplejoIf.py`: ejemplo de doble verificación de credenciales.
- `UsuariosMach.py`: usa `match` para evaluar estructuras de usuario.
- `VariableMayor.py`: compara tres valores para encontrar el mayor.
- `VariableMayor2.py`: versión alternativa de comparación de valores.
- `hora.py`: evalúa una hora para determinar un mensaje.
- `saldo.py`: muestra decisiones basadas en un saldo disponible.
- `temperatura.py`: evalúa la temperatura y selecciona un mensaje.

## Ejercicios de funciones

- `AccederDocstrings.py`: demuestra cómo acceder a la documentación (`docstring`) de una función.
- `AsignarFuncionVariable.py`: asigna una función a una variable y la llama.
- `Buena_PracticaContarPalabras.py`: define una función para contar palabras en un texto.
- `Buena_PracticaFomatearNombre.py`: formatea nombre y apellido.
- `Buena_PracticaObtenerElemento.py`: obtiene un elemento de una lista con validación.
- `Buena_PracticaValidar.py`: muestra buenas prácticas para validar datos antes de usarlos.
- `BuenasPracticasContraseña.py`: genera una contraseña segura con un parámetro opcional.
- `CalcularAreaRectangulo.py`: calcula el área de un rectángulo.
- `CalcularDescuento.py`: calcula un descuento en base a un precio y porcentaje.
- `CalcularDescuentoValidacion.py`: calcula un descuento con validación adicional.
- `CalcularPagoCombinandoParametros.py`: calcula el pago usando parámetros posicionales y valores predeterminados.
- `CalcularParemetroPosicionales.py`: muestra cómo usar parámetros posicionales en funciones.
- `CalcularPrecioIvaProcesamiento.py`: calcula el precio con IVA.
- `CalcularPromedioDocstring.py`: calcula el promedio de una lista y documenta la función.
- `Calcular_Documentar_practica.py`: documenta cómo calcular un descuento correctamente.
- `Calcular_Evitar_Efectos_Secundarios.py`: muestra la buena práctica de separar cálculo y presentación.
- `CalculasCuadradoReturn.py`: devuelve el cuadrado de un número.
- `Calificacion_Return_CasoEspecial.py`: devuelve una calificación basada en puntuación.
- `CrearPerfilValorPredeterminado.py`: crea un perfil usando valores predeterminados.
- `CrearUsuarioParametros.py`: crea un usuario con parámetros y valores opcionales.
- `DividirParametroNombre.py`: divide dos números y muestra manejo de parámetros nombrados.
- `DividirReturnAnticipado.py`: usa `return` anticipado para validar una división segura.
- `DocstringComplejo.py`: ejemplo de docstring detallado para funciones más complejas.
- `DocstringComportamientoEspecial.py`: documenta comportamiento especial de la función.
- `DocstringsFuncionSimple.py`: docstring para una función sencilla.
- `EjemploPracticoTemperatura.py`: convierte temperaturas entre unidades.
- `EstadisticasMultiplesValores.py`: calcula estadísticas básicas de una lista de números.
- `EstiloDocstrings_Google.py`: muestra el estilo de docstrings de Google.
- `Estilo_NumPy_Scipy.py`: muestra estilo de docstrings similar a NumPy/SciPy.
- `Estilo_reStructuredText.py`: muestra docstrings en formato reStructuredText.
- `FiltrarPositivosReturn_Practica.py`: devuelve solo valores positivos de una lista.
- `FuncionDocstringCompleto.py`: define y documenta una función completa.
- `FuncionFormatearTexto.py`: formatea texto con opciones de mayúsculas y prefijos/sufijos.
- `HerramientasDocstrings.py`: muestra cómo documentar funciones utilitarias.
- `MayorEdadBooleana.py`: devuelve un valor booleano si es mayor de edad.
- `NombreVariable_kwargs.py`: usa `**kwargs` para mostrar información variable.
- `ReturnEstructuraDatos.py`: devuelve una estructura de datos (lista de pares).
- `SaludarReturn.py`: devuelve un saludo personalizado.
- `SaludoParametroArgumento.py`: demuestra parámetros y argumentos en una función.
- `SaludoParametroValor.py`: usa un parámetro con valor predeterminado para saludar.
- `SumaArgumentoPosicional_args.py`: suma un número variable de argumentos con `*args`.
- `SumaDockstrings.py`: suma dos valores y documenta la función.
- `TransformacionDatos.py`: transforma nombre y apellido en formato específico.
- `VerificarNumero.py`: verifica si un número es par.

## Ejercicios de iterativos

- `BucleAnidado.py`: muestra un bucle `for` anidado.
- `BucleErrorInfinito.py`: advierte sobre un bucle infinito mal construido.
- `BucleForAnidado.py`: genera una tabla multiplicativa con bucles anidados.
- `BucleInfinito.py`: ejemplo de `while True` que puede no terminar.
- `BuclesWhile.py`: ejemplo básico de bucle `while`.
- `BuscarElementoBreak.py`: busca un elemento en una lista y usa `break`.
- `BusquedaElse.py`: usa `else` junto a un bucle `for`.
- `CadenasIterando.py`: itera cada carácter de una cadena.
- `CalcularNumerosFor_Range.py`: calcula valores usando `for` y `range()`.
- `ClausulaElseBucle.py`: muestra la cláusula `else` en bucles.
- `CombinandoBreakContinue.py`: usa `break` y `continue` en el mismo bucle.
- `CombinandoPassElse.py`: usa `pass` y `else` en un bucle.
- `ComparacionBuclesWhile.py`: compara patrones de bucles `while`.
- `ComprensionFor.py`: muestra una comprensión de lista con `for`.
- `ConsideracionEstiloLegibilidad.py`: ejemplo con comentarios y estilo legible.
- `ContadorBucleWhy.py`: cuenta con `while`.
- `DebugPass.py`: usa `pass` como marcador en el código.
- `DiccionariosIterando.py`: itera sobre las claves y valores de un diccionario.
- `DiccionariosIterando2.py`: otro ejemplo de iterar diccionarios.
- `EncontradoBucleAnidado.py`: busca un elemento en bucles anidados.
- `EncontrarNumerosFor_Range.py`: busca números primos con `for` y `range()`.
- `EntradaWhile.py`: solicita entrada del usuario dentro de un `while`.
- `EventosWhile.py`: genera eventos aleatorios en un bucle.
- `FiltradoDatosContinue.py`: filtra datos usando `continue`.
- `FrutaBucleFor.py`: recorre una lista de frutas.
- `IndicesRange.py`: usa índices con `range()` para iterar una lista.
- `IndicesRange2.py`: otra versión del uso de índices y `range()`.
- `ManejoNumerosContinue.py`: demuestra el uso de `continue` con números.
- `NumeroPrimoElse.py`: usa `else` en un bucle para detectar primos.
- `NumeroSentenciaBreak.py`: usa `break` para detener un bucle antes de tiempo.
- `NumerosElse.py`: busca un número primo y usa `else` si no se encuentra.
- `NumerosPassBucle.py`: ejemplo de `pass` dentro de un bucle.
- `OptimizacionAlgoritmos.py`: presenta una función para optimizar la búsqueda de primos.
- `PatronesWhile.py`: imprime un patrón con un bucle `while`.
- `ProcesamientoDatosFor_Range.py`: procesa una lista de temperaturas con `for` y `range()`.
- `ProcesamientoTransacciones.py`: itera sobre transacciones para analizarlas.
- `ProcesarDatosWhile.py`: usa `while` para calcular el factorial.
- `Range.py`: ejemplo básico de `range()`.
- `SaldoBucle.py`: recorre y evalúa un saldo en un bucle.
- `SentenciaContinue.py`: usa `continue` para saltar iteraciones.
- `SimulacionAproxWhile.py`: simula una aproximación con `while`.
- `SistemaValidacion.py`: valida datos de un formulario en un bucle.
- `UsoBuclesWhile.py`: usa `while` para encontrar una raíz con iteraciones limitadas.
- `ValidacionBreak.py`: usa `break` dentro de `while`.
- `ValidacionContraseña.py`: valida una contraseña con una función.
- `ValidacionElse.py`: valida una lista de edades usando `else`.
- `ValidacionEntradaWhile.py`: pide un número válido en un rango usando `while`.
- `ValidarDatos.py`: filtra valores válidos de una lista de cadenas.

## Consejos

- Ejecuta un ejercicio a la vez para entender su salida.
- Si un archivo usa `input()`, escribe la información directamente en la terminal.
- Para listar archivos en una carpeta puedes usar:

```powershell
Get-ChildItem src\condicionales
Get-ChildItem src\funciones
Get-ChildItem src\iterativos
```

- Si quieres ver el contenido de un ejercicio, ábrelo en el editor o con una herramienta de lectura de texto.


Este repositorio contiene ejercicios de Python organizados por temas: condicionales, funciones e iterativos.

## Requisitos

- Python 3 instalado en el sistema.
- Usar la terminal o consola desde la carpeta raíz del proyecto.

## Estructura del proyecto

- `src/condicionales/`: ejercicios de condicionales y estructuras de decisión.
- `src/funciones/`: ejercicios sobre definición y uso de funciones.
- `src/iterativos/`: ejercicios con bucles e iteraciones.

## Cómo ejecutar un ejercicio

Cada archivo Python corresponde a un ejercicio. Para ejecutarlo, abre una terminal en la carpeta raíz del proyecto y usa el siguiente comando:

```powershell
python src/<categoria>/<archivo>.py
```

Por ejemplo:

```powershell
python src/condicionales/edad.py
python src/funciones/SaludarReturn.py
python src/iterativos/NombreDelArchivo.py
```

## Ejecución paso a paso

1. Abre la terminal o PowerShell.
2. Navega a la carpeta raíz del proyecto:

```powershell
cd c:\Users\uiehc\fundamentos_python_control_fun
```

3. Ejecuta el archivo deseado con Python:

```powershell
python src/condicionales/numero.py
```

## Notas

- Si el archivo solicita datos con `input()`, deberás ingresar los valores directamente en la terminal.
- Puedes explorar los nombres de los archivos dentro de cada carpeta para elegir el ejercicio que quieres correr.
- Si tienes varias versiones de Python, usa `python3` en lugar de `python` si es necesario.

## Consejos

- Para ver los archivos de una carpeta desde la terminal puedes usar:

```powershell
Get-ChildItem src\condicionales
Get-ChildItem src\funciones
Get-ChildItem src\iterativos
```

- Ejecuta un ejercicio a la vez para revisar su salida y comportamiento.

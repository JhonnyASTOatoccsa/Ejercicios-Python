# REPASO PYTHON

## 1.TIPOS DE DATOS

 * *TIPOS DE DATOS PRIMITIVOS* 
 * *'a' -->string cadena de texto*
 * *'hola' -->esto tambien es un string*
 * *'hola' --> soy un strig y te saludo' # cadena larga*


>#### OBSERVACIÓN: todo lo que este entre comillas es un string 
>* *'100'*,
>*'false'*,
>*'hola'*.

>### Un string puede estar entre comillas simples o dobles 
>
>* *100 -->etse es un tipo de dato númerico entero* 
>* *2.1 --> este es un tipo de dato numerioc flotante*
>* *False --> este es un tipo de dato boleano falso* 
>* *true -->tipo de dato boleano verdadero*


## 2. VARIABLES
 
* *Es donde almacenamos nuestros tipos de datos.*
* *Esos datos pueden mutar o ccambiar o modificarse.*
* *Como creamos una variable para almacenar nuestros datos.*
* *1.Darle un nombre significante o realacionado al dato que estamos almacenando.*
* *2. Indicarle a que dato esta relacionado -> asignacion*
* *3. indicar el tipo de dato que va a almcenar -> darle el dato a guardar*
* *primero el dato voy a pedir la edad de nadine* 
```python
edad_nadine=18 
```


## 3.OPERADORES
###  *Operadores aritmetricos*
*suma*,*resta*,
*multiplicacion*,*division*.
#### *suma=45+12* 
#### *resta=45-12*
#### *multiplicacion=45 * 2*
#### *division=45/5*
```python
operacion=(45+12+23)/4
op=15+12+14/4
```
### Operadores de Presedencia
* suma=45+42   *operador suma resulatado 87*
* suma='45'+12 *operador concatenacion resultado 4512*
* saludo ='hola'+'+mundo' *concatenacion holamundo*
* saludo2='hola'+''+'mundo' *concatenar hola mundo*
* saludos='hola'* 2  *holahola*


## 4.DATOS ESTRUCTURADOS
#### Listas
* *Puede alamcenar distintos tipos de datos en una sola lista* 
```python
     ['nombre',10,False]
     lista_amigos=['jori','edwin','adan','chinita']
```
#### Objetos
* *tambien al igual que las listas almacenan distintos tipos de datos pero son un orden*
* *para almacenar datos en un objeto necesitamos especificar un inidce y un valor clave->valor*
```python
alumno={
    'nombre':'jori'
    'edad':52',
    'sexo':'todos los dias'
```
#### Combinar ambas estructuras de datos 
``` python
alumno={
    'nombre' : 'jori'
    'edad':30,
    'amigos':['antony','edwin','china']
'direccion': {
    'departamento':'ayacucho'
    'provincia':'lucanas'
    'distrito':'puquio'
    'jiron':'san peter'
    'numero':152 
 }
}
```
## 5. funciones
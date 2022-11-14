
## Resolcuion de los ejercicios planteados en la unidad 18 - Bases de datos NO-SQL

Utilizando los conceptos aprendidos en el módulo 18- Bases de datos
no relacionales, se pide resolver los siguientes puntos:

 1.  Instalar MongoDB y Compass
 2. Acceder desde compass y crear una base de datos
 3. Acceder a MongoDB desde PowerShell
 4. Acceder a la base de datos del paso 2
 5. Crear dos colecciones
 6. Insertar 1 documentos
 7. Insertar varios documentos con un solo comando
 8. Listar los documentos existentes en una colección
 9. Listar un documento específico dentro de la colección
 10. Realizar un update en un registro 
 11. Realizar un update a varios registros de forma simultánea

  

# Instalacion de mongo :

antes de inicar a resolver los ejercicios planteados, es necesario preparar el entorno de trabajo de mongo-db, para poder realizarlo de forma repizada utilizaremos docker  

    Comandos : 
    
	docker run -d -p 27017:27017 --name mongo mongo
    
![enter image description here](https://raw.githubusercontent.com/ricardolujan991/alkemy/main/UNIDAD-18-NO-SQL/img/1.png)

DOCS : https://hub.docker.com/_/mongo


 # Resolucion de ejercicios :

## 1.  Instalar MongoDB y Compass
 
	comandos para instalar en ubuntu :
	
    wget https://downloads.mongodb.com/compass/mongodb-compass_1.33.1_amd64.deb
    sudo dpkg -i mongodb-compass_1.33.1_amd64.deb
    mongodb-compass
DOCS : https://www.mongodb.com/docs/compass/current/install/

## 2. Acceder desde compass y crear una base de datos

Pagina de inicio compass

![Pagina de inicio compass](https://raw.githubusercontent.com/ricardolujan991/alkemy/main/UNIDAD-18-NO-SQL/img/2.png)

se crea la base de datos
![enter image description here](https://raw.githubusercontent.com/ricardolujan991/alkemy/main/UNIDAD-18-NO-SQL/img/3.png)

Se comprueba que la base de datos se creo correctamente
![enter image description here](https://raw.githubusercontent.com/ricardolujan991/alkemy/main/UNIDAD-18-NO-SQL/img/4.png)

## 3. Acceder a MongoDB desde PowerShell

Para poder iniciar la interfaz de shell de mongo db en docker es necesario ejecutar el sigueinte comadno:

    sudo docker exec -it <image_name> mongosh

![enter image description here](https://raw.githubusercontent.com/ricardolujan991/alkemy/main/UNIDAD-18-NO-SQL/img/5.png)
## 4. Acceder a la base de datos del paso 2
comando para visualizar las db existentes y selecionar una para trabajar :

    shows dbs
    use practica-no-sql

![enter image description here](https://raw.githubusercontent.com/ricardolujan991/alkemy/main/UNIDAD-18-NO-SQL/img/7.png)
## 5. Crear dos colecciones

comandos para crear colecciones : 

    db.createCollection("<collection-name>")

![enter image description here](https://raw.githubusercontent.com/ricardolujan991/alkemy/main/UNIDAD-18-NO-SQL/img/8.png)
 ## 6. Insertar 1 documentos
Comando para insertar documento : 

    db.getCollection('<collection-name>').insertOne({key1: value1, key2:value2})


![enter image description here](https://raw.githubusercontent.com/ricardolujan991/alkemy/main/UNIDAD-18-NO-SQL/img/9.png)
 ## 7. Insertar varios documentos con un solo comando
Comando para insertar varios documentos : 

    db.getCollection('<collection-name>').insertMany([{key_1_doc_1 : value_1_doc_1, key_2_doc_1 : value_2_doc_1},{key_1_doc_2 : value_1_doc_2, key_2_doc_2 : value_2_doc_2}])


![enter image description here](https://raw.githubusercontent.com/ricardolujan991/alkemy/main/UNIDAD-18-NO-SQL/img/10.png)

 ## 8. Listar los documentos existentes en una colección

comando para visulaizar todos los documentos de una coleccion 

    db.getCollection('<collection-name>').find()

![enter image description here](https://raw.githubusercontent.com/ricardolujan991/alkemy/main/UNIDAD-18-NO-SQL/img/11.png)
 ## 9. Listar un documento específico dentro de la colección
 Comando para visualizar un documento especifico : 
 
comando para vizualizar documentos con un basados en un criterio de busqueda

     db.getCollection('<collection-name>').find({"key:value})

![enter image description here](https://raw.githubusercontent.com/ricardolujan991/alkemy/main/UNIDAD-18-NO-SQL/img/12.png)

## 10. Realizar un update en un registro 
Comando para actualizar un documento : 

     db.getCollection('<collection-name>').updateOne({key_criterion_to_update: value_criterion_to_update}, {$set:{key_to_update : new_value} }


![enter image description here](https://raw.githubusercontent.com/ricardolujan991/alkemy/main/UNIDAD-18-NO-SQL/img/13.png)
 ## 11. Realizar un update a varios registros de forma simultánea
comando para actualizar varios documentos dado 

     db.getCollection('<collection-name>').updateMany({}, {$set: {key_update: value_update}})


![enter image description here](https://raw.githubusercontent.com/ricardolujan991/alkemy/main/UNIDAD-18-NO-SQL/img/14.png)

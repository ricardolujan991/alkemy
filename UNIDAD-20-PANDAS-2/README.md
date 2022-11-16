# UNIDAD 20 - PANDAS 2 

Utilizando los conceptos aprendidos en el módulo 20 - Datos con
Pandas II, resolver el siguiente ejercicio.

Desarrollar una aplicación que realice la siguientes tareas:

1. Conectarse a la [url](http://winterolympicsmedals.com/medals.csv) que contiene el archivo CSV de medallas
2. Descargar los datos y obtener un sub dataset que contenga a
todas las medallas de oro (Gold) Estados Unidos (USA) a partir del
año 1950.
3. Crear una base de datos “olympics” en SQLite y la tabla “medals”.
4. Guardar en la base de datos. los datos generados en el sub
dataset.
5. Consultar la base de datos y validar que los datos se hayan
cargado correctamente.

---

1. Conectarse a la [url](http://winterolympicsmedals.com/medals.csv) que contiene el archivo CSV de medallas


```python
import pandas as pd 

url_csv_medallas = 'http://winterolympicsmedals.com/medals.csv'

df_medallas = pd.read_csv(url_csv_medallas)

df_medallas
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>City</th>
      <th>Sport</th>
      <th>Discipline</th>
      <th>NOC</th>
      <th>Event</th>
      <th>Event gender</th>
      <th>Medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1924</td>
      <td>Chamonix</td>
      <td>Skating</td>
      <td>Figure skating</td>
      <td>AUT</td>
      <td>individual</td>
      <td>M</td>
      <td>Silver</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1924</td>
      <td>Chamonix</td>
      <td>Skating</td>
      <td>Figure skating</td>
      <td>AUT</td>
      <td>individual</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1924</td>
      <td>Chamonix</td>
      <td>Skating</td>
      <td>Figure skating</td>
      <td>AUT</td>
      <td>pairs</td>
      <td>X</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1924</td>
      <td>Chamonix</td>
      <td>Bobsleigh</td>
      <td>Bobsleigh</td>
      <td>BEL</td>
      <td>four-man</td>
      <td>M</td>
      <td>Bronze</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1924</td>
      <td>Chamonix</td>
      <td>Ice Hockey</td>
      <td>Ice Hockey</td>
      <td>CAN</td>
      <td>ice hockey</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2306</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Snowboard</td>
      <td>USA</td>
      <td>Half-pipe</td>
      <td>M</td>
      <td>Silver</td>
    </tr>
    <tr>
      <th>2307</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Snowboard</td>
      <td>USA</td>
      <td>Half-pipe</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2308</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Snowboard</td>
      <td>USA</td>
      <td>Half-pipe</td>
      <td>W</td>
      <td>Silver</td>
    </tr>
    <tr>
      <th>2309</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Snowboard</td>
      <td>USA</td>
      <td>Snowboard Cross</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2310</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Snowboard</td>
      <td>USA</td>
      <td>Snowboard Cross</td>
      <td>W</td>
      <td>Silver</td>
    </tr>
  </tbody>
</table>
<p>2311 rows × 8 columns</p>
</div>



---

2. Descargar los datos y obtener un sub dataset que contenga a
todas las medallas de oro (Gold) Estados Unidos (USA) a partir del
año 1950.


```python
df_medallas_desde_1950 = df_medallas[(df_medallas['Medal'] == 'Gold') 
                         & (df_medallas['Year'] >= 1950)]
                         
df_medallas_desde_1950
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>City</th>
      <th>Sport</th>
      <th>Discipline</th>
      <th>NOC</th>
      <th>Event</th>
      <th>Event gender</th>
      <th>Medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>254</th>
      <td>1952</td>
      <td>Oslo</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>AUT</td>
      <td>downhill</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>258</th>
      <td>1952</td>
      <td>Oslo</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>AUT</td>
      <td>slalom</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>259</th>
      <td>1952</td>
      <td>Oslo</td>
      <td>Ice Hockey</td>
      <td>Ice Hockey</td>
      <td>CAN</td>
      <td>ice hockey</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>262</th>
      <td>1952</td>
      <td>Oslo</td>
      <td>Skiing</td>
      <td>Cross Country S</td>
      <td>FIN</td>
      <td>10km</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>266</th>
      <td>1952</td>
      <td>Oslo</td>
      <td>Skiing</td>
      <td>Cross Country S</td>
      <td>FIN</td>
      <td>4x10km relay</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2301</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>USA</td>
      <td>Alpine combined</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2302</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>USA</td>
      <td>giant slalom</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2305</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Snowboard</td>
      <td>USA</td>
      <td>Half-pipe</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2307</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Snowboard</td>
      <td>USA</td>
      <td>Half-pipe</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2309</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Snowboard</td>
      <td>USA</td>
      <td>Snowboard Cross</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
  </tbody>
</table>
<p>691 rows × 8 columns</p>
</div>



---

3. Crear una base de datos “olympics” en SQLite y la tabla “medals”.


```python
import sqlite3

conexion = sqlite3.connect("olympics.db")

query_create_table = """ CREATE TABLE IF NOT EXISTS medals(
                            id integer primary key autoincrement,
                            Year int,	
                            City text,	
                            Sport text,	
                            Discipline text,	
                            NOC text,	
                            Event text,	
                            'Event gender' text,	
                            Medal text    
                        )
                     """
conexion.execute(query_create_table)


```




    <sqlite3.Cursor at 0x7f9d487b75c0>



---

4. Guardar en la base de datos. los datos generados en el sub
dataset.


```python
df_medallas_desde_1950.to_sql('medals', con=conexion, if_exists='replace', index=False)
```




    691



---

5. Consultar la base de datos y validar que los datos se hayan
cargado correctamente.


```python
df = pd.read_sql_query('SELECT * FROM medals', con=conexion)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>City</th>
      <th>Sport</th>
      <th>Discipline</th>
      <th>NOC</th>
      <th>Event</th>
      <th>Event gender</th>
      <th>Medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1952</td>
      <td>Oslo</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>AUT</td>
      <td>downhill</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1952</td>
      <td>Oslo</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>AUT</td>
      <td>slalom</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1952</td>
      <td>Oslo</td>
      <td>Ice Hockey</td>
      <td>Ice Hockey</td>
      <td>CAN</td>
      <td>ice hockey</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1952</td>
      <td>Oslo</td>
      <td>Skiing</td>
      <td>Cross Country S</td>
      <td>FIN</td>
      <td>10km</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1952</td>
      <td>Oslo</td>
      <td>Skiing</td>
      <td>Cross Country S</td>
      <td>FIN</td>
      <td>4x10km relay</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>686</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>USA</td>
      <td>Alpine combined</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>687</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>USA</td>
      <td>giant slalom</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>688</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Snowboard</td>
      <td>USA</td>
      <td>Half-pipe</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>689</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Snowboard</td>
      <td>USA</td>
      <td>Half-pipe</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>690</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Snowboard</td>
      <td>USA</td>
      <td>Snowboard Cross</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
  </tbody>
</table>
<p>691 rows × 8 columns</p>
</div>



---

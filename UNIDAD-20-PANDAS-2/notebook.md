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
                         & (df_medallas['Year'] >= 1950) 
                         & (df_medallas['NOC'] == 'CAN')]
                         
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
      <th>398</th>
      <td>1960</td>
      <td>Squaw Valley</td>
      <td>Skating</td>
      <td>Figure skating</td>
      <td>CAN</td>
      <td>pairs</td>
      <td>X</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>399</th>
      <td>1960</td>
      <td>Squaw Valley</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>CAN</td>
      <td>slalom</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>483</th>
      <td>1964</td>
      <td>Innsbruck</td>
      <td>Bobsleigh</td>
      <td>Bobsleigh</td>
      <td>CAN</td>
      <td>four-man</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>586</th>
      <td>1968</td>
      <td>Grenoble</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>CAN</td>
      <td>giant slalom</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>793</th>
      <td>1976</td>
      <td>Innsbruck</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>CAN</td>
      <td>giant slalom</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1013</th>
      <td>1984</td>
      <td>Sarajevo</td>
      <td>Skating</td>
      <td>Speed skating</td>
      <td>CAN</td>
      <td>1000m</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1014</th>
      <td>1984</td>
      <td>Sarajevo</td>
      <td>Skating</td>
      <td>Speed skating</td>
      <td>CAN</td>
      <td>1500m</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1291</th>
      <td>1992</td>
      <td>Albertville</td>
      <td>Skating</td>
      <td>Short Track S.</td>
      <td>CAN</td>
      <td>3000m relay</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1293</th>
      <td>1992</td>
      <td>Albertville</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>CAN</td>
      <td>downhill</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>1994</td>
      <td>Lillehammer</td>
      <td>Biathlon</td>
      <td>Biathlon</td>
      <td>CAN</td>
      <td>15km</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>1994</td>
      <td>Lillehammer</td>
      <td>Biathlon</td>
      <td>Biathlon</td>
      <td>CAN</td>
      <td>7.5km</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1461</th>
      <td>1994</td>
      <td>Lillehammer</td>
      <td>Skiing</td>
      <td>Freestyle Ski.</td>
      <td>CAN</td>
      <td>moguls</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1642</th>
      <td>1998</td>
      <td>Nagano</td>
      <td>Bobsleigh</td>
      <td>Bobsleigh</td>
      <td>CAN</td>
      <td>two-man</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1644</th>
      <td>1998</td>
      <td>Nagano</td>
      <td>Curling</td>
      <td>Curling</td>
      <td>CAN</td>
      <td>curling</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1649</th>
      <td>1998</td>
      <td>Nagano</td>
      <td>Skating</td>
      <td>Short Track S.</td>
      <td>CAN</td>
      <td>5000m relay</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1650</th>
      <td>1998</td>
      <td>Nagano</td>
      <td>Skating</td>
      <td>Short Track S.</td>
      <td>CAN</td>
      <td>500m</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1654</th>
      <td>1998</td>
      <td>Nagano</td>
      <td>Skating</td>
      <td>Speed skating</td>
      <td>CAN</td>
      <td>500m</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1656</th>
      <td>1998</td>
      <td>Nagano</td>
      <td>Skiing</td>
      <td>Snowboard</td>
      <td>CAN</td>
      <td>giant-slalom</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1850</th>
      <td>2002</td>
      <td>Salt Lake City</td>
      <td>Ice Hockey</td>
      <td>Ice Hockey</td>
      <td>CAN</td>
      <td>ice hockey</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1851</th>
      <td>2002</td>
      <td>Salt Lake City</td>
      <td>Ice Hockey</td>
      <td>Ice Hockey</td>
      <td>CAN</td>
      <td>ice hockey</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1852</th>
      <td>2002</td>
      <td>Salt Lake City</td>
      <td>Skating</td>
      <td>Figure skating</td>
      <td>CAN</td>
      <td>pairs</td>
      <td>X</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1856</th>
      <td>2002</td>
      <td>Salt Lake City</td>
      <td>Skating</td>
      <td>Short Track S.</td>
      <td>CAN</td>
      <td>5000m relay</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1857</th>
      <td>2002</td>
      <td>Salt Lake City</td>
      <td>Skating</td>
      <td>Short Track S.</td>
      <td>CAN</td>
      <td>500m</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1861</th>
      <td>2002</td>
      <td>Salt Lake City</td>
      <td>Skating</td>
      <td>Speed skating</td>
      <td>CAN</td>
      <td>500m</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1862</th>
      <td>2002</td>
      <td>Salt Lake City</td>
      <td>Skiing</td>
      <td>Cross Country S</td>
      <td>CAN</td>
      <td>5km pursuit</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2087</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Bobsleigh</td>
      <td>Skeleton</td>
      <td>CAN</td>
      <td>individual</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2090</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Curling</td>
      <td>Curling</td>
      <td>CAN</td>
      <td>curling</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2092</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Ice Hockey</td>
      <td>Ice Hockey</td>
      <td>CAN</td>
      <td>ice hockey</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2099</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skating</td>
      <td>Speed skating</td>
      <td>CAN</td>
      <td>1500m</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2103</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skating</td>
      <td>Speed skating</td>
      <td>CAN</td>
      <td>5000m</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2106</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Cross Country S</td>
      <td>CAN</td>
      <td>Sprint 1.5km</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2108</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Freestyle Ski.</td>
      <td>CAN</td>
      <td>moguls</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
  </tbody>
</table>
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




    <sqlite3.Cursor at 0x7fe8f4bf39c0>



---

4. Guardar en la base de datos. los datos generados en el sub
dataset.


```python
df_medallas_desde_1950.to_sql('medals', con=conexion, if_exists='replace', index=False)
```




    33



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
      <td>Ice Hockey</td>
      <td>Ice Hockey</td>
      <td>CAN</td>
      <td>ice hockey</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1960</td>
      <td>Squaw Valley</td>
      <td>Skating</td>
      <td>Figure skating</td>
      <td>CAN</td>
      <td>pairs</td>
      <td>X</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1960</td>
      <td>Squaw Valley</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>CAN</td>
      <td>slalom</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1964</td>
      <td>Innsbruck</td>
      <td>Bobsleigh</td>
      <td>Bobsleigh</td>
      <td>CAN</td>
      <td>four-man</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1968</td>
      <td>Grenoble</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>CAN</td>
      <td>giant slalom</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1976</td>
      <td>Innsbruck</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>CAN</td>
      <td>giant slalom</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1984</td>
      <td>Sarajevo</td>
      <td>Skating</td>
      <td>Speed skating</td>
      <td>CAN</td>
      <td>1000m</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1984</td>
      <td>Sarajevo</td>
      <td>Skating</td>
      <td>Speed skating</td>
      <td>CAN</td>
      <td>1500m</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1992</td>
      <td>Albertville</td>
      <td>Skating</td>
      <td>Short Track S.</td>
      <td>CAN</td>
      <td>3000m relay</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1992</td>
      <td>Albertville</td>
      <td>Skiing</td>
      <td>Alpine Skiing</td>
      <td>CAN</td>
      <td>downhill</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1994</td>
      <td>Lillehammer</td>
      <td>Biathlon</td>
      <td>Biathlon</td>
      <td>CAN</td>
      <td>15km</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1994</td>
      <td>Lillehammer</td>
      <td>Biathlon</td>
      <td>Biathlon</td>
      <td>CAN</td>
      <td>7.5km</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1994</td>
      <td>Lillehammer</td>
      <td>Skiing</td>
      <td>Freestyle Ski.</td>
      <td>CAN</td>
      <td>moguls</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1998</td>
      <td>Nagano</td>
      <td>Bobsleigh</td>
      <td>Bobsleigh</td>
      <td>CAN</td>
      <td>two-man</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1998</td>
      <td>Nagano</td>
      <td>Curling</td>
      <td>Curling</td>
      <td>CAN</td>
      <td>curling</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1998</td>
      <td>Nagano</td>
      <td>Skating</td>
      <td>Short Track S.</td>
      <td>CAN</td>
      <td>5000m relay</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1998</td>
      <td>Nagano</td>
      <td>Skating</td>
      <td>Short Track S.</td>
      <td>CAN</td>
      <td>500m</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1998</td>
      <td>Nagano</td>
      <td>Skating</td>
      <td>Speed skating</td>
      <td>CAN</td>
      <td>500m</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1998</td>
      <td>Nagano</td>
      <td>Skiing</td>
      <td>Snowboard</td>
      <td>CAN</td>
      <td>giant-slalom</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2002</td>
      <td>Salt Lake City</td>
      <td>Ice Hockey</td>
      <td>Ice Hockey</td>
      <td>CAN</td>
      <td>ice hockey</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2002</td>
      <td>Salt Lake City</td>
      <td>Ice Hockey</td>
      <td>Ice Hockey</td>
      <td>CAN</td>
      <td>ice hockey</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2002</td>
      <td>Salt Lake City</td>
      <td>Skating</td>
      <td>Figure skating</td>
      <td>CAN</td>
      <td>pairs</td>
      <td>X</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2002</td>
      <td>Salt Lake City</td>
      <td>Skating</td>
      <td>Short Track S.</td>
      <td>CAN</td>
      <td>5000m relay</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2002</td>
      <td>Salt Lake City</td>
      <td>Skating</td>
      <td>Short Track S.</td>
      <td>CAN</td>
      <td>500m</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2002</td>
      <td>Salt Lake City</td>
      <td>Skating</td>
      <td>Speed skating</td>
      <td>CAN</td>
      <td>500m</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2002</td>
      <td>Salt Lake City</td>
      <td>Skiing</td>
      <td>Cross Country S</td>
      <td>CAN</td>
      <td>5km pursuit</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Bobsleigh</td>
      <td>Skeleton</td>
      <td>CAN</td>
      <td>individual</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Curling</td>
      <td>Curling</td>
      <td>CAN</td>
      <td>curling</td>
      <td>M</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Ice Hockey</td>
      <td>Ice Hockey</td>
      <td>CAN</td>
      <td>ice hockey</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skating</td>
      <td>Speed skating</td>
      <td>CAN</td>
      <td>1500m</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skating</td>
      <td>Speed skating</td>
      <td>CAN</td>
      <td>5000m</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Cross Country S</td>
      <td>CAN</td>
      <td>Sprint 1.5km</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
    <tr>
      <th>32</th>
      <td>2006</td>
      <td>Turin</td>
      <td>Skiing</td>
      <td>Freestyle Ski.</td>
      <td>CAN</td>
      <td>moguls</td>
      <td>W</td>
      <td>Gold</td>
    </tr>
  </tbody>
</table>
</div>



---

# AnalysisNLP-Google_Places

Aplicación para hacer un análisis NLP de reviews extraídas de la API de Google Places. 

## Demo

Se puede ver una demo del trabajo inicial, el cual extraigo las reviews de Tripadivisor haciendo scraping a la Web en el siguiente enlace:

[Link](https://github.com/catraba/testingstuffs/blob/master/TripadvisorNLP.ipynb)

Ahora he hecho lo mismo pero en Web y con Google Places API, lo cual es más fiable y contiene más información sobre un lugar.

Está realizada en Python y JavaScript. La parte de backend se hizo inicialmente con Node.js, aunque finalmente acabé con Django Rest Framework para así hacer las peticiones más fácilmente con Spacy, librería de Python de tratamiento NLP.


## Backend

| Descripción | Método | Request | Parámetros | Ejemplo |
| ----------- | ------ | ------- | ---------- | ------- |
| Ver usuarios registrados | GET | /users/ | |  |
| Registrar nuevo usuario | POST | /users/ | username, email, password | "perico", "perico@mail.com", "123456789" |
| Usuarios con API_KEY registrada | GET | /consumers/ | | |
| Ingresar API_KEY para usuario registrado | POST | /consumers/ | consumer_id, api_key | 1, "abcdefghijklmnopqrstuvwxz" | 
| Obtener usuario con API_KEY | GET | /consumers/<consumer_id>/ | | |
| Actualizar API_KEY | PUT | /consumers/<consumer_id>/ | consumer_id, api_key | 1, "zxwvutsrqponmlkjihgfedcba" |
| Eliminar API_KEY | DELETE | /consumers/<consumer_id>/ | |

### JSON requests

```
{
  "media": 4.3,
  "reviews_amount: 1108,
  "reviews_amount": {
    1: 45,
    2: 21,
    3: 26,
    4: 57,
    5: 78
    },
  "reviews_by_year": {
    2014: 3.1,
    2015: 3.9,
    2016: 3.3,
    2017: 3.2,
    2018: 2.5,
    2019: 2.9
  }
}
```

# Frontend (básico)

Para el frontend he utilizado Svelte, además de Chart.js en los gráficos y Bootstrap para los diseños.

Aquí tenemos una muestra de lo que vería el usuario una vez ha introducido sus datos correctamente:

![alt text](https://i.postimg.cc/28LBStx5/Sin-t-tulo.png)

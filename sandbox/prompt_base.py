TEMPLATE_NER = """
Como periodista y científico de redes, está analizando la red social que surgió de un Escándalo de corrupción en Colombia.
Su tarea es inferir y reconocer las entidades nombradas de organizaciones e individuos de la noticia entre ```.
Algunas de las entidades no son explicitas, por lo que debe inferirlas a partir de la información de la noticia.

La salida solo deberia ser en formato JSON con las siguientes claves:

"Organizaciones": Lista de Nombres de Organizaciones 
"Individuos": Lista de diccionarios con los nombres de los individuos y su rol en el escándalo:
    "Nombre"
    "Cargo"
    "rolEnEscandalo"
"Relaciones": Lista de triplas de las relaciones entre individuos y organizaciones, con la siguiente estructura:
    "Individuo"
    "Relación" // Clasificador de la relación frase verbal + frase preposicional
    "Organización"
    
    
Los clasificadores de relaciones deben tener una frase verbal como ejemplo (nacio) + frase preposicional (EnCiudad) -> nacioenCiudad:\n 

```
{article}
```
"""

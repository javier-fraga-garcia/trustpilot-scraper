# TrustPilot Scraper

Script para automatizar la recolección de reseñas en la plataforma TrustPilot

## Instalación

Es necesario tener instalado Python y todas las dependencias del proyecto. Para realizar este paso ejecutar el comando `pip install -r requirements.txt`

## Ejecución y argumentos del script

Para ejecutar el script es necesario utilizar el comando `py main.py` seguido de los argumentos necesarios para el correcto funcionamiento del programa. Estos argumentos son:

* `-d`, `--domain`: el dominio para el que se desean obtener las reseñas. Ejemplo: *www.example.com*. Se recomienda consultarlo en la página de TrustPilot accediendo a la página de reseñas del objetivo y observando el dominio que contiene la url. Para el dominio de ejemplo sería: `https://es.trustpilot.com/review/www.example.com`.
* `-p`, `--pages`: el número de páginas para las que se desea obtener las reseñas. Ejemplo: **10**.
* `-o`, `--output`: el formato del archivo con los resultados, opciones: `csv` y `xlsx`. Cuando la ejecución termine se habrá generado un archivo con el formato de exportación seleccionado y el nombre del dominio para el que se realizó la ejecución. Ejemplo: `www.example.com.csv`.

**Comando de ejemplo**

`py main.py -d www.example.com -p 10 -o csv`

## Interfaz gráfica

*Sección en desarrollo, es posible que en el futuro se incluya un cuaderno de Google Colab que funcione a modo de UI*
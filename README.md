# Teachable-Discord-Machine
# Discord Bot de Análisis de Imágenes

Este proyecto es un bot de Discord que analiza imágenes enviadas por los usuarios utilizando un modelo de aprendizaje automático entrenado con [Teachable Machine](https://teachablemachine.withgoogle.com/). El bot procesa las imágenes para clasificar su contenido según las categorías definidas durante el entrenamiento del modelo.

---

## Descripción

El bot de Discord utiliza un modelo exportado desde Teachable Machine para realizar tareas de clasificación de imágenes. Funciona de la siguiente manera:

1. **Recepción de imágenes**: Los usuarios envían imágenes a un canal específico en Discord.
2. **Análisis**: El bot procesa las imágenes utilizando el modelo preentrenado.
3. **Resultados**: Devuelve la categoría más probable junto con el porcentaje de confianza para cada una.

### Tecnologías utilizadas

- **Python**: Lenguaje de programación principal del bot.
- **Discord.py**: Librería para interactuar con la API de Discord.
- **TensorFlow/Keras**: Framework para ejecutar el modelo exportado.
- **Pillow**: Librería para manejar imágenes.
- **Teachable Machine**: Herramienta para crear y entrenar el modelo de aprendizaje automático.

---

## Características

- Clasificación automática de imágenes enviadas por los usuarios.
- Respuestas claras y fáciles de entender.
- Integración sencilla con servidores de Discord.

### Ejemplo de uso

1. Un usuario envía una imagen al canal configurado.
2. El bot analiza la imagen y responde con un mensaje como:

    ```
    Esta imagen pertenece a la categoría: Gatos 🐱 (Confianza: 92%)
    ```

---

## Configuración

### Requisitos previos

- Python 3.9 o superior.
- Una cuenta de desarrollador de Discord y un bot registrado.
- Librerías necesarias (instalables con `pip`):
  ```bash
  pip install discord.py tensorflow pillow
  ```

### Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/discord-bot-analisis-imagenes.git
   ```
2. Configura las variables de entorno necesarias en un archivo `.env`:
   ```env
   DISCORD_TOKEN=tu_token_de_discord
   MODEL_PATH=ruta/a/tu/modelo/exportado
   ```
3. Ejecuta el bot:
   ```bash
   python bot.py
   ```

---

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un *issue* o un *pull request* con tus mejoras o ideas.

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

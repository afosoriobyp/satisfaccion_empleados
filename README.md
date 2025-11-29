# 🎭 Sistema de Satisfacción de Empleados - Intensamente

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1.2-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Sistema web interactivo para medir y analizar el impacto de los empleados, utilizando las cinco emociones de la película "Intensamente" (Inside Out).

## 📋 Descripción

Esta aplicación permite a los empleados expresar cómo se sienten en su trabajo mediante una interfaz visual atractiva basada en los personajes de Intensamente. Los datos recopilados se analizan mediante un diagrama de Ishikawa para identificar causas raíz de la insatisfacción laboral.

### ✨ Características principales

- **Interfaz emocional intuitiva**: 5 emociones representadas con imágenes de Intensamente
  - 😨 Miedo (Morado)
  - 😡 Furia (Rojo)
  - 😢 Tristeza (Azul)
  - 🤢 Desagrado (Verde)
  - 😄 Alegría (Amarillo)

- **Análisis de causa raíz**: 8 categorías específicas para emociones negativas
  - Sobrecarga de trabajo / Presión excesiva
  - Falta de reconocimiento / Valoración
  - Problemas de comunicación / Conflictos
  - Falta de recursos / Herramientas inadecuadas
  - Ambiente laboral negativo / Tóxico
  - Inseguridad laboral / Incertidumbre
  - Falta de desarrollo / Oportunidades
  - Problemas con liderazgo / Gestión

- **Reportes visuales**: 
  - Estadísticas por emoción
  - Diagrama de Ishikawa interactivo
  - Filtrado por fechas
  - Exportación a PDF

## 🚀 Tecnologías utilizadas

- **Backend**: Flask 3.1.2
- **Base de datos**: SQLite con SQLAlchemy
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Exportación**: html2pdf.js

## 📦 Instalación

### Requisitos previos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/afosoriobyp/satisfaccion_empleados.git
cd satisfaccion_empleados
```

2. **Crear entorno virtual**
```bash
python -m venv venv
```

3. **Activar entorno virtual**

En Windows:
```bash
venv\Scripts\activate
```

En Linux/Mac:
```bash
source venv/bin/activate
```

4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

5. **Ejecutar la aplicación**
```bash
python app.py
```

6. **Abrir en el navegador**
```
http://localhost:5000
```

## 🗂️ Estructura del proyecto

```
satisfaccion_empleados/
│
├── app.py                  # Aplicación principal Flask
├── requirements.txt        # Dependencias del proyecto
├── runtime.txt            # Versión de Python para despliegue
├── Procfile               # Configuración para Render/Heroku
├── DESPLIEGUE.md          # Guía de despliegue
│
├── instance/              # Base de datos SQLite (generada automáticamente)
│   └── feedback.db
│
├── static/                # Archivos estáticos
│   ├── style.css         # Estilos personalizados
│   └── img/              # Imágenes de emociones
│       ├── miedo.png
│       ├── furia.png
│       ├── tristeza.png
│       ├── desagrado.png
│       └── alegria.png
│
└── templates/             # Plantillas HTML
    ├── base.html         # Plantilla base
    ├── index.html        # Formulario de feedback
    └── report.html       # Dashboard de reportes
```

## 🎯 Uso

### Para empleados

1. Acceder a la página principal
2. Seleccionar una emoción que represente cómo te sientes
3. Si seleccionas una emoción negativa (Miedo, Furia, Tristeza, Desagrado):
   - Seleccionar la causa raíz del problema
4. Opcionalmente agregar un comentario
5. Enviar la opinión

### Para administradores

1. Acceder a `/informe` para ver el dashboard
2. Filtrar por rango de fechas si es necesario
3. Analizar las estadísticas por emoción
4. Revisar el diagrama de Ishikawa con las causas raíz
5. Exportar a PDF si es necesario

## 🌐 Despliegue

La aplicación está lista para desplegarse en plataformas como:

- **Render** (recomendado)
- **Heroku**
- **Railway**
- **PythonAnywhere**

Consulta el archivo `DESPLIEGUE.md` para instrucciones detalladas.

### Variables de entorno

```bash
DATABASE_PATH=/opt/render/project/data  # Ruta para BD en producción
PORT=5000                                # Puerto de la aplicación
```

## 📊 Base de datos

El modelo de datos incluye:

```python
class Feedback:
    id: Integer (Primary Key)
    level: String(20)      # miedo, furia, tristeza, desagrado, alegria
    category: String(50)   # Causa raíz o 'N/A'
    comment: Text          # Comentario opcional
    date: DateTime         # Fecha y hora del registro
```

## 🎨 Personalización

### Cambiar colores de emociones

Edita el archivo `static/style.css`:

```css
.emotion-miedo { border-color: #9370DB; }
.emotion-furia { border-color: #E74C3C; }
/* ... */
```

### Agregar nuevas categorías

Edita `templates/index.html` y `app.py`:

```html
<option value="NuevaCategoria">Nueva Categoría</option>
```

```python
ishikawa_data = {
    'NuevaCategoria': [],
    # ...
}
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**afosoriobyp**

- GitHub: [@afosoriobyp](https://github.com/afosoriobyp)

## 🙏 Agradecimientos

- Inspirado en la película "Intensamente" (Inside Out) de Pixar
- Metodología de análisis: Diagrama de Ishikawa (Espina de Pescado)

## 📸 Screenshots

### Formulario de Feedback
![Formulario](https://i.ibb.co/Z1hRT2Gk/formulario.png)

### Dashboard de Reportes
![Dashboard](https://i.ibb.co/pSPNpQd/dashboard.png)

### Diagrama de Ishikawa
![Ishikawa](https://i.ibb.co/Df8y3ZD4/Ishikawa.png)

---

⭐️ Si este proyecto te resulta útil, considera darle una estrella en GitHub!

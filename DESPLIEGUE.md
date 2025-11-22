# Guía de Despliegue - Aplicación de Satisfacción de Empleados

## 📋 Requisitos Previos
- Cuenta de GitHub (gratuita)
- Cuenta de Render (gratuita, sin tarjeta de crédito)

## 🚀 Pasos para Desplegar en Render

### 1. Subir el Proyecto a GitHub

```powershell
# Inicializar repositorio Git (si no lo has hecho)
git init

# Agregar todos los archivos
git add .

# Hacer commit inicial
git commit -m "Preparar aplicación para producción"

# Crear repositorio en GitHub y conectarlo
# Ve a https://github.com/new y crea un nuevo repositorio
# Luego ejecuta:
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
git branch -M main
git push -u origin main
```

### 2. Configurar Render

1. **Ir a Render:** https://render.com/
2. **Crear cuenta gratuita** (usa tu cuenta de GitHub)
3. **Clic en "New +"** → Selecciona **"Web Service"**
4. **Conectar tu repositorio de GitHub**
5. **Configurar el servicio:**

   - **Name:** `satisfaccion-empleados` (o el nombre que prefieras)
   - **Region:** Oregon (US West) - más cercano a Latinoamérica
   - **Branch:** `main`
   - **Root Directory:** (dejar vacío)
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Plan:** Free

6. **Variables de Entorno (Environment Variables):**
   - Clic en "Advanced"
   - Agregar: `DATABASE_PATH` = `/opt/render/project/data`

7. **Configurar Disco Persistente (IMPORTANTE para guardar la base de datos):**
   - En la sección "Advanced"
   - Agregar "Disk":
     - **Name:** `data`
     - **Mount Path:** `/opt/render/project/data`
     - **Size:** 1 GB (gratuito)

8. **Clic en "Create Web Service"**

### 3. Esperar el Despliegue

Render automáticamente:
- ✅ Clonará tu repositorio
- ✅ Instalará las dependencias
- ✅ Iniciará la aplicación con Gunicorn
- ✅ Te dará una URL pública (ej: `https://satisfaccion-empleados.onrender.com`)

**Tiempo estimado:** 2-5 minutos

## 🔄 Actualizaciones Automáticas

Cada vez que hagas `git push` a tu repositorio, Render desplegará automáticamente la nueva versión.

```powershell
git add .
git commit -m "Actualización de funcionalidad"
git push
```

## 🎯 Alternativas Gratuitas

### **PythonAnywhere** (más simple, sin necesidad de Git)
- URL: https://www.pythonanywhere.com
- Plan gratuito: 512MB RAM
- Subida manual de archivos via web
- Perfecto para demos rápidas

### **Railway** (con $5 USD de crédito gratis)
- URL: https://railway.app
- Muy similar a Render
- Requiere tarjeta de crédito (no se cobra si no excedes el crédito)

### **Fly.io** (más técnico)
- URL: https://fly.io
- Requiere tarjeta de crédito
- 3 aplicaciones gratuitas

## ⚠️ Consideraciones de Producción

### Limitaciones del Plan Gratuito de Render:
- ⏱️ La app "duerme" después de 15 minutos de inactividad
- 🐌 Primera carga después de dormir: 30-60 segundos
- 💾 750 horas/mes de tiempo activo (suficiente para pruebas)
- 🗄️ SQLite funciona pero no es ideal para alta concurrencia

### Para Producción Real (cuando escales):
1. **Base de datos:** Migrar a PostgreSQL
2. **Plan pago:** Evita el "sleep" ($7/mes en Render)
3. **CDN:** Para archivos estáticos
4. **Monitoreo:** Configurar alertas

## 🔒 Seguridad

Para producción, agrega estas mejoras:

```python
# En app.py
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

# Variables de entorno en Render
SECRET_KEY = tu-clave-secreta-aleatoria
```

## 📊 Verificación Post-Despliegue

1. ✅ Visita tu URL de Render
2. ✅ Prueba el formulario de feedback
3. ✅ Verifica el informe con filtros de fecha
4. ✅ Confirma que los datos persisten después de reinicios

## 🆘 Troubleshooting

**Si la app no inicia:**
- Revisa los logs en el Dashboard de Render
- Verifica que `gunicorn` esté en requirements.txt
- Confirma que el Start Command sea `gunicorn app:app`

**Si pierdes datos:**
- Verifica que el disco persistente esté montado en `/opt/render/project/data`
- Confirma que `DATABASE_PATH` esté configurado correctamente

## 📞 Soporte
- Render Docs: https://render.com/docs
- Community Forum: https://community.render.com/

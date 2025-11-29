from flask import Flask, render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

# Configure the SQLite database
# Use /opt/render/project/data for persistent storage in Render
database_path = os.environ.get('DATABASE_PATH', os.path.join(basedir, 'instance'))
os.makedirs(database_path, exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(database_path, 'feedback.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)

# Create the database tables
with app.app_context():
    db.create_all()


# Route for the feedback form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("=== DEBUG: Datos del formulario ===")
        print(f"Form data: {request.form}")
        print(f"Level: {request.form.get('level')}")
        print(f"Category: {request.form.get('category')}")
        print(f"Comment: {request.form.get('comment')}")
        print("===================================")
        
        level = request.form.get('level', '')
        category = request.form.get('category', 'N/A')
        comment = request.form.get('comment', '')
        
        # Si no hay categoría (emociones positivas/neutras), usar 'N/A'
        if not category or category == '':
            category = 'N/A'

        new_feedback = Feedback(level=level, category=category, comment=comment)

        try:
            db.session.add(new_feedback)
            db.session.commit()
            return redirect(url_for('gracias'))
        except:
            return "There was an issue adding your feedback."

    return render_template('index.html')

# Route for the thank you page
@app.route('/gracias')
def gracias():
    return render_template('base.html', content="<h1>¡Gracias por tu retroalimentación!</h1><a href='/' class='btn btn-primary mt-3'>Volver</a>")

#Generar Informe
@app.route('/informe')
def informe():
    # 1. Obtener fechas de los parámetros GET (URL)
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')

    # 2. Consulta base
    query = Feedback.query

    # 3. Aplicar filtros si existen
    if start_date_str:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        query = query.filter(Feedback.date >= start_date)
    
    if end_date_str:
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        # Sumamos 1 día para incluir todo el día final (hasta las 23:59:59)
        query = query.filter(Feedback.date < end_date + timedelta(days=1))

    # Ejecutar la consulta filtrada
    feedbacks = query.all()
    
    # 4. Recalcular estadísticas BASADAS EN LOS DATOS FILTRADOS
    stats = {
        'miedo': sum(1 for f in feedbacks if f.level == 'miedo'),
        'furia': sum(1 for f in feedbacks if f.level == 'furia'),
        'tristeza': sum(1 for f in feedbacks if f.level == 'tristeza'),
        'desagrado': sum(1 for f in feedbacks if f.level == 'desagrado'),
        'alegria': sum(1 for f in feedbacks if f.level == 'alegria'),
    }
    
    # 5. Filtrar datos para Ishikawa - Nuevas categorías
    ishikawa_data = {
        'Sobrecarga': [],
        'Reconocimiento': [],
        'Comunicacion': [],
        'Recursos': [],
        'Ambiente': [],
        'Inseguridad': [],
        'Desarrollo': [],
        'Liderazgo': []
    }
    
    for f in feedbacks:
        # Solo incluir emociones negativas
        if f.level in ['miedo', 'furia', 'tristeza', 'desagrado'] and f.category in ishikawa_data:
            # Agregamos la emoción y fecha al comentario para contexto
            emociones_emoji = {
                'miedo': '😨',
                'furia': '😡',
                'tristeza': '😢',
                'desagrado': '🤢'
            }
            emoji = emociones_emoji.get(f.level, '')
            comentario_con_fecha = f"{emoji} {f.comment or 'Sin comentario'} ({f.date.strftime('%d/%m')})"
            ishikawa_data[f.category].append(comentario_con_fecha)

    # Pasamos las fechas originales para mantenerlas en los inputs del HTML
    return render_template('report.html', 
                           stats=stats, 
                           ishikawa=ishikawa_data,
                           start_date=start_date_str,
                           end_date=end_date_str)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
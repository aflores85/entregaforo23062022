import json
from flask import Flask, request, jsonify # diccionarios de python los convienrte en Json y en response, objeto request
from flask_sqlalchemy import SQLAlchemy # libreria para BBDD - ORM mapeos de objetos a una base Relacional
from flask_cors import CORS # por seguridad Cros Origin
from routers.routers import get_posts
from routers.routers import get_subject
from routers.routers import new_post
from routers.routers import new_subject
from routers.routers import new_foro
from routers.routers import delete_posts
from routers.routers import delete_subject
from routers.routers import get_foro
# initialize app
app = Flask(__name__) #creamos el objeto, un servidor web, responde peticiones de request
app.register_blueprint(get_foro)
app.register_blueprint(get_posts)
app.register_blueprint(get_subject)
app.register_blueprint(new_post)
app.register_blueprint(new_subject)
app.register_blueprint(new_foro)
app.register_blueprint(delete_posts)
app.register_blueprint(delete_subject)


if __name__ == "__main__":
    app.run(debug=True)

CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:admin@localhost:5432/forodb" # conexion a la base 
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://cjbntwlxqcxuqv:acbed88d66591c93b084bc6393f11ee95f3106b45f655672cafc3fa119c03755@ec2-34-225-159-178.compute-1.amazonaws.com:5432/d3vkm95ntvr4ni" # conexion a la base
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.create_all()


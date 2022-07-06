from time import sleep
from flask import Flask, request, jsonify  # diccionarios de python los convienrte en Json y en response, objeto request
from flask_sqlalchemy import SQLAlchemy # libreria para BBDD - ORM mapeos de objetos a una base Relacional
from flask_cors import CORS # por seguridad Cros Origin
from flask import Blueprint 
from venv import create
from flask_cors import CORS # por seguridad Cros Origin
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from
from sqlalchemy import Integer, null



# initialize app

app = Flask(__name__) #creamos el objeto, un servidor web, responde peticiones de request
app.json_encoder = LazyJSONEncoder
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:admin@localhost:5432/forodb" # conexion a la base 
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://cjbntwlxqcxuqv:acbed88d66591c93b084bc6393f11ee95f3106b45f655672cafc3fa119c03755@ec2-34-225-159-178.compute-1.amazonaws.com:5432/d3vkm95ntvr4ni" # conexion a la base
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

swagger_template = dict(
info = {
    'title': LazyString(lambda: 'Swagger UI document'),
    'version': LazyString(lambda: '0.1'),
    'description': LazyString(lambda: 'Document and implements functionality.'),
    },
    host = LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'Doc',
            "route": '/apidocs/',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

swagger = Swagger(app, template=swagger_template,             
                  config=swagger_config)


class Foro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Foro %r>' % self.title

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(80), nullable=False)
    foro_id = db.Column(db.Integer, db.ForeignKey('foro.id'), nullable=False)
    foro = db.relationship('Foro', 
    backref=db.backref('subjects', lazy=True))

    def __repr__(self):
        return '<Subject %r>' % self.title

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(80), nullable=False)
    image_url = db.Column(db.String(180), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    subject = db.relationship('Subject', 
    backref=db.backref('posts', lazy=True))


    def __repr__(self):
        return '<Post %r>' % self.title

@app.route('/api/v1/newforo', methods=['POST'])
def new_foro():
    foro_to_create = Foro(title=request.json['title'],
                          content=request.json['content']
                                                         )
    if foro_to_create is None:
        return jsonify({'message': 'Por favor complete el titulo'}), 404 
    else:
        db.session.add(foro_to_create)
        db.session.commit()
    return jsonify({'message': 'Foro created successfully'})
    


@app.route('/api/v1/newsubject', methods=['POST'])
def new_subject():
    subject_to_create = Subject(title=request.json['title'],
                          content=request.json['content'],
                          foro_id=request.json['foro_id'])

    db.session.add(subject_to_create)
    db.session.commit()
    return jsonify({'message': 'Subject created successfully'})


@app.route('/api/v1/newpost', methods=['POST'])
def new_post():
    post_to_create = Post(title=request.json['title'],
                          content=request.json['content'],
                          image_url=request.json['image_url'],
                          subject_id=request.json['Subject_id'])

    db.session.add(post_to_create)
    db.session.commit()
    return jsonify({'message': 'Post created successfully'})

@app.route('/api/v1/getforo', methods=['GET'])
def get_foro():
    
    foros_Query = Foro.query.all() 
    foros_list = []
    for foros in foros_Query:
        foros_list.append(
            {'title': foros.title,
             'id': foros.id,
             'content': foros.content,          
             })
    return jsonify({'foros': foros_list, 'message': 'foros fetched successfully'})

@app.route('/api/v1/getcantidadforo', methods=['GET'])
def get_cantidad_foro():
    foros_Cantidad_Query = Foro.query.all.count()
    foros_list = []
    for foros in foros_Cantidad_Query:
        foros_list.append(
            {'title': foros.title,
             'id': foros.id,
             'content': foros.content,          
             })
    return jsonify( foros_list.count  )
    #return jsonify({'cantidadforos': foros_list , 'message': 'getcantidadforo fetched successfully'})

@app.route('/api/v1/getsubject', methods=['GET'])
def get_subject():    
    subject_Query = Subject.query.all()
    subject_list = []
    for subject in subject_Query:
        subject_list.append(
            {'title': subject.title,
             'id': subject.id,
             'content': subject.content,
             'foro_id': subject.foro_id
            })
    return jsonify({'Subject': subject_list, 'message': 'subject fetched successfully'})

@app.route('/api/v1/getPosts', methods=['GET'])
def get_posts():
    posts_query = Post.query.all()
    posts_list = []
    for posts in posts_query:
        posts_list.append(
            {'title': posts.title,
             'id': posts.id,
             'content': posts.content,
             'image': posts.image_url
             })
    return jsonify({'posts': posts_list, 'message': 'Posts fetched successfully'})

#los deletes

@app.route('/api/v1/deletepost/<id>', methods=['DELETE'])
def delete_posts(id):
    query_post_to_delete = Post.query.filter_by(id=id).first()
    if query_post_to_delete is None:
        return jsonify({'message': 'Post does not exists'}), 404
    db.session.delete(query_post_to_delete)
    db.session.commit()
    return jsonify({'message': 'Posts fetched successfully'})


@app.route('/api/v1/deletesubject/<id>', methods=['DELETE'])
def delete_subject(id):
    query_subject_to_delete = Subject.query.filter_by(id=id).first()
    if query_subject_to_delete is None:
        return jsonify({'message': 'Subject does not exists'}), 404

    db.session.delete(query_subject_to_delete)
    db.session.commit()
    return jsonify({'message': 'Subject fetched successfully'})



@app.route('/api/v1/updateforo', methods=['PUT'])
def update_foro():
    id: request.form['id']
    title: request.form['title']
    content:request.form['content']

    query_update_foro = Foro.query.filter_by(id=id).one()
    if query_update_foro is None:
        return jsonify({'message': 'Foro does not exists'}), 404

    db.session.update(query_update_foro)
    db.session.commit()
    return jsonify({'message': 'Foro update fetched successfully'})

db.create_all()


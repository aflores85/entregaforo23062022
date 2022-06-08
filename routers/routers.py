
from models.models import Foro
from models.models import Subject
from models.models import Post  
from flask import Blueprint 
from flask import Flask, request, jsonify # diccionarios de python los convienrte en Json y en response, objeto request
from app import app 
from app import db

new_foro = Blueprint('newforo'. __name__)
@app.route('/api/v1/newforo', methods=['POST'])
def new_foro():
    foro_to_create = Foro(title=request.json['title'],
                          content=request.json['content']
                                                        )

    db.session.add(foro_to_create)
    db.session.commit()
    return jsonify({'message': 'Foro created successfully'})

new_subject = Blueprint('newsubject'. __name__)
@app.route('/api/v1/newsubject', methods=['POST'])
def new_subject():
    subject_to_create = Subject(title=request.json['title'],
                          content=request.json['content'],
                          foro_id=request.json['foro_id'])

    db.session.add(subject_to_create)
    db.session.commit()
    return jsonify({'message': 'Subject created successfully'})

new_post = Blueprint('newpost'. __name__)
@app.route('/api/v1/newpost', methods=['POST'])
def new_post():
    post_to_create = Post(title=request.json['title'],
                          content=request.json['content'],
                          image_url=request.json['imageURL'],
                          subject_id=request.json['subjectid'])

    db.session.add(post_to_create)
    db.session.commit()
    return jsonify({'message': 'Post created successfully'})

get_foro = Blueprint('getforo'. __name__)
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

get_subject = Blueprint('getsubject'. __name__)
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

get_Posts = Blueprint('getPosts'. __name__)
@app.route('/api/v1/getPosts', methods=['GET'])
def get_posts():
    # current_app.logger.info('request')
    posts = Post.query.all()
    posts_list = []
    for post in posts:
        posts_list.append(
            {'title': post.title,
             'id': post.id,
             'content': post.content,
             'image': post.image_url
             })
    return jsonify({'posts': posts_list, 'message': 'Posts fetched successfully'})

#los deletes
delete_post = Blueprint('deletepost'. __name__)
@app.route('/api/v1/deletepost/<id>', methods=['DELETE'])
def delete_posts(id):
    query_post_to_delete = Post.query.filter_by(id=id).first()
    if query_post_to_delete is None:
        return jsonify({'message': 'Post does not exists'}), 404
    db.session.delete(query_post_to_delete)
    db.session.commit()
    return jsonify({'message': 'Posts fetched successfully'})


delete_subject = Blueprint('deletesubject'. __name__)
@app.route('/api/v1/deletesubject/<id>', methods=['DELETE'])
def delete_subject(id):
    query_subject_to_delete = Subject.query.filter_by(id=id).first()
    if query_subject_to_delete is None:
        return jsonify({'message': 'Subject does not exists'}), 404

    db.session.delete(query_subject_to_delete)
    db.session.commit()
    return jsonify({'message': 'Subject fetched successfully'})


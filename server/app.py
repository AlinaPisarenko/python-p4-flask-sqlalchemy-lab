#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)
    
    return make_response(
        f'''
            <ul style="font-size: 40px">
                <li>ID: {animal.id}</li>
                <li>Name: {animal.name}</li>
                <li>Species: {animal.species}</li>
                <li>Zookeper: {animal.zookeeper.name}</li>
                <li>Environment: {animal.enclosure.environment}</li>
            </ul>
        '''
    )

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    
    response_body = f'''
            <ul style="font-size: 40px">
                <li>ID: {zookeeper.id}</li>
                <li>Name: {zookeeper.name}</li>
                <li>Birthday: {zookeeper.birthday}</li>
            </ul>
            <p style="font-size: 40px">Animals:</p>
        '''
    
    for animal in zookeeper.animals:
        response_body += f'<li style="font-size: 40px">{animal.name}</li>'

    return make_response(response_body)

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    
    response_body = f'''
            <ul style="font-size: 40px">
                <li>ID: {enclosure.id}</li>
                <li>Environment: {enclosure.environment}</li>
                <li>Open to visitors: {enclosure.open_to_visitors}</li>
            </ul>
            <p style="font-size: 40px">Animals:</p>
        '''
    
    for animal in enclosure.animals:
        response_body += f'<li style="font-size: 40px">{animal.name}</li>'
        
    return make_response(response_body)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

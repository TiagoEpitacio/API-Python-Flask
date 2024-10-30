from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Biblia',
        'autor': 'King James'
    },
    {
        'id': 2,
        'titulo': 'Uma Vida com Propósitos',
        'autor': 'Rick Warren'
    },
    {
        'id': 3,
        'titulo': 'O verdadeiro Evangelho',
        'autor': 'Paul Washer'
    },
    {
        'id': 4,
        'titulo': 'Até que nada mais importe',
        'autor': 'Luciano Subirá'
    }
      {
        'id': 5,
        'titulo': 'Base de conhecimento em teste de software',
        'autor': 'Ricardo Cristalli'
    }
]

@app.route('/livros')
def obter_livros():
    return jsonify(livros)
app.run(port=5000,host='localhost',debug=True)
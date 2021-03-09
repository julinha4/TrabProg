from config import *
from modelo import Novela, Genero, Personagem


@app.route("/")
def padrao():
    return "backend funcionando"

@app.route("/listar_novelas")
def listar_novelas():
    novelas = db.session.query(Novela).all()
    retorno = []
    for n in novelas:
        retorno.append(n.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listar_generos")
def listar_generos():
    generos = db.session.query(Genero).all()
    retorno = []
    for g in generos:
        retorno.append(g.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listar_personagens")
def listar_personagens():
    personagens = db.session.query(Personagem).all()
    retorno = []
    for p in personagens:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/incluir_novela", methods=['post'])
def incluir_novela():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json(force=True)
    try:
        nova = Novela(**dados)
        db.session.add(nova)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


@app.route("/excluir_novela/<int:novela_id>", methods=['DELETE'])
def excluir_novela(novela_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Novela.query.filter(Novela.id == novela_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
    
app.run(debug = True)
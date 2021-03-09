from config import *

class Genero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(254))
    popularidade = db.Column(db.Integer)
    def __str__(self):
        return self.tipo +  ", " + str(self.popularidade)
    
    def json(self):
        return{
            "id" : self.id,
            "tipo" : self.tipo,
            "popularidade" : self.popularidade
        }

class Novela(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    emissora = db.Column(db.String(254))
    data_transmissao = db.Column(db.String(254))
    genero_id = db.Column(db.Integer, db.ForeignKey(Genero.id), nullable = False)
    genero = db.relationship("Genero")

    def __str__(self):
        return str(self.id) + ", " + self.nome + ", " + self.emissora + ", " + \
               self.data_transmissao
    def json(self):
        return{
            "id": self.id,
            "nome": self.nome,
            "emissora": self.emissora,
            "data_transmissao": self.data_transmissao,
            "genero_id" : self.genero_id,
            "genero" : self.genero.json()
        }

class Personagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    idade = db.Column(db.Integer)
    resumo = db.Column(db.String(254))
    novela_id = db.Column(db.Integer, db.ForeignKey(Novela.id), nullable = False)
    novela = db.relationship("Novela")
    def __str__(self):
        return self.nome + ", " + str(self.idade) + ", " + self.resumo

    def json(self):
        return{
            "id" : self.id,
            "nome" : self.nome,
            "idade" : self.idade,
            "resumo" : self.resumo,
            "novela_id" : self.novela_id,
            "novela" : self.novela.json()
        }

if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    genero1 = Genero(tipo = "Drama", popularidade = 10)
    db.session.add(genero1)
    db.session.commit()
    print(genero1)

    novela1 = Novela(nome = "Claudinho e Buchecha", emissora = "TV Record", data_transmissao = "26/08/2011", genero = genero1)
    db.session.add(novela1)
    db.session.commit()
    print(novela1)

    novela2 = Novela(nome = "Cesar Fabiano & Menotti", emissora = "SBT", data_transmissao = "12/06/2017", genero = genero1)
    db.session.add(novela2)
    db.session.commit()
    print(novela2)

    personagem1 = Personagem(nome = "Tobias", idade = 30, resumo = "Um jovem de 30 anos que apenas está começando a sua vida nessa cidade nova", novela = novela1)
    db.session.add(personagem1)
    db.session.commit()
    print(personagem1)


    """
    todas = db.session.query(Novela).all()
    for n in todas:
        print(n)
        print(n.json())

    #print(nova.nome)

    """
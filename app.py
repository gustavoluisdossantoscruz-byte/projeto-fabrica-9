from flask import Flask, request, jsonify

app = Flask(__name__)

itens = [
    {
        "id": 1,
        "nome": "Arroz 5kg",
        "quantidade": 2,
        "categoria": "Alimentos",
        "prioridade": "alta",
        "comprado": False
    }
]

@app.route("/items", methods=["GET"])
def listar_itens():
    return jsonify(itens)

@app.route("/items/<id>", methods=["GET"])
def buscar_item(id):
    item = next((i for i in itens if i["id"] == id), None)
    if not item:
        return jsonify({"erro": "item não encontrada!"}), 404

    return jsonify(item)

@app.route("/items", methods=["POST"])
def add_item():
    dados = request.get_json()
    nova_item = {
        "id": len(itens) + 1,
        "nome": dados["nome"],
        "quantidade": dados["quantidade"],
        "categoria": dados["categoria"],
        "prioridade": dados["prioridade"]
        "comprado": dados["comprado"]
    }
    musicas.append(nova_item)
    return jsonify(nova_item), 201

@app.route("/items/<id>", methods=["PUT"])
def atualizar_item(id):
    musica = next((i for i in item if i["id"] == id), None)
    if not item:
        return jsonify({"erro": "item não encontrada!"}), 404

    dados = request.get_json()
    musica["titulo"] = dados.get('nom-e', musica["titulo"])
    musica["artista"] = dados.get('artista', musica["artista"])
    musica["duracao"] = dados.get('duracao', musica["duracao"])
    musica["url"] = dados.get('url', musica["url"])

    return jsonify(musica)

@app.route("/tracks/<id>", methods=["DELETE"])
def atualizar_musica(id):
    global musicas
    musica = next((m for m in musica if m["id"] == id), None)
    if not musica:
        return jsonify({"erro": "musica não encontrada!"}), 404

    musicas = [m for m in musica if m["id"] != id]

    return jsonify({"mensagem": "musica excluida com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)
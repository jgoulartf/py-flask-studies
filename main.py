from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return


@app.route('/nome', methods=['POST'])
def nome():
    # lógica do post aqui
    nome = request.get_json() # exemplo de como acessar os dados enviados no corpo do post
    return nome['nome']

@app.route('/upload', methods=['POST'])
def upload():
    # Verificar se a requisição contém um arquivo com o nome "arquivo"
    if 'arquivo' not in request.files:
        return 'Nenhum arquivo enviado'

    # Obter o arquivo enviado
    arquivo = request.files['arquivo']

    # Verificar se o arquivo tem um nome
    if arquivo.filename == '':
        return 'Nenhum arquivo selecionado'

    # Salvar o arquivo no disco
    arquivo.save(f'data/{arquivo.filename}')

    # Retornar uma mensagem de sucesso
    return 'Arquivo {} enviado com sucesso'.format(arquivo.filename)

if __name__ == '__main__':
    app.run()
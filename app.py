from flask import Flask, render_template, request
from numero_por_extenso import monetario
from util import data_extenso, cpf_cnpj, formata_processo

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/declaracao_de_isencao_irpf', methods=['GET'])
def declaracao_de_isencao_irpf():
    return render_template('declaracao_de_isencao_irpf.html')


@app.route('/imprimir_declaracao_de_isencao_irpf', methods=['POST'])
def imprimir_declaracao_de_isencao_irpf():
    valor_extenso = monetario(request.form.get('valornumero'))
    cpf_cnpj_formatado = cpf_cnpj(request.form.get('cpf-cnpj'))
    return render_template('imprimir_declaracao_de_isencao_irpf.html',
                           dados=request.form.to_dict(),
                           valor_extenso=valor_extenso,
                           data_extenso=data_extenso(),
                           cpf_cnpj_formatado=cpf_cnpj_formatado,
                           formata_processo=formata_processo(request.form.get('processo'))
                           )


if __name__ == '__main__':
    app.run(debug=True)

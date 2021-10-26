from flask import Flask, render_template, request
from util import data_extenso, cpf_cnpj, formata_processo, formata_data, formata_moeda, valor_por_extenso

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/declaracao_de_isencao_irpf', methods=['GET'])
def declaracao_de_isencao_irpf():
    return render_template('declaracao_de_isencao_irpf.html')


@app.route('/imprimir_declaracao_de_isencao_irpf', methods=['POST'])
def imprimir_declaracao_de_isencao_irpf():
    salario = formata_moeda(request.form.get('valornumero'))
    valor_extenso = valor_por_extenso(salario)
    cpf_cnpj_formatado = cpf_cnpj(request.form.get('cpf-cnpj'))
    return render_template('imprimir_declaracao_de_isencao_irpf.html',
                           dados=request.form.to_dict(),
                           valor_extenso=valor_extenso,
                           salario=salario,
                           data_extenso=data_extenso(),
                           cpf_cnpj_formatado=cpf_cnpj_formatado,
                           formata_processo=formata_processo(request.form.get('processo'))
                           )


@app.route('/declaracao_de_renda', methods=['GET'])
def declaracao_de_renda():
    return render_template('declaracao_de_renda.html')


@app.route('/imprimir_declaracao_de_renda', methods=['POST'])
def imprimir_declaracao_de_renda():
    cpf = cpf_cnpj(request.form.get('cpf'))
    salario = formata_moeda(request.form.get('salario'))
    return render_template('imprimir_declaracao_de_renda.html',
                           dados=request.form.to_dict(),
                           valor_extenso=valor_por_extenso(salario),
                           cpf=cpf,
                           data_extenso=data_extenso(),
                           salario=salario,
                           ci_emissao=formata_data(request.form.get('ci_emissao')),
                           data1_salario=formata_data(request.form.get('data1_salario')),
                           data2_salario=formata_data(request.form.get('data2_salario')),
                           )


if __name__ == '__main__':
    app.run(debug=True)

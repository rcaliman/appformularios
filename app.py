from flask import Flask, render_template, request
from numero_por_extenso import monetario
from util import data_extenso, cpf_cnpj, formata_processo, formata_data
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/declaracao_de_isencao_irpf', methods=['GET'])
def declaracao_de_isencao_irpf():
    return render_template('declaracao_de_isencao_irpf.html')


@app.route('/imprimir_declaracao_de_isencao_irpf', methods=['POST'])
def imprimir_declaracao_de_isencao_irpf():
    valor_extenso = monetario(request.form.get('valornumero').replace('.', ''))
    cpf_cnpj_formatado = cpf_cnpj(request.form.get('cpf-cnpj'))
    return render_template('imprimir_declaracao_de_isencao_irpf.html',
                           dados=request.form.to_dict(),
                           valor_extenso=valor_extenso,
                           data_extenso=data_extenso(),
                           cpf_cnpj_formatado=cpf_cnpj_formatado,
                           formata_processo=formata_processo(request.form.get('processo'))
                           )


@app.route('/declaracao_de_renda', methods=['GET'])
def declaracao_de_renda():
    return render_template('declaracao_de_renda.html')


@app.route('/imprimir_declaracao_de_renda', methods=['POST'])
def imprimir_declaracao_de_renda():
    valor_extenso = monetario(request.form.get('salario').replace('.', ''))
    cpf = cpf_cnpj(request.form.get('cpf'))
    return render_template('imprimir_declaracao_de_renda.html',
                           dados=request.form.to_dict(),
                           valor_extenso=valor_extenso,
                           cpf=cpf,
                           data_extenso=data_extenso(),
                           ci_emissao=formata_data(request.form.get('ci_emissao')),
                           data1_salario=formata_data(request.form.get('data1_salario')),
                           data2_salario=formata_data(request.form.get('data2_salario')),
                           )


if __name__ == '__main__':
    app.run(debug=True)

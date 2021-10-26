from datetime import datetime
from num2words import num2words


def valor_por_extenso(numero: str) -> str:
    """
    usa a biblioteca num2words para transformar o valor em extenso
    :param numero: str
    :return: str
    """
    valor, centavos = numero.split(',')
    valor = valor.replace('.', '')
    reais = num2words(valor, lang='pt_BR')
    if centavos == '00':
        texto_centavos = ''
    elif centavos == '01':
        texto_centavos = ' e um centavo'
    else:
        texto_centavos = ' e ' + num2words(centavos, lang='pt_BR') + ' centavos'
    return reais + ' reais' + texto_centavos


def data_extenso() -> str:
    """
    transforma a data de numeral para extenso
    :return: str
    """
    mes = 'janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho',\
          'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'

    return f'Colatina-ES, {datetime.today().day} de {mes[datetime.today().month]} de {datetime.today().year}'


def formata_data(data: str) -> str:
    """
    formata a data dividindo os campos por /
    :param data: str
    :return: str
    """
    print(type(data))
    if len(str(data)) > 6:
        return f'{data[-8:-6]}/{data[-6:-4]}/{data[-4:]}'
    else:
        return f'{data[-6:-4]}/{data[-4:]}'


def cpf_cnpj(_cpf_cnpj: str) -> str:
    """
    formata o cpf ou cnpj dividindo o numero pelos campos
    :param _cpf_cnpj: str
    :return: str
    """
    if len(str(_cpf_cnpj)) <= 11:
        return f'{_cpf_cnpj[:-8]}.{_cpf_cnpj[-8:-5]}.{_cpf_cnpj[-5:-2]}-{_cpf_cnpj[-2:]}'
    else:
        return f'{_cpf_cnpj[:-12]}.{_cpf_cnpj[-12:-9]}.{_cpf_cnpj[-9:-6]}/{_cpf_cnpj[-6:-2]}-{_cpf_cnpj[-2:]}'


def formata_processo(_processo: str) -> str:
    """
    formata o numero do processo divindo o numero pelos devidos campos
    :param _processo: str
    :return: str
    """
    return f'{_processo[:-11]}.{_processo[-11:-9]}.{_processo[-9:-7]}.{_processo[-7:-1]}-{_processo[-1:]}'


def formata_moeda(_valor: str) -> str:
    """
    formata moeda para o padrão brasileiro
    :param _valor: str
    :return: str
    """
    centavos = _valor[-2:]
    inteiros = int(_valor[:-2])
    return ('{:,}'.format(inteiros)).replace(',', '.') + ',' + centavos


from datetime import datetime


def data_extenso():
    mes = 'janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho',\
          'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'

    return f'Colatina-ES, {datetime.today().day} de {mes[datetime.today().month]} de {datetime.today().year}'


def cpf_cnpj(_cpf_cnpj):
    if len(str(_cpf_cnpj)) <= 11:
        return f'{_cpf_cnpj[:-8]}.{_cpf_cnpj[-8:-5]}.{_cpf_cnpj[-5:-2]}-{_cpf_cnpj[-2:]}'
    else:
        return f'{_cpf_cnpj[:-12]}.{_cpf_cnpj[-12:-9]}.{_cpf_cnpj[-9:-6]}/{_cpf_cnpj[-6:-2]}-{_cpf_cnpj[-2:]}'


def formata_processo(_processo):
    return f'{_processo[:-11]}.{_processo[-11:-9]}.{_processo[-9:-7]}.{_processo[-7:-1]}-{_processo[-1:]}'

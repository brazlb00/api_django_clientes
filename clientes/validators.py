from validate_docbr import CPF
import re

def cpf_valido(numerp_do_cpf):
    cpf = CPF()
    cpf.validate(numerp_do_cpf)  # True
    return cpf.validate(numerp_do_cpf)

def nome_valido (nome):
     return nome.isalpha()

def rg_valido(numero_do_rg):
        return len(numero_do_rg) == 9

def celular_valido(numero_do_celular):
    #Verifica se o celular é válido com expressão regular
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_do_celular)
    return resposta

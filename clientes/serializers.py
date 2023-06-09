from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'CPF inválido.'})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': 'O campo nome deve conter apenas letras.'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': 'O campo rg deve conter exatamente 9 dígitos.'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': 'O campo celular deve seguir este exemplo: nn nnnnn-nnnn.'})
        return data      

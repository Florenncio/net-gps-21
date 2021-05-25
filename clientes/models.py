from django.db import models
import uuid

class Cliente (models.Model):
    
    """
    id_cli = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    dt_criacao_cli = models.DateTimeField(auto_now_add=True)
    """
    tip_pessoa_cli = models.CharField(max_length=10)
    nome_cli = models.CharField(max_length=50)
    tell_cli = models.CharField(max_length=15)
    cell_cli = models.CharField(max_length=15)
    cell2_cli = models.CharField(max_length=15)
    email_cli = models.EmailField()
    email2_cli = models.EmailField()
    cgc_cli = models.CharField(max_length=15)
    cnpj_cli = models.CharField(max_length=30)
    cep_cli = models.CharField(max_length=8)
    uf_cli = models.CharField(max_length=2)
    cidade_cli = models.CharField(max_length= 30)
    bairro_cli = models.CharField(max_length=30)
    endereco_cli = models.CharField(max_length= 50)
    num_cli = models.PositiveIntegerField()
    comp_cli = models.CharField(max_length=100)


    def __str__(self):
        return 'ID: %s | Nome: %s' % (self.pk, self.nome_cli)

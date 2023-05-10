from django.db import models
from django.core.validators import RegexValidator

class TimesTampsModel (models.Model):
    ativo = models.BooleanField(default = True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True, auto_now=False, null=True)
    alterado_em = models.DateTimeField('Alterado em', auto_now_add=False, auto_now=True, null=True)
    criado_por = models.CharField('Criado por', max_length=50, null=True, blank=True)
    alterado_por = models.CharField('Alterado por', max_length=50, null=True, blank=True)
    # criado_navegador = models.TextField(blank=True, null=True, verbose_name='Criado no Navegador')
    # editado_navegador = models.TextField(blank=True, null=True, verbose_name='Editado no Navegador')

    def _criado_por(self):
        return self.criado_em.now.strftime('%d/%m/%Y')
    
    def _alterado_em(self):
        return self.alterado_em.strftime('%d/%m/%Y')
    
    def get_criado_em(self):
        try:
            data = self.criado_em.strftime('%d/%m/%Y %H:%M:%S')
        except:
            data = None
        return data

    class Meta:
        abstract=True


class Apartamento(models.Model):
    numero = models.IntegerField(unique=True, default=0)
    bloco_apt = models.IntegerField(unique=True, null=True, default=0)

    def __str__(self):
        return str(self.numero)
    
    class Meta:
        verbose_name_plural = "Apartamentos"


class Visitante(TimesTampsModel):
    nome = models.CharField(max_length=100)
    cpf_regex = RegexValidator(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', 'CPF inválido. O formato deve ser: 000.000.000-00')
    cpf = models.CharField(validators=[cpf_regex], unique=True, max_length=14)
    data_visita = models.DateField()
    apartamentos = models.ForeignKey(Apartamento, on_delete=models.CASCADE)
    uber = models.BooleanField(default=False)
    modelo_carro = models.CharField(max_length=50, blank=True, null=True)
    placa_carro = models.CharField(max_length=7, blank=True, null=True)
    cor_carro = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.cpf}) - {self.data_visita}"
    
    class Meta:
        verbose_name_plural = "Visitantes"


class Sucesso(models.Model):
    mensagem = models.CharField(max_length=100)

    def __str__(self):
        return self.mensagem
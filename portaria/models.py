from django.db import models
from django.core.validators import RegexValidator

class Apartamento(models.Model):
    numero = models.IntegerField(unique=True, default=0)
    bloco_apt = models.IntegerField(unique=True, null=True, default=0)

    def __str__(self):
        return str(self.numero)
    
    class Meta:
        verbose_name_plural = "Apartamentos"


class Visitante(models.Model):
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
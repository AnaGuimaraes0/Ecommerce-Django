from django.db import models

class RelatorioVendas(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    faturamento_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        permissions = [
            ('view_relatorio_vendas', 'Pode visualizar o faturamento')
        ]

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    birth_time = models.TimeField(null=True, blank=True)
    birth_city = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.username

class Sign(models.Model):
    name = models.CharField(max_length=20, unique=True)
    element = models.CharField(max_length=20)
    symbol = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
    def calcular_compatibilidade(self, outro_signo):
        """Calcula compatibilidade entre dois signos baseado nos elementos"""
        
        # Tabela de compatibilidade por elemento
        tabela = {
            # FOGO + ?
            ('Fogo', 'Fogo'): 80,
            ('Fogo', 'Ar'): 95,
            ('Fogo', 'Terra'): 50,
            ('Fogo', 'Água'): 45,
            
            # TERRA + ?
            ('Terra', 'Terra'): 85,
            ('Terra', 'Água'): 90,
            ('Terra', 'Ar'): 55,
            ('Terra', 'Fogo'): 50,
            
            # AR + ?
            ('Ar', 'Ar'): 80,
            ('Ar', 'Água'): 60,
            ('Ar', 'Fogo'): 95,
            ('Ar', 'Terra'): 55,
            
            # ÁGUA + ?
            ('Água', 'Água'): 90,
            ('Água', 'Fogo'): 45,
            ('Água', 'Terra'): 90,
            ('Água', 'Ar'): 60,
        }
        
        # Busca compatibilidade (ordem não importa)
        chave1 = (self.element, outro_signo.element)
        chave2 = (outro_signo.element, self.element)
        
        if chave1 in tabela:
            return tabela[chave1]
        elif chave2 in tabela:
            return tabela[chave2]
        
        # Compatibilidade padrão
        return 70
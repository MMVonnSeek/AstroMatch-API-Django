import os
import sys
import django

# Configurar o ambiente Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
django.setup()

from core.models import Sign

def run():
    signs_data = [
        # FOGO
        {'name': 'Áries', 'element': 'Fogo', 'symbol': '♈'},
        {'name': 'Leão', 'element': 'Fogo', 'symbol': '♌'},
        {'name': 'Sagitário', 'element': 'Fogo', 'symbol': '♐'},
        
        # TERRA
        {'name': 'Touro', 'element': 'Terra', 'symbol': '♉'},
        {'name': 'Virgem', 'element': 'Terra', 'symbol': '♍'},
        {'name': 'Capricórnio', 'element': 'Terra', 'symbol': '♑'},
        
        # AR
        {'name': 'Gêmeos', 'element': 'Ar', 'symbol': '♊'},
        {'name': 'Libra', 'element': 'Ar', 'symbol': '♎'},
        {'name': 'Aquário', 'element': 'Ar', 'symbol': '♒'},
        
        # ÁGUA
        {'name': 'Câncer', 'element': 'Água', 'symbol': '♋'},
        {'name': 'Escorpião', 'element': 'Água', 'symbol': '♏'},
        {'name': 'Peixes', 'element': 'Água', 'symbol': '♓'},
    ]
    
    for data in signs_data:
        sign, created = Sign.objects.get_or_create(
            name=data['name'],
            defaults={
                'element': data['element'],
                'symbol': data['symbol']
            }
        )
        if created:
            print(f'✅ Criado: {sign.name} {sign.symbol}')
        else:
            print(f'⚠️ Já existe: {sign.name}')

    print(f'\n📊 Total de signos no banco: {Sign.objects.count()}')

if __name__ == '__main__':
    run()

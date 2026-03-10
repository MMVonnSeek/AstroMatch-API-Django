from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Sign
from .serializers import SignSerializer

class SignViewSet(viewsets.ModelViewSet):
    queryset = Sign.objects.all()
    serializer_class = SignSerializer
    
    @action(detail=True, methods=['get'])
    def compatibilidade(self, request, pk=None):
        """Endpoint para calcular compatibilidade entre signos"""
        signo1 = self.get_object()
        signo2_id = request.query_params.get('com')
        
        if not signo2_id:
            return Response({'erro': 'Parâmetro "com" é obrigatório'}, status=400)
        
        try:
            signo2 = Sign.objects.get(pk=signo2_id)
            
            # Calcular compatibilidade
            compat = signo1.calcular_compatibilidade(signo2)
            
            # Mensagens personalizadas baseadas na pontuação
            if compat >= 90:
                mensagem = "🔥 COMBINAÇÃO PERFEITA! Muita química e sintonia!"
                cor = "#4CAF50"
            elif compat >= 80:
                mensagem = "💕 Excelente compatibilidade! Muito potencial!"
                cor = "#8BC34A"
            elif compat >= 70:
                mensagem = "✨ Boa compatibilidade! Vale a pena investir."
                cor = "#FFC107"
            elif compat >= 60:
                mensagem = "🤔 Compatibilidade média. Tem desafios, mas pode dar certo."
                cor = "#FF9800"
            else:
                mensagem = "💔 Compatibilidade baixa. Precisam de muito diálogo."
                cor = "#F44366"
            
            return Response({
                'signo1': {
                    'id': signo1.id,
                    'nome': signo1.name,
                    'elemento': signo1.element,
                    'simbolo': signo1.symbol
                },
                'signo2': {
                    'id': signo2.id,
                    'nome': signo2.name,
                    'elemento': signo2.element,
                    'simbolo': signo2.symbol
                },
                'compatibilidade': compat,
                'mensagem': mensagem,
                'cor': cor,
                'dica': get_dica_por_elemento(signo1.element, signo2.element)
            })
            
        except Sign.DoesNotExist:
            return Response({'erro': 'Signo não encontrado'}, status=404)

def get_dica_por_elemento(e1, e2):
    """Retorna dica baseada nos elementos"""
    dicas = {
        ('Fogo', 'Fogo'): "Muita paixão! Cuidado com o ego de ambos.",
        ('Fogo', 'Ar'): "Combinação explosiva! Muita criatividade juntos.",
        ('Fogo', 'Terra'): "Equilíbrio entre ação e estabilidade.",
        ('Fogo', 'Água'): "Paixão e emoção - podem se completar ou se afogar.",
        ('Terra', 'Terra'): "Estabilidade e segurança. Relação sólida.",
        ('Terra', 'Água'): "Terra fértil! Muito potencial de crescimento.",
        ('Terra', 'Ar'): "Prático com intelectual - aprendizado mútuo.",
        ('Ar', 'Ar'): "Muita conversa e ideias. Nunca entediantes.",
        ('Ar', 'Água'): "Emoções e razão - equilíbrio delicado.",
        ('Água', 'Água'): "Conexão profunda. Cuidado com melodrama.",
    }
    
    chave = (e1, e2)
    if chave in dicas:
        return dicas[chave]
    return "Respeitem as diferenças e celebrem as semelhanças."
<div align="center">
  <h1>ASTROMATCH API</h1>
  <p><strong>Descubra a compatibilidade entre os signos do zodíaco com uma API elegante e intuitiva</strong></p>
  
 
  <img src="https://img.shields.io/badge/Autor-Max Muller-darkblue?style=for-the-badge&logo=" alt="MMVonnSeek">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Django-4.2-green?style=for-the-badge&logo=django" alt="Django">
  <img src="https://img.shields.io/badge/DRF-3.15-red?style=for-the-badge" alt="DRF">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">

  
  <br>
  <br>
  
 <img width="1838" height="934" alt="Screenshot" src="https://github.com/user-attachments/assets/0a4984c4-5a57-4983-be2c-349e564a5e16" />

  <p><em>Interface bonita e intuitiva para visualizar todos os signos</em></p>
</div>

---

## SOBRE O PROJETO

AstroMatch é uma API RESTful completa de astrologia que permite consultar informações sobre os signos do zodíaco e calcular a compatibilidade entre eles.

**Um projeto especial:** Desenvolvido durante a semana de comemoração ao **Dia das Mulheres**, o projeto foi pensado especialmente para o público feminino - o maior consumidor de conteúdo astrológico. Cada detalhe da interface foi cuidadosamente escolhido para criar uma experiência acolhedora e intuitiva.

**Tecnologia com propósito:** Combinando uma API robusta em Python e Django com uma interface que prioriza a experiência do usuário, este projeto demonstra habilidades avançadas em desenvolvimento full stack, provando que código de qualidade pode andar de mãos dadas com design emocional.

**Open Source:** Este projeto é aberto para colaborações! Se você tem ideias, sugestões ou quer melhorar algo, fique à vontade para contribuir. Toda ajuda é bem-vinda!❤️


## FERRAMENTAS E TECNOLOGIAS UTILIZADAS

### Backend
| Tecnologia | Versão | Para que serve |
|------------|--------|-----------------|
| **Python** | 3.11+ | Linguagem principal |
| **Django** | 4.2.11 | Framework web |
| **Django REST Framework** | 3.15.1 | Criação da API REST |
| **SQLite** | - | Banco de dados |


### Frontend
| Tecnologia | Para que serve |
|------------|-----------------|
| **HTML5** | Estrutura das páginas |
| **CSS3** | Estilização e design responsivo |
| **JavaScript** | Interatividade e consumo da API |
| **Fetch API** | Requisições assíncronas |


### Ferramentas de Desenvolvimento
| Ferramenta | Uso |
|------------|-----|
| **Git** | Controle de versão |
| **Virtualenv** | Isolamento do ambiente Python |
| **VS Code / PyCharm** | Editor de código |

---


##  COMO CLONAR E USAR

###  Pré-requisitos (o que precisa ter instalado)

Você só precisa ter **Python** instalado no computador.  
Para verificar, abra o terminal e digite:
```bash
python --version
```


## PASSO 1: Clonar o repositório


### Abra o terminal e digite:
```bash
git clone https://github.com/MMVonnSeek/AstroMatch-API-Django.git
```

### Entre na pasta do projeto
```bash
cd AstroMatch-API-Django
```
_Se não tiver o Git instalado, baixe o ZIP do projeto e extraia!_



## PASSO 2: Criar ambiente virtual (recomendado)


### No Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

### No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```


## PASSO 3: Instalar as dependências



### Instalar os pacotes necessários
```bash
pip install django djangorestframework
```


### Ou instalar tudo de uma vez (se tiver requirements.txt)
```bash
pip install -r requirements.txt
```


## PASSO 4: Configurar o banco de dados


### Entre na pasta do backend
```bash
cd backend
```

### Criar as tabelas no banco
python manage.py migrate



## PASSO 5: Popular com os signos


```bash
python manage.py shell
```

Dentro do shell Python, cole isso:


```bash

from core.models import Sign
signos = [
 {'name': 'Áries', 'element': 'Fogo', 'symbol': '♈'},
 {'name': 'Touro', 'element': 'Terra', 'symbol': '♉'},
 {'name': 'Gêmeos', 'element': 'Ar', 'symbol': '♊'},
 {'name': 'Câncer', 'element': 'Água', 'symbol': '♋'},
 {'name': 'Leão', 'element': 'Fogo', 'symbol': '♌'},
 {'name': 'Virgem', 'element': 'Terra', 'symbol': '♍'},
 {'name': 'Libra', 'element': 'Ar', 'symbol': '♎'},
 {'name': 'Escorpião', 'element': 'Água', 'symbol': '♏'},
 {'name': 'Sagitário', 'element': 'Fogo', 'symbol': '♐'},
 {'name': 'Capricórnio', 'element': 'Terra', 'symbol': '♑'},
 {'name': 'Aquário', 'element': 'Ar', 'symbol': '♒'},
 {'name': 'Peixes', 'element': 'Água', 'symbol': '♓'},
]
for s in signos:
 Sign.objects.get_or_create(name=s['name'], defaults={'element': s['element'], 'symbol': s['symbol']})
print(f"{Sign.objects.count()} signos criados!")
exit()
```


## PASSO 6: Iniciar o servidor

```bash
python manage.py runserver
```


## PASSO 7: Abrir no navegador

Abra seu navegador e acesse:

http://127.0.0.1:8000/

**PRONTO!** Agora você já pode usar a aplicação!

----------

# COMO USAR A APLICAÇÃO

### Para usuários comuns (interface visual)

1.  **Página inicial** (`http://127.0.0.1:8000/`)
    
    -   Veja todos os 12 signos em cards coloridos
        
    -   Cada elemento tem uma cor diferente:
        
        -    **Fogo**: Vermelho
            
        -    **Terra**: Verde-água
            
        -    **Ar**: Azul
            
        -    **Água**: Verde-claro
          
            
2.  **Detalhes do signo** (clique em qualquer card)
    
    -   Veja o símbolo gigante do signo
        
    -   Descubra a compatibilidade com todos os outros signos
        
    -   Cores indicam o nível de compatibilidade:
        
        -   🟢 **Verde**: Alta (80%+) - Combinação perfeita!
            
        -   🟡 **Amarelo**: Média (60-79%) - Dá para investir
            
        -   🔴 **Vermelho**: Baixa (abaixo 60%) - Desafios pela frente
            


## Para desenvolvedores (API REST)

**Listar todos os signos:**
GET http://127.0.0.1:8000/api/signs/

**Ver detalhes de um signo específico:**
GET http://127.0.0.1:8000/api/signs/1/

_(Troque o 1 pelo ID desejado)_

**Calcular compatibilidade entre dois signos:**
GET http://127.0.0.1:8000/api/signs/1/compatibilidade/?com=5

_(Signo 1 com Signo 5)_


**Tabela de IDs dos signos:**


| ID | Signo | Símbolo |
|----|-------|---------|
| 1 | Áries | ♈ |
| 2 | Leão | ♌ |
| 3 | Sagitário | ♐ |
| 4 | Touro | ♉ |
| 5 | Virgem | ♍ |
| 6 | Capricórnio | ♑ |
| 7 | Gêmeos | ♊ |
| 8 | Libra | ♎ |
| 9 | Aquário | ♒ |
| 10 | Câncer | ♋ |
| 11 | Escorpião | ♏ |
| 12 | Peixes | ♓ |

----------

##  EXEMPLOS DE RESPOSTA DA API

### Lista de signos

[

 {
 
 "id": 1,
 
 "name": "Áries",
 
 "element": "Fogo",
 
 "symbol": "♈"
 
 },
 
 {
 
 "id": 2,
 
 "name": "Leão",
 
 "element": "Fogo",
 
 "symbol": "♌"
 
 }
 
]


### Compatibilidade entre signos

{
 
 "signo1": {
 
 "id": 1,
 
 "nome": "Áries",
 
 "elemento": "Fogo",
 
 "simbolo": "♈"
 
 },
 
 "signo2": {
 
 "id": 5,
 
 "nome": "Virgem",
 
 "elemento": "Terra",
 
 "simbolo": "♍"
 
 },
 
 "compatibilidade": 50,
 
 "mensagem": "💔 Compatibilidade baixa. Precisam de muito diálogo.",
 
 "dica": "Equilíbrio entre ação e estabilidade."
 
}   

----------

### LICENÇA

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](https://LICENSE) para mais detalhes.

----------

### AUTOR

**Professor: Max Muller**
    

----------

#### AGRADECIMENTOS

Se você gostou deste projeto, não esqueça de deixar uma estrela no GitHub! ⭐

----------

<div align="center"> <p> <a href="#top"> Voltar ao topo</a> </p> </div>

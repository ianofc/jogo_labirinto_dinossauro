Jogo do Labirinto com Dinossauro

Este projeto é um jogo simples onde o jogador controla um dinossauro que deve atravessar um labirinto sem tocar nas paredes. O objetivo é guiar o dinossauro do ponto inicial (verde) até o ponto final (vermelho). Se o jogador vencer, será exibida uma mensagem com a opção de reiniciar ou sair.


Requisitos

Para rodar o jogo, você precisa ter o Python e as bibliotecas do Pygame instalados. Abaixo estão os passos para instalar e configurar:


Instalação do Python

Baixe o Python.

Durante a instalação, selecione a opção "Add Python to PATH".


Instalação de dependências

Instale as dependências listadas no arquivo requirements.txt usando o pip:

pip install -r requirements.txt


Como Jogar

Execute o arquivo principal do jogo:

python <nome_do_arquivo>.py

Use as setas do teclado para mover o dinossauro:

Seta para cima: move para cima.

Seta para baixo: move para baixo.

Seta para esquerda: move para a esquerda.

Seta para direita: move para a direita.


Objetivo: Alcance o ponto final (quadrado vermelho) sem tocar nas paredes pretas.


Se você vencer, uma mensagem aparecerá com as opções de:

Reiniciar o jogo (pressione 1).

Sair do jogo (pressione 2).


Arquivos Principais

<nome_do_arquivo>.py: Arquivo principal que contém o código do jogo.

requirements.txt: Lista de dependências do projeto.

dinossauro.png: Imagem do dinossauro usada como sprite.


Regras do Jogo

O dinossauro deve se mover apenas dentro dos caminhos livres (amarelos).

Colisões com as paredes pretas resetam o movimento.

Apenas um caminho garantido leva ao ponto final.


Requisitos Técnicos

Python 3.8 ou superior.

Pygame 2.0 ou superior.


Desenvolvimento Futuro

Adicionar novos tipos de labirinto.

Melhorar os gráficos e sons.

Implementar níveis com dificuldade progressiva.


Contato

Caso tenha dúvidas ou sugestões, entre em contato.


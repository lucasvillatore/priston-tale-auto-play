# Priston Tale Auto Play

O Priston Tale Auto Play não é um bot "pronto para usar" (plug-and-play), mas sim um esqueleto robusto de engenharia de software para quem deseja criar suas próprias rotinas de jogo.

O objetivo deste projeto é resolver os problemas fundamentais de interação com a janela do jogo — como movimentação indetectável e injeção de inputs — permitindo que o desenvolvedor foque apenas na lógica de decisão (estratégia).

# Disclaimer
Este software foi desenvolvido para fins de estudo sobre Visão Computacional, Automação de Inputs e Curvas de Bézier. O uso deste software no jogo oficial pode violar os Termos de Serviço. Use por sua própria conta e risco.

## Funcionalidades Atuais

O núcleo do projeto já conta com uma arquitetura baseada em filas de ações:

- **Sistema de Fila de Prioridade (Priority Queue):** O bot não utiliza loops fixos ou sequenciais. Em vez disso, cada intenção de ação (atacar, curar, coletar) possui um peso de prioridade.
- **Auto Attack:** Identificação e ação de atacar o alvo.
- **Auto Loot:** Rotina para coletar itens do chão.
- **Auto Potion:** Consumo inteligente das poções (Slots 1, 2 e 3).
- **Re-stock:** Ação automatizada para encher o bracelete de poções usando o inventário.

## Orquestrador de ações (WIP)

A lógica de decisão central ("o cérebro do bot") está em fase de planejamento e desenvolvimento. O objetivo não é criar scripts lineares, mas sim um sistema reativo baseada em Visão Computacional.

A arquitetura planejada para o Ciclo de Decisão segue 4 etapas:
1. Captura Visual (Snapshot): Um modelo de IA/Visão Computacional captura o frame atual da janela do jogo.
2. Extração de Contexto: O sistema processa a imagem para extrair informações vitais (Nível de HP/MP, presença de monstros, itens raros no chão, status dos buffs).
3. Fila de Prioridades (Heurística): Com base nos dados extraídos, as ações são inseridas em uma fila dinâmica.
4. Execução: O consumidor da fila retira a ação de maior prioridade e delega para os controladores de Mouse/Teclado executarem.


## Controle do Mouse

Um dos maiores desafios em bots é evitar a detecção por comportamento robótico (movimentos lineares perfeitos).

Para resolver isso, este projeto utiliza as bibliotecas win32api e win32con para interagir em baixo nível com o Windows. Foi implementado um algoritmo de Curvas de Bézier Quadráticas combinado com funções de Easing para suavização de movimento.
Nessa implementação, temos:

- **Trajetória não-linear:** O mouse nunca viaja em linha reta perfeita. Ele cria um arco natural usando pontos de controle aleatórios.
- **Velocidade Variável:** O cursor acelera e desacelera durante o trajeto (easing), simulando a inércia da mão humana.
- **Randimização:** O início, o fim e o tempo de cada movimento possuem variações aleatórias (min_delay, max_delay) para garantir que nenhum clique seja idêntico ao anterior.

## Controle de Teclado

Para a manipulação do teclado, o projeto foge de bibliotecas de alto nível que muitas vezes falham em jogos com proteção (como DirectX/DirectInput). Foi implementado chamadas diretas de eventos de hardware via win32api.

Isso permite um controle granular sobre o estado das teclas, possibilitando:

- **Pressão e Liberação (Key Down/Key Up):** Controle exato do tempo que a tecla fica pressionada.
- **Combos (Hold Sequence):** Capacidade de segurar uma tecla (como Shift ou Ctrl) enquanto executa uma sequência de outras teclas, essencial para atalhos de troca de barra de skills ou comandos específicos do jogo.
- **Input Humano:** Delays configuráveis entre o pressionar e o soltar, evitando inputs instantâneos (0ms) que são fáceis de detectar.

## Detalhes das Ações (Game Actions)

O framework implementa classes específicas para lidar com as mecânicas repetitivas do jogo. Cada ação é projetada para ser atômica e configurável.

### Auto Attack (pronto para uso)

Recebe uma coordenada alvo (X, Y) 

- Execução: Move o cursor suavemente até o alvo e executa um clique com o Botão Direito do mouse (skill ativa).

### Auto Loot (pronto para uso)

Gerencia a coleta de itens do chão, priorizando a segurança do movimento
- Pressiona e segura a tecla A (comando nativo de travar mira/movimento forçado).
- Move o cursor até a localização do item.
- Executa um clique com o Botão Esquerdo.
- Solta a tecla A após a confirmação da ação.

### Rebuff (necessário atualização)

Sistema de manutenção de buffs do personagem. Itera sobre a lista de teclas de atalho configuradas (ex: F1 a F8).

- Execução: Para cada buff, seleciona a tecla correspondente e clica com o Botão Direito no próprio personagem ou na área vazia (dependendo da skill) para ativar o efeito.

Nesse ponto, precisa configurar qual são as teclas de buff necessárias para utilizar.

### Auto Potion (pronto para uso)

- Execução: Aciona as teclas 1, 2 ou 3 individualmente.

### Refill (necessário atualização)

Automação para reabastecer o cinto de poções usando o inventário.

- Execução: Utiliza a classe KeyboardDevice para segurar a tecla SHIFT (modificador) e pressiona sequencialmente 1, 2 ou 3, movendo pilhas inteiras de poções do inventário para o cinto instantaneamente.

Nesse ponto, precisa identificar onde está as poções no inventário para dar como coordenada para o bot.

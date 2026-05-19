# 🐍 Snake Game — Terminal

Jogo da cobrinha clássico rodando diretamente no terminal, desenvolvido em Python com a biblioteca `curses`.

## 📋 Sobre o Projeto

Implementação do clássico jogo Snake sem dependências externas, utilizando a biblioteca nativa `curses` para renderização no terminal. O projeto explora conceitos de lógica de jogo, manipulação de estado, detecção de colisão e controle de entrada em tempo real.

## ✨ Funcionalidades

- 5 níveis de dificuldade selecionáveis antes de iniciar a partida
- Controle da cobra pelas setas do teclado
- Detecção de colisão com bordas e com o próprio corpo
- Crescimento da cobra ao comer frutas
- Prevenção de movimento reverso (não é possível ir na direção oposta)
- Exibição da pontuação final ao fim da partida

## 🛠️ Tecnologias

- Python 3
- `curses` (biblioteca nativa do Python)

## ▶️ Como Executar

**Pré-requisito:** Python 3 instalado.

> ⚠️ O módulo `curses` é nativo no Linux e macOS. No Windows, é necessário instalar o pacote `windows-curses`:
> ```bash
> pip install windows-curses
> ```

**Clone o repositório e execute:**

```bash
git clone https://github.com/juan-borinelli/snake_game.git
cd snake_game
python py_snake.py
```

Ao iniciar, selecione a dificuldade digitando um número de 1 a 5:

| Nível | Velocidade |
|-------|-----------|
| 1     | Muito lenta |
| 2     | Lenta |
| 3     | Média |
| 4     | Rápida |
| 5     | Muito rápida |

## 🎮 Controles

| Tecla | Ação |
|-------|------|
| ↑ ↓ ← → | Mover a cobra |

## 📁 Estrutura do Projeto

```
snake_game/
└── py_snake.py   # Código principal do jogo
```

## 📚 Aprendizados

- Uso da biblioteca `curses` para I/O no terminal
- Modelagem de estado de jogo com listas mutáveis
- Lógica de movimentação e colisão
- Controle de tempo real com `timeout` e `getch`
- Organização do código em funções reutilizáveis

---

Desenvolvido por [Juan Borinelli](https://github.com/juan-borinelli)
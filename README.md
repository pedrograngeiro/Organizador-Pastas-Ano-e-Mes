# Organizador de Arquivos DEJT por Região, Ano e Mês

Este repositório contém um script Python que organiza os arquivos de uma estrutura de pastas do DEJT (Diário Eletrônico da Justiça do Trabalho), identificando informações no nome dos arquivos e movendo-os para uma nova estrutura de pastas organizada por **Região**, **Ano** e **Mês**.

## Estrutura Original

A estrutura de pastas de origem segue o seguinte formato:

```
DEJT/
│
├── 2023/
│   ├── 01/
│   │   └── TRT_Administrativo_Caderno_do_TRT_da_8a_Regiao_2023_01_11.pdf
│   ├── 02/
│   │   └── TRT_Administrativo_Caderno_do_TRT_da_5a_Regiao_2023_02_15.pdf
│   └── ...
├── 2024/
│   └── 01/
│       └── TRT_Administrativo_Caderno_do_TRT_da_10a_Regiao_2024_01_10.pdf
└── ...

```

Cada arquivo possui um nome no formato:

```
TRT_Administrativo_Caderno_do_TRT_da_Xa_Regiao_YYYY_MM_DD.pdf
```

- Xa Regiao: Número da região do TRT (ex: "8a Regiao").
- YYYY: Ano do arquivo (ex: "2023").
- MM: Mês do arquivo (ex: "01" para janeiro).
- DD: Dia do arquivo (ex: "11").

# Funcionalidade do Script
O script percorre todas as pastas de anos e meses, e para cada arquivo que segue o padrão de nome, ele:

1. Identifica o número da região (ex: 8ª Região).
2. Identifica o ano e mês a partir do nome do arquivo e da estrutura de pastas.
3. Move o arquivo para uma nova estrutura de pastas, organizada da seguinte forma:

```
DEJT_Organizado/
│
├── TRT_05/
│   ├── 2023/
│   │   └── 02/
│   │       └── TRT_Administrativo_Caderno_do_TRT_da_5a_Regiao_2023_02_15.pdf
│   └── ...
├── TRT_08/
│   ├── 2023/
│   │   └── 01/
│   │       └── TRT_Administrativo_Caderno_do_TRT_da_8a_Regiao_2023_01_11.pdf
│   └── ...
└── ...
```

### Requisitos
- Python 3.7+
- Biblioteca padrão do Python (os, shutil, re).

### Como Usar
1. **Clone este repositório**:

   ```bash
   git clone https://github.com/seu-usuario/dejt-organizer.git
   cd dejt-organizer
2. **Configure a pasta de origem:** Certifique-se de que a pasta DEJT está localizada no mesmo diretório que o script ou ajuste o caminho da variável pasta_origem no código.
3. **Execute o script:**
Execute o script organizar_dejt.py que moverá os arquivos para a nova estrutura:
```
python organizar_dejt.py
```
4. **Verifique a pasta** DEJT_Organizado:_ Após a execução, os arquivos serão movidos para a pasta DEJT_Organizado, organizados por região, ano e mês.


## Observações
- O script move os arquivos da estrutura original para a nova estrutura. Se preferir apenas copiar os arquivos, substitua a função shutil.move() por shutil.copy2() no código.
- Certifique-se de que os nomes dos arquivos seguem o padrão esperado. Caso contrário, eles não serão movidos.

## Exemplo de Execução
Para um arquivo com o nome TRT_Administrativo_Caderno_do_TRT_da_8a_Regiao_2023_01_11.pdf localizado na pasta 2023/01/, o script irá movê-lo para a seguinte estrutura:

```
DEJT_Organizado/
└── TRT_08/
    └── 2023/
        └── 01/
            └── TRT_Administrativo_Caderno_do_TRT_da_8a_Regiao_2023_01_11.pdf

```

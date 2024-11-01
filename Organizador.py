import os
import re
import shutil

pasta_origem = "/mnt/dmlocal/dados/DEJT/txt"
pasta_destino = "/mnt/dmlocal/dados/DEJT/Organizado"

# Expressão regular para capturar a região e a data
regex_trt = r"TRT_da_([0-9]+)a_Regiao_(\d{4})_(\d{2})_(\d{2})"

if not os.path.exists(pasta_origem):
    os.makedirs(pasta_destino)

for ano in os.listdir(pasta_origem):
    caminho_ano = os.path.join(pasta_origem, ano)
    if os.path.isdir(caminho_ano):
        for mes in os.listdir(caminho_ano):
            caminho_mes = os.path.join(caminho_ano, mes)
            if os.path.isdir(caminho_mes):
                for arquivo in os.listdir(caminho_mes):
                    match = re.search(regex_trt, arquivo)
                    if match:
                        numero_regiao = match.group(1).zfill(2)  # Preenche com zero à esquerda se necessário
                        regiao = f"TRT{numero_regiao}"
                        ano_arquivo = match.group(2)
                        mes_arquivo = mes

                        destino_final = os.path.join(pasta_destino, regiao, ano_arquivo, mes_arquivo)
                        if not os.path.exists(destino_final):
                            os.makedirs(destino_final)

                        caminho_arquivo = os.path.join(caminho_mes, arquivo)
                        caminho_destino = os.path.join(destino_final, arquivo)

                        shutil.move(caminho_arquivo, caminho_destino)
                        print(f"Arquivo {arquivo} movido para {caminho_destino}")
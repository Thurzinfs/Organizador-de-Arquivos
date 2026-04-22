import os

import shutil

from app.domain.repositories import IOrganizadorDiretorio

from dotenv import load_dotenv

load_dotenv()


class OrganizadorDiretorio(IOrganizadorDiretorio):
    def __init__(self) -> None:
        self._diretorio: str = os.getenv('CAMINHO_DIRETORIO', '')
        self.pastas_atuais: list = []
        self.arquivos_atuais: list = []
        self.pasta_default = 'OUTROS'
        self.organizar_imagens: list = [
            '.PNG',
            '.JPEG',
            '.SVG',
            '.JPG',
            '.GIF',
        ]

    @property
    def DIRETORIO(self) -> str:
        return self._diretorio

    def listar_pastas_diretorio(self):
        try:
            self.limpar_pastas_vazias()

            sistema = os.listdir(self.DIRETORIO)
            pastas = []

            for componente in sistema:
                caminho = os.path.join(self.DIRETORIO, componente)

                if os.path.isdir(caminho):
                    pastas.append(componente.upper())

            self.pastas_atuais = pastas

        except Exception as e:
            print(f'Error na funcao listar pastas: {e}')

    def listar_arquivos_livres(self):
        try:
            sistema = os.listdir(self.DIRETORIO)
            arquivos = []

            for arquivo in sistema:
                caminho_arquivos = os.path.join(self.DIRETORIO, arquivo)

                if os.path.isfile(caminho_arquivos):
                    _, extensao = os.path.splitext(arquivo)
                    extensao_upper = extensao.upper()

                    if extensao_upper in self.organizar_imagens:
                        arquivos.append((arquivo, 'IMAGENS'))

                    elif extensao:
                        arquivos.append(
                            (arquivo, extensao_upper.removeprefix('.'))
                        )

                    else:
                        arquivos.append((arquivo, self.pasta_default))

            self.arquivos_atuais = arquivos

        except Exception as e:
            print(f'Error na funcao listar arquivos: {e}')

    def mover_arquivo_para_pasta(self, arquivo: str, pasta: str):
        try:
            ORIGEM_ARQUIVO = os.path.join(self.DIRETORIO, arquivo)

            DIRETORIO_PASTA = os.path.join(self.DIRETORIO, pasta)

            DIRETORIO_ALVO = os.path.join(DIRETORIO_PASTA, arquivo)

            os.makedirs(DIRETORIO_PASTA, exist_ok=True)

            if os.path.exists(ORIGEM_ARQUIVO):
                shutil.move(ORIGEM_ARQUIVO, DIRETORIO_ALVO)

        except Exception as e:
            print(f'Error na funcao mover arquivo: {e}')

    def criar_pasta(self, pasta: str):
        DIRETORIO_PASTA = os.path.join(self.DIRETORIO, pasta.upper())

        try:

            os.makedirs(DIRETORIO_PASTA, exist_ok=True)

            if os.path.exists(DIRETORIO_PASTA):
                return DIRETORIO_PASTA

        except FileExistsError:
            return DIRETORIO_PASTA

        except Exception as e:
            print(f'Error na funcao listar pastas: {e}')

        return DIRETORIO_PASTA

    def limpar_pastas_vazias(self):
        sistema: list = os.listdir(self.DIRETORIO)

        pastas_vazias = [
            pasta
            for pasta in sistema
            if os.path.isdir(os.path.join(self.DIRETORIO, pasta))
            and len(os.listdir(os.path.join(self.DIRETORIO, pasta))) == 0
        ]

        for vazia in pastas_vazias:
            caminho = os.path.join(self.DIRETORIO, vazia)
            os.rmdir(caminho)

    def executar(self):
        self.listar_pastas_diretorio()
        self.listar_arquivos_livres()

        for arquivo in self.arquivos_atuais:
            extensao = arquivo[1]
            nome_arquivo = arquivo[0]

            if extensao not in self.pastas_atuais:
                self.criar_pasta(extensao)
                self.pastas_atuais.append(extensao)

            self.mover_arquivo_para_pasta(nome_arquivo, extensao)

        self.limpar_pastas_vazias()

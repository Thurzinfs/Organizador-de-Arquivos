from abc import ABC, abstractmethod

from watchdog.events import (
    DirCreatedEvent,
    FileCreatedEvent,
    FileSystemEventHandler,
)


class IOrganizadorDiretorio(ABC):
    @property
    @abstractmethod
    def DIRETORIO(self) -> str:
        ...

    @abstractmethod
    def listar_pastas_diretorio(self):
        ...

    @abstractmethod
    def listar_arquivos_livres(self):
        ...

    @abstractmethod
    def mover_arquivo_para_pasta(self, arquivo: str, pasta: str):
        ...

    @abstractmethod
    def criar_pasta(self, pasta: str):
        ...

    @abstractmethod
    def executar(self):
        ...


class IServiceMonitoramento(FileSystemEventHandler):
    def __init__(self, organizador: IOrganizadorDiretorio) -> None:
        super().__init__()
        self.organizador = organizador

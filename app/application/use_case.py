from domain.repositories import (
    IOrganizadorDiretorio,
    IServiceMonitoramento,
)

from watchdog.observers import Observer

from time import sleep

from typing import Type


class ExecuteAutomationFileUseCase:
    def __init__(
        self,
        organizador: IOrganizadorDiretorio,
        service_monitoramento: Type[IServiceMonitoramento],
    ) -> None:
        self.DIRETORIO = organizador.DIRETORIO
        self.ORGANIZADOR = organizador
        self.service_monitorador = service_monitoramento

    def execute(self):
        self.ORGANIZADOR.executar()

        event_handler = self.service_monitorador(organizador=self.ORGANIZADOR)

        observer = Observer()

        observer.daemon = True

        observer.schedule(event_handler, path=self.DIRETORIO, recursive=False)

        observer.start()

        print('-----Iniciando-------')

        try:
            while True:
                sleep(2)

        except KeyboardInterrupt:
            observer.stop()

        observer.join()

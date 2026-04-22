from watchdog.events import (
    DirCreatedEvent,
    FileCreatedEvent,
)

from domain.repositories import (
    IOrganizadorDiretorio,
    IServiceMonitoramento,
)

from threading import Thread

from time import sleep


class MonitoradorDiretorio(IServiceMonitoramento):
    def __init__(self, organizador: IOrganizadorDiretorio) -> None:
        self.organizar = organizador

    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
        print(
            f'Evento detectado: {event.event_type} no caminho {event.src_path}'
        )
        if not event.is_directory:
            print('Executando')

            thread = Thread(target=self.executar_com_atraso)
            thread.daemon = True
            thread.start()

    def executar_com_atraso(self):
        sleep(1)
        self.organizar.executar()

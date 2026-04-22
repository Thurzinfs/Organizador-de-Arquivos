from app.application.use_case import ExecuteAutomationFileUseCase
from app.infrastructure.repository import OrganizadorDiretorio
from app.infrastructure.services import MonitoradorDiretorio


use_case = ExecuteAutomationFileUseCase(
    organizador=OrganizadorDiretorio(),
    service_monitoramento=MonitoradorDiretorio,
)

if __name__ == '__main__':
    use_case.execute()

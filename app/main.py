from application.use_case import ExecuteAutomationFileUseCase
from infrastructure.repository import OrganizadorDiretorio
from infrastructure.services import MonitoradorDiretorio


use_case = ExecuteAutomationFileUseCase(
    organizador=OrganizadorDiretorio(),
    service_monitoramento=MonitoradorDiretorio,
)

if __name__ == '__main__':
    use_case.execute()

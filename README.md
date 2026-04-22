# Organizador de Diretório por Extensão

Uma automação de arquivos que organiza e monitora um diretório local, movendo arquivos para pastas por extensão e mantendo o diretório sempre limpo.

---

## 📝 Descrição

Este projeto implementa uma aplicação Python que:  
- Organiza arquivos dentro de um diretório definido por extensão;  
- Cria pastas automaticamente para cada tipo de arquivo;  
- Detecta novos arquivos criados no diretório e reorganiza automaticamente.

A solução é ideal para manter pastas de download, desktop ou qualquer diretório de trabalho organizado sem intervenção manual.

---

## 🛠 Tecnologias / Ferramentas

- Python 3.12+  
- [watchdog](https://pypi.org/project/watchdog/) (Monitoramento de eventos de sistema)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (Gerenciamento de variáveis de ambiente)
- [PyInstaller](https://pyinstaller.org/) (Criação de executáveis)
- Shutil / Pathlib (Manipulação de arquivos e caminhos)

---

## 🏛 Arquitetura e Padrões

O projeto segue princípios de **Clean Architecture** para separar responsabilidades:  
- `app/application` — Caso de uso principal (`ExecuteAutomationFileUseCase`) que orquestra a inicialização.  
- `app/domain` — Interfaces e abstrações (Portas).  
- `app/infrastructure` — Implementações concretas (Adaptadores) para organização e serviços de monitoramento.
- `run.py` — Ponto de entrada (Entry Point) para garantir a resolução correta de caminhos no ambiente de produção.

---

## 🚀 Como utilizar (Desenvolvimento)

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Thurzinfs/seu-repositorio.git](https://github.com/Thurzinfs/seu-repositorio.git)
   cd _PYTHON
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   Crie um arquivo `.env` na raiz do projeto:
   ```
   CAMINHO_DIRETORIO=/home/usuario/Downloads
   ```

5. **Execute a aplicação:**
   ```bash
   python run.py
   ```

---

## 📦 Empacotamento e Automação (Linux)

Para que a automação rode como um serviço do sistema que inicia automaticamente com o computador, siga os passos abaixo:

### 1. Gerar o executável nativo

Com o ambiente virtual ativo, gere o binário:

```bash
pyinstaller --noconfirm --onedir --name "Orquestrador de Diretorio" --paths ./app run.py
```

O resultado estará disponível na pasta `dist/Orquestrador de Diretorio`.

### 2. Configurar como Serviço do Sistema (Systemd)

Crie um arquivo de configuração para o sistema:

```bash
sudo nano /etc/systemd/system/automacao.service
```

Cole o conteúdo abaixo (ajustando o campo User e os caminhos):

```ini
[Unit]
Description=Servico de Automacao Python
After=network.target

[Service]
User=seu_usuario_linux
WorkingDirectory=/home/seu_usuario/Documentos/ESTUDO/_PYTHON/dist/Orquestrador de Diretorio
ExecStart="/home/seu_usuario/Documentos/ESTUDO/_PYTHON/dist/Orquestrador de Diretorio/Orquestrador de Diretorio"
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### 3. Ativar e Monitorar

```bash
## Recarregar as configurações
sudo systemctl daemon-reload

## Habilitar para iniciar com o sistema
sudo systemctl enable automacao.service

## Iniciar agora
sudo systemctl start automacao.service

## Verificar status e logs
sudo systemctl status automacao.service
journalctl -u automacao.service -f
```

---

## 📁 Estrutura de Pastas Organizadas

- **IMAGENS**: PNG, JPEG, SVG, JPG, GIF.
- **OUTROS**: Arquivos sem extensão detectada.
- **EXTENSÃO**: Pastas criadas dinamicamente (Ex: PDF, TXT, MP3).

---

## 📞 Contato

**Autor** — Arthur França Silva

**E-mail** — arthurfranca.dev@gmail.com

**GitHub** — @Thurzinfs

<div align="center">
Desenvolvido com ❤️ por <a href="https://github.com/Thurzinfs">Arthur França Silva</a>
</div>
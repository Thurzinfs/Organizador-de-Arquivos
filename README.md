# Organizador de Diretório por Extensão

Um automação de arquivos que organiza e monitora um diretório local, movendo arquivos para pastas por extensão e mantendo o diretório sempre limpo.

---

## Descrição

Este projeto implementa uma aplicação Python que:  
- organiza arquivos dentro de um diretório definido por extensão;  
- cria pastas automaticamente para cada tipo de arquivo;  
- detecta novos arquivos criados no diretório e reorganiza automaticamente.

A solução é ideal para manter pastas de download, desktop ou qualquer diretório de trabalho organizado sem intervenção manual.

---

## Tecnologias / Ferramentas

- Python 3.10+  
- watchdog  
- python-dotenv  
- shutil  
- pathlib / os  

---

## Sobre a arquitetura e padrões

O projeto está organizado em camadas claras para separar responsabilidades:  
- `app/application` — caso de uso principal (`ExecuteAutomationFileUseCase`) que orquestra a inicialização e o monitoramento.  
- `app/domain` — contratos (interfaces/abstrações) usados pela aplicação; define as portas do sistema.  
- `app/infrastructure` — implementações concretas de organização de diretório e monitoramento de eventos.

Padrões e princípios aplicados:  
- `Dependency Inversion` — o `UseCase` depende de abstrações em vez de implementações diretas.  
- `Ports and Adapters` — a camada de domínio define interfaces e a infraestrutura fornece as adaptações reais.  
- `Event-driven` — o diretório é observado por eventos (`watchdog`) e toda vez que um arquivo é criado, a organização é acionada.

---

## Como utilizar

1. Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd _PYTHON
```

2. Crie e ative um ambiente virtual (recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install watchdog python-dotenv
```

4. Crie um arquivo `.env` na raiz do projeto com o caminho do diretório que será monitorado:

```env
CAMINHO_DIRETORIO=/caminho/para/seu/diretorio
```

5. Execute a aplicação:

```bash
python app/main.py
```

6. Coloque arquivos dentro do diretório definido em `CAMINHO_DIRETORIO` e observe a organização automática.

---

## O que a aplicação organiza

- arquivos de imagem são movidos para a pasta `IMAGENS` (PNG, JPEG, SVG, JPG, GIF)  
- arquivos com outras extensões são movidos para pastas nomeadas pela extensão (por exemplo, `PDF`, `TXT`, `MP3`)  
- arquivos sem extensão são movidos para a pasta `OUTROS`

---

## Estrutura do projeto

- `app/main.py` — ponto de entrada da aplicação.  
- `app/application/use_case.py` — caso de uso principal que inicializa o observador.  
- `app/domain/repositories.py` — contratos de abstração para o organizador e o monitor.  
- `app/infrastructure/repository.py` — lógica de organização e movimentação de arquivos.  
- `app/infrastructure/services.py` — monitoramento de criação de arquivos e disparo da organização.

---

## 📞 Contato

- **Autor** — Arthur França Silva
- **E-mail** — arthurfranca.dev@gmail.com
- **GitHub** — [@Thurzinfs](https://github.com/Thurzinfs)

---

<div align="center">
  Desenvolvido com ❤️ por <a href="https://github.com/Thurzinfs">Arthur França Silva</a>
</div>
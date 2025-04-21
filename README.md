# NASA Astronomy Picture of the Day (APOD) Viewer

Este projeto é uma aplicação simples em Python que usa a [API Astronomy Picture of the Day (APOD)](https://api.nasa.gov/) da NASA para exibir a Imagem Astronômica do Dia. A aplicação faz uma requisição à API, recupera os dados e exibe o título e a explicação da imagem ou vídeo do dia. Se for uma imagem, ela será aberta no navegador.

## Funcionalidades

- Conecta-se à API da NASA para obter a Imagem Astronômica do Dia.
- Exibe o título e a explicação da imagem ou vídeo.
- Abre a imagem ou vídeo diretamente no navegador.
- O programa só exibe imagens e abre o navegador para visualização.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação utilizada para o desenvolvimento do script.
- **requests**: Biblioteca Python para fazer requisições HTTP à API da NASA.
- **webbrowser**: Biblioteca Python para abrir a URL da imagem/vídeo diretamente no navegador.
- **python-dotenv**: Biblioteca para carregar variáveis de ambiente a partir de um arquivo `.env`, onde a chave de API da NASA será armazenada de forma segura.

## Pré-requisitos

1. **Chave de API da NASA**:
   - Para usar este programa, você precisa obter uma chave de API gratuita da NASA. Vá até [https://api.nasa.gov/](https://api.nasa.gov/) e registre-se para obter a chave.
2. **Dependências**:
   - Este projeto usa as bibliotecas `requests` e `python-dotenv`. Elas podem ser instaladas com o comando abaixo.

## Como Instalar e Configurar

### 1. Obtenha a chave de API da NASA

Vá até [https://api.nasa.gov/](https://api.nasa.gov/) e registre-se para obter uma chave de API gratuita.

### 2. Configure o arquivo `.env`

Crie um arquivo chamado `.env` na raiz do seu projeto e adicione a chave de API da NASA no seguinte formato:

```env
API_KEY=sua_chave_de_api_aqui
```

### 3. Instale as dependências

Execute o seguinte comando para instalar as dependências:

```bash
pip install -r requirements.txt
```

### 4. Execute o Script

Com o arquivo `.env` configurado e as dependências instaladas, você pode executar o script principal. O código faz uma requisição à API e exibe o título e a explicação da imagem, além de abrir a imagem no seu navegador.

```bash
python apod_viewer.py
```

Se o script funcionar corretamente, você verá o título e a explicação da Imagem Astronômica do Dia no terminal e a imagem será aberta automaticamente no seu navegador.

## Estrutura do Projeto

```
nasa-apod-viewer/
│
├── apod_viewer.py          # Script principal que faz a requisição à API e exibe os resultados
├── .env                    # Arquivo de variáveis de ambiente com a chave da API
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
```

## Como Funciona

1. **Carregamento da Chave da API**: O programa carrega a chave de API da NASA a partir do arquivo `.env` utilizando a biblioteca `python-dotenv`.
2. **Requisição à API**: Ele faz uma requisição HTTP à API da NASA utilizando a biblioteca `requests`. A URL da API é construída com a chave de API fornecida.
3. **Processamento dos Dados**: Se a requisição for bem-sucedida (status 200), o programa verifica se o conteúdo retornado é uma imagem. Se for, ele exibe o título e a explicação da imagem e a abre no navegador.
4. **Exibição no Navegador**: A URL da imagem ou vídeo é aberta no navegador padrão utilizando a biblioteca `webbrowser`.

## Exemplo de Saída

Se o código for executado corretamente, a saída no terminal será algo assim:

```
Título: A vista incrível do planeta Saturno
Explicação: Esta imagem foi capturada pela sonda Cassini da NASA, mostrando Saturno em todo o seu esplendor...
```

Além disso, o navegador será aberto com a imagem ou vídeo do dia.

## Licença

Este projeto está licenciado sob a MIT License - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Se tiver alguma dúvida ou sugestão, sinta-se à vontade para abrir uma issue ou contribuir com o projeto!

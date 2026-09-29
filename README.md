# 🌐 LinguaFlow — AI-Powered Translator

Aplicação web de tradução de textos desenvolvida em Python, utilizando a API da OpenAI e o Streamlit.

## Sobre o projeto

O LinguaFlow permite traduzir textos por meio de inteligência artificial, com uma interface web personalizada. O projeto foi desenvolvido para explorar a integração de modelos de linguagem em aplicações Python.

## Funcionalidades

- Tradução de textos utilizando o modelo GPT-4.1 mini
- Detecção automática do idioma de origem
- Seleção e inversão dos idiomas
- Interface web personalizada com Streamlit
- Opção para copiar a tradução
- Reprodução da tradução por voz, utilizando recursos do navegador
- Limite de 5.000 caracteres para o texto de entrada

## Tecnologias utilizadas

- Python
- OpenAI API
- Streamlit
- HTML e CSS
- JavaScript

## Como executar

**1. Clone o repositório**

Substitua `SEU-USUARIO` e `SEU-REPOSITORIO` pelos dados do repositório no GitHub:

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
cd SEU-REPOSITORIO
```

**2. Crie e ative um ambiente virtual**

No Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**3. Instale as dependências**

```bash
python -m pip install -r requirements.txt
```

**4. Configure a chave da API**

No PowerShell, copie o arquivo de exemplo para criar o `.env`. Se você já possui um `.env` configurado, pule a cópia:

```powershell
Copy-Item .env.example .env
```

Abra o `.env` no editor e substitua `sua_chave_aqui` pela sua chave da OpenAI:

```env
OPENAI_API_KEY=sua_chave_aqui
```

O `.env` contém sua chave pessoal e está ignorado pelo Git. O `.env.example` serve como modelo de configuração.

**5. Execute a aplicação**

```bash
python -m streamlit run app.py
```

Acesse `http://localhost:8501` no navegador.

### Versão pelo terminal

Após instalar as dependências e configurar o `.env`, você também pode executar a versão pelo terminal:

```bash
python main.py
```

Digite o texto e o idioma de destino quando solicitado. A tradução será exibida no próprio terminal.

## Observações

Para realizar traduções, é necessário possuir uma chave da API da OpenAI com créditos disponíveis. O consumo da API pode gerar custos.

## Autor

Thiago

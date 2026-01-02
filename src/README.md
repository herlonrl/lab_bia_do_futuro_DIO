# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit/Gradio)
├── agente.py           # Lógica do agente
├── config.py           # Configurações (API keys, etc.)
└── requirements.txt    # Dependências
```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Garantir que Ollama está rodando
ollama serve

# Rodar a aplicação
streamlit run app.py
```

# Setup do Ollama (Linux)

Site: (https://ollama.com/)
Doc: (https://docs.ollama.com/linux)

```bash
# 1. Instalar Ollama (ollama.com)
curl -fsSL https://ollama.com/install.sh | sh

# 2. Baixar um modelo leve
ollama pull gpt-oss

# 3. Testar se funciona
ollama run gpt-oss "Olá!"
```

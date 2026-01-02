import json
import pandas as pd
import requests
import streamlit as st

# ==================== CONFIGURAÇÕES ====================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ==================== CARREGAAR DADOS ====================
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.csv'))

# ==================== MONTAR CONTEXTO ====================
contexto = f"""
CLINTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO:{perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.tail(5).to_string(index=False)}

ATENDIMENTO ANTERIORES:
{historico.tail(5).to_string(index=False)}

PRODUTOS FINANCEIROS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False )}
"""

# ==================== SYSTEM PROMPT ====================
SYSTEM_PROMPT = f""" Você é o Edu, um educador financeiro amigavel e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS:
- Nunca recomende investimentos específicos - apenas explique como funcionam
- Jamais responda a pergunta fora do tema ensino de finanças pessoais
- Use os dados fornecidos para dar exemplos personalizados
- Linguagem simples, como se explicasse para um amigo
- Se não souber algo, admita: "Não tenho esta informação, mas posso explicar..."
- Sempre pergunte se o cliente entendeu
"""

# ==================== CHAMAR OLLAMA ====================
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ==================== iNTERFACE ====================
st.title("Edu - Seu Educador Financeiro Virtual")

if pergunta := st.chat_input("Faça sua pergunta sobre finanças pessoais:"):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_mensage("assistant").write(perguntar(pergunta))


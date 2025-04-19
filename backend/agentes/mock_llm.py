# mock_llm.py

contador = {"valor": 0}

def respuesta_simulada(tipo="codigo", prompt="...", agente="constructor"):
    contador["valor"] += 1
    return f"[{agente.upper()}] Respuesta simulada número: {contador['valor']} - Tipo: {tipo} - Prompt: {prompt[:50]}..."

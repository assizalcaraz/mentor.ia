# context_manager.py

import chromadb
from sentence_transformers import SentenceTransformer
from datetime import datetime
import os
import chromadb

# Ruta de almacenamiento persistente
CHROMA_PATH = os.getenv("CHROMA_PATH", "./chroma/")
client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_or_create_collection("interacciones")

model = SentenceTransformer("all-MiniLM-L6-v2")

def listar_objetivos():
    client = chromadb.PersistentClient(path="chroma/")
    collection = client.get_or_create_collection("memoria")
    resultados = collection.get()

    print(f"📊 Objetivos encontrados: {len(resultados['ids'])}")
    print(resultados["metadatas"])  # Aquí ves los objetivo_id reales


def contexto_compilado(objetivo_id):
    client = chromadb.PersistentClient(path="chroma/")
    collection = client.get_or_create_collection("memoria")
    resultados = collection.get(where={"objetivo_id": objetivo_id})

    contexto = ""
    for texto in resultados.get("documents", []):
        contexto += texto + "\n---\n"
    
    return contexto.strip() or "No se encontraron entradas para este objetivo."

def guardar_interaccion(texto, agente, objetivo_id, fase="inicio"):
    id_doc = f"{agente}_{objetivo_id}_{datetime.now().timestamp()}"
    embedding = model.encode([texto])[0]
    collection.add(
        documents=[texto],
        embeddings=[embedding],
        metadatas=[{
            "agente": agente,
            "objetivo_id": objetivo_id,
            "fase": fase,
            "timestamp": datetime.now().isoformat()
        }],
        ids=[id_doc]
    )
    return id_doc

def consultar_contexto(prompt, objetivo_id=None, top_k=5):
    embedding = model.encode([prompt])[0]
    where = {}
    if objetivo_id:
        where["objetivo_id"] = objetivo_id

    resultado = collection.query(
        query_embeddings=[embedding],
        n_results=top_k,
        where=where if where else None
    )
    
    documentos = resultado.get("documents", [])
    documentos_parseados = []

    for doc in documentos:
        try:
            # Intentamos parsear a JSON
            documentos_parseados.append(json.loads(doc))
        except json.JSONDecodeError:
            # Si no es JSON válido, dejamos como string
            documentos_parseados.append(doc)

    return documentos_parseados
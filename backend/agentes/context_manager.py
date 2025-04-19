# context_manager.py

import chromadb
from sentence_transformers import SentenceTransformer
from datetime import datetime
import os

# Ruta de almacenamiento persistente
CHROMA_PATH = os.getenv("CHROMA_PATH", "./chroma/")
client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_or_create_collection("interacciones")

model = SentenceTransformer("all-MiniLM-L6-v2")

def contexto_compilado(objetivo_id):
    resultado = collection.get(where={"objetivo_id": objetivo_id})
    textos = resultado.get("documents", [])
    return "\n\n".join(textos)


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
    return resultado.get("documents", [])

# agentes/chroma_manager.py

import os
import json
import chromadb
from chromadb.config import Settings

# Inicializar cliente persistente de Chroma
chroma_client = chromadb.PersistentClient(
    path=os.getenv("CHROMA_DB_DIR", "./chroma_db")
)

# Colecciones
CHECKIN_COLLECTION = "checkins"
TAREA_COLLECTION = "tareas"

collection_checkins = chroma_client.get_or_create_collection(CHECKIN_COLLECTION)
collection_tareas = chroma_client.get_or_create_collection(TAREA_COLLECTION)

# ----- Funciones Generales -----

def guardar_checkin(objetivo_id: str, contenido_checkin: dict):
    collection_checkins.upsert(
        documents=[json.dumps(contenido_checkin, ensure_ascii=False)],
        ids=[f"checkin-{objetivo_id}"]
    )
    # NO persist() necesario

def guardar_tarea(objetivo_id: str, tarea_data: dict, tarea_id: str):
    collection_tareas.upsert(
        documents=[json.dumps(tarea_data, ensure_ascii=False)],
        ids=[f"tarea-{tarea_id}"],
        metadatas={"objetivo_id": objetivo_id}
    )
    # NO persist() necesario

def buscar_checkin(objetivo_id: str):
    results = collection_checkins.get(ids=[f"checkin-{objetivo_id}"])
    if results and results.get("documents"):
        return json.loads(results["documents"][0])
    return None

def buscar_tareas_por_objetivo(objetivo_id: str):
    results = collection_tareas.get(where={"objetivo_id": objetivo_id})
    tareas = []
    for doc in results.get("documents", []):
        tareas.append(json.loads(doc))
    return tareas

def eliminar_objetivo_vectores(objetivo_id: str):
    collection_checkins.delete(where={"objetivo_id": objetivo_id})

def eliminar_checkin(objetivo_id: str):
    collection_checkins.delete(ids=[f"checkin-{objetivo_id}"])

def eliminar_tareas_por_objetivo(objetivo_id: str):
    resultados = collection_tareas.get(where={"objetivo_id": objetivo_id})
    ids_a_eliminar = resultados.get("ids", [])
    if ids_a_eliminar:
        collection_tareas.delete(ids=ids_a_eliminar)

# ----- Fin del archivo -----

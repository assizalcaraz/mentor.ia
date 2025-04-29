# preload_models.py
from chromadb.utils.embedding_functions import ONNXMiniLM_L6_V2

def preload_onnx_model():
    embedder = ONNXMiniLM_L6_V2()
    embedder._download_model_if_not_exists()
    print("✅ Modelo descargado y verificado correctamente.")

if __name__ == "__main__":
    preload_onnx_model()

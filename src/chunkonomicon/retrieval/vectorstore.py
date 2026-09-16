class VectorStore:
    def add(self, chunks, embeddings):
        raise NotImplementedError

    def search(self, query_embedding, k: int = 5):
        raise NotImplementedError

from chunkonomicon.config import settings


def build_index():
    raise NotImplementedError


def answer(query: str) -> str:
    raise NotImplementedError


if __name__ == "__main__":
    build_index()

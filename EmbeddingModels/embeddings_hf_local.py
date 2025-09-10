from langchain_huggingface import HuggingFaceEmbeddings

embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = ["Hello world", "Mitesh Chokshi",
             "This is a test document", "Another document",
            "Yet another document", "This is a sample document"
]
vectors = embeddings.embed_documents(documents)
print(str(vectors))
from langchain.text_splitters import RecursiveCharacterTextSplitter

text = "This is a long text. " * 200
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
chunks = splitter.split_text(text)
print(f"Total chunks: {len(chunks)}")
print(chunks[0])

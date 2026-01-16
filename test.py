import os
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_huggingface.llms import HuggingFaceEndpoint

# 1️⃣ Set your HuggingFace token as environment variable
# You can set it in terminal or uncomment below:
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if HF_TOKEN is None:
    raise ValueError("Set the HuggingFace token in HUGGINGFACEHUB_API_TOKEN env variable")

# 2️⃣ Test Instructor-XL embeddings
print("Testing Instructor-XL embeddings...")

try:
    embeddings_model = HuggingFaceEmbeddings(
        model_name="hkunlp/instructor-xl",
        model_kwargs={"device": "cpu"}  # or "cuda" if you have GPU
    )

    text = "Hello! This is a test for embeddings."
    embedding_vector = embeddings_model.embed_query(text)
    print("Embedding vector length:", len(embedding_vector))
    print("Embedding test passed ✅\n")

except Exception as e:
    print("Embedding test failed ❌")
    print(e)

# 3️⃣ Test HuggingFaceEndpoint LLM
print("Testing HuggingFaceEndpoint (LLM)...")

MODEL_ID = "hkunlp/instructor-xl"

try:
    llm = HuggingFaceEndpoint(
        repo_id=MODEL_ID,
        task="text-generation",  # Instructor-XL supports short text generation
        temperature=0.3,
        max_new_tokens=50
        # NO huggingfacehub_api_token here
    )

    response = llm.invoke("Hello HuggingFace! Can you respond briefly?")
    print("LLM response:")
    print(response)

except Exception as e:
    print("LLM test failed ❌")
    print(e)

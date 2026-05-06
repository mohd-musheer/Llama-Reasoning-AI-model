from llama_cpp import Llama

llm = Llama(
    model_path="./model/llama3-q4_k_m.gguf",
    n_ctx=2048,
    verbose=False
)

print("✅ Model loaded successfully!")

while True:

    prompt = input("\nEnter Prompt: ")

    if prompt.lower() == "exit":
        break

    output = llm(
        prompt,
        max_tokens=1024,
        temperature=0.7,
        top_p=0.9
    )

    response = output["choices"][0]["text"]

    print("\n🧠 Response:\n")
    print(response)
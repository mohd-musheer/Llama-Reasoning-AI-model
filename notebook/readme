# 🧠 Musheer LLaMA Fine-Tuned Model (LoRA Adapter)

## 📌 Overview

This repository contains a **fine-tuned LoRA adapter** built on top of a LLaMA-based model using efficient parameter-efficient fine-tuning (PEFT).
The model is trained to improve structured reasoning and solution generation from problem-based inputs.

> ⚠️ This repository contains **LoRA adapter weights only**, not the full base model.

---

## 🧩 Base Model

* **Base Model:** `meta-llama/Meta-Llama-3-3B` *(or your exact base model name — update if needed)*
* Architecture: LLaMA (Causal Language Model)
* Parameters: ~3 Billion
* Precision: `float16`
* Quantization: 4-bit (bitsandbytes - NF4)

---

## ⚙️ Model Architecture

| Component          | Value  |
| ------------------ | ------ |
| Hidden Size        | 3072   |
| Layers             | 28     |
| Attention Heads    | 24     |
| KV Heads           | 8      |
| Intermediate Size  | 8192   |
| Activation         | SiLU   |
| Max Context Length | 131072 |
| Vocabulary Size    | 128256 |

---

## ⚡ Quantization Details

* Method: **bitsandbytes (4-bit NF4)**
* Compute dtype: `float16`
* Double Quantization: Enabled

This allows the model to run efficiently on low-memory systems.

---

## 🧠 Training Details

* Method: **LoRA (Low-Rank Adaptation)**
* Framework: Unsloth + Hugging Face Transformers
* Objective: Improve reasoning, structured outputs, and problem-solving capability
* Dataset: Custom dataset with:

  * Problem
  * Reasoning (thought process)
  * Final solution

---

## 📦 What’s Included

* ✅ LoRA adapter weights (~110 MB)
* ❌ Full base model weights (NOT included)

---

## 🚀 How to Use

### Step 1 — Install dependencies

```bash
pip install transformers peft bitsandbytes
```

---

### Step 2 — Load model

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

base_model_name = "meta-llama/Meta-Llama-3-3B"

base_model = AutoModelForCausalLM.from_pretrained(
    base_model_name,
    load_in_4bit=True,
    device_map="auto"
)

tokenizer = AutoTokenizer.from_pretrained(base_model_name)

model = PeftModel.from_pretrained(base_model, "musheer/your-model-name")
```

---

### Step 3 — Inference

```python
input_text = "Solve: What is 2+2?"

inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=200
)

print(tokenizer.decode(outputs[0]))
```

---

## 🔄 Optional: Merge Model

To create a standalone full model:

```python
model = model.merge_and_unload()
model.save_pretrained("merged_model")
```

> ⚠️ This will increase size to ~7+ GB

---

## 💻 System Requirements

### Minimum:

* 8 GB RAM (with 4-bit quantization)
* CPU inference supported

### Recommended:

* 16 GB RAM or GPU with ≥6 GB VRAM

---

## ⚠️ Limitations

* Requires base model to run
* Performance depends heavily on dataset quality
* Not optimized for long-context reasoning beyond training distribution

---

## 📊 Notes

* This is a **parameter-efficient fine-tuned model**, not a full retrained LLM
* Adapter modifies only a small subset of weights (~1–2%)

---

## 📌 Future Improvements

* Better dataset curation and filtering
* Evaluation benchmarks (BLEU, ROUGE, etc.)
* Deployment optimization (GGUF / inference acceleration)

---

## 🤝 Acknowledgements

* Hugging Face Transformers
* Unsloth
* Meta AI (LLaMA)

---

## 📬 Contact

**Mohd. Musheer**

* Email: [musheerayan@gmail.com](mailto:musheerayan@gmail.com)
* GitHub: https://github.com/mohd-musheer
* LinkedIn: https://linkedin.com/in/mohdmusheer

---

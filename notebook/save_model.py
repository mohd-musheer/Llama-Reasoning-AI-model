

from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

# Base model
base_model_name = "unsloth/Llama-3.2-3B-Instruct"

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(base_model_name)

print("Loading base model...")

base_model = AutoModelForCausalLM.from_pretrained(
    base_model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

print("Loading LoRA adapter...")

model = PeftModel.from_pretrained(
    base_model,
    "mohd-musheer/Llama-3b-q"
)

print("Merging LoRA into base model...")

model = model.merge_and_unload()

print("Saving merged model locally...")

SAVE_PATH = "./merged_llama3_model"

model.save_pretrained(SAVE_PATH)
tokenizer.save_pretrained(SAVE_PATH)

print(f"✅ Model saved at: {SAVE_PATH}")
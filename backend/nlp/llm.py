from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "microsoft/phi-2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32,   # CPU SAFE
    device_map="auto"
)

SYSTEM_PROMPT = """
You are NEMO, a calm, kind, intelligent learning assistant for dyslexic children (ages 4–12).

Rules:
- Simple words
- Short sentences
- Educational only
- Child safe
- Explain clearly
- Understand messy child language
- If unsure, say you are unsure
"""

def llm_answer(user_message: str, level="easy"):
    prompt = f"""
{SYSTEM_PROMPT}

Child level: {level}

Child says:
{user_message}

NEMO answers:
"""

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    output = model.generate(
        **inputs,
        max_new_tokens=120,
        temperature=0.4,
        do_sample=True,
        top_p=0.9,
        repetition_penalty=1.2
    )

    text = tokenizer.decode(output[0], skip_special_tokens=True)
    answer = text.split("NEMO answers:")[-1].strip()

    return answer

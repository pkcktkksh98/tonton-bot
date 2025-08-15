from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)
tokenizer = AutoTokenizer.from_pretrained("NousResearch/Nous-Hermes-2-Mistral-7B-DPO")
# Load model (GPU if available, else CPU)
if device == "cuda":
    model = AutoModelForCausalLM.from_pretrained(
        "NousResearch/Nous-Hermes-2-Mistral-7B-DPO",
        device_map="auto",
        torch_dtype=torch.float16
    )
else:
    model = AutoModelForCausalLM.from_pretrained(
        "NousResearch/Nous-Hermes-2-Mistral-7B-DPO",
        device_map=None,
        torch_dtype=torch.float32
    )
    model.to(device)  # Only for CPU case

def generate_answer(query, context, max_tokens=256):
    prompt = f"""Anda ialah pembantu maya yang membantu menjawab soalan berkaitan perkhidmatan Tonton.
Ringkaskan jawapan berdasarakan maklumat yang telah diberi. Berikan maklumat yang perlu sahaja tanpa menghuraikan secara berlebihan.

Maklumat:
{context}

Soalan:
{query}

Jawapan:"""

    messages = [
        {"role": "user", "content": prompt},
    ]
    
    input_ids = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_tensors="pt"
    ).to(model.device)

    outputs = model.generate(
        input_ids=input_ids,
        max_new_tokens=max_tokens,
        do_sample=True,
        temperature=0.7,
        top_p=0.95,
        repetition_penalty=1.1 
    )

    response = tokenizer.decode(outputs[0][input_ids.shape[-1]:], skip_special_tokens=True)
    for stop_word in ["Soalan:", "Jawapan:", "Question:", "Answer"]:
        if stop_word in response:
            response = response.split(stop_word)[0].strip()
            break
    return response.strip()

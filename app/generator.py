from llama_cpp import Llama
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load GGUF model (make sure it's in the same directory or specify full path)
# llm = Llama(
#     model_path="model.gguf",  # Use your downloaded model path
#     n_ctx=2048,
#     n_threads=8,          # Adjust based on your CPU
#     n_gpu_layers=20,      # Optional: if running with GPU (for Metal/CUDA/OpenBLAS)
#     verbose=False
# )

tokenizer = AutoTokenizer.from_pretrained("NousResearch/Nous-Hermes-2-Mistral-7B-DPO")
model = AutoModelForCausalLM.from_pretrained("NousResearch/Nous-Hermes-2-Mistral-7B-DPO")
device="cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

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
    
    # response = llm(
    #     prompt=prompt,
    #     max_tokens=max_tokens,
    #     temperature=0.7,
    #     top_p=0.95,
    #     repeat_penalty=1.1,
    #     stop=["Soalan:", "Jawapan:", "Question:","Answer"]
    # )

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
        temperature=0.7
    )

    response = tokenizer.decode(outputs[0][input_ids.shape[-1]:], skip_special_tokens=True)
    return response.strip()

from transformers import BertTokenizer, BertModel
import torch

def question_answer(question, reference):
    model = BertModel.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
    tokenizer = BertTokenizer.from_pretrained("bert-large-uncased-whole-word-masking")

    inputs = tokenizer(question, reference, return_tensors="pt",
                       max_length=512, truncation=True)
    
    with torch.no_grad():
        outputs = model(**inputs)

    start_scores = outputs.start_logits
    end_scores = outputs.end_logits

    start_idx = torch.argmax(start_scores)
    end_idx = torch.argmax(end_scores) + 1

    if start_idx < len(reference):
        answer = reference[start_idx:end_idx]
    else:
        return None
    
    return answer.strip()
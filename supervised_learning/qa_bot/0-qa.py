import torch
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer
import warnings

warnings.simplefilter("ignore")

"""Tutorial taken from this site:
https://www.kaggle.com/code/arunmohan003/question-answering-using-bert"""

def question_answer(question, reference):
    token_path = "bert-large-uncased-whole-word-masking-finetuned-squad"

    tokenizer = BertTokenizer.from_pretrained(token_path)

    model = BertForQuestionAnswering.from_pretrained(token_path)

    # print("You made it. Congrats.")
    # I'm not sure where to go from here
    # Like. How do I bring in the data?

    input_ids = tokenizer.encode(question, reference)
    # print(f'there are roughly {len(input_ids)} tokens generated')

    tokens = tokenizer.convert_ids_to_tokens(input_ids)
    
    # print("examples:")
    # for i, (token, inp_id) in enumerate(zip(tokens, input_ids)):
    #     print(token, ":", inp_id)
    # That's a lot of pairings.
    # At least we're getting output

    # So these are segmentation embeddings I guess
    sep_idx = tokens.index('[SEP]')

    token_type_ids = [0 for i in range(sep_idx+1)] + [1 for i in range(sep_idx+1, len(tokens))]
    # print(token_type_ids)

    out = model(torch.tensor([input_ids]),
                token_type_ids=torch.tensor([token_type_ids]))
    
    start_logits, end_logits = out['start_logits'], out['end_logits']

    answer_start = torch.argmax(start_logits)
    answer_end = torch.argmax(end_logits)

    # print("You made it here. Good job.")

    # print('This should print:')
    # print(''.join(tokens[answer_start:answer_end]))

    return ' '.join(tokens[answer_start:answer_end])
from transformers import pipeline
from question_formater import question_formater
def model(img_path , question):
    answers = []
    model_checkpoints = {
        "LayoutLMv1 🦉": "impira/layoutlm-document-qa",
        "LayoutLMv1 for Invoices": "impira/layoutlm-invoices",
        "Donut 🍩": "naver-clova-ix/donut-base-finetuned-docvqa",
    }
    pipe = pipeline("document-question-answering" , model = model_checkpoints["LayoutLMv1 for Invoices"])
    question_list , no_of_questions = question_formater(question)
    print(question_list)
   
    for question in question_list:
        answers.append(pipe(image=img_path, question = question))
    
    answers = [x if x[0]['score'] >= 0.5 else None for x in answers]

    
    
    
    

    return answers , no_of_questions


def button_model(img_path , question):
    model_checkpoints = {
        "LayoutLMv1 🦉": "impira/layoutlm-document-qa",
        "LayoutLMv1 for Invoices": "impira/layoutlm-invoices",
        "Donut 🍩": "naver-clova-ix/donut-base-finetuned-docvqa",
    }
    pipe = pipeline("document-question-answering" , model = model_checkpoints["LayoutLMv1 for Invoices"])
    answer=  pipe(image=img_path, question = question)
    print(answer[0]['score'])
    if answer[0]['score'] <= 0.5:
        return None
    else : 
        return answer
    
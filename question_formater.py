def question_formater(question):
    
    question_list = question.split('?')
    
    return [x for x in question_list if x != ' '] , len([x for x in question_list if x != (' ' and '')] )
    
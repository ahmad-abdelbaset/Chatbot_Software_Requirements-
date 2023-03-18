import re
#import long_responses as long
stored_answers ={}
decidedField = False

#This function will decide which response to provide
def get_response(user_input):
    global decidedField
    if bool(stored_answers) and decidedField:
        with open("RS.txt", 'w+') as f:
            for value in stored_answers.values():
                f.write(str(value)) #to Document the answer (The field of the application)
        return "Documented"
    split_message = re.split(r'\s+|[,;?!-]]\s*', user_input.lower())
    response = check_all_messages(split_message)

    if 'Medical' in response:
        stored_answers['Field'] = 'This is an application in medical field'
        decidedField = True
    elif 'Gaming' in response:
        stored_answers['Field'] = 'This is an application in Gaming field'
        decidedField = True
    elif 'Business' in response:
        stored_answers['Field'] = 'This is an application in Business field'
        decidedField = True
    elif 'Educational' in response:
        stored_answers['Field'] = 'This is an application in Educational field'
        decidedField = True
    elif 'E-commerce' in response:
        stored_answers['Field'] = 'This is an application in E-commerce field'
        decidedField = True
    elif 'Travel' in response:
        stored_answers['Field'] = 'This is an application in Travel field'
        decidedField = True
    elif 'E-commerce' in response:
        stored_answers['Logistic'] = 'This is an application in Logistic field'
        decidedField = True


    return response

def message_probability(user_message, recognized_words, single_response= False, required_words=[]):
    message_certainity = 0
    has_required_words = True

    #Calculate how many words are present in each predefined message
    for word in user_message:
        if word in recognized_words:
            message_certainity += 1

    #Calculates the percent of recognized words in a user message
    percentage = float(message_certainity)/float(len(recognized_words))

    #Checks that the required words are in the string
    for word in required_words:
        if word not in required_words:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False,required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words,single_response,required_words)

    #Responses
    response('Hello!, can you tell me about your product?',['hello','hi','sup','heyo'], single_response=True)
    response('I\'m fine, what about you?', ['how', 'are', 'you', 'doing'], required_words=['how','you'])
    response('It is a Medical product, right?',['hospital','clinic','medicine','patient','patients','doctors','dentist','dentists'], single_response=True)
    response('It is a Gaming product, right?',['players','player','game','gaming','score','playing'], single_response=True)
    response('It is a Business product, right?',['selling','sale','sales','buying','buyer','goods','paying','pays','money','company','shope','companies'], required_words=['company','companies','shope'])
    response('It is a Educational product, right?',['student','students','school','marks','grades','courses','university','courses','training','teacher','teachers'], single_response=True)
    response('It is a E-commerce product, right?',['product','payment','payments','products','selling','buying','website','app','online'], required_words=['online','website'])
    response('It is a Travel product, right?',['travel','traveling','city','cities','countries','tickets','ticket'], single_response=True)
    response('It is a Logistic product, right?',['moving','move','send','recieve','calling','calls','mission','book'], single_response=True)
    response('Documented',['yes'], single_response=True)


    best_match = max (highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknow() if highest_prob_list[best_match] ==0 else best_match


while True:
    print ('ChatBot: '+ get_response(input ("User(you): ")))
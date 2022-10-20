from survey import AnonSurvey

#define a question, and make a survey
question = "What language do you speak?"
my_survey = AnonSurvey(question)

#show question and store response to the question
my_survey.show_question()
print("Enter 'q' at anytime to quit")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
#show survey result
print("\n Thank you for participating!")
my_survey.show_results()
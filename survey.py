
class AnonSurvey:
    """Collect anonymous answers to a survey"""
    def __init__(self, question) -> None:
        """store a question and prepare to store a response"""
        self.question: str = question
        self.response: list[str] = [] 

    def show_question(self):
        """show a question"""
        print(self.question)

    def store_response(self, new_response: str) -> str:
        """Store a single response to the survey"""
        self.response.append(new_response)
        return new_response

    def show_results(self):
        """Show all response that have been given"""
        print("Survey results: ")
        for response in self.response:
            print(f"- {response}")
 
    
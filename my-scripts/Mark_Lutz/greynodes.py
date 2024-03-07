
'''
Function analyze_response: This function takes the user input, analyzes it based on scenario answer's the user.
Input: Take user's inputs from prompt
Output: Analyzes input and shows ouput based on scenario.
'''
def analyze_response(response):
    while not response.isspace() and len(response) > 0:
        new_response=input("Have you had this problem before (yes or no)?")
        new_response = new_response.lower().strip(' ')
        if new_response == 'yes':
            print("Well, you have it again.")
            break
        elif new_response == 'no':
            print("Well, you have it now")
            break
        else:
            print("Please answer my question: Have you had this problem before (yes or no)?")
    else:
        response=input("Please answer my question: What is your problem? ")
        analyze_response(response)


response=input("What is your problem? ")
analyze_response(response)

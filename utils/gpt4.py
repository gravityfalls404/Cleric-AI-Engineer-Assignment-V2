import openai

openai.api_key = 'sk-proj-O8tBCwyJ2ayGPcbguaO8T3BlbkFJjYUrvju7Ghfbzc4G0OBF'

def get_openai_response(question, documents):
    # Create a prompt by combining the question and the list of documents
    prompt = f"I'm going to give you a list of call logs and along with that a question related to what the team has decided based on the logs. Give response in bullet points. Q: {question}\nDocuments:\n" + '\n'.join(documents)

    # Call the OpenAI API to generate a completion based on the prompt
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Choose the OpenAI engine (e.g., davinci or curie)
        prompt=prompt,
        max_tokens=150,  # Adjust the maximum number of tokens in the response
        n=1,  # Number of responses to generate
        stop=None,  # Specify any stop sequence if needed
    )

    # Extract and return the generated text from the API response
    if response and len(response['choices']) > 0:
        return response['choices'][0]['text']
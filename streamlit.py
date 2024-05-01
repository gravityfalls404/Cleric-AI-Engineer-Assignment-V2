import streamlit as st
import requests

SUBMIT_REQUEST_API = 'http://0.0.0.0:5000/submit_question_and_documents'
RESPONSE_API = 'http://0.0.0.0:5000/get_question_and_facts'
def hit_api(question, urls):
    data = {
        "question": question,
        "documents": urls
    }
    response = requests.post(SUBMIT_REQUEST_API, json=data)
    if response.status_code == 200:
        return True
    else:
        return None

def main():
    st.title('Information Extraction From Call Transcripts')
    urls = []
    question = st.text_input('Enter a question')
    no_of_transcripts = st.number_input('Enter the number of transcripts', 1)
    
    for i in range(no_of_transcripts):
        urls.append(st.text_input(f'Enter the url of transcript {i+1}'))

    if st.button('Submit'):
        ## Remove empty strings urls from urls list. 
        urls = [url for url in urls if url!= '']

        # Call the API with the question and URLs
        response = hit_api(question, urls)

        if response is not None:
            st.write("Job Submitted!")
        else:
            st.write('An error occurred while submitting the question and transcripts.')

    if st.button('Poll for response'):
        response = requests.get(RESPONSE_API)
        if response.status_code == 200:
            response = response.json()
            if not response['question']:
                st.write("Please Submit the question and transcripts first.")
            elif response['status'] == 'processing':
                st.write('Processing...')
            elif response['status'] == 'done':
                output = ''
                for _fact in response['facts']:
                    output += "- " + _fact + "\n"
                st.markdown(output)
            else:
                st.write('An error occurred while fetching the response.')
        else:
            st.write('An error occurred while fetching the response.')


if __name__ == '__main__':
    main()

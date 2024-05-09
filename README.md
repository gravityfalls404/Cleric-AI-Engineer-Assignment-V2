# Call Log Processor

This web application processes and extracts information from a set of call logs using an LLM (Language Model). It allows users to input a single question along with a list of call logs and extracts relevant facts from these logs.

## How to Use

1. **Input Question**: Provide a single question related to the call logs.
2. **Submit Call Logs**: provide a URL(s) where the logs are accessible.
3. **Submit Request**: Click on the "Process Logs" button to extract facts based on the provided question and call logs.
4. **View Results**: The application will present a final list of facts extracted from the call logs relevant to the question.

## Example

Consider the following call log as an example:

**URL**: `https://example.com/call_log_1.txt`

```
00:00:10 - Alex: Let's choose our app's color scheme today.
00:00:36 - Jordan: I suggest blue for a calm feel.
00:00:51 - Casey: We need to make sure it's accessible to all users.
```

If the question being asked was “What product design decisions did the team make?”, the application would extract facts such as:

- The team will use blue for the color scheme of the app.
- The team will make the app accessible to all users.

## Technologies Used

- Python Flask: Backend framework for handling requests and processing logs.
- Celery: Used for handling asynchronous job scheduling and processing.
- GPT-4: Used for text analysis and extraction of relevant information from logs.
- Streamlit: Frontend interface for user interaction.

## Installation

1. Clone the repository.
2. Install the relevent packages using the following command:
    `pip install -r requirements.txt`
3. Set enviroment variable for gpt-4 apikey using the following command:
    `export $OPENAI_API_KEY=<YOUR_API_KEY>`
4. Start the services using the following commands on different terminals:
```
$ celery -A task worker --loglevel=info
$ flask run
$ streamlit run streamlit.py
```

4. Navigate to the http://localhost:8501 to access the streamlit UI.

## Contributors
- Prashant Gaurav
import threading
import queue
import time

# Input and output queues for messages
input_queue = queue.Queue()
output_queue = queue.Queue()

# Function to process messages from the input queue
def process_messages():
    while True:
        try:
            # Get a message from the input queue (blocking call)
            message = input_queue.get(timeout=1)  # Timeout to avoid blocking indefinitely
            # Process the message (for demonstration, just add a prefix)
            processed_message = f"Processed: {message}"
            # Put the processed message into the output queue
            output_queue.put(processed_message)
            # Mark the task as done in the input queue
            input_queue.task_done()
        except queue.Empty:
            # If the input queue is empty, wait for a short time before checking again
            time.sleep(0.1)

# Start the thread to process messages
processing_thread = threading.Thread(target=process_messages)
processing_thread.daemon = True  # Daemonize the thread to exit when the main thread exits
processing_thread.start()

# Example: Add messages to the input queue (simulate incoming messages)
input_queue.put("Message 1")
input_queue.put("Message 2")
input_queue.put("Message 3")

# Wait for the processing to finish (join the processing thread)
input_queue.join()

# Retrieve processed messages from the output queue
while not output_queue.empty():
    processed_message = output_queue.get()
    print(processed_message)
    output_queue.task_done()

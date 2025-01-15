# import ollama
#
# # Send a message to the model
# response = ollama.chat(
#     model='qwen2:0.5b',  # Replace with your desired model
#     messages=[
#         {
#             'role': 'user',
#             'content': 'Why is the sky blue?',
#         },
#     ]
# )
#
# # Print the model's response
# print(response['message']['content'])


# import ollama
#
# stream = ollama.chat(
#     model='qwen2:0.5b',
#     messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
#     stream=True,
# )
#
# for chunk in stream:
#     print(chunk['message']['content'], end='', flush=True)


# import speech_recognition as sr
#
# def transcribe_audio():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)
#     try:
#         text = recognizer.recognize_google(audio)
#         print("You said:", text)
#         return text
#     except sr.UnknownValueError:
#         print("Sorry, I did not understand.")
#         return None
#     except sr.RequestError:
#         print("Could not request results.")
#         return None
#
#
# import ollama
#
# def get_llm_response(prompt):
#     response = ollama.chat(
#         model='llama3.1',
#         messages=[
#             {'role': 'user', 'content': prompt}
#         ]
#     )
#     return response['message']['content']
#
#
# def voice_command_to_llm():
#     while True:
#         # Transcribe voice to text
#         command = transcribe_audio()
#
#         if command:
#             # Process command with the LLM
#             response = get_llm_response(command)
#             print("LLM Response:", response)
#
#         # Option to break the loop (optional)
#         if command and command.lower() in ["exit", "stop"]:
#             print("Exiting...")
#             break
#
# voice_command_to_llm()
import openai

def meeting_summary(audio_file_path, api_key):
    
    openai.api_key = api_key

    
    with open(audio_file_path, "rb") as audio_file:
        response = openai.Audio.transcribe(model="whisper-1", file=audio_file, response_format="text")

        
        if isinstance(response, dict):
            transcript = response.get("text", "")
        else:
            transcript = response 

   
    summary_response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",  
        prompt=f"Provide a summary of the following content :\n\n{transcript}",
        max_tokens=1000
    )
    summary = summary_response.choices[0].text.strip()

    return summary


audio_file_path = 'file_path'  
api_key = 'API key'  
summary = meeting_summary(audio_file_path, api_key)
print("Summary:\n", summary)

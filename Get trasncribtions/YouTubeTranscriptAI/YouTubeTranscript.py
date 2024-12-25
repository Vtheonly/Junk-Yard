from youtube_transcript_api import YouTubeTranscriptApi
from groq import Groq
url="https://www.youtube.com/watch?v=i9x0UO8MY0g"
























video_id = url[32:]
context = ""
client = Groq(api_key="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",)


def extract_text_from_subtitles(subtitles):
  full_text = ""
  for segment in subtitles:
    full_text += segment['text'] + " "
  return full_text.strip() 


try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    context=extract_text_from_subtitles(transcript)
except Exception as e:
    print(f"Error: {e}")




chat_completion = client.chat.completions.create(
    messages=[
        {
                "role": "user",
                "content": f"""
                
You are a helpful assistant tasked with explaining educational content. 
Based on the information presented in this portion of an educational video, provide an informative explanation of the key concepts and topics discussed.
Focus on explaining the main ideas as if you had watched the video yourself.

**Instructions for Formatting:**
- Use **Markdown** to format your response.
- Use **headers** (e.g., `# Header`, `## Subheader`) to organize the content.
- Use **bold** text for important terms and concepts.
- Use **lists** (both ordered and unordered) to present steps, points, or examples.
- Use **tables** if needed to present data in a structured format.
- Use **italics** for emphasis or additional notes.

**Transcript:**
            : {context}""",
        }
    ],
    model="llama-3.2-90b-vision-preview",
)

print("\n"*4)
print(chat_completion.choices[0].message.content)


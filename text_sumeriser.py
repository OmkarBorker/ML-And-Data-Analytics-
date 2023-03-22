from transformers import pipeline

# Load the summarization model
summarizer = pipeline("summarization")

# Define the input text
text = """I am happy! There is a deep sense of contentment that fills my heart and soul, and it seems as though every moment is illuminated with a bright and joyful light. I feel at peace with myself and the world around me, and everything seems to be aligned in perfect harmony."""

# Generate the summary
summary = summarizer(text, max_length=50, min_length=10, do_sample=False)

# Print the summary
print(summary[0]['summary_text'])
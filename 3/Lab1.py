# Import the Python SDK
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-pro')

# Define the prompts
few_shot_prompt = "Here are some examples of magic stories: ...\nNow, write a new story about a magic backpack."
cot_prompt = "Describe the step-by-step process of how a magic backpack can transform objects placed inside it."
prompt_chain = [
    "Write the beginning of a story about a magic backpack.",
    "Continue the story by introducing a conflict involving the magic backpack.",
    "Resolve the conflict and conclude the story."
]
tree_of_thoughts_prompt = "Consider different ways a magic backpack could help someone in various situations, and explain each."

# Function to generate and print response
def generate_and_print(prompt, description):
    response = model.generate_content(prompt)
    print(f"Prompt: {prompt}\nResponse: {response.text}\n")
    return prompt, response.text

# Collect responses
responses = []
responses.append(generate_and_print(few_shot_prompt, "Few-shot Prompt"))
responses.append(generate_and_print(cot_prompt, "Chain-of-Thought Prompt"))

for i, prompt in enumerate(prompt_chain, 1):
    responses.append(generate_and_print(prompt, f"Prompt Chain Part {i}"))

responses.append(generate_and_print(tree_of_thoughts_prompt, "Tree of Thoughts Prompt"))

# Save responses to a file
filename = "gemini_responses.txt"
with open(filename, "w") as file:
    for desc, response in responses:
        file.write(f"Prompt: {desc}\nResponse: {response}\n\n")





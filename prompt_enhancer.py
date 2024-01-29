import openai

# Set your OpenAI API key 
#Note: this is not set due to security concerns
openai.api_key = 'API-Key'

def enhance_prompt(prompt):
    # Set the model and prompt for the OpenAI API request
    model = "gpt-3.5-turbo-instruct"  # You can use other models as well
    prompt_for_api = f"Enhance the following text:\n{prompt}"

    # Make the API request
    response = openai.Completion.create(
        engine=model,
        prompt=prompt_for_api,
        max_tokens=150  # You can adjust this parameter based on your needs
    )

    # Extract the generated text from the API response
    generated_text = response['choices'][0]['text']

    return generated_text

def main():
    # Get user input
    user_prompt = input("Enter the text you want to enhance: ")

    # Enhance the prompt using the OpenAI API
    enhanced_prompt = enhance_prompt(user_prompt)

    # Print the enhanced prompt
    print("\nEnhanced Text:")
    print(enhanced_prompt)

if __name__ == "__main__":
    main()







import google.generativeai as genai

# Set your API key
genai.configure(api_key="AIzaSyCiWbAjbHFXpEFXb5oiTdFUH4kZfgdDNao")

# List all available models
models = genai.list_models()

# Print model names and their supported methods
for model in models:
    print(f"Model ID: {model.name}")
    print(f"  Supported methods: {model.supported_generation_methods}")
    print("-" * 40)

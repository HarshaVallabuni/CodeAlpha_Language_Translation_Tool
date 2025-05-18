# Language Translation Tool using deep-translator
from deep_translator import GoogleTranslator

# Function to translate text
def translate_text(text, source_lang, target_lang):
    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"Translation failed: {e}"

# ----------------------------
# Inputs below the function
# ----------------------------
print("------ Language Translation Tool ------")

# Take dynamic inputs from the user
input_text = input("Enter the text to translate: ")
source_language = input("Enter source language code (e.g., en for English): ").strip()
target_language = input("Enter target language code (e.g., te for Telugu): ").strip()

# Call the function
translated_output = translate_text(input_text, source_language, target_language)

# Output
print(f"\nTranslated ({source_language} → {target_language}): {translated_output}")

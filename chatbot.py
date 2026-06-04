from learning_resource.response_database import PORTFOLIO_INFO, INTENT_KEYWORDS
from learning_resource.model_learning import appending_learning_entry, predict_intent_from_learned_entries
from text_normalization import lemmatize_word, lemmatize_words
import random


def generate_response(phrase):
    intents = get_intent(phrase)
    return get_response(phrase, intents)


def parse_phrase(phrase):
    parse_list = []
    for word in phrase.lower().split():
        cleaned_word = word.strip(".,!?;:").replace(".", "")
        if cleaned_word:
            parse_list.append(cleaned_word)
    return parse_list


def get_intent(phrase):
    word_list = parse_phrase(phrase)
    normalized_words = lemmatize_words(word_list)
    top_intent = top_level_intent(normalized_words)
    sub_intent = second_level_intent(top_intent, normalized_words)
    return [top_intent, sub_intent]


def top_level_intent(word_list):
    greeting_detected = False

    for word in word_list:
        for category_name, subcategories in INTENT_KEYWORDS.items():
            for keywords in subcategories.values():
                normalized_keywords = [lemmatize_word(k) for k in keywords]
                if word in normalized_keywords:
                    if category_name == "greeting":
                        greeting_detected = True
                        continue
                    return category_name

    if greeting_detected:
        return "greeting"

    return False


def second_level_intent(top_intent, word_list):
    if not top_intent or top_intent == "greeting":
        return top_intent

    for word in word_list:
        for subcategory_name, keywords in INTENT_KEYWORDS[top_intent].items():
            normalized_keywords = [lemmatize_word(keyword) for keyword in keywords]
            if word in normalized_keywords:
                return subcategory_name

    return next(iter(INTENT_KEYWORDS[top_intent]), False)


def build_guess_message(top_intent, sub_intent):
    messages = {
        "about": "I'm guessing you want to know about Carson.",
        "resume": "I'm guessing you want Carson's resume.",
        "skills": "I'm guessing you want to know about Carson's skills.",
        "projects": "I'm guessing you want to know about Carson's projects.",
        "contact": "I'm guessing you want Carson's contact information.",
        "education": "I'm guessing you want to know about Carson's education.",
        "greeting": "I'm guessing you're saying hello.",
    }
    return messages.get(top_intent, "I'm guessing based on what I've learned.")


def format_guessed_response(response, top_intent, sub_intent):
    guess_message = build_guess_message(top_intent, sub_intent)

    if isinstance(response, dict):
        return {**response, "text": f"{guess_message}\n{response.get('text', '')}"}

    if isinstance(response, str):
        return f"{guess_message}\n{response}"

    return response


def get_response(original_phrase, intents, guessed_from_learning=False):
    top_intent, sub_intent = intents

    if not top_intent:
        predicted_intents = predict_intent_from_learned_entries(original_phrase)
        if predicted_intents:
            return get_response(original_phrase, predicted_intents, guessed_from_learning=True)
        return "I'm not sure about that. Try asking about Carson's skills, projects, resume, or how to contact him."

    appending_learning_entry(original_phrase, top_intent, sub_intent)

    if top_intent == "greeting":
        response = random.choice(PORTFOLIO_INFO["greeting"]["responses"])
    elif top_intent == "resume":
        response = {"text": PORTFOLIO_INFO["resume"]["response"], "action": "download_resume"}
    elif top_intent in PORTFOLIO_INFO:
        response = PORTFOLIO_INFO[top_intent]["response"]
    else:
        return "I'm not sure about that. Try asking about Carson's skills, projects, resume, or how to contact him."

    return format_guessed_response(response, top_intent, sub_intent) if guessed_from_learning else response

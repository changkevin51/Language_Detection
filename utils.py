from lingua import LanguageDetectorBuilder, Language
import pyjokes
import streamlit as st  # Import Streamlit for caching

language_mapping = {
    Language.BASQUE: 'eu',
    Language.CZECH: 'cs',
    Language.GERMAN: 'de',
    Language.ENGLISH: 'en',
    Language.SPANISH: 'es',
    Language.FRENCH: 'fr',
    Language.HUNGARIAN: 'hu',
    Language.ITALIAN: 'it',
    Language.LITHUANIAN: 'lt',
    Language.POLISH: 'pl',
    Language.RUSSIAN: 'ru',
    Language.SWEDISH: 'sv',
}

@st.cache(allow_output_mutation=True)
def get_detector():
    return LanguageDetectorBuilder.from_all_languages().with_preloaded_language_models().build()

def detect_language(text):
    detector = get_detector()
    language = detector.detect_language_of(text)
    confidence_values = detector.compute_language_confidence_values(text)
    if language is not None:
        return language, confidence_values[:4]
    else:
        return None, None

def tell_joke(language):
    """
    Returns a joke in the specified language if available.
    """
    if language in language_mapping:
        joke_language = language_mapping[language]
        try:
            joke = pyjokes.get_joke(language=joke_language)
            return joke  # Return only the joke string
        except pyjokes.lang.JokesNotFoundError:
            return None  # Indicate that no joke is available
    else:
        return None  # Language not supported by pyjokes

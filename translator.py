import numpy as np
import json
import tensorflow as tf

VECTORIZER_JSON_PATH = r"Models/Attention/text_vectorizer.json"
MODEL_PATH = r"Models/Attention/TranslationModel"

f = open(VECTORIZER_JSON_PATH)
data = json.load(f)
f.close()
MAX_TOKENS = data['max_tokens']
OUTPUT_SEQUENCE_LENGTH = data['output_sequence_length']
VOCAB = data['vocab_data']

text_vec_layer_es = tf.keras.layers.TextVectorization(
    max_tokens=MAX_TOKENS,
    output_sequence_length=OUTPUT_SEQUENCE_LENGTH,
    vocabulary=VOCAB
)

model = tf.keras.models.load_model(MODEL_PATH)

def translate(en_sentence):
    print(f"Translating sentence: {en_sentence}")
    translation = ""
    for word_idx in range(OUTPUT_SEQUENCE_LENGTH):
        X = np.array([en_sentence])
        X_dec = np.array(["startofseq " + translation])
        y_proba = model.predict((X, X_dec))[0, word_idx]
        predicted_word_id = np.argmax(y_proba)
        predicted_word = text_vec_layer_es.get_vocabulary()[predicted_word_id]
        if predicted_word == "endofseq":
            break
        translation += " " + predicted_word

    print(translation.strip())

    return translation.strip()

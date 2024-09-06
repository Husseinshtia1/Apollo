import pandas as pd
import tensorflow as tf
from transformers import BertTokenizer, TFBertModel
from tensorflow.keras import layers
from config import CLEANED_DATA_FILE, MAX_TOKENS, SEQUENCE_LENGTH, BATCH_SIZE, EPOCHS

class BertTextAnalyzer:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = TFBertModel.from_pretrained('bert-base-uncased')

    def analyze(self, texts):
        inputs = self.tokenizer(texts, return_tensors='tf', padding=True, truncation=True, max_length=512)
        outputs = self.model(inputs)
        # استخدام GlobalAveragePooling1D لتقليل الأبعاد
        pooled_output = tf.keras.layers.GlobalAveragePooling1D()(outputs.last_hidden_state)
        return pooled_output

def build_model(input_dim, output_dim, input_length):
    model = tf.keras.Sequential([
        layers.Dense(128, activation='relu', input_shape=(input_dim,)),
        layers.Dropout(0.2),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_and_evaluate_bert():
    data = pd.read_csv(CLEANED_DATA_FILE)
    texts = data['text'].values

    # التحقق من أن النصوص صالحة وغير فارغة
    texts = [str(text) for text in texts if isinstance(text, str) and text.strip() != ""]
    if not texts:
        raise ValueError("No valid texts available for analysis.")

    analyzer = BertTextAnalyzer()
    embeddings = analyzer.analyze(texts)

    model = build_model(embeddings.shape[-1], 64, SEQUENCE_LENGTH)
    model.summary()

    # Placeholder labels for training (adjust as needed)
    y = tf.random.uniform((embeddings.shape[0], 1), minval=0, maxval=2, dtype=tf.int32)

    model.fit(embeddings, y, epochs=EPOCHS, batch_size=BATCH_SIZE)
    return model

if __name__ == "__main__":
    model = train_and_evaluate_bert()

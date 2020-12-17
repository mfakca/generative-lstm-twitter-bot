from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import pickle
import os
import sys



def predict(new_metin):

	new_sayi = 40
	# Model load
	model = tf.keras.models.load_model('saved_model.h5')

	# Tokenizer load
	with open('tokenizer.pickle', 'rb') as handle:
		tokenizer = pickle.load(handle)


	max_sequence_len =143

	for x in range(new_sayi):

		token_list = tokenizer.texts_to_sequences([new_metin])[0]
		token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
		predicted = model.predict_classes(token_list, verbose=0)

		output_word = ""
		for word,index in tokenizer.word_index.items():
			if index == predicted:
				output_word = word
				break

		new_metin += " "+output_word

	return new_metin

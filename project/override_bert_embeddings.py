# Override utility functions for TopicModelDataPreparation to support SentenceTransformers built from scratch
from sentence_transformers import SentenceTransformer
import numpy as npmodels

def bert_embeddings_from_file(text_file, sbert_model_to_load, custom=False, tokenizer_args=None, model_args=None, batch_size=200):
    """
    Creates SBERT Embeddings from an input file
    """
    from sentence_transformers import SentenceTransformer, models

    # For indicBERT
    if sbert_model_to_load == 'ai4bharat/indic-bert':
      custom = True
      tokenizer_args = {"keep_accents": True}

    # If build custom sentence transformer model
    if custom is True:
      if tokenizer_args and model_args:   # both set of arguments given in dict to pass into hugging face model
        word_embedding_model = models.Transformer(sbert_model_to_load, 
                                                  tokenizer_args=tokenizer_args, 
                                                  model_args = model_args)
      
      elif tokenizer_args:   # tokenizer arguments given in dict to pass into hugging face model
        word_embedding_model = models.Transformer(sbert_model_to_load, tokenizer_args = tokenizer_args)

      elif model_args:   # model arguments given in dict to pass into hugging face model
        word_embedding_model = models.Transformer(sbert_model_to_load, model_args = model_args)
      
      else:
        word_embedding_model = models.Transformer(sbert_model_to_load)

      # Pass modules to build sentence transformer model
      pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
      model = SentenceTransformer(modules=[word_embedding_model, pooling_model])   
    
    # Else retrieve model from hugging face
    else:
        model = SentenceTransformer(sbert_model_to_load)

    with open(text_file, encoding="utf-8") as filino:
        train_text = list(map(lambda x: x, filino.readlines()))

    return np.array(model.encode(train_text, show_progress_bar=True, batch_size=batch_size))


def bert_embeddings_from_list(texts, sbert_model_to_load, custom=False, tokenizer_args=None, model_args=None, batch_size=200, max_seq_length = 200):
    """
    Creates SBERT Embeddings from a list
    """
    from sentence_transformers import SentenceTransformer, models

    # For indicBERT
    if sbert_model_to_load == 'ai4bharat/indic-bert':
      custom = True
      tokenizer_args = {"keep_accents": True}

    # If build custom sentence transformer model
    if custom is True:
      if tokenizer_args and model_args:   # both set of arguments given in dict to pass into hugging face model
        word_embedding_model = models.Transformer(sbert_model_to_load, 
                                                  tokenizer_args=tokenizer_args, 
                                                  model_args = model_args)
      
      elif tokenizer_args:   # tokenizer arguments given in dict to pass into hugging face model
        word_embedding_model = models.Transformer(sbert_model_to_load, tokenizer_args = tokenizer_args)

      elif model_args:   # model arguments given in dict to pass into hugging face model
        word_embedding_model = models.Transformer(sbert_model_to_load, model_args = model_args)
      
      else:
        word_embedding_model = models.Transformer(sbert_model_to_load)

      # Pass modules to build sentence transformer model
      pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
      model = SentenceTransformer(modules=[word_embedding_model, pooling_model])   

    # Else retrieve model from hugging face
    else:
        model = SentenceTransformer(sbert_model_to_load)

    return np.array(model.encode(texts, show_progress_bar=True, batch_size=batch_size))

contextualized_topic_models.utils.data_preparation.bert_embeddings_from_file = bert_embeddings_from_file
contextualized_topic_models.utils.data_preparation.bert_embeddings_from_list = bert_embeddings_from_list

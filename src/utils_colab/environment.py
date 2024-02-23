import os
from dotenv import load_dotenv

content_path = '/content/privateGPT-axon'
private_path = '/content/drive/MyDrive/Projects/Python/private-DOCU'

env_path = f'{private_path}/src'

env_file = '.env'
env_file_path = f'{env_path}/{env_file}'
print(f'env_file_path: {env_file_path}')

#load_dotenv(env_file_path)

models_folder = 'models'

#source_documents_path = f'{private_path}/{source_documents}'
ue_53_path = 'UE_5.3/en-US/BlueprintAPI'
source_documents_path = f'{content_path}/{ue_53_path}'

dest_db = 'db'
dest_db_path = f'{private_path}/{dest_db}'
print(f'dest_db_path: {dest_db_path}')

#model_name = 'tinyllama-1.1b-chat-v1.0.Q5_K_M.gguf'
model_name = 'dolphin-2.6-mistral-7b.Q5_K_M.gguf'
embeddings_model_name = 'all-MiniLM-L6-v2'
model_type = 'LlamaCpp'
model_path = f'{content_path}/{models_folder}/{model_name}'
model_n_ctx = '1000'
model_n_batch = '8'
target_source_chunks = '4'

# Definisci la classe Environment
class Environment:
    def __init__(self):
        self.persist_directory = os.environ.get('PERSIST_DIRECTORY', dest_db_path)
        self.source_directory = os.environ.get('SOURCE_DIRECTORY', source_documents_path)
        self.model_name = os.environ.get('MODEL_NAME', model_name)
        self.embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME', embeddings_model_name)
        self.model_type = os.environ.get('MODEL_TYPE', model_type)
        self.model_path = os.environ.get('MODEL_PATH', model_path)
        self.model_n_ctx = os.environ.get('MODEL_N_CTX', model_n_ctx)
        self.model_n_batch = int(os.environ.get('MODEL_N_BATCH', model_n_batch))
        self.target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS', target_source_chunks))

    # Metodi set per ogni variabile
    def set_persist_directory(self, directory):
        self.persist_directory = directory
    
    def set_source_directory(self, directory):
        self.source_directory = directory
    
    def set_embeddings_model_name(self, name):
        self.embeddings_model_name = name
    
    # Metodi get per ogni variabile
    def get_persist_directory(self):
        return self.persist_directory
    
    def get_source_directory(self):
        return self.source_directory
    
    def get_embeddings_model_name(self):
        return self.embeddings_model_name

    def get_model_type(self):
        return self.model_type
    
    def get_model_path(self):
        return self.model_path
    
    def get_model_n_ctx(self):
        return self.model_n_ctx
    
    def get_model_n_batch(self):
        return self.model_n_batch
    
    def get_target_source_chunks(self):
        return self.target_source_chunks
    
    def print(self):
        # Accedere ai parametri e stamparli
        print("Persist Directory:", self.persist_directory)
        print("Source Directory:", self.source_directory)
        print("Model Name:", self.model_name)
        print("Embeddings Model Name:", self.embeddings_model_name)
        print("Model Type:", self.model_type)
        print("Model Path:", self.model_path)
        print("Model N Ctx:", self.model_n_ctx)
        print("Model N Batch:", self.model_n_batch)
        print("Target Source Chunks:", self.target_source_chunks)

    # Metodo print per stampare i dati della classe
    def print_data(self):
        data_str = f"persist_directory: {self.persist_directory}\n"
        data_str += f"source_directory: {self.source_directory}\n"
        data_str += f"model_name: {self.model_name}\n"
        data_str += f"embeddings_model_name: {self.embeddings_model_name}\n"
        data_str += f"model_type: {self.model_type}\n"
        data_str += f"model_path: {self.model_path}\n"
        data_str += f"model_n_ctx: {self.model_n_ctx}\n"
        data_str += f"model_n_batch: {self.model_n_batch}\n"
        data_str += f"target_source_chunks: {self.target_source_chunks}\n"
        return data_str    
from flask import Flask, render_template, request
import chromadb
from llama_index.core import Settings, StorageContext, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.chroma import ChromaVectorStore

# Initialize Flask app
app = Flask(__name__)

# Initialize ChromaDB client and collection
chroma_client1 = chromadb.PersistentClient(path='./final_project_db')
chroma_collection = chroma_client1.get_or_create_collection('finalproject_col')

# Set embedding model and LLM
embed_model = HuggingFaceEmbedding(model_name='BAAI/bge-small-en')
Settings.llm = Ollama(model="catsarethebest/llama3.2-4oClaude:latest", request_timeout=360.0)
Settings.embed_model = embed_model

# Set up vector store and index
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_vector_store(vector_store, storage_context=storage_context)

# Query engine
query_engine = index.as_query_engine(llm=Settings.llm)

@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'POST':
        company = request.form['company']
        focus = request.form['focus']

        # The main query instruction sent to your RAG
        full_query = (
            f"You are an AI Cloud Consultant helping design solutions for {company} with a focus on {focus}. "
            f"Suggest 3 to 5 AWS Bundles. "
            f"Each recommendation must: "
            f"- Be numbered (Recommendation 1, 2, etc.). "
            f"- Contain 3 to 5 AWS services bundled together, separated by commas. "
            f"- Include a short 1-2 line business reason. "
            f"Output STRICTLY in HTML table row format like this: "
            f"<tr><td>Recommendation 1</td><td>AWS Service 1, AWS Service 2, AWS Service 3</td><td>Short reason here.</td></tr>. "
            f"DO NOT explain anything else outside the table. DO NOT use bullet points. DO NOT create multiple columns for services. "
            f"Bundle services TOGETHER inside one single cell."
        )

        response = query_engine.query(full_query)
        return render_template('index.html', response=response)

    return render_template('index.html', response=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
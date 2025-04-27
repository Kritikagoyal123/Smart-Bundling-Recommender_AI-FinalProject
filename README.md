**📊 Smart Bundling Recommender**

The Smart Bundling Recommender is an AI-powered business tool that helps users generate customized AWS service bundles based on company name and focus area.
It is built using Flask, ChromaDB, Ollama LLM, and HuggingFace Embeddings, combined with a clean and responsive web front-end.


**🚀 Project Overview**
	•	Enter or select a Company Name
	•	Choose a Priority Area (Healthcare, AI/ML, Security, etc.)
	•	Get 3–5 tailored AWS product bundle recommendations with short business-focused reasons
	•	Output shown in a neatly formatted table (Recommendation #, Bundles, Reason)
	•	Built for Data Analysts, Cloud Consultants, and Solution Architects to quickly generate strategic cloud bundles


**🛠️ Technologies Used**
	•	Python (Flask Framework)
	•	HTML/CSS (Responsive Frontend)
	•	Chromadb (Vector Store)
	•	LlamaIndex (Vector RAG-based AI querying)
	•	Ollama LLM (Local Model Inference)
	•	HuggingFace Embeddings (BAAI/bge-small-en model)


**📸 Project Screenshot**
![Smart Bundling Recommender Screenshot](https://github.com/Kritikagoyal123/Smart-Bundling-Recommender_AI-FinalProject/raw/main/FrontEnd_SS.png)


**✨ Features**
	•	🔵 Flexible company input (type or select)
	•	🟢 Dynamic AWS Bundling based on use case
	•	🧠 Local LLM Integration with fast RAG querying
	•	📈 Clean, professional dashboard layout
	•	📋 Ready for expansion with CSV/PDF export (future scope)


**🧠 How It Works**
	1.	User inputs company name and priority.
	2.	Flask sends a structured query to the local Ollama LLM.
	3.	RAG (Retrieval Augmented Generation) based search enhances the model context.
	4.	Model returns AWS bundles formatted directly as HTML <tr><td> rows.
	5.	Frontend renders a clean, professional-looking recommendation table.


**🛠️ Setup Instructions**
	1.	Clone the repository:

git clone YOUR_REPO_LINK_HERE
cd your_project_folder

	2.	Install dependencies:

pip install flask chromadb llama-index huggingface-hub

	3.	Run Flask app:

python app.py

	4.	Open browser at:
http://127.0.0.1:5000/


**🔮 Future Enhancements **
	•	⭐ Highlight Top Recommendation
	•	📥 Download results as PDF or CSV
	•	📈 Add Bundle Suitability Scoring
	•	🎯 Build an enterprise multi-user version


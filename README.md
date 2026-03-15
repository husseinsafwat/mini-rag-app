# mini rag

---

this is a minimal implementation of the rag model for question answering.

## Requirements

---

- Python 3.8 or later

#### Install it using miniconda or conda

---



1) Download a miniconda through this link from [here](https://www.anaconda.com/docs/getting-started/miniconda/main#quick-command-line-install)
2) create a new environement using the following command

   ```
   $ conda create -n mini-rag python=3.8
   ```
3) activate conda environment using the following command

   ```
   conda activate mini-rag-app
   ```
   ## Installation

   ---

   ### Install the required packages


   ```
   $ pip install -r requirements.txt
   ```
   ### Setup the environment variables

   ```
   cp .env.example .env
   ```
   Set your environment variable in the .env file like OPENAI_API_KEY value.

   ## Run the FastAPI server

   ```
   uvicorn main:app --reload --host 0.0.0.0 --port 5000
   ```
   ## Donwload postman collection

   Download from postman collections [\assets\mini-rag-app.postman_collection.json](\assets\mini-rag-app.postman_collection.json)

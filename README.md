# Chat with Multiple PDFs

This project is a Streamlit application that leverages large language models and libraries such as Langchain, OpenAI, and Hugging Face to interact with multiple PDFs.

## Requirements

The following libraries are required for this project:

- streamlit
- pypdf2
- langchain
- python-dotenv
- faiss-cpu
- openai
- huggingface_hub

## Setup

1. **Clone the repository**

    ```sh
    git clone <repository-url>
    cd chat-with-multiple-pdf
    ```

2. **Create a virtual environment**

    - **Windows**

        ```sh
        python -m venv .venv
        .\.venv\Scripts\activate
        ```

    - **macOS/Linux**

        ```sh
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3. **Install the dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Create an `.env` file**

    In the root directory of the project, create a file named `.env` and add the following lines with your actual API keys and tokens:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    HUGGINGFACE_API_KEY=your_huggingface_api_key
    HUGGINGFACE_API_TOKEN=your_huggingface_api_token
    PINECONE_API_KEY=your_pinecone_api_key
    PINECONE_INDEX_NAME=your_pinecone_index_name
    PINECONE_ENVIRONMENT=your_pinecone_environment
    ```

5. **Run the application**

    ```sh
    streamlit run app.py
    ```

    This will start the Streamlit application and you can view it in your browser.

## .gitignore

Ensure you have a `.gitignore` file to exclude unnecessary files from the repository. Below is an example:

    ```plaintext
    # Virtual environment
    .venv/
    venv/
    ENV/
    env/

    # Python bytecode files
    __pycache__/
    *.py[cod]
    *$py.class

    # Environment variables
    .env

    # Jupyter Notebook checkpoints
    .ipynb_checkpoints

    # VS Code settings
    .vscode/

    # macOS system files
    .DS_Store

    # Windows system files
    Thumbs.db
    Desktop.ini

    # PyCharm
    .idea/

    # Log files
    *.log
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


# AI-Multi-Agent

A multi-agent AI system that fetches research papers from arXiv and summarizes them in a literature review format. This project leverages OpenAI's language model to streamline the research process by providing concise and informative summaries of relevant academic papers.

## Features

- **Paper Retrieval**: Automatically fetches research papers from arXiv based on user-defined queries.
- **Summarization**: Generates literature review-style summaries of the retrieved papers.
- **Multi-Agent Architecture**: Utilizes separate agents for searching and summarizing to enhance modularity and maintainability.

## Requirements

- Python 3.7 or higher
- `arxiv` library
- `autogen-agentchat` library
- `dotenv` library
- OpenAI API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/neelsoni26/ai-multi-agent.git
   cd ai-multi-agent
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the root directory and add your OpenAI API key:
     ```plaintext
     OPENAI_API_KEY="your_openai_api_key"
     ```

## Usage

To run the project, execute the following command:
```bash
python agent-be.py
```

## Example

You can modify the `task` variable in the `run_team` function to change the topic of the literature review. For example:
```python
task = "Conduct a literature review on the topic - Machine Learning and return exactly 5 papers."
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## Acknowledgments

- arXiv for providing access to a vast repository of research papers.
- OpenAI for their powerful language models.

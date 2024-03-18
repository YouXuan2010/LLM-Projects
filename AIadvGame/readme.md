# AI Adventure Game

This project is an interactive text-based adventure game where players embark on a mystical journey in the Whispering Woods. The game dynamically adapts the tale based on the player's decisions, creating a branching narrative experience where each choice leads to a new path, ultimately determining the fate of the traveler named Elara.

## Technologies Used

- **Cassandra Database**: Used for storing and managing chat history and conversation data.
- **OpenAI API**: Performs natural language processing and generates responses based on user input.
- **ConversationBufferMemory**: Stores chat history in memory.
- **PromptTemplate**: Defines template for generating prompts.

## Setup

### Prerequisites

- Python 3.x installed on your system.
- An OpenAI API key. You can obtain one from the OpenAI website.
- Cassandra database credentials and access to a Cassandra cluster.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/YouXuan2010/AI-playground.git
```

2. Navigate to the project directory:
```bash
cd AIadvGame
```

3. Install the required Python packages:
```bash
pip install -r requirements.txt
```
### Configuration

1. Create a .env file in the root directory of the project.
2. Add your OpenAI API key to the .env file:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```
3. Configure your Cassandra database credentials and connection details in the Python script.

## Usage

1. Run the Python script:
```bash
python main.py
```

2. Follow the prompts in the terminal to play the game. Make choices when prompted and watch the story unfold dynamically based on your decisions.

3. The game ends when the traveler finds the Gem of Serenity or gets killed, indicated by the text "The End.".
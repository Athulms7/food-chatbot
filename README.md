# Food & Recipe Chatbot

An AI-powered chatbot that provides nutritional information, healthy meal suggestions, and step-by-step recipes. Built with Gradio and powered by Groq's LLM.

## Features

- Interactive chat interface
- Nutritional information
- Recipe suggestions
- Dietary advice
- Step-by-step cooking instructions

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Athulms7/food-chatbot.git
   cd food-chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Groq API key:
   - Create a `.env` file in the root directory
   - Add your API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

4. Run the application:
   ```bash
   python app.py
   ```

## Local Development

The application will be available at:
- Local URL: http://localhost:8080
- Public URL: (provided when running the app)

## Technologies Used

- Python
- Gradio
- Groq API
- Render (for deployment)

## Environment Variables

- `GROQ_API_KEY`: Your Groq API key

## License

MIT 
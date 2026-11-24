
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Initialize Gemini client
client = genai.Client(api_key=api_key)


# Create Research Agent
class ResearchAgent:

    def __init__(self):
        self.name = "Research Assistant"

        self.instructions = """
        You are an intelligent AI Research Assistant.

        Your responsibilities:
        1. Understand the research topic.
        2. Explain the topic clearly.
        3. Organize the response into sections.
        4. Include applications, benefits and challenges.
        5. Provide a meaningful conclusion.

        Do not invent research citations or statistics.
        Mention when information needs verification.
        """

    def research(self, topic):

        print("\nResearch Agent is working...\n")

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"Research this topic: {topic}",
            config=types.GenerateContentConfig(
                system_instruction=self.instructions,
                temperature=0.4
            )
        )

        return response.text


# Create agent
agent = ResearchAgent()

# Get user input
topic = input("Enter your research topic: ")

# Execute agent
result = agent.research(topic)

# Display result
print("\n========== RESEARCH REPORT ==========\n")
print(result)

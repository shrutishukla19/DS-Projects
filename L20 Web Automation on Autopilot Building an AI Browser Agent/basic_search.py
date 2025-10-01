import os
import asyncio
from dotenv import load_dotenv
from browser_use import Agent
from browser_use.llm import ChatGoogle


# Load variables from .env
load_dotenv()

async def main():
    # Fetch the key from .env
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found. Check your .env file.")

    llm = ChatGoogle(model="gemini-2.5-flash", api_key)	
	
    
    agent = Agent(task="Search for AI news", llm=llm)
    result = await agent.run()
    
    print('------------------------------------------')
    print("Visited URLs:")
    print(result.urls())
    print('------------------------------------------')

if __name__ == "__main__":
    asyncio.run(main())

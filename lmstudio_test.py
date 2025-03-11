import asyncio
import sys
from app.llm import LLM
from app.schema import Message
from app.logger import logger

async def test_lmstudio():
    """Test the LM Studio integration"""
    try:
        # Initialize LLM with lmstudio configuration
        llm = LLM(config_name="lmstudio")
        
        # Log the configuration
        logger.info(f"Using model: {llm.model}")
        logger.info(f"Base URL: {llm.base_url}")
        logger.info(f"API type: {llm.api_type}")
        
        # Create a simple message
        messages = [
            Message.system_message("You are a helpful assistant."),
            Message.user_message("Hello, can you tell me a short joke?")
        ]
        
        # Test the ask method
        print("\nTesting ask method...")
        response = await llm.ask(messages)
        print(f"\nResponse: {response}")
        
        print("\nTest completed successfully!")
        return 0
    except Exception as e:
        logger.error(f"Error testing LM Studio: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(asyncio.run(test_lmstudio())) 
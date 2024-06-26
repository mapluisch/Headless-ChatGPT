import asyncio
from gpt import GPT

async def run_session():
    # create gpt instance & send initial prompt
    session = GPT(prompt="Tell me a joke.", streaming=True)
    
    await session.start() 
    
    # (optional) send additional prompts and handle them
    print("\n -- asking GPT to explain the joke -- \n")
    await session.handle_prompt("Explain the joke.")

    # gracefully close the session again
    await session.close()

asyncio.run(run_session())

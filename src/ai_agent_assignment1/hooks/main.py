import asyncio
from agents import Runner
from dotenv import load_dotenv
import os
from inventory_agent.main import coordinator_agent

load_dotenv()

async def main():
    runner = Runner()

    print("📦 Inventory Management System")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\n📝 Command: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        result = await runner.run(coordinator_agent, user_input)
        print("✅ Response:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

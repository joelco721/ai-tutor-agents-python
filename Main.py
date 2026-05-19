from dotenv import load_dotenv
import asyncio
import Instructions
from agents import Agent, Runner, function_tool, WebSearchTool

load_dotenv()

@function_tool
def math_fun_jokes() -> str:
    """Return a short math joke"""
    return " did you know 2 + 2 = 22. HAHA, I am joking :)"


math_agent_tutor = Agent(
    name="Math tutor",
    instructions=Instructions.MATH,
    tools=[math_fun_jokes],
    model="gpt-5.5",
) 


history_agent_tutor = Agent(
    name="History tutor",
    instructions=Instructions.HISTORY,
    tools=[WebSearchTool()],
    model="gpt-5.5",
)



choice_agent = input("Choose which agent you want:\n1: Math tutor\n2: History tutor.\n")


if choice_agent == "1":
    agent = math_agent_tutor
    user_input = input("Ask any math questions.\n")
elif choice_agent == "2":
    agent = history_agent_tutor
    user_input = input("Ask any history question.\n")
else:
    print("Invalid choice")
    exit()
    
async def main() -> None:
    result = await Runner.run(
        agent,
        user_input,
    )


    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
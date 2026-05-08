from agent.planner import Planner
from agent.executor import Executor

def main():
    task = input("Enter your task: ")

    planner = Planner()
    executor = Executor()

    plan = planner.create_plan(task)
    result = executor.execute(plan)

    print("\nFinal Result:\n", result)

if __name__ == "__main__":
    main()

class Executor:
    def execute(self, plan):
        print("Executing plan...")
        results = []
        for step in plan:
            results.append(f"Executed: {step['action']}")
        return "\n".join(results)

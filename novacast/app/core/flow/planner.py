class PlanStep:
    def __init__(self, name, action, dependencies=None):
        self.name = name
        self.action = action
        self.dependencies = dependencies if dependencies else []

    def validate(self):
        if not self.name or not self.action:
            raise ValueError("Both name and action must be provided for a plan step.")

class Planner:
    def __init__(self):
        self.plans = []

    def create_plan(self, plan_name, steps):
        plan = {
            "name": plan_name,
            "steps": steps
        }
        self.plans.append(plan)

    def validate_plan(self, plan):
        for step in plan['steps']:
            step.validate()

    def execute_plan(self, plan):
        for step in plan['steps']:
            step.action()  # Assuming action is a callable

    def get_plans(self):
        return self.plans

# Example usage
if __name__ == "__main__":
    planner = Planner()
    step1 = PlanStep("Step 1", lambda: print("Executing Step 1"))
    step2 = PlanStep("Step 2", lambda: print("Executing Step 2"), dependencies=[step1])

    planner.create_plan("My Plan", [step1, step2])
    for plan in planner.get_plans():
        planner.validate_plan(plan)
        planner.execute_plan(plan)
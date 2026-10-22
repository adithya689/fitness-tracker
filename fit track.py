print("=" * 40)
print("       FITTRACK ANALYZER")
print("=" * 40)

# Get fitness information from the user
weight = float(input("Enter your weight in kg: "))
steps = int(input("Enter your daily steps: "))
workout_minutes = int(input("Enter workout duration in minutes: "))

daily_step_goal = 10000

print("\n--- Your Fitness Report ---")

print(f"Weight: {weight} kg")
print(f"Daily Steps: {steps}")
print(f"Workout Duration: {workout_minutes} minutes")

print("\n--- Fitness Insights ---")

if steps >= daily_step_goal:
    print("Step Goal: Achieved!")
else:
    remaining = daily_step_goal - steps
    print(f"Steps remaining: {remaining}")

if workout_minutes > 0:
    print("Workout Status: Completed")
else:
    print("Workout Status: Rest Day")

print("=" * 40)
print("Fitness report completed!")
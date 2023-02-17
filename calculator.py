# here is the original code for the formula
reps = float(input("Reps: "))
rpe = float(input("RPE: "))
load = float(input("Weight: "))

rpe10_reps = reps + (10 - rpe)
percentage = -0.01651 * rpe10_reps**3 + 0.3743 * rpe10_reps**2 - 5.2 * rpe10_reps + 104.9
e1rm = round(100 * load / percentage)

print(f"Estimated 1 rep max: {e1rm}")


# here it is as a function
def calc_e1rm(reps, load, rir):
    rpe10_reps = reps + rir
    percentage = -0.01651 * rpe10_reps**3 + 0.3743 * rpe10_reps**2 - 5.2 * rpe10_reps + 104.9
    e1rm = round(100 * load / percentage)
    return e1rm


def calc_e1rm(reps, load, rir):
    rpe10_reps = reps + rir
    percentage = -0.01651 * rpe10_reps**3 + 0.3743 * rpe10_reps**2 - 5.2 * rpe10_reps + 104.9
    e1rm = round(100 * load / percentage)
    return e1rm

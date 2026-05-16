def run_simulation(orders, workers, speed):

    total_capacity = workers * speed

    time_required = orders / total_capacity

    delay_risk = "LOW"

    if workers < 5:
        delay_risk = "HIGH"
    elif workers < 10:
        delay_risk = "MEDIUM"

    return {
        "total_capacity": total_capacity,
        "time_required": round(time_required, 2),
        "delay_risk": delay_risk
    }
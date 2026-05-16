from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')


def simulate(request):
    result = None

    if request.method == "POST":
        orders = int(request.POST.get('orders'))
        workers = int(request.POST.get('workers'))
        speed = int(request.POST.get('speed'))

        # Simple Simulation Logic
        total_capacity = workers * speed
        time_required = orders / total_capacity

        if time_required <= 8:
            status = "No Delay"
        else:
            status = "Delay"

        result = {
            "time": round(time_required, 2),
            "status": status
        }

    return render(request, 'home.html', {"result": result})

def optimize(request):

    orders = int(request.GET.get("orders", 100))
    speed = float(request.GET.get("speed", 1))

    best_workers = None
    best_time = float("inf")

    results = []

    for workers in range(1, 21):

        total_capacity = workers * speed

        if total_capacity <= 0:
            continue

        time_required = orders / total_capacity

        results.append({
            "workers": workers,
            "capacity": total_capacity,
            "time": round(time_required, 2)
        })

        if time_required < best_time:
            best_time = time_required
            best_workers = workers

    return JsonResponse({
        "input": {
            "orders": orders,
            "speed": speed
        },
        "best_configuration": {
            "workers": best_workers,
            "time_required": round(best_time, 2)
        },
        "all_simulations": results,
        "status": "Optimization completed"
    })  
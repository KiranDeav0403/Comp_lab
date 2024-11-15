import random

def estimate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x,y = random.uniform(-1,1), random.uniform(-1,1)
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

    return (4 * points_inside_circle) / (num_points)

sample_sizes = [100, 1000, 10000, 100000, 1000000, 100000000]
for size in sample_sizes:
    print(f"Estimate for {size} points: {estimate_pi(size)}")




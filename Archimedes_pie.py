import math

def archimedes_pie_estimation(sides):

    radius = 1
    angle = math.pi / sides

    #Circumscribed polygon

    circumscribed_perimeter = sides * (2 * radius * math.tan(angle))
    circumscribed_pie = circumscribed_perimeter/(2 * radius)

    #Inscribed polygon
    inscribed_perimeter = sides * (2 * radius * math.sin(angle))
    inscribed_pie = inscribed_perimeter/ (2 * radius)

    # average
    average_pi = (circumscribed_pie+inscribed_pie)/ 2
    return inscribed_pie, circumscribed_pie, average_pi

for sides in [6, 8, 10, 12]:
    inscribed, circumscribed, average = archimedes_pie_estimation(sides)
    print(f"Sides: {sides}, Inscribed: {inscribed}, Circumscribed: {circumscribed}, Average: {average}")
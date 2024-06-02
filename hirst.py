import colorgram
colors = colorgram.extract('photo.jpg', 11)
list1 = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.r
    b = i.rgb.b
    new_color_scheme = (r, g, b)
    list1.append(new_color_scheme)

print(list1)

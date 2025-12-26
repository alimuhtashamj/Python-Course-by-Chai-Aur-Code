
color_input = (input("What is your banana color?")).lower().strip()
#strip removes the leading and trailing space
color = [ 'green', 'yellow','brown']
ripeness = ['Unripe','Ripe','Overripe']
if color_input in color:
    idx = color.index(color_input)
    print(ripeness[idx])
else:
    print('Information not available')
    
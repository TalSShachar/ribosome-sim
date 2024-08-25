import pygame

# Function to draw the polygon with rectangular "teeth"
def draw_polygon_with_bottom_teeth(screen, color, x, y, rect_width, rect_height, teeth_height, num_teeth):
    teeth_width = rect_width / (2*num_teeth + 1)
    points = [
        (x, y),  # Top-left corner
        (x + rect_width, y),  # Top-right corner
        (x + rect_width, y + rect_height)  # Bottom-right before teeth start
    ]
    start_x, start_y = x + rect_width, y + rect_height

    # Add the teeth as rectangular segments
    for i in range(num_teeth):
        # start_x = x + i * (teeth_width * 2)
        points.append((start_x - teeth_width, start_y))  # left
        points.append((start_x - teeth_width, start_y - teeth_height))  # up
        start_x -= teeth_width
        points.append((start_x - teeth_width, start_y - teeth_height))  # left
        points.append((start_x - teeth_width, start_y))  # down
        start_x -= teeth_width

    points.append((x, y + rect_height))  # Close the polygon at bottom-left

    # Draw the polygon
    pygame.draw.polygon(screen, color, points)

    

def draw_polygon_with_upper_teeth(screen, color, x, y, rect_width, rect_height, teeth_height, num_teeth):
    teeth_width = rect_width / (2*num_teeth + 1)
    points = [
        (x, y + rect_height),  # Bottom-left corner
        (x + rect_width, y + rect_height)  # Bottom-right before teeth start
    ]
    start_x, start_y = x + rect_width, y 

    # Add the teeth as rectangular segments
    for i in range(num_teeth):
        points.append((start_x - teeth_width, start_y))  # left
        points.append((start_x - teeth_width, start_y - teeth_height))  # up
        start_x -= teeth_width
        points.append((start_x - teeth_width, start_y - teeth_height))  # left
        points.append((start_x - teeth_width, start_y))  # down
        start_x -= teeth_width


    # Draw the polygon
    pygame.draw.polygon(screen, color, points)

    
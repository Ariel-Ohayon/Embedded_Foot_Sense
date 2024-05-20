import cv2

# Global variable to store the last mouse position
last_x, last_y = -1, -1

# Mouse callback function to update the last mouse position
def update_mouse_position(event, x, y, flags, param):
    global last_x, last_y
    if event == cv2.EVENT_MOUSEMOVE:
        last_x, last_y = x, y

# Read the image from file
image_path = 'img.png'  # Path to the image file
image = cv2.imread(image_path)

# Check if the image was loaded properly
if image is None:
    print("Error: Could not load image.")
else:
    # Resize the image to 361x791
    image = cv2.resize(image, (361, 791))

    # Create a window and set the mouse callback function
    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', update_mouse_position)

    while True:
        # Create a copy of the image to display the color information
        img_copy = image.copy()

        # Check if the mouse is inside the image bounds
        if 0 <= last_x < image.shape[1] and 0 <= last_y < image.shape[0]:
            # Get the BGR color of the pixel at the last mouse position
            bgr_color = image[last_y, last_x]
            b, g, r = bgr_color[0], bgr_color[1], bgr_color[2]

            # Put text on the image displaying the BGR color values
            text = f"BGR: ({b}, {g}, {r})"
            cv2.putText(img_copy, text, (last_x, last_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Display the image with the color information
        cv2.imshow('Image', img_copy)

        # Wait for a key press and exit the loop if ESC is pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Destroy all windows
    cv2.destroyAllWindows()

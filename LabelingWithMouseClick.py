import cv2
import os

# Create a function based on a CV2 Event (Left button click)
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img_copy, (x, y), 1, (0, 0, 255), 5)
        
        # Write the coordinates to a file with a unique name
        file_name = os.path.join(texts_folder, os.path.splitext(image_file)[0] + ".txt")
        with open(file_name, "a") as f:
            f.write(f"({x}, {y})\n")

# Folder path containing the photos
folder_path = 'images'
# Folder path containing the texts
texts_folder = 'texts'
# Folder path containing images with circles
img_folder = 'imageWithCircles'
# Get a list of all the image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".png"))]

for image_file in image_files:
    # Build the full path of the image file
    image_path = os.path.join(folder_path, image_file)

    # Read the image
    img = cv2.imread(image_path)
    img_copy = img.copy()

    # Create a named window for each image
    cv2.namedWindow(winname='Get_points')
    # Connect the mouse button to the callback function
    cv2.setMouseCallback('Get_points', draw_circle)

    while True:  # Runs forever until we break with Esc key on the keyboard
        # Show the image window with circles
        cv2.imshow('Get_points', img_copy)
        if cv2.waitKey(20) & 0xFF == 27:
            break

    # Save the modified image with circles
    new_image_path = os.path.join(img_folder, os.path.splitext(image_file)[0] + "_circles.jpg")
    cv2.imwrite(new_image_path, img_copy)

    # Close the image window
    cv2.destroyAllWindows()
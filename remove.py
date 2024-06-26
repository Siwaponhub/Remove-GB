from rembg import remove
from PIL import Image
import os

def list_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    return image_files

def convert_to_png(input_folder_path, file_name):
    input_path = os.path.join(input_folder_path, file_name)
    output_path = os.path.splitext(input_path)[0] + ".png"
    
    if input_path != output_path:
        try:
            Image.open(input_path).convert("RGBA").save(output_path)
            os.remove(input_path)  
            print(f"converted {file_name} to PNG")
        except Exception as e:
            print(f"A conversion error occurred. {file_name} to PNG: {e}")

def main():
    #set your project_directory
    project_directory = r'C:\Users\Siwapon\Desktop\Learning\removebg'
    input_folder = 'before'
    output_folder = 'after'
    input_folder_path = os.path.join(project_directory, input_folder)
    image_files = list_files_in_folder(input_folder_path)
    for file in image_files:
        if not file.lower().endswith('.png'):
            convert_to_png(input_folder_path, file)
    image_files = list_files_in_folder(input_folder_path)

    print("List of files in folde before:")
    for i, file in enumerate(image_files, start=1):
        print(f"{i}. {file}")
    while True:
        try:
            selection = int(input("Select the number of image files to edit : "))
            if 1 <= selection <= len(image_files):
                selected_file = image_files[selection - 1]
                break
            else:
                print("Please select the correct number.")
        except ValueError:
            print("Please enter number")
    input_path = os.path.join(input_folder_path, selected_file)
    output_path = os.path.join(project_directory, output_folder, selected_file)
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)

    print(f"Save the edited image to {output_path}")

if __name__ == "__main__":
    main()

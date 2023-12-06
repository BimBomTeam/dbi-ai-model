from PIL import Image
import os


def load_data_set(test_folder_path):
    all_objects = os.listdir(test_folder_path)

    folders = [obj for obj in all_objects if os.path.isdir(os.path.join(test_folder_path, obj))]

    # Виведіть назви всіх папок
    for i in range(len(folders)):
        class_folder_path = os.path.join(test_folder_path, folders[i])
        all_objects = os.listdir(class_folder_path)
        images_names = [obj for obj in all_objects if obj.lower().endswith(('.jpg', '.jpeg',
                                                                            '.png', '.gif', '.bmp', '.tiff'))]

        for image_name in images_names:
            img_path = os.path.join(class_folder_path, image_name)
            try:
                img = Image.open(img_path)
                resized_img = img.resize((150, 150))
                resized_img.save(img_path)

            except:
                if os.path.exists(img_path):
                    os.remove(img_path)
                    print(f"Файл {img_path} удален.")
                else:
                    print(f"Файл {img_path} не существует.")


def main():
    path = input("Enter path to dataset (folder train\ valid\ test):\n")
    load_data_set(path)


main()

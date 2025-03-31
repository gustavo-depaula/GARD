import os
import cv2

folder_path = "p_BaseImages_dreamshaper-xl"

selected_folder = "p_selected_BaseImages"
os.makedirs(selected_folder, exist_ok=True)

history_file = "classified_images.txt"

# Load already classified images
if os.path.exists(history_file):
    with open(history_file, "r") as f:
        classified_images = set(f.read().splitlines())
else:
    classified_images = set()

# Gather images that haven't been classified yet
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
image_files = [img for img in image_files if img not in classified_images]

if not image_files:
    print("✅ All images have been classified! No more images to review.")
    exit()

print(f"📂 Found {len(image_files)} images to classify.")

cv2.namedWindow("🖼 Image Viewer", cv2.WINDOW_NORMAL)
cv2.resizeWindow("🖼 Image Viewer", 1280, 720)

for idx, img_name in enumerate(image_files):
    img_path = os.path.join(folder_path, img_name)
    original_image = cv2.imread(img_path)

    if original_image is None:
        print(f"⚠️ Skipping invalid image: {img_name}")
        continue

    print(f"[{idx+1}/{len(image_files)}] Viewing: {img_name}")
    cv2.imshow("🖼 Image Viewer", original_image)

    while True:
        key = cv2.waitKey(100)
        if key == 32:  # SPACE key
            cv2.imwrite(os.path.join(selected_folder, img_name), original_image)
            print(f"✅ Selected: {img_name}")
            break

        elif key == ord('x'):  # 'x' key -> delete the image
            os.remove(img_path)
            print(f"❌ Deleted: {img_name}")
            break


        elif key == ord('q'):  # Quit early
            print("🚪 Exiting early. Progress saved.")
            cv2.destroyAllWindows()
            exit()

    with open(history_file, "a") as f:
        f.write(img_name + "\n")

cv2.destroyAllWindows()
print("🎉 Done! All images have been reviewed.")


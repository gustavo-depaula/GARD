# GARD: Gustavo’s Awesome Runway Dataset ✈️

Read the full thesis here: [**LANDING IN THE LATENT SAPCE**](./thesis/LandingInTheLatentSpace.pdf), _Building labeled synthetic runway datasets with a data augmentation pipeline that uses diffusion models_

Access the dataset on [Kaggle](https://www.kaggle.com/datasets/depaulagu/gard2025)

> "But test everything; hold fast what is good." — _1 Thessalonians 5:21_

---

## 📜 About

GARD is the largest publicly available synthetic runway dataset, created entirely through a modular data augmentation pipeline called **Canny2Concrete** that leverages latent diffusion models (Stable Diffusion XL + ControlNet). It was developed as part of a BSc Computer Science Final Project at the University of London in 2025.

GARD contains **45,486 high-resolution images**, annotated with pixel-level segmentation masks and YOLO-format labels, featuring:

- Varied **lighting** conditions (day, night, dusk, dawn)
- Multiple **weather** conditions (rain, fog, snow)
- Realistic **backgrounds** and occlusions

---

## 🧠 Key Contributions

- 🔧 **Canny2Concrete Pipeline**: A modular, open-source pipeline to generate realistic runway images from structural templates using ControlNet and Stable Diffusion XL.
- 🧪 **Intrinsic and Extrinsic Evaluations**: Metrics like SSIM and real-model performance using YOLOv11.
- 📊 **Largest Synthetic Runway Dataset**: Surpassing BARS, RLD, LARD, and FS2020 in size and environmental diversity.
- 💡 **Reproducibility**: Full metadata stored in JSON for every image, including generation parameters and random seeds.

---

## 🖼️ Sample Images

First row is template image (from LARD), canny edge structure, and binary segmentation
mask. Then, the other three rows are images from the Base Images, Variant
Images, and Variant Images With Occlusion datasets, respectively.

![](./thesis/figures/GeneratedImage1.png)
![](./thesis/figures/GeneratedImage2.png)
![](./thesis/figures/GeneratedImage3.png)

---

## 📁 Dataset Access

📦 **Kaggle**:  
👉 [https://www.kaggle.com/datasets/depaulagu/gard2025](https://www.kaggle.com/datasets/depaulagu/gard2025)

🧪 Includes:

- `BaseImages/`: 6,498 base images
- `VariantImages/`: 19,494 with rotation and outpainting
- `VariantImagesWithOcclusion/`: 19,494 with environmental occlusion

Each image has:

- `.png` image
- `.json` label with metadata
- `.mask.png` segmentation mask
- `.txt` YOLO-format label

---

## 🧪 Experimental Validation

Using YOLOv11:

- Trained on GARD, validated against real LARD test sets.
- GARD-trained models matched or outperformed models trained on LARD. Results
  published in the thesis and, along with trained segmentation models' weights, publicly available on Kaggle
- SSIM confirms image diversity while maintaining structural fidelity.

---

## 🛠 Tech Stack

- Python, PyTorch
- Diffusers, ControlNet, Albumentations, ImgAug, OpenCV
- Stable Diffusion XL (DreamShaper XL)
- YOLOv11
- Kaggle Datasets
- Jupyter Notebooks

---

## 🤝 Acknowledgments

This work is dedicated to:

- _To Our Lady, Mary_, Mother of God and my mother, in gratitude for
  her maternal care and intercession throughout this journey.
- _To Saint Thomas Aquinas_, the Angelic Doctor, whose love of truth
  shaped the Christian intellectual tradition.

_**May this work, in whatever good it contains, be for the glory of God and
the service of truth.**_

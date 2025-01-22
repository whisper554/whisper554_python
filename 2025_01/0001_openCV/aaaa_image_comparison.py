"""
环境：opencv-python、numpy
运行脚本时，通过命令行传入两个图像路径，例如：
python aaaa_image_comparison.py image1.jpg image2.jpg
"""


import cv2
import argparse


def comparison_mse(image_path1, image_path2):
    # 读入两张图像
    img1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

    # 检查图像是否为空
    if img1 is None:
        print(f"Failed to read {image_path1}. Please check the file path.")
        return
    if img2 is None:
        print(f"Failed to read {image_path2}. Please check the file path.")
        return

    # 检查图像大小是否一致
    if img1.shape != img2.shape:
        print("Error: Images have different sizes.")
        return

    # 均方误差
    mse = ((img1 - img2) ** 2).mean()
    print('MSE:', mse)
    return mse, img1, img2


def main():
    # 使用 argparse 解析命令行参数
    parser = argparse.ArgumentParser(description="Compare two images and calculate MSE.")
    parser.add_argument("image1", help="Path to the first image")
    parser.add_argument("image2", help="Path to the second image")
    args = parser.parse_args()

    comparison_mse(args.image1, args.image2)


if __name__ == '__main__':
    main()

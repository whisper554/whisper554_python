"""
环境：opencv-python、numpy
运行脚本时，通过命令行传入两个图像路径，例如：
python aadb_image_PSNR.py image1.jpg image2.jpg

PSNR 值越大，表示图像的质量越好，一般来说：
（1）高于40dB：说明图像质量极好(即非常接近原始图像)
（2）30—40dB：通常表示图像质量是好的(即失真可以察觉但可以接受)
（3）20—30dB：说明图像质量差
（4）低于20dB：图像质量不可接受
"""


from aaaa_image_comparison import comparison_mse
import numpy as np
import argparse


def comparison_rgbPSNR(image_path1, image_path2):
    mse, img1, img2 = comparison_mse(image_path1, image_path2)  # from aaaa_image_comparison

    """
    计算两幅 RGB 图像之间的 PSNR（峰值信噪比）。
    :param image1: 第一幅图像（NumPy数组，形状为(row, col, 3)）
    :param image2: 第二幅图像（NumPy数组，形状为(row, col, 3)）
    :return: PSNR 值（单位：dB）
    """

    # 确保输入图像是浮点类型
    image1 = np.float64(img1)
    image2 = np.float64(img2)

    # 获取图像的行数和列数
    row, col = image1.shape[:2]

    # 分离 RGB 通道
    image1_r, image1_g, image1_b = image1[:, :, 0], image1[:, :, 1], image1[:, :, 2]
    image2_r, image2_g, image2_b = image2[:, :, 0], image2[:, :, 1], image2[:, :, 2]

    # 计算每个通道的 MSE
    mse_r = np.sum((image1_r - image2_r) ** 2)
    mse_g = np.sum((image1_g - image2_g) ** 2)
    mse_b = np.sum((image1_b - image2_b) ** 2)

    # 计算总 MSE
    mse_rgb = mse_r + mse_g + mse_b
    mse_new = mse_rgb / (row * col * 3)  # 除以总像素数和通道数

    # 计算 PSNR
    b = 8  # 每个像素的位数
    image_max = 2 ** b - 1  # 最大像素值（对于8位图像，为255）
    psnr_value = 20 * np.log10(image_max / np.sqrt(mse_new))
    print(f"PSNR 值: {psnr_value:.2f} dB")

    return psnr_value, image1, image2


def comparison_grayPSNR(image_path1, image_path2):
    mse, img1, img2 = comparison_mse(image_path1, image_path2)  # from aaaa_image_comparison
    pass


def comparison_ycbcPSNR(image_path1, image_path2):
    mse, img1, img2 = comparison_mse(image_path1, image_path2)  # from aaaa_image_comparison
    pass


def main():
    # 使用 argparse 解析命令行参数
    parser = argparse.ArgumentParser(description="Compare two images and calculate PSNR.")
    parser.add_argument("image1", help="Path to the first image")
    parser.add_argument("image2", help="Path to the second image")
    args = parser.parse_args()

    rgb_psnr_value = comparison_rgbPSNR(args.image1, args.image2)[0]
    gray_psnr_value = comparison_grayPSNR(args.image1, args.image2)[0]
    ycbc_psnr_value = comparison_ycbcPSNR(args.image1, args.image2)[0]
    avr_psnr_value = (rgb_psnr_value + gray_psnr_value + ycbc_psnr_value) / 3

if __name__ == '__main__':
    main()

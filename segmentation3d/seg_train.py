import argparse

from segmentation3d.core.seg_train import train


def main():

    import os
    os.environ['CUDA_VISIBLE_DEVICES'] = '7'

    long_description = "Training engine for 3d medical image segmentation"
    parser = argparse.ArgumentParser(description=long_description)

    parser.add_argument('-i', '--input',
                        default=['/home/qinliu19/projects/Medical-Segmentation3d-Toolkit/segmentation3d/config/train_config.py',
                                 '/home/qinliu19/projects/Medical-Segmentation3d-Toolkit/segmentation3d/config/infer_config.py'],
                        help='configure file for medical image segmentation training.')
    parser.add_argument('-g', '--gpu_id',
                        help='gpu_id for inference',
                        default=0)

    args = parser.parse_args()
    train(args.input[0], args.input[1], args.gpu_id)


if __name__ == '__main__':
    main()

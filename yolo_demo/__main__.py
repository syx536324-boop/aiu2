"""Command-line composition root for training and prediction."""

from __future__ import annotations

import argparse
from pathlib import Path

from .tasks import predict_image, train_demo


def main() -> None:
    parser = argparse.ArgumentParser(description="AIU2 YOLO11n demo")
    subcommands = parser.add_subparsers(dest="command", required=True)
    subcommands.add_parser("train", help="Fine-tune YOLO11n on COCO8 for three epochs")
    predict = subcommands.add_parser("predict", help="Run detection on one image")
    predict.add_argument("--source", type=Path, help="Image path; defaults to a COCO8 validation image")
    args = parser.parse_args()
    if args.command == "train":
        train_demo()
    else:
        predict_image(args.source)


if __name__ == "__main__":
    main()

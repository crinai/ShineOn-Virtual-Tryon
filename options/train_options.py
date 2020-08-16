import argparse

from options.base_options import BaseOptions


class TrainOptions(BaseOptions):
    def initialize(self, parser: argparse.ArgumentParser):
        parser = BaseOptions.initialize(self, parser)
        # data
        parser.add_argument("--no_shuffle", action="store_true", help="don't shuffle input data")
        # checkpoints
        parser.add_argument(
            "--save_count",
            type=int,
            help="how often in steps to always save a checkpoint",
            default=1000,
        )
        parser.add_argument(
            "--val_check_interval",
            "--val_frequency",
            dest="val_check_interval",
            type=float,
            default=1,
            help="validate and potentially save a checkpoint after this many epochs"
        )
        # optimization
        parser.add_argument(
            "--lr", type=float, default=1e-4, help="initial learning rate for adam"
        )
        parser.add_argument(
            "--keep_epochs",
            type=int,
            help="number of epochs with initial learning rate",
            default=5,
        )
        parser.add_argument(
            "--decay_epochs",
            type=int,
            help="number of epochs to linearly decay the learning rate",
            default=5,
        )
        self.isTrain = True
        return parser

import ml_collections


def get_config():
    """
    Configure hyperparameters for training here.
    Data from ConfigDict can be accessed from the
    outside as any DictLike object.
    Example:
        >>> cfg = get_config()
        >>> print(cfg.learning_rate)
        >>> 0.1
    """
    config = ml_collections.ConfigDict()

    config.learning_rate = 0.1
    config.warmup_epochs = 5.0
    config.momentum = 0.9
    config.batch_size = 64

    config.num_epochs = 10
    config.log_every_steps = 100

    config.cache = False
    config.half_precision = False

    # If num_train_steps==-1 then the number of training steps is calculated from
    # num_epochs using the entire dataset. Similarly for steps_per_eval.
    config.num_train_steps = -1
    config.steps_per_eval = -1

    return config

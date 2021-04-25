from django.apps import AppConfig
from pathlib import Path

from predictor.settings import BASE_DIR

import tensorflow as tf


class AppConfig(AppConfig):
    name = "app"

    model = tf.keras.models.load_model(str(BASE_DIR / "model.tf"))

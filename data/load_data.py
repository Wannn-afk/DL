"""Helper untuk memuat data UTS DL.

klasifikasi_train.npz dan clustering.npz dipecah jadi beberapa part (<100 MB per file,
batas GitHub). Fungsi di sini menggabungkannya kembali sesuai urutan `indeks` di file meta.

Contoh:
    from data.load_data import load_klasifikasi_train
    gambar, sensor, meta = load_klasifikasi_train()
"""
from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent


def _load_parts(prefix):
    parts = sorted(DATA_DIR.glob(f"{prefix}_part*.npz"), key=lambda p: int(p.stem.rsplit("part", 1)[1]))
    if not parts:
        raise FileNotFoundError(f"Tidak ada file {prefix}_part*.npz di {DATA_DIR}")
    loaded = [np.load(p) for p in parts]
    return {k: np.concatenate([z[k] for z in loaded]) for k in loaded[0].files}


def load_klasifikasi_train():
    arr = _load_parts("klasifikasi_train")
    meta = pd.read_csv(DATA_DIR / "klasifikasi_train_meta.csv")
    return arr["gambar"], arr["sensor"], meta


def load_klasifikasi_test():
    z = np.load(DATA_DIR / "klasifikasi_test.npz")
    meta = pd.read_csv(DATA_DIR / "klasifikasi_test_meta.csv")
    return z["gambar"], z["sensor"], meta


def load_rul():
    return pd.read_csv(DATA_DIR / "rul_train.csv.gz"), pd.read_csv(DATA_DIR / "rul_test.csv.gz")


def load_clustering():
    arr = _load_parts("clustering")
    meta = pd.read_csv(DATA_DIR / "clustering_meta.csv")
    return arr["gambar"], arr["spektrum"], meta

# DL

Data UTS Deep Learning. Penjelasan lengkap tiap kolom ada di [`data/kamus_data.md`](data/kamus_data.md).

## Isi folder `data/`

| Tugas | File | Isi |
| --- | --- | --- |
| 1. Klasifikasi | `klasifikasi_train_part1..3.npz`, `klasifikasi_train_meta.csv` | 48.000 sampel latih: `gambar` (64×64), `sensor` (3×128), label `kelas` |
| | `klasifikasi_test.npz`, `klasifikasi_test_meta.csv` | 16.000 sampel uji (tanpa label) |
| 2. RUL | `rul_train.csv.gz`, `rul_test.csv.gz` | Log per siklus mesin press, 3 setelan + 21 sensor |
| 3. Clustering | `clustering_part1..2.npz`, `clustering_meta.csv` | 36.000 sampel: `gambar` (64×64), `spektrum` (128) |

`klasifikasi_train.npz` dan `clustering.npz` asli lebih dari 100 MB (batas file GitHub), jadi dipecah
per baris. Isinya identik dengan file asli setelah digabung urut part1, part2, dst.

## Cara memuat

```python
from data.load_data import load_klasifikasi_train, load_klasifikasi_test, load_rul, load_clustering

gambar, sensor, meta = load_klasifikasi_train()   # (48000,64,64), (48000,3,128), DataFrame
rul_train, rul_test = load_rul()
gambar_c, spektrum, meta_c = load_clustering()
```

File zip asli juga ada di [Release v2.0](https://github.com/Wannn-afk/DL/releases/tag/v2.0).

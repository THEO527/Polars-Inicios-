import polars as pl
print(pl.__version__)

Almacen = pl.DataFrame({
    "producto": ["manzana", "platano", "manzana", "naranja"],
    "ventas": [10, 20, 15, 5],
    "fecha": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"]
})
print(Almacen)
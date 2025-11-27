#!/usr/bin/env python3
"""
VERSIÓN CORREGIDA — Funciona con TSV y threshold numérico

Objetivo del programa:
1. Leer un archivo TSV con columnas: gene, expression
2. Leer un threshold desde la línea de comandos
3. Filtrar los genes cuya expresión sea >= threshold
4. Imprimir la lista de genes filtrados
"""
import argparse
import pandas as pd # type: ignore


def load_expression_table(path):
    """
    Carga un archivo TSV con columnas 'gene' y 'expression'.
    """
    # Separador correcto para TSV
    df = pd.read_csv(path, sep="\t")

    # Validación básica de columnas
    if "gene" not in df.columns or "expression" not in df.columns:
        raise ValueError("El archivo debe tener columnas 'gene' y 'expression'.")

    # Convertir expresión a numérico, valores inválidos se convierten en NaN
    df["expression"] = pd.to_numeric(df["expression"], errors="coerce")

    # Eliminar filas con NaN en expression
    df = df.dropna(subset=["expression"])

    return df


def filter_gene(df, threshold):
    """
    Filtra genes con expresión mayor o igual al threshold.
    """
    filtered = df[df["expression"] >= threshold]  # operador >= correcto

    # Ordenar alfabéticamente por gene
    filtered = filtered.sort_values("gene")

    return filtered


def build_parser():
    """
    Construye el parser de argumentos.
    """
    parser = argparse.ArgumentParser(
        description="Filtra genes por expresión usando un archivo TSV y pandas."
    )

    parser.add_argument(
        "file",
        help="Archivo TSV con columnas 'gene' y 'expression'."
    )

    # Threshold numérico y default como float
    parser.add_argument(
        "-t",
        "--threshold",
        type=float,
        default=0.0,  # corregido a float
        help="Umbral mínimo de expresión (ej. 10.5)."
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    df = load_expression_table(args.file)

    threshold = args.threshold

    filtered = filter_gene(df, threshold)

    if filtered.empty:
        print("No se encontraron genes por encima del threshold.")
        return

    print("Genes filtrados:")
    for gene in filtered["gene"].tolist():
        print(gene)


if __name__ == "__main__":
    main()

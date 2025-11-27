#!/usr/bin/env python3
"""
Contador de k-mers.

Requerimientos:
- Validar que la secuencia solo tenga A,T,C,G.
- Leer k desde una opción -k / --kmer_size.
- Imprimir k-mers y conteos.
"""
import argparse
import sys

def validate_sequence(seq):
    """Valida que la secuencia solo contenga A, T, C y G."""
    seq = seq.upper()
    valid = {"A", "T", "C", "G"}

    for base in seq:
        if base not in valid:
            print(f"Error: carácter inválido en la secuencia: '{base}'")
            sys.exit(1)

    return seq


def count_kmers(seq, k):
    """Cuenta todos los k-mers contiguos de longitud k."""
    if k <= 0:
        print("Error: k debe ser mayor que cero.")
        sys.exit(1)

    if k > len(seq):
        print("Error: k no puede ser mayor que la longitud de la secuencia.")
        sys.exit(1)

    counts = {}

    for i in range(len(seq) - k + 1):
        kmer = seq[i : i + k]
        counts[kmer] = counts.get(kmer, 0) + 1

    return counts


def main():
    parser = argparse.ArgumentParser(description="Contador de k-mers.")
    parser.add_argument("sequence", help="Secuencia de ADN (solo A,T,C,G).")
    parser.add_argument("-k", "--kmer_size", type=int, required=True,
                        help="Tamaño del k-mer.")
    args = parser.parse_args()

    seq = validate_sequence(args.sequence)
    k = args.kmer_size

    kmers = count_kmers(seq, k)

    for kmer, count in kmers.items():
        print(f"{kmer}\t{count}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import argparse
import os
import sys

def validar_archivo(ruta):
    """Verifica que el archivo exista."""
    if not os.path.exists(ruta):
        print(f"Error: el archivo no existe: {ruta}")
        sys.exit(1)


def leer_fasta(ruta):
    """Lee el archivo FASTA completo y regresa su contenido."""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print("Error al leer el archivo:", e)
        sys.exit(1)


def extraer_secuencia(contenido):
    """Extrae encabezado y secuencia del contenido FASTA."""
    if ">" not in contenido:
        print("Error: El archivo no parece estar en formato FASTA.")
        sys.exit(1)

    partes = contenido.split(">")

    if len(partes) < 2:
        print("Error: FASTA vacío o sin secuencia válida.")
        sys.exit(1)

    bloque = partes[1].strip().split("\n")
    header = bloque[0]
    sec = "".join(bloque[1:]).strip().upper()

    if len(sec) == 0:
        print("Error: la secuencia está vacía.")
        sys.exit(1)

    return header, sec


def limpiar_secuencia(sec):
    """Elimina caracteres no válidos y reporta avisos."""
    bases_validas = {"A", "T", "G", "C"}
    seq_limpia = ""

    for base in sec:
        if base in bases_validas:
            seq_limpia += base
        else:
            print(f"Aviso: caracter inválido '{base}' ignorado en la secuencia")

    if len(seq_limpia) == 0:
        print("Error: la secuencia no contiene bases válidas (A,T,G,C).")
        sys.exit(1)

    return seq_limpia


def contar_frecuencias(seq):
    """Regresa un diccionario con las frecuencias de ATGC."""
    return {
        "A": seq.count("A"),
        "T": seq.count("T"),
        "G": seq.count("G"),
        "C": seq.count("C"),
    }


def imprimir_resultados(header, seq, frec):
    """Imprime los resultados exactamente igual al programa original."""
    total = len(seq)

    print("Encabezado:", header)
    print("Longitud secuencia válida:", total)
    print("Frecuencias:")
    for base in ["A", "T", "G", "C"]:
        valor = frec[base]
        porcentaje = round((valor / total) * 100, 2)
        print(f"{base}: {valor} ({porcentaje}%)")


def main():
    parser = argparse.ArgumentParser(
        description="Calcula la frecuencia de A, T, G y C de un archivo FASTA con una sola secuencia."
    )
    parser.add_argument("fasta", help="Archivo FASTA que contiene una sola secuencia.")
    args = parser.parse_args()

    validar_archivo(args.fasta)
    contenido = leer_fasta(args.fasta)
    header, sec = extraer_secuencia(contenido)
    seq_limpia = limpiar_secuencia(sec)
    frecuencias = contar_frecuencias(seq_limpia)
    imprimir_resultados(header, seq_limpia, frecuencias)


if __name__ == "__main__":
    main()

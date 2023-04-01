def transcribe_nucleotide(nucleotide):
    if nucleotide == "G":
        return "C"
    if nucleotide == "C":
        return "G"
    if nucleotide == "T":
        return "A"
    if nucleotide == "A":
        return "U"
    return ""


def to_rna(dna_strand):
    return "".join(transcribe_nucleotide(nucleotide) for nucleotide in dna_strand)

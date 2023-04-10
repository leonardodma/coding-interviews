def swap_odd_even_bits(x: int) -> int:
    return ((x & 0xAAAAAAAA) >> 1) | ((x & 0x55555555) << 1)

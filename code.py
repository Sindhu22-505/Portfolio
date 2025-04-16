import heapq
import sys

# Node structure for the Huffman Tree
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq  # Min-Heap based on frequency

# Build the frequency dictionary
def build_frequency_dict(text):
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict

# Build Huffman Tree
def build_huffman_tree(freq_dict):
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)  # Min-Heap (Priority Queue)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]  # Root of Huffman Tree

# Generate Huffman Codes
def generate_codes(root, code="", huffman_codes={}):
    if root is None:
        return

    if root.char is not None:
        huffman_codes[root.char] = code

    generate_codes(root.left, code + "0", huffman_codes)
    generate_codes(root.right, code + "1", huffman_codes)

    return huffman_codes

# Encode the text
def encode_text(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)

# Decode the binary string using Huffman Tree
def decode_text(encoded_text, root):
    decoded_text = ""
    current = root

    for bit in encoded_text:
        current = current.left if bit == '0' else current.right
        if current.char is not None:
            decoded_text += current.char
            current = root  # Reset to root

    return decoded_text

# Compression function
def compress(text):
    freq_dict = build_frequency_dict(text)
    huffman_tree = build_huffman_tree(freq_dict)
    huffman_codes = generate_codes(huffman_tree)

    encoded_text = encode_text(text, huffman_codes)
    return huffman_tree, encoded_text, huffman_codes

# Driver function
if __name__ == "__main__":
    text = input("Enter text to compress: ")
    
    # Compression
    huffman_tree, compressed_text, huffman_codes = compress(text)

    # Print Huffman Codes
    print("\nHuffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")

    print("\nCompressed Binary Text:", compressed_text)

    # Decompression
    decompressed_text = decode_text(compressed_text, huffman_tree)
    print("\nDecompressed Text:", decompressed_text)

    # Statistics
    original_size = len(text) * 8  # Each char takes 8 bits
    compressed_size = len(compressed_text)
    compression_ratio = compressed_size / original_size

    print("\nOriginal Size:", original_size, "bits")
    print("Compressed Size:", compressed_size, "bits")
    print("Compression Ratio:", round(compression_ratio, 2))

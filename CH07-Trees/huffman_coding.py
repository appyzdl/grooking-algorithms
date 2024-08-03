import heapq
from collections import defaultdict


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_freq_dict(text):
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    return freq


def build_huffman_tree(freq):
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        internal = Node(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        heapq.heappush(heap, internal)

    return heap[0]


def generate_codes(root):
    def traverse(node, code):
        if node.char:
            codes[node.char] = code
            return
        traverse(node.left, code + '0')
        traverse(node.right, code + '1')

    codes = {}
    traverse(root, '')
    return codes


def huffman_encode(text):
    frequency = build_freq_dict(text)
    root = build_huffman_tree(frequency)
    codes = generate_codes(root)
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, root


def huffman_decode(encoded_text, root):
    decoded_text = []
    current = root
    for bit in encoded_text:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        if current.char:
            decoded_text.append(current.char)
            current = root
    return ''.join(decoded_text)


# Example usage
text = "this is an example for huffman encoding"
encoded, tree = huffman_encode(text)
decoded = huffman_decode(encoded, tree)

print(f"Original text: {text}")
print(f"Encoded text: {encoded}")
print(f"Decoded text: {decoded}")
print(f"Compression ratio: {len(encoded) / (len(text) * 8):.2f}")

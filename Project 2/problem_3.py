import sys
import heapq
from collections import Counter


class HuffmanNode:

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __eq__(self, other):
        return self.freq == other.freq

    def __ne__(self, other):
        return self.freq != other.freq

    def __str__(self):
        return "Node( {} : {} )".format(self.char, self.freq)


class HuffmanTree:

    def __init__(self, data):
        # doesn't make sense if we want to encode 0 or 1 character
        if len(data) < 2:
            raise ValueError('Text must be more than 1 character')
        freq_table = Counter(data)

        # in case data only contain 1 char repeatedly such as 'aaaaaaaaaaaaaaaaaa'
        if len(freq_table) == 1:
            self.root = HuffmanNode(data[0], freq_table[data[0]])
            self._encode_dict = {data[0]: "0"}
            self._decode_dict = {"0": data[0]}
            return

            # normal case
        nodes = [HuffmanNode(i, freq_table[i]) for i in freq_table]
        heapq.heapify(nodes)

        while len(nodes) > 1:
            node1 = heapq.heappop(nodes)
            node2 = heapq.heappop(nodes)
            combine_node = HuffmanNode(None, node1.freq + node2.freq)
            combine_node.left = node1
            combine_node.right = node2  # node1 <= node2 always true
            heapq.heappush(nodes, combine_node)

        self.root = nodes[0]
        self._encode_dict = None
        self._decode_dict = None

    def get_encode_dict(self):
        if self._encode_dict is not None:
            return self._encode_dict

        self._encode_dict = dict()
        HuffmanTree._make_encode_dict(self.root, "", self._encode_dict)
        return self._encode_dict

    def get_decode_dict(self):
        if self._decode_dict is not None:
            return self._decode_dict

        self._decode_dict = dict()
        HuffmanTree._make_decode_dict(self.root, "", self._decode_dict)
        return self._decode_dict

    @staticmethod
    def _make_encode_dict(node, prefix, encode_dict):
        if node.left is None and node.right is None:
            encode_dict[node.char] = prefix
        else:
            HuffmanTree._make_encode_dict(node.left, prefix + "1", encode_dict)
            HuffmanTree._make_encode_dict(node.right, prefix + "0", encode_dict)

    @staticmethod
    def _make_decode_dict(node, prefix, decode_dict):
        if node.left is None and node.right is None:
            decode_dict[prefix] = node.char
        else:
            HuffmanTree._make_decode_dict(node.left, prefix + "1", decode_dict)
            HuffmanTree._make_decode_dict(node.right, prefix + "0", decode_dict)


def huffman_encoding(data):
    huffman_tree = HuffmanTree(data)
    encode_table = huffman_tree.get_encode_dict()
    encode_text = ''
    for i in data:
        encode_text += encode_table[i]
    return encode_text, huffman_tree


def huffman_decoding(data, tree):
    decode_text = ''
    decode_table = tree.get_decode_dict()
    temp = ''
    for s in data:
        temp += s
        if temp in decode_table:
            decode_text += decode_table[temp]
            temp = ''

    return decode_text


if __name__ == "__main__":
    # Test 0: Udacity Test Case
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))  # 45
    print("The content of the data is: {}\n".format(a_great_sentence))  # The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))  # 22
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # 0001000000010101110011001111010011010010010100000010101111000110011110

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))  # 45
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The bird is the word

    # Test 1:
    print("Test 1")
    test1_sentence = "mississippi"
    print("The size of the data is: {}\n".format(sys.getsizeof(test1_sentence)))  # 36

    print("The content of the data is: {}\n".format(test1_sentence))  # mississippi
    encoded_data, tree = huffman_encoding(test1_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))  # 16
    print("The content of the encoded data is: {}\n".format(encoded_data))  # 011100001000010100101

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))  # 36
    print("The content of the encoded data is: {}\n".format(decoded_data))  # mississippi

    # Test 2:
    print("Test 2")
    test2_sentence = "111"
    print("The size of the data is: {}\n".format(sys.getsizeof(test2_sentence)))  # 28

    print("The content of the data is: {}\n".format(test2_sentence))  # 111
    encoded_data, tree = huffman_encoding(test2_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))  # 12
    print("The content of the encoded data is: {}\n".format(encoded_data))  # 000

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))  # 28
    print("The content of the encoded data is: {}\n".format(decoded_data))  # 111

    # Test 3:
    print("Test 3")
    test3_sentence = ""
    encoded_data, tree = huffman_encoding(test3_sentence)  # raise ValueError Text must be more than 1 character

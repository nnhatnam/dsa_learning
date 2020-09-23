import sys
import heapq
from collections import Counter


class PriorityQueue:

    def __init__(self, arr):
        self.min_heap = heapq.heapify(arr)
        pass


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
        freq_table = Counter(data)
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
        HuffmanTree._make_decode_dict(self.root, "",  self._decode_dict)
        return  self._decode_dict

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
    codes = {}

    a_great_sentence = "The bird is the word"
    tree = HuffmanTree(a_great_sentence)
    print(tree.get_encode_dict())

    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))
    #
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print(encoded_data)
    print(tree)


    #
    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))
    #
    decoded_data = huffman_decoding(encoded_data, tree)
    print(decoded_data)
    #
    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))

class StoreNode:
    """
    每个Node存储了一个文档的相关信息
    """

    def __init__(self, doc_id, positions):
        self.doc_id = doc_id  # 文档唯一标识符
        self.positions = positions  # 是一个列表，存储该词汇在对应文档中出现的位置
        self.next = None  # 指针，指向该词汇下一个文档，没有为None
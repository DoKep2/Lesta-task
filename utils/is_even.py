class SegmentTree:

    def __init__(self, nums):
        self.size = len(nums)
        self.tree = [0] * (4 * self.size)
        self.build(nums, 0, 0, self.size - 1)

    def build(self, nums, idx, left, right):
        if left == right:
            self.tree[idx] = nums[left] % 2 == 0
        else:
            mid = (left + right) // 2
            self.build(nums, 2 * idx + 1, left, mid)
            self.build(nums, 2 * idx + 2, mid + 1, right)
            self.tree[idx] = self.tree[2 * idx + 1] + self.tree[2 * idx + 2]

    def query(self, idx, left, right, query_left, query_right):
        if query_right < left or query_left > right:
            return 0
        elif query_left <= left and query_right >= right:
            return self.tree[idx]
        else:
            mid = (left + right) // 2
            return self.query(2 * idx + 1, left, mid, query_left, query_right) + \
                self.query(2 * idx + 2, mid + 1, right, query_left, query_right)


def is_even(value):
    nums = [value] * 1
    seg_tree = SegmentTree(nums)
    return seg_tree.query(0, 0, seg_tree.size - 1, 0, 0) > 0


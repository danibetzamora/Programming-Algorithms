
def solve(items):
    """
    Sort the given list of items in ascending order
    """

    def merge(left, mid, right):
        a = items[left:mid]
        b = items[mid:right+1]
        i = 0
        j = 0

        for k in range(left, right + 1):
            if i >= len(a):
                items[k] = b[j]
                j += 1
            elif j >= len(b):
                items[k] = a[i]
                i += 1
            elif a[i] < b[j]:
                items[k] = a[i]
                i += 1
            else:
                items[k] = b[j]
                j += 1

        return
    
    def merge_sort(left, right):
        if left < right:
            mid = int((left+right)/2)
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            merge(left, mid + 1, right)

        return

    merge_sort(0, len(items)-1)
    return

# # Given an array arr[], where arr[i] represents the number of pages in the i-th book, and an integer k denoting the total number of students, allocate all books to the students such that:

# # Each student gets at least one book.
# # Books are allocated in a contiguous sequence.
# # The maximum number of pages assigned to any student is minimized.
# # If it is not possible to allocate all books among k students under these conditions, return -1.

# # Output the maximum number of pages allocated

# Input: arr[] = [12, 34, 67, 90], k = 2
# Output: 113
# Explanation: Books can be distributed in following ways:

# [12] and [34, 67, 90] - The maximum pages assigned to a student is  34 + 67 + 90 = 191.
# [12, 34] and [67, 90] - The maximum pages assigned to a student is 67 + 90 = 157.
# [12, 34, 67] and [90] - The maximum pages assigned to a student is 12 + 34 + 67 = 113.
# The third combination has the minimum pages assigned to a student which is 113.

def can_allocate(arr, k, limit):

    students = 1
    pages = 0

    for book in arr:

        if pages + book <= limit:
            pages += book
        else:
            students += 1
            pages = book

    return students <= k
def allocateBooks(arr, k):

    if k > len(arr):
        return -1

    low = max(arr)
    high = sum(arr)

    answer = high

    while low <= high:

        mid = (low + high) // 2

        if can_allocate(arr, k, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer
        

arr = [12, 34, 67, 90]
k =2
print(allocateBooks(arr,k))
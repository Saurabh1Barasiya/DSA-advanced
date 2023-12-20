# What is Book Allocation Problem.

# Given an integer array called ‘pages’, where each ‘pages[i]’ represents the number of pages in the ‘i-th’ book, and a total of ‘m’ students, the objective is to allocate all the books among the students.
# Allocate books in a way such that:

# Each student gets at least one book.
# Each book should be allocated to a student.
# Book allocation should be in a contiguous manner.

# The task is to distribute the books among ‘m’ students in such a way that the maximum number of pages assigned to any student is minimized.


def is_solution_possible(arr,total_pages,total_students,mid):
    student_count = 1
    pages = 0
    for i in range(total_pages):
        if pages + arr[i] <= mid:
            pages += arr[i]
        else:
            student_count += 1
            if student_count > total_students or arr[i] > mid:
                return False
            pages = 0
            pages += arr[i]
    return True

def find_pages(arr,total_pages,total_students):
    if total_students > total_pages:
        return -1
        # agar student hi jyadha h total pages se to 
        # book hi allocate nahi kar payege.
    
        # allocate karne ki condition ye h ki har student ko 
        # 1 - 1 book milni chahiye.
    
    # make search space.
    start = 0
    end = sum(arr)

    ans = 0

    while start <= end:
        mid = start + (end - start) // 2
        if is_solution_possible(arr,total_pages,total_students,mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans

if __name__ == "__main__":
    N = 4
    arr = [12,34,67,90]
    # arr = [10,20,30,40]
    M = 2 # total student
    result = find_pages(arr,N,M)
    if result != -1:
        print(f"Answer is {result}")
    else:
        print("Book allocation nahi ho sakta hai.")
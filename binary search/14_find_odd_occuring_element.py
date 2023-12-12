# find odd occuring element in a array.
 
# 👀👀👀👀 basiclly we have a array = [1,1,2,2,3,3,5,5,3,500,500,2,2,6,6].
 
# har 1 pair me 2 hi element hoge like (1,1) (2,2) (3,3) (5,5) (500,500) (2,2) (6,6)
 
# hamare paas array me pair h . ye pair kabhi bhi adjacent nahi hoge.
 
# means --> (2,2) (2,2)  kabhi bhi shat me nahi hoge .
 
# to apko odd occuring element ko find karna h.
 
'''
    element   ----> occured time.
        1     ---->  2,
        2     ---->  4,
        3     ---->  3,
        5     ---->  2,
        500     ---->  2,
        6     ---->  2,
 
    but,
        3     ---->  3,
 
so yaha 3 , 3times (odd times) occur hua h , uska matlab yahi answer h.
'''
 
 
# 👀👀👀👀👀
 
# ab array ko obserb kero ko (Attention) dhyan se samjho.
 
                                      #ans
# element =>  [1 ,1, 2, 2, 3, 3, 5, 5, 3, 500, 500, 2, 2, 6, 6].
#index        0   1  2  3  4  5  6  7  8  9    10  11 12 13 14.
# index =>    e   o  e  o  e  o  e  o  e  o     e   o  e  o  e.
 
# 👀👀👀 answer hamesha even index par hoga.
 
# to ab 1 cheecj par focus kero jo  hamara answer h that is index no. 8 element 3
 
# iske left me sare pair even index se start ho rahe h and odd index par end ho rahe h.
# and answer ke right ke sare pair odd index se start ho rahe h and even index par end ho rahe h.
 
# bas isi condition ke base par hamko ye question ko solve karna h .
 
 
# mid even hua to kya karna h and mid odd hua to kya karna h bas ye pata lagao.
 
# and answer hamesa even index par hi milega
 
# aao code likhte h.
 
def find_odd_occruing(arr):
    start = 0
    end = len(arr) - 1
 
    while start <= end:
        mid = start + (end - start ) // 2
 
        # if array me single element hua to start ya end jisko return karna h, usko return kar dena  .
        # kyoki dono same hi index ko point karege.
        if start == end:
            return start
       
        if mid % 2 == 0:
            # Even case.
            if mid + 1 <= end and  arr[mid] == arr[mid+1]:
                # iska matlab me answer ke left side par hu.
                # to right side par jao.
 
                start = mid + 2  # (mid + 2) kyo , because hamne mid + 1 ko check kar liya h and vo answer to hoga hi nahi.
            else:
                # to ab samjho .
                # agar mera mid index 8 par h. that is even index.
                # to ye possibility h ki mid ki mera andwer ho sakta h.
                # ya answer peeche kahi hoga.
 
                end = mid
                # agar end = mid - 1 kar deta to mera answer lost ho jata
                # kabhi answer hi nahi milta.
        else:
            # Odd case.
            # ab samjho ki mid kisi odd index par h or uske peeche wala element (mid-1) dono same h.
            # iska matlab ye (even , odd) index h . starting even , end odd.
            # iska matlb ye hua ki ham abhi left side par h answer ke. to right par jao.
 
            if mid-1 >= start and arr[mid] == arr[mid-1]:
                start = mid + 1
                # ab mid + 2 kyo nahi kiya kyoki hamne mid-1 element ko check kiya h .
            else:
                # to bas just peeche chale jao.
                end = mid - 1
 
                # answer hamesh even index par hi milega. if app mid - 2 kar doge to fir se odd index par chale jaoge, to kabhi app answer tak reach hi nahi kar paoge.

                # yaha yaha mid - 2 kar doge to answer ke peeche chale jaoge. or kabhi answer nahi mil payega.
                # isiliye mid -1
 
                # 1 baar odd case ko lekar dry run kar lena . sab samaj me aa jayega.
 
 
if __name__ == "__main__":
    arr = [1,1,2,2,3,3,5,5,3,3,5,500,500,2,2,6,6]
    result = find_odd_occruing(arr)
    if result != -1:
        print(f"Odd occuring element {arr[result]} found at index no. {result} in the array.")
    else:
        print("Odd occuring element not found in the array.")
 
 
# Time complexity --> O(log n).
# Space complexity -- O(1).
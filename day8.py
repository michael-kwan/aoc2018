#day 8
#star 15

with open('day8.txt', 'r') as f:
    nums = [line.strip().split() for line in f.readlines()][0]

nums = [int(x) for x in nums]
hashes = []


#returns a tuple, the firs tbeing the trivial total (Part 1) the second being the carried value between nodes (Part 2),
#and the shortening of the list as more and more nodes are being processed. Thus, the answer two the two parts only needs
#the help of the first two elements of the the tuple.
def parse(nums):
    childs, mdnum = nums[:2]
    nums = nums[2:]
    hashes = []
    sums = 0

    for i in range(childs):
        total, hashs, nums = parse(nums)
        sums += total
        hashes.append(hashs)

    sums += sum(nums[:mdnum])

    if childs == 0:
        return (sums, sum(nums[:mdnum]), nums[mdnum:])
    else:
        return (
                sums,
                sum(hashes[k - 1] for k in nums[:mdnum] if k > 0 and k <= len(hashes)),
                nums[mdnum:]
                )

a = parse(nums)
print "Part 1:", a[0]
print "Part 2:", a[1]


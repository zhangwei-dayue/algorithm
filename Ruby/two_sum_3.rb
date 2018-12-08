# Time complexity: O(n);
# Space complexity: O(n);
def two_sum(nums, target)
  hash = {}
  nums.each_with_index do |num, index|
    return [hash[target - num], index] if hash.has_key?(target - num)
    hash[num] = index
  end

  raise ArgumentError, 'No two sum solution'
end

nums = [2, 7, 11, 15]
target = 9

puts two_sum(nums, target)
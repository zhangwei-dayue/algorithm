# Time complexity: O(n2);
# Space complexity: O(1);
def two_sum(nums, target)
  for i in 0...nums.size
    for j in (i + 1)...nums.size
      return [i, j] if nums[i] + nums[j] == target
    end
  end

  raise ArgumentError, 'No two sum solution'
end

nums = [2, 7, 11, 15]
target = 9

puts two_sum(nums, target)
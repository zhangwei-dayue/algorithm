# Time complexity: O(n);
# Space complexity: O(n);
def is_valid(s)
  arr = []
  match_hash = {')': '(', ']': '[', '}': '{'}

  str_arr = s.split('')
  str_arr.each do |char|
    if !match_hash.has_key?(char.to_sym)
      arr.push(char)
    elsif match_hash[char.to_sym] != arr.pop
      return false
    end
  end

  return arr.empty?
end

puts is_valid('{{{((()))}}}[')
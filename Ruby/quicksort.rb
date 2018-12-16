def quicksort(array)
  if array.size < 2
    return array
  else
    pivot = array[0]
    less = []
    greater = []
    array.each {|arr| less << arr if arr < pivot}
    array.each {|arr| greater << arr if arr > pivot}

    return quicksort(less) + [pivot] + quicksort(greater)
  end
end

puts quicksort([10,1,2,7,9,4])
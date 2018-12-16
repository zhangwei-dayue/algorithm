class Array
  def bubble_sort!
    for i in 0...(self.size - 1)
      for j in 0...(self.size - i - 1)
        self[j], self[j + 1] = self[j + 1], self[j] if self[j] > self[j + 1]
      end
    end
    return self
  end
end


puts [100,2,324,1,6,32].bubble_sort!
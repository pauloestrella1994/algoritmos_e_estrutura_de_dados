# Given two strings, s1 and s2, check
# if they're anagrams. Two string are anagrams if
# they're made of the sma characteres with the same
# frequencies

# Example
# input
# s1 = 'danger'
# s2 = 'garden'
# output: true

def are_anagrams(s1, s2)
  if s1.size != s2.size
    return false
  end

  freq1 = Hash.new
  freq2 = Hash.new

  s1.each_char do |chr|
    if freq1.keys.include?(chr)
      freq1[chr] += 1
    else
      freq1[chr] = 1
    end
  end

  s2.each_char do |chr2|
    if freq2.keys.include?(chr2)
      freq2[chr2] += 1
    else
      freq2[chr2] = 1
    end
  end

  freq1.each_key do |freq1_key|
    if freq2.include?(freq1_key) && freq2[:freq1_key] == freq1[:freq1_key]
      return true
    else
      return false
    end
  end
end

if __FILE__ == $0
  puts 'Check if two strings are anagrams'
  puts 'Write first string'
  s1 = gets.chomp
  puts 'Write second string'
  s2 = gets.chomp
  puts are_anagrams(s1, s2)
end
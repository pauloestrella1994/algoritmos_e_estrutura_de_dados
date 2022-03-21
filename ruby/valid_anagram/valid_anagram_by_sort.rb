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
  s1_sorted = s1.chars.sort(&:casecmp).join
  s2_sorted = s2.chars.sort(&:casecmp).join

  if s1_sorted == s2_sorted
    return true
  end
  false
end

if __FILE__ == $0
  puts 'Check if two strings are anagrams'
  puts 'Write first string'
  s1 = gets.chomp
  puts 'Write second string'
  s2 = gets.chomp
  puts are_anagrams(s1, s2)
end
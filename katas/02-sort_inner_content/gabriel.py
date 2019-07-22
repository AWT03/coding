def sort_the_inner_content(words):
  new_string = ""
  for word in words.split():
      if len(word) != 1:
          re_order = list(word[1:-1])
          re_order.sort(reverse=True)
          new_word = word[0] + ''.join(re_order) + word[-1]
      else:
          new_word = word
      new_string += new_word + " "
  return new_string[:-1]


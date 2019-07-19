function sortTheInnerContent(words)
{
  let words_array = [];
  for (let i=0; i<words.split(' ').length; i++){
    let word = words.split(' ')[i]
    if (word.length!=1){
        words_array.push(word[0] + 
        word.substring(1, word.length-1).split('').sort().reverse().join('') + 
        word[word.length-1]);
    } else {
      words_array.push(word);
    }
  }
  return words_array.join(' ');
}


function isPalindrome(word)
{
  x = word.toLowerCase();
  y = ''
  // Please write your code here.
  for (var i = x.length - 1; i >= 0; i--) {
      y += x[i];
  }

  if (x == y){
    return true;
  } else {
    return false;
  }
}

var w = ['oppO', 'samsung']

for (i = 0; i < w.length; i++){
    console.log(w[i] + ' : ' + isPalindrome(w[i]))
}
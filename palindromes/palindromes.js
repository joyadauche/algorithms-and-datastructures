function isPalindrome(string){
    leftIndex = 0;
    rightIndex = string.length - 1;
    while(leftIndex < rightIndex){
        if(string[leftIndex] != string[rightIndex]) return false;
        leftIndex += 1;
        rightIndex -= 1;
    }
    return true;
}

console.log(isPalindrome("aba"));
console.log(isPalindrome("ojo"))
console.log(isPalindrome("bless"));
console.log(isPalindrome("a"));
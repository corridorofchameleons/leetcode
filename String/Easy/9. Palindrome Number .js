var isPalindrome = function(x) {
    if (x < 0) { return False }
    let num_digs = parseInt(Math.log10(x) + 1)
    new_num = 0
    for i in range(1, num_digs + 1):
        new_num += (((x % 10**i) / 10**(i - 1)) * 10**(num_digs - i))
    if (new_num === x) {return True}
    else {return False}
    }
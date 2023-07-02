function longest(strs) {
    lcp = ""
outer_loop:
    for (i = 0; i < strs[0].length; i++) {
        let a = strs[0][i]
inner_loop:
        for (st in strs) {
            if (strs[st][i] !== a) {
                break outer_loop;
            }
        }
        lcp += a
    } return lcp
}
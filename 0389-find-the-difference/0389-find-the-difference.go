func findTheDifference(s string, t string) byte {
    var bs, bt byte

    for i := 0; i < len(s); i++ {
        bs += s[i]
    }

    for i := 0; i < len(t); i++ {
        bt += t[i]
    }

    return bt-bs
}
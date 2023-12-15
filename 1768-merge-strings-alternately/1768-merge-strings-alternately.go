func mergeAlternately(word1 string, word2 string) string {
    word1Len := len(word1)
    word2Len := len(word2)

    var result string

    if (word1Len < word2Len){
        for i := 0; i < word1Len; i++ {
            result += string(word1[i])
            result += string(word2[i])
        }
        for i := word1Len; i < word2Len; i++ {
            result += string(word2[i])
        }
    } else if (word1Len > word2Len) {
        for i := 0; i < word2Len; i++ {
            result += string(word1[i])
            result += string(word2[i])
        }
        for i := word2Len; i < word1Len; i++ {
            result += string(word1[i])
        }
    } else {
        for i := 0; i < word2Len; i++ {
            result += string(word1[i])
            result += string(word2[i])
        }
    }

    return result
}
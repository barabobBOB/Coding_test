func strStr(haystack string, needle string) int {
    var result = -1

    var count int
    for i := 0; i < len(haystack); i++ {
        count = 0
        for j := 0; j < len(needle); j++ {
            if i+j >= len(haystack) {
                return result
            } else if string(haystack[i + j]) == string(needle[j]){
                count++
            }
            if count == len(needle) {
                result = i
                break
            }
        }
        if result != -1 {
            break
        }
    }

    return result
}
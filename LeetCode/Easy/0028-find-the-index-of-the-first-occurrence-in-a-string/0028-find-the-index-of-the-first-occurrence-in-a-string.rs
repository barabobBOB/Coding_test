impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        let mut result = -1;

        for i in 0..haystack.len() {
            let mut count = 0;
            for (j, c) in needle.chars().enumerate() {
                if i + j >= haystack.len() {
                    return result;
                } else if haystack.chars().nth(i + j).unwrap() == c {
                    count += 1;
                }
                if count == needle.len() {
                    result = i as i32;
                    break;
                }
            }
            if result != -1 {
                break;
            }
        }

        result
    }
}


package main

func longestCommonPrefix(strs []string) string {
	prefix := strs[0]
	for i := 1; i < len(strs); i++ {
		if len(strs[i]) < len(prefix) {
			prefix = strs[i]
		}
	}
	for i := 0; i < len(strs); i++ {
		for j := 0; j < len(prefix); j++ {
			if prefix[j] != strs[i][j] {
				prefix = prefix[:j]
				break
			}
		}
	}
	return prefix
}

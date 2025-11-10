class Solution {
public:
    vector < string > fullJustify(vector < string > & words, int maxWidth) {
    vector < string > result;
    int i = 0, n = words.size();

    while (i < n) {
            int lineLen = words[i].size();
            int j = i + 1;

            while (j < n & & lineLen + 1 + words[j].size() <= maxWidth) {
                    lineLen += 1 + words[j].size();
                    j++;
                    }

            int numWords = j - i;
            int totalChars = 0;
            for (int k = i; k < j; ++k) totalChars += words[k].size();
            string line;
            int spaces = maxWidth - totalChars;

            if (j == n | | numWords == 1) {
                for (int k = i; k < j; ++k) {
                    line += words[k];
                    if (k < j - 1) line += ' ';
                    }
                line += string(maxWidth - line.size(), ' ');
                } else {
                        int avgSpace = spaces / (numWords - 1);
                        int extra = spaces % (numWords - 1);
                        for (int k = i; k < j; ++k) {
                                line += words[k];
                                if (k < j - 1) {
                                    int spaceCount = avgSpace + (k - i < extra ? 1: 0);
                                    line += string(spaceCount, ' ');
                                }
                        }
                    }

            result.push_back(line);
            i = j;
        }

        return result;
    }
};
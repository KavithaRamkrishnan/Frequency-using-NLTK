

import nltk
from nltk.corpus import webtext
from nltk.probability import FreqDist
 
nltk.download('webtext')
wt_words = webtext.words('/Users/ramakrishnan_k/Desktop/sales_usecase/test.txt')
visualize_data = nltk.FreqDist(wt_words)
 
# Let's take the specific words only if their frequency is greater than 3.
filtering_words = dict([(m, n) for m, n in visualize_data.items() if len(m) > 3])
 
for key in sorted(filtering_words):
    print("%s: %s" % (key, filtering_words[key]))
 
visualize_data = nltk.FreqDist(filtering_words)
 
visualize_data.plot(20, cumulative=False)
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
document = "To do this, we’ll use Google Chrome’s excellent Inspect tool. Open the news article we chose in a new tab, right-click on the page and choose Inspect from the drop-down menu. That will bring up the Inspect tool which looks like thisNatural language generation (NLG) is the natural language processing task of generating natural language from a machine representation system such as a knowledge base or a logical form. Psycholinguists prefer the term language production when such formal representations are interpreted as models for mental representations."

# object of automatic summarization
n_gram_auto_abstractor = AutoAbstractor()

#Set tokenizer
# Object of automatic summarization.
auto_abstractor = AutoAbstractor()

# Set tokenizer.
auto_abstractor.tokenizable_doc = SimpleTokenizer()

# Set delimiter for making a list of sentence.
auto_abstractor.delimiter_list = [".", "\n"]

# Object of abstracting and filtering document.
abstractable_doc = TopNRankAbstractor()

# Summarize document.
result_dict = auto_abstractor.summarize(document, abstractable_doc)

# Output result.
for sentence in result_dict["summarize_result"]:
    print(sentence)


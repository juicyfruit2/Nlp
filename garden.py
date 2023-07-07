# imported spacy 
import spacy 

nlp = spacy.load("en_core_web_sm")


# Use 2 Garden Path sentences and added three more to the list 
garden_path_Sentences = [("The raft floated down the river bank."), 
                       ("We painted the wall with cracks."),
                       ("Mary gave the child a Band-Aid."), 
                       ("That Jill is never here hurts."),
                       ("The cotton clothing is made of grows in Mississippi.")]

 
# Here,tokenize each of the sentences 
result = []
for line in garden_path_Sentences:
    sent = nlp(line)
    token_result = []
    for token in sent:
        token_result.append(token)
    result.append(token_result)
print(result)



# spaCy has categorized these sentences and perform Entity recognition for them
paragraph = """The raft floated down the river sank.
We painted the wall with cracks. Mary gave the child a Band-Aid.
That Jill is never here hurts.The cotton clothing is made of grows in Mississippi."""
nlp_paragraph = nlp(paragraph)
print([(i, i.label_, i.label) for i in nlp_paragraph.ents])


import spacy

nlp = spacy.load("en_core_web_sm")
 
# Explanation for "ORG"
print(spacy.explain("ORG")) 

# Explanation for "GPE"
print(spacy.explain("GPE")) 



# What was the entity and its explanation that you looked up?
''' "Time flies like an arrow; fruit flies like a banana."

Explanation:. At first glance, the sentence seems to compare the 
speed of time flying with the way fruit flies (the insects) are attracted to 
a banana. 

'''

# Did the entity make sense in terms of the word associated with it?
''' However, upon closer analysis, it becomes clear that "flies" is used as a
verb in the first part of the sentence, while it functions as a noun in the
second part. The sentence intends to convey that time moves quickly, and fruit 
(specifically, flies) are attracted to bananas. 

'''

# What was the entity and its explanation that you looked up?
'''  "The old man the boats."

Explanation: At first glance, the sentence seems 
grammatically incorrect and confusing. However, upon closer analysis and 
re-parsing, the sentence can be understood as "The old [people] man the boats." 
In this interpretation, "man" functions as a verb meaning to operate or control,
and "the old" describes the people doing the action. Therefore, the sentence 
means that the elderly people are the ones operating the boats. 

'''

# Did the entity make sense in terms of the word associated with it?
'''The entity, "The old man the boats," does make sense in terms of the word 
associated with it, as it challenges the reader's initial assumption and 
requires re-parsing for a correct understanding.

'''
import markovify

# Get raw text as string.
with open("beowulf.txt", errors ="ignore") as b:
    text_a = b.read()

with open("grimms_fairy_tales.txt", errors="ignore") as g:
    text_b = g.read()

# Build the models
model_a = markovify.Text(text_a)
model_b = markovify.Text(text_b)

# Combine the models. The numbers indicate how much weight to give a particular model
model_combo = markovify.combine([ model_a, model_b ], [ .5, .5 ])

# Print five randomly-generated sentences
for i in range(10000):
    print(model_combo.make_sentence())

print ("\n")

# Print three randomly-generated sentences of no more than 280 characters
#for i in range():
    #print(model_combo.make_short_sentence(280))



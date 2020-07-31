from monkeylearn import MonkeyLearn

ml = MonkeyLearn('e3aeff8e27ceef5d1d60e142268d41c27a344aee')

data = ["Once up a time there were three lions. Daddy lion, Mummy lion and Baby lion. It was soon going to be Baby lion’s birthday he would be one year old."]

model_id = 'ex_YCya9nrn'

result = ml.extractors.extract(model_id, data)

# print(result.body[0])

for i in result.body[0]['extractions']:
    print(i)
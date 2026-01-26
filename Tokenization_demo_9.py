from my_function_2 import create_vocab,decode,encode

vocab = create_vocab()

text = "the British Indian Empire  was partitioned into two independent dominions"

my_ids_list = encode(text,vocab)

my_original_test = decode(my_ids_list,vocab)

# Print results
print(f"My Original text is ::: {text}")

print(f"My Token after encode function ::: {my_ids_list}")

print(f"My Original text after decode functions ::: {my_original_test}")


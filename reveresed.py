sentence= input("Enter a sentence:")
words = sentence.split()
reversed_words = words[: : -1]
print("revers sentence "+ " ".join(reversed_words) )
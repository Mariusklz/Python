text = input("Entrez une phrase: ")
text = ''.join(e for e in text if e.isalpha())
if text.lower() == text[::-1].lower():
  print("Cette phrase est un palindrome")
else:
  print("Cette phrase n'est pas un palindrome")

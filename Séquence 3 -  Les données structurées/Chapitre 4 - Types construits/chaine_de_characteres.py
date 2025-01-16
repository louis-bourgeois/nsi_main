# # Exercice 6 (BONUS)
# print("Exercice 6 (BONUS):")


# def est_palindrome(chaine):
#     chaine_nettoyee = ''.join(
#         caractere for caractere in chaine if caractere.isalnum()).lower()
#     return chaine_nettoyee == chaine_nettoyee[::-1]


# chaine6 = "s.o.s"
# if est_palindrome(chaine6):
#     print(f"La chaîne \"{chaine6}\" est un palindrome.")
# else:
#     print(f"La chaîne \"{chaine6}\" n'est pas un palindrome.")

# exemples_palindromes = ["radar", "kayak", "été", "A man a plan a canal Panama"]  # Mdrr

# for exemple in exemples_palindromes:
#     if est_palindrome(exemple):
#         print(f"La chaîne \"{exemple}\" est un palindrome.")
#     else:
#         print(f"La chaîne \"{exemple}\" n'est pas un palindrome.")


perso = {"nom": "Gandalf", "age" : 7000}
print(perso.age)
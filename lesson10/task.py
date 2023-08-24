# В единственной строке записан текст 
# Для каждого слова из данного текста подсчитайте 
# Сколько раз оно встречалось в этом тексте ранее 
# Словом считается последовательность непробельным символов идущих подряд 
# слова разделены одним или большим числом пробелов или символами конца строки 
 
string_text = input("Enter the string: ").split() 
count_word = { 
 
} 
  
for word in string_text: 
    count_word[word] = string_text.count(word) 
print(count_word) 
 
 
sin = { 
    "hello":"hi", 
    "goodbye":"bye" 
} 
  
 
input_word = "bye" 
 
for i in range(word): 
    first, second = input().split() 
    empty_value[first] = second 
    empty_value[second] = first 
print(empty_value[input()])
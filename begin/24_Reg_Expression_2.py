import re
input_filename = "dumpfile.txt"
result_filename = "result.txt"

inputfile = open(input_filename, mode='r', encoding='utf_8')
resultfile = open(result_filename, mode='w', encoding='utf_8')

mytext = inputfile.read()
# немоного офтопа https://regex101.com/ - сайт поможет с регулярками
#lookfor = r"[\w.-]+@[\w.-]+"

#lookfor = r"[\w.-]+@[A-Za-z-]+\.[\w.]+"

lookfor = r"[\w.-]+@(?!intel\.com)[A-Za-z-]+\.[\w.]+" # исключаем запись intel.com  (?!intel\.com)
lookfor2 = r"[A-Z][a-z]+\s[A-Z][a-z]+" # ищем Имена

results = re.findall(lookfor, mytext)   # что искать, где искать
results2 = re.findall(lookfor2, mytext)
#print(results)
#print(results2)

#for item in results:
#    print(item)
    #resultfile.write(item) запишит все в кучу
    #resultfile.write(item + "\n") # запишит покрасивеекрасиво

#uniq = [1,2,3,4,5]
#fifa = ['a','b','c','d','e']
#uniq_and_fifa = dict(zip(uniq, fifa))

totalresult =  dict(zip(results2, results))
#print(totalresult)

for item in totalresult:
    print(item + totalresult[item])
    resultfile.write(item + totalresult[item] + "\n")
print(f"Total: {str(len(results))}")

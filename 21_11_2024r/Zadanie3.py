napis = str("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin posuere sem eu elit mattis, nec nunc.")

n = 3
x = 0
def parzystyStr(x):
    even = []

    for i in range(len(x)):
        if i % 2 == 0:
            even.append(x[i])
    print(even)

parzystyStr(napis)

def last(napis,n):
    return napis[len(napis)-n:]

print(last(napis,n))

def reverse(napis,x):
    if x < len(napis):
        x += 1
        return napis[len(napis) -x]

print(reverse(napis,x))
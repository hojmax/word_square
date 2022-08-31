# Word Square

## 📝 Description
Below you can see the famous [Sator Square](https://en.wikipedia.org/wiki/Sator_Square) - a two-dimensional word square containing five Latin palindromes:
```
S A T O R
A R E P O
T E N E T
O P E R A
R O T A S
```

Opun first seing this, two questions immediately came to mind:

1. How large is the maximal size word square in the english language?

2. Can i efficiently compute all possible word squares?

These questions formed the basis of this quick project.

## 🔬 Results
It is important to note that all results are dependent on the dictionary used. I choose the largest possible dictionary i could find of 466K english words. If one were to use a larger dictionary, one may come to different conclusions.

It turns out that there exists no wordsquares of size greater than 6x6, and that there exists exactly 2 wordsquares of size 6x6. This is what i call the 'Kramer Square':
```
K R A M E R
R O M A N E
A M U N A M
M A N U M A
E N A M O R
R E M A R K
```
You can construct the other 6x6 word square by simply reversing the row order. The validity of some of the words used are debatable, but since it is the only possible 6x6 i favor leniency.

There are plenty of 5x5's, 56970 to be exact. A favorite of mine is this checkerboard-like square:
```
A B A K A
B A N A K
A N A N A
K A N A B
A K A B A
```
Word squares are, in my estimation, a bit cooler when you actually know the vocabulary. Here are the word squares using the most frequent words for sizes 5x5, 4x4, 3x3 and 2x2:
```
A S S E T
S T A T E
S A L A S
E T A T S
T E S S A

S T E P
T I D E
E D I T
P E T S

L E T
E Y E
T E L

O N
N O
```
And finally my all time favourite. A 4x4 word square, formed from 2x2 word squares:
```
E R   O S
R E   D O
    +    
O D   E R
S O   R E

    =

 E R O S
 R E D O
 O D E R
 S O R E
```
This type of 4x4 square is less rare than one might expect. I favor this specific configuration, since it is constructed from the most frequent 4 letter words.


## 🏗 Implementation
I will firstly 
```
      *
     / \
    a   b
   / \   \
  b   t   e
 / \  
e   s 
```

## 🏄‍♂️ Usage
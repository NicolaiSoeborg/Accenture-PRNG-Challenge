# Accenture (broken) RNG Challenge

Accenture had a nice challenge at the DSE fair at DTU 2017.

## The challenge

Playing cards are used as reels for the slot machine. Each slot machine reel can take 14 values (Accenture logo + the 13 normal cards). The Accenture logo maps to 1, while the ace maps to 14.

The next four random values (cards) are chosen as shown below.

![equation1](http://frog.isima.fr/cgi-bin/bruno/tex2png--10.cgi?z_n%20%3D%20n_%7Bn-1%7D%20%5Ccdot%20607%20%5C%25%20990881%2C%5C%20z_0%20%3D%20%5Bz_1%2C%20z_2%2C%20z_3%2C%20z_4%5D%5ET%0A)
<!--
  z_n = n_{n-1} \cdot 607 \% 990881,\ z_0 = [z_1, z_2, z_3, z_4]^T
-->

![equation2](http://frog.isima.fr/cgi-bin/bruno/tex2png--10.cgi?r%20%3D%20%5Cleft%28%20%5Cleft%28z_n%20-%20%5Cbegin%7Bbmatrix%7D1%5C%5C1%5C%5C1%5C%5C1%5Cend%7Bbmatrix%7D%5Cright%29%20%5Ccdot%20%20%5Cbegin%7Bbmatrix%7D977%5C%5C607%5C%5C1069%5C%5C547%5Cend%7Bbmatrix%7D%20%2B%20u%20%5Cright%29%20%5C%25%2014%20%2B%20%5Cbegin%7Bbmatrix%7D1%5C%5C1%5C%5C1%5C%5C1%5Cend%7Bbmatrix%7D)
<!--
  r = \left( \left(z_n - \begin{bmatrix}1\\1\\1\\1\end{bmatrix}\right) \cdot  \begin{bmatrix}977\\607\\1069\\547\end{bmatrix} + u \right) \% 14 + \begin{bmatrix}1\\1\\1\\1\end{bmatrix}
-->

Here `r = [r_1, r_2, r_3, r_4]` is the reel vector where `r_1` is the left most reel.  `z_0` is just a random vector.

The `*` is an element-by-element multiplication and `%` is the modulo operator. The vector `u` is generated by grouping the lower 16 bit of the number provided by the user (input field below the reels), into groups of 4 bits.

### Example

Let's assume the user has provided the number `12886`, which in hex decimal is `0x3256`; hence, the vector `u` is in the case given by `u = [3, 2, 5, 6]^T`.

Let assume `z_{n-1}` is `[5, 3, 8, 2]^T`, then `z_n` is defined as:

![equation3](http://frog.isima.fr/cgi-bin/bruno/tex2png--10.cgi?z_n%20%3D%20%5Cbegin%7Bbmatrix%7D5%5C%5C3%5C%5C8%5C%5C2%5Cend%7Bbmatrix%7D%20%5Ccdot%20607%20%5C%25%20990881%20%3D%20%5Cbegin%7Bbmatrix%7D3035%5C%5C1821%5C%5C4856%5C%5C1214%5Cend%7Bbmatrix%7D)
<!--
  z_n = \begin{bmatrix}5\\3\\8\\2\end{bmatrix} \cdot 607 \% 990881 = \begin{bmatrix}3035\\1821\\4856\\1214\end{bmatrix}
-->

Resulting in the following reel:

![equation4]((http://frog.isima.fr/cgi-bin/bruno/tex2png--10.cgi?r%20%3D%20%5Cleft%28%20%5Cleft%28%5Cbegin%7Bbmatrix%7D3035%5C%5C1821%5C%5C4856%5C%5C1214%5Cend%7Bbmatrix%7D%20-%20%5Cbegin%7Bbmatrix%7D1%5C%5C1%5C%5C1%5C%5C1%5Cend%7Bbmatrix%7D%5Cright%29%20%5Ccdot%20%5Cbegin%7Bbmatrix%7D977%5C%5C607%5C%5C1069%5C%5C547%5Cend%7Bbmatrix%7D%20%2B%20%5Cbegin%7Bbmatrix%7D3%5C%5C2%5C%5C5%5C%5C6%5Cend%7Bbmatrix%7D%5Cright%29%20%5C%25%2014%20%2B%20%5Cbegin%7Bbmatrix%7D1%5C%5C1%5C%5C1%5C%5C1%5Cend%7Bbmatrix%7D%20%3D%20%5Cbegin%7Bbmatrix%7D2%5C%5C3%5C%5C5%5C%5C2%5Cend%7Bbmatrix%7D)
<!--
  r = \left( \left(\begin{bmatrix}3035\\1821\\4856\\1214\end{bmatrix} - \begin{bmatrix}1\\1\\1\\1\end{bmatrix}\right) \cdot \begin{bmatrix}977\\607\\1069\\547\end{bmatrix} + \begin{bmatrix}3\\2\\5\\6\end{bmatrix}\right) \% 14 + \begin{bmatrix}1\\1\\1\\1\end{bmatrix} = \begin{bmatrix}2\\3\\5\\2\end{bmatrix}
-->

## Running the script

The script will create a random `z` (seed) and try to guess an input (`u`) that will produce the desired output (all cards `1`).

```
Spin 1 (u = [0, 0, 0, 0]).    Cards: [5|12|14|7]
Spin 2 (u = [6, 9, 13, 8]).   Cards: [5|5|11|14]
Spin 3 (u = [4, 7, 11, 5]).   Cards: [12|11|2|11]
Spin 4 (u = [0, 9, 1, 8]).    Cards: [4|6|14|3]
Spin 5 (u = [13, 1, 6, 7]).   Cards: [13|1|11|8]
Spin 6 (u = [1, 7, 2, 10]).   Cards: [12|6|1|5]
Spin 7 (u = [0, 6, 4, 10]).   Cards: [1|1|1|1]
Spin 8 (u = [4, 7, 11, 6]).   Cards: [1|1|1|1]
Spin 9 (u = [12, 1, 4, 9]).   Cards: [1|1|1|1]
Spin 10 (u = [5, 13, 0, 11]). Cards: [1|1|1|1]
```

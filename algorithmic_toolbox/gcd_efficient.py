# Key Lemma:
# Let a' be the remainder when a is divided by b, then:
# gcd(a,b) = gcd(a',b) = gcd(b, a')


def gcd_efficient(a, b):
    if b == 0:
        return a
    else:
        return gcd_efficient(b, a % b)


print(gcd_efficient(5, 15))

# main.py
from sum import add
from difference import subtract
from product import multiply
from division import divide

if __name__ == "__main__":
    a, b = 12, 4
    print("Sum:", add(a, b))
    print("Difference:", subtract(a, b))
    print("Product:", multiply(a, b))
    print("Division:", divide(a, b))

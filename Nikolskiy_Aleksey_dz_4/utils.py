import sys
import task4_2


command = sys.argv[1]
lst = task4_2.currency_rates(command)
print(f"на  {lst[0]} 1 {lst[1]} равен {lst[2]} рублей")

from random import randint

def find_missing_nums(nums):
  normal_spisok = [chislo for chislo in range(1, len(nums)+1)]
  pystoy_spisok_dla_chisel = []
  for founds in normal_spisok:
    if founds not in nums:
      pystoy_spisok_dla_chisel.append(founds)
  return pystoy_spisok_dla_chisel

vvodnoe_chislo = int(input())
nums = [randint(1, vvodnoe_chislo) for i in range(vvodnoe_chislo)]

print(find_missing_nums(nums))

water=int(input("Enter Amount : "))
final_amount=0
if water>1000 and water<20001:
    final_amount=final_amount+15
    remaning_water=water-1000
    result=remaning_water*0.0175
    final_amount=final_amount+result
elif water>2000 and water<30001:
    final_amount=final_amount+15
    final_amount=final_amount+17.5
    remaning_water=water-2000
    result=remaning_water*0.02
    final_amount=final_amount+result
else:
    final_amount=70
print(final_amount)
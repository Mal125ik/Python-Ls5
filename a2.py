ac=int(input("Enter actual cost of item:"))
sc=int(input("Enter selling cost of item:"))
if sc>ac:
    profit=sc-ac
    print('profit ts:',profit)

else:
    loss=ac-sc
    print('loss ts:',loss)
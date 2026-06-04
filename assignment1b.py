farmer_name=input("Enter farmer name: ")
morn_coll=float(input("Enter morning milk collection: "))
even_coll=float(input("Enter evening milk collection: "))
priceperl=float(input("Enter price per litre: "))

deliveries=[morn_coll,even_coll]

tot_coll=morn_coll+even_coll

tot_amount=priceperl*tot_coll

farmer={
  "name":farmer_name,
  "morning milk":morn_coll,
  "evening milk":even_coll,
  "total litres":tot_coll,
  "price per litre":priceperl,
  "amount payable":tot_amount
}

print(farmer)

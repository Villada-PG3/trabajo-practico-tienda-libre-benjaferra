
#1
Producto.objects.all()
<QuerySet [<Producto: gaseosa sabor cola-coca cola - $5000.00>, <Producto: gaseosa sabor cola-doble cola - $2500.00>, <Producto: gaseosa sabor limon-prity - $3000.00>, <Producto: gaseosa sabor limon-sprite - $3000.00>, <Producto: gaseosa sabor cola-pepsi - $2000.00>, <Producto: gaseosa sabor naranja-fanta - $2022.00>, <Producto: leche- serenisima - $3000.00>, <Producto: galletas pepitos - $2000.00>, <Producto: formis - $3000.00>, <Producto: tortitas black - $1500.00>, <Producto: don satur - $2000.00>, <Producto: television - $6700000.00>, <Producto: lavarropa - $1000000.00>, <Producto: microondas - $500000.00>, <Producto: iphone 17 pro max - $9999999.99>, <Producto: pack de cubiertos - $5000.00>, <Producto: sarten - $6700.00>, <Producto: mochila - $100000.00>, <Producto: termo stanley - $3000.00>, <Producto: reloj de pared - $20000.00>]>
#2
Producto.objects.filter(nombre__icontains='gaseosa')
<QuerySet [<Producto: gaseosa sabor cola-coca cola - $5000.00>, <Producto: gaseosa sabor cola-doble cola - $2500.00>, <Producto: gaseosa sabor limon-prity - $3000.00>, <Producto: gaseosa sabor limon-sprite - $3000.00>, <Producto: gaseosa sabor cola-pepsi - $2000.00>, <Producto: gaseosa sabor naranja-fanta - $2022.00>]>
#3
Producto.objects.filter(precio__gt=1000)
<QuerySet [<Producto: gaseosa sabor cola-coca cola - $5000.00>, <Producto: gaseosa sabor cola-doble cola - $2500.00>, <Producto: gaseosa sabor limon-prity - $3000.00>, <Producto: gaseosa sabor limon-sprite - $3000.00>, <Producto: gaseosa sabor cola-pepsi - $2000.00>, <Producto: gaseosa sabor naranja-fanta - $2022.00>, <Producto: leche- serenisima - $3000.00>, <Producto: galletas pepitos - $2000.00>, <Producto: formis - $3000.00>, <Producto: tortitas black - $1500.00>, <Producto: don satur - $2000.00>, <Producto: television - $6700000.00>, <Producto: lavarropa - $1000000.00>, <Producto: microondas - $500000.00>, <Producto: iphone 17 pro max - $9999999.99>, <Producto: pack de cubiertos - $5000.00>, <Producto: sarten - $6700.00>, <Producto: mochila - $100000.00>, <Producto: termo stanley - $3000.00>, <Producto: reloj de pared - $20000.00>]>
#4
Producto.objects.filter(precio__lte=2000, stock__gt=0)
<QuerySet [<Producto: gaseosa sabor cola-pepsi - $2000.00>, <Producto: galletas pepitos - $2000.00>, <Producto: tortitas black - $1500.00>, <Producto: don satur - $2000.00>]>
#5
Producto.objects.exclude(marca='Coca Cola')
<QuerySet [<Producto: gaseosa sabor cola-coca cola - $5000.00>, <Producto: gaseosa sabor cola-doble cola - $2500.00>, <Producto: gaseosa sabor limon-prity - $3000.00>, <Producto: gaseosa sabor limon-sprite - $3000.00>, <Producto: gaseosa sabor cola-pepsi - $2000.00>, <Producto: gaseosa sabor naranja-fanta - $2022.00>, <Producto: leche- serenisima - $3000.00>, <Producto: galletas pepitos - $2000.00>, <Producto: formis - $3000.00>, <Producto: tortitas black - $1500.00>, <Producto: don satur - $2000.00>, <Producto: television - $6700000.00>, <Producto: lavarropa - $1000000.00>, <Producto: microondas - $500000.00>, <Producto: iphone 17 pro max - $9999999.99>, <Producto: pack de cubiertos - $5000.00>, <Producto: sarten - $6700.00>, <Producto: mochila - $100000.00>, <Producto: termo stanley - $3000.00>, <Producto: reloj de pared - $20000.00>]>
#6
Producto.objects.order_by('-precio')
<QuerySet [<Producto: iphone 17 pro max - $9999999.99>, <Producto: television - $6700000.00>, <Producto: lavarropa - $1000000.00>, <Producto: microondas - $500000.00>, <Producto: mochila - $100000.00>, <Producto: reloj de pared - $20000.00>, <Producto: sarten - $6700.00>, <Producto: gaseosa sabor cola-coca cola - $5000.00>, <Producto: pack de cubiertos - $5000.00>, <Producto: gaseosa sabor limon-prity - $3000.00>, <Producto: gaseosa sabor limon-sprite - $3000.00>, <Producto: leche- serenisima - $3000.00>, <Producto: formis - $3000.00>, <Producto: termo stanley - $3000.00>, <Producto: gaseosa sabor cola-doble cola - $2500.00>, <Producto: gaseosa sabor naranja-fanta - $2022.00>, <Producto: gaseosa sabor cola-pepsi - $2000.00>, <Producto: galletas pepitos - $2000.00>, <Producto: don satur - $2000.00>, <Producto: tortitas black - $1500.00>]>
#7
 p = Producto.objects.first()
>>> p.categoria.nombre
'bebidas'
#8
 Producto.objects.filter(nombre__icontains='cola')
<QuerySet [<Producto: gaseosa sabor cola-coca cola - $5000.00>, <Producto: gaseosa sabor cola-doble cola - $2500.00>, <Producto: gaseosa sabor cola-pepsi - $2000.00>]>
#9
 Producto.objects.filter(precio__gt=5000)
<QuerySet [<Producto: television - $6700000.00>, <Producto: lavarropa - $1000000.00>, <Producto: microondas - $500000.00>, <Producto: iphone 17 pro max - $9999999.99>, <Producto: sarten - $6700.00>, <Producto: mochila - $100000.00>, <Producto: reloj de pared - $20000.00>]>
#10
Producto.objects.exclude(nombre__icontains='sabor')
<QuerySet [<Producto: leche- serenisima - $3000.00>, <Producto: galletas pepitos - $2000.00>, <Producto: formis - $3000.00>, <Producto: tortitas black - $1500.00>, <Producto: don satur - $2000.00>, <Producto: television - $6700000.00>, <Producto: lavarropa - $1000000.00>, <Producto: microondas - $500000.00>, <Producto: iphone 17 pro max - $9999999.99>, <Producto: pack de cubiertos - $5000.00>, <Producto: sarten - $6700.00>, <Producto: mochila - $100000.00>, <Producto: termo stanley - $3000.00>, <Producto: reloj de pared - $20000.00>]>
"""50-იდან 100-ის ჩათვლით არსებული ყველა რიცხვი დააჯამეთ for ციკლის გამოყენებით.
ეს ჯამი უნდა შეინახოს ცვლადში, ამიტომ ციკლის გარეთ შექმენით sum ცვლადი,
რომელსაც ციკლში მიემატება საიტერაციო ცვლადის მნიშვნელობა. საბოლოოდ დაპტინტეთ
sum ცვლადის მნიშვნელობა."""

sum = 0
for i in range (50,100 + 1):
    print(sum)
    sum = sum + i
    
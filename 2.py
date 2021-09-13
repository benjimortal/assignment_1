def toStr(n,base):
   convert_to_Str =  "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   if n < base:
      return convert_to_Str[n]
   else:
      return toStr(n//base,base) + convert_to_Str[n % base]

print(toStr(4545,16))





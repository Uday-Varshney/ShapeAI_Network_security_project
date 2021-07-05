import hashlib
st=input("Enterh the string to hash:")
hash=st.encode('utf-8')
result=hashlib.md5(hash)
print(result.digest())

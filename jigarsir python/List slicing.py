l = [1,2,3,'tops',1.1,2.2,True,'Python',10,20,1,2,False,'tech',100,1]

print(l[15:])
print(l[:1]) # we do not count end.. 1 lkhyu 6 matlab 1 count nahi thay..
print(l[12::5])
print(l[9:10:2]) #jumping na nakhyu hot to pan answer 20 j aave
print(l[::10])
print(l[1:15:-5]) #answer is zero
print(l[1::-5]) #answer is one.. It will print one as ending range is not mentioned eventhough jump is negative..
print(l[:15:-5]) #answer is zero

print(l[-1:])
print(l[:14]) # we do not count end.. 14 lkhyu 6 matlab 14 count nahi thay.. 0 thi 13 sudhi jase..
print(l[-5:-12])
print(l[-16:-1:7])
print(l[::-5])
print(l[-12:-2:-3]) #-12 + -3 = -15 which is not in range which we have specified so answer is blank
print(l[-16:-1:5])
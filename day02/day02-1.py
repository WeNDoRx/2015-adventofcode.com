# this was part of a small internal "golf" chalange so it may be harder to read
t = 0
with open("day02.input") as f:
 for i in f:
  d=map(int,sorted(i.rstrip('\n').split("x"),key=int))
  l,w,h=d[0],d[1],d[2]
  t+=2*h*l+2*h*w+3*l*w
print t
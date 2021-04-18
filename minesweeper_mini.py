# casio-minesweeper
# A simple minesweeper python script for CASIO calculator (9860G3)
# by @pdjdev (https://github.com/pdjdev/)
k='Replay? (Yes=+)> '
j='*'
d='+'
a='.'
Z=input
V=int
U=str
K=False
E=range
D=''
B=True
A=print
import random as S
F=21
G=5
W=B
def X():B='+-------------------+';A(B);A('| MINE SWEEPER      |');A('|       by @PDJDEV  |');A(B)
def b(mapdata):
	for C in mapdata:
		for B in C:
			if B==0:A(a,end=D)
			elif B==-1:A(j,end=D)
			else:A(U(B),end=D)
		A()
def e(mapdata,clickdata):
	I=clickdata;H=mapdata
	for B in E(G):
		for C in E(F):
			if I[B][C]==0:A('L',end=D)
			elif I[B][C]==-1:A('#',end=D)
			elif H[B][C]==-1:A(j,end=D)
			elif H[B][C]==0:A(a,end=D)
			else:A(U(H[B][C]),end=D)
		A()
def L(mapdata,y,x):
	A=mapdata
	if y>=0 and y<G and x>=0 and x<F:
		if A[y][x]!=-1:A[y][x]+=1
def M(clickdata,y,x):
	A=clickdata
	if y>=0 and y<G and x>=0 and x<F:
		if A[y][x]==1:return K
		A[y][x]=1;return B
def f(mapdata,clickdata,y,x):
	I=mapdata;A=clickdata
	if Q:
		if A[y][x]==-1:A[y][x]=0
		else:A[y][x]=-1
		return B
	if I[y][x]==-1:return K
	else:
		if A[y][x]==1:0
		elif A[y][x]==0:
			A[y][x]=1
			if I[y][x]==0:
				C=B
				while C:
					C=K
					for D in E(G):
						for H in E(F):
							if A[D][H]==1 and I[D][H]==0:
								if M(A,D-1,H-1):C=B
								if M(A,D-1,H):C=B
								if M(A,D-1,H+1):C=B
								if M(A,D,H-1):C=B
								if M(A,D,H+1):C=B
								if M(A,D+1,H-1):C=B
								if M(A,D+1,H):C=B
								if M(A,D+1,H+1):C=B
		return B
def g(mapdata,clickdata):
	for A in E(G):
		for C in E(F):
			if mapdata[A][C]!=-1:
				if clickdata[A][C]!=1:return K
	return B
def h(clickdata):
	A=0
	for B in E(G):
		for C in E(F):
			if clickdata[B][C]==-1:A+=1
	return A
while W:
	X();C=[];N=[];O=D;P=D;Q=K;A('Number of mines?(~99)\n');J=B
	while J:
		try:
			T=V(Z('> '))
			if T<1 or T>99:X();A('    Please enter\n   between 1 to 99');J=B;continue
			J=K
		except:X();A('    Please enter\n     valid value  ');J=B
	for c in E(G):
		R=[]
		for i in E(F):R.append(0)
		C.append(R)
	for c in E(G):
		R=[]
		for i in E(F):R.append(0)
		N.append(R)
	for c in E(T):
		H=S.randrange(0,F);I=S.randrange(0,G)
		while C[I][H]==-1:H=S.randrange(0,F);I=S.randrange(0,G)
		C[I][H]=-1
	for I in E(G):
		for H in E(F):
			if C[I][H]==-1:L(C,I-1,H-1);L(C,I-1,H);L(C,I-1,H+1);L(C,I,H-1);L(C,I,H+1);L(C,I+1,H-1);L(C,I+1,H);L(C,I+1,H+1)
	J=K
	while B:
		if not J:A('[W:'+U(F)+' H:'+U(G)+' MINE: '+U(T-h(N))+']====')
		e(C,N)
		if O==D or P==D:A('Enter (x.y)',end=D)
		else:A('Prev:'+O+a+P,end=D)
		if Q:A(' Flag',end=D)
		Y=Z(' > ')
		if d in Y:
			Q=not Q;J=B
			if Q:A('[Flag mode ON]=======')
			else:A('[Flag mode OFF]======')
			continue
		try:
			if Y==D:A('[Enter x.y location]=');J=B;continue
			O,P=Y.split(a)
			if V(O)>F or V(P)>G:A('[Out of range!]======');J=B;continue
			if not f(C,N,V(P)-1,V(O)-1):
				A('[GAME OVER]==========');b(C)
				if Z(k)!=d:W=K
				break
			if g(C,N):
				A('[GAME CLEAR]=========');b(C)
				if Z(k)!=d:W=K
				break
		except:A('[Try Again]==========');J=B;continue
		J=K
